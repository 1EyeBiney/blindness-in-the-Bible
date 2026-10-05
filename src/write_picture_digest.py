"""Write docs/PICTURE_DIGEST.md from data/reference/picture_candidates.json, data/reference/picture_remarks.json and the prose below.

The counts, the item index (with file offsets) and the tables of remarks and flagged passages are generated
from the two JSON files, so they cannot drift from what was verified. The prose is written by hand.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "reference" / "picture_candidates.json").read_text(encoding="utf-8"))
rem = json.loads((ROOT / "data" / "reference" / "picture_remarks.json").read_text(encoding="utf-8"))
n = {k: len(v) for k, v in data.items()}
total = sum(n.values())
per_key = ", ".join(f"`{k}` {v}" for k, v in n.items())

SHORT = {
    "matthew_henry_vol1_genesis_to_deuteronomy.txt": "Henry vol. 1",
    "matthew_henry_vol2.txt": "Henry vol. 2",
    "matthew_henry_vol3.txt": "Henry vol. 3",
    "matthew_henry_vol4.txt": "Henry vol. 4",
    "matthew_henry_vol5_matthew_to_john.txt": "Henry vol. 5",
    "matthew_henry_vol6.txt": "Henry vol. 6",
    "edersheim_life_and_times.txt": "Edersheim, Life and Times",
    "edersheim_sketches.txt": "Edersheim, Sketches",
    "easton_ebd.txt": "Easton",
    "smiths_bible_dictionary.txt": "Smith's",
}
for i in range(1, 6):
    SHORT[f"isbe_1915_vol{i}.txt"] = f"ISBE vol. {i}"


def sf(name):
    return SHORT.get(name, name)


def index_for(key):
    lines = []
    for i, it in enumerate(data[key]):
        locs = "; ".join(f"{sf(e['file'])} @{e['offset']}" for e in it["evidence"])
        first = it["text"].split(". ")[0].rstrip(".")
        if len(first) > 150:
            first = first[:147] + "..."
        lines.append(f"- `{key}[{i}]` ({it['confidence']}): {first}. Locators: {locs}.")
    return "\n".join(lines)


def remarks_table():
    rows = ["| Commentator | Place | What he says | Locator |", "|---|---|---|---|"]
    for r in rem["remarks"]:
        q = r["quote"].replace("|", "/")
        rows.append(f"| {r['who']} | {r['locator']} | {r['note']}: \"{q}\" | {sf(r['file'])} @{r['offset']} |")
    return "\n".join(rows)


def flagged_table():
    rows = ["| Commentator | Place | Why flagged | Locator |", "|---|---|---|---|"]
    for r in rem["flagged"]:
        rows.append(f"| {r['who']} | {r['locator']} | {r['note']} | {sf(r['file'])} @{r['offset']} |")
    return "\n".join(rows)


DOC = f"""# Blindness as a picture: digest of the place-and-time candidates

Written 5 October 2026. This goes with `data/reference/picture_candidates.json`, which holds candidate items for the seven "Blindness as a picture" pages in `src/picture.py`: what Matthew Henry (volumes 1 to 6, the whole Bible) and Alfred Edersheim (*Life and Times*, *Sketches*), with the 1915 encyclopaedia, Easton and Smith's where they help, say about the passages, the places and customs behind them, and, above all, how they relate the figure to physical blindness. It is built by `src/build_picture_candidates.py`, which refuses to write a quote it cannot find in the shelf, and checked by `tests/test_picture_candidates.py`. The remarks table and the flagged list below come from `data/reference/picture_remarks.json`, written by the same script with the same check.

Every item has a short paragraph, a citation as a reader would see it, verbatim quotes with file and character offset (line endings as LF), a confidence of `high` or `medium`, and a `caution`. The test checks that each quote is really in its file at its offset. It does not check that the paragraph is a fair reading of the quote, and nothing here has been seen by Brian or a second reader. Read the `caution` lines before using an item. Nothing in the JSON was filled from memory. Where something is known only from general knowledge it is said so here and marked unverified; the JSON leaves it out.

Counts: {total} items across {len(n)} keys. Per key: {per_key}.

## How to read the locators

