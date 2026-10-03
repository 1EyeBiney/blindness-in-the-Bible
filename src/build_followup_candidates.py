"""Build data/reference/followup_candidates.json from quotes taken from the reference shelf.

Same method as build_law_candidates.py: each item is written by hand (a plain statement
of what the shelf says, a citation, one or more verbatim quotes). This script finds each
quote in its file (whitespace-insensitive), records the character offset (line endings as
LF) and refuses to write anything if a quote cannot be found.

Keys follow Brian's follow-up questions of 3 October 2026:
  eli-duties, ahijah-duties      Shiloh: what a priest-judge and a prophet did
  gate-life                      the walled town's gate, activity by activity
  canes-and-staffs               canes, staffs and guides, in the Bible and the ancient world
  jerusalem-layout               the streets, stairs and valleys of first-century Jerusalem
  tent-life                      a blind person in a nomadic camp; heat, dust, eye disease
  history-of-the-blind           the history of blind people's lives, beyond the Bible

    python src/build_followup_candidates.py   -> data/reference/followup_candidates.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
OUT = ROOT / "data" / "reference" / "followup_candidates.json"

_cache: dict[str, str] = {}
FAILS: list = []


def text_of(name):
    if name not in _cache:
        _cache[name] = (SHELF / name).read_text(encoding="utf-8")
    return _cache[name]


def find(name, quote):
    words = quote.split()
    rx = r"\s+".join(re.escape(w) for w in words)
    ms = list(re.finditer(rx, text_of(name)))
    if not ms:
        FAILS.append((name, quote[:90]))
        return 0, 0
    return ms[0].start(), len(ms)


def ev(name, quote):
    off, _ = find(name, quote)
    assert len(quote.split()) < 60, quote[:60]
    return {"file": name, "offset": off, "quote": " ".join(quote.split())}


def item(text, source, evidence, confidence="high", caution=None):
    d = {"text": text, "source": source, "evidence": evidence, "confidence": confidence}
    if caution:
        d["caution"] = caution
    return d


# ---------------------------------------------------------------- files
H1 = "matthew_henry_vol1_genesis_to_deuteronomy.txt"
H2 = "matthew_henry_vol2.txt"
H3 = "matthew_henry_vol3.txt"
H4 = "matthew_henry_vol4.txt"
H5 = "matthew_henry_vol5_matthew_to_john.txt"
H6 = "matthew_henry_vol6.txt"
EAS = "easton_ebd.txt"
SMI = "smiths_bible_dictionary.txt"
I1, I2, I3, I4, I5 = (f"isbe_1915_vol{i}.txt" for i in range(1, 6))
EDL = "edersheim_life_and_times.txt"
EDS = "edersheim_sketches.txt"
JW = "josephus_wars_pg2850.txt"
JA = "josephus_antiquities_pg2848.txt"
WIL = "wilson_biography_of_the_blind_1838.txt"
LEV = "levy_blindness_and_the_blind_1872.txt"


def wk(name):
    return f"wikipedia_{name}.wiki.txt"


def wsrc(title, date):
    return f"Wikipedia, '{title}', revision of {date} (CC BY-SA 4.0)"


HENRY = "Matthew Henry, Commentary on the Whole Bible (1706-1721), on "
OLD_OCR = ("The 1915 encyclopaedia text on the shelf is an OCR scan with occasional misread letters; "
           "quotations keep the scan's spelling.")

K = {}

# ================================================================= eli-duties
K["eli-duties"] = [
    item(
        "Easton's dictionary gives Eli three roles in one man: high priest while the ark was at Shiloh, civil judge "
        "of Israel for forty years, and (in the story of his death) an old man who sat by the sanctuary gate on the "
        "road, waiting for news from the battle. Easton glosses his eyes as 'stiffened', that is fixed, 'as of a blind "
        "eye unaffected by the light'.",
        "Easton's Bible Dictionary (1897), entry 'Eli'",
        [ev(EAS, "Ascent, the high priest when the ark was at Shiloh (1 Sam. 1:3, 9)."),
         ev(EAS, "He acted also as a civil judge in Israel after the death of Samson (1 Sam. 4:18), and judged Israel for forty years."),
         ev(EAS, "There Eli sat outside the gate of the sanctuary by the wayside, anxiously waiting for tidings from the battle-field."),
         ev(EAS, 'When the old man, whose eyes were "stiffened" (i.e., fixed, as of a blind eye unaffected by the light) with age,')],
        "high",
        "Easton goes on to say Eli 'failed to reprove' his sons sternly enough; that moral verdict is not used here. "
        "The dictionary does not say when Eli's sight began to fail.",
    ),
    item(
        "Three older reference works agree that Eli held the offices of priest and judge together. The 1915 encyclopaedia "
        "says it was the first time in Israel the two were combined in one person; Smith's says he held both; Easton's "
        "(in its entry 'Judge') says the judgeship came to him 'ex officio'.",
        "International Standard Bible Encyclopaedia (1915), entry 'Eli', vol 2; Smith's Bible Dictionary (1884 edition), entry 'Eli'; Easton's Bible Dictionary (1897), entry 'Judge'",
        [ev(I2, "For the first, time in Israel, Eli combined in his own person the functions of high priest and judge, judging Israel for 40 years"),
         ev(SMI, "In addition to the office of high priest he held that of judge."),
         ev(EAS, "and as to Eli, the office of judge seems to have devolved naturally or rather ex officio upon him.")],
        "high",
        OLD_OCR + " 'First time in Israel' is one writer's claim (A. C. Grant); the other works do not repeat it.",
    ),
    item(
        "Smith's lists the chief duties of the priests: keep the altar fire burning day and night, feed the golden lamp "
        "with oil, offer the morning and evening sacrifices at the door of the tabernacle, teach the children of Israel the "
        "statutes of the Lord, and act as a court of appeal in difficult criminal or civil cases (Deuteronomy 17:8-13).",
        "Smith's Bible Dictionary (1884 edition), entry 'Priest', section 'Duties'",
        [ev(SMI, "The chief duties of the priests were to watch over the fire on the altar of burnt offering, and to keep it burning evermore both by day and night,"),
         ev(SMI, "to feed the golden lamp outside the vail with oil (Exodus 27:20,21; Leviticus 24:2) to offer the morning and evening sacrifices, each accompanied with a meet offering and a drink offering, at the door of the tabernacle."),
         ev(SMI, "They were also to teach the children of Israel the statutes of the Lord."),
         ev(SMI, "They were to act (whether individually or collectively does not distinctly appear) as a court of appeal in the more difficult controversies in criminal or civil cases.")],
        "high",
        "These are the duties of the Aaronic priesthood in general, taken from the law. Smith's does not say which of them Eli "
        "himself carried out, or how they were shared among the priests and their servants at Shiloh.",
    ),
    item(
        "Henry, on 1 Samuel 1, pictures Eli seated where he could 'receive addresses and give direction', and notes how he "
        "judged Hannah: he 'marked her mouth' and, seeing only her lips move, took her to be drunk. The verses printed in "
        "Henry have Eli 'sat upon a seat by a post of the temple of the Lord'.",
        HENRY + "1 Samuel 1",
        [ev(H2, "Now Eli the priest sat upon a seat by a post of the temple of the Lord."),
         ev(H2, "Eli marked her mouth. 13 Now Hannah, she spake in her heart; only her lips moved, but her voice was not heard: therefore Eli thought she had been drunken."),
         ev(H2, "There Eli sat to receive addresses and give direction, and somewhere (it is probable in a private corner) he espied Hannah at her prayers")],
        "medium",
        "The verses are the King James text as printed by Henry. 'In a private corner' is Henry's own guess. Neither the verses "
        "nor Henry say how well Eli could see at this point; his eyes are first called dim in chapter 3.",
    ),
    item(
        "Henry, on 1 Samuel 2:25, says the 'judge' in the law (Deuteronomy 17:9) means the priest, who was 'appointed to be the "
        "judge in many cases', and adds that Eli 'was himself a judge' who had often made intercession for wrongdoers.",
        HENRY + "1 Samuel 2",
        [ev(H2, "the judge (that is, the priest, who was appointed to be the judge in many cases, Deut. xvii. 9) shall judge him, shall undertake his cause, arbitrate the matter, and make atonement for the offender"),
         ev(H2, "Eli was himself a judge, and had often made intercession for transgressors")],
        "high",
        "Henry is reading Eli's rebuke to his sons ('If one man sin against another, the judge shall judge him'). The exact "
        "procedure of Eli's court is not described anywhere on the shelf.",
    ),
    item(
        "A duty that depended on looking: in Leviticus 13 the priest 'shall look on' a skin disease and pronounce the person "
        "clean or unclean, again after seven days. Henry reports a Jewish rule that a priest disabled from the sanctuary by a "
        "blemish could still judge the disease 'provided the blemish were not in his eye', and that he could take a common "
        "person to assist him in the search, 'but the priest only must pronounce the judgment'.",
        HENRY + "Leviticus 13",
        [ev(H1, "And the priest shall look on the plague in the skin of the flesh: and when the hair in the plague is turned white, and the plague in sight be deeper than the skin of his flesh, it is a plague of leprosy: and the priest shall look on him, and pronounce him unclean."),
         ev(H1, '"Any priest, though disabled by a blemish to attend the sanctuary, might be a judge of the leprosy, provided the blemish were not in his eye.'),
         ev(H1, 'And he might" (they say) "take a common person to assist him in the search, but the priest only must pronounce the judgment."')],
        "medium",
        "'Leprosy' is the King James word for the skin conditions of Leviticus 13. Henry gives the Jewish rule as 'All the Jews "
        "say' with no named source and no date, so it may be later than Eli's time. His remark that lepers were 'stigmatized by "
        "the justice of God' is a dated attitude and is not used.",
    ),
    item(
        "In 1 Samuel 3 Eli's eyes 'began to wax dim, that he could not see' while the lamp of God was still burning and Samuel "
        "slept nearby. Henry pictures Samuel as having 'waited on' Eli to his bed, and says that when Samuel kept coming to him "
        "Eli, perceiving it was God's voice, 'gave him instructions what to say'.",
        HENRY + "1 Samuel 3",
        [ev(H2, "2 And it came to pass at that time, when Eli was laid down in his place, and his eyes began to wax dim, that he could not see; 3 And ere the lamp of God went out in the temple of the Lord, where the ark of God was, and Samuel was laid down to sleep;"),
         ev(H2, "Samuel had waited on him to his bed, and the rest that attended the service of the sanctuary had gone, we may suppose, to their several apartments"),
         ev(H2, "Eli, perceiving that it was the voice of God that Samuel heard, gave him instructions what to say, v.")],
        "medium",
        "Henry connects Eli's failing sight to his sons' faults ('an affliction which came justly upon him'); that is a "
        "dated and patronising reading of blindness and is deliberately not quoted. 'Waited on him to his bed' is Henry's picture, not the text.",
    ),
    item(
        "Henry, on 1 Samuel 4, calls Eli 'old, and blind, and heavy' yet unable to stay in his chamber: he placed himself "
        "'by the way-side, to receive the first intelligence'. In the verses Eli hears 'the noise of the crying' and asks what it "
        "means; Henry says the messenger 'was loth to tell him first' and so, having passed Eli 'in the gate', told the city before telling Eli.",
        HENRY + "1 Samuel 4",
        [ev(H2, "14 And when Eli heard the noise of the crying, he said, What meaneth the noise of this tumult? And the man came in hastily, and told Eli."),
         ev(H2, "Eli sat in the gate (v. 13, 18), but the messenger was loth to tell him first, and therefore passed him by, and told it in the city"),
         ev(H2, "Though old, and blind, and heavy, yet he could not keep his chamber when he was sensible the glory of Israel lay at stake, but placed himself by the way-side, to receive the first intelligence")],
        "high",
        "Henry's 'heavy' is his word for Eli's age and weight; the verse says Eli's eyes were dim at ninety-eight. Where exactly the "
        "'gate' of Shiloh stood is not known; Easton's has the seat 'outside the gate of the sanctuary by the wayside'.",
    ),
    item(
        "The 1915 encyclopaedia says what a judge's hearing looked like: the court was open to the public, each party presented "
        "his own view of the case, and the only evidence the court considered was what the witnesses said. The judge's first duty "
        "was to give absolute justice, with the same impartiality to rich and poor.",
        "International Standard Bible Encyclopaedia (1915), entry 'Judge', vol 3",
        [ev(I3, "The first duty of a judge was to execute absolute justice, showing the same impartiality to rich and poor,"),
         ev(I3, "The court was open to the public (Ex 18 13; Ruth 4 1.2). Each party presented his view of the case to the judge (Dt 1 16; 25 1)."),
         ev(I3, "The only evidence considered by the court was that given by the witnesses.")],
        "high",
        OLD_OCR + " This is a general account of the judge's work in Israel's law; it is not specific to the period of Eli.",
    ),
    item(
        "Wikipedia gives a shorter modern summary: Eli was a priest (kohen) of Shiloh and the second-to-last judge before the "
        "kings; priestly duties were offering the sacrifices and delivering the Priestly Blessing; and biblical passages attest "
        "priests teaching Torah and 'issuing judgment'. Certain physical blemishes could disqualify a kohen from service, but "
        "never permanently.",
        wsrc("Eli (biblical figure)", "29 July 2026") + "; " + wsrc("Kohen", "22 September 2026"),
        [ev(wk("Eli_biblical_figure"), "Eli was a priest (''kohen'') of Shiloh, the second-to-last Israelite [[biblical judges|judge]]"),
         ev(wk("Kohen"), "Priestly duties involved offering the Temple [[Korban|sacrifices]], and delivering the [[Priestly Blessing]]."),
         ev(wk("Kohen"), "Numerous Biblical passages attest to the role of the priests in teaching [[Torah]] to the people and in issuing judgment."),
         ev(wk("Kohen"), "The kohen is never permanently disqualified from service, but may return to his normal duties once the disqualification ceases.")],
        "medium",
        "Raw wikitext (links and templates left in). The Kohen article's disqualification sentence rests on Leviticus 21:17-23 and "
        "later rabbinic law; the shelf has no source saying whether a blind priest was ever allowed to serve at the altar, or whether Eli was exempt as high priest.",
    ),
]

# ================================================================= ahijah-duties
K["ahijah-duties"] = [
    item(
        "The 1915 encyclopaedia, in its entry on Shiloh, calls Ahijah 'the blind old prophet' whom Jeroboam's wife consulted in "
        "vain; in its entry on Ahijah it says the narrative gives the impression that he was 'a very old man' at the time.",
        "International Standard Bible Encyclopaedia (1915), entries 'Shiloh' and 'Ahijah', vols 4 and 1",
        [ev(I4, "the blind old prophet Ahijah was appealed to ni vain by Jeroboam's wife on behalf of her son"),
         ev(I1, "The narrative makes the impression that Ahijah was at this time a very old man (ver 4).")],
        "high",
        OLD_OCR + " ('ni vain' is the scan's error for 'in vain'.) The word 'blind' is the encyclopaedia's reading of 1 Kings 14:4.",
    ),
    item(
        "1 Kings 14:4-6, as printed in Henry: 'Ahijah could not see; for his eyes were set by reason of his age', and when he "
        "'heard the sound of her feet, as she came in at the door' he called Jeroboam's wife by name and asked why she pretended "
        "to be another woman.",
        HENRY + "1 Kings 14",
        [ev(H2, "But Ahijah could not see; for his eyes were set by reason of his age."),
         ev(H2, "And it was so, when Ahijah heard the sound of her feet, as she came in at the door, that he said, Come in, thou wife of Jeroboam; why feignest thou thyself to be another?")],
        "high",
        "The verses say he heard her feet; they also say the Lord had warned him ('God gave Ahijah notice', in Henry's words), so "
        "the recognising is not attributed to hearing alone.",
    ),
    item(
        "Henry says Ahijah 'lived obscurely and neglected in Shiloh, blind through age, yet still blest with the visions of the "
        "Almighty'. Henry adds that such visions 'need not bodily eyes, but are rather favoured by the want of them'.",
        HENRY + "1 Kings 14",
        [ev(H2, "blind through age, yet still blest with the visions of the Almighty, which need not bodily eyes, but are rather favoured by the want of them, the eyes of the mind being then most intent and least diverted.")],
        "medium",
        "This is Henry's devotional opinion, not something the text says. The idea that blindness sharpens inner vision can sound "
        "like romanticising; it is offered as how one commentator read the verse, not as a claim about blind people.",
    ),
    item(
        "Henry lists what the prophet did and did not do when the queen came: God told him she was coming in disguise and what "
        "to say; he 'had no regard' to her rank or to the 'handsome country present' she brought, since it was usual to bring "
        "prophets tokens of respect, which they accepted 'and yet were no hirelings'.",
        HENRY + "1 Kings 14",
        [ev(H2, "III. God gave Ahijah notice of the approach of Jeroboam's wife, and that she came in disguise, and full instructions what to say to her (v. 5)"),
         ev(H2, "It was usual for those who consulted prophets to bring them tokens of respect, which they accepted, and yet were no hirelings."),
         ev(H2, "She brought him a handsome country present (v. 3)")],
        "medium",
        "The custom of bringing a gift to a consulted prophet is Henry's statement; he cites 1 Samuel 9 and 1 Kings 14:3 only. How "
        "often Ahijah saw visitors, or who helped him receive them, is not recorded.",
    ),
    item(
        "Earlier, Ahijah met Jeroboam on the road and gave him a sign: he clad himself in a new garment and tore it into twelve "
        "pieces, giving Jeroboam ten. Henry notes the sign was probably Ahijah's own garment, and that prophets 'both true and "
        "false' used such acted signs.",
        HENRY + "1 Kings 11",
        [ev(H2, "The sign by which it was represented to him was the rending of a garment into twelve pieces, and giving him ten, v. 30, 31."),
         ev(H2, "The prophets, both true and false, used such signs, even in the New Testament, as Agabus, Acts xxi. 10, 11."),
         ev(H2, "He delivered his message to Jeroboam in the way, his servants being probably ordered to retire")],
        "high",
        "This is the earlier meeting (1 Kings 11:29-31), when nothing says Ahijah's sight had failed; the later one is chapter 14. "
        "How many years lay between them is not stated on the shelf.",
    ),
    item(
        "Easton's entry on Ahijah describes the prophet of Shiloh: two of his prophecies are on record (the rending of the ten "
        "tribes from Solomon, and the message to Jeroboam's wife about the death of the king's son and the fall of his house), "
        "and Jeroboam showed 'the high esteem in which he was held'.",
        "Easton's Bible Dictionary (1897), entry 'Ahijah'",
        [ev(EAS, "A prophet of Shiloh (1 Kings 11:29; 14:2), called the \"Shilonite,\" in the days of Rehoboam."),
         ev(EAS, "We have on record two of his remarkable prophecies, 1 Kings 11:31-39, announcing the rending of the ten tribes from Solomon;"),
         ev(EAS, "Jeroboam bears testimony to the high esteem in which he was held as a prophet of God")],
        "high",
        "Easton gives the two prophecies as his 'record'; whether he did anything else (taught, led a school, advised in other "
        "matters) is not said.",
    ),
    item(
        "Easton on 'prophet': a spokesman for God who speaks in God's name; foretelling was 'only an incidental part' of the office. "
        "The great task was 'to correct moral and religious abuses' and proclaim truths about God's character. From Samuel's time "
        "there were colleges, 'schools of the prophets', where young men were trained.",
        "Easton's Bible Dictionary (1897), entry 'Prophet'; Smith's Bible Dictionary (1884 edition), entry 'Prophet'",
        [ev(EAS, "Thus a prophet was a spokesman for God; he spake in God's name and by his authority (Ex. 7:1)."),
         ev(EAS, "The foretelling of future events was not a necessary but only an incidental part of the prophetic office."),
         ev(EAS, "Colleges, \"schools of the prophets\", were instituted for the training of prophets"),
         ev(SMI, "They were preachers of morals and of spiritual religion.")],
        "high",
        "General accounts of the prophetic office. Nothing on the shelf says Ahijah belonged to a school; he is called a prophet "
        "of Shiloh and a Shilonite only.",
    ),
    item(
        "Where prophets worked: Easton says prophets 'frequently delivered their messages' at the city gates. Henry, on 1 Kings 22, "
        "pictures the two kings sitting 'in their robes and chairs of state, in the gate of Samaria, ready to receive this poor "
        "prophet' Micaiah.",
        "Easton's Bible Dictionary (1897), entry 'Gate'; " + HENRY + "1 Kings 22",
        [ev(EAS, "At the gates prophets also frequently delivered their messages (Prov. 1:21; 8:3; Isa. 29:21; Jer. 17:19, 20; 26:10)."),
         ev(H2, "The two kings sat each in their robes and chairs of state, in the gate of Samaria, ready to receive this poor prophet")],
        "medium",
        "Neither passage is about Ahijah; they show the setting prophets spoke in. Ahijah is described receiving a visitor 'at the "
        "door' of his house (1 Kings 14:6) and meeting Jeroboam 'in the way' (1 Kings 11:29).",
    ),
    item(
        "Wikipedia notes that Ahijah is credited in 2 Chronicles with writing a book, 'the Prophecy of Ahijah the Shilonite', about "
        "Solomon's reign, which has not survived; and that the Midrash, from the description of him as 'extremely aged in Jeroboam's "
        "time', identified him with an earlier priest and gave him a very long life.",
        wsrc("Ahijah the Shilonite", "22 September 2026"),
        [ev(wk("Ahijah_the_Shilonite"), "authored a book, described as the \"Prophecy of Ahijah the Shilonite,\" which contained information about Solomon's reign."),
         ev(wk("Ahijah_the_Shilonite"), "The Midrash, basing itself on the fact that, according to II Chron. ix. 29, Ahijah is described as extremely aged in Jeroboam's time (I Kings, xiv. 4)")],
        "medium",
        "Raw wikitext. The rabbinic ages (hundreds of years) are tradition, not text. Whether a prophet who could not see would "
        "have dictated or recited such a book is not discussed on the shelf.",
    ),
]

# ================================================================= gate-life
K["gate-life"] = [
    item(
        "Edersheim's picture of an ancient fortified town: a low wall and a ditch, then the city wall and 'a massive gate, often "
        "covered with iron, and secured by strong bars and bolts', with the watch-tower above it. 'Within the gate' was the "
        "sheltered place where 'the elders' sat to discuss public affairs or the news of the day or transact business.",
        "Edersheim, Sketches of Jewish Social Life (1876), chapter 6, 'Jewish Homes' (the passage on town and country life)",
        [ev(EDS, "Crossing this moat, one would be at the city wall proper, and enter through a massive gate, often covered with iron, and secured by strong bars and bolts."),
         ev(EDS, "Above the gate rose the watch-tower."),
         ev(EDS, "Here grave citizens discussed public affairs or the news of the day, or transacted important business.")],
        "medium",
        "Edersheim (1876) draws on the Bible and on rabbinic writings of several centuries; his town is a composite. He also "
        "describes a Pharisee, an Essene and a publican in this scene in colourful terms that are not quoted.",
    ),
    item(
        "Beyond the gate, Edersheim says, 'large squares' opened where the streets met: country people hawked produce of "
        "field, orchard and dairy; foreign merchants and pedlars exposed their wares; the crowd was 'chattering, chaffing, "
        "good-humoured'. The streets were named after the trades or guilds, and workmen 'sat outside their shops' and "
        "'exchanged greetings or banter with the passers-by'.",
        "Edersheim, Sketches of Jewish Social Life (1876), chapter 6, 'Jewish Homes'",
        [ev(EDS, "The gates opened upon large squares, on which the various streets converged. Here was the busy scene of intercourse and trade."),
         ev(EDS, "The country-people stood or moved about, hawking the produce of field, orchard, and dairy; the foreign merchant or pedlar exposed his wares"),
         ev(EDS, "These streets are all named, mostly after the trades or guilds which have there their bazaars."),
         ev(EDS, "In these bazaars many of the workmen sat outside their shops, and, in the interval of labour, exchanged greetings or banter with the passers-by.")],
        "medium",
        "A nineteenth-century composite, as above. It is a description of towns of Jesus's day, not of Shiloh or the walled towns of the judges.",
    ),
    item(
        "Smith's on the gate: the gates were 'carefully guarded, and closed at nightfall', held 'chambers over the gateway', and "
        "had two-leaved doors 'plated with metal, closed with locks and fastened with metal bars'. They were places of public "
        "deliberation, justice, audience for kings and ambassadors, and public markets.",
        "Smith's Bible Dictionary (1884 edition), entry 'Gate'",
        [ev(SMI, "Places for public deliberation, administration of Justice, or of audience for kings and rulers or ambassadors."),
         ev(SMI, "Regarded therefore as positions of great importance, the gates of cities were carefully guarded, and closed at nightfall."),
         ev(SMI, "They contained chambers over the gateway."),
         ev(SMI, "The doors themselves of the larger gates mentioned in Scripture were two leaved, plated with metal, closed with locks and fastened with metal bars.")],
        "high",
        "The scripture references in Smith's are mostly to the monarchy and later; the town gate in the time of the judges "
        "was probably simpler. Smith's does not describe the guard's routine at closing time.",
    ),
    item(
        "The 1915 encyclopaedia on the build of the gate: doors on pivots set in sockets in sill and lintel; when shut, a bar "
        "'fitted into clamps on the doors and sockets in the post'; a tower to protect it, 'often... overhanging', sometimes "
        "an inner gate; and to 'possess the gate' was to possess the city.",
        "International Standard Bible Encyclopaedia (1915), entry 'Gate', vol 2",
        [ev(I2, "When closed, the doors were secured with a bar (usually of wood, Nah 3 13, but sometimes of metal, 1 K 4 13; Ps 107 16; Isa 45 2), which fitted into clamps on the doors and sockets in the post, uniting the whole firmly (Jgs 16 3)."),
         ev(I2, "it was protected by a tower (2 S 18 24.33; 2 Ch 14 7; 26 9), often, doubtless, overhanging and with flanking projec- tions. Sometimes an inner gate was added (2 S 18 24).")],
        "high",
        OLD_OCR + " The writer adds that 'Pal gives us little monumental detail', so this is partly reconstruction.",
    ),
    item(
        "Henry on Ruth 4: Boaz 'went up to the gate' as 'one having authority', perhaps as 'father of the city' who 'sat chief'. "
        "Though it was not court-day he gathered ten elders 'in the town-hall over the gate, where public business used to be "
        "transacted', and, being a judge, 'would not be judge in his own cause'. The sale was confirmed by a man drawing off "
        "his shoe and giving it to his neighbour.",
        HENRY + "Ruth 4",
        [ev(H2, "Perhaps he was father of the city, and sat chief; for he seems here to have gone up to the gate as one having authority, and not as a common person"),
         ev(H2, "he got ten men of the elders of the city to meet him in the town-hall over the gate, where public business used to be transacted, v. 2."),
         ev(H2, "Boaz, though a judge, would not be judge in his own cause, but desired the concurrence of other elders."),
         ev(H2, "a man plucked off his shoe, and gave it to his neighbour: and this was a testimony in Israel.")],
        "medium",
        "'Town-hall over the gate' and 'sat chief' are Henry's inferences from the text, which says only that Boaz sat at the gate "
        "and took ten elders. The seating arrangement beyond that is not given.",
    ),
    item(
        "Job 29:7-8 as printed in Henry (the passage where Job says he was 'eyes to the blind'): Job 'went out to the gate "
        "through the city' and 'prepared my seat in the street'; the young men 'saw me, and hid themselves: and the aged arose, "
        "and stood up'. The verses show who stood and who sat when a man of standing came to the gate.",
        HENRY + "Job 29",
        [ev(H3, "7 When I went out to the gate through the city, when I prepared my seat in the street! 8 The young men saw me, and hid themselves: and the aged arose, and stood up.")],
        "high",
        "The passage is also used on the law-and-life page for Job 29; it is repeated here for its gate scene. The verses are "
        "the King James text; they describe Job's own account of his past standing.",
    ),
    item(
        "The watchman and the porter: in 2 Samuel 18:24-27, as printed in Henry, David 'sat between the two gates' while the "
        "watchman 'went up to the roof over the gate unto the wall' and called out each runner he saw; he 'called unto the "
        "porter' and recognised the first runner by his running. Easton's 'Porter' says porters were gate-keepers, 4,000 of "
        "them Levites 'to take charge of the doors and gates of the temple'.",
        HENRY + "2 Samuel 18; Easton's Bible Dictionary (1897), entry 'Porter'",
        [ev(H2, "24 And David sat between the two gates: and the watchman went up to the roof over the gate unto the wall, and lifted up his eyes, and looked, and behold a man running alone."),
         ev(H2, "And the watchman said, Me thinketh the running of the foremost is like the running of Ahimaaz the son of Zadok."),
         ev(EAS, "A gate-keeper (2 Sam. 18:26; 2 Kings 7:10; 1 Chr. 9:21; 2 Chr. 8:14)."),
         ev(EAS, "to take charge of the doors and gates of the temple.")],
        "high",
        "The 1915 encyclopaedia (entry 'Watchman') says there were sentinels on the walls and also 'watchmen that go about the "
        "city', which 'points to some system of municipal police'; the shelf has no account of night patrols in an ordinary town.",
    ),
    item(
        "Easton on the elders and the gate: elders were 'local magistrates, administering justice'; 'at the gates of cities courts "
        "of justice were frequently held, and hence \"judges of the gate\" are spoken of'; 'criminals were punished without the "
        "gates'. Among the Arabs, Easton notes, the sheik ('the old man') is the highest authority in the tribe.",
        "Easton's Bible Dictionary (1897), entries 'Elder' and 'Gate'",
        [ev(EAS, "At the gates of cities courts of justice were frequently held, and hence \"judges of the gate\" are spoken of (Deut. 16:18; 17:8; 21:19; 25:6, 7, etc.)."),
         ev(EAS, "Criminals were punished without the gates (1 Kings 21:13; Acts 7:59)."),
         ev(EAS, "They appear as governors (Deut. 31:28), as local magistrates (16:18), administering justice (19:12)."),
         ev(EAS, "At the present day this is the case among the Arabs, where the sheik (i.e., \"the old man\") is the highest authority in the tribe.")],
        "high",
        "The 'present day' in Easton is 1897. How the elders took turns or who sat where is not described.",
    ),
    item(
        "Trade at the gate: Smith's lists 'public markets' among the gate's uses (2 Kings 7:1). Henry, on 2 Kings 7, explains "
        "Elisha's promise that corn would be sold 'in the gate of Samaria' as meaning the siege would end, 'for the gate of the "
        "city shall be opened, and the market shall be held there as formerly'. Easton adds that in early times markets were held "
        "at the gates, and that particular goods were sold in particular streets.",
        "Smith's Bible Dictionary (1884 edition), entry 'Gate'; " + HENRY + "2 Kings 7; Easton's Bible Dictionary (1897), entry 'Market-place'",
        [ev(SMI, "Public markets. (2 Kings 7:1)"),
         ev(H2, "that is, the siege shall be raised, for the gate of the city shall be opened, and the market shall be held there as formerly."),
         ev(EAS, "In early times markets were held at the gates of cities, where commodities were exposed for sale (2 Kings 7:18).")],
        "high",
        "This is one siege-time example; the shelf does not give prices, hours, or how buyers and sellers were arranged.",
    ),
    item(
        "Henry on Amos 5:10-12 makes the gate also the place of injustice: 'Thus they turn aside the poor in the gate, in the courts "
        "of justice, from their right', and they 'hate him that rebukes in the gate', 'in the places of concourse'.",
        HENRY + "Amos 5",
        [ev(H4, "Thus they turn aside the poor in the gate, in the courts of justice, from their right."),
         ev(H4, "They hate him that rebukes in the gate, in the gate of the Lord's house, or in their courts of justice, or in the places of concourse")],
        "high",
        "Henry is explaining the prophet's complaint (Amos 5:10, 12); it is not specifically about blind or disabled people, though "
        "'the poor' who could not press their own case would include them.",
    ),
]

# ================================================================= canes-and-staffs
K["canes-and-staffs"] = [
    item(
        "Greek tradition: the myth of Tiresias gives the blind prophet a staff. Wikipedia's account of Pherecydes' version has "
        "Athena grant him 'a staff of cornel-wood, \"wherewith he walked like those who see\"'. Levy (1872) reads this as proof "
        "that the ancients were struck by blind people walking alone 'aided only by a stick', and made it 'a miraculous gift of the gods'.",
        wsrc("Tiresias", "2 October 2026") + "; Levy, Blindness and the Blind (1872), chapter 'On the Blind Walking Alone, and of Guides'",
        [ev(wk("Tiresias"), "granted him a staff of [[Cornus mas|cornel-wood]], \"wherewith he walked like those who see\""),
         ev(LEV, "The ancients were so much struck with the circumstance of the blind walking alone, aided only by a stick, that, in their usual way, they made it a miraculous gift of the gods")],
        "medium",
        "A myth, not a record of practice; it is as early as the shelf gets for a staff in a blind person's hand, but it is Greek, "
        "and Wikipedia cites the mythographer Pseudo-Apollodorus (a later retelling) for the staff. Levy's inference from the myth "
        "is his own. Nothing on the shelf shows how ancient Israelites who were blind moved about.",
    ),
    item(
        "Levy (1872) argues that blind people walking alone in the streets was 'by no means uncommon "
        "250 years ago' and says Leviticus 19:14 and Deuteronomy 27:18 'show the special care of God'. (His reference 'Deuteronomy xvii. 18' "
        "is a slip for 27:18.) He says a blind walker needs a light stick that does not flex.",
        "Levy, Blindness and the Blind (1872), chapter 'On the Blind Walking Alone, and of Guides'",
        [ev(LEV, "The above graphic lines show that the phenomenon of the blind walking alone in the streets was by no means uncommon 250 years ago"),
         ev(LEV, "These passages forcibly show the special care of God"),
         ev(LEV, "One of the greatest aids to him who would walk by himself is a stick ; this should be light and not elastic, in order that correct impressions may be transmitted from the objects with which it comes in contact to the hand of the user.")],
        "medium",
        "Levy's reading of Leviticus 19:14 as proof that blind people in the law's time walked abroad without a guide is an "
        "inference, not something the verse says. His text elsewhere is patronising about some sighted helpers and some groups; "
        "only the practical points are used.",
    ),
    item(
        "Levy gives a 1872 teaching of stick technique: wave the stick 'alternately from right to left to correspond with the "
        "movements of the feet', and on coming to a step 'its depth or height should be gauged with the stick, and this operation "
        "should be rigidly carried out, as the life of the individual may depend on the result'.",
        "Levy, Blindness and the Blind (1872), chapter 'On the Blind Walking Alone, and of Guides'",
        [ev(LEV, "When stepping, the stick should be waved alternately from right to left to correspond with the movements of the feet"),
         ev(LEV, "On coming to a step, its depth or height should be gauged with the stick, and this operation should be rigidly carried out, as the life of the individual may depend on the result.")],
        "medium",
        "A 19th-century manual, not evidence for ancient practice. It is useful as a description of what a stick does on steps and "
        "uneven ground, which Brian can compare with his own cane technique.",
    ),
    item(
        "James Wilson, blind from infancy and writing in 1838, describes his own staff: 'A blind person always inclines to the hand "
        "in which his staff is carried, and this often has a tendency to lead him astray, when he travels on a road with which he is "
        "unacquainted.' He tells of 'groping about with my staff' at a fork in the road when a man stopped him two steps from a "
        "well 'eighty feet deep, and half full of water'.",
        "Wilson, Biography of the Blind (1838), the author's own life",
        [ev(WIL, "A blind person always inclines to the hand in which his staff is carried, and this often has a tendency to lead him astray, when he travels on a road with"),
         ev(WIL, "I was groping about with my staff to ascertain the turn of the road, when a man bawled out to me, to stand still, and not move a single step."),
         ev(WIL, "told me, that two steps more would have hurried me into a well eighty feet deep, and half full of water.")],
        "high",
        "A first-person account by a blind man in Ulster (the text names Ballymena and Broughshane); the habit he describes (veering to the stick hand on "
        "unfamiliar ground) is the kind of detail that carries across centuries but is not evidence about the first century.",
    ),
    item(
        "Wilson also writes of using his staff to cross a stream: 'I groped with my staff for the first stepping stone, and getting "
        "on it, I took hold of his hand, and bade him put his foot where mine was'; the sighted soldier he led across remarked that "
        "Wilson's eyes were better than his. Wilson quotes Dr. Bew on the blind road-builder John Metcalf: 'With the assistance only of a "
        "long staff, I have several times met this man traversing the road, ascending precipices'.",
        "Wilson, Biography of the Blind (1838), the author's own life; and the life of Metcalf",
        [ev(WIL, "I groped with my staff for the first stepping stone, and getting on it, I took hold of his hand, and bade him put his foot where mine was"),
         ev(WIL, "only of a long staff, I have several times met this man traversing the road, ascending precipices.")],
        "high",
        "Both are 18th-19th century accounts. The Metcalf remark is a sighted observer's testimony reported by Wilson.",
    ),
    item(
        "A rule that may bear on Brian's question: Edersheim, citing rabbinic rules, says one 'must not enter' the Temple 'carrying a "
        "staff, nor with shoes, nor even dust on the feet, nor with scrip or purse', and that Jesus's order to the Twelve not to take a "
        "staff corresponds to 'the Rabbinic injunction not to enter the Temple-precincts with staff, shoes'. The rule is stated for "
        "everyone; the shelf does not say whether a blind person's staff or guide was exempt.",
        "Edersheim, The Life and Times of Jesus the Messiah (1883), chapter X ('The Synagogue at Nazareth') and chapter XXVII ('Second Visit to Nazareth - the Mission of the Twelve')",
        [ev(EDL, "such as, that we must not enter it carrying a staff, nor with shoes, nor even dust on the feet, nor with scrip or purse, do not apply to the Synagogue"),
         ev(EDL, "exactly correspond to the Rabbinic injunction not to enter the Temple-precincts with staff, shoes")],
        "medium",
        "Edersheim gives the rule as rabbinic and cites it only by footnote; the shelf does not hold the Mishnah itself. A blind person's exemption "
        "(if any) is not in these sources, so none is claimed. Edersheim also says the rule did not apply to synagogues.",
    ),
    item(
        "Edersheim, on Sabbath law, says anything forming part of a person's ordinary dress might be worn on the Sabbath and that it "
        "'was also allowed to go about on crutches, or with a wooden leg'. He also says a staff might have 'a secret receptacle at "
        "the top... to hold valuables, or, in the case of the poor, water' (Kelim 17:16), which shows the staff was ordinary equipment.",
        "Edersheim, The Life and Times of Jesus the Messiah (1883), Appendix XVII (the Sabbath law in the Mishnah) and chapter XXVII (the Mission of the Twelve)",
        [ev(EDL, "It was also allowed to go about on crutches, or with a wooden leg, and children might have bells on their dresses;"),
         ev(EDL, "Sometimes there was a secret receptacle at the top of the staff to hold valuables, or, in the case of the poor, water (Kel. xvii. 16).")],
        "medium",
        "Edersheim does not mention canes for the blind; the crutch rule is the nearest neighbour, and whether a blind person's "
        "staff counted as dress or as a burden on the Sabbath is not answered on the shelf.",
    ),
    item(
        "Staffs in the Bible, as the verses stand in Henry: Jacob, 'with my staff I passed over this Jordan'; Israel ate the Passover "
        "with 'your staff in your hand'; and Zechariah promises 'old men and old women' in Jerusalem's streets, 'every man with his "
        "staff in his hand for very age'. The 1915 encyclopaedia adds that Hebrew has several words for 'rod' and 'staff' and that "
        "'in Ps 23 4 ... shebhet is the shepherd's rod, figurative of Divine guidance and care'.",
        HENRY + "Genesis 32, Exodus 12 and Zechariah 8; International Standard Bible Encyclopaedia (1915), entries 'Rod' and 'Staff', vols 4 and 5",
        [ev(H1, "for with my staff I passed over this Jordan; and now I am become two bands."),
         ev(H1, "with your loins girded, your shoes on your feet, and your staff in your hand;"),
         ev(H4, "There shall yet old men and old women dwell in the streets of Jerusalem, and every man with his staff in his hand for very age."),
         ev(I4, "shebhet is the shepherd's rod, figurative of Divine guidance and care.")],
        "high",
        "None of these verses is about a blind person. They show that a staff was ordinary equipment for travel and old age. "
        + OLD_OCR,
    ),
    item(
        "Guides in the Bible: Samson 'said unto the lad that held him by the hand, Suffer me that I may feel the pillars' (Judges "
        "16:26); of Elymas, 'he went about seeking some to lead him by the hand' (Acts 13:11); and Saul, struck blind, was led by the "
        "hand into Damascus, as Henry's note on Acts 9 puts it. Jesus 'took the blind man by the hand, and led him out of the town' "
        "(Mark 8:23).",
        HENRY + "Judges 16, Acts 9, Acts 13 and Mark 8",
        [ev(H2, "26 And Samson said unto the lad that held him by the hand, Suffer me that I may feel the pillars whereupon the house standeth, that I may lean upon them."),
         ev(H6, "and he went about seeking some to lead him by the hand."),
         ev(H6, "They led him by the hand into Damascus"),
         ev(H5, "And he took the blind man by the hand, and led him out of the town;")],
        "high",
        "The verses show a guide by the hand, not a staff; they are the nearest biblical evidence for how a newly or long-blind "
        "person was moved about. Where the verses do not mention a cane or staff, none is assumed.",
    ),
    item(
        "Wikipedia's 'White cane' says in one sentence that 'Blind people have used canes as mobility tools for centuries', "
        "and then gives the modern history: James Biggs painted his walking stick white in 1921; Peoria passed the first white-cane "
        "ordinance in December 1930; France followed in 1931; Richard Hoover developed the long-cane technique in 1944.",
        wsrc("White cane", "25 September 2026"),
        [ev(wk("White_cane"), "Blind people have used canes as mobility tools for centuries."),
         ev(wk("White_cane"), "painted his walking stick white to be more easily visible."),
         ev(wk("White_cane"), "The first special white cane ordinance was passed in December 1930 in [[Peoria, Illinois]]")],
        "medium",
        "The 'centuries' sentence is supported only by a link to a page on the history of orientation and mobility as a profession; "
        "it gives no date or place. The Wikipedia articles 'Walking stick' and 'Staff of office' on the shelf say nothing about "
        "the Bible or ancient practice and are not used.",
    ),
]

# ================================================================= jerusalem-layout
K["jerusalem-layout"] = [
    item(
        "Josephus, Wars V.4.1: Jerusalem was built on two hills 'opposite to one another' with 'a valley to divide them asunder', "
        "the corresponding rows of houses on both hills ending at it. The Valley of the Cheesemongers 'extended as far as Siloam'. "
        "The Hasmoneans filled in part of the other valley to 'join the city to the temple' and cut down the height of Acra.",
        "Josephus (Whiston translation), Wars of the Jews, Book V, chapter 4, section 1",
        [ev(JW, "The city was built upon two hills, which are opposite to one another, and have a valley to divide them asunder; at which valley the corresponding rows of houses on both hills end."),
         ev(JW, "However, in those times when the Asamoneans reigned, they filled up that valley with earth, and had a mind to join the city to the temple."),
         ev(JW, "Now the Valley of the Cheesemongers, as it was called, and was that which we told you before distinguished the hill of the upper city from that of the lower, extended as far as Siloam")],
        "high",
        "Whiston's 1737 translation; Josephus wrote c. 75 CE, after the 70 CE destruction, from memory and from earlier "
        "sources. The 'valley' he calls the Tyropoeon is the central valley of the city.",
    ),
    item(
        "Josephus, Antiquities XV.11.5, on the west side of Herod's Temple: four gates; the first 'went to a passage over the "
        "intermediate valley' (to the king's palace); the last 'led to the other city, where the road descended down into the "
        "valley by a great number of steps, and thence up again by the ascent'. The south royal cloister stood over a valley so "
        "deep that a person looking down 'would be giddy'.",
        "Josephus (Whiston translation), Antiquities of the Jews, Book XV, chapter 11, section 5",
        [ev(JA, "the first led to the king's palace, and went to a passage over the intermediate valley; two more led to the suburbs of the city; and the last led to the other city, where the road descended down into the valley by a great number of steps, and thence up again by the ascent"),
         ev(JA, "while the valley was very deep, and its bottom could not be seen, if you looked from above into the depth, this further vastly high elevation of the cloister stood upon that height, insomuch that if any one looked down from the top of the battlements, or down both those altitudes, he would be giddy")],
        "high",
        "The shelf's translation is Whiston's; its numbers are Josephus's own and are not checked against excavation here.",
    ),
    item(
        "Josephus, Wars V.5: the Temple courts were reached by successive flights of steps. A stone partition three cubits high; the "
        "second court 'ascended to by fourteen steps from the first court'; further steps 'each of five cubits' led to the gates; "
        "the eastern gate had 'fifteen steps' from the court of women; the holy house was 'ascended to by twelve steps'. The "
        "outer cloisters were thirty cubits broad and the compass of the outer court six furlongs.",
        "Josephus (Whiston translation), Wars of the Jews, Book V, chapter 5, sections 1-4",
        [ev(JW, "The cloisters [of the outmost court] were in breadth thirty cubits, while the entire compass of it was by measure six furlongs, including the tower of Antonia;"),
         ev(JW, "and was ascended to by fourteen steps from the first court."),
         ev(JW, "Now there were fifteen steps, which led away from the wall of the court of the women to this greater gate;"),
         ev(JW, "it was ascended to by twelve steps;")],
        "medium",
        "Whiston's text says 'fourteen steps' and, a few lines later, 'thirteen steps' for the same stair, and his footnote "
        "notes the difficulty; so counts are uncertain. Josephus's cubit is not defined on the shelf (about 18 inches is the usual "
        "figure, but that is not from the shelf).",
    ),
    item(
        "Easton on the Tyropoeon Valley: the valley or ravine that separated Mount Moriah from Mount Zion, now 'filled up with a vast "
        "accumulation of rubbish', was 'spanned by bridges', the most noted 'Zion Bridge'; the western wall of the temple area 'rose "
        "up from the bottom of this valley to the height of 84 feet'. In the entry 'Market-place' Easton adds that sale of particular "
        "articles seems to have been confined to certain streets.",
        "Easton's Bible Dictionary (1897), entries 'Tyropoeon Valley' and 'Market-place'; Wikipedia, 'Tyropoeon Valley', revision of 19 April 2026 (CC BY-SA 4.0)",
        [ev(EAS, "the name given by Josephus the historian to the valley or rugged ravine which in ancient times separated Mount Moriah from Mount Zion."),
         ev(EAS, "was spanned by bridges, the most noted of which was Zion Bridge, which was probably the ordinary means of communication between the royal palace on Zion and the temple."),
         ev(EAS, "The western wall of the temple area rose up from the bottom of this valley to the height of 84 feet"),
         ev(wk("Tyropoeon_Valley"), "was spanned by bridges, the most noted of which was [[Zion]] Bridge")],
        "medium",
        "Easton (1897) relies on Robinson and Warren's excavations; the 84-foot figure and the 'Zion Bridge' are of the Herodian "
        "temple wall. The Wikipedia quotation is a fragment (the article repeats Easton).",
    ),
    item(
        "Wikipedia's 'Stepped street (Jerusalem)': a street from Jerusalem's southern gates, by the Pool of Siloam, up to the Temple "
        "Mount's south-west corner, 'eight meters wide' and 600 metres long, paved 'in the pattern of two steps followed by a long "
        "landing, followed by two more steps and another landing'. "
        "It was built at the earliest in the 30s CE; the latest coin under the pavement dates to 30-31 CE.",
        wsrc("Stepped street (Jerusalem)", "16 August 2026"),
        [ev(wk("Stepped_street_Jerusalem"), "street connecting the [[Temple Mount]] from its southwestern corner, to [[Jerusalem]]'s southern gates of the time via the [[Pool of Siloam]]."),
         ev(wk("Stepped_street_Jerusalem"), "The stepped street was built at the earliest during the 30s CE, with the latest coin found under the pavement dating to 30–31 CE"),
         ev(wk("Stepped_street_Jerusalem"), "The ancient path was improved and paved in large, well-cut stone in the pattern of two steps followed by a long landing, followed by two more steps and another landing. The street was eight meters wide and its length from the Pool of Siloam to the Temple Mount is 600 meters."),
         ev(wk("Stepped_street_Jerusalem"), "pilgrims used the Pool of Siloam as a [[mikveh]] for ritual purification before walking up the street to the [[Second Temple|Temple]].")],
        "medium",
        "The street may date from after the likely year of John 9 (the article gives 30s CE as the earliest, and a proposal that "
        "Pilate built it). Whether it was there when the man born blind went to Siloam is therefore uncertain. Yoel Elitzur argues "
        "that the pool was a Roman public swimming pool, not a mikveh; the article reports both views. It also describes the "
        "politics of the excavation (the City of David / Elad), which is not repeated here.",
    ),
    item(
        "Wikipedia 'Pool of Siloam': the pool is 'the lowest place in altitude within the historical city', about 625 m above sea "
        "level; the way up to the Temple Mount was a climb of 115 m over about 634 m. The pool found in later excavations was about "
        "225 feet wide with steps on at least three sides, 'three sets of five steps' with platforms. Older excavations "
        "found a stairway of 34 rock-hewn steps west of the pool, tapering from 27 ft to 22 ft in width.",
        wsrc("Pool of Siloam", "20 June 2026"),
        [ev(wk("Pool_of_Siloam"), "Today, the Pool of Siloam is the lowest place in altitude within the historical city of Jerusalem"),
         ev(wk("Pool_of_Siloam"), "The ascent from it unto the [[Temple Mount]] meant a [[Grade (slope)|gradient]] of {{convert|115|m|ft|}} in altitude at a linear distance of about {{convert|634|m}}"),
         ev(wk("Pool_of_Siloam"), "The excavations also revealed that the pool was {{convert|225|ft|abbr=on}} wide, and that steps existed on at least three sides of the pool."),
         ev(wk("Pool_of_Siloam"), "There are three sets of five steps, two leading to a platform, before the bottom is reached"),
         ev(wk("Pool_of_Siloam"), "noted that there was a stairway of 34 rock-hewn steps to the west of the Pool of Siloam"),
         ev(wk("Pool_of_Siloam"), "The breadth of the steps varies from {{convert|27|ft|abbr=on}} at the top to {{convert|22|ft|abbr=on}} at the bottom."),
         ev(wk("Pool_of_Siloam"), "Until the discovery of the Second Temple pool, this pool was wrongly thought to be the one described in the [[New Testament]] and Second Temple sources.")],
        "medium",
        "Raw wikitext: the two '{{convert...}}' quotations mean 115 metres and 634 metres, and 225 feet. The article says a smaller "
        "Byzantine-era pool nearby was 'wrongly thought' until the Second Temple pool was found to be the one in the New Testament; so "
        "figures in older dictionaries (Easton's 53-foot pool) belong to the smaller later pool.",
    ),
    item(
        "Wikipedia 'Robinson's Arch': 'a monumental staircase carried by an unusually wide stone arch' at the south-west corner "
        "of the Temple Mount, built under Herod; it 'carried traffic up from ancient Jerusalem's Lower Market area and over the "
        "Tyropoeon street to the Royal Stoa'. The width of the stepped street 'approximates that of a modern four-lane highway'. "
        "The arch spanned 15 m, was 15.2 m wide and rose about 17 m above the street below; the stair was more than 35 m long.",
        wsrc("Robinson's Arch", "12 August 2026"),
        [ev(wk("Robinsons_Arch"), "was a monumental staircase carried by an unusually wide stone arch, which once stood at the southwestern corner of the [[Temple Mount]]."),
         ev(wk("Robinsons_Arch"), "It carried traffic up from ancient [[Jerusalem]]'s Lower Market area and over the Tyropoeon street to the [[Royal Stoa (Jerusalem)|Royal Stoa]] complex on the esplanade of the Mount."),
         ev(wk("Robinsons_Arch"), "It was built as part of the expansion of the [[Second Temple]] initiated by [[Herod the Great]] at the end of the 1st century BCE."),
         ev(wk("Robinsons_Arch"), "The heavy public traffic to and from this edifice accounts for the width of the stepped street, which approximates that of a modern four-lane highway."),
         ev(wk("Robinsons_Arch"), "Upon completion the arch spanned {{convert|15|m|ft}} and had a width of {{convert|15.2|m|ft}}."),
         ev(wk("Robinsons_Arch"), "The stepped street it bore over a series of seven additional arches was more than {{convert|35|m|ft}} in length."),
         ev(wk("Robinsons_Arch"), "soaring some {{convert|17|m|ft}} over the ancient Tyropoeon street")],
        "medium",
        "Raw wikitext. The article reports recent finds that the arch 'may not have been completed until at least 20 years after "
        "[Herod's] death', and that it was destroyed in 70 CE, so it stood through Jesus's lifetime only in part or at the end of it. "
        "Josephus says the older (Hasmonean) bridge crossed the valley; the 1915 encyclopaedia gives the bridge span as 50 ft.",
    ),
    item(
        "The 1915 encyclopaedia on the lie of the land: the city 'must ever have consisted, as it does today, of houses terraced on steep "
        "slopes with stairways for streets'; a city gate found in the excavated southern wall near the mouth of the Tyropoeon gave onto "
        "'the great main street running down the Tyropceon, underneath which ran a great rock-cut drain'; the approach to the Virgin's "
        "Spring is 'down two flights of steps', of ten and fourteen.",
        "International Standard Bible Encyclopaedia (1915), entry 'Jerusalem', vol 3",
        [ev(I3, "The city covering so hilly a site as this must ever have consisted, as it does today, of houses terraced on steep slope's with stairways for streets."),
         ev(I3, "The gate gave access to the great main street running down the Tyropceon, underneath which ran a great rock-cut drain, which probably traversed the whole central valley of the city."),
         ev(I3, "The approach to the spring is down two flights of steps, an upper of 10 leading to a small level platform, covered by a modern arch, and a lower, narrower flight of 14 steps, which ends at the mouth of a small cave.")],
        "medium",
        OLD_OCR + " 'As it does today' means Jerusalem in about 1915, so the staircase streets are inferred for earlier times; the gate "
        "and main street refer to the excavations of the early 1900s.",
    ),
    item(
        "Edersheim's walk through Herodian Jerusalem: the Tyropoeon 'cleft', the Lower City as 'the business-quarter with its markets, "
        "bazaars, and streets of trades and guilds', the Upper City of palaces across the great bridge, 'narrow streets in the "
        "business quarters' with shops next to mansions, and craftsmen at work outside their shops: 'the shoemaker hammering "
        "his sandals, the tailor plying his needle'. Jerusalem covered about 300 acres at its greatest.",
        "Edersheim, The Life and Times of Jesus the Messiah (1883), chapter I ('In Jerusalem when Herod reigned')",
        [ev(EDL, "If the Lower City and suburb form the business-quarter with its markets bazaars, and streets of trades and guilds, the Upper City' is that of palaces."),
         ev(EDL, "As of old there were still the same narrow streets in the business quarters; but in close contiguity to bazaars and shops rose stately mansions of wealthy merchants, and palaces of princes."),
         ev(EDL, "Outside their shops in the streets, or at least in sight of the passers, and within reach of their talk, was the shoemaker hammering his sandals, the tailor plying his needle, the carpenter, or the worker in iron and brass.")],
        "medium",
        "Edersheim's reconstruction from Josephus and rabbinic writing; it is 19th-century scholarship and some details (the 'great "
        "bridge' as a single structure) have been revised by excavation. The quotations keep stray footnote marks (' and [542]).",
    ),
    item(
        "Wikipedia 'Temple Mount': Herod's retaining walls enlarged the natural plateau into a platform measuring 488 m on the west, "
        "470 m on the east, 315 m on the north and 280 m on the south; the Mount rises above the Kidron valley to the east and "
        "the Tyropoeon to the west. A 'monumental street... took pilgrims from the city's southern gate via the Tyropoeon Valley to "
        "the western side of the Temple Mount'. 'Huldah Gates': the southern gates gave access 'by means of underground vaulted ramps'.",
        wsrc("Temple Mount", "24 September 2026") + "; " + wsrc("Huldah Gates", "17 July 2026"),
        [ev(wk("Temple_Mount"), "Rising above the [[Kidron Valley]] to the east and [[Tyropoeon Valley]] to the west,"),
         ev(wk("Temple_Mount"), "In around 19&nbsp;BCE, [[Herod the Great]] extended the Mount's natural [[plateau]] by enclosing the area with four massive retaining walls and filling the voids."),
         ev(wk("Temple_Mount"), "The [[Trapezoid|trapezium]] shaped platform measures {{cvt|488|m}} along the west, {{cvt|470|m}} along the east, {{cvt|315|m}} along the north and {{cvt|280|m}} along the south"),
         ev(wk("Temple_Mount"), "took pilgrims from the city's southern gate via the Tyropoeon Valley to the western side of the Temple Mount."),
         ev(wk("Huldah_Gates"), "Both sets of gates were set into the [[Southern Wall]] of the Temple compound and gave access to the Temple Mount esplanade by means of underground vaulted ramps.")],
        "medium",
        "Raw wikitext ('{{cvt|488|m}}' means 488 metres). The Huldah Gates article says the surviving gates are Herodian and later "
        "and were walled up in the Middle Ages. Josephus (Antiquities XV.11.5) is the only source on the shelf for the west-side gates.",
    ),
]

# ================================================================= tent-life
K["tent-life"] = [
    item(
        "The 1915 encyclopaedia on the Bedouin tent (the fullest description on the shelf): black goats'-hair cloth sewed "
        "into one large piece, held up by poles 'at intervals', 'stretched over these poles by ropes of goats' hair or hemp... "
        "fastened to hard-wood pins driven into the ground'. 'A large wooden mallet for driving the pegs is part of the regular camp "
        "equipment.' The entrance is a corner of matting turned back; in summer the walls are mostly removed.",
        "International Standard Bible Encyclopaedia (1915), entry 'Tent', vol 5",
        [ev(I5, "Poles are placed under this covering at intervals to hold it from the ground, and it is stretched over these poles by ropes of goats' hair or hemp (cf Job 4 21; Isa 54 2; Jer 10 20),"),
         ev(I5, "hard-wood pins driven into the ground"),
         ev(I5, "A large wooden mallet for driving the pegs is part of the regular camp equipment"),
         ev(I5, "turned back to form the door of the tent (Gen 18 1). In the summer time the walls are mostly removed.")],
        "high",
        OLD_OCR + " It describes the Arab tent of c. 1900 and says there is 'little doubt about the antiquity' of the pattern; "
        "nothing in it speaks of blind or disabled people.",
    ),
    item(
        "The same entry on what is inside: straw mats, goats'-hair or woollen rugs on the floor of the poorer tents; food in goats'-hair "
        "bags and liquids in skins; a small set of copper cooking vessels; a coffee set. 'It is the women's duty to pitch the tents.' "
        "A sheikh has 'several tents', one for himself and guests, others for the women and servants and for animals.",
        "International Standard Bible Encyclopaedia (1915), entry 'Tent', vol 5",
        [ev(I5, "Straw mats, goats' hair or woolen rugs (cf Jgs 4 18), more or less elaborate as the taste and means of the family allow, are the usual coverings for the tent floor."),
         ev(I5, "It is the women's duty to pitch the tents."),
         ev(I5, "A sheikh or chief has several tents, one for himself and"),
         ev(I5, "and still others for his animals")],
        "medium",
        OLD_OCR + " The sentence on the sheikh's tents runs across a page break in the scan, hence the two quotations.",
    ),
    item(
        "Wikipedia 'Bedouin' says Bedouin 'lived in black goat-hair tents called bayt al-shar, divided by cloth curtains into "
        "rug-floor areas for males, family and cooking', and says they travelled 'in groups of fifty to a hundred'; among their values it lists 'courage, hospitality, loyalty to family and "
        "pride of ancestry'.",
        wsrc("Bedouin", "27 September 2026"),
        [ev(wk("Bedouin"), "They lived in black goat-hair tents called bayt al-shar, divided by cloth curtains into rug-floor areas for males, family and cooking."),
         ev(wk("Bedouin"), "would travel in family and tribal groups, across the [[Arabian Peninsula]] in groups of fifty to a hundred."),
         ev(wk("Bedouin"), "The Bedouins' ethos comprises courage, hospitality, loyalty to family and pride of ancestry.")],
        "medium",
        "The article describes Bedouin of the Arabian Peninsula in modern times (the passage is attributed in the article to Ali Al-Naimi's "
        "account of the Arabian Peninsula, and is about the early twentieth century); it is only analogy for the tents of Israel's early centuries. It says nothing about blind "
        "or disabled members of a camp.",
    ),
    item(
        "Easton on tents in Israel's life: the patriarchs were 'dwellers in tents' and 'during their wilderness wanderings all Israel "
        "dwelt in tents'; 'tents have always occupied a prominent place in Eastern life'. His entry 'Camp' puts the camp of the "
        "twelve tribes at 'about 3 square miles' in area.",
        "Easton's Bible Dictionary (1897), entries 'Tent' and 'Camp'",
        [ev(EAS, "The patriarchs were \"dwellers in tents\" (Gen. 9:21, 27; 12:8; 13:12; 26:17); and during their wilderness wanderings all Israel dwelt in tents (Ex. 16:16; Deut. 33:18; Josh. 7:24)."),
         ev(EAS, "Tents have always occupied a prominent place in Eastern life"),
         ev(EAS, "The area of the camp would be in all about 3 square miles.")],
        "high",
        "The camp figure is Easton's estimate from Numbers 2; the shelf gives no way to check it. Nothing about how a blind "
        "person got about it is recorded.",
    ),
    item(
        "Henry on Genesis 18:1: Abraham 'sat in the tent-door, in the heat of the day; not so much to repose or divert himself as to "
        "seek an opportunity of doing good, by giving entertainment to strangers and travellers, there being perhaps no inns to "
        "accommodate them'.",
        HENRY + "Genesis 18",
        [ev(H1, "He sat in the tent-door, in the heat of the day; not so much to repose or divert himself as to seek an opportunity of doing good, by giving entertainment to strangers and travellers, there being perhaps no inns to accommodate them.")],
        "medium",
        "Henry's reading of why Abraham sat there. It is a description of the household's hospitality at midday, not of disability. "
        "Isaac, who is blind in Genesis 27, is in his tent and receives visitors; the shelf has no further description.",
    ),
    item(
        "Eye disease in that life: the 1915 encyclopaedia says 'the types of disease which are referred to in the Bible are those that "
        "still prevail', and lists 'ophthalmia and skin diseases' among 'the commonest'. Smith's says that in Egypt the common flies "
        "are 'the great instrument of spreading the well-known ophthalmia, which is conveyed from one individual to another by "
        "these dreadful pests'.",
        "International Standard Bible Encyclopaedia (1915), entry 'Disease', vol 2; Smith's Bible Dictionary (1884 edition), entry 'Fly, Flies'",
        [ev(I2, "The types of disease which are referred to in the Bible are those that still prevail."),
         ev(I2, "ophthalmia and skin diseases are among the commonest and will be described under their several names."),
         ev(SMI, "and are the great instrument of spreading the well-known ophthalmia, which is conveyed from one individual to another by these dreadful pests.")],
        "medium",
        "'Ophthalmia' is a broad old term (inflammation of the eye); the shelf does not say which diseases were meant in the Bible. "
        + OLD_OCR,
    ),
    item(
        "Wikipedia 'Trachoma' (modern medical text): the infection can spread 'through clothing or flies that have come into contact "
        "with an affected person's eyes or nose'; 'poor sanitation, crowded living conditions, and insufficient clean water' increase "
        "spread; and 'blinding endemic trachoma results from multiple episodes of reinfection'. It adds that trachoma became a problem "
        "'as people moved into crowded settlements or towns with poor hygiene'.",
        wsrc("Trachoma", "18 September 2026"),
        [ev(wk("Trachoma"), "Indirect contact includes through clothing or flies that have come into contact with an affected person's eyes or nose."),
         ev(wk("Trachoma"), "Poor sanitation, crowded living conditions, and insufficient clean water and toilets also increase the spread."),
         ev(wk("Trachoma"), "Blinding endemic trachoma results from multiple episodes of reinfection that maintains the intense inflammation in the conjunctiva."),
         ev(wk("Trachoma"), "Trachoma became a problem as people moved into crowded settlements or towns with poor hygiene.")],
        "medium",
        "A modern medical description, not evidence that trachoma was the cause of blindness in the Bible. The article's own date for "
        "trachoma in Egypt ('as early as 15 BCE') looks like an error and is not used. The shelf has nothing saying whether camp "
        "or town life carried more risk in the ancient world.",
    ),
    item(
        "Dust and sand: Easton says 'storms of sand and dust sometimes overtake Eastern travellers. They are very dreadful, many "
        "perishing under them'. Smith's, on the plague of darkness, describes the desert sandstorm that 'often' causes 'the darkness of "
        "twilight' and the Khamaseen wind that 'carries so much sand with it that it produces the appearance of a yellow fog'.",
        "Easton's Bible Dictionary (1897), entry 'Dust'; Smith's Bible Dictionary (1884 edition), entry 'Plagues, The Ten'",
        [ev(EAS, "Storms of sand and dust sometimes overtake Eastern travellers. They are very dreadful, many perishing under them."),
         ev(SMI, "The former is a sand-storm which occurs in the desert, seldom lasting more than a quarter of an hour or twenty minutes, but for the time often causing the darkness of twilight, and affecting man and beast."),
         ev(SMI, "carries so much sand with it that it produces the appearance of a yellow fog.")],
        "medium",
        "Neither entry mentions eyes or blindness. The 'darkness' in Smith's is the sandstorm explanation of the ninth plague, one "
        "view among others.",
    ),
    item(
        "Levy (1872) on causes of blindness: 'exposure to the sun, and sudden changes of weather, are among the most usual productive "
        "agents' of ophthalmia, and Arabia's blind he reckons at 'one in every 400 of the inhabitants'; he also mentions 'a "
        "particular kind of fly in the country which is specially inimical to sight'.",
        "Levy, Blindness and the Blind (1872), chapters 'The Causes of Blindness' and 'The Blind of Various Countries' (Arabia)",
        [ev(LEV, "exposure to the sun, and sudden changes of weather, are among the most usual productive agents of this disease."),
         ev(LEV, "placing the ratio of the blind as one in every 400 of the inhabitants"),
         ev(LEV, "there is a particular kind of fly in the country which is specially inimical to sight")],
        "medium",
        "Levy's ratios are his own estimates from travellers' remarks, not a census, and describe the nineteenth century; they "
        "should not be used as an ancient figure. Levy is useful mainly for what he thought the causes were.",
    ),
    item(
        "A caravan story from 1656, retold by Levy: Casaubon, quoting Leo Africanus, writes of 'a blind man that was a guide to "
        "certain merchants travelling through the deserts of Arabia', who 'rode upon a camel, and led his company, not by his eyes, "
        "which he had not, but by his smell'.",
        "Levy, Blindness and the Blind (1872), chapter 'The Blind of Various Countries' (Africa), quoting Meric Casaubon, Treatise on Enthusiasm (1656)",
        [ev(LEV, "a blind man that was a guide to certain merchants travelling through the deserts of Arabia."),
         ev(LEV, "rode upon a camel, and led his company, not by his eyes, which he had not, but by his smell")],
        "medium",
        "A traveller's tale at third hand (Leo Africanus, then Casaubon, then Levy), from the early modern period; it is not "
        "evidence about Israelite camps and may be a legend. Levy himself notes that 'Arabia' there probably means the African deserts.",
    ),
]

# ================================================================= history-of-the-blind
K["history-of-the-blind"] = [
    item(
        "James Wilson's Biography of the Blind (1838) was written by a man 'blind from his infancy'. His introduction says the book "
        "aimed at 'rescuing my fellow sufferers from the neglect and obscurity in which many of them were involved' and 'to exemplify "
        "the powers of the human mind' under blindness; he often had to depend on the kindness of strangers for the loan of books.",
        "Wilson, Biography of the Blind, 4th edition (1838), title page and introduction",
        [ev(WIL, "WHO HAS BEEN BLIND FROM HIS INFANCY."),
         ev(WIL, "My principal object was, to exemplify the powers of the human mind,"),
         ev(WIL, "I had often to depend on the kindness of strangers, for the loan of such books as were")],
        "high",
        "A 19th-century, first-person source. Its idea of 'distinguished' blind people (poets, philosophers, engineers) is one "
        "approach to the history and leaves out ordinary lives; the book is sympathetic but can read as admiration of exceptions.",
    ),
    item(
        "Wilson lists blind people of note, including from antiquity: 'Homer, the venerable father of epic poetry', and in 'the "
        "science of mathematics' many; and 'Here, we find architects building bridges, drawing plans of new roads, and executing "
        "them to the satisfaction of the commissioners'. Chapters cover Homer and Didymus of Alexandria, who 'lost his sight at "
        "five years of age'.",
        "Wilson, Biography of the Blind (1838), Introduction and the chapters on Homer and Didymus",
        [ev(WIL, "Homer, the venerable father of epic poetry, and Milton, the inimitable author of \" Paradise Lost.\""),
         ev(WIL, "Here, we find architects building bridges, drawing plans of new roads, and executing them to the satisfaction of the commissioners."),
         ev(WIL, "although he lost his sight at five years of age")],
        "medium",
        "Wilson takes the Homer tradition and Jerome's account of Didymus at face value; Wikipedia says Didymus lost his sight at four, "
        "and that Homer's blindness is a tradition 'whose basis in truth is uncertain'.",
    ),
    item(
        "Wikipedia on Didymus the Blind (died 398), a teacher in the Church of Alexandria: 'Despite his blindness, Didymus excelled in scholarship "
        "because of his incredible memory', and 'found ways to help blind people to read, experimenting with carved wooden letters'.",
        wsrc("Didymus the Blind", "24 February 2026"),
        [ev(wk("Didymus_the_Blind"), "Didymus became blind at the age of four, before he had learned to read."),
         ev(wk("Didymus_the_Blind"), "Despite his blindness, Didymus excelled in scholarship because of his incredible memory.")],
        "medium",
        "Raw wikitext. The 'carved wooden letters' claim is cited in the article to a journal article calling him 'an unknown precursor "
        "of Louis Braille'; the shelf does not hold that article. Wilson (above) says five years of age.",
    ),
    item(
        "Levy on institutions: St Louis (Louis IX) in 1260 'founded an institution for the reception of 300 blind persons' (the "
        "Quinze-Vingts); he calls it the oldest in Europe or perhaps the world. He also says medieval blind men begged on English "
        "streets crying 'Sainte terre' to show they had lost their sight in the Holy Land.",
        "Levy, Blindness and the Blind (1872), chapter 'The Causes of Blindness'",
        [ev(LEV, "in 1260, founded an institution for the reception of 300 blind persons."),
         ev(LEV, "This was to show that they had lost their sight in the Holy Land, and it was doubtless the strongest appeal that could be made for alms to the pious people of those days.")],
        "medium",
        "Levy says 'it is said' of the street cries and 'the oldest' with a 'perhaps'; the 1260 date is his and fits what is "
        "commonly stated, but the shelf holds no second source. He also gives painful accounts of blinding as punishment, not quoted here.",
    ),
    item(
        "Wikipedia on Valentin Haüy, founder of the first school for the blind (Paris, 1785): his impulse began in 1771 when he "
        "saw people from the Quinze-Vingts hospice for the blind 'being mocked during the religious street festival'; they were given "
        "'oversized cardboard glasses and told to play their instruments'. Louis Braille entered the school in 1819.",
        wsrc("Valentin Haüy", "18 March 2026"),
        [ev(wk("Valentin_Haüy"), "founder of [[Institut National des Jeunes Aveugles]], the first school for the blind"),
         ev(wk("Valentin_Haüy"), "They were given [[dunce cap]]s, oversized cardboard glasses and told to play their instruments which resulted in a [[cacophony]] of noises.")],
        "medium",
        "The second quotation records mockery of blind people; it is given because it explains the founding of the school, not "
        "to repeat it. Raw wikitext.",
    ),
    item(
        "Guides in the ancient world: Wikipedia's 'Cultural depictions of blindness' says that in Sophocles's Oedipus at Colonus, "
        "Oedipus is 'led and supported by his daughter Antigone'. Wikipedia 'Guide dog' says a house wall at Herculaneum "
        "(buried in 79 CE) shows 'a blind-man being guided by his dog'.",
        wsrc("Cultural depictions of blindness", "13 August 2026") + "; " + wsrc("Guide dog", "27 August 2026"),
        [ev(wk("Cultural_depictions_of_blindness"), "In Sophocles's ''[[Oedipus at Colonus]]'', Oedipus is a wandering outcast, led and supported by his daughter [[Antigone]]."),
         ev(wk("Guide_dog"), "Evidence suggests that dogs may have been used as guides for the visually impaired based on depictions of a blind-man being guided by his dog on the wall of a house in [[Herculaneum]], buried when [[Mount Vesuvius|Vesuvius]] erupted in 79 CE.")],
        "medium",
        "The Guide dog article itself says 'additional material evidence would be required' to confirm dogs were used as guides, "
        "and that the oldest written reference it knows is from 1247. The Oedipus play is of the fifth century BCE and is fiction.",
    ),
    item(
        "Wikipedia 'Book of Tobit': Tobit is "
        "blinded, 'becomes dependent on his wife', and his son Tobias travels with the angel 'along with Tobias' dog'; the gall of "
        "a fish cures Tobit's blindness. Wikipedia says the blindness came after 'physicians place ointment in his eyes'.",
        wsrc("Book of Tobit", "8 August 2026"),
        [ev(wk("Book_of_Tobit"), "He becomes dependent on his wife, but accuses her of stealing and prays for death."),
         ev(wk("Book_of_Tobit"), "offers to accompany him (along with Tobias' [[dog]])."),
         ev(wk("Book_of_Tobit"), "he later becomes fully blind after physicians place ointment in his eyes."),
         ev(wk("Book_of_Tobit"), "The gall cures Tobit's blindness")],
        "medium",
        "The article presents Tobit as a story and gives its own dating and canonical discussion, which is not summarised here; the summary does not say "
        "the dog was a guide for the blind man. Brian may want to read the book itself.",
    ),
    item(
        "Levy on the ancient Near East and Persia: 'In Persia it is common for the blind to walk about the cities without guides', "
        "'mendicancy is their ordinary mode of obtaining a livelihood', as a diplomat's account of a procession shows. He says "
        "of France that the blind 'seem to have no idea of walking alone, for even mendicants have guides'.",
        "Levy, Blindness and the Blind (1872), chapter 'The Blind of Various Countries' (Persia and France)",
        [ev(LEV, "In Persia it is common for the blind to walk about the cities without guides"),
         ev(LEV, "The blind of France seem to have no idea of walking alone, for even mendicants have guides")],
        "medium",
        "These are 1870s observations. Levy's generalisations about whole nations are second-hand and he does not show his sources "
        "for the French claim. They show that different societies in his day expected different things of blind people, which is "
        "the point that the first-century picture was probably not uniform either.",
    ),
    item(
        "Wikipedia 'Blind musicians': 'the idea of Homer, the blind poet, for example, has had a long existence in Western tradition, "
        "even though its basis in truth is uncertain'; and 'at many points in history and in many different cultures, blind "
        "musicians... have made important contributions'. Wikipedia 'Homer' says most ancient biographies depict him as blind.",
        wsrc("Blind musicians", "28 June 2026") + "; " + wsrc("Homer", "28 September 2026"),
        [ev(wk("Blind_musicians"), "it remains true that at many points in history and in many different cultures, blind musicians, individually or as a group, have made important contributions to the development of music."),
         ev(wk("Homer"), "In most ancient biographies, Homer is depicted as being blind;")],
        "medium",
        "The 'Homer' quotation says the ancient biographies depict Homer as blind; the article also points out that this is likely "
        "drawn from the passage about the blind bard Demodocus. Neither article addresses everyday blind life.",
    ),
]

# ----------------------------------------------------------------------------
if FAILS:
    print("QUOTES NOT FOUND:")
    for f, q in FAILS:
        print("  ", f, "|", q)
    sys.exit(1)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(K, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
print("wrote", OUT)
for k, v in K.items():
    print(k, len(v))
