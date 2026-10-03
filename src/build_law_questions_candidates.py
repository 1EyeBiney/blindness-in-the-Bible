"""Build data/reference/law_questions_candidates.json from quotes taken from the reference shelf.

Same method as build_followup_candidates.py: each item is written by hand (a plain statement of
what the shelf says, a citation, one or more verbatim quotes). This script finds each quote in
its file (whitespace-insensitive), records the character offset (line endings as LF) and refuses
to write anything if a quote cannot be found.

Keys follow Brian's two questions of 3 October 2026 (from reading the law pages):
  A. Is the Bible the first recorded anything that addresses the blind? Hammurabi against Moses.
     dating, earlier-texts-blinding, earlier-texts-regard
  B. Priestly duties; would a blind priest touch what he should not; would fitting him in burden the Levites?
     priest-duties, touching-holy-things, blemished-priest-provision, priestly-numbers

    python src/build_law_questions_candidates.py   -> data/reference/law_questions_candidates.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
OUT = ROOT / "data" / "reference" / "law_questions_candidates.json"

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
H5 = "matthew_henry_vol5_matthew_to_john.txt"
EAS = "easton_ebd.txt"
SMI = "smiths_bible_dictionary.txt"
I1, I2, I3, I4, I5 = (f"isbe_1915_vol{i}.txt" for i in range(1, 6))
EDL = "edersheim_life_and_times.txt"
JA = "josephus_antiquities_pg2848.txt"
LEV = "levy_blindness_and_the_blind_1872.txt"
HAM = "hammurabi_johns_pg17150.txt"
BUD = "budge_amenemopet_1924.txt"


def wk(name):
    return f"wikipedia_{name}.wiki.txt"


def wsrc(title, date):
    return f"Wikipedia, '{title}', revision of {date} (CC BY-SA 4.0)"


HENRY = "Matthew Henry, Commentary on the Whole Bible (1706-1721), on "
OLD_OCR = ("The 1915 encyclopaedia text on the shelf is an OCR scan with occasional misread letters; "
           "quotations keep the scan's spelling.")

K = {}

# ================================================================= dating
K["dating"] = [
    item(
        "Hammurabi was the sixth king of the First Dynasty of Babylon. Wikipedia's 2026 article gives his reign as about "
        "1792 to 1750 BC. His law collection (the 'Code') belongs to that reign, so on this figure it was set down roughly "
        "1,750 years before the birth of Christ. (The subtraction of Hammurabi from Moses, below, is arithmetic from the "
        "two ranges, not a statement in any source.)",
        wsrc("Hammurabi", "2 October 2026"),
        [ev(wk("Hammurabi"), "Sixth king of Babylon (r. 1792–1750 BC)"),
         ev(wk("Hammurabi"), "reign = c. 1792 – c. 1750 BC")],
        "high",
        "Ancient dates are conventions: Mesopotamian chronology has several competing schemes and the article does not say "
        "which it follows. Treat 1792 to 1750 as 'about', with an uncertainty of decades.",
    ),
    item(
        "The 1915 encyclopaedia on the shelf dated Hammurabi to about 2100 BC, roughly three centuries earlier than the "
        "2026 figure. Wikipedia now gives about 2100 BC for the older Code of Ur-Nammu instead. So any older book on the "
        "shelf that places Hammurabi in Abraham's day or much earlier is using a chronology that has since moved.",
        "International Standard Bible Encyclopaedia (1915), entry 'Hammurabi, the Code of', vol 2, pp. 1329-1332; "
        + wsrc("Code of Ur-Nammu", "8 September 2026"),
        [ev(I2, "Hammurabi (more exactly Hammurapi, c2100BC)"),
         ev(wk("Code_of_Ur-Nammu"), "date_created= {{Circa|2100 BC}}")],
        "high",
        OLD_OCR + " The 1915 entry is quoted only for its date, which later scholarship has revised.",
    ),
    item(
        "The 'early date' of the Exodus puts it at about 1490 or 1491 BC on the shelf's older books. Easton (1897) says "
        "about B.C. 1490, four hundred and eighty years before Solomon's temple (1 Kings 6:1); Matthew Henry heads his "
        "comments on the laws of Leviticus 24 with 'b. c. 1490'. The 1446 BC figure often quoted today for the early "
        "date is not in any shelf text; the shelf's 1490 and 1491 rest on the same 480-year verse and an older "
        "(Ussher-type) chronology.",
        "Easton's Bible Dictionary (1897), entry 'Exodus'; " + HENRY + "Leviticus 24",
        [ev(EAS, "about B.C. 1490, and four hundred and eighty years (1 Kings 6:1) before the building of Solomon's temple"),
         ev(H1, "Laws Concerning the Lamps. (b. c. 1490.)")],
        "high",
        "Both are nineteenth-century or earlier dates. Neither shows 1446. Someone who holds the early date would use a "
        "modern recalculation; the shelf cannot confirm or deny it.",
    ),
    item(
        "The 'late date' is on the shelf in Easton's entry on Egypt (1897): Rameses II, builder of Pithom, he says, must "
        "have been the Pharaoh of the Oppression, and the Pharaoh of the Exodus may have been one of his immediate "
        "successors, which puts the Exodus in the thirteenth century BC. Wikipedia's 2026 article on the Exodus says "
        "most scholars who see a historical core date possible Exodus-group activity to the thirteenth century BCE, at "
        "the time of Ramesses II, with some dating it to the twelfth.",
        "Easton's Bible Dictionary (1897), entry 'Egypt'; " + wsrc("The Exodus", "10 September 2026"),
        [ev(EAS, "he must have been the Pharaoh of the Oppression. The Pharaoh of the Exodus may have been one of his immediate successors, whose reigns were short."),
         ev(wk("The_Exodus"), "date possible Exodus group activity to the thirteenth century BCE at the time of")],
        "high",
        "The Wikipedia sentence is about scholars who accept a 'historical core'; the same article says most mainstream "
        "scholars do not accept the biblical account as history. Easton's regnal dates for Rameses II (1348 to 1281) are "
        "1890s figures and are not used here. The article is about the Exodus group, not about when Leviticus was written.",
    ),
    item(
        "Who wrote Deuteronomy and when? The tradition is that Moses did: Deuteronomy 31:9 says 'Moses wrote this law and "
        "gave it to the priests, the sons of Levi'. Wikipedia's 'Mosaic authorship' says the tradition probably began with "
        "Deuteronomy, and that scholars generally agree Deuteronomy was composed in Jerusalem during the reform of King "
        "Josiah in the late seventh century BCE. Those two answers are about 600 years apart.",
        wsrc("Mosaic authorship", "20 August 2026"),
        [ev(wk("Mosaic_authorship"), "Moses wrote this law and gave it to the priests, the sons of Levi, the ones carrying the Ark of the Covenant of the Lord"),
         ev(wk("Mosaic_authorship"), "which scholars generally agree was composed in Jerusalem during the reform program of King")],
        "high",
        "'Scholars generally agree' is the article's phrase and reports one scholarly position. The article also notes that "
        "traditional Jewish circles and some evangelical scholars hold to Mosaic authorship as a matter of faith. This "
        "file takes no side; it shows the range.",
    ),
    item(
        "Leviticus, the book with the blemish rule (21:16-23), is the one whose date matters most to Brian's question. "
        "Under the documentary hypothesis as Wikipedia lays it out, the Priestly source (which includes most of Leviticus) "
        "is dated to the sixth to fifth century BCE. The article adds that the classical consensus around the hypothesis "
        "'has now faltered', so this date is one view among several.",
        wsrc("Documentary hypothesis", "21 August 2026"),
        [ev(wk("Documentary_hypothesis"), "(6th–5th century BCE)"),
         ev(wk("Documentary_hypothesis"), "The consensus around the classical documentary hypothesis has now faltered.")],
        "medium",
        "The first quotation is a short fragment from a source list in the article's infobox; its label ('Priestly') sits "
        "just before it in the wikitext. The file does not state a date for the Levitical laws as laws, only for the "
        "written source. A law can be older than its writing down.",
    ),
    item(
        "The 1915 encyclopaedia entry 'Priests and Levites' lays out the range in one place: the old belief that all the "
        "Pentateuchal laws were Moses's work; the Wellhausen view that the Levitical Law was unknown in early times; and "
        "the author's own alternative, which accepts the Mosaic authenticity of all the Pentateuchal legislation while "
        "treating Chronicles as a later reading of it.",
        "International Standard Bible Encyclopaedia (1915), entry 'Priests and Levites', vol 4, p. 2447",
        [ev(I4, "The old belief was that the whole of the Penta- teuchal laws were the work of Moses"),
         ev(I4, "The whole Levitical Law was unknown and the distinction between priests and Levites unheard of."),
         ev(I4, "accepts the Mosaic authenticity of all the Pentateuchal legislation")],
        "high",
        OLD_OCR + " The 1915 article is itself a participant in the debate, not a neutral map, and it is over a century old.",
    ),
    item(
        "Dates of the other texts the shelf has, for the comparison with Moses (all from Wikipedia, 2025-2026 revisions): "
        "Code of Ur-Nammu about 2100 BC; Laws of Eshnunna about 1930 BC; Hittite laws 1650-1500 BCE; Middle Assyrian laws "
        "developed between 1450 and 1250 BCE (the first copy found dates to the reign of Tiglath-Pileser I, 1114-1076 BCE); "
        "Ebers Papyrus about 1550 BCE; Instruction of Amenemope most likely 1300-1075 BCE (Budge, in 1924, put its author "
        "under the Eighteenth Dynasty, which is earlier).",
        wsrc("Laws of Eshnunna", "20 August 2026") + "; " + wsrc("Hittite laws", "14 April 2026") + "; "
        + wsrc("Assyrian law", "15 December 2025") + "; " + wsrc("Ebers Papyrus", "10 September 2026") + "; "
        + wsrc("Instruction of Amenemope", "20 May 2026"),
        [ev(wk("Laws_of_Eshnunna"), "date back to c. 1930 BC"),
         ev(wk("Hittite_laws"), "ancient legal code]] dating from {{circa|1650}} – 1500&nbsp;BCE"),
         ev(wk("Assyrian_law"), "developed between 1450 and 1250 BCE"),
         ev(wk("Ebers_Papyrus"), "dating to {{circa|1550 BCE}}"),
         ev(wk("Instruction_of_Amenemope"), "(ca. 1300–1075 BCE)")],
        "high",
        "These are Wikipedia's figures, not those of a primary edition. Several of the texts are known from copies centuries "
        "younger than their composition (the Assyrian laws, Amenemope), so 'date' means a scholarly estimate of when the "
        "text was composed, not of the tablet or papyrus.",
    ),
]

# ================================================================= earlier-texts-blinding
K["earlier-texts-blinding"] = [
    item(
        "Hammurabi (about 1792-1750 BC) prices the loss of an eye by the victim's rank. Johns's 1903 translation, "
        "sections 196, 198 and 199: for a gentleman's eye, the offender's own eye; for a poor man's eye, one mina of "
        "silver; for the eye of a gentleman's servant, half his price. This is the earliest text on the shelf that "
        "deals with a person losing an eye, and it treats the loss as an injury to be paid for or repaid.",
        "Code of Hammurabi, translated by C. H. W. Johns (1903), sections 196-199 (Project Gutenberg 17150)",
        [ev(HAM, "If a man has caused the loss of a gentleman's eye, his eye one shall cause to be lost."),
         ev(HAM, "If he has caused a poor man to lose his eye or shattered a poor man's limb, he shall pay one mina of silver."),
         ev(HAM, "If he has caused the loss of the eye of a gentleman's servant or has shattered the limb of a gentleman's servant, he shall pay half his price.")],
        "high",
        "The Code does not use the word 'blind' anywhere in the Johns text (a search of the file finds none). It prices "
        "the injury; it says nothing about how the person who has lost sight is to live or be treated afterwards. "
        "Johns's numbering differs a little from King's, and he omits the prologue and epilogue.",
    ),
    item(
        "Hammurabi also uses the loss of an eye as a punishment: section 193 says that an adopted son who comes to hate "
        "the father or mother who raised him and goes back to his own father's house is to have his eye torn out. This "
        "is blinding as a penalty, set by a king, centuries before Moses on any dating.",
        "Code of Hammurabi, translated by C. H. W. Johns (1903), section 193",
        [ev(HAM, "and has hated the father that brought him up or the mother that brought him up, and has gone off to the house of his father, one shall tear out his eye.")],
        "high",
        "Graphic penalty; quoted only because the question is which texts punish blinding. The shelf does not say how "
        "often such penalties were carried out. No source on the shelf says the Hebrew law had a corresponding penalty.",
    ),
    item(
        "Hammurabi's sections on doctors treat the eye as an organ a surgeon can save or lose: ten shekels for a "
        "gentleman's eye opened with a bronze lancet and cured; the surgeon's hands cut off if the gentleman loses the "
        "eye; money, half the slave's price, if a poor man's slave loses his eye (sections 215, 218, 220). This shows "
        "eye surgery was practised and its failures priced in Babylon.",
        "Code of Hammurabi, translated by C. H. W. Johns (1903), sections 215-220",
        [ev(HAM, "or has opened an abscess of the eye for a gentleman with the bronze lancet and has cured the eye of the gentleman, he shall take ten shekels of silver."),
         ev(HAM, "has caused the loss of the gentleman's eye, one shall cut off his hands."),
         ev(HAM, "If he has opened his abscess with a bronze lancet and has made him lose his eye, he shall pay money, half his price.")],
        "high",
        "These sections are about the surgeon's fee and liability, not about the patient who is left blind.",
    ),
    item(
        "The Code of Ur-Nammu, about 2100 BC and the oldest law code known, has a tariff for the eye (section 15): "
        "'If a man knocks out the eye of another man, he shall weigh out half a mina of silver.' It sits among fixed money "
        "payments for a foot (ten shekels), a limb, a nose. Wikipedia says the code is three centuries older than Hammurabi's "
        "and that it fines money for bodily damage 'as opposed to the later' eye-for-an-eye principle of Babylonian law.",
        wsrc("Code of Ur-Nammu", "8 September 2026"),
        [ev(wk("Code_of_Ur-Nammu"), "If a man knocks out the eye of another man, he shall weigh out half a mina of silver."),
         ev(wk("Code_of_Ur-Nammu"), "It is three centuries older than the")],
        "high",
        "The table is Wikipedia's rendering of a translation, with the section number from that translation in brackets. The "
        "article says the text is only partly preserved. 'Three centuries' is the article's round figure.",
    ),
    item(
        "The Middle Assyrian laws (developed between 1450 and 1250 BCE, a span that covers both the early and the late Exodus "
        "dates) include blinding as a penalty. Wikipedia's excerpt gives the case of a woman who injures a man's "
        "testicle in a quarrel: one of her fingers is cut off, and for a second injury 'they shall destroy both of her "
        "eyes'. The article says the Assyrian penalties were generally more brutal than the Babylonian.",
        wsrc("Assyrian law", "15 December 2025"),
        [ev(wk("Assyrian_law"), "they shall destroy both of her eyes."),
         ev(wk("Assyrian_law"), "although the penalties for offenses were generally more brutal.")],
        "medium",
        "The article calls the list 'conjectural laws' and 'incomplete'. A translation of the whole tablet is not on the "
        "shelf, so other sections on eyes cannot be checked. Graphic content, quoted in part for the question only.",
    ),
    item(
        "Hittite laws (about 1650-1500 BCE) are case laws that price injuries (Wikipedia's example: 3 shekels of silver for "
        "tearing off a slave's ear), and the first group of clauses (1-24) covers assault. The Wikipedia article gives no "
        "section on blinding or on the blind. I recall that the Hittite laws do have sections on blinding a free man or a "
        "slave; that is from general knowledge and is NOT on the shelf, and the shelf has no public-domain translation of "
        "the Hittite laws.",
        wsrc("Hittite laws", "14 April 2026"),
        [ev(wk("Hittite_laws"), "If anyone tears off the ear of a male or female slave, he shall pay 3"),
         ev(wk("Hittite_laws"), "I Aggression and [[assault]]: Clauses 1 - 24")],
        "medium",
        "What is quoted is only the pattern of pricing injuries. The statement that the Hittite laws have a blinding "
        "section is unverified general knowledge and must be checked in Hoffner, The Laws of the Hittites (1997), a "
        "modern copyrighted edition not on the shelf (archive.org lists it, but it cannot be taken).",
    ),
    item(
        "The Laws of Eshnunna (about 1930 BC) price bodily injury in silver and divide people into classes; Wikipedia's "
        "one example is the nose: 'If a man bit and severed the nose of a man, one mina silver he shall weigh out.' The "
        "article lists 'bodily injuries' as one of five groups of laws. The Code of Lipit-Ishtar (reign 1934-1924 BCE) is "
        "described only as covering boats, agriculture, fugitive slaves, false testimony, foster care, apprenticeship, "
        "marriage and rented oxen; no eye or blind provision is mentioned.",
        wsrc("Laws of Eshnunna", "20 August 2026") + "; " + wsrc("Code of Lipit-Ishtar", "4 October 2025"),
        [ev(wk("Laws_of_Eshnunna"), "If a man bit and severed the nose of a man, one mina silver he shall weigh out."),
         ev(wk("Code_of_Lipit-Ishtar"), "The first set of them deals with boats.")],
        "medium",
        "Wikipedia's articles are summaries. Absence from them is not proof that the tablets lack an eye provision: the "
        "Eshnunna bodily-injury section is not quoted in full, and the Lipit-Ishtar code is incompletely preserved.",
    ),
    item(
        "Wikipedia's article on 'Eye for an eye' says the principle can be found in earlier Mesopotamian law codes such "
        "as those of Ur-Nammu and Lipit-Ishtar, and in Babylonian law. The Hebrew form (Exodus 21:24, Leviticus 24:20) "
        "therefore stands in a long tradition of rules about eye injury, rather than being the first.",
        wsrc("Eye for an eye", "2 October 2026"),
        [ev(wk("Eye_for_an_eye"), "The principle can be found in earlier Mesopotamian law codes such as")],
        "medium",
        "This sentence's claim about Ur-Nammu is in tension with the Ur-Nammu article, which says the code fines money "
        "'as opposed to' eye for an eye, and shows a money payment for the eye. Read it as: older codes also legislated "
        "about eye injury, in different ways.",
    ),
]

# ================================================================= earlier-texts-regard
K["earlier-texts-regard"] = [
    item(
        "The best earlier parallel on the shelf to Leviticus 19:14 is the Egyptian Instruction of Amenemope. Budge's "
        "1924 translation of line 478 reads 'Make not a laughing-stock of the blind man', with 'Vex (or, browbeat) not "
        "the dwarf' and 'frustrate not the plans of the afflicted (or, lame) man' beside it. This is a text that "
        "protects, by instruction, the dignity of a blind man. Wikipedia dates the Instruction most likely to "
        "1300-1075 BCE; Budge placed its author under the Eighteenth Dynasty.",
        "E. A. Wallis Budge, The Teaching of Amen-em-apt, Son of Kanekht (London, 1924), line 478 (Archive.org copy `in.ernet.dli.2015.82818`); "
        + wsrc("Instruction of Amenemope", "20 May 2026"),
        [ev(BUD, "478. Make not a laughing-stock of the blind man."),
         ev(BUD, "Vex^ (or, browbeat) not the dwarf,"),
         ev(wk("Instruction_of_Amenemope"), "(ca. 1300–1075 BCE)")],
        "high",
        "The OCR has a stray caret ('Vex^'). Budge's translation is a hundred years old and later translators phrase the "
        "line differently; I have not compared them. The date of the text relative to Moses depends on which Exodus date is "
        "used: on a late date it is roughly a contemporary, on an early date one to three centuries later. The line is advice to a "
        "reader; it is not a law with a penalty.",
    ),
    item(
        "Budge, summarising the Teaching in 1924, lists the same kindness among its commands: 'Do nothing that will make "
        "the blind man a laughing-stock to his neighbours. Moreover, mock not the dwarf because of his form and colour, "
        "and interfere not in the affairs of the man with a physical defect to injure him.' He cites lines 478 to 481 and "
        "says the admonition shows 'the kindly disposition of the man and his thoughtfulness for others'.",
        "E. A. Wallis Budge, The Teaching of Amen-em-apt (1924), Introduction",
        [ev(BUD, "Do nothing that will make the blind man a laughing- stock to his neighbours."),
         ev(BUD, "is well illustrated by his admonition \" Treat not the blind man with ridicule")],
        "high",
        "The second line is Budge's paraphrase in his introduction; the text of line 478 itself is the other item. The "
        "word 'dwarf' is the translator's. Budge's phrasing of the 'physical defect' line is his own wording of lines "
        "479-481, which other translators render differently.",
    ),
    item(
        "Egyptian images show blind harpists. Wikipedia's 'Harper's Songs' says blind harpists are depicted on Middle "
        "Kingdom tomb walls (about 2040-1640 BCE) and that the songs accompanying such drawings are thought to have "
        "been sung; 'Blind musicians' pictures a blind harpist from an Eighteenth Dynasty mural of the fifteenth "
        "century BC. These show blind people in a recognised role (singers to the harp) in Egypt before or around "
        "Moses on any date.",
        wsrc("Harper's Songs", "1 June 2026") + "; " + wsrc("Blind musicians", "28 June 2026"),
        [ev(wk("Harpers_Songs"), "blind harpists are depicted on tomb walls."),
         ev(wk("Harpers_Songs"), "These texts are accompanied by drawings of blind harpists and are therefore thought to have been sung."),
         ev(wk("Blind_musicians"), "A blind harpist, from a mural of the Eighteenth dynasty of Egypt, 15th century BC")],
        "high",
        "A picture of a role is not a statement of regard. The articles do not say how these harpists were treated, "
        "whether blindness was the reason for the role, or whether the artists drew blindness literally.",
    ),
    item(
        "Levy (1872), quoting the Bible scholar John Kitto, describes an Egyptian wall painting from the tombs at "
        "Alabastron: a blind harper seated cross-legged, attended by seven other blind men who sing and beat time with "
        "their hands, 'evidently professional musicians'. Levy concludes that music was very early a source of work for "
        "the blind in Egypt.",
        "W. H. Levy, Blindness and the Blind (1872), chapter on blind musicians (OCR, no page locator); quoting J. Kitto",
        [ev(LEV, "represents a blind harper sitting cross-legged on the ground, attended by seven other blind men, similarly seated, who sing and beat time with their hands."),
         ev(LEV, "They are evidently professional mu- sicians.")],
        "medium",
        "Nineteenth-century secondhand description; the painting is not dated in the quotation. Levy's next words about the "
        "numbers of blind in Egypt use a loaded adverb and are not quoted. 'Professional' is Kitto's inference from the image.",
    ),
    item(
        "Ur-Nammu (about 2100 BC) boasts that he protected the weak, but the weak he names are the orphan, the widow and "
        "the man with one shekel: 'The orphan was not delivered up to the rich man; the widow was not delivered up to the "
        "mighty man; the man of one shekel was not delivered up to the man of one mina.' The blind are not named. "
        "Wikipedia says these have been seen as among the earliest documented cases of regard for widows, orphans and the poor.",
        wsrc("Code of Ur-Nammu", "8 September 2026"),
        [ev(wk("Code_of_Ur-Nammu"), "The orphan was not delivered up to the rich man; the widow was not delivered up to the mighty man; the man of one shekel was not delivered up to the man of one mina."),
         ev(wk("Code_of_Ur-Nammu"), "earliest documented cases of regard for")],
        "high",
        "It shows an ancient text caring about vulnerable groups; it does not mention blind people. If a blind person was "
        "poor, the protection may have reached them, but the text does not say so.",
    ),
    item(
        "Hammurabi says in his prologue, as Wikipedia reports it, that the gods gave him his rule 'to prevent the strong from "
        "oppressing the weak'. The weak are not listed in what Wikipedia quotes. The English Code on the shelf (Johns) "
        "omits the prologue, and no source on the shelf lists the blind among the weak it means.",
        wsrc("Code of Hammurabi", "2 October 2026"),
        [ev(wk("Code_of_Hammurabi"), "to prevent the strong from oppressing the weak")],
        "medium",
        "A general intention; not a provision. It is included because Brian's question is whether Hammurabi 'has nothing' "
        "about the blind: it has no section on the blind, but it does have this stated purpose.",
    ),
    item(
        "Wikipedia on Amenemope: the author urges the reader to defend the weaker classes of society and to respect the "
        "elderly, widows and the poor, while condemning abuses of power. Wikipedia also sets Amenemope beside Proverbs "
        "22:17 to 23:11, and quotes 'Rob not the poor, for he is poor' against 'Beware of robbing the poor, and "
        "oppressing the afflicted'. This places the blind-man line inside a wider ethic of care for the vulnerable, and "
        "shows that Hebrew wisdom writing has a close Egyptian relative.",
        wsrc("Instruction of Amenemope", "20 May 2026"),
        [ev(wk("Instruction_of_Amenemope"), "He urges the reader to defend the weaker classes of society and to respect the elderly, widows and the poor, while he condemns abuses of power or authority."),
         ev(wk("Instruction_of_Amenemope"), "most likely during the")],
        "medium",
        "The Proverbs parallel is to Proverbs, not to Leviticus 19:14 or Deuteronomy 27:18; the article does not discuss "
        "the blind-man line and the direction of influence between the two books is, as it says, contested. The second "
        "quotation is a short fragment used to anchor the article's dating sentence.",
    ),
    item(
        "Egyptian medicine had eye remedies. Wikipedia says the Ebers Papyrus (about 1550 BCE, copied from earlier texts) "
        "contains chapters on 'eye and skin problems'. Babylon's Code also paid fees for eye surgery (see "
        "earlier-texts-blinding). So physicians in Egypt and Babylon treated eye disease before Moses on the early date.",
        wsrc("Ebers Papyrus", "10 September 2026"),
        [ev(wk("Ebers_Papyrus"), "intestinal disease and parasites, eye and skin problems,")],
        "medium",
        "Treating eye disease is concern about the eye; it is not a social regard for blind people. The article does not "
        "list individual remedies, and the shelf has no translation of the papyrus.",
    ),
    item(
        "For the Hebrew side of the comparison, the shelf's Henry gives the two texts: Leviticus 19:14, 'Thou shalt not "
        "curse the deaf, nor put a stumbling block before the blind', and Deuteronomy 27:18, 'Cursed be he that maketh "
        "the blind to wander out of the way'. Henry reads them as protecting those who cannot help themselves. These "
        "are the laws (rather than advice) on the shelf that single out the blind for protection.",
        HENRY + "Leviticus 19 and Deuteronomy 27",
        [ev(H1, "Thou shalt not curse the deaf, nor put a stumbling block before the blind, but shalt fear thy God: I am the Lord."),
         ev(H1, "Cursed be he that maketh the blind to wander out of the way."),
         ev(H1, "To be particularly tender of the credit and safety of those that cannot help themselves, v. 14.")],
        "high",
        "'The first law that protects the blind' is a stronger claim than the shelf can support. The shelf has Egyptian "
        "advice of a similar kind; whether it is earlier than Leviticus depends on the dates in the dating key. The Bible "
        "texts are laws with a curse or fear-of-God sanction; the Egyptian line is an instruction.",
    ),
]

# ================================================================= priest-duties
K["priest-duties"] = [
    item(
        "Smith's dictionary lists the priests' duties: to watch the fire on the altar of burnt offering and keep it "
        "burning day and night; to feed the golden lamp outside the veil with oil; to offer the morning and evening "
        "sacrifices; to teach the statutes of the Lord; in the wilderness, to cover the ark and the vessels of the sanctuary "
        "before the Levites approached them; and to blow the silver trumpets. Priests were barefoot in all their ministrations.",
        "Smith's Bible Dictionary (1884 edition), entry 'Priest'",
        [ev(SMI, "The chief duties of the priests were to watch over the fire on the altar of burnt offering, and to keep it burning evermore both by day and night,"),
         ev(SMI, "to feed the golden lamp outside the vail with oil"),
         ev(SMI, "They were also to teach the children of Israel the statutes of the Lord."),
         ev(SMI, "In all their acts of ministration they were to be bare footed.")],
        "high",
        "A summary list. It does not say which tasks every priest did and which were done by lot or by the high priest. "
        "The word 'duties' covers very different work: fire and blood on the one hand, teaching on the other.",
    ),
    item(
        "Touch, blood and heat: the sacrifice. Leviticus 1 says the offerer kills the bullock and the priests 'bring the "
        "blood, and sprinkle the blood round about upon the altar'; the beast is flayed and cut into pieces; the priests "
        "put fire on the altar, lay the wood in order and lay the parts on it. Henry adds that the animal was killed by "
        "the priests or Levites and cut up 'according to the art of the butcher', and that the inwards and legs were washed.",
        HENRY + "Leviticus 1",
        [ev(H1, "And he shall kill the bullock before the Lord: and the priests, Aaron's sons, shall bring the blood, and sprinkle the blood round about upon the altar"),
         ev(H1, "And the sons of Aaron the priest shall put fire upon the altar, and lay the wood in order upon the fire"),
         ev(H1, "7. The beast was to be flayed and decently cut up, and divided into its several joints or pieces, according to the art of the butcher")],
        "high",
        "Henry's note that the priests or Levites did the killing is his gloss; the verse itself gives the killing to the "
        "offerer ('he shall kill'). The text describes the tasks; it says nothing about who among the priests did which, "
        "or about touch as an issue.",
    ),
    item(
        "Touch and heat again: the ashes. Leviticus 6:10-11 has the priest, in his linen garment, 'take up the ashes which "
        "the fire hath consumed with the burnt offering on the altar' and put them beside the altar, then change clothes "
        "and carry them outside the camp. Henry says this was done every morning and that it taught the priests 'to stoop "
        "to the meanest services' for God's honour. Smith's puts the priests' watch over the altar fire as the first duty.",
        HENRY + "Leviticus 6",
        [ev(H1, "and take up the ashes which the fire hath consumed with the burnt offering on the altar, and he shall put them beside the altar."),
         ev(H1, "He must clear the altar of them every morning, and put them on the east side of the altar"),
         ev(H1, "God would have the priests themselves to keep it so, to teach them and us to stoop to the meanest services for the honour of God")],
        "high",
        "The shelf gives the task and its meaning; it does not describe how a priest knew by sight or by touch that "
        "ashes were cool enough. The ashes were of fire already burned down, per the verse.",
    ),
    item(
        "The lamps: Easton says the tabernacle had no windows, so the seven-branched lampstand gave the only light; it "
        "was lit every evening and extinguished in the morning. In the morning the priests trimmed the seven lamps with "
        "golden snuffers, carrying away the ashes in golden dishes and supplying fresh oil. Henry on Leviticus 24:3-4: "
        "'The priests were to tend the lamps; they must snuff them, clean the candlestick, and supply them with oil.'",
        "Easton's Bible Dictionary (1897), entry 'Candlestick'; " + HENRY + "Leviticus 24",
        [ev(EAS, "In the morning the priests trimmed the seven lamps, borne by the seven branches, with golden snuffers, carrying away the ashes in golden dishes (Ex. 25:38), and supplying the lamps at the same time with fresh oil."),
         ev(EAS, "It was lighted every evening, and was extinguished in the morning."),
         ev(H1, "The priests were to tend the lamps; they must snuff them, clean the candlestick, and supply them with oil, morning and evening")],
        "high",
        "The lamps are the one duty where light and sight come into the sources directly, but the sources describe tending, "
        "not how a priest judged the work by eye. That a blind man could not do it is an inference, not a source claim.",
    ),
    item(
        "Incense, in the Holy Place. Easton: incense was offered daily on the golden altar, and on the Day of Atonement "
        "burned by the high priest in the Holy of Holies. Edersheim describes the daily incensing as Luke 1 sets it: two "
        "assistants clear the altar and spread live coals; the celebrant 'stood alone within the Holy Place', waits for a "
        "signal, and Zacharias 'waited, until he saw the incense kindling'. The lot chose who would do it.",
        "Easton's Bible Dictionary (1897), entry 'Incense'; Alfred Edersheim, The Life and Times of Jesus the Messiah, Book II, ch. 1; "
        + HENRY + "Luke 1",
        [ev(EAS, "daily offered on the golden altar in the holy place, and on the great day of atonement was burnt by the high priest in the holy of holies"),
         ev(EDL, "But the celebrant Priest, bearing the golden censer, stood alone within the Holy Place, lit by the sheen of the seven-branched candlestick."),
         ev(EDL, "Zacharias waited, until he saw the incense kindling."),
         ev(H5, "his lot was to burn incense when he went into the temple of the Lord")],
        "high",
        "Edersheim's description rests on the Mishnah (Tamid and Yoma) and Jewish tradition, written long after the "
        "Temple; Luke's account is much shorter. Sight appears in this picture (the lit lamps, the signal, the kindling "
        "incense), but the sources do not say a blind priest was or was not able to serve here; Leviticus 21:23 keeps "
        "a blemished priest from the veil and the altar in any case.",
    ),
    item(
        "The showbread: twelve loaves renewed every Sabbath; the old ones eaten by the priests in the holy place (Easton, "
        "Leviticus 24:5-9). Wikipedia, reporting the Mishnah, says that to replace the bread two priests entered the "
        "sanctuary ahead of four priests carrying the new bread, with two more bringing the incense cups; i.e. the work "
        "was done by a team in a set order. Josephus says the loaves were brought in on the Sabbath morning and set on the table.",
        "Easton's Bible Dictionary (1897), entry 'Shewbread'; " + wsrc("Showbread", "13 February 2026")
        + "; Josephus (Whiston), Antiquities III.10.7",
        [ev(EAS, "They were renewed every Sabbath (Lev. 24:5-9), and those that were removed to give place to the new ones were to be eaten by the priests only in the holy place"),
         ev(wk("Showbread"), "states that to replace the bread, two priests would enter the sanctuary ahead of another four priests carrying the replacement bread;"),
         ev(JA, "were brought into the holy place on the morning of the sabbath, and set upon the holy table, six on a heap")],
        "high",
        "The Mishnah's choreography was written down centuries after the first Temple and describes the Second Temple. "
        "The tabernacle account in Leviticus 24 gives no such team arrangement.",
    ),
    item(
        "Speaking, not touching: the blessing. Henry on Leviticus 9:22: Aaron 'lifted up his hand towards the people, and "
        "blessed them', which he calls 'one part of the priest's work'. Henry on Numbers 6:22-27 says the priests were "
        "appointed to bless Israel with the words of the threefold blessing. Smith's adds teaching: priests were 'to teach "
        "the children of Israel the statutes of the Lord', and under Deuteronomy 17 to act as a court of appeal.",
        HENRY + "Leviticus 9 and Numbers 6; Smith's Bible Dictionary (1884 edition), entry 'Priest'",
        [ev(H1, "he lifted up his hand towards the people, and blessed them, v. 22. This was one part of the priest's work"),
         ev(H1, "On this wise ye shall bless the children of Israel, saying unto them,"),
         ev(SMI, "They were to act (whether individually or collectively does not distinctly appear) as a court of appeal in the more difficult controversies in criminal or civil cases.")],
        "high",
        "These duties are spoken. The sources do not say who among the priests blessed or judged in the time of a "
        "blemished priest. Wikipedia's Emor article reports a Talmudic rule about who may lift his hands to bless (see "
        "blemished-priest-provision); the Bible text itself does not.",
    ),
    item(
        "Looking: skin disease. Leviticus 13 has the priest examine skin and hair repeatedly ('the priest shall look on the "
        "plague in the skin of the flesh'; 'in sight be not deeper than the skin'), shut up the patient for seven days "
        "and look again on the seventh, then pronounce clean or unclean. This duty depends on sight throughout, and "
        "Henry reports the Jewish rule about it (see blemished-priest-provision).",
        HENRY + "Leviticus 13",
        [ev(H1, "3 And the priest shall look on the plague in the skin of the flesh: and when the hair in the plague is turned white"),
         ev(H1, "4 If the bright spot be white in the skin of his flesh, and in sight be not deeper than the skin, and the hair thereof be not turned white; then the priest shall shut up him that hath the plague seven days")],
        "high",
        "'Leprosy' here is the translation's word for a range of skin conditions; Smith's dictionary says it was probably "
        "not leprosy in the modern sense. This verse text is from the King James Version, as Henry gives it.",
    ),
    item(
        "The Levites' work (distinct from the priests'): Easton says they carried the tent and the parts of the sacred "
        "structure and waited on the priests; they were the special guardians of the tabernacle. Smith's says that under "
        "David and in the Temple they were gatekeepers, vergers, sacristans and choristers, to 'wait on the sons of Aaron "
        "for the service of the house of Jehovah, in the courts, and the chambers, and the purifying of all holy things', "
        "to stand every morning and evening to thank and praise the Lord, and to assist in offering burnt sacrifices.",
        "Easton's Bible Dictionary (1897), entry 'Levite'; Smith's Bible Dictionary (1884 edition), entry 'Levites'",
        [ev(EAS, "It was their duty to move the tent and carry the parts of the sacred structure from place to place."),
         ev(SMI, "the Levites were the gatekeepers, vergers, sacristans, choristers, of the central sanctuary of the nation."),
         ev(SMI, "to stand every morning to thank and praise Jehovah, and likewise at even.")],
        "high",
        "A summary from the biblical lists (1 Chronicles 23-26). It describes the whole tribe's roles; it does not say "
        "how many of each kind were needed or whether any Levite had a bodily difference.",
    ),
]

# ================================================================= touching-holy-things
K["touching-holy-things"] = [
    item(
        "Numbers 4:15 and 4:20. When the camp moved, Aaron and his sons covered the sanctuary and all its vessels first; "
        "after that the Kohathites came to carry them, 'but they shall not touch any holy thing, lest they die'. And "
        "'they shall not go in to see when the holy things are covered, lest they die'. So for the Kohathite Levites the "
        "rule was both not to touch and not to look at the holy things, on pain of death. Henry's comment on the second "
        "rule: 'Even those that bore the vessels of the Lord saw not what they bore.'",
        HENRY + "Numbers 4",
        [ev(H1, "but they shall not touch any holy thing, lest they die."),
         ev(H1, "But they shall not go in to see when the holy things are covered, lest they die."),
         ev(H1, "The Kohathites must not see the holy things till the priests had covered them, v. 20. Even those that bore the vessels of the Lord saw not what they bore"),
         ev(H1, "When the holy things were covered, they might not touch them, at least not the ark, called here the holy thing, upon pain of death")],
        "high",
        "These are the rules for the Levites (Kohathites), not for the priests, who did handle the holy things. "
        "Nothing here is about an accidental touch: the verses describe the rule and the penalty. Whether an unintended "
        "touch drew the same penalty is not stated in these verses or in Henry's note.",
    ),
    item(
        "The 1915 encyclopaedia reads the same rules narrowly: the Levites' charge over the tabernacle and its furniture "
        "meant porterage only, and Numbers 18:3 shows 'death would be the result of a Levite's touching any of these "
        "vessels'. 'They shall not touch the sanctuary, lest they die' limits the Kohathites to carrying after the "
        "articles had been wrapped up by Aaron and his sons. The writer adds that these were desert services only.",
        "International Standard Bible Encyclopaedia (1915), entry 'Priests and Levites', vol 4, p. 2448",
        [ev(I4, "We learn from 18 3 that death would be the result of a Levite's touching any of these vessels"),
         ev(I4, "they shall not touch the sanctuary, lest they die"),
         ev(I4, "service of porterage after the articles have been wrapped up by Aaron and his sons")],
        "high",
        OLD_OCR + " This is the writer's own reading (he accepts the Mosaic date, see the dating key) and is not the only reading.",
    ),
    item(
        "Smith's dictionary puts the sequence plainly: during the wilderness journeys it belonged to the priests to cover the "
        "ark and all the vessels of the sanctuary with a purple or scarlet cloth before the Levites might approach them. "
        "The sacred things were therefore handled by priests (the family of Aaron) and carried, already covered, by Levites.",
        "Smith's Bible Dictionary (1884 edition), entry 'Priest'",
        [ev(SMI, "During the journeys in the wilderness it belonged to them to cover the ark and all the vessels of the sanctuary with a purple or scarlet cloth before the Levites might approach them.")],
        "high",
        "It gives the arrangement, not the reason; the reason implied by the verse is holiness.",
    ),
    item(
        "Uzzah (2 Samuel 6:6-7). When the oxen shook the cart carrying the ark, Uzzah 'put forth his hand to the ark of God, "
        "and took hold of it', and 'God smote him there for his error'. Henry's reading: Uzzah was a Levite, 'but priests "
        "only might touch the ark'; the law about the Kohathites was express (Numbers 4:15); Henry thinks Uzzah acted "
        "with 'a very good intention' to save the ark from falling, and still it was his crime. Wikipedia: he steadied "
        "the ark with his hand, in violation of the divine law, and was killed.",
        HENRY + "2 Samuel 6; " + wsrc("Uzzah", "27 January 2026"),
        [ev(H2, "6 And when they came to Nachon's threshingfloor, Uzzah put forth his hand to the ark of God, and took hold of it; for the oxen shook it."),
         ev(H2, "Uzzah was a Levite, but priests only might touch the ark."),
         ev(H2, "to save it from falling, we have reason to think with a very good intention"),
         ev(wk("Uzzah"), "Uzzah steadied the Ark with his hand, in direct violation of the divine law")],
        "high",
        "The best-known case of an unplanned-looking touch with a fatal outcome. It was a deliberate grab by a sighted "
        "man, not a mistake of orientation, so it does not speak directly to a blind person's incidental contact. Henry "
        "gives several reasons for the severity (the cart, the law, presumption); the text does not choose among them. "
        "It is also not a priest's case: Uzzah was a Levite, if Henry is right.",
    ),
    item(
        "Leviticus 10: Nadab and Abihu, sons of Aaron, 'took either of them his censer, and put fire therein, and put "
        "incense thereon, and offered strange fire before the Lord, which he commanded them not', and fire went out and "
        "devoured them. Henry reads the sin as taking common fire rather than the fire God had kindled. The fault is "
        "about the fire and the permission, not about touching a holy object. Wikipedia adds that the bodies were carried "
        "out by their tunics, so the bearers would touch the clothing and not the bodies.",
        HENRY + "Leviticus 10; " + wsrc("Nadab and Abihu", "14 May 2026"),
        [ev(H1, "took either of them his censer, and put fire therein, and put incense thereon, and offered strange fire before the Lord, which he commanded them not."),
         ev(H1, "they took common fire, probably from that with which the flesh of the peace-offerings was boiled"),
         ev(wk("Nadab_and_Abihu"), "to be careful to only touch Nadab and Abihu's tunics, and not their bodies.")],
        "high",
        "Henry's 'common fire' is his explanation; the text says only 'strange fire'. This case is a warning about fire "
        "and incense, which are duties inside the sanctuary that Leviticus 21:23 already closes to a blemished priest.",
    ),
    item(
        "The washing rule. Easton: the laver held water in which the priests washed their hands and feet when they entered the "
        "tabernacle, and it stood in the court between the altar and the door. Smith's: 'a vessel of brass containing water for "
        "the priests to wash their hands and feet before offering sacrifice.' Wikipedia's 'Kohen' says a priest would "
        "immerse in a mikveh before vesting and wash his hands and feet before any sacred act.",
        "Easton's Bible Dictionary (1897), entry 'Laver'; Smith's Bible Dictionary (1884 edition), entry 'Laver'; "
        + wsrc("Kohen", "22 September 2026"),
        [ev(EAS, "It contained water wherewith the priests washed their hands and feet when they entered the tabernacle (40:32)."),
         ev(SMI, "a vessel of brass containing water for the priests to wash their hands and feet before offering sacrifice."),
         ev(wk("Kohen"), "and wash his hands and his feet before performing any sacred act.")],
        "high",
        "The 'Laver' article on Wikipedia is only a disambiguation page and is not used. These sources describe "
        "washing as a rule of preparation, not as a rule that bears on touching by mistake. The mikveh statement is "
        "later Jewish practice as Wikipedia reports it.",
    ),
    item(
        "Numbers 18:3. The Levites and priests are to keep charge, but 'only they shall not come nigh the vessels of the "
        "sanctuary and the altar, that neither they, nor ye also, die'. Henry says that if strangers or unclean persons "
        "intruded into the sanctuary, 'the blame should lie upon the Levites and priests, who ought to have kept them off'. "
        "So part of the duty was watching: keeping others, and each other, from improper contact.",
        HENRY + "Numbers 18",
        [ev(H1, "only they shall not come nigh the vessels of the sanctuary and the altar, that neither they, nor ye also, die."),
         ev(H1, "the blame should lie upon the Levites and priests, who ought to have kept them off.")],
        "medium",
        "Henry's paraphrase of the verse applies to guarding duty. The text does not say how the watch was kept or "
        "whether every watcher had to see. It says the Levites keep the charge and bear the burden if the sanctuary is "
        "profaned.",
    ),
    item(
        "Putting the touching rules beside the rule for the blemished priest. Leviticus 21:23 says the blemished priest "
        "'shall not go in unto the vail, nor come nigh unto the altar, because he hath a blemish; that he profane not my "
        "sanctuaries'. The rule's own stated reason is the profaning of the sanctuary. The sources on the shelf give "
        "no instance of anyone profaning it by accidental touch, other than Uzzah's deliberate grab.",
        HENRY + "Leviticus 21",
        [ev(H1, "23 Only he shall not go in unto the vail, nor come nigh unto the altar, because he hath a blemish; that he profane not my sanctuaries: for I the Lord do sanctify them.")],
        "high",
        "Whether the rule was meant to prevent accidental touching is not stated; the verse says 'because he hath a "
        "blemish' and 'that he profane'. The inference that the rule also spares a blind priest from the places where the "
        "touching dangers lie is mine, not a source's.",
    ),
]

# ================================================================= blemished-priest-provision
K["blemished-priest-provision"] = [
    item(
        "Leviticus 21:17-23 in Henry's text: a descendant of Aaron with a blemish, and a blind man heads the list, 'shall "
        "not approach to offer the bread of his God'. But 'He shall eat the bread of his God, both of the most holy, and "
        "of the holy. Only he shall not go in unto the vail, nor come nigh unto the altar'. So he keeps his place as a "
        "priest and his share of the food, and does not do the altar service or enter the veil.",
        HENRY + "Leviticus 21",
        [ev(H1, "Whosoever he be of thy seed in their generations that hath any blemish, let him not approach to offer the bread of his God."),
         ev(H1, "For whatsoever man he be that hath a blemish, he shall not approach: a blind man, or a lame"),
         ev(H1, "He shall eat the bread of his God, both of the most holy, and of the holy.")],
        "high",
        "The King James list in this chapter includes words now considered harsh; only the clauses needed are quoted. "
        "The verse text is the source; the reading that 'blind' here means the same as modern blindness is the translators'.",
    ),
    item(
        "Henry on the provision: 'The blemishes were such as they could not help, and therefore, though they might not "
        "work, they must not starve. Note, None must be abused for their natural infirmities.' He lists what the "
        "blemished priest keeps: the most holy things such as the show-bread and the sin-offerings, and the holy things "
        "such as the tithes and first-fruits.",
        HENRY + "Leviticus 21",
        [ev(H1, "The blemishes were such as they could not help, and therefore, though they might not work, they must not starve. Note, None must be abused for their natural infirmities."),
         ev(H1, "He shall eat of the sacrifices with the other priests, even the most holy things, such as the show-bread and the sin-offerings")],
        "high",
        "Henry's chapter note also gives an appearance-based reason for the rule, and uses dated words for bodily "
        "differences and for the people at the altar; those parts are not quoted. The paragraph above is Henry's reading of "
        "'they must not starve', not a statement in Leviticus.",
    ),
    item(
        "Josephus (Whiston), retelling the Law: the priest who has any blemish 'should have his portion indeed among the "
        "priests, but he forbade him to ascend the altar, or to enter into the holy house.' He adds that the priests "
        "were to be unblemished in all respects and that sacrifices must be entire. Josephus is the earliest "
        "non-biblical report on the shelf (first century AD).",
        "Josephus (Whiston), Antiquities of the Jews, Book III, ch. 12, sect. 2",
        [ev(JA, "He ordered that the priest who had any blemish, should have his portion indeed among the priests, but he forbade him to ascend the altar, or to enter into the holy house.")],
        "high",
        "Josephus restates the law as he knew it; he does not say how many blemished priests there were or what duties "
        "they took in place of altar work.",
    ),
    item(
        "The 1915 encyclopaedia 'Blemish': a blemish in a person of priestly descent 'prevented him from the execution of "
        "the priestly office'; it reads the Hebrew word broadly as disfiguring affections of the skin, and for the 'blemish "
        "in the eye' of Leviticus 21:20 it gives 'cataract, white spots in the eye'. This is one scholar's reading of "
        "what the eye blemish was, in addition to the word 'blind' in verse 18.",
        "International Standard Bible Encyclopaedia (1915), entry 'Blemish', vol 1, pp. 486-487",
        [ev(I1, "The existence of a blem ish in a person of priestly descent prevented him from the execution of the priestly office"),
         ev(I1, "cataract, white spots in the eye (Lev 21 20)")],
        "medium",
        OLD_OCR + " The entry's reading of the Hebrew is one view; modern commentaries (not on the shelf) may differ.",
    ),
    item(
        "The skin-disease helper rule. Henry on Leviticus 13: 'All the Jews say, \"Any priest, though disabled by a blemish "
        "to attend the sanctuary, might be a judge of the leprosy, provided the blemish were not in his eye. And he might\" "
        "(they say) \"take a common person to assist him in the search, but the priest only must pronounce the judgment.\"' "
        "So by the rule's wording a blemished priest could still judge skin disease unless the blemish was in his eye, and "
        "even a sighted priest could take a lay assistant to help with the searching.",
        HENRY + "Leviticus 13",
        [ev(H1, "All the Jews say, \"Any priest, though disabled by a blemish to attend the sanctuary, might be a judge of the leprosy, provided the blemish were not in his eye."),
         ev(H1, "take a common person to assist him in the search, but the priest only must pronounce the judgment.")],
        "high",
        "This is Henry quoting a Jewish rule at second hand, with no source given (it is not in Leviticus 13). The rule, as "
        "Henry gives it, does NOT make skin inspection open to a blind priest: the exception is for a blemish 'not in his "
        "eye'. The helper is for the search, and the priest must see to pronounce. Henry's surrounding phrase about the "
        "lepers being 'stigmatized' is not quoted.",
    ),
    item(
        "Wikipedia's 'Emor' article (the Torah portion containing Leviticus 21) summarises: no disabled priest could "
        "offer sacrifices; he could eat the meat of sacrifices but not come near the altar; and in the Mishnah (Bekhorot "
        "7) the disabilities that disqualify priests do not disqualify Levites, and the reverse. Levites were disqualified "
        "by age (30 to 50, for carrying) and 'nothing else disqualifies them'. So on the rabbinic reading a Levite with a "
        "bodily difference was not barred by it.",
        wsrc("Emor", "14 May 2026"),
        [ev(wk("Emor"), "no disabled priest could offer [[korban|sacrifices]]."),
         ev(wk("Emor"), "The Mishnah taught that a disability that did not disqualify priests disqualified Levites, and a disability that did not disqualify Levites disqualified priests."),
         ev(wk("Emor"), "to instruct that \"this\", that is, age, only disqualifies Levites, but nothing else disqualifies them.")],
        "high",
        "The article's rabbinic material dates from the Mishnah and Talmud (about 200 to 500 CE), centuries after the "
        "tabernacle. The statement describes how the rabbis read Numbers 8:24-25, not what was done under Moses. The "
        "article also notes that the Sifre says the age limit applied only to carrying in the wilderness.",
    ),
    item(
        "The rabbinic discussion in 'Emor' also gives rules about the priestly blessing: Rabbi Johanan said that a man blind "
        "in one eye should not lift up his hands, but the Gemara notes that if the townspeople were accustomed to him he was "
        "permitted. The reason given in the article for a similar rule about discoloured hands is that the congregation should "
        "not look at the priest during the blessing. The same page says a priest with a blemish who officiated in the "
        "Sanctuary was liable to death at the hands of Heaven on one rabbi's view, merely prohibited on the Sages'.",
        wsrc("Emor", "14 May 2026"),
        [ev(wk("Emor"), "Rabbi Joḥanan said that a man blind in one eye should not lift up his hands."),
         ev(wk("Emor"), "because it would cause the congregation to look at him during this blessing when they should not."),
         ev(wk("Emor"), "said that a priest with a blemish within the meaning of Leviticus 21:20 who officiated at services in the Sanctuary was liable to death at the hands of")],
        "medium",
        "These are rabbinic rulings of the Talmudic period (the article cites the Mishnah and the Talmud) about the "
        "blessing, not Leviticus. The sources on the shelf do not say how a fully blind priest was treated in the blessing. The 'accustomed' "
        "exception shows that the rule bent to local familiarity.",
    ),
    item(
        "Henry's pastoral turn on the verse: 'Under the gospel, 1. Those that labour under any such blemishes as these have "
        "reason to thank God that they are not thereby excluded from offering spiritual sacrifices to God; nor, if "
        "otherwise qualified for it, from the office of the ministry.' So Henry, writing in 1706-1721, takes the Levitical "
        "limit as belonging to the ceremonial law and not carried into the church.",
        HENRY + "Leviticus 21",
        [ev(H1, "Those that labour under any such blemishes as these have reason to thank God that they are not thereby excluded from offering spiritual sacrifices to God; nor, if otherwise qualified for it, from the office of the ministry.")],
        "high",
        "Henry's own application, not a source for what Leviticus meant. In the same note he also uses 'blind' as a "
        "figure for sinful ministers; that use is not quoted and is flagged in the digest.",
    ),
]

# ================================================================= priestly-numbers
K["priestly-numbers"] = [
    item(
        "Easton: in David's time the priests were divided into twenty-four courses or classes (1 Chronicles 24:7-18), "
        "and the number was kept after the Captivity (Ezra 2:36-39; Nehemiah 7:39-42). Smith's: the priesthood was divided "
        "into twenty-four courses, each serving in rotation for one week, and 'the further assignment of special services "
        "during the week was determined by lot' (Luke 1:9).",
        "Easton's Bible Dictionary (1897), entry 'Priest'; Smith's Bible Dictionary (1884 edition), entry 'Priest'",
        [ev(EAS, "In the time of David the priests were divided into twenty-four courses or classes (1 Chr. 24:7-18). This number was retained after the Captivity"),
         ev(SMI, "each of which was to serve in rotation for one week, while the further assignment of special services during the week was determined by lot.")],
        "high",
        "Both are dictionary summaries of the biblical lists. Neither says how many priests were in a course.",
    ),
    item(
        "1 Chronicles 24:4-5 (in Henry's text): 'sixteen chief men of the house of their fathers' of Eleazar's sons and eight of "
        "Ithamar's, 'divided by lot, one sort with another'. Henry's comment: 'That which was to be determined by the lot "
        "was only the precedency, not who should serve (for they chose all the chief men), but who should serve first, and "
        "who next.' So the lot fixed the order of the courses, not who was in or out.",
        HENRY + "1 Chronicles 24",
        [ev(H2, "Among the sons of Eleazar there were sixteen chief men of the house of their fathers, and eight among the sons of Ithamar according to the house of their fathers."),
         ev(H2, "That which was to be determined by the lot was only the precedency, not who should serve (for they chose all the chief men), but who should serve first, and who next")],
        "high",
        "Henry's reading of the chapter. The Chronicler's 24-course system is dated by many scholars to after the exile (see "
        "the next item). The text does not say how many priests were in each of the 24.",
    ),
    item(
        "Josephus (Antiquities VII) gives the same arrangement: David found of the priests 'twenty-four courses, sixteen of "
        "the house of Eleazar, and eight of that of Ithamar'; each course ministered 'from sabbath to sabbath'; the courses "
        "were distributed by lot in the presence of David, Zadok and Abiathar, and the course that came up first was written "
        "down as the first.",
        "Josephus (Whiston), Antiquities of the Jews, Book VII, ch. 14, sect. 7",
        [ev(JA, "he found of these priests twenty-four courses, sixteen of the house of Eleazar, and eight of that of Ithamar; and he ordained that one course should minister to God eight days, from sabbath to sabbath."),
         ev(JA, "And thus were the courses distributed by lot, in the presence of David, and Zadok and Abiathar the high priests, and of all the rulers")],
        "high",
        "Josephus follows Chronicles closely and adds 'eight days' (a Sabbath to the next Sabbath, counted inclusively). He is "
        "writing about 1,000 years after the events he describes.",
    ),
    item(
        "Zechariah (Luke 1:5-9) was 'of the course of Abia' (the eighth course), and 'his lot was to burn incense'. Henry says "
        "David divided the family of Aaron into twenty-four courses 'that it might never be either neglected for want "
        "of hands or engrossed by a few'. Edersheim adds that Zechariah, a man of at least sixty, had never before been "
        "chosen to incense, and 'for the first, and for the last time in life the lot had marked him'.",
        HENRY + "Luke 1; Edersheim, Life and Times, Book II, ch. 1",
        [ev(H5, "he divided them into twenty-four courses, for the more regular performances of their office, that it might never be either neglected for want of hands or engrossed by a few."),
         ev(EDL, "never during these many years had he been honoured with the office of incensing"),
         ev(EDL, "For the first, and for the last time in life the lot had marked him for incensing")],
        "high",
        "Edersheim's detail comes from the Mishnah and from his own inference about Zechariah's age ('at least sixty "
        "winters'); Luke says only that he was well on in years. It shows that most priests might never be chosen for the "
        "incense, not that no sighted priest was ever passed over.",
    ),
    item(
        "Numbers, from Edersheim's note: if the total of the twenty-four courses of the officiating priesthood is reckoned at "
        "20,000, according to Josephus (Against Apion, ii. 8), and a little more than a third of each course came up for "
        "duty, 'this would give fifty priests for each week-day, while on the Sabbath the whole course would be on duty'. He "
        "calls this considerably more than the number required.",
        "Alfred Edersheim, The Life and Times of Jesus the Messiah, Book II, ch. 1, note 626",
        [ev(EDL, "If we reckon the total number in the twenty-four courses of, presumably, the officiating priesthood, at 20,000, according to Josephus (Ag. Ap. ii. 8)"),
         ev(EDL, "this would give fifty priests for each week-day, while on the Sabbath the whole course would be on duty.")],
        "medium",
        "A reckoning in a footnote, with assumptions (the one-third that came up, Josephus's 20,000). Edersheim also "
        "mentions a much larger Talmudic count that he calls exaggerated. It describes the late Second Temple, not the "
        "tabernacle in the wilderness.",
    ),
    item(
        "Smith's, on the numbers 'given by Jewish writers', if they are 'at all trustworthy': 'not fewer than 24,000 stationed "
        "permanently at Jerusalem, and 12,000 at Jericho', over and above the priests scattered in the country. Smith's also "
        "gives 22,000 Levites at the first consecration, 'almost exactly the number of the first-born males in the whole "
        "nation'. These are figures for a large order, though Smith's numbers are not the same as Edersheim's.",
        "Smith's Bible Dictionary (1884 edition), entries 'Priest' and 'Levites'",
        [ev(SMI, "Over and above those that were scattered in the country and took their turn there were not fewer than 24,000 stationed permanently at Jerusalem, and 12,000 at Jericho."),
         ev(SMI, "At the time of their first consecration there were 22,000 of them, almost exactly the number of the first-born males in the whole nation.")],
        "medium",
        "Smith's himself hedges these figures ('if we may accept'). They conflict with Edersheim's 20,000 total, so none "
        "should be treated as a headcount. The entry's next sentences describe the priests of the later period in "
        "disparaging terms, which are not quoted.",
    ),
    item(
        "Wikipedia's 'Priestly divisions' states that the 24 divisions are first listed in 1 Chronicles 24, that lots decided "
        "the order, that each order ministered for a week, and that all orders were present at the biblical festivals. "
        "It adds that many scholars see the courses as reflecting practice after the Babylonian captivity or as the "
        "Chronicler's idealised picture (written about 350 to 300 BCE), but that by the end of the Second Temple period "
        "'the divisions worked in the order specified'.",
        wsrc("Priestly divisions", "23 June 2026"),
        [ev(wk("Priestly_divisions"), "The 24 priestly divisions are first listed in"),
         ev(wk("Priestly_divisions"), "Lots were drawn to designate the order of Temple service for the different priestly orders according to 1 Chronicles 24:5."),
         ev(wk("Priestly_divisions"), "At the end of the [[Second Temple period]], it is clear that the divisions worked in the order specified.")],
        "high",
        "Scholarly dating of the system is disputed; the shelf's older sources (Henry, Easton, Josephus) take it as David's. "
        "The article's account of the Mishnah and Talmud is later reporting.",
    ),
    item(
        "The Levites, who did the carrying, guarding and singing, were a far larger group than the priests (22,000 at the "
        "first count in Smith's; Josephus has David assigning 23,000 to the building of the temple, 6,000 as judges and "
        "scribes, and 4,000 each as porters and singers). So a priesthood and a Levitical body of this size had many roles "
        "of different kinds, and the Temple's work was spread by rotation across thousands of people.",
        "Smith's Bible Dictionary (1884 edition), entry 'Levites'; Josephus (Whiston), Antiquities VII.14.7",
        [ev(SMI, "At the time of their first consecration there were 22,000 of them"),
         ev(JA, "twenty-three thousand to take care of the building of the temple, and out of the same, six thousand to be judges of the people and scribes, four thousand for porters to the house of God, and as many for singers")],
        "medium",
        "Josephus's figures follow 1 Chronicles 23 as he read it; Chronicles' numbers are often questioned by modern "
        "scholars. The point used here is only the scale and variety of the roles. Whether one blind priest would have been "
        "a burden on the others is not addressed by any source on the shelf.",
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