Henry's text is arranged by passage: the verses are printed in a block and the exposition follows. Locators in the JSON give the passage Henry is expounding (for example "Matthew 23:16-22") and every quote has an offset, so a writer can open the file and search. Edersheim's locators give the Book and chapter, because his chapters are named for the Gospel passages. The 1915 encyclopaedia text is OCR and keeps the scan's misreadings and line-end hyphens ("physi cal"); quotes from it keep them. Easton and Smith's are cited by headword.

## What was searched, and what the shelf does not say

- Henry has something on every passage on the seven pages, because volumes 2, 3, 4 and 6 are now on the shelf. The Isaiah, Lamentations, Zephaniah and Zechariah passages are in volume 4; the psalms and Job in volume 3; Deuteronomy and Exodus in volume 1; Matthew, Luke and John in volume 5; Romans to Revelation in volume 6.
- Edersheim comments on: the Matthew 23 woes and their setting (Book V ch. iv); the hand-washing and "blind leaders" of Matthew 15 (Book III ch. xxxi); John 9:39-41 (Book IV ch. ix); John 12:37-41 (Book V ch. iii); Luke 4:16-21 (Book III ch. xi); the Rabbinic reading of Isaiah 35:5-6 and Psalm 146:8 (Appendix IX). I found no comment by him on Isaiah 29, 42, 43, 56 or 59, Lamentations, Zephaniah, Zechariah, Deuteronomy 28, 2 Corinthians 4, 2 Peter, 1 John or Revelation 3 that bears on blindness (his one Romans 11 remark, on 'blindness in part', is flagged below) (a search of both books for Laodicea finds only sandals from Laodicea in *Sketches*). So for those the shelf has Henry and the dictionaries only.
- The 1915 encyclopaedia, Easton and Smith's add: the Laodicean eye-powder and school of medicine (ISBE only); the filtering of wine behind the gnat (Easton only); who a watchman was (ISBE); bribery and "Blindness, Judicial" (ISBE); the physical and figurative eye (ISBE).
- Not on the shelf: any first-century description of the Temple-gold oath (Henry and Edersheim give the rule as a statement, and Edersheim says the allusion is uncertain); anything on how a Pharisee strained his wine beyond Easton's two sentences; any account of the Laodicean eye-salve beyond the encyclopaedia's, which cites Ramsay (not on the shelf); anything about how blind people lived in the streets of Jerusalem beyond Edersheim's notes on begging and the encyclopaedia's remark that blindness was no less common.

## `blind-guides` ({n['blind-guides']} items)

Coverage: Matthew 15:12-14, 23:13-28 (oaths, gnat, cup, setting), Luke 6:39, Isaiah 56:9-11 (watchmen), Romans 2:17-21; strong on all five passages.

Digest. Henry's reading of "blind leaders of the blind" is ignorance joined to pride: they "think they see better and further than any" and lead anyway (`blind-guides[0]`). Edersheim sums up the Matthew 15 warning as "the leadership of the blind by the blind" ending in ruin for both. On the Temple gold: Henry gives the rule (an oath by the temple does not bind, an oath by its gold does) and says the point was to make people bring gold to the treasury; Edersheim says the fourth woe is aimed at the guides' "moral blindness" and that the precise allusion is not easy to understand (`blind-guides[1]`). The gnat and camel is explained by Easton as filtering wine for fear of an unclean insect (Lev. 11:23) while neglecting weightier matters; Edersheim adds the tithing of anise and the like (`blind-guides[3]`). The hand-washing is called by Edersheim a "tradition of the elders", not a law of Moses, first meant to keep sacred offerings clean (`blind-guides[4]`). The woes belong to the third day of Passion Week, "the last day in the Temple", eight woes for eight beatitudes in both Henry and Edersheim (`blind-guides[5]`). The watchmen are sentinels on the city walls (ISBE) who should have given warning; Henry offers three referents (false prophets, wicked princes, the chief priests and scribes) (`blind-guides[6]`). On the assumption: Henry reads blind Ahijah as seeing visions that "need not bodily eyes" (`blind-guides[7]`).

Item index:

{index_for('blind-guides')}

## `eyes-that-cannot-see` ({n['eyes-that-cannot-see']} items)

