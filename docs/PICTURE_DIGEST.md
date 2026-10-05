# Blindness as a picture: digest of the place-and-time candidates

Written 5 October 2026. This goes with `data/reference/picture_candidates.json`, which holds candidate items for the seven "Blindness as a picture" pages in `src/picture.py`: what Matthew Henry (volumes 1 to 6, the whole Bible) and Alfred Edersheim (*Life and Times*, *Sketches*), with the 1915 encyclopaedia, Easton and Smith's where they help, say about the passages, the places and customs behind them, and, above all, how they relate the figure to physical blindness. It is built by `src/build_picture_candidates.py`, which refuses to write a quote it cannot find in the shelf, and checked by `tests/test_picture_candidates.py`. The remarks table and the flagged list below come from `data/reference/picture_remarks.json`, written by the same script with the same check.

Every item has a short paragraph, a citation as a reader would see it, verbatim quotes with file and character offset (line endings as LF), a confidence of `high` or `medium`, and a `caution`. The test checks that each quote is really in its file at its offset. It does not check that the paragraph is a fair reading of the quote, and nothing here has been seen by Brian or a second reader. Read the `caution` lines before using an item. Nothing in the JSON was filled from memory. Where something is known only from general knowledge it is said so here and marked unverified; the JSON leaves it out.

Counts: 48 items across 7 keys. Per key: `blind-guides` 8, `eyes-that-cannot-see` 8, `gods-people-called-blind` 7, `like-the-blind` 5, `eyes-dim-with-grief` 6, `bribes-and-curses` 6, `eyes-opened` 8.

## How to read the locators

Henry's text is arranged by passage: the verses are printed in a block and the exposition follows. Locators in the JSON give the passage Henry is expounding (for example "Matthew 23:16-22") and every quote has an offset, so a writer can open the file and search. Edersheim's locators give the Book and chapter, because his chapters are named for the Gospel passages. The 1915 encyclopaedia text is OCR and keeps the scan's misreadings and line-end hyphens ("physi cal"); quotes from it keep them. Easton and Smith's are cited by headword.

## What was searched, and what the shelf does not say

- Henry has something on every passage on the seven pages, because volumes 2, 3, 4 and 6 are now on the shelf. The Isaiah, Lamentations, Zephaniah and Zechariah passages are in volume 4; the psalms and Job in volume 3; Deuteronomy and Exodus in volume 1; Matthew, Luke and John in volume 5; Romans to Revelation in volume 6.
- Edersheim comments on: the Matthew 23 woes and their setting (Book V ch. iv); the hand-washing and "blind leaders" of Matthew 15 (Book III ch. xxxi); John 9:39-41 (Book IV ch. ix); John 12:37-41 (Book V ch. iii); Luke 4:16-21 (Book III ch. xi); the Rabbinic reading of Isaiah 35:5-6 and Psalm 146:8 (Appendix IX). I found no comment by him on Isaiah 29, 42, 43, 56 or 59, Lamentations, Zephaniah, Zechariah, Deuteronomy 28, 2 Corinthians 4, 2 Peter, 1 John or Revelation 3 that bears on blindness (his one Romans 11 remark, on 'blindness in part', is flagged below) (a search of both books for Laodicea finds only sandals from Laodicea in *Sketches*). So for those the shelf has Henry and the dictionaries only.
- The 1915 encyclopaedia, Easton and Smith's add: the Laodicean eye-powder and school of medicine (ISBE only); the filtering of wine behind the gnat (Easton only); who a watchman was (ISBE); bribery and "Blindness, Judicial" (ISBE); the physical and figurative eye (ISBE).
- Not on the shelf: any first-century description of the Temple-gold oath (Henry and Edersheim give the rule as a statement, and Edersheim says the allusion is uncertain); anything on how a Pharisee strained his wine beyond Easton's two sentences; any account of the Laodicean eye-salve beyond the encyclopaedia's, which cites Ramsay (not on the shelf); anything about how blind people lived in the streets of Jerusalem beyond Edersheim's notes on begging and the encyclopaedia's remark that blindness was no less common.

## `blind-guides` (8 items)

Coverage: Matthew 15:12-14, 23:13-28 (oaths, gnat, cup, setting), Luke 6:39, Isaiah 56:9-11 (watchmen), Romans 2:17-21; strong on all five passages.

Digest. Henry's reading of "blind leaders of the blind" is ignorance joined to pride: they "think they see better and further than any" and lead anyway (`blind-guides[0]`). Edersheim sums up the Matthew 15 warning as "the leadership of the blind by the blind" ending in ruin for both. On the Temple gold: Henry gives the rule (an oath by the temple does not bind, an oath by its gold does) and says the point was to make people bring gold to the treasury; Edersheim says the fourth woe is aimed at the guides' "moral blindness" and that the precise allusion is not easy to understand (`blind-guides[1]`). The gnat and camel is explained by Easton as filtering wine for fear of an unclean insect (Lev. 11:23) while neglecting weightier matters; Edersheim adds the tithing of anise and the like (`blind-guides[3]`). The hand-washing is called by Edersheim a "tradition of the elders", not a law of Moses, first meant to keep sacred offerings clean (`blind-guides[4]`). The woes belong to the third day of Passion Week, "the last day in the Temple", eight woes for eight beatitudes in both Henry and Edersheim (`blind-guides[5]`). The watchmen are sentinels on the city walls (ISBE) who should have given warning; Henry offers three referents (false prophets, wicked princes, the chief priests and scribes) (`blind-guides[6]`). On the assumption: Henry reads blind Ahijah as seeing visions that "need not bodily eyes" (`blind-guides[7]`).

