# Reference shelf report

Written 2026-10-03. A shelf of public-domain and freely licensed background works, so that each story on the site can gain a section on the place and the time. The files are in `data/raw/shelf/` (licences and sources in `SOURCE.md` there). The passage index is `data/reference/shelf_index.csv`. Everything in the digest below is a quotation, with the work and a locator so a writer can go to the source; nothing is from memory.

## What was obtained

| Work | Licence basis | File |
|---|---|---|
| Sketches of Jewish Social Life, Alfred Edersheim (1876 (CCEL print basis: Hodder and Stoughton, 1904)) | Public domain; see SOURCE.md | `edersheim_sketches.txt` |
| The Life and Times of Jesus the Messiah, Alfred Edersheim (1883 (CCEL print basis: Eerdmans, 1953)) | Public domain; see SOURCE.md | `edersheim_life_and_times.txt` |
| Antiquities of the Jews, Flavius Josephus, translated by William Whiston (Whiston translation 1737) | Public domain in the United States; see SOURCE.md | `josephus_antiquities_pg2848.txt` |
| The Wars of the Jews, Flavius Josephus, translated by William Whiston (Whiston translation 1737) | Public domain in the United States; see SOURCE.md | `josephus_wars_pg2850.txt` |
| Smith's Bible Dictionary, William Smith (1863 (CCEL print basis: 1884 American edition, with editors' additions marked --ED.)) | Public domain; see SOURCE.md | `smiths_bible_dictionary.txt` |
| The International Standard Bible Encyclopaedia, vol. 1 (A to Clemency), James Orr, general editor (1915) | Public domain in the United States; see SOURCE.md | `isbe_1915_vol1.txt` |
| The International Standard Bible Encyclopaedia, vol. 2, James Orr, general editor (1915) | Public domain in the United States; see SOURCE.md | `isbe_1915_vol2.txt` |
| The International Standard Bible Encyclopaedia, vol. 3, James Orr, general editor (1915) | Public domain in the United States; see SOURCE.md | `isbe_1915_vol3.txt` |
| The International Standard Bible Encyclopaedia, vol. 4 (Naarah to Socho), James Orr, general editor (1915) | Public domain in the United States; see SOURCE.md | `isbe_1915_vol4.txt` |
| The International Standard Bible Encyclopaedia, vol. 5 (Socho to Zuzim, with index), James Orr, general editor (1915) | Public domain in the United States; see SOURCE.md | `isbe_1915_vol5.txt` |
| Commentary on the Whole Bible, vol. 5 (Matthew to John), Matthew Henry (1706-1721) | Public domain; see SOURCE.md | `matthew_henry_vol5_matthew_to_john.txt` |
| Commentary on the Whole Bible, vol. 1 (Genesis to Deuteronomy), Matthew Henry (1706-1721) | Public domain; see SOURCE.md | `matthew_henry_vol1_genesis_to_deuteronomy.txt` |
| Eleven Wikipedia articles (see SOURCE.md for revision ids) | CC BY-SA 4.0 | `wikipedia_*.wiki.txt` |

Requests made: 24 of the 60 allowed (log: `data/raw/shelf/request_log.txt`). Wikipedia was fetched with one API call (revisions with content and revision ids) instead of eleven action=raw calls.

## What was not obtained, and why

- **Easton's Bible Dictionary**: not found as text (CCEL address 404, Gutenberg search empty). Smith's was taken instead, as the brief allowed.
- **Matthew Henry, complete**: only volume 1 (Genesis to Deuteronomy) and volume 5 (Matthew to John) were taken. Volumes 2, 3, 4 and 6 were not requested; that was a choice, not a licence problem.
- **Edersheim on Project Gutenberg**: not there; both books came from CCEL, whose files carry "Rights: Public Domain".
- **Wikipedia, 'Blindness in literature'** redirects to "Cultural depictions of blindness"; **'Bartimaeus'** redirects to "Healing the blind near Jericho"; the Siloam tunnel article is the same as 'Hezekiah's Tunnel'. All taken under their target names.
- Nothing was left out for an unclear licence.

## Notes on quality