Coverage: John 9:39-41 and 12:37-41 (Henry and Edersheim), Romans 11:7-10, 2 Corinthians 4:3-6, 2 Peter 1:5-9, 1 John 2:9-11 (Henry), with ISBE on the usage of "blind".

Digest. Henry says John 9:39 is "a metaphor borrowed from the miracle" and reads the saying about nations and persons both (`eyes-that-cannot-see[0]`); on verse 41 he says invincible ignorance "excuses" and lessens guilt, and that the danger is in those who "fancy they do see" (`[1]`). Edersheim's verdict, the plainest on the shelf: "It was not the calamity of blindness; but it was a blindness in which they were guilty... the result of their deliberate choice", set at the Temple entrance where the blind sat and "the blind were regarded as specially entitled to charity" (`[2]`). John 12:40 is handled by both as a hard saying: Henry says "could not" means "would not" and also allows a "righteous hand of God"; Edersheim says "they did not believe, because they could not believe", then, in a note, that this is "not decreed beforehand, and irrespective of their conduct" (`[3]`). Romans 11, 2 Corinthians 4 and 1 John 2 are read as hardening, the devil's darkening of the understanding, and darkened conscience (`[4]`, `[5]`); 2 Peter 1:9 Henry glosses as "blind, that is, as to spiritual and heavenly things" and ISBE notes the verb is "usually" the spiritual sense (`[6]`). The contrast that matters for "who": Henry on Matthew 9:27 says those "deprived of bodily sight" may see with "the eyes of their understanding" what the leaders cannot (`[7]`).

Item index:

{index_for('eyes-that-cannot-see')}

## `gods-people-called-blind` ({n['gods-people-called-blind']} items)

Coverage: Isaiah 29:9-14, 42:16-20, 43:8-10 and Revelation 3:14-18; Henry on all four, the encyclopaedia on Laodicea.

Digest. Henry on Isaiah 29: the guides "were themselves blindfolded" and "when the blind lead the blind" (`gods-people-called-blind[0]`); the "sealed book" is a vision they have but cannot read (`[1]`), and in Luke 4 he says the Old Testament was "in a manner shut up till Christ opened them". On Isaiah 42:19 Henry has God's servants as the blind, and he suggests verse 18 is addressed to idolaters (`[2]`); on 43:8, "blind people that have eyes" are idolaters, after Psalm 115 (`[3]`). On Laodicea Henry says they "could not see their state, nor their way, nor their danger", and "the sight of the body will not enlighten the soul" (`[4]`). The encyclopaedia says Laodicea made a Phrygian eye-powder and had a renowned school of medicine in the vicinity, and that the city refused Rome's aid after the earthquake of A.D. 60 (`[5]`); Henry's remedy is to give up "their own wisdom and reason" (`[6]`).

Item index:

{index_for('gods-people-called-blind')}

## `like-the-blind` ({n['like-the-blind']} items)

Coverage: Deuteronomy 28:28-29, Isaiah 59:9-10, Lamentations 4:13-15, Zephaniah 1:17 (Henry); ISBE and Easton for how common blindness was and the law.

Digest. In all four Henry reads the blindness as a judgment on understanding or a figure of helplessness: "wilfully blind to their duty... made blind to their interest" (`like-the-blind[0]`), "we see no way open for our relief" (`[1]`), "blind to every thing that is good, but to do evil they were quick-sighted" (`[2]`), "their hearts and hands shall fail them" (`[3]`). The one line where Henry states what he takes a blind man's walking to be (Zephaniah 1:17) is flagged below and not used. The reference works say blindness was "no less rife" in antiquity and that the law named care for the blind (`[4]`).

Item index:

{index_for('like-the-blind')}

## `eyes-dim-with-grief` ({n['eyes-dim-with-grief']} items)

Coverage: all five laments (Job 17:7; Psalms 6, 38, 88; Lamentations 5:17), Henry on each, ISBE's "Eye" entry for the pattern.

Digest. Henry takes all five as physical: Job "wept so much that he had almost lost his sight", David "wept till he had almost wept his eyes out", the light of David's eyes "gone... with much weeping or by a defluxion of rheum... or... fainting", the mourning eye of Psalm 88 weeping while praying, and the people's dim sight in Lamentations "as is usual in a deliquium, or fainting fit". ISBE lists them together: "Eyes may grow dim with sorrow and tears". Neither Henry nor the encyclopaedia calls these blindness. Edersheim has nothing on them.