Item index:

- `blind-guides[0]` (high): Henry on Matthew 15:14: the Pharisees are 'blind leaders of the blind' because they are ignorant of the spiritual meaning of the law and proud enou.... Locators: Henry vol. 5 @1289494; Henry vol. 5 @1289910; Henry vol. 5 @3783149; Edersheim, Life and Times @2176568.
- `blind-guides[1]` (medium): What the oath about the Temple gold was (Matthew 23:16-22). Locators: Henry vol. 5 @1995715; Henry vol. 5 @1996443; Edersheim, Life and Times @3302983.
- `blind-guides[2]` (high): Henry on Romans 2:19: Paul's 'guide of the blind' is a boast the Jews of his day made of themselves, as teachers of the Gentiles who 'sat in darkne.... Locators: Henry vol. 6 @2236656.
- `blind-guides[3]` (high): The 'gnat and camel' (Matthew 23:24). Locators: Easton @486895; Easton @1214080; ISBE vol. 2 @4888660; Edersheim, Life and Times @3303953; Henry vol. 5 @2006240.
- `blind-guides[4]` (high): The hand-washing that set off Matthew 15 (Henry and Edersheim agree on the facts). Locators: Henry vol. 5 @1261437; Edersheim, Life and Times @2142771; Edersheim, Life and Times @2143777; Edersheim, Life and Times @2144604.
- `blind-guides[5]` (high): The setting of the woes (Matthew 23). Locators: Edersheim, Life and Times @3261261; Edersheim, Life and Times @3261726; Edersheim, Life and Times @3299603; Henry vol. 5 @1979447; Edersheim, Life and Times @3316078.
- `blind-guides[6]` (high): Who the 'watchmen' were (Isaiah 56:10, 'His watchmen are blind'). Locators: Henry vol. 4 @1931199; Henry vol. 4 @1932273; Henry vol. 4 @1933137; ISBE vol. 5 @2174649.
- `blind-guides[7]` (high): Henry on blind Ahijah and what the figure takes for granted. Locators: Henry vol. 2 @3687763; ISBE vol. 1 @3978973.

## `eyes-that-cannot-see` (8 items)

Coverage: John 9:39-41 and 12:37-41 (Henry and Edersheim), Romans 11:7-10, 2 Corinthians 4:3-6, 2 Peter 1:5-9, 1 John 2:9-11 (Henry), with ISBE on the usage of "blind".

Digest. Henry says John 9:39 is "a metaphor borrowed from the miracle" and reads the saying about nations and persons both (`eyes-that-cannot-see[0]`); on verse 41 he says invincible ignorance "excuses" and lessens guilt, and that the danger is in those who "fancy they do see" (`[1]`). Edersheim's verdict, the plainest on the shelf: "It was not the calamity of blindness; but it was a blindness in which they were guilty... the result of their deliberate choice", set at the Temple entrance where the blind sat and "the blind were regarded as specially entitled to charity" (`[2]`). John 12:40 is handled by both as a hard saying: Henry says "could not" means "would not" and also allows a "righteous hand of God"; Edersheim says "they did not believe, because they could not believe", then, in a note, that this is "not decreed beforehand, and irrespective of their conduct" (`[3]`). Romans 11, 2 Corinthians 4 and 1 John 2 are read as hardening, the devil's darkening of the understanding, and darkened conscience (`[4]`, `[5]`); 2 Peter 1:9 Henry glosses as "blind, that is, as to spiritual and heavenly things" and ISBE notes the verb is "usually" the spiritual sense (`[6]`). The contrast that matters for "who": Henry on Matthew 9:27 says those "deprived of bodily sight" may see with "the eyes of their understanding" what the leaders cannot (`[7]`).

Item index:

- `eyes-that-cannot-see[0]` (high): Henry on John 9:39: the verse 'explains' a 'great truth by a metaphor borrowed from the miracle' just wrought. Locators: Henry vol. 5 @5997480; Henry vol. 5 @5998244; Henry vol. 5 @5998684; Henry vol. 5 @5997861.
- `eyes-that-cannot-see[1]` (high): Henry on John 9:41, 'If you were blind, you would have no sin'. Locators: Henry vol. 5 @6002067; Henry vol. 5 @6002664; Henry vol. 5 @6003166.
- `eyes-that-cannot-see[2]` (high): Edersheim on John 9:39-41 and the place of the miracle. Locators: Edersheim, Life and Times @2636426; Edersheim, Life and Times @2637150; Edersheim, Life and Times @2636860; Edersheim, Life and Times @2637419; Edersheim, Life and Times @2662671; Edersheim, Life and Times @2661799.
- `eyes-that-cannot-see[3]` (medium): John 12:37-41, 'they could not believe', on Isaiah's blinded eyes. Locators: Henry vol. 5 @6336476; Henry vol. 5 @6337125; Edersheim, Life and Times @3249601; Edersheim, Life and Times @3260655; Edersheim, Life and Times @4049358.
- `eyes-that-cannot-see[4]` (medium): Henry on Romans 11:7-10, 'the rest were blinded'. Locators: Henry vol. 6 @2637060; Henry vol. 6 @2635729; Henry vol. 6 @2636100; Henry vol. 6 @2636192.
- `eyes-that-cannot-see[5]` (high): Henry on 2 Corinthians 4:4 and 1 John 2:9-11. Locators: Henry vol. 6 @3623597; Henry vol. 6 @3624066; Henry vol. 6 @6260781.
- `eyes-that-cannot-see[6]` (high): Henry on 2 Peter 1:9, 'he that lacketh these things is blind': he says 'blind, that is, as to spiritual and heavenly things, as the next words expl.... Locators: Henry vol. 6 @6099531; Henry vol. 6 @6099640; ISBE vol. 1 @3976036.
- `eyes-that-cannot-see[7]` (high): The contrast that matters for who is called blind. Locators: Henry vol. 5 @770192; Henry vol. 5 @5992314; Henry vol. 5 @5992571.

## `gods-people-called-blind` (7 items)

Coverage: Isaiah 29:9-14, 42:16-20, 43:8-10 and Revelation 3:14-18; Henry on all four, the encyclopaedia on Laodicea.

Digest. Henry on Isaiah 29: the guides "were themselves blindfolded" and "when the blind lead the blind" (`gods-people-called-blind[0]`); the "sealed book" is a vision they have but cannot read (`[1]`), and in Luke 4 he says the Old Testament was "in a manner shut up till Christ opened them". On Isaiah 42:19 Henry has God's servants as the blind, and he suggests verse 18 is addressed to idolaters (`[2]`); on 43:8, "blind people that have eyes" are idolaters, after Psalm 115 (`[3]`). On Laodicea Henry says they "could not see their state, nor their way, nor their danger", and "the sight of the body will not enlighten the soul" (`[4]`). The encyclopaedia says Laodicea made a Phrygian eye-powder and had a renowned school of medicine in the vicinity, and that the city refused Rome's aid after the earthquake of A.D. 60 (`[5]`); Henry's remedy is to give up "their own wisdom and reason" (`[6]`).

Item index:

- `gods-people-called-blind[0]` (high): Henry on Isaiah 29:9-10, 'blind', 'drunken, but not with wine', 'a spirit of deep sleep'. Locators: Henry vol. 4 @972123; Henry vol. 4 @971389; Henry vol. 4 @972293.
- `gods-people-called-blind[1]` (high): Isaiah's sealed scroll (29:11-12). Locators: Henry vol. 4 @973114; Henry vol. 4 @973324; Henry vol. 4 @973760; Henry vol. 5 @3662077.
- `gods-people-called-blind[2]` (high): Henry on Isaiah 42:18-20, 'Who is blind but my servant?'. Locators: Henry vol. 4 @1385910; Henry vol. 4 @1385758; Henry vol. 4 @1387658.
- `gods-people-called-blind[3]` (high): Henry on Isaiah 43:8, 'Bring forth the blind people that have eyes': he reads it as a reference to Psalm 115:8, 'the prophet seems here to refer wh.... Locators: Henry vol. 4 @1406087.
- `gods-people-called-blind[4]` (high): Henry on Revelation 3:17, Laodicea 'blind': 'they could not see their state, nor their way, nor their danger', and 'they thought they saw'. Locators: Henry vol. 6 @6654319; Henry vol. 6 @6655596; Henry vol. 6 @6654618.
- `gods-people-called-blind[5]` (medium): The Laodicea behind the 'eye-salve' (Revelation 3:18). Locators: ISBE vol. 3 @3986819; ISBE vol. 3 @3986889; ISBE vol. 3 @3986939; ISBE vol. 3 @3987034; ISBE vol. 3 @3987225; ISBE vol. 2 @3436293; ISBE vol. 2 @3436485; Henry vol. 6 @6648997.
- `gods-people-called-blind[6]` (high): Henry on the counsel of Revelation 3:18: 'they were blind; and he counsels them to buy of him eye-salve, that they might see, to give up their own .... Locators: Henry vol. 6 @6281305; Henry vol. 6 @6657972.

## `like-the-blind` (5 items)

Coverage: Deuteronomy 28:28-29, Isaiah 59:9-10, Lamentations 4:13-15, Zephaniah 1:17 (Henry); ISBE and Easton for how common blindness was and the law.

Digest. In all four Henry reads the blindness as a judgment on understanding or a figure of helplessness: "wilfully blind to their duty... made blind to their interest" (`like-the-blind[0]`), "we see no way open for our relief" (`[1]`), "blind to every thing that is good, but to do evil they were quick-sighted" (`[2]`), "their hearts and hands shall fail them" (`[3]`). The one line where Henry states what he takes a blind man's walking to be (Zephaniah 1:17) is flagged below and not used. The reference works say blindness was "no less rife" in antiquity and that the law named care for the blind (`[4]`).