- The ISBE (1915) text is raw OCR. Words are sometimes split or garbled and Greek and Hebrew are mostly unreadable. Locators for ISBE are the entry headword as found in the OCR; page numbers could not be read reliably. Every digest line also gives a file offset.
- Edersheim's footnote numbers appear inline as [1234]. Whiston's notes in Josephus are his own 18th-century comments, not Josephus.
- None of the old works use the word mikveh; the Wikipedia Mikveh article is the only source of that word.
- The index holds one row per paragraph (long paragraphs are cut into chunks of about 1,500 characters) that contains a search term. 'eyes near sight/blind' means 'eye' or 'eyes' within 150 characters of 'sight' or 'blind'.

## Hits per work and term

Raw occurrences of each term (regular expressions, case-insensitive). 'Siloam/Siloah' and 'Shiloah' are separate counts (Shiloah includes Shiloach). 'blind' counts blind, blinded, blinding and so on but not blindness. Index rows per work are in the last column.

| Work | blind | blindness | born blind | Siloam/Siloah | Shiloah | Bethsaida | Bethesda | Bartimaeus | Jericho | beggar | begging | alms | mikveh | Gihon | Hezekiah's tunnel | eyes near sight/blind | index rows |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Edersheim, Sketches of Jewish Social Life | 9 | 0 | 1 | 0 | 2 | 2 | 0 | 0 | 7 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 20 |
| Edersheim, Life and Times of Jesus the Messiah | 94 | 24 | 8 | 18 | 7 | 46 | 21 | 0 | 43 | 8 | 7 | 24 | 0 | 4 | 0 | 14 | 193 |
| Josephus (Whiston), Antiquities of the Jews | 9 | 2 | 0 | 1 | 10 | 1 | 0 | 0 | 54 | 0 | 4 | 0 | 0 | 1 | 0 | 6 | 75 |
| Josephus (Whiston), Wars of the Jews | 3 | 1 | 0 | 9 | 0 | 0 | 2 | 0 | 35 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 46 |
| Smith's Bible Dictionary | 16 | 5 | 1 | 38 | 25 | 13 | 5 | 3 | 78 | 6 | 3 | 13 | 0 | 9 | 0 | 2 | 127 |
| ISBE 1915 vol 1 | 37 | 15 | 0 | 7 | 7 | 29 | 3 | 4 | 69 | 22 | 19 | 52 | 0 | 1 | 0 | 10 | 171 |
| ISBE 1915 vol 2 | 27 | 15 | 2 | 15 | 19 | 1 | 0 | 0 | 39 | 1 | 2 | 11 | 0 | 28 | 0 | 11 | 118 |
| ISBE 1915 vol 3 | 59 | 10 | 1 | 52 | 18 | 11 | 9 | 5 | 74 | 6 | 4 | 6 | 0 | 27 | 0 | 5 | 215 |
| ISBE 1915 vol 4 | 21 | 9 | 1 | 41 | 55 | 8 | 3 | 0 | 47 | 9 | 1 | 13 | 0 | 7 | 0 | 2 | 153 |
| ISBE 1915 vol 5 | 14 | 12 | 0 | 43 | 40 | 4 | 10 | 3 | 40 | 7 | 7 | 16 | 0 | 17 | 0 | 8 | 189 |
| Matthew Henry vol 1 (Genesis-Deuteronomy) | 57 | 8 | 0 | 0 | 7 | 1 | 0 | 0 | 15 | 6 | 4 | 6 | 0 | 1 | 0 | 30 | 107 |
| Matthew Henry vol 5 (Matthew-John) | 332 | 35 | 30 | 19 | 19 | 32 | 9 | 3 | 20 | 51 | 24 | 61 | 0 | 0 | 0 | 76 | 381 |
| Wikipedia: Pool of Siloam | 8 | 0 | 0 | 44 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 4 | 2 | 0 | 15 |
| Wikipedia: Siloam tunnel | 0 | 0 | 0 | 33 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 20 | 0 | 14 |
| Wikipedia: Bethsaida | 1 | 0 | 0 | 0 | 0 | 79 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 27 |
| Wikipedia: Jericho | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 272 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 72 |
| Wikipedia: Second Temple | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 4 |
| Wikipedia: Pool of Bethesda | 0 | 0 | 0 | 2 | 0 | 5 | 30 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 12 |
| Wikipedia: Healing the blind near Jericho (Bartimaeus) | 15 | 1 | 0 | 0 | 0 | 1 | 0 | 20 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Wikipedia: Healing the man blind from birth | 19 | 2 | 7 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 6 |
| Wikipedia: Cultural depictions of blindness | 92 | 32 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 5 | 19 |
| Wikipedia: Begging | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 122 | 135 | 12 | 0 | 0 | 0 | 0 | 49 |
| Wikipedia: Mikveh | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 163 | 0 | 0 | 0 | 37 |