Item index:

{index_for('eyes-dim-with-grief')}

## `bribes-and-curses` ({n['bribes-and-curses']} items)

Coverage: Exodus 23:6-8, Deuteronomy 16:18-20, Zechariah 11:15-17 and 12:4; Henry on all, ISBE and Easton on bribery.

Digest. Henry on Exodus 23:8: a gift "has a strange tendency to blind those that otherwise would do well" (`bribes-and-curses[0]`); on Deuteronomy 16 he says courts sat "in the gates" and gives the three tiers of judges (`[1]`, medium confidence: he gives no source). ISBE: "the OT abounds with allusions to the corruption and venality of the magisterial bench", and a bribe "blindeth the eyes of the open- eyed" (`[2]`); Easton gives the Hebrew literally. On Zechariah 11:17 Henry reads the darkened right eye as losing sight of danger and calls it "fulfilled when Christ said to the Pharisees... those who see may be made blind" (`[3]`); ISBE says putting out the right eye "robbed the victim of his beauty, and made him unfit to take his part in war" (`[4]`). On 12:4, "blinding the horses will be as bad as houghing them" (`[5]`).

Item index:

{index_for('bribes-and-curses')}

## `eyes-opened` ({n['eyes-opened']} items)

Coverage: Psalm 146:8, Isaiah 29:18, 35:5, 42:7 and 42:16, Luke 4:16-21. Henry on all; Edersheim on Luke 4 and on the Rabbinic use of Isaiah 35:5 and Psalm 146:8.

Digest. Does Henry read these physically, spiritually or both? Psalm 146:8: both, and physical first ("He gives sight to those that have been long deprived of it... special reference to Christ... one that was born blind... spiritual illumination") (`eyes-opened[0]`). Isaiah 35:5: both, "wonders... on men's bodies" then "greater wonders... on men's souls" (`[2]`). Isaiah 29:18: spiritual only, ignorance to understanding (`[3]`). Isaiah 42:7: spiritual, "present the object... prepared the organ" (`[4]`). Isaiah 42:16: spiritual ("by nature blind"), and not physical guidance (`[5]`). Luke 4:18: spiritual, with eye-salve; Samson and Zedekiah as pictures of bondage (`[6]`). Edersheim: Isaiah 35:5-6 was "repeatedly applied to Messianic times" in the Rabbinic collections, including the Midrash on Psalm 146:8, and Jesus pointed John to it (`[1]`); at Nazareth Jesus read the Haphtarah from the Isaiah scroll, "much more than" the passage "within range of His eyes", and Edersheim's summary is "the healing which He offers to those whom sin had blinded" (`[7]`). Henry does not read Isaiah 42:16 ("I will lead the blind by a way they did not know") as a promise to people who are physically blind, and Edersheim is silent on it; that reading is the page's own, and should be marked so.

Item index:

{index_for('eyes-opened')}

## Every place the commentators remark on physical versus figurative blindness

These are the remarks, with offsets, found by searching Henry, Edersheim, the 1915 encyclopaedia, Easton and Smith's for "bodily", "spiritual", "eyes of the mind", "natural" and the like next to "blind" or "sight", and by reading each passage. They are the heart of Brian's question, what the picture assumes about the blind. Some are also used as evidence in the items above; all are checked against the shelf.

{remarks_table()}

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

{flagged_table()}

What Edersheim's polemic is, and what is used: his sentences against Pharisees and "Rabbinism" are not reproduced. Used: his dating and setting of the woes, his account of hand-washing and tithing, his statement of the John 9:41 distinction, and his report of the Rabbinic readings of Isaiah 35:5. Henry's remarks about "the Jews" under judgment "unto this day", the imprecation on their children, and "Papists" are not reproduced; they are listed above by locator.
"""

(ROOT / "docs" / "PICTURE_DIGEST.md").write_text(DOC, encoding="utf-8", newline="\n")
print("wrote docs/PICTURE_DIGEST.md", len(DOC))
