# Place and time: digest of the candidates

Written 3 October 2026. This goes with `data/reference/place_and_time_candidates.json`, which holds candidate "place and time" items for the 23 stories that do not have one yet (the man born blind already has its own), plus answers to Brian's four requests from his notes of 3 October.

Every item in the JSON has a short paragraph, a citation written as a reader would see it, one or more verbatim quotes with the file and the character offset in that file (line endings normalised to LF), a confidence of "high" or "medium", and often a `caution`. `tests/test_place_candidates.py` checks that every quote really is in its file at its offset. It does not check that the paragraph is a fair reading of the quotes, and nothing here has been seen by Brian or by a second reader yet. Read the `caution` lines before using an item: several say the paragraph needs trimming or the link is the writer's.

Counts: 94 items across the 23 stories (3 to 7 each), and 29 across the four request keys (some of those are also used for the stories they belong to). Nothing was taken from outside the shelf.

## Per story

"Coverage" is a judgement from the searches made, not a count.

| Story | Items | Coverage of the shelf |
|---|---|---|
| isaac | 4 | Fair on blindness in old age (ISBE, Josephus) and what a blessing meant; nothing on the household or country of Genesis 27. |
| jacob | 3 | Thin. Matthew Henry on his dim sight and his words, and Smith's on Goshen; the link to Goshen is the writer's. |
| eli | 3 | Good on Eli (Smith's, ISBE, Josephus) and on Shiloh's position and standing. No Edersheim or Henry (Henry's volume 2 is not on the shelf). |
| ahijah | 3 | Fair. Josephus gives the scene and his dim eyes; Smith's and ISBE give Shiloh, Tirzah and old-age blindness. No distance between Tirzah and Shiloh. |
| samson | 4 | Good. Smith's on Gaza, Samson and the hand mill, and Josephus on the boy who led him. No modern archaeology of Gaza. |
| zedekiah | 4 | Good. Smith's, Josephus, Henry on Jeremiah 34, and the route from Jerusalem to Jericho to Riblah. |
| men-of-sodom | 4 | Fair. Josephus and Smith's for the setting; the Henry passage on the sin of the city is not used because of its language. |
| aramean-raiders | 4 | Fair. Josephus retells the whole episode; Smith's gives Dothan, Samaria and Benhadad. |
| saul-on-the-damascus-road | 4 | Thin. Henry's volume 5 stops at John and Edersheim does not cover Acts, so only Smith's and ISBE speak. |
| elymas | 3 | Thin. Smith's on Cyprus, Paphos, Sergius Paulus and Elymas; nothing else. |
| two-blind-men | 4 | Fair. Henry gives the setting in Capernaum; Edersheim gives two places that do not agree. |
| blind-and-mute-man | 3 | Thin on place and time. One Henry comment, one Edersheim note on order of events, one ISBE note. |
| bethsaida | 4 | Good. Wikipedia, Smith's, Edersheim and ISBE, which disagree on whether the man was born blind. |
| bartimaeus | 6 | Rich. Edersheim's picture of Jericho, Smith's, Josephus, Wikipedia (the lowest city, winter palaces, balsam). |
| the-temple | 4 | Good. Edersheim on the court and the market, Henry on the blind and lame admitted, ISBE on the priesthood. |
| crowds-by-the-sea | 3 | Thin to fair. Henry on the scene and how the sick were brought; Edersheim places it in the Decapolis. |
| answer-to-john | 4 | Good on Machaerus and on why John was held there. Henry on the question and answer; Smith's on the prophecy about the blind. |
| pool-of-bethesda | 7 | Rich. Wikipedia on the site, the two pools and the baths, Edersheim, Henry, Smith's. |
| the-banquet | 6 | Good. Smith's on the customs of a formal meal, Edersheim and Henry on the parable. Shares items with `luke-14-parable`. |
| the-return | 4 | Fair. Henry on Jeremiah 31 and ISBE. No source on the history of the return from exile. Shares items with `jeremiah-31`. |
| job | 7 | Fair. Shares items with `job-29-15`, plus Smith's on Job and the city gate. |
| jabesh-gilead | 3 | Fair. ISBE, Smith's and Josephus (who gives the reason for the threat). |
| the-jebusite-taunt | 3 | Fair. Josephus, Whiston's note, Smith's and ISBE. The meaning of the verse is not settled on the shelf. |

## The four requests

### Luke 14:12-24 (key `luke-14-parable`, 8 items)

Three kinds of material.

Matthew Henry (Commentary on Luke 14, in volume 5) reads verses 12 to 14 as a rebuke of a host who invited only people who could pay him back. He says Jesus does not forbid entertaining friends, but warns against making it a habit, against showing off, and against hoping to be repaid in kind; the poor and maimed cannot repay, and the payment comes at the resurrection of the just. For the parable he follows the invited guests: the first group are the people at the table, the poor and maimed brought in from the streets and lanes are, he says, the publicans and sinners, and the people from the highways and hedges are the Gentiles. He adds that the gospel has often had its greatest success "among those that labour under worldly disadvantages", naming "the maimed, and the halt, and the blind". Of the second sending he says the servant is to compel "not by force of arms, but by force of arguments", because the guests would be shy and would not believe they were welcome.

Edersheim (Life and Times, Book IV, chapter XVI) sets the scene: a Sabbath meal in a ruler's house, after the healing of a man with dropsy. A guest said "Blessed is he who shall eat bread in the kingdom of God", which Edersheim says to a Pharisee meant the great feast expected at the start of the Messianic kingdom. He reads the parable the same way Henry does, with the city's chief people first, the poor of the city's streets and lanes second, and the world beyond the city last, and says "constrain" means earnest persuasion and not force. Edersheim is sharply polemical about Pharisees here and the `caution` says not to reproduce that. He also notes the Midrash on Lamentations 4:2, which says no one in Jerusalem went to a feast until the invitation had been given and repeated (Book V, chapter V).

Smith's Dictionary (entry "Meals") supplies the custom behind the second summons: on state occasions guests were invited beforehand and "on the day of the feast a second invitation was issued to those that were bidden". It also describes couches on three sides of a square, one dish into which each guest dipped his hand, and seating by rank. Smith's entry "Beggar, Begging" says the poor were "also invited to feasts" under the Law (Deuteronomy 14:29; 26:12).

What the shelf does not give: any author who treats the parable from a blind person's side. None of these sources makes the blind a special case; they appear in the list with the poor, maimed and lame.

### Jeremiah 31:7-9 (key `jeremiah-31`, 4 items; also `the-return`)

Only Matthew Henry (Commentary on Jeremiah 31, volume 4) speaks to this passage in detail. He heads the chapter "Joyful Return from Captivity" and dates it about 594 BC. On verse 8 he says many of those returning are unfit for travel, yet "the blind and the lame shall come": they will have such good will that they will not make their blindness and lameness an excuse. He says their companions "will be eyes to the blind and legs to the lame", citing Job 29:15, and that, above all, God will help them: "let none plead that he is blind who has God for his guide". On verse 9 he treats each hazard of the road in turn: a dry country, a wilderness with no road or track, a rough and rocky country, and says God will give rivers of water, a straight way they shall not miss, and no stumbling. He thinks the promise was fully accomplished "in the days of the Messiah". ISBE (entry "Jeremiah") calls chapters 30 to 33 the "Book of Comfort". The `caution` on the first item says Henry's "do not plead inability" is a sermon point a blind reader may not welcome. The shelf has nothing on the actual history of a return of exiles, so the "time" part is only Henry's date.

### Job 29:15 (key `job-29-15`, 8 items; also `job`)

Brian asked whether anyone separates serving as eyes from giving to the blind. One source does, in one sentence, and Henry's reading of Job itself is a third thing.

1. On Job 29:15 itself (volume 3), Henry reads "I was eyes to the blind" as "counselling and advising those ... that knew not what to do", and "feet to the lame" as "assisting those with money and friends that knew what they should do, but knew not how to compass it". He adds: "Those we best help whom we help out in that very thing wherein they are defective and most need help." So in Henry's reading Job's gift to the blind is advice and direction, and the lame get practical help.
2. In his comment on the two blind men of Matthew 9 (volume 5) Henry says: "Job was eyes to the blind (Job xxix. 15); was to them instead of eyes, but he could not give eyes to the blind." The same paragraph says that opening the eyes of the blind is God's prerogative (Psalm 146:8). This is the one place on the shelf that explicitly separates being someone's eyes from giving them sight.
3. In his comment on Jeremiah 31:8 (volume 4) the phrase is something companions do for each other on a journey.
4. In his comment on Proverbs 1 (volume 3) he says it is more charity "to be counsellor to the poor, as Job was with his wisdom", and cites Job 29:15 again.

ISBE and Smith's Dictionary have nothing on Job 29:15: they were searched for the verse reference and for the phrase "eyes to the blind" and did not turn it up. What they do say is that care of the blind was specially enjoined by the Law (Leviticus 19:14) and offences against them were breaches of the Law (Deuteronomy 27:18); Smith's says the Jews were specially charged to treat the blind with compassion and care. Neither source joins this to Job. No source on the shelf distinguishes "providing for" the blind from "taking pity on" them, and none discusses guiding a blind person in the way Brian means. If Brian wants that, it is his own reflection to write; the shelf supports only the "counsel and direction" reading and the one-sentence "instead of eyes, but could not give eyes".

### The walk from the Temple to the Pool of Siloam (key `siloam-walk`, 9 items)

The shelf gives the following, and only these numbers:

- Wikipedia ("Pool of Siloam", citing a 1980 Israeli guide): the pool is the lowest place in the historical city, at about 625 metres above sea level; the Temple Mount has a mean elevation of 740 metres; the climb between them is about 115 metres over a straight-line distance of about 634 metres. Going from the Temple to the pool is therefore downhill, and the way back is a climb.
- The same article: a stairway of 34 rock-hewn steps to the west of the pool, leading up from a court in front of it, recorded by the 1880s excavators; the 21st-century excavation found the Second Temple pool with steps on at least three sides in sets of five; a tiled road ending at the pool with its origins near the Temple Mount, which the excavators take to be the worshippers' road (quoting a 2006 newspaper report); and a Talmudic tradition that pilgrims started at the pool and went up on foot to the Temple, and used it for purification.
- Josephus (Wars V.4.1): the Valley of the Cheesemongers ran between the upper and lower city as far as Siloam, which he calls a fountain with sweet water in great plenty; the hills were ringed by deep valleys and precipices; the Hasmonean rulers had filled in a valley to join the city to the temple. Josephus (Wars V.4.2) has the old wall bend "above the fountain Siloam". Josephus (Antiquities XV.11.5) says the royal cloister stood over a valley so deep a person looking down would be giddy.
- Edersheim (Book IV, chapter VII): the priests' procession at the Feast of Tabernacles went, he says "probably", through Ophel, covered with buildings to the edge of Siloam, down the edge of the Tyropoeon Valley to the Fountain-Gate and the pool, and returned to the Temple by the Water-gate. He places the pool at the south-east angle of the city and says it lay still inside the wall; the Wikipedia article quotes a source that puts it outside.
- Smith's Dictionary: the rock-cut conduit from the spring to the pool is 1,708 feet long. Wikipedia's Second Temple article: Herod doubled the Temple Mount to 14.4 hectares, and water from Siloam was poured at the altar at Tabernacles.

What it does not give: a walking distance along the route (the 634 metres is a straight line), a walking time, a street-by-street route, anything about crowds, surfaces, slopes of individual streets, or whether the way was paved in Jesus's day apart from the tiled road the excavators reported. Brian's own note that the man "travelled through the city from north to south" is not supported by anything specific on the shelf either. A realistic description will need to mark clearly which parts are numbers from sources and which are written to help the reader picture it.

## Where the shelf was thin, and what would help

- **Acts (Saul, Elymas):** a commentary on Acts (Matthew Henry's volume 6, Acts to Revelation, was not taken), or fuller dictionary articles on Damascus, the street called Straight, Cyprus and the proconsulship. Edersheim does not cover Acts.
- **Joshua to 2 Kings (Eli, Ahijah, Samson, Jabesh-gilead, the Jebusites, the Aramean raiders, Zedekiah's flight):** Matthew Henry's volume 2 (Joshua to Esther) is not on the shelf; it would give a verse-by-verse comment. Archaeological summaries of Shiloh, Gaza, Tirzah and Jerusalem's Jebusite city would give place and time.
- **Genesis households (Isaac, Jacob):** a source on patriarchal customs of blessing and inheritance, and on tents and daily meals.
- **Blindness and daily life in the Gospel period:** a source on how blind people were supported in first-century Judea (family, alms, the Temple gates); Smith's and ISBE give only a few lines, and the begging note comes from Edersheim in the man-born-blind story.
- **The return from exile (the-return):** a history of the return under Cyrus and the roads between Babylon and Judah.
- **Galilee and the Decapolis (two-blind-men, blind-and-mute-man, crowds-by-the-sea):** a map-based geography of the Sea of Galilee's shores; Edersheim and Henry disagree or are silent.
- **The route to Siloam:** a plan of Second Temple Jerusalem with streets and gates, such as an archaeological atlas; the 2004 to 2008 excavation reports on the Pilgrim's Road would settle the route and the number of steps.

## Notes on how to use the JSON

- Quotes keep the shelf files' quirks: OCR errors and running heads in ISBE, footnote numbers such as `[3148]` in Edersheim and `7` in Whiston's Josephus, and raw wikitext in Wikipedia. Do not copy them into prose. Where a quote carries one of these, the `caution` says so.
- Some `caution` lines tell the editor to delete a clause or to ask Brian first (for example the rabbinic rule about blind people and the priestly blessing under `the-temple`, which is from Edersheim's other book and concerns synagogue worship).
- The paragraphs are drafts of two to four sentences; a few run to five. The paragraph for `the-banquet`, `the-return` and `job` are copies of items under the request keys, so edits should be made in both places or the copies dropped.
- Prejudiced language was met in Edersheim (about Pharisees and Rabbis), in ISBE ("disgusting" of diseased eyes), in Smith's (about a modern village's people), in Whiston's notes and in Matthew Henry (about Sodom and "the vulgar"). None of it was knowingly put into a `text`. Two quotes keep an author's harsh word about Nebuchadnezzar's act ('a refinement of barbarity'), which is a judgement on a king, not on a people; check the quotes before reuse.