## Digest by topic

Each line is a short quotation (under 60 words, whitespace tidied, wikitext markup removed, OCR errors left as they are), the work, and a locator. The file offset is the character position in the raw file (read as UTF-8) where the quotation begins.

### Blindness and blind people in first-century life

- "Blindness is extremely common in the East from many causes. Blind beggars figure repeatedly in the New Testament (Matthew 12:22) and "opening the eyes of the blind" is mentioned in prophecy as a peculiar attribute of the Messiah. (Isaiah 29:18; 42:7) etc. The Jews were specially charged to ..." (Smith's Bible Dictionary; entry: Blindness; file `smiths_bible_dictionary.txt`, offset 382676)
- "The commonest disease is a purulent ophthalmia, a highly infectious condition propagated largely by the flies which can be seen infesting the crusts of dried secretion undisturbed even on the eyes of infants. (In Egypt there is a superstition that it is ..." (ISBE 1915 vol 1; vol 1, entry: BLINDNESS; file `isbe_1915_vol1.txt`, offset 3977047)
- "Blindness unfitted a man for the priesthood (Lev 21 18); but care of the blind was specially enjoined in the Law (Lev 19 14), and offences against them are regarded as breaches of Law (Dt 27 18). Figuratively, blindness is ..." (ISBE 1915 vol 1; vol 1, entry: BLINDNESS; file `isbe_1915_vol1.txt`, offset 3980521)
- "Indeed, the blind were regarded as specially entitled to charity; [4120] and the Jerusalem Talmud [4121] relates some touching instances of the ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2637419)
- "and we constantly find Rabbis, when meeting such unfortunate persons, asking them, how or by what sin this had come to them. But, as this man was blind from his birth,' the possibility of some actual sin before birth would ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2638288)
- "It was a common Jewish view, that the merits or demerits of the parents would appear in the children. In fact, up to thirteen years of age a child was ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2638929)
- "The eulogies or "tephillah" proper, as well as the priestly benediction, could not be pronounced by those who were not properly clothed, nor by those who were so blind as not to be able to discern daylight. If any one introduced into the prayers heretical views, or what were regarded ..." (Edersheim, Sketches of Jewish Social Life; Chapter 17; file `edersheim_sketches.txt`, offset 496988)
- "In like manner, let no one revile a person blind or dumb ..." (Josephus (Whiston), Antiquities of the Jews; book IV, chapter 8, section 32; file `josephus_antiquities_pg2848.txt`, offset 586281)
- "shut their gates, and placed the blind, and the lame, and all their maimed persons, upon the wall, in way of derision of the king, and said that the very lame themselves would hinder his entrance into it. This they did out of contempt of ..." (Josephus (Whiston), Antiquities of the Jews; book VII, chapter 3, section 1; file `josephus_antiquities_pg2848.txt`, offset 966660)
- "These blind men were sitting by the way-side, as blind beggars used to do. Note, Those that would receive mercy from Christ, must place themselves there where his out-goings are; where he manifests himself to those that seek him. It ..." (Matthew Henry vol 5 (Matthew-John); Matthew chap. XX; file `matthew_henry_vol5_matthew_to_john.txt`, offset 1740880)

### Begging and alms in Jesus's day

- "Begging was well known and beggars formed a considerable class in the gospel age. Proof of this is found in the references to almsgiving 5. In the in the Sermon on the Mount (Mt 5-7 Gospel Age and parallels), and in the accounts of beggars ..." (ISBE 1915 vol 1; vol 1, entry: BEGGING; file `isbe_1915_vol1.txt`, offset 3478674)
- "and in the accounts of beggars in connection with public places, e.g. the entrance to Jericho (Mt 20 30 and parallels), which was a gateway to pilgrims going up to Jerus to the great festivals and in the neigh borhood of rich men's houses (Lk 16 20), and esp. the ..." (ISBE 1915 vol 1; vol 1, entry: BEGGING; file `isbe_1915_vol1.txt`, offset 3478930)
- "This prevalence of begging was due largely to the want of any adequate system of ministering relief, to the lack of any true medical science and the resulting ignorance of remedies for common dis eases like ophthalmia, for instance, and to the impoverishment of the land under the excessive taxation ..." (ISBE 1915 vol 1; vol 1, entry: BEGGING; file `isbe_1915_vol1.txt`, offset 3479295)
- "As to professional beggars, originally, certainly, and for a long time, they were a despised class among the Hebrews; and the Jewish 4. Profes- communities are forbidden to support sional Beg- them from the general charity fund gars a (BB, 9a; Yoreh De]ah, 250, 3) ..." (ISBE 1915 vol 1; vol 1, entry: BEGGING; file `isbe_1915_vol1.txt`, offset 3478137)
- "Remembering, that the entrance to the Temple or its Courts was then - as that of churches is on the Continent - the chosen spot for those who, as objects of pity, solicited charity; [4118] remembering, also, how rapidly the healing of the blind man became known, and how soon ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2635959)
- "where this blind beggar was wont to sit, probably soliciting alms, perhaps in some such terms as these, which were common at the time: Gain merit by me;' or, O tenderhearted, by me gain merit, to thine own benefit.' But on the Sabbath he would, of course, neither ask nor ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2637009)
- "For to persons so wretchedly poor as to allow their son to live by begging, [4145] the consequence of being un-Synagogued,' or put outside the congregation [4146] - ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2650573)
- "the shrinking from receiving alms was in proportion to the duty of giving them. Only extreme necessity would warrant begging, and to solicit charity needlessly, or to simulate any disease for the purpose, would, deservedly, bring the reality in punishment on the guilty. [4146] posungogos gnesthai. So also St. John ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2664905)
- "Alms were collected at regular times every week, either in money or in victuals. At least two were employed in collecting, and three in distributing charity, so as to avoid the suspicion of dishonesty or partiality. These collectors of charity, who required to be "men ..." (Edersheim, Sketches of Jewish Social Life; Chapter 18; file `edersheim_sketches.txt`, offset 509231)
- "Whenever," we read, "a poor man stands at thy door, the Holy One, blessed be His Name, stands at his right hand. If thou givest him alms, know that thou shalt receive a reward from Him who standeth at his right hand." In another commentary God Himself and His angels are said ..." (Edersheim, Sketches of Jewish Social Life; Chapter 4; file `edersheim_sketches.txt`, offset 88089)
- "The New Testament contains several references to Jesus' status as the savior of the ptōchós, usually translated as "the poor", considered the most wretched portion of society. In the rich man and Lazarus parable, Lazarus is called ptōchós and presented ..." (Wikipedia: Begging; section: Greece; file `wikipedia_Begging.wiki.txt`, offset 4021)

### The Pool of Siloam and the water system

- "Siloam is one of the few undisputed localities in the topography of Jerusalem; still retaining its old name (with Arabic modification, Silwan), while every other pool has lost its Bible designation. This is the more remarkable as it is a mere suburban tank of no great size, and for many an age not particularly good ..." (Smith's Bible Dictionary; entry: Siloam; file `smiths_bible_dictionary.txt`, offset 2703064)
- "though Josephus tells us that in his day they were both "sweet and abundant." A little way below the Jewish burying-ground, but on the opposite side ..." (Smith's Bible Dictionary; entry: Siloam; file `smiths_bible_dictionary.txt`, offset 2703459)
- "At the back part of this fountain a subterraneous passage begins, through which the water flows, and through which a man may make his way, sometimes walking erect, sometimes stooping, sometimes kneeling, and sometime crawling, to Siloam. This conduit is 1708 feet long, 16 feet high at the entrance, but ..." (Smith's Bible Dictionary; entry: Siloam; file `smiths_bible_dictionary.txt`, offset 2703950)
- "extended as far as Siloam; for that is the name of a fountain which hath sweet water in it, and this in great plenty also. But on the outsides, these hills are surrounded by deep ..." (Josephus (Whiston), Wars of the Jews; book V, chapter 4, section 1; file `josephus_wars_pg2850.txt`, offset 922688)
- "It was made by King Hezekiah, in order both to divert from a besieging army the spring of Gihon, which could not be brought within the City-wall, and yet to bring its waters within the City. [3999] This explains the origin of the name Siloam, sent' - a conduit [4000] ..." (Edersheim, Life and Times of Jesus the Messiah; chapter VII (IN THE LAST, THE GREAT DAY OF THE FEAST'); file `edersheim_life_and_times.txt`, offset 2574303)
- "at the Feast of Tabernacles, amidst universal rejoicing, water from Siloam was poured from a golden pitcher on the altar, as emblem of the outpouring of the Holy Ghost. [1984] But the saying of our Lord to the Samaritaness referred ..." (Edersheim, Life and Times of Jesus the Messiah; chapter VIII (JESUS AT THE WELL OF SYCHAR); file `edersheim_life_and_times.txt`, offset 1301281)
- "saliva was commonly regarded as a remedy for diseases of the eye, although, of course, not for the removal of blindness. With this He made clay, which He ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2644012)
- "adding to it the direction to go and wash in the Pool of Siloam, a term which literally meant sent.' [4134] A symbolism, this, of Him Who was the Sent of the Father. For, all is here symbolical: the cure ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); file `edersheim_life_and_times.txt`, offset 2644182)
- "is a passive form and means "sent" or "conducted")^ "the waters of [the] Shiloah" (Isa 8 6). (2) nblTH TD^a, h^re- khaih hn-shelah, "the jxjol of [the] Shelah" ..." (ISBE 1915 vol 4; vol 4, entry: SHILOAH; file `isbe_1915_vol4.txt`, offset 6039964)
- "The pool was rediscovered during an excavation work for a sewer in the autumn of 2004, by Ir David Foundation workers, following a request and directions given by archaeologists Eli Shukron accompanied by Ori Orbach from the Israel Nature and Parks Authority ..." (Wikipedia: Pool of Siloam; section: Second Temple period pool; file `wikipedia_Pool_of_Siloam.wiki.txt`, offset 12434)
- "The pools were fed by the waters of the Gihon Spring, carried there by the Siloam tunnel. The Lower Pool or "Old ..." (Wikipedia: Pool of Siloam; section: lead; file `wikipedia_Pool_of_Siloam.wiki.txt`, offset 840)
- "Its popular name is due to the most common hypothesis that it dates from the reign of Hezekiah of Judah, late 8th and early 7th century BC ..." (Wikipedia: Siloam tunnel; section: lead; file `wikipedia_Siloam_tunnel.wiki.txt`, offset 1449)

### Bethsaida

- "Bethsaida (house of fish) of Galilee, (John 12:21) a city which was the native place of Andrew, Peter and Philip, (John 1:44; 12:21) in the land of Gennesareth, (Mark 6:46) comp. Mark 6:53 And therefore on the west side of the lake. By comparing the narratives in (Mark 6:31-53) and ..." (Smith's Bible Dictionary; entry: Bethsaida; file `smiths_bible_dictionary.txt`, offset 359736)
- "also Bethsaida, [12] the name, "house of fishes," indicating its trade. Capernaum was the station where Matthew sat at the ..." (Edersheim, Sketches of Jewish Social Life; Chapter 3; file `edersheim_sketches.txt`, offset 68348)
- "just as he changed the name of Bethsaida, a village of which he made an opulent city, into Julias, after the daughter of Augustus. But he was a moderate and ..." (Edersheim, Life and Times of Jesus the Messiah; chapter XI (IN THE FIFTEENTH YEAR OF TIBERIUS CÆSAR AND UNDER THE PONTIFICATE OF A); file `edersheim_life_and_times.txt`, offset 852279)
- "He led him out of the town. Had he herein only designed privacy, he might have led him into a house, into an inner chamber, and have cured him there; but he intended hereby to upbraid Bethsaida with the mighty works that had in vain been done in her (Matt. xi. 21) ..." (Matthew Henry vol 5 (Matthew-John); Mark chap. VIII; file `matthew_henry_vol5_matthew_to_john.txt`, offset 2964099)

### Jericho

- "Under Herod the Great it again became an important place. He fortified it and built a number of new palaces, which he named after his friends. If he did not make Jericho his habitual residence, he at last retired thither to die, and it was in the amphitheater of Jericho that the ..." (Smith's Bible Dictionary; entry: Jericho; file `smiths_bible_dictionary.txt`, offset 1199087)
- "Thus Jericho was once more "a city of palms" when our Lord visited it. Here he restored sight to the blind. (Matthew 20:30; Mark 10:46; Luke ..." (Smith's Bible Dictionary; entry: Jericho; file `smiths_bible_dictionary.txt`, offset 1199880)
- "Flanked and defended by four surrounding forts, lay the important city of Jericho. Herod had built its walls, its theatre and amphitheatre; Archelaus its new palace, surrounded by splendid gardens. Through Jericho led the pilgrim way from Galilee, followed by our Lord Himself (Luke 19:1); and there also passed the ..." (Edersheim, Sketches of Jewish Social Life; Chapter 5; file `edersheim_sketches.txt`, offset 112554)
- "Rome had made it a central station for the collection of tax and custom, known to us from Gospel history as that by which the chief publican Zaccheus had gotten his wealth ..." (Edersheim, Sketches of Jewish Social Life; Chapter 5; file `edersheim_sketches.txt`, offset 113264)
- "along the fifth great highway (comp. Luke 19:1, 28; Matt 20:17, 29), that led from Jerusalem, by Bethany, to Jericho. Here the Jordan was forded, and the road led to Gilead, and thence either southwards, or else north ..." (Edersheim, Sketches of Jewish Social Life; Chapter 4; file `edersheim_sketches.txt`, offset 80673)
- "there is a fountain by Jericho, that runs plentifully, and is very fit for watering the ground; it arises near the old city, which Joshua, the son of Naue, the general of the Hebrews, took the first of ..." (Josephus (Whiston), Wars of the Jews; book IV, chapter 8, section 3; file `josephus_wars_pg2850.txt`, offset 819811)
- "BARTIMAEUS, bar-ti-me'us (Bapi-C^cucs, Bar- timaios): A hybrid word from Aram. bar = "son," and Gr ..." (ISBE 1915 vol 1; vol 1, entry: BARTIMAEUS; file `isbe_1915_vol1.txt`, offset 3334688)

### The Temple and who could enter

- "there was a partition made of stone all round, whose height was three cubits: its construction was very elegant; upon it stood pillars, at equal distances from one another, declaring the law of purity, some in Greek, and some in Roman letters, that "no foreigner should go within that sanctuary" for that second [court of ..." (Josephus (Whiston), Wars of the Jews; book V, chapter 5, section 2; file `josephus_wars_pg2850.txt`, offset 936276)
- "Here also there lay about a crowd of noisy beggars, unsightly from disease, and clamorous for help. And close by passed the luxurious scion of the High-Priestly families; the proud ..." (Edersheim, Life and Times of Jesus the Messiah; chapter I (IN JERUSALEM WHEN HEROD REIGNED); file `edersheim_life_and_times.txt`, offset 399943)
- "and the child must be free from all such bodily blemishes as would have disqualified him for the priesthood - or, as it was expressed: the firstborn for the priesthood.' It was ..." (Edersheim, Life and Times of Jesus the Messiah; chapter VII (THE PURIFICATION OF THE VIRGIN AND THE PRESENTATION IN THE TEMPLE); file `edersheim_life_and_times.txt`, offset 646116)
- "According to the Mishnah, they who pronounce the benediction must have no blemish on their hands, face, or feet, so as not to attract attention; but this presumably ..." (Edersheim, Life and Times of Jesus the Messiah; chapter X (THE SYNAGOGUE AT NAZARETH - SYNAGOGUE-WORSHIP AND ARRANGEMENTS.); file `edersheim_life_and_times.txt`, offset 1385650)
- "Blindness unfitted a man for the priesthood (Lev 21 18); but care of the blind was specially enjoined in the Law (Lev 19 14), and offences against them are regarded ..." (ISBE 1915 vol 1; vol 1, entry: BLINDNESS; file `isbe_1915_vol1.txt`, offset 3980521)
- "Hundreds of mikvot from the Second Temple period have been discovered so far across the Land of Israel, including in Jerusalem, Hebron ..." (Wikipedia: Mikveh; section: History; file `wikipedia_Mikveh.wiki.txt`, offset 6617)

### Things the digest suggests for the stories (pointers only)

- John 9: Edersheim's chapter IX, 'The Healing of the Man Born Blind' (offset about 2,635,000 onward in `edersheim_life_and_times.txt`) treats the whole chapter: the begging spot at the Temple entrance, the saliva-and-clay detail, the Pool of Siloam, and the parents' fear of being put out of the synagogue.
- Mark 10 and Matthew 20: ISBE (entry BARTIMAEUS and entry BEGGING) and Matthew Henry vol. 5 on Matthew 20 and Mark 10 give the Jericho setting; Smith's and Edersheim's Sketches give Herod's Jericho; Josephus Wars 4.8.3 gives the spring.
- Mark 8: Matthew Henry vol. 5 on Mark 8 for Bethsaida, Smith's for the two Bethsaidas.

## Statements in the old sources that read as prejudiced

These are flagged so they are not repeated without thought. The works are from 1706 to 1915 and reflect their own times. Several treat 'the Jews', or 'the Pharisees', as one block, set Jewish learning against Christian teaching as 'error' or 'externalism', or use blindness as an insult. The review below is of the passages found through this index; the books were not read through for prejudice, so more will exist (Matthew Henry and Whiston's notes especially).

- "so thoroughly Judaised were they by their late contact with the Pharisees, that no thought of possible mercy came to them, only a truly and characteristically Jewish question, addressed to Him expressly, and as Rabbi:' [4122] through whose guilt this ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); offset 2637757). Treats Jewish thought as something the disciples had to be freed from; 'Judaised' used as a criticism.
- "to which they sought to apply the common Jewish solution. Many similar mysteries meet us in the administration of God's ..." (Edersheim, Life and Times of Jesus the Messiah; chapter IX (THE HEALING OF THE MAN BORN BLIND.); offset 2639856). Presents rabbinic reasoning about sin and disability as a 'solution' to be corrected.
- "despised them as cursed, ignorant country people, little better than heathens, or, for that matter, than brute beasts. Here also there lay about a crowd of noisy beggars, unsightly from ..." (Edersheim, Life and Times of Jesus the Messiah; chapter I (IN JERUSALEM WHEN HEROD REIGNED); offset 399818). Contempt attributed to Jewish leaders, stated as a generalisation about their class.
- "Here also there lay about a crowd of noisy beggars, unsightly from disease, and clamorous for help. And close by ..." (Edersheim, Life and Times of Jesus the Messiah; chapter I (IN JERUSALEM WHEN HEROD REIGNED); offset 399943). Not anti-Jewish, but the language about disabled and sick people is demeaning.
- "The result was a system of pure externalism, which often contravened the spirit of those very ordinances, the letter of which was slavishly worshipped. To ..." (Edersheim, Sketches of Jewish Social Life; Chapter 14; offset 427282). Sweeping verdict on Pharisaic Judaism; 'arrant hypocrisy' follows in the same passage.
- "despised, rejected, and delivered up unto death by the blind guides of His blinded fellow-countrymen. Had He entirely discarded the period in ..." (Edersheim, Sketches of Jewish Social Life; Chapter 18; offset 528462). Uses blindness as an insult and blames 'fellow-countrymen' collectively for the death of Jesus.
- "far more deeply tinged with superstition and error of every kind. For historical purposes, also ..." (Edersheim, Sketches of Jewish Social Life; Chapter 3; offset 75889). Dismisses the Babylonian Talmud wholesale.
- "were taught Josephus by the Pharisees, a body of men at once very wicked and very superstitious.] 25 (return) [ Of this ..." (Josephus (Whiston), Antiquities of the Jews; Whiston's footnotes after book II; offset 332748). Whiston's own editorial footnote (footnotes are gathered at the end of Book 2), not Josephus's text; it calls the Pharisees 'very wicked'.
- "defective eyes and bleared, inflamed lids are among the commonest and most disgusting sights in a Pal crowd. In the Papyrus Ebers (1500 BC) there ..." (ISBE 1915 vol 1; vol 1, entry: BLINDNESS; offset 3976493). Contemptuous about people with eye disease; also stereotypes crowds in Palestine.
- "indolent and licentious and about 40 houses. Dr. Olin says it is the "meanest and foulest village of Palestine;" yet ..." (Smith's Bible Dictionary; entry: Jericho; offset 1200787). Editor's remark about the people of modern Jericho (Riha); stereotyping of local people.

Two more cautions that are not about any single quote:

- Edersheim calls the disciples' question in John 9 'thoroughly Jewish' (Life and Times) and 'a strictly Jewish question' (Sketches). The question is in the Gospel text as the disciples asked it; it should not be attached to Jewish people as a whole.
- Several sources (ISBE, Smith's, Edersheim) describe disabled or poor people in the language of disgust. A writer should keep the facts (how common eye disease was, how begging worked) and drop the tone.