Item index:

- `like-the-blind[0]` (high): Henry on Deuteronomy 28:28-29, 'the Lord shall smite thee with madness and blindness. Locators: Henry vol. 1 @4781307; Henry vol. 1 @4781851.
- `like-the-blind[1]` (high): Henry on Isaiah 59:10, 'We grope for the wall like the blind': it is the people's own confession to God, and he glosses 'we see no way open for our.... Locators: Henry vol. 4 @2048395; Henry vol. 4 @2048538; Henry vol. 4 @2048781.
- `like-the-blind[2]` (high): Henry on Lamentations 4:13-15, 'They have wandered as blind men in the streets': the prophets and priests are the ones who 'wandered as blind men',.... Locators: Henry vol. 4 @4310950; Henry vol. 4 @4311460.
- `like-the-blind[3]` (medium): Henry on Zephaniah 1:17, 'they shall walk like blind men': he reads the verse as the day of the Lord's distress, in which 'their hearts and hands s.... Locators: Henry vol. 4 @7991711; Henry vol. 4 @7992114.
- `like-the-blind[4]` (medium): Blind people in the streets, and the law's protection of them, from the reference works. Locators: ISBE vol. 1 @3976345; ISBE vol. 1 @3980593; Easton @420153.

## `eyes-dim-with-grief` (6 items)

Coverage: all five laments (Job 17:7; Psalms 6, 38, 88; Lamentations 5:17), Henry on each, ISBE's "Eye" entry for the pattern.

Digest. Henry takes all five as physical: Job "wept so much that he had almost lost his sight", David "wept till he had almost wept his eyes out", the light of David's eyes "gone... with much weeping or by a defluxion of rheum... or... fainting", the mourning eye of Psalm 88 weeping while praying, and the people's dim sight in Lamentations "as is usual in a deliquium, or fainting fit". ISBE lists them together: "Eyes may grow dim with sorrow and tears". Neither Henry nor the encyclopaedia calls these blindness. Edersheim has nothing on them.

Item index:

- `eyes-dim-with-grief[0]` (high): Henry on Job 17:7, 'My eye also is dim by reason of sorrow': 'He wept so much that he had almost lost his sight'. Locators: Henry vol. 3 @598224.
- `eyes-dim-with-grief[1]` (high): Henry on Psalm 6:6-7, 'Mine eye is consumed because of grief': 'wept till he had almost wept his eyes out'; he says 'this not only kept his eyes wa.... Locators: Henry vol. 3 @1563939; Henry vol. 3 @1564397; Henry vol. 3 @1565058; Henry vol. 3 @1565100.
- `eyes-dim-with-grief[2]` (high): Henry on Psalm 38:10, 'the light of mine eyes, it also is gone from me': he offers three causes for the lost light: 'either with much weeping or by.... Locators: Henry vol. 3 @2286748.
- `eyes-dim-with-grief[3]` (high): Henry on Psalm 88:9, 'Mine eye mourneth by reason of affliction': 'Sometimes giving vent to grief by weeping gives some ease to a troubled spirit. Locators: Henry vol. 3 @3446421.
- `eyes-dim-with-grief[4]` (high): Henry on Lamentations 5:17, 'for these things our eyes are dim': 'our heart is faint. Locators: Henry vol. 4 @4341699; Henry vol. 4 @4341930.
- `eyes-dim-with-grief[5]` (high): The 1915 encyclopaedia's entry 'Eye' gathers the pattern: 'Eyes may grow dim with sorrow and tears (Job 17 7), they may "waste away with griefs" (P.... Locators: ISBE vol. 2 @3431490; ISBE vol. 2 @3432801.

## `bribes-and-curses` (6 items)

Coverage: Exodus 23:6-8, Deuteronomy 16:18-20, Zechariah 11:15-17 and 12:4; Henry on all, ISBE and Easton on bribery.

Digest. Henry on Exodus 23:8: a gift "has a strange tendency to blind those that otherwise would do well" (`bribes-and-curses[0]`); on Deuteronomy 16 he says courts sat "in the gates" and gives the three tiers of judges (`[1]`, medium confidence: he gives no source). ISBE: "the OT abounds with allusions to the corruption and venality of the magisterial bench", and a bribe "blindeth the eyes of the open- eyed" (`[2]`); Easton gives the Hebrew literally. On Zechariah 11:17 Henry reads the darkened right eye as losing sight of danger and calls it "fulfilled when Christ said to the Pharisees... those who see may be made blind" (`[3]`); ISBE says putting out the right eye "robbed the victim of his beauty, and made him unfit to take his part in war" (`[4]`). On 12:4, "blinding the horses will be as bad as houghing them" (`[5]`).

Item index:

- `bribes-and-curses[0]` (high): Henry on Exodus 23:8, 'the gift blindeth the wise': the judge 'must not so much as take a gift, lest it should have a bad influence upon them, and .... Locators: Henry vol. 1 @2160989.
- `bribes-and-curses[1]` (medium): Where the judges sat, and how many (Deuteronomy 16:18-20). Locators: Henry vol. 1 @4502266; Henry vol. 1 @4502892; Henry vol. 1 @4503593.
- `bribes-and-curses[2]` (high): How common bribery was, and what it meant for the blind picture. Locators: ISBE vol. 1 @3982519; Easton @445020; ISBE vol. 1 @4242550.
- `bribes-and-curses[3]` (high): Henry on Zechariah 11:17, the idol shepherd whose right eye is 'utterly darkened': he reads the darkened eye as losing sight of danger ('he shall n.... Locators: Henry vol. 4 @8465080; Henry vol. 4 @8465225; Henry vol. 4 @8465589.
- `bribes-and-curses[4]` (high): The 1915 encyclopaedia on blinding as a punishment ('Eye'): 'A cruel custom therefore sanctioned among heathen nations the putting out of the eyes .... Locators: ISBE vol. 2 @3431225; ISBE vol. 2 @3430879.
- `bribes-and-curses[5]` (high): Henry on Zechariah 12:4, 'I will smite every horse of the people with blindness': 'so that they shall be no way serviceable to them; blinding the h.... Locators: Henry vol. 4 @8478552.

## `eyes-opened` (8 items)

Coverage: Psalm 146:8, Isaiah 29:18, 35:5, 42:7 and 42:16, Luke 4:16-21. Henry on all; Edersheim on Luke 4 and on the Rabbinic use of Isaiah 35:5 and Psalm 146:8.

Digest. Does Henry read these physically, spiritually or both? Psalm 146:8: both, and physical first ("He gives sight to those that have been long deprived of it... special reference to Christ... one that was born blind... spiritual illumination") (`eyes-opened[0]`). Isaiah 35:5: both, "wonders... on men's bodies" then "greater wonders... on men's souls" (`[2]`). Isaiah 29:18: spiritual only, ignorance to understanding (`[3]`). Isaiah 42:7: spiritual, "present the object... prepared the organ" (`[4]`). Isaiah 42:16: spiritual ("by nature blind"), and not physical guidance (`[5]`). Luke 4:18: spiritual, with eye-salve; Samson and Zedekiah as pictures of bondage (`[6]`). Edersheim: Isaiah 35:5-6 was "repeatedly applied to Messianic times" in the Rabbinic collections, including the Midrash on Psalm 146:8, and Jesus pointed John to it (`[1]`); at Nazareth Jesus read the Haphtarah from the Isaiah scroll, "much more than" the passage "within range of His eyes", and Edersheim's summary is "the healing which He offers to those whom sin had blinded" (`[7]`). Henry does not read Isaiah 42:16 ("I will lead the blind by a way they did not know") as a promise to people who are physically blind, and Edersheim is silent on it; that reading is the page's own, and should be marked so.

Item index:

- `eyes-opened[0]` (high): Henry on Psalm 146:8, 'The Lord openeth the eyes of the blind': he reads it both ways at once. Locators: Henry vol. 3 @4696201; Henry vol. 3 @4696480; Henry vol. 3 @4692850.
- `eyes-opened[1]` (medium): Edersheim on how Isaiah 35:5-6 was read before and in Jesus's day. Locators: Edersheim, Life and Times @4285413; Edersheim, Life and Times @1113089.
- `eyes-opened[2]` (high): Henry on Isaiah 35:5-6: 'Wonders shall be wrought on men's bodies (v. Locators: Henry vol. 4 @1175369; Henry vol. 4 @1176111; Henry vol. 4 @1176501.
- `eyes-opened[3]` (high): Henry on Isaiah 29:18, 'the eyes of the blind shall see out of obscurity': he reads it as ignorance giving way to understanding: 'Those that were i.... Locators: Henry vol. 4 @985430; Henry vol. 4 @985488; Henry vol. 4 @985930.
- `eyes-opened[4]` (high): Henry on Isaiah 42:7, 'To open the blind eyes': Christ is 'given for a light to the Gentiles', not only to reveal what they needed to know 'but to .... Locators: Henry vol. 4 @1368666; Henry vol. 4 @1368874; Henry vol. 4 @1369090; Henry vol. 4 @1368552.
- `eyes-opened[5]` (high): Henry on Isaiah 42:16, 'I will bring the blind by a way that they knew not': he writes 'Those who by nature were blind, and those who, being under .... Locators: Henry vol. 4 @1380156; Henry vol. 4 @1380526; Henry vol. 4 @1380759; Henry vol. 4 @1381021.
- `eyes-opened[6]` (high): Henry on Luke 4:18, 'recovering of sight to the blind', preached at Nazareth: he says Christ came 'by the power of his grace to give sight to them .... Locators: Henry vol. 5 @3665151; Henry vol. 5 @3665359; Henry vol. 5 @3660803.
- `eyes-opened[7]` (medium): Edersheim on the Nazareth synagogue (Luke 4:16-21). Locators: Edersheim, Life and Times @1420777; Edersheim, Life and Times @1421701; Edersheim, Life and Times @1425152.

## Every place the commentators remark on physical versus figurative blindness

These are the remarks, with offsets, found by searching Henry, Edersheim, the 1915 encyclopaedia, Easton and Smith's for "bodily", "spiritual", "eyes of the mind", "natural" and the like next to "blind" or "sight", and by reading each passage. They are the heart of Brian's question, what the picture assumes about the blind. Some are also used as evidence in the items above; all are checked against the shelf.

| Commentator | Place | What he says | Locator |
|---|---|---|---|
| Henry | Matthew 9:27 (the two blind men) | the physically blind can see what the leaders cannot: "They who, by the providence of God, are deprived of bodily sight, may yet, by the grace of God, have the eyes of their understanding so enlightened" | Henry vol. 5 @770270 |
| Henry | Matthew 9:27-31 (the cure) | the blind men's request as a model for the spiritual one: "Lord, that the eyes of our mind may be opened! Many are spiritually blind, and yet say they see, John ix. 41." | Henry vol. 5 @1748151 |
| Henry | Luke 18:35-43 (Bartimaeus, near Jericho) | the bodily healings are a 'token' of giving sight to 'blind souls': "As a token of this, he cured many of their bodily blindness" | Henry vol. 5 @4573292 |
| Henry | John 9:35-38 (the healed man) | physical sight valued for what it does for faith: "Note, The Greatest comfort of bodily eyesight is its serviceableness to our faith and the interests of our souls." | Henry vol. 5 @5992314 |
| Henry | John 9:39 ('those who see might be made blind') | he says the verse is a metaphor taken from the healing: "This great truth he explains by a metaphor borrowed from the miracle which he had lately wrought." | Henry vol. 5 @5997480 |
| Henry | Isaiah 35:5 | physical first, then 'greater wonders... on men's souls': "Wonders shall be wrought on men's bodies (v. 5, 6): The eyes of the blind shall be opened" | Henry vol. 4 @1175369 |
| Henry | Psalm 146:8 | reads the verse as both: "But this has special reference to Christ; for since the world began was it not heard that any man opened the eyes of one that was born blind till Christ did it (John ix. 32) and thereby encouraged us to hope in him for spiritual illumination." | Henry vol. 3 @4696480 |
| Henry | Isaiah 29:18 | reads the verse as ignorance becoming understanding only: "Those that were ignorant shall become intelligent, v. 18." | Henry vol. 4 @985430 |
| Henry | Isaiah 42:7 | the opened eye is a picture of an enlightened heart: "By his Spirit in the word he presents the object; by his Spirit in the heart he prepared the organ." | Henry vol. 4 @1368874 |
| Henry | Isaiah 42:16 | 'blind by nature' = spiritually blind: "Those who by nature were blind, and those who, being under convictions of sin and wrath are quite at a loss and know not what to do with themselves" | Henry vol. 4 @1380156 |
| Henry | Isaiah 42:18-19 | the blind in verse 18 may be idolaters (cf. Ps. 115:8): "The verse before may be understood as spoken to the Gentile idolaters, whom he calls deaf and blind, because they worshipped gods that were so." | Henry vol. 4 @1385910 |
| Henry | Isaiah 43:8 | 'blind people that have eyes': eyes that work and do not see: "to which the prophet seems here to refer when he calls idolaters blind people that have eyes, and deaf people that have ears." | Henry vol. 4 @1406087 |
| Henry | Luke 4:18 | the promise applied to souls, with two physically blinded men as examples: "but by the power of his grace to give sight to them that were blind; not only the Gentile world, but every unregenerate soul, that is not only in bondage, but in blindness, like Samson and Zedekiah." | Henry vol. 5 @3665151 |
| Henry | Romans 11:8 | eyes that work but do not see: "They had the faculties, but in the things that belonged to their peace they had not the use of those faculties" | Henry vol. 6 @2637060 |
| Henry | 2 Peter 1:9 | he says outright that 'blind' here is spiritual: "blind, that is, as to spiritual and heavenly things, as the next words explain it: He cannot see far off." | Henry vol. 6 @6099531 |
| Henry | Revelation 3:17 | bodily sight is no help to the soul: "The riches of the body will not enrich the soul; the sight of the body will not enlighten the soul" | Henry vol. 6 @6655596 |
| Henry | Ecclesiastes 7:11 | the eye of the understanding is better than bodily sight: "The clearness of the eye of the understanding is of greater use to us than bodily eye-sight." | Henry vol. 3 @6109009 |
| Henry | Acts 9:8-9 (Paul) | a bodily blindness sent to teach him of the other kind: "Now Paul was thus struck with bodily blindness to make him sensible of his spiritual blindness" | Henry vol. 6 @1710227 |
| Henry | 1 Kings 14:4 (Ahijah) | a blind prophet sees better for it: "blind through age, yet still blest with the visions of the Almighty, which need not bodily eyes, but are rather favoured by the want of them" | Henry vol. 2 @3687763 |
| Edersheim | John 9:41 | physical blindness is a calamity; the Pharisees' kind is guilt: "It was not the calamity of blindness; but it was a blindness in which they were guilty" | Edersheim, Life and Times @2662671 |
| Edersheim | John 9:2-3 (why was he born blind) | he separates the natural cause of blindness from the moral one: "There is a physical, natural reason for them." | Edersheim, Life and Times @2640441 |
| Edersheim | Matthew 9:27-31 (the two blind men) | he uses 'the blindness of the Gentile world' as a figure beside the physical healing: "Yet the leprosy of Israel and the blindness of the Gentile world are equally removed by the touch of His Hand at the cry of faith." | Edersheim, Life and Times @2261600 |
| Edersheim | Mark 8:22-26 (Bethsaida) | he draws a spiritual lesson from the physical healing's two stages: "Lastly, the confusedness of his sight, when first restored to him, surely conveyed, not only to him but to us all, both a spiritual lesson and a spiritual warning." | Edersheim, Life and Times @2256740 |
| Edersheim | Luke 4:18 | summarises the Nazareth text as healing of sin-blindness: "the healing which He offers to those whom sin had blinded" | Edersheim, Life and Times @1425152 |
| ISBE 1915 | 'Blindness' | the verb is mostly spiritual; physical blindness is noun and adjective: "The word blind is used as a vb., as Jn 12 40, usually in the sense of ob scuring spiritual perception." | ISBE vol. 1 @3976036 |
| ISBE 1915 | 'Blindness' (end) | lists the figure's meanings and cites exactly the picture pages' texts: "Figuratively, blindness is used to represent want of mental perception, want of prevision, reckless ness, and incapacity to perceive moral distinctions (Isa 42 16.18.19; Mt 23 16 ff; Jn 9 39 ff)." | ISBE vol. 1 @3980755 |
| ISBE 1915 | 'Blindness': the 'scales' of Paul | the 'scales' are a figure inside a physical healing: "The "scales" mentioned were not material but in the restoration of his sight it seemed as if scales had fallen from his eyes." | ISBE vol. 1 @3979475 |
| ISBE 1915 | 'Eye' (2) | names the figurative eye as its own category: "Figurative : The eye of the heart or mind, the organ of spiritual perception, which may be en- lightened or opened (Ps 119 IS)." | ISBE vol. 2 @3432801 |
| ISBE 1915 | 'Eyesalve' | the medical detail serves a figurative reference: "but the figurative reference is to the restoring of spiritual vision." | ISBE vol. 2 @3436485 |
| Easton | 'Blind' | a reference-work statement of the figure: "Blindness denotes ignorance as to spiritual things (Isa. 6:10; 42:18, 19; Matt. 15:14; Eph. 4:18)." | Easton @420499 |
| Easton | 'Blind' | treats the opening promise as a Messianic sign: "The opening of the eyes of the blind is peculiar to the Messiah (Isa. 29:18)." | Easton @420608 |
| Smith's | 'Blindness' | same, from Smith's: "opening the eyes of the blind" is mentioned in prophecy as a peculiar attribute of the Messiah." | Smith's @382840 |

What they add up to. (1) Everyone on the shelf takes for granted that the figure is borrowed from the physical condition: Henry calls John 9:39 "a metaphor borrowed from the miracle"; ISBE says the verb is "usually" the spiritual sense and the noun and adjective the physical. (2) Edersheim and Henry both say the figure is not a verdict on blind people: "It was not the calamity of blindness"; "They who... are deprived of bodily sight, may yet... have the eyes of their understanding so enlightened"; "the sight of the body will not enlighten the soul". (3) Henry in two places goes further and says a blind man may see better inwardly: Ahijah's visions "need not bodily eyes, but are rather favoured by the want of them"; "The clearness of the eye of the understanding is of greater use to us than bodily eye-sight". (4) Against that, in a few places he also writes as if blindness is wretchedness (flagged below). (5) Both commentators treat the physical healings as tokens of the spiritual: "As a token of this, he cured many of their bodily blindness".

## What the picture assumes about the blind: what the shelf says, plainly

- The shelf's commentators do not say that the figure insults blind people. They say it describes a refusal, ignorance or self-satisfaction in people who can see.
- They do say, or imply, that blindness is a familiar picture of helplessness and groping (Henry on Deuteronomy 28, Isaiah 59, Zephaniah 1:17), and Henry in three places states a view of the condition itself that Brian may want to answer (the flagged Zephaniah 1:17 and Luke 18 lines).
- The one place that treats an actual blind guide, Ahijah, treats him as seeing well in the way that counts for a prophet (Henry, `blind-guides[7]`).
- Nothing on the shelf, in any of these commentators, calls a blind person spiritually blind. Edersheim's and Henry's blind beggar and blind men are the ones who see who Jesus is.
- What the shelf does not say: whether anyone in the first century heard "blind guide" as a slight on blind people; no source on the shelf records how blind people took the saying.

## What remains unknown

- Whether the Temple-gold oath was exactly as Henry says: no first-century source on the shelf; Edersheim says the allusion is unclear.
- Whether the Laodicean eye-powder was what Rev. 3:18 means: ISBE says "seems to have been famous"; the source it cites (Ramsay) is not on the shelf.
- How the wine was strained: Easton says the Jews "carefully filtered" it; no source is named.
- Whether the Nazareth lesson was a fixed reading for that Sabbath: Edersheim, weighing the evidence, says the verses quoted were not the whole Haphtarah.
- How the Rabbinic Midrashim Edersheim cites for Isaiah 35:5 relate in date to Jesus's time.

## Modern works Brian could consult

Not on the shelf and not read; named so he or a second reader can look. All are general knowledge and unverified here: commentaries on John 9 and on Revelation 3:14-22 that discuss the Laodicean medicine (Ramsay, *The Letters to the Seven Churches*, is named by the 1915 encyclopaedia itself); Craig Koester's or Beasley-Murray's commentaries on John; scholarly work on disability in the Bible (for example by Nancy Eiesland, Candida Moss and Jeremy Schipper, Hector Avalos). I have not read any of them and cannot vouch for what they say.

## General knowledge, marked unverified

Nothing in the JSON comes from general knowledge. In this digest the only such statements are the names of modern works in the previous section, which are unverified.

## Language flagged, not reproduced

Henry (1706-1721) and Edersheim (1883) write with the assumptions of their times, and both are hard on the Pharisees and the Jews, and in a few places on people who cannot see. The flagged passages below are located and checked (offsets are for the file's own text) but are not quoted at length here and are not used as evidence in the JSON, with these exceptions, which are used with a caution: Henry's "poor blind Gentiles" (Romans 2:19), his "senselessness and stupidity of spirit" (Romans 11:8), and ISBE's "heathen nations" (Eye). The Zephaniah 1:17 and Luke 18 lines, which Brian may most want to read, are not in the JSON. Three flagged lines bear directly on what the picture assumes about blind people (Zephaniah 1:17 "walk as blind men... without any guide or comfort"; Luke 18 "poor and blind are wretched and miserable"; John 9 "contentedly... returned to his former blindness"). They are listed by locator so Brian can read them himself and decide whether they should be quoted on a page.

| Commentator | Place | Why flagged | Locator |
|---|---|---|---|
| Henry | Zephaniah 1:17 | describes how a blind man walks as dark, doubtful, dangerous and unguided, and ends in a fall; bears directly on what the picture assumes, so Brian may want to read the sentence | Henry vol. 4 @7991930 |
| Henry | Luke 18 (Bartimaeus) | says of people who are poor and blind that they are wretched and miserable, citing Rev. 3:17, before calling them objects of compassion | Henry vol. 5 @1748634 |
| Henry | Matthew 9:27-31 | treats the blind men's crying out as begging, a mild but real assumption | Henry vol. 5 @769407 |
| Henry | John 9:35-38 | says the healed man could have gone back to being blind content, having seen the Son of God | Henry vol. 5 @5992434 |
| Henry | Acts 9:8-9 | calls Israel's blindness lasting, and sets Sodom and Egypt beside the unbelieving Jews | Henry vol. 6 @1709190 |
| Henry | Romans 11:7-10 | presents the cry of Matthew 27:25 as a curse entailed on the Jews and their children | Henry vol. 6 @395842 |
| Henry | Romans 11:8 | says Jewish unbelief is inherited by succession | Henry vol. 6 @2638106 |
| Henry | Isaiah 42:18-25 | says Israel was worse than the Gentiles | Henry vol. 4 @1386302 |
| Henry | Isaiah 42:18-25 | says the Jews who rejected Christ are still scattered, under a curse, in his own day | Henry vol. 4 @1384684 |
| Henry | Revelation 3:14-22 | calls the ruins of Laodicea a monument to the wrath of Christ | Henry vol. 6 @6649579 |
| Henry | Matthew 15:1-9 and Matthew 23 | uses Roman Catholics as the type of a church of tradition and 'church-oppressors' as the Pharisees' type | Henry vol. 5 @2913602 |
| Henry | 1 John 2:9-11 | calls Samaritans poor and ignorant in passing | Henry vol. 6 @6261092 |
| Edersheim | Matthew 23:15 (third woe) | polemical sentence about Judaism | Edersheim, Life and Times @3301223 |
| Edersheim | Matthew 23 (before the woes) | polemical sentence about Rabbinic self-assertion | Edersheim, Life and Times @3297242 |
| Edersheim | Matthew 15 (purification) | apology for his own account of Rabbinic purity rules, with a nod to 'blindness in part' | Edersheim, Life and Times @2160748 |
| Edersheim | Sketches, ch. on the Pharisees | polemical summary of the Pharisees' system and the 'blind guides' | Edersheim, Sketches @427282 |
| ISBE 1915 | 'Blindness' | calls the sight of diseased eyes in a Palestinian crowd 'disgusting' | ISBE vol. 1 @3976546 |
| ISBE 1915 | 'Eye' | 'heathen nations' for the neighbours of Israel (used in an item, with a caution) | ISBE vol. 2 @3430879 |

What Edersheim's polemic is, and what is used: his sentences against Pharisees and "Rabbinism" are not reproduced. Used: his dating and setting of the woes, his account of hand-washing and tithing, his statement of the John 9:41 distinction, and his report of the Rabbinic readings of Isaiah 35:5. Henry's remarks about "the Jews" under judgment "unto this day", the imprecation on their children, and "Papists" are not reproduced; they are listed above by locator.
