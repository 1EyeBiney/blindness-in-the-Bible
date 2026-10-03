"""Build data/reference/law_and_life_candidates.json from quotes taken from the reference shelf.

Each item below is written by hand: a plain statement of what the shelf says, the
citation as a reader would see it, and one or more verbatim quotes. This script
finds each quote in its file (whitespace-insensitive), records the character offset
(line endings as LF, the same convention as place_and_time_candidates.json) and
refuses to write anything if a quote cannot be found.

    python src/build_law_candidates.py   -> data/reference/law_and_life_candidates.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
OUT = ROOT / "data" / "reference" / "law_and_life_candidates.json"

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
H6 = "matthew_henry_vol6.txt"
I1, I2, I5 = "isbe_1915_vol1.txt", "isbe_1915_vol2.txt", "isbe_1915_vol5.txt"
SM = "smiths_bible_dictionary.txt"
EA = "easton_ebd.txt"
SK = "edersheim_sketches.txt"
LT = "edersheim_life_and_times.txt"
JA = "josephus_antiquities_pg2848.txt"
JW = "josephus_wars_pg2850.txt"
HAM = "hammurabi_johns_pg17150.txt"
W_HAM = "wikipedia_Code_of_Hammurabi.wiki.txt"
W_EYE = "wikipedia_Eye_for_an_eye.wiki.txt"
W_GATE = "wikipedia_City_gate.wiki.txt"
W_SHI = "wikipedia_Shiloh_biblical_city.wiki.txt"
W_JAB = "wikipedia_Jabesh-Gilead.wiki.txt"
W_JER = "wikipedia_Jericho.wiki.txt"
W_SIL = "wikipedia_Pool_of_Siloam.wiki.txt"
W_TEM = "wikipedia_Second_Temple.wiki.txt"
W_BETH = "wikipedia_Pool_of_Bethesda.wiki.txt"
W_CULT = "wikipedia_Cultural_depictions_of_blindness.wiki.txt"
I3 = "isbe_1915_vol3.txt"

# ---------------------------------------------------------------- citations
def henry(on):
    return f"Matthew Henry, Commentary on the Whole Bible (1706-1721), on {on}"


def isbe(entry, loc=""):
    return f"International Standard Bible Encyclopaedia (1915), entry '{entry}'" + (f", {loc}" if loc else "")


def smith(entry):
    return f"Smith's Bible Dictionary (1884 edition), entry '{entry}'"


def easton(entry):
    return f"Easton's Bible Dictionary (1897), entry '{entry}'"


def wiki(title, rev, extra=""):
    return f"Wikipedia, '{title}', revision of {rev} (CC BY-SA 4.0)" + (f", {extra}" if extra else "")


W_HAM_SRC = wiki("Code of Hammurabi", "2 October 2026")
W_EYE_SRC = wiki("Eye for an eye", "2 October 2026")
JOHNS = "C. H. W. Johns (translator), The Oldest Code of Laws in the World (1903), Code of Hammurabi"
JOS_ANT = "Josephus, Antiquities of the Jews (Whiston translation)"
JOS_WAR = "Josephus, The Wars of the Jews (Whiston translation)"
ED_LT = "Edersheim, The Life and Times of Jesus the Messiah (1883)"
ED_SK = "Edersheim, Sketches of Jewish Social Life (1876)"

PERIOD_HENRY = ("Commentary of the early 18th century. Henry's wording about bodily 'blemishes' is dated and some of it "
                "is not suitable to repeat; the digest says which parts.")

DATA = {}

# ================================================================ law-stumbling-block
DATA["law-stumbling-block"] = [
    item("Matthew Henry reads Leviticus 19:14 as a command about the blind person's safety. To put a stumbling-block before "
         "a blind person, he says, is to add affliction to the afflicted and to make God's providence serve one's malice. "
         "He adds that the prohibition also implies a duty to help the blind and to remove stumbling-blocks from their way.",
         henry("Leviticus 19"),
         [ev(H1, "2. The safety of the blind we must likewise be tender of, and not put a stumbling-block before them; for this is to add affliction to the afflicted, and to make God's providence a servant to our malice."),
          ev(H1, "This prohibition implies a precept to help the blind, and remove stumbling-blocks out of their way.")]),
    item("Henry gives a reason the verse ends with 'fear thy God': the deaf and the blind cannot answer back or get even, so "
         "people who would never do this to someone who could retaliate need to be reminded that God sees and hears and "
         "'will plead their cause'. The reasoning is that the law protects people who cannot protect themselves.",
         henry("Leviticus 19"),
         [ev(H1, "Do not injure any because they are unwilling, or unable, to avenge themselves, for God sees and hears, though they do not."),
          ev(H1, "Thou dost not fear the deaf and blind, they cannot right themselves; but remember it is the glory of God to help the helpless, and he will plead their cause.")],
         caution="The second quotation is Henry quoting an unnamed Jewish saying; he does not say where it comes from."),
    item("For Deuteronomy 27:18 ('Cursed be he that maketh the blind to wander out of the way') Henry understands the "
         "offender as an adviser who, when asked the way, sends a trusting person somewhere that will harm him. He calls "
         "this barbarous and treacherous, and links it to Jesus's saying about the blind leading the blind. He also says the "
         "Jews held that by saying Amen to these curses the people bound themselves to keep the laws and to stop their neighbours "
         "breaking them.",
         henry("Deuteronomy 27"),
         [ev(H1, "who, when his advice is asked, maliciously directs his friend to that which he knows will be to his prejudice, which is making the blind to wander out of the way, under pretence of directing him in the way"),
          ev(H1, "which our Saviour has explained, Matt. xv. 14, The blind lead the blind, and both shall fall into the ditch."),
          ev(H1, "All the people, by saying this Amen, became bound for one another, that they would observe God's laws")],
         confidence="medium",
         caution="Henry takes the verse as being about misleading advice; the verse in the King James text is about 'the blind' and the "
                 "shelf does not say whether a literal blind traveller is meant. The 'Jews say' passage is Henry quoting Bishop Patrick quoting them."),
    item("The 1915 Bible encyclopaedia sums up the Law's two sides in one sentence: blindness disqualified a man from the "
         "priesthood (Leviticus 21:18), but care of the blind was specially enjoined (Leviticus 19:14) and wrongs against them "
         "were counted as breaches of the Law (Deuteronomy 27:18).",
         isbe("Blindness", "vol 1, pp. 487-488"),
         [ev(I1, "Blindness unfitted a man for the priesthood (Lev 21 18); but care of the blind was specially enjoined in the Law (Lev 19 14), and offences against them are regarded as breaches of Law (Dt 27 18).")]),
    item("Smith's and Easton's dictionaries both say the Law commanded compassion toward the blind and cite Leviticus 19:14 and "
         "Deuteronomy 27:18.",
         "Smith's Bible Dictionary (1884 edition), entry 'Blindness'; Easton's Bible Dictionary (1897), entry 'Blind'",
         [ev(SM, "The Jews were specially charged to treat the blind with compassion and care."),
          ev(EA, "The blind are to be treated with compassion (Lev. 19:14; Deut. 27:18).")],
         caution="Smith's prints the second reference as 'Leviticus 19:14; 27:18'; the second is plainly Deuteronomy 27:18."),
    item("Josephus, retelling the Law in the first century, puts the same concern in everyday terms: it is a duty to show the "
         "road to people who do not know it and not to treat it as a joke to send them the wrong way; and 'let no one revile "
         "a person blind or dumb'. This is Josephus's own summary, with details that are not in Leviticus.",
         f"{JOS_ANT}, Book IV, chapter 8, section 31-32",
         [ev(JA, "It is also a duty to show the roads to those who do not know them, and not to esteem it a matter for sport, when we hinder others' advantages, by setting them in a wrong way. 32. In like manner, let no one revile a person blind or dumb.")],
         caution="Josephus (about AD 93) is retelling, not translating; the sentence about the blind is his wording. 'Dumb' means unable to speak."),
    item("Hammurabi, king of Babylon, says in his prologue that the gods gave him "
         "his rule 'to prevent the strong from oppressing the weak', and the 1915 encyclopaedia says the epilogue calls him a "
         "helper of the oppressed and an adviser of widows and orphans. A search of the shelf found no mention of the blind in "
         "the Code: the word does not occur in Johns's English text.",
         f"{W_HAM_SRC}; {isbe('Hammurabi', 'vol 2, p. 1331')}",
         [ev(W_HAM, 'In the prologue, Hammurabi claims to have been granted his rule by the gods "to prevent the strong from oppressing the weak".'),
          ev(I2, "as a helper of the oppressed, as an ad- viser of widows and orphans, in short, as the father of his people.")],
         confidence="medium",
         caution="Johns (1903) leaves out the prologue and epilogue (he says so), so the shelf has the king's own claims only at second hand. "
                 "'No mention of the blind' is based on a search of the Johns text, which found no occurrence of 'blind'."),
]

# ================================================================ law-servant-blinded
DATA["law-servant-blinded"] = [
    item("Matthew Henry puts Exodus 21:26-27 under 'the care God took of servants'. If a master maimed a servant, even by "
         "striking out a tooth, the servant went free. Henry gives two purposes: to keep masters from abusing servants, since "
         "they would lose the servant's service, and to comfort a servant who was abused, because losing a limb meant gaining "
         "liberty, which would somewhat balance the pain and disgrace.",
         henry("Exodus 21"),
         [ev(H1, "II. The care God took of servants. If their masters maimed them, though it was only striking out a tooth, that should be their discharge, v. 26, 27."),
          ev(H1, "To comfort them if they were abused; the loss of a limb should be the gaining of their liberty, which would do something towards balancing both the pain and disgrace they underwent.")]),
    item("Smith's Bible Dictionary says in two places that the master's power over a servant was limited by this law: in "
         "'Law of Moses' that maiming gave liberty at once, and in 'Slave' that provision was made for the protection of the "
         "servant's person and that loss of an eye or a tooth was to be recompensed by giving the servant his liberty.",
         "Smith's Bible Dictionary (1884 edition), entries 'Law of Moses' and 'Slave'",
         [ev(SM, "Power of master so far limited that death under actual chastisement was punishable, (Exodus 21:20) and maiming was to give liberty ipso facto"),
          ev(SM, "provision was made for the protection of his person. (Exodus 21:20; Leviticus 24:17,22)"),
          ev(SM, "was to be recompensed by giving the servant his liberty.")],
         caution="The 'Slave' entry calls the loss of an eye or tooth a 'minor personal injury'. That phrase is not suitable to repeat; "
                 "the second quotation is cut to start after it."),
    item("Hammurabi's law for an eye lost between equals: 'If a man has caused the loss of a gentleman's eye, his eye one shall "
         "cause to be lost.' The class is part of the rule. The 1915 encyclopaedia quotes the same section with 'a free man' in place of Johns's 'gentleman'.",
         f"{JOHNS}, section 196; {isbe('Hammurabi', 'vol 2, p. 1331')}",
         [ev(HAM, "section 196. If a man has caused the loss of a gentleman's eye, his eye one shall cause to be lost."),
          ev(I2, "If a man destroy the eye of a free man, his eye shall be de- stroyed.")],
         caution="Johns renders the class term 'gentleman'; later translations use other words ('free man', 'awilum')."),
    item("Hammurabi sets lower penalties for the same injury when the victim is of lower rank. For a poor man who loses an eye "
         "the payment is one mina of silver (section 198); for the eye of a gentleman's servant the payment is half his price "
         "(section 199). Exodus 21:26 instead frees the servant. Johns's text does not say who receives the payment in 199.",
         f"{JOHNS}, sections 198-199",
         [ev(HAM, "section 198. If he has caused a poor man to lose his eye or shattered a poor man's limb, he shall pay one mina of silver."),
          ev(HAM, "section 199. If he has caused the loss of the eye of a gentleman's servant or has shattered the limb of a gentleman's servant, he shall pay half his price.")],
         caution="Johns writes 'servant' where the 1915 encyclopaedia and Wikipedia write 'slave'."),
    item("The same graded pattern holds for teeth, the other injury named in Exodus 21:27. Between equals the offender loses his "
         "tooth (section 200); for a poor man's tooth the fine is one-third of a mina of silver (section 201).",
         f"{JOHNS}, sections 200-201",
         [ev(HAM, "section 200. If a man has made the tooth of a man that is his equal to fall out, one shall make his tooth fall out. section 201. If he has made the tooth of a poor man to fall out, he shall pay one-third of a mina of silver.")]),
    item("The 1915 encyclopaedia (article by A. Ungnad) says Hammurabi's rules on wounding begin with the 'jus talionis', an "
         "eye for an eye, a bone for a bone, a tooth for a tooth, and that persons lower in the social grade usually accepted "
         "money instead (sections 196 and following).",
         isbe("Hammurabi", "vol 2, p. 1330"),
         [ev(I2, "occupies itself with wounding of all kinds, in the first place with the jus talionis: an eye for an eye, a bone for a bone, a tooth for a tooth. Persons lower in the social grade usually accepted money instead (§§ 196 ff).")]),
    item("Wikipedia's article on 'an eye for an eye' says that in Exodus 21, as in Hammurabi's Code, reciprocal justice seems to "
         "apply between social equals, and that Exodus then gives a different rule for a slave-owner who blinds a slave's eye or "
         "knocks out a tooth: the slave is freed.",
         W_EYE_SRC,
         [ev(W_EYE, "In Exodus 21, as in the [[Code of Hammurabi]], the concept of reciprocal justice seemingly applies to social equals;"),
          ev(W_EYE, "if a slave-owner blinds the eye or knocks out the tooth of a slave, the slave is freed but the owner pays no other consequence.")],
         confidence="medium",
         caution="The words 'pays no other consequence' are the Wikipedia editors' reading (they cite Michael Coogan, 2009); the "
                 "shelf has no commentary that says whether freedom was the whole remedy."),
    item("Josephus's version of the law of maiming (about AD 93) is that the offender suffers the same loss 'unless he that is "
         "maimed will accept of money instead of it', because the law lets the injured person judge the value of the loss.",
         f"{JOS_ANT}, Book IV, chapter 8, section 35",
         [ev(JA, "He that maimeth any one, let him undergo the like himself, and be deprived of the same member of which he hath deprived the other, unless he that is maimed will accept of money instead of it"),
          ev(JA, "for the law makes the sufferer the judge of the value of what he hath suffered")],
         confidence="medium",
         caution="This is Josephus's summary of the law for free persons and does not mention servants or eyes by name."),
    item("Hammurabi's Code also deals with eye operations. A doctor who opens an abscess of the eye with a bronze lancet and "
         "cures it takes ten shekels of silver (section 215); if the eye is lost, a doctor's hands are cut off when the patient is "
         "a gentleman (section 218), but for a poor man's slave he pays half the slave's price (section 220). The shelf's "
         "1915 encyclopaedia adds that Hammurabi's surgeon rules were 'an effective preventive against quacks'.",
         f"{JOHNS}, sections 215, 218, 220; {isbe('Hammurabi', 'vol 2, p. 1331')}",
         [ev(HAM, "or has opened an abscess of the eye for a gentleman with the bronze lancet and has cured the eye of the gentleman, he shall take ten shekels of silver."),
          ev(HAM, "has caused the loss of the gentleman's eye, one shall cut off his hands."),
          ev(HAM, "section 220. If he has opened his abscess with a bronze lancet and has made him lose his eye, he shall pay money, half his price."),
          ev(I2, "Certainly this law was an effective preventive against quacks!")],
         confidence="medium",
         caution="A side-find, not part of Exodus 21. The point for Brian is only that eyes were already being operated on, and sight lost "
                 "in the operating room had a penalty that depended on rank."),
]

# ================================================================ law-priest
DATA["law-priest"] = [
    item("Matthew Henry's text of Leviticus 21:22-23 shows what the priest with a blemish kept and what he lost: he 'shall eat the bread "
         "of his God, both of the most holy, and of the holy', but shall not go in to the veil or come near the altar.",
         henry("Leviticus 21 (text of verses 22-23 as printed by Henry)"),
         [ev(H1, "22 He shall eat the bread of his God, both of the most holy, and of the holy. 23 Only he shall not go in unto the vail, nor come nigh unto the altar, because he hath a blemish; that he profane not my sanctuaries")]),
    item("On the same verses Henry says the priest with a blemish was entitled to his share of the sacrifices, even the most "
         "holy things such as the show-bread and sin-offerings. His reason: the blemishes were ones the priest could not help, "
         "'therefore, though they might not work, they must not starve', and 'None must be abused for their natural infirmities.'",
         henry("Leviticus 21"),
         [ev(H1, "He shall eat of the sacrifices with the other priests, even the most holy things, such as the show-bread and the sin-offerings, as well as the holy things"),
          ev(H1, "The blemishes were such as they could not help, and therefore, though they might not work, they must not starve. Note, None must be abused for their natural infirmities.")],
         caution="Henry goes on to say 'the deformed child in the family must have its child's part'; 'deformed' is dated wording and is not "
                 "reproduced."),
    item("Henry notes that the list of blemishes mixed lasting ones, 'as blindness', with passing ones such as a scab, where the "
         "disability ceased when the condition cleared. His reason for the rule is about public appearance: it was 'requisite that "
         "comely men should be chosen to minister about holy things, for the sake of the people, who were apt to judge according to "
         "outward appearance'.",
         henry("Leviticus 21"),
         [ev(H1, "Divers blemishes are here specified; some that were ordinarily for life, as blindness; others that might be for a time, as a scurf or scab, and, when they were gone, the disability ceased."),
          ev(H1, "But it was especially requisite that comely men should be chosen to minister about holy things, for the sake of the people, who were apt to judge according to outward appearance, and to think meanly of the service")],
         confidence="medium",
         caution="The second quotation gives Henry's own reason (appearance and reputation of the sanctuary); the Bible text does not give a "
                 "reason in these verses. Henry's wording ('comely', 'disfigured') should not be adopted."),
    item("Henry's gospel application: people who live with such blemishes 'have reason to thank God that they are not thereby "
         "excluded from offering spiritual sacrifices to God', nor, if otherwise qualified, from the ministry.",
         henry("Leviticus 21"),
         [ev(H1, "Under the gospel, 1. Those that labour under any such blemishes as these have reason to thank God that they are not thereby excluded from offering spiritual sacrifices to God; nor, if otherwise qualified for it, from the office of the ministry.")],
         caution="In the next sentences Henry uses 'spiritually blind, and lame' as pictures of sinful ministers. That figure runs the two senses of "
                 "blindness together and is not repeated."),
    item("The 1915 encyclopaedia says the existence of a blemish in a man of priestly descent kept him from the priestly office, "
         "and that the same held for animals fit for sacrifice. It identifies the eye blemish of Leviticus 21:20 as cataract or "
         "white spots in the eye.",
         isbe("Blemish", "vol 1, pp. 486-487"),
         [ev(I1, "The existence of a blem ish in a person of priestly descent prevented him from the execution of the priestly office; similarly an animal fit for sacrifice was to be without blemish."),
          ev(I1, "cataract, white spots in the eye (Lev 21 20).")],
         caution="The identification with cataract is the encyclopaedia's (the Hebrew word is uncertain)."),
    item("Josephus, giving the law, says a priest with any blemish 'should have his portion indeed among the priests', but was "
         "forbidden to go up to the altar or into the holy house.",
         f"{JOS_ANT}, Book III, chapter 12, section 2",
         [ev(JA, "He ordered that the priest who had any blemish, should have his portion indeed among the priests, but he forbade him to ascend the altar, or to enter into the holy house.")]),
    item("Later rules about sight and the blessing. The 1915 encyclopaedia says that among those excluded from pronouncing the priestly "
         "blessing was one who 'was blind even of one eye'. Edersheim, describing synagogue worship, says the 'tephillah' (the prayer proper), "
         "'as well as the priestly benediction', could not be pronounced by those 'so blind as not to be able to discern daylight', and that the "
         "Mishnah directed that priests with blemishes on their hands were not to pronounce the benediction. That makes the rule a matter of degree.",
         f"{isbe('Benediction', 'vol 1, p. 435')}; {ED_SK}, chapter 17",
         [ev(I1, "If one was blind even of one eye, or had a defect in his hands or speech, or was a hunchback, he was also excluded."),
          ev(SK, "But the Mishnah already directs that priests having blemishes on their hands, or their fingers dyed, were not to pronounce the benediction"),
          ev(SK, "could not be pronounced by those who were not properly clothed, nor by those who were so blind as not to be able to discern daylight.")],
         confidence="medium",
         caution="The two sources disagree on how much sight was required (one eye versus daylight); neither says which period it describes. "
                 "Edersheim's sentence is in his chapter on synagogue prayer, so it may concern leading prayer there and not the Temple. He is reporting "
                 "rabbinic rules written down after the New Testament era."),
    item("Edersheim adds a related rule from the Mishnah: priests with blemishes on their hands, face or feet were not to pronounce the "
         "blessing, 'so as not to attract attention'; he adds that this 'presumably refers to those officiating in the Temple'.",
         f"{ED_LT}, Book III, chapter X",
         [ev(LT, "According to the Mishnah, they who pronounce the benediction must have no blemish on their hands, face, or feet, so as not to attract attention; but this presumably refers to those officiating in the Temple.")],
         confidence="medium",
         caution="Rabbinic rules, not the text of Leviticus. Edersheim writes of the Temple practice of the first century AD from later records."),
    item("Josephus records that the priestly blemish rule was used in his own history: in the first century BC Antigonus, brought back into Judea "
         "by the king of the Parthians, cut off the ears of his rival, the high priest Hyrcanus, so that the high priesthood 'should never come to him any more', "
         "'while the law required that this dignity should belong to none but such as had all their members entire'.",
         f"{JOS_ANT}, Book XIV, chapter 13, section 10",
         [ev(JA, "he cut off his ears, and thereby took care that the high priesthood should never come to him any more, because he was maimed, while the law required that this dignity should belong to none but such as had all their members entire")],
         confidence="medium",
         caution="The man was not blind, and the injury was inflicted to bar him, but it shows the law about the priesthood was still read "
                 "literally in the first century BC."),
]

# ================================================================ law-blind-animals
DATA["law-blind-animals"] = [
    item("Matthew Henry on Leviticus 22: the first of the four laws is that whatever was offered had to be without blemish, and the "
         "chapter now says what counted as a blemish: if the beast 'was blind, or lame, had a wen, or the mange' (verse 22).",
         henry("Leviticus 22"),
         [ev(H1, "Whatever was offered in sacrifice to God should be without blemish, otherwise it should not be accepted."),
          ev(H1, "Now here they are told what was to be accounted a blemish which rendered a beast unfit for sacrifice: if it was blind, or lame, had a wen, or the mange (v. 22)")]),
    item("Henry gives the reason as honour to God: everything used for his honour should be the best of its kind, 'he that is the best "
         "must have the best'. He adds that the law made the sacrifices fitter to be types of Christ, 'a Lamb without blemish and without spot' "
         "(1 Peter 1:19).",
         henry("Leviticus 22"),
         [ev(H1, "It was fit that every thing that was employed for his honour should be the best of the kind; for, as he is the greatest and brightest, so he is the best of beings; and he that is the best must have the best."),
          ev(H1, "In allusion to this law, he is said to be a Lamb without blemish and without spot, 1 Pet. i. 19.")]),
    item("Henry sets Israel's rule beside the neighbours' practice: 'The heathen priests were many of them not so strict in this matter, but "
         "would receive sacrifices for their gods that were ever so scandalous; but let strangers know that the God of Israel would not be so "
         "served.'",
         henry("Leviticus 22"),
         [ev(H1, "The heathen priests were many of them not so strict in this matter, but would receive sacrifices for their gods that were ever so scandalous; but let strangers know that the God of Israel would not be so served.")],
         confidence="medium",
         caution="Henry's claim about 'the heathen priests' is a general statement with no source given; the shelf has nothing to check it against."),
    item("Henry on Deuteronomy 15:21 ('if there be any blemish therein, as if it be lame, or blind'): a blemished firstling "
         "'must not be brought near the sanctuary' but 'must not be reared, but killed and eaten at their own houses as common food'. "
         "Verse 22 says the unclean and the clean person may eat it alike.",
         henry("Deuteronomy 15"),
         [ev(H1, "if there be any blemish therein, as if it be lame, or blind, or have any ill blemish, thou shalt not sacrifice it unto the Lord thy God. 22 Thou shalt eat it within thy gates: the unclean and the clean person shall eat it alike"),
          ev(H1, "it must not be brought near the sanctuary, nor used either for sacrifice or for holy feasting, for it would not be fit to honour God with, nor to typify Christ, who is a Lamb without blemish; yet it must not be reared, but killed and eaten at their own houses as common food")]),
    item("Malachi 1:8 and Henry's reading. The prophet says: 'if ye offer the blind for sacrifice, is it not evil? ... offer it now unto thy "
         "governor; will he be pleased with thee?' Henry reads it as an argument from honour: would they dare treat an earthly prince "
         "so, as a tribute or a present, and would he not take it as an affront?",
         henry("Malachi 1"),
         [ev(H4, "And if ye offer the blind for sacrifice, is it not evil? and if ye offer the lame and sick, is it not evil? offer it now unto thy governor; will he be pleased with thee, or accept thy person? saith the Lord of hosts."),
          ev(H4, 'Would they, durst they, affront an earthly prince thus? "You offer to God the lame and the sick; offer it now unto thy governor (v. 8), either as tribute or as a present')]),
    item("Easton's dictionary groups the two rules in one entry: 'Blemish' is an imperfection 'excluding men from the priesthood, and rendering "
         "animals unfit to be offered in sacrifice (Lev. 21:17-23; 22:19-25)'. The 1915 encyclopaedia says the same in one sentence.",
         f"{easton('Blemish')}; {isbe('Blemish', 'vol 1, pp. 486-487')}",
         [ev(EA, "excluding men from the priesthood, and rendering animals unfit to be offered in sacrifice (Lev. 21:17-23; 22:19-25)."),
          ev(I1, "similarly an animal fit for sacrifice was to be without blemish.")],
         caution="Easton's opening word for a blemish is a dated term for a bodily difference and is cut from the quotation."),
    item("Henry also reads the verse as a rule for worship: 'If our devotions are ignorant, and cold, and trifling, and full of "
         "distractions, we offer the blind, and the lame, and the sick, for sacrifice'. Here blindness stands for a poor offering.",
         henry("Leviticus 22"),
         [ev(H1, "If our devotions are ignorant, and cold, and trifling, and full of distractions, we offer the blind, and the lame, and the sick, for sacrifice; but cursed be the deceiver that does so")],
         confidence="medium",
         caution="This is the commentator's figure for poor worship. It uses 'the blind' as an image of something second-rate and should not be "
                 "carried over to people; included so Brian can see how the verse was applied."),
]

# ================================================================ life-camp
DATA["life-camp"] = [
    item("Smith's dictionary says that when the pasture near an encampment is used up the tents are taken down, packed on camels "
         "and moved, citing Genesis 26:17, 22 and 25, which are the passages about Isaac's moves.",
         smith("Tent"),
         [ev(SM, "When the pasture near an encampment is exhausted, the tents are taken down, packed on camels and removed. (Genesis 26:17,22,25; Isaiah 38:12)")]),
    item("Smith's describes the tent itself: a covering of black goat's hair, usually nine tent-poles in three groups, ropes fastened "
         "to pins driven in with a mallet, and a carpet partition dividing the tent in two. It also says that "
         "Arabs choosing a camp 'prefer the neighborhood of trees, for the sake of the shade and coolness'.",
         smith("Tent"),
         [ev(SM, "made of black goat's-hair"),
          ev(SM, "The tent-poles or columns are usually nine in number, placed in three groups"),
          ev(SM, "The ends of the tent-ropes are fastened to short sticks or pins, which are driven into the ground with a mallet."),
          ev(SM, "The tent is divided into two apartments, separated by a carpet partition drawn across the middle of the tent and fastened to the three middle posts."),
          ev(SM, "In choosing places for encampment, Arabs prefer the neighborhood of trees, for the sake of the shade and coolness which they afford. (Genesis 18:4,8)")],
         confidence="medium",
         caution="Describes the modern Arab tent as known to the 19th-century editors. Nothing on the shelf says what the layout, the ropes or "
                 "the pins meant for someone who could not see; that is for Brian or a later source."),
    item("Smith's on shepherds: in a nomadic society 'every man, from the sheikh down to the slave, is more or less a shepherd', and "
         "the work meant exposure to heat and cold, wild beasts and raiders.",
         smith("Shepherd"),
         [ev(SM, "In a nomadic state of society every man, from the sheikh down to the slave, is more or less a shepherd."),
          ev(SM, "He was exposed to the extremes of heat and cold, (Genesis 31:40)"),
          ev(SM, "he had to encounter the attacks of wild beasts, occasionally of the larger species"),
          ev(SM, "nor was he free from the risk of robbers or predators hordes.")]),
    item("Smith's on wells: they are usually cut into solid limestone, 'sometimes with steps to descend into them', with a stone curb "
         "or low wall round the mouth, and water is drawn with a rope and bucket or waterskin among other methods.",
         smith("Well"),
         [ev(SM, "Wells in Palestine are usually excavated from the solid limestone rock, sometimes with steps to descend into them. (Genesis 24:16)"),
          ev(SM, "The brims are furnished with a curb or low wall of stone"),
          ev(SM, "The rope and bucket, or waterskin. (Genesis 24:14-20; John 4:11)")],
         confidence="medium",
         caution="Describes wells of Palestine as seen in the 19th century. Genesis 26 is about wells in the Philistine country around Gerar and Beersheba."),
    item("Henry on Genesis 26: when the Philistines expelled Isaac and gave him 'continual molestation' and forced him to move from "
         "place to place, God visited him; Isaac 'pitched his tent there: and there Isaac's servants digged a well'. This is the "
         "setting a father moving between camps is in when Genesis 27 opens.",
         henry("Genesis 26"),
         [ev(H1, "And he builded an altar there, and called upon the name of the Lord, and pitched his tent there: and there Isaac's servants digged a well."),
          ev(H1, "When the Philistines expelled him, forced him to remove from place to place, and gave him continual molestation, then God visited him")],
         confidence="medium",
         caution="The first quotation is the King James text as printed by Henry; the second is Henry's comment. The link to Genesis 27 is the writer's."),
    item("Henry on Genesis 27:1: Esau 'though married, had not yet removed', and his parents had not expelled him despite grief over his "
         "marriage, so the blind father's household still had grown sons near it.",
         henry("Genesis 27"),
         [ev(H1, "He calls him to him, v. 1. For Esau, though married, had not yet removed; and, though he had greatly grieved his parents by his marriage, yet they had not expelled him")],
         confidence="medium",
         caution="Henry is explaining why Esau was within call; he says nothing about daily care of a blind man."),
    item("Smith's on caring for the infirm in Israel: 'Those who were indigent through bodily infirmities were usually taken care of by "
         "their kindred.' This is a general statement about the Hebrews, not about camps.",
         smith("Beggar, Begging"),
         [ev(SM, "Those who were indigent through bodily infirmities were usually taken care of by their kindred.")],
         confidence="medium",
         caution="General statement; 'usually' is Smith's hedge. Smith's gives no source for it."),
    item("The 1915 encyclopaedia on the setting for eye disease: the diseases are 'aggravated by sand, and the sun glare', purulent "
         "eye disease is spread by flies, and the blindness of old age 'probably from senile cataract' is named in Eli, Ahijah and Isaac.",
         isbe("Blindness", "vol 1, pp. 487-488"),
         [ev(I1, "All these diseases are aggravated by sand, and the sun glare, to which the unprotected inflamed eyes are exposed."),
          ev(I1, "a purulent ophthalmia, a highly infectious condition propagated largely by the flies"),
          ev(I1, "The blindness of old age, probably from senile cataract, is described in the cases of Eli at 98 years of age (1 S 3 2; 4 15), Ahijah (1 K 14 4), and Isaac (Gen 27 1).")],
         confidence="medium",
         caution="Written by a physician in 1915 who describes some conditions in language not repeated here; the medical claims are a century old."),
]

# ================================================================ life-village
DATA["life-village"] = [
    item("Smith's on Shiloh: it lay 'on the north side of Bethel, on the east side of the highway that goeth up from Bethel to Shechem "
         "and on the south of Lebonah' (Judges 21:19); the ark was kept there 'from the last days of Joshua to the time of Samuel', and it "
         "was one of the earliest and most sacred Hebrew sanctuaries.",
         smith("Shiloh"),
         [ev(SM, "Shiloh was one of the earliest and most sacred of the Hebrew sanctuaries."),
          ev(SM, "it is said that Shiloh is \"on the north side of Bethel, on the east side of the highway that goeth up from Bethel to Shechem and on the south of Lebonah.\"")]),
    item("Wikipedia's article says people made pilgrimages to Shiloh for major feasts and sacrifices and that Judges 21 records "
         "an annual dance of maidens among the vineyards there.",
         wiki("Shiloh (biblical city)", "26 September 2026"),
         [ev(W_SHI, "The people made [[pilgrimage]]s there for major feasts and sacrifices, and [[Judges 21]] records the place as the site of an annual dance of maidens among the [[vineyard]]s.")],
         caution="Wikipedia's account of the site's history is partly disputed in the article itself (it notes disagreement over the date and cause of its destruction)."),
    item("Henry's text of 1 Samuel 1:3 shows the yearly rhythm of the sanctuary town: Elkanah 'went up out of his city yearly to worship "
         "and to sacrifice unto the Lord of hosts in Shiloh'; Hannah brought Samuel's little coat 'from year to year'.",
         henry("1 Samuel 1-2 (text of the verses)"),
         [ev(H2, "And this man went up out of his city yearly to worship and to sacrifice unto the Lord of hosts in Shiloh."),
          ev(H2, "Moreover his mother made him a little coat, and brought it to him from year to year, when she came up with her husband to offer the yearly sacrifice.")],
         caution="Both quotations are the King James text as printed in Henry's volume, not Henry's own words."),
    item("Henry on 1 Samuel 3 pictures young Samuel sleeping 'in some closet near "
         "to Eli's room, as his page of the back-stairs, ready within call if the old man should want any thing in the night, perhaps to "
         "read to him if he could not sleep'. On this picture the household at the sanctuary supplied the help.",
         henry("1 Samuel 3"),
         [ev(H2, "Samuel had laid down to sleep, in some closet near to Eli's room, as his page of the back-stairs, ready within call if the old man should want any thing in the night, perhaps to read to him if he could not sleep."),
          ev(H2, "an affliction which came justly upon him for winking at his sons' faults")],
         confidence="medium",
         caution="The arrangement is Henry's picture, not stated in the text. In the sentence before it Henry says Eli's dim eyes 'came justly upon him for "
                 "winking at his sons' faults'; that links blindness to the person's sin and is the idea John 9:3 rejects. It is not repeated."),
    item("The text of 1 Samuel 4:13-18 as printed by Henry shows Eli at the town's entrance: he 'sat upon a seat by the wayside "
         "watching', heard the crying and asked 'What meaneth the noise of this tumult?', and 'fell from off the seat backward by the side of "
         "the gate'. At 98 'his eyes were dim, that he could not see.'",
         henry("1 Samuel 4 (text of the verses)"),
         [ev(H2, "lo, Eli sat upon a seat by the wayside watching: for his heart trembled for the ark of God."),
          ev(H2, "Now Eli was ninety and eight years old; and his eyes were dim, that he could not see."),
          ev(H2, "And when Eli heard the noise of the crying, he said, What meaneth the noise of this tumult?"),
          ev(H2, "he fell from off the seat backward by the side of the gate, and his neck brake, and he died")],
         caution="King James text as printed in Henry. 'Heard the noise' is what the verse says; the verse does not say who led or seated him."),
    item("Henry's text of 1 Kings 14:4-6 for Ahijah of Shiloh: 'Ahijah could not see; for his eyes were set by reason of his age', and "
         "'when Ahijah heard the sound of her feet, as she came in at the door', he spoke before she did.",
         henry("1 Kings 14 (text of the verses)"),
         [ev(H2, "But Ahijah could not see; for his eyes were set by reason of his age."),
          ev(H2, "when Ahijah heard the sound of her feet, as she came in at the door, that he said, Come in, thou wife of Jeroboam")],
         caution="King James text as printed in Henry. Brian has pointed out that the verse does not say he recognised her footsteps; the "
                 "verse leaves it open how he knew."),
    item("Smith's on the rural house: 'mere huts of mud or sunburnt bricks', usually one storey and often one room, "
         "sometimes with the cattle in the same building; windows 'small apertures high up in the walls'; flat roofs "
         "where booths of boughs are raised as sleeping-places in summer.",
         smith("House"),
         [ev(SM, "The houses of the rural poor in Egypt, as well as in most parts of Syria, Arabia and Persia, are generally mere huts of mud or sunburnt bricks."),
          ev(SM, "The houses are usually of one story only, viz., the ground floor, and often contain only one apartment."),
          ev(SM, "in some cases the cattle are housed in the same building"),
          ev(SM, "The windows are small apertures high up in the walls, sometimes grated with wood."),
          ev(SM, "upon the flat roofs, tents or \"booths\" of boughs or rushes are often raised to be used as sleeping-places in summer.")],
         confidence="medium",
         caution="Describes village houses of the 19th-century East; the Shiloh of Eli is some three thousand years earlier."),
    item("Smith's on roads: in the East 'the eastern roads are more like our paths', and on villages: Arab villages 'are often mere collections "
         "of stone huts'.",
         smith("Road; Village"),
         [ev(SM, "Where a travelled road is meant \"path\" or \"way\" is used, since the eastern roads are more like our paths."),
          ev(SM, "Arab villages, as found in Arabia, are often mere collections of stone huts")],
         confidence="medium",
         caution="Dictionary of 1863; general statement, not about Shiloh."),
]

# ================================================================ life-town-gate
DATA["life-town-gate"] = [
    item("The 1915 encyclopaedia on the gate: 'most of the men passed through the gate every day, and the gate was the place for meeting "
         "others and for assemblages'; open places near it were 'the centers of the public life', markets were held there, and the gate was "
         "the place of the legal tribunals.",
         isbe("Gate", "vol 2, p. 1170"),
         [ev(I2, "(2) As even farm laborers slept in the cities, most of the men passed through the gate every day, and the gate was the place for meeting others (Ruth 4 1; 2 S 15 2) and for assemblages."),
          ev(I2, "In particular, the \"gate\" was the place of the legal tribunals")]),
    item("Smith's on the gate: it was a place for public deliberation and justice and for markets, and gates 'were carefully guarded, "
         "and closed at nightfall'. Easton's adds that courts were 'frequently held' at the gates of cities, and that prophets delivered their messages there. "
         "The 1915 encyclopaedia thinks Jerusalem of the Jebusites was a small place 'encircled with powerful walls, with but one or perhaps two gates'.",
         f"{smith('Gate')}; {easton('Gate')}; {isbe('Jerusalem', 'vol 3, p. 1614')}",
         [ev(SM, "Places for public deliberation, administration of Justice, or of audience for kings and rulers or ambassadors."),
          ev(SM, "Public markets. (2 Kings 7:1)"),
          ev(SM, "Regarded therefore as positions of great importance, the gates of cities were carefully guarded, and closed at nightfall."),
          ev(EA, "At the gates of cities courts of justice were frequently held, and hence \"judges of the gate\" are spoken of"),
          ev(EA, "At the gates prophets also frequently delivered their messages"),
          ev(I3, "it is probable that Jerus was like other contemporary fortified sites, a compara- t ively small place encircled wit h power-"),
          ev(I3, "ful walls, with but one or perhaps two the Jebu- gates;")],
         confidence="medium",
         caution="The Jerusalem quotation is the 1915 writer's inference about the pre-Davidic city, not a statement about Israelite towns generally; the OCR "
                 "has the page's side-headings run into the sentence ('3. Site of ... the Jebu-')."),
    item("Wikipedia's article on city gates: they were built 'to provide a point of controlled access to and departure from a walled city for "
         "people, vehicles, goods and animals', and also displayed public information such as announcements and legal texts.",
         wiki("City gate", "27 September 2026"),
         [ev(W_GATE, "City gates were traditionally built to provide a point of controlled access to and departure from a walled city for people, vehicles, goods and animals."),
          ev(W_GATE, "The city gate was also commonly used to display diverse kinds of public information such as announcements, tax and toll schedules, standards of local measures, and legal texts.")],
         confidence="medium",
         caution="A general article on city gates in many countries and periods; only the opening description is used."),
    item("Henry on Job 29: Job's 'I was eyes to the blind' comes within a passage about the gate, the 'place of judgment', where "
         "'judgment was administered in the gate, in the street, in the places of concourse, to which every man might have a free "
         "access'. Henry reads 'eyes to the blind' as giving advice, 'counselling and advising those for the best that knew not what to do', "
         "and says we best help people in the very thing they lack.",
         henry("Job 29"),
         [ev(H3, "Observe, Judgment was administered in the gate, in the street, in the places of concourse, to which every man might have a free access"),
          ev(H3, "I was eyes to the blind, counselling and advising those for the best that knew not what to do"),
          ev(H3, "Those we best help whom we help out in that very thing wherein they are defective and most need help.")],
         caution="Henry reads 'the blind' figuratively (people without direction) and does not discuss a person who cannot see."),
    item("Henry on 1 Samuel 11: the Ammonite king offered the men of Jabesh-gilead a covenant if they would 'thrust out all your right "
         "eyes'. Henry explains the purpose: to disable them for war, because soldiers fought with shields in the left hand covering the left eye, "
         "'so that a soldier without his right eye was in effect blind'. Wikipedia says the townspeople were told they had 'a choice of death by sword or "
         "having their right eyes gouged out' and Smith's calls Jabesh 'the chief' of the cities of Gilead.",
         f"{henry('1 Samuel 11')}; {wiki('Jabesh-Gilead', '15 July 2026')}; {smith('Jabesh')}",
         [ev(H2, "They must disable them for war, and render them incapable, though not of labour (that would have been a loss to their lords), yet of bearing arms"),
          ev(H2, "so that a soldier without his right eye was in effect blind."),
          ev(W_JAB, "but were told by Nahash that they had a choice of death by sword or having their right eyes gouged out.")],
         confidence="medium",
         caution="Henry's explanation of the military reason is his own; the text says only that it was to be 'a reproach upon all Israel'."),
    item("Smith's on Jericho: its walls 'were so considerable that houses were built upon them'; Wikipedia says 'copious springs "
         "in and around the city have attracted human habitation for thousands of years'.",
         f"{smith('Jericho')}; {wiki('Jericho', '23 September 2026')}",
         [ev(SM, "Its walls were so considerable that houses were built upon them."),
          ev(W_JER, "Copious springs in and around the city have attracted human habitation for thousands of years.")]),
    item("Smith's on the street and the beggar's place: streets of an eastern town are 'generally narrow, "
         "tortuous and gloomy' and each street 'is locked up at night'; beggars 'were accustomed, it would seem, to have a fixed place at the corners "
         "of the streets, or at the gates of the temple, or of private houses'.",
         f"{smith('Street')}; {smith('Beggar, Begging')}",
         [ev(SM, "The streets of a modern Oriental town present a great contrast to those with which we are familiar, being generally narrow, tortuous and gloomy, even in the best towns."),
          ev(SM, "Each street and bazaar in a modern town is locked up at night; the same custom appears to have prevailed in ancient times."),
          ev(SM, "In later times beggars were accustomed, it would seem, to have a fixed place at the corners of the streets, (Mark 10:46) or at the gates of the temple, (Acts 3:2) or of private houses, (Luke 16:20)")],
         confidence="medium",
         caution="Smith's describes 'a modern Oriental town' of 1863 for the first quotation; the second is about 'later times', meaning New Testament times, not Job's or Jabesh's."),
    item("Josephus on the Jebusite walls: the inhabitants 'shut their gates, and placed the blind, and the lame, and all their maimed "
         "persons, upon the wall, in way of derision of the king'. Henry's alternative is that the blind and lame were invalid or maimed "
         "soldiers set on the walls 'in scorn of David'. The 1915 encyclopaedia thinks the words were a challenge, with David turning the "
         "term back on the Jebusites as a mocking name.",
         f"{JOS_ANT}, Book VII, chapter 3, section 1; {henry('2 Samuel 5')}; {isbe('Jerusalem', 'vol 3, p. 1614')}",
         [ev(JA, "shut their gates, and placed the blind, and the lame, and all their maimed persons, upon the wall, in way of derision of the king"),
          ev(H2, "Probably they set blind and lame people, invalids or maimed soldiers, to make their appearance upon the walls, in scorn of David and his men"),
          ev(I3, "challenged David: \"Thou shalt not come in hither, but the blind and the lame shall turn thee away\" (ver 6 in), and that David directed his followers to go up the \"watercourse\" and smite the \"lame and the blind\" \u2014 a term he in his turn applies mockingly to the Jebusites.")],
         confidence="medium",
         caution="This is a contested verse; the sources do not agree on whether real blind people were on the wall. Josephus is a late retelling."),
]

# ================================================================ life-jerusalem
DATA["life-jerusalem"] = [
    item("Edersheim on where the man born blind of John 9 probably sat: the entrance to the Temple 'was then ... the chosen spot for those who, "
         "as objects of pity, solicited charity', and he thinks the miracle took place at the entering to the Temple or on the Temple Mount. He "
         "says the blind beggar was probably asking 'in some such terms as these, which were common at the time: Gain merit by me'.",
         f"{ED_LT}, Book IV, chapter IX",
         [ev(LT, "the entrance to the Temple or its Courts was then - as that of churches is on the Continent - the chosen spot for those who, as objects of pity, solicited charity"),
          ev(LT, "Gain merit by me;' or, O tenderhearted, by me gain merit, to thine own benefit.")],
         confidence="medium",
         caution="Edersheim says 'presumably' and 'we can scarcely doubt'; it is his inference, not stated in John. 'Objects of pity' is his phrase."),
    item("Smith's on begging places: 'in later times beggars were accustomed ... to have a fixed place at the corners of the streets, ... "
         "or at the gates of the temple, or of private houses' (Mark 10:46, Acts 3:2, Luke 16:20). Smith's also says that in the Old Testament "
         "those poor through bodily infirmities were usually cared for by their kindred, and that a beggar 'was regarded and abhorred as a vagabond'.",
         smith("Beggar, Begging"),
         [ev(SM, "Those who were indigent through bodily infirmities were usually taken care of by their kindred."),
          ev(SM, "A beggar was sometimes seen, however, and was regarded and abhorred as a vagabond. (Psalms 109:10)"),
          ev(SM, "In later times beggars were accustomed, it would seem, to have a fixed place at the corners of the streets, (Mark 10:46) or at the gates of the temple, (Acts 3:2) or of private houses, (Luke 16:20)")],
         confidence="medium",
         caution="'Abhorred as a vagabond' is Smith's gloss on Psalm 109:10 and describes the Old Testament view of the wicked's children, not the "
                 "blind. Care or containment: the sources describe the places but do not say who chose them."),
    item("The 1915 encyclopaedia (article 'Begging', by Geo. B. Eager) says begging grew with the larger cities, that 'beggars formed a considerable "
         "class in the gospel age', and names the places: the entrance to Jericho, 'a gateway to pilgrims going up to Jerus to the great festivals', "
         "the neighbourhood of rich men's houses, and 'esp. the gates of the Temple'. It gives as causes the lack of any adequate system of "
         "relief, the lack of medical science and the resulting ignorance of remedies for common diseases like ophthalmia, and the Roman taxation.",
         isbe("Beg, Beggar, Begging", "vol 1, pp. 425-426"),
         [ev(I1, "Begging, however, came to be known to the Jews in the course of time with the development of the larger cities"),
          ev(I1, "Begging was well known and beggars formed a considerable class in the gospel age."),
          ev(I1, "which was a gateway to pilgrims going up to Jerus to the great festivals and in the neigh borhood of rich men's houses (Lk 16 20), and esp. the gates of the Temple at Jerus (Acts 3 2)."),
          ev(I1, "This prevalence of begging was due largely to the want of any adequate system of ministering relief, to the lack of any true medical science and the resulting ignorance of remedies for common dis eases like ophthalmia, for instance"),
          ev(I1, "and to the impoverishment of the land under the excessive taxation of the Rom government")],
         caution="The same entry goes on to describe modern European Jewish beggars in language that is prejudiced; none of that is used here."),
    item("Edersheim on charity in the Jewish towns: 'Alms were collected at regular times every week, either in money or in victuals', "
         "two people collecting and three distributing, 'so as to avoid the suspicion of dishonesty or partiality'; and a Rabbinic saying that when "
         "a poor man stands at your door, God stands at his right hand.",
         f"{ED_SK}, chapters 4 and 18",
         [ev(SK, "Alms were collected at regular times every week, either in money or in victuals. At least two were employed in collecting, and three in distributing charity, so as to avoid the suspicion of dishonesty or partiality."),
          ev(SK, "Whenever,\" we read, \"a poor man stands at thy door, the Holy One, blessed be His Name, stands at his right hand.")],
         confidence="medium",
         caution="Rabbinic sources written down after the New Testament; Edersheim writes that 'such collectors' were not employed in every synagogue."),
    item("Steps and courts of the Temple. Edersheim: 'Fifteen steps led up to the Upper Court' from the Court of the Women, where the Nicanor Gate "
         "was; Josephus: the second court 'was ascended to by fourteen steps from the first court', with further steps to the gates. Edersheim also says "
         "the Beautiful Gate 'formed the principal entrance into the Court of the Women' and that a 'flight of steps ... led from the Terrace into the "
         "Temple-building'. Easton's dictionary names 'the beautiful gate (Acts 3:2)' among the gates of the outer courts.",
         f"{ED_LT}, Book II chapter X, Book IV chapter VI and Book V chapter III; {JOS_WAR}, Book V, chapter 5, section 2; {easton('Gate')}",
         [ev(LT, "Fifteen steps led up to the Upper Court, which was bounded by a wall, and where was the celebrated Nicanor Gate, covered with Corinthian brass."),
          ev(JW, "was ascended to by fourteen steps from the first court"),
          ev(LT, "faced the Beautiful Gate,' that formed the principal entrance into the Court of the Women,' and so into the Sanctuary."),
          ev(LT, "had ascended the flight of steps which led from the Terrace' into the Temple-building.")],
         confidence="medium",
         caution="The two accounts disagree on the number of steps (fifteen, fourteen); both describe the Temple before AD 70. Edersheim's layout is a "
                 "reconstruction from rabbinic and Josephus sources, and the exact position of the 'Beautiful Gate' was disputed."),
    item("Pool and stair. Wikipedia says archaeologists in the 1880s found 'a stairway of 34 rock-hewn steps to the west of the Pool of "
         "Siloam leading up from a court in front of the Pool', and that the pool 'would have been a major gathering place' for pilgrims.",
         wiki("Pool of Siloam", "20 June 2026"),
         [ev(W_SIL, "noted that there was a stairway of 34 rock-hewn steps to the west of the Pool of Siloam leading up from a court in front of the Pool of Siloam."),
          ev(W_SIL, "the pool would have been a major gathering place for ancient Jews making religious pilgrimages to the city.")],
         confidence="medium",
         caution="The stair is described from 19th-century excavation of a pool that was rebuilt in the Roman era; its date is not given in these sentences."),
    item("Crowds and stepped approaches. Wikipedia says the Hasmoneans 'built wide, stepped roads designed to control the massive crowds "
         "and guide them smoothly toward the Temple gates', and that at Passover Jerusalem was packed with pilgrims 'perhaps numbering 300,000 to "
         "400,000'. Josephus (Wars, Book II) gives the crowd at one Passover as 'not fewer in number than three millions'.",
         f"{wiki('Second Temple', '19 September 2026')}; {JOS_WAR}, Book II, chapter 14, section 3",
         [ev(W_TEM, "the Hasmoneans built wide, stepped roads designed to control the massive crowds and guide them smoothly toward the Temple gates."),
          ev(W_TEM, "perhaps numbering 300,000 to 400,000."),
          ev(JW, "the people came about him not fewer in number than three millions")],
         confidence="medium",
         caution="The crowd numbers disagree by a factor of ten and are estimates; Josephus's are probably exaggerated."),
    item("Roads, terrain and the sound of crowds. Smith's quotes Dean Stanley that Jerusalem's ascent from any side but the south is 'perpetual'; "
         "Josephus says the hills around are 'surrounded by deep valleys' that are 'every where unpassable'; Edersheim describes the road from Jericho as "
         "'a rough, but still broad and well-defined mountain-track, winding over rock and loose stones; a steep declivity on the left'. At Jericho, "
         "Edersheim says, the blind men by the roadside 'heard the tramp of many feet and the sound of many voices'.",
         f"{smith('Jerusalem')}; {JOS_WAR}, Book V, chapter 4, section 1; {ED_LT}, Book V chapter I and Book IV chapter XXIV",
         [ev(SM, "But from any other side the ascent is perpetual"),
          ev(JW, "But on the outsides, these hills are surrounded by deep valleys, and by reason of the precipices to them belonging on both sides they are every where unpassable."),
          ev(LT, "It is now a rough, but still broad and well-defined mountain-track, winding over rock and loose stones; a steep declivity on the left"),
          ev(LT, "As they heard the tramp of many feet and the sound of many voices, they learned that Jesus of Nazareth was passing by.")],
         confidence="medium",
         caution="Edersheim describes the road as a traveller saw it in the 19th century and applies it to Jesus's last journey; his Jericho sentence is a "
                 "retelling of Luke 18:36-37 with the sounds added, and the verses do not say who told the blind men."),
]

# ================================================================ walk-by-faith
DATA["walk-by-faith"] = [
    item("Matthew Henry on 2 Corinthians 5:7: 'We have not the vision and fruition of God, as of an object that is present with us ... "
         "Faith is for this world, and sight is reserved for the other world: and it is our duty, and will be our interest, to walk by faith, till we "
         "come to live by sight.' For Henry the 'sight' is seeing God face to face after death.",
         henry("2 Corinthians 5:7"),
         [ev(H6, "Faith is for this world, and sight is reserved for the other world: and it is our duty, and will be our interest, to walk by faith, till we come to live by sight."),
          ev(H6, "We have not the vision and fruition of God, as of an object that is present with us, and as we hope for hereafter, when we shall see as we are seen.")],
         caution="Henry's 'sight' means the vision of God, not physical sight; he does not discuss blindness here. His 'opening our eyes in a world of glory' language is "
                 "his picture of death and is not used."),
    item("Henry sets the verse in Paul's argument: the chapter gives reasons they did not faint under afflictions, namely their 'expectation, "
         "desire, and assurance of happiness after death'. Believers, he says, 'are pilgrims and strangers in this world' and 'are absent from the "
         "Lord'; 'Faith will be turned into sight.'",
         henry("2 Corinthians 5"),
         [ev(H6, "The apostle proceeds in showing the reasons why they did not faint under their afflictions, namely, their expectation, desire, and assurance of happiness after death (ver. 1-5)"),
          ev(H6, "they are absent from the Lord (v. 6); they are pilgrims and strangers in this world; they do but sojourn here in their earthly home, or in this tabernacle"),
          ev(H6, "Faith will be turned into sight.")],
         confidence="medium",
         caution="Henry reads the passage mostly as about death and the life to come; the letter's wider context (afflictions, the 'earthly tent') is the "
                 "part that speaks of weakness."),
    item("The 1915 encyclopaedia on faith: pistis in the New Testament normally means 'reliance', 'trust'. On Hebrews 11:1 it denies that "
         "faith is 'a faculty of second sight' and says the faith of Abraham, Moses and Rahab 'was simply reliance upon a God known to be "
         "trustworthy', which 'enabled the believer to treat the future as present and the invisible as seen'.",
         isbe("Faith", "vol 2, pp. 1087-1088"),
         [ev(I2, "But in the over- whelming majority of cases, \"faith,\" as rendering pistis, means \"reliance,\" \"trust.\""),
          ev(I2, "This is sometimes interpreted as if faith, in the writer's view, were, so to speak, a faculty of second sight, a mysterious intuition into the spiritual world."),
          ev(I2, "was simply reliance upon a Cod known to be trustworthy. Such reliance enabled the believer to treat the future as present and the invisible as seen.")],
         confidence="medium",
         caution="The entry explains Hebrews 11:1; it does not discuss 2 Corinthians 5:7. The OCR reads 'Cod' for 'God'."),
    item("Easton's dictionary: faith's 'primary idea is trust. A thing is true, and therefore worthy of trust.'",
         easton("Faith"),
         [ev(EA, "Its primary idea is trust. A thing is true, and therefore worthy of trust.")]),
    item("The 1915 encyclopaedia's entry 'Walk' lists 2 Corinthians 5:7 under the figurative use of 'walk' for 'conduct and of spiritual "
         "states', next to 'walk in the light', 'walk in newness of life' and 'walk by the Spirit'.",
         isbe("Walk", "vol 5"),
         [ev(I5, "the word \"walk\" is used figuratively of conduct and of spiritual states."),
          ev(I5, "\"For we walk by faith, not by sight\" (2 Cor 5 7).")]),
    item("On the word for 'sight': the 1915 encyclopaedia glosses the Greek eidos as 'thing seen', 'external appearance', 'shape' and, in "
         "its entry 'Appearance', gives 'eidos = \"sight\"' for a verse in 1 Thessalonians. Neither entry discusses the eidos of 2 Corinthians 5:7.",
         f"{isbe('Fashion', 'vol 2, p. 1099')}; {isbe('Appearance', 'vol 1')}",
         [ev(I2, "lit. \"thing seen,\" \"external appearance,\" \"shape,\" is trd \"fashion\" in Lk 9 29"),
          ev(I1, "See also 1 Thess 6 22 ERVm (eidos = \"sight\").")],
         confidence="medium",
         caution="The shelf does not tell us what eidos means in 2 Corinthians 5:7. These are general glosses of the word elsewhere; the OCR prints the "
                 "1 Thessalonians reference as '6 22' for 5:22."),
]

# ================================================================ law-as-evidence
DATA["law-as-evidence"] = [
    item("Henry says the Jewish writers thought it impossible that anyone would be 'so barbarous as to put a stumbling-block in the "
         "way of the blind', and so read Leviticus 19:14 as a figure for giving bad advice. That is a reading in which the literal act "
         "was unthinkable, which cuts against taking the law as evidence of a common practice.",
         henry("Leviticus 19"),
         [ev(H1, "The Jewish writers, thinking it impossible that any should be so barbarous as to put a stumbling-block in the way of the blind, understood it figuratively, that it forbids giving bad counsel to those that are simple and easily imposed upon")],
         caution="Henry reports this; the shelf does not say who the 'Jewish writers' were or how early."),
    item("Henry on the servant's law: it was intended 'to prevent their being abused' and 'to comfort them if they were abused'. The "
         "second purpose assumes abuse happened; the first assumes masters could be deterred.",
         henry("Exodus 21"),
         [ev(H1, "This was intended, 1. To prevent their being abused; masters would be careful not to offer them any violence, lest they should lose their service."),
          ev(H1, "To comfort them if they were abused; the loss of a limb should be the gaining of their liberty")],
         confidence="medium",
         caution="This is Henry's reading of purpose; it is an argument from the law's wording, not evidence from a case."),
    item("Henry on the curses of Deuteronomy 27 says that some of them cover wrongs a magistrate 'could not take cognizance of', which "
         "God, 'who knows the heart', judges. The curse on those who make the blind wander is in the same list, and the people said Amen to each.",
         henry("Deuteronomy 27"),
         [ev(H1, "But to set light by them in his heart was a thing which the magistrate could not take cognizance of, and therefore it is here laid under the curse of God, who knows the heart.")],
         confidence="medium",
         caution="Henry says this about the curse on contempt of parents (verse 16), not about the blind; the use here is by analogy and is the writer's."),
    item("What neighbouring peoples did: Henry on 1 Samuel 11:2 says the Ammonites asked for the right eye of every man in Jabesh-gilead and "
         "explains that 'a soldier without his right eye was in effect blind'. Easton's says 'Conquerors sometimes blinded their captives' "
         "(2 Kings 25:7; 1 Samuel 11:2) and Smith's says blindness 'willfully inflicted for political or other purposes' is alluded to in Scripture.",
         f"{henry('1 Samuel 11')}; {easton('Blind')}; {smith('Blindness')}",
         [ev(H2, "so that a soldier without his right eye was in effect blind."),
          ev(EA, "Conquerors sometimes blinded their captives (2 Kings 25:7; 1 Sam. 11:2)."),
          ev(SM, "Blindness willfully inflicted for political or other purposes is alluded to in Scripture. (1 Samuel 11:2; Jeremiah 39:7)")],
         caution="Evidence for neighbours' warfare, not for how they treated blind people in daily life."),
    item("Hammurabi's Code and Moses: the 1915 encyclopaedia (A. Ungnad) says the parallels between Exodus and the Code are not accidental, "
         "'but just as little could one say that they are directly taken from the Code', and that 'numerous marked divergences also exist'. It "
         "compares Leviticus 24:19-20 with sections 196 and following of the Code.",
         isbe("Hammurabi", "vol 2, p. 1332"),
         [ev(I2, "One can hardly assert that the parallels quoted are accidental, but just as little could one say that they are directly taken from the Code; for they bear quite a definite impression due to the Israelitish culture, and numerous marked divergences also exist."),
          ev(I2, "Lev 24 19 f with CH, §§ 196 ff")],
         caution="A 1915 scholar's view; later scholarship has revised dating and relationships and none of that is on the shelf."),
    item("Wikipedia on what the Babylonian Code was: scholars have disputed whether it was legislation, a 'law report' of past cases, or "
         "'an abstract work of jurisprudence', the last having 'gained much support within Assyriology'. It also notes that the Code's laws are all "
         "'if ... then' cases and that 'unlike in the Mosaic Law, there are no apodictic laws (general commands)'. Leviticus 19:14 is a general command.",
         W_HAM_SRC,
         [ev(W_HAM, "Theories fall into three main categories: that it is [[legislation]], whether a [[code of law]] or a body of [[statute]]s; that it is a sort of [[law report]], containing records of past cases and judgments; and that it is an abstract work of [[jurisprudence]]."),
          ev(W_HAM, "The jurisprudence theory has gained much support within Assyriology."),
          ev(W_HAM, 'The laws are also strictly casuistic ("if{{nbsp}}... then"); unlike in the Mosaic Law, there are no apodictic laws (general commands).')],
         confidence="medium",
         caution="If the Code is a scholarly work and not enforced legislation, then its sections are weaker evidence of Babylonian practice than "
                 "once thought. Wikipedia presents this as a debate."),
    item("The 1915 encyclopaedia's entry 'Beg, Beggar, Begging' opens by saying it is significant that the Mosaic law 'contains no enactment "
         "concerning beggars, or begging', and that this omission 'certainly is not accidental'. It adds that begging 'came to be known to the Jews in the course "
         "of time with the development of the larger cities'. Easton's says 'there is no mention of beggars properly so called in the Old Testament'.",
         f"{isbe('Beg, Beggar, Begging', 'vol 1, p. 425')}; {easton('Beg')}",
         [ev(I1, "It is significant that the Mosaic law contains no enactment concerning beggars, or begging"),
          ev(I1, "This omis sion certainly is not accidental ; it comports with the very nature of the Mosaic law"),
          ev(I1, "Begging, however, came to be known to the Jews in the course of time with the development of the larger cities"),
          ev(EA, "there is no mention of beggars properly so called in the Old Testament")],
         confidence="medium",
         caution="Both entries are from 1897-1915; they argue from the absence of a law or a word, which is a weak sort of proof."),
    item("The same entry says the Mosaic provisions 'as far as actually practised, have always virtually done away with beggars and begging "
         "among the Jews', and that the spirit of the law is shown in the rule against driving a beggar away without alms.",
         isbe("Beg, Beggar, Begging", "vol 1, p. 425"),
         [ev(I1, "These laws, as far as actually practised, have always virtually done away with beggars and begging among the Jews."),
          ev(I1, "it is likewise forbidden to drive a beggar away without an alms")],
         confidence="medium",
         caution="'Always virtually' is more than a 1915 encyclopaedia could know, and the entry itself later records begging among the Jews in "
                 "the gospel age."),
    item("The Talmud, as described by Wikipedia, reasoned about the blind within the law: it rejected a literal reading of 'an eye for an eye' "
         "partly because it would be 'inapplicable to blind or eyeless offenders', and the Torah 'requires that penalties be universally "
         "applicable'. The argument is attributed to the Talmud (Bava Kamma 83b-84a).",
         W_EYE_SRC,
         [ev(W_EYE, "argues against the interpretations by [[Sadducees]] that the Bible verses refer to physical retaliation in kind, using the argument that such an interpretation would be inapplicable to blind or eyeless offenders.")],
         confidence="medium",
         caution="A late rabbinic argument, summarised by Wikipedia; it shows blind people were a thinkable test case for the law, not how they were treated."),
    item("Greek stories, as Wikipedia summarises them: gods inflict blindness as punishment, and 'sometimes, blind people in Greek mythology are "
         "granted special abilities by way of compensation', such as prophecy.",
         wiki("Cultural depictions of blindness", "13 August 2026"),
         [ev(W_CULT, "Sometimes, blind people in Greek mythology are granted special abilities by way of compensation.")],
         confidence="medium",
         caution="Myth is not evidence of practice. The shelf has nothing on how any neighbouring people actually treated blind persons."),
]

REQUIRED = ["law-stumbling-block", "law-servant-blinded", "law-priest", "law-blind-animals", "life-camp", "life-village",
            "life-town-gate", "life-jerusalem", "walk-by-faith", "law-as-evidence"]


def main():
    assert set(DATA) == set(REQUIRED), set(DATA) ^ set(REQUIRED)
    if FAILS:
        for f in FAILS:
            print("NOT FOUND", f)
        raise SystemExit(1)
    OUT.write_text(json.dumps(DATA, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    for k in REQUIRED:
        print(k, len(DATA[k]))


if __name__ == "__main__":
    main()
