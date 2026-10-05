"""Build data/reference/picture_candidates.json from quotes taken from the reference shelf.

Same method as build_law_questions_candidates.py: each item is written by hand (a plain statement of
what the shelf says, a citation, one or more verbatim quotes). This script finds each quote in its
file (whitespace-insensitive), records the character offset (line endings as LF) and refuses to
write anything if a quote cannot be found.

Keys are the seven pages of src/picture.py (blindness as a picture):
  blind-guides, eyes-that-cannot-see, gods-people-called-blind, like-the-blind,
  eyes-dim-with-grief, bribes-and-curses, eyes-opened

It also writes data/reference/picture_remarks.json: every place the shelf's commentators remark on
the relation between the figure and physical blindness (REMARKS), and a list of flagged passages
(FLAGGED) that are located and checked here but are not used as evidence anywhere. FLAGGED anchors
are short on purpose; the digest points to them and does not reproduce them at length.

    python src/build_picture_candidates.py   -> data/reference/picture_candidates.json
                                                data/reference/picture_remarks.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
OUT = ROOT / "data" / "reference" / "picture_candidates.json"
OUT_REM = ROOT / "data" / "reference" / "picture_remarks.json"

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

HENRY = "Matthew Henry, Commentary on the Whole Bible (1706-1721), on "
EDER = "Alfred Edersheim, The Life and Times of Jesus the Messiah (1883), "
OLD_OCR = ("The 1915 encyclopaedia text on the shelf is an OCR scan with occasional misread letters; "
           "quotations keep the scan's spelling and line-end hyphens.")
HENRY_NOTE = ("Henry is a commentator of 1706-1721 and writes from inside his own age: he reads the Pharisees "
              "as a type of corrupt church leaders of any time, and some of his phrases about the Jews of the "
              "Gospels are harsh and are not reproduced here (see the digest).")
EDER_NOTE = ("Edersheim (a Jewish-born Christian writing in 1883) sets the New Testament against Pharisaic Judaism "
             "throughout, and his language about Pharisees and 'Rabbinism' is often polemical; only the "
             "historical and exegetical statements are quoted here (see the digest).")

K = {}

# ================================================================= blind-guides
K["blind-guides"] = [
    item(
        "Henry on Matthew 15:14: the Pharisees are 'blind leaders of the blind' because they are ignorant of the "
        "spiritual meaning of the law and proud enough to lead anyway. He adds that if they had owned they were blind "
        "and come to Christ for eye-salve they might have seen. For Luke 6:39 he reads the same saying as a warning "
        "to those who put themselves under the guidance of the ignorant. Edersheim, on the same Matthew 15 scene, "
        "sums up the warning as 'the leadership of the blind by the blind', ending in ruin for both.",
        HENRY + "Matthew 15:12-14 and Luke 6:39-49; " + EDER + "Book III, ch. xxxi (Matt. xv.)",
        [ev(H5, "They are grossly ignorant in the things of God, and strangers to the spiritual nature of the divine law; and yet so proud, that they think they see better and further than any"),
         ev(H5, "Though they were blind, if they had owned it, and come to Christ for eye-salve, they might have seen, but they disdained the intimation of such a thing"),
         ev(H5, "Those who put themselves under the guidance of the ignorant and erroneous are likely to perish with them"),
         ev(EDL, "as being the leadership of the blind by the blind, [3414] which must end in ruin to both.")],
        "high",
        "All four quotes read the saying as being about knowledge and pride, never about people who cannot see. "
        "Henry's 'proud and ignorant' is his judgment on first-century Pharisees as a group. " + HENRY_NOTE,
    ),
    item(
        "What the oath about the Temple gold was (Matthew 23:16-22). Henry: the Pharisees allowed oaths by the temple "
        "and the altar but ruled that an oath by the temple itself did not bind, while an oath by the gold of the "
        "temple, or by the gift on the altar, did. His charge is that this pushed people to bring gold and gifts to "
        "the Temple treasury, which the teachers hoped to profit from. Edersheim calls this fourth woe a rebuke of "
        "the guides' 'moral blindness' rather than their hypocrisy, and says the precise allusion is not easy to "
        "understand: he thinks Jesus has in mind oaths and vows, where the casuistry was complicated.",
        HENRY + "Matthew 23:16-22; " + EDER + "Book V, ch. iv ('the eight woes')",
        [ev(H5, "They distinguished between an oath by the temple and an oath by the gold of the temple; an oath by the altar and an oath by the gift upon the altar; making the latter binding, but not the former."),
         ev(H5, "they preferred the gold before the temple, and the gift before the altar, to encourage people to bring gifts to the altar, and gold to the treasures of the temple, which they hoped to be gainers by."),
         ev(EDL, "The fourth Woe is denounced on the moral blindness of these guides rather than on their hypocrisy. From the nature of things it is not easy to understand the precise allusion of Christ.")],
        "medium",
        "Henry states the gold-versus-temple rule as fact without a source; Edersheim, who knows the Talmud, says "
        "the allusion is not easy to pin down. So the detail of the rule is Henry's account, not confirmed by "
        "Edersheim. Henry's motive charge (gain for the teachers) is his inference. " + HENRY_NOTE,
    ),
    item(
        "Henry on Romans 2:19: Paul's 'guide of the blind' is a boast the Jews of his day made of themselves, as "
        "teachers of the Gentiles who 'sat in darkness', and the rabbis made of themselves over the common people. "
        "The picture in the verse is Paul quoting their self-image back to them, not Paul calling anyone blind.",
        HENRY + "Romans 2:17-29",
        [ev(H6, "They thought themselves guides to the poor blind Gentiles that sat in darkness, were very proud of this, that whoever would have the knowledge of God must be beholden to them for it.")],
        "high",
        "Henry writes 'the poor blind Gentiles': here 'blind' means Gentiles without the Scriptures, and 'poor' is "
        "his pity. It is a figurative use that takes nothing from physical blindness, but the phrase reads "
        "oddly now. " + HENRY_NOTE,
    ),
    item(
        "The 'gnat and camel' (Matthew 23:24). Easton: the Jews carefully filtered their wine, because the law (Lev. "
        "11:23) forbade insects as unclean, and yet omitted the weightier matters of the law. The 1915 encyclopaedia "
        "reads the saying the same way, as inconsistency in taking pains over food while neglecting weightier matters. "
        "Edersheim ties it to tithing: the Pharisees' rule extended the law of tithes to the smallest garden herbs "
        "such as anise, and he sets that beside the omission of judgement, mercy and faith. Henry: it is not the "
        "scruple over a little sin that Christ condemns, but doing that and then swallowing a camel.",
        "Easton's Bible Dictionary (1897), entries 'Gnat' and 'Camel'; International Standard Bible Encyclopaedia (1915), "
        "'Gnat'; " + EDER + "Book V, ch. iv; " + HENRY + "Matthew 23:23-24",
        [ev(EAS, "The Jews carefully filtered their wine before drinking it, for fear of swallowing along with it some insect forbidden in the law as unclean"),
         ev(EAS, "The custom of filtering wine for this purpose was common among the Jews. It was founded on Lev. 11:23."),
         ev(I2, "in taking extraordinary pains in some things, as in the preparation of food, while leaving weightier matters unattended to"),
         ev(EDL, "which extended the mosaic law of tithing, in most burdensome minuteness, even to the smallest products of the soil that were esculent and could be preserved, [5276] such as anise."),
         ev(H5, "It is not the scrupling of a little sin that Christ here reproves; if it be a sin, though but a gnat, it must be strained at")],
        "high",
        "Easton and the encyclopaedia describe the wine-straining as a general Jewish practice; neither is a first-century "
        "source and neither cites one. "
        + OLD_OCR + " " + EDER_NOTE,
    ),
    item(
        "The hand-washing that set off Matthew 15 (Henry and Edersheim agree on the facts). Henry: the tradition was "
        "that people should wash their hands often and always before meat, and the Pharisees made it a matter of "
        "conscience and a sin to omit. Edersheim: the practice is 'expressly admitted' to have been a tradition of the "
        "elders and not a law of Moses; it seems first to have been enjoined to keep sacred offerings from being "
        "eaten in defilement; and some Rabbis defended washing after the meal on health grounds, because something "
        "left on the hands might injure the eyes.",
        HENRY + "Matthew 15:1-9; " + EDER + "Book III, ch. xxxi",
        [ev(H5, "That people should often wash their hands, and always at meat. This they placed a great deal of religion in, supposing that the meat they touched with unwashen hands would be defiling to them."),
         ev(EDL, "this practice is expressly admitted to have been, not a Law of Moses, but a tradition of the elders"),
         ev(EDL, "it seems to have been first enjoined in order to ensure that sacred offerings should not be eaten in defilement."),
         ev(EDL, "which some, indeed, explained on sanitary grounds, as there might be left about the hands what might prove injurious to the eyes.")],
        "high",
        "This is the occasion of the saying in Matthew 15:14, not a comment on the blind. The eye remark is "
        "Edersheim's report of one Rabbinic explanation. " + EDER_NOTE,
    ),
    item(
        "The setting of the woes (Matthew 23). Edersheim: it is the third day of Passion Week, 'the last day in the "
        "Temple', after the Sadducees' question and the great-commandment exchange; the woes close the public "
        "ministry as the Beatitudes opened it, eight woes for eight beatitudes. Henry makes the same count, eight woes "
        "'in opposition to the eight beatitudes'. Edersheim notes that verse 14 is probably not original but the "
        "woe is found in Mark 12:40 and Luke 20:47.",
        EDER + "Book V, ch. iv (heading, and the paragraph beginning 'It was not a break in the Discourse'); " + HENRY + "Matthew 23:13-33",
        [ev(EDL, "THE THIRD DAY IN PASSION-WEEK - THE LAST CONTROVERSIES AND DISCOURSES - THE SADDUCEES AND THE RESURRECTION - THE SCRIBE AND THE GREAT COMMANDMENT"),
         ev(EDL, "THE last day in the Temple was not to pass without other temptations"),
         ev(EDL, "Corresponding to the eight Beatitudes in the Sermon on the Mount with which His public Ministry began, He now closed it with eight denunciations of woe."),
         ev(H5, "but here are eight woes, in opposition to the eight beatitudes"),
         ev(EDL, "Although St. Matt. xxiii. 14 is in all probability spurious, this woe' occurs in St. Mark xii. 40, and in St. Luke xx. 47.")],
        "high",
        "Edersheim says verse 14 is probably not original, so whether the woes number seven or eight depends on "
        "the text one reads; both commentators on the shelf count eight. " + EDER_NOTE,
    ),
    item(
        "Who the 'watchmen' were (Isaiah 56:10, 'His watchmen are blind'). Henry: they should have been the watchmen of the "
        "flock, to see the beasts coming and keep them off; the phrase may mean the false prophets and priests of "
        "Isaiah's day, or the wicked princes, or, in Jesus' time, the chief priests and scribes who should have "
        "discerned the signs of the times. He ties it to Matthew 15:14. The 1915 encyclopaedia defines a watchman as a "
        "sentinel on the city walls (or the hilltops), so the figure is of a guard who cannot see danger.",
        HENRY + "Isaiah 56:9-12; International Standard Bible Encyclopaedia (1915), 'Watchman'",
        [ev(H4, "should have been the watchmen of the flock, to discover the approaches of the beasts of prey, to keep them off, and protect the sheep"),
         ev(H4, "Or it may refer to those who were the nation's watchmen in our Saviour's time, the chief priests and the scribes, who should have discerned the signs of the times and have given notice to the people of the approach of the Messiah"),
         ev(H4, "Christ describes the Pharisees to be blind leaders of the blind, Matt. xv. 14."),
         ev(I5, "a sentinel on the city walls")],
        "high",
        "Henry is offering three possible referents, not choosing one. The encyclopaedia gives the office; it does "
        "not comment on Isaiah's use of the picture. " + OLD_OCR,
    ),
    item(
        "Henry on blind Ahijah and what the figure takes for granted. In 1 Kings 14, Jeroboam sends his wife in disguise "
        "to Ahijah of Shiloh, 'blind through age'. Henry says Ahijah was 'yet still blest with the visions of the "
        "Almighty, which need not bodily eyes, but are rather favoured by the want of them'. The 1915 encyclopaedia "
        "lists Ahijah with Eli and Isaac as cases of the blindness of old age, 'probably from senile cataract'. "
        "So Henry treats an actual blind guide as seeing well in the way that matters for prophecy.",
        HENRY + "1 Kings 14:1-20; International Standard Bible Encyclopaedia (1915), 'Blindness' (Alex. Macalister)",
        [ev(H2, "blind through age, yet still blest with the visions of the Almighty, which need not bodily eyes, but are rather favoured by the want of them, the eyes of the mind being then most intent and least diverted."),
         ev(I1, "The blindness of old age, probably from senile cataract, is described in the cases of Eli at 98 years of age")],
        "high",
        "This is Henry's remark on one man, not a general claim, and it is a comment on Ahijah, not on Matthew 23. "
        "The 'cataract' diagnosis is the encyclopaedia author's guess. " + OLD_OCR,
    ),
]

# ================================================================= eyes-that-cannot-see
K["eyes-that-cannot-see"] = [
    item(
        "Henry on John 9:39: the verse 'explains' a 'great truth by a metaphor borrowed from the miracle' just wrought. "
        "Christ came to give sight to those 'spiritually blind', revealing the object by his word and healing the "
        "organ by his Spirit, and the other half, 'that those who see might be made blind', is the sealing up in "
        "ignorance of those with a high opinion of their own wisdom. Henry says the Gentiles who had long lacked "
        "revelation might see, and 'the Jews, who had long enjoyed it' might have it hidden from them.",
        HENRY + "John 9:39-41",
        [ev(H5, "This great truth he explains by a metaphor borrowed from the miracle which he had lately wrought. That those who see not might see, and that those who see might be made blind."),
         ev(H5, "Intentionally and designedly to give sight to those that were spiritually blind; by his word to reveal the object, and by his Spirit to heal the organ"),
         ev(H5, "those who have a high conceit of their own wisdom, and set up that in contradiction to divine revelation, might be sealed up in ignorance and infidelity"),
         ev(H5, "the Gentiles, who had long been destitute of the light of divine revelation, might see it; and the Jews, who had long enjoyed it, might have the things of their peace hid from their eyes")],
        "high",
        "Henry applies the verse to 'nations and people' as well as individuals, which brings in the Jew-Gentile contrast "
        "he repeats throughout (see the digest's flagged section). The word 'metaphor' is his; it is the clearest "
        "statement on the shelf that the John 9 saying is a figure drawn from a physical healing. " + HENRY_NOTE,
    ),
    item(
        "Henry on John 9:41, 'If you were blind, you would have no sin'. He gives two readings. If they had been "
        "really ignorant, their guilt would be lighter: 'invincible ignorance, though it does not justify sin, excuses "
        "it, and lessens the guilt'. Or, if they had known they were blind, they would have accepted Christ as guide. "
        "He concludes that 'those are most blind who will not see', and that those who fancy they see are in the most "
        "danger.",
        HENRY + "John 9:39-41",
        [ev(H5, "The times of ignorance God winked at; invincible ignorance, though it does not justify sin, excuses it, and lessens the guilt."),
         ev(H5, "Those that are convinced of their disease are in a fair way to be cured, for there is not a greater hindrance to the salvation of souls than self-sufficiency."),
         ev(H5, "And as those are most blind who will not see, so their blindness is most dangerous who fancy they do see.")],
        "high",
        "Henry's 'those who will not see' is the line the whole page turns on: the blindness here is a refusal. "
        "He also says 'the poor Gentiles' might be called blind in the excusable sense. " + HENRY_NOTE,
    ),
    item(
        "Edersheim on John 9:39-41 and the place of the miracle. He thinks the healing happened at the Temple "
        "entrance, where beggars sat, on the Sabbath after the Feast of Tabernacles, and that the man's begging "
        "plea may have been 'Gain merit by me'. He writes that the blind 'were regarded as specially entitled to charity'. "
        "On the verdict: the Pharisees' blindness 'was not the calamity of blindness' but a blindness 'in which "
        "they were guilty', 'the result of their deliberate choice'; he also speaks of 'the blindness of judgment' "
        "that fell on the leaders.",
        EDER + "Book IV, ch. ix (The Healing of the Man Born Blind)",
        [ev(EDL, "we can scarcely doubt that the miracle took place at the entering to the Temple, or on the Temple-Mount."),
         ev(EDL, "Gain merit by me;' or, O tenderhearted, by me gain merit, to thine own benefit."),
         ev(EDL, "It was the Sabbath - the day after the Octave of the Feast"),
         ev(EDL, "Indeed, the blind were regarded as specially entitled to charity;"),
         ev(EDL, "It was not the calamity of blindness; but it was a blindness in which they were guilty, and for which they were responsible, [4171] which indeed was the result of their deliberate choice: therefore their sin - not their blindness only - remained!"),
         ev(EDL, "to the blindness of judgment which had fallen on those who were the leaders of Israel!")],
        "high",
        "Edersheim says the Temple-gate setting rests on 'strong presumption' and he 'cannot offer actual proof'. "
        "His sentence separating 'the calamity of blindness' from guilty blindness is the single most direct "
        "answer on the shelf to the question of what the picture assumes about blind people. " + EDER_NOTE,
        ),
    item(
        "John 12:37-41, 'they could not believe', on Isaiah's blinded eyes. Henry: 'They could not believe, that is, they "
        "would not', with Chrysostom and Augustine; and in the second sense he allows 'a righteous hand of God' in the "
        "blinding of those who persist in unbelief, a judgment on resistance already made. Edersheim: 'they did not "
        "believe, because they could not believe', after a long history of resisting; he adds in a note that "
        "the sentence is 'decreed' but 'not decreed beforehand, and irrespective of their conduct'. He also "
        "observes in an appendix that the Targum gives the Isaiah 6 words to God's Memra (Word), which "
        "John 12:40 applies to Christ.",
        HENRY + "John 12:37-41; " + EDER + "Book V, ch. iii (summary of the public ministry) and Appendix II (Philo and Rabbinic theology)",
        [ev(H5, "They could not believe, that is, they would not; they were obstinately resolved in their infidelity"),
         ev(H5, "There is a righteous hand of God sometimes to be acknowledged in the blindness and obstinacy of those who persist in impenitency and unbelief"),
         ev(EDL, "In face of the clearest evidence, they did not believe, because they could not believe."),
         ev(EDL, "We say decreed' - but not decreed beforehand, and irrespective of their conduct."),
         ev(EDL, "It is intensely interesting to notice that in St. John xii. 40, these words are prophetically applied in connection with Christ.")],
        "medium",
        "The 'could not' passage is a hard one and both commentators handle it as theology, not as a statement about "
        "the eyes. Henry's own phrase 'hard saying' is his. Edersheim's footnote number [5161] points to this "
        "note. Both speak of 'Israel' or 'the Jews' as a body in terms that are harsh: not reproduced here. "
        + HENRY_NOTE + " " + EDER_NOTE,
    ),
    item(
        "Henry on Romans 11:7-10, 'the rest were blinded'. He says the gospel was 'the savour of life unto life' to "
        "believers and 'death unto death' to the unbelieving, 'the same sun softens wax and hardens clay'. On Isaiah's "
        "'eyes that they should not see' he says 'They had the faculties, but in the things that belonged to their "
        "peace they had not the use of those faculties': the same kind of blindness as 'senselessness', in "
        "his words. He distinguishes their sin ('they shut their eyes') from their punishment ('God... blinded their "
        "eyes').",
        HENRY + "Romans 11:7-10",
        [ev(H6, "They had the faculties, but in the things that belonged to their peace they had not the use of those faculties; they were quite infatuated, they saw Christ, but they did not believe in him"),
         ev(H6, "The same sun softens wax and hardens clay."),
         ev(H6, "Blindness and hardness are expressive of the same senselessness and stupidity of spirit."),
         ev(H6, "They shut their eyes, and would not see; this was their sin: and then God, in a way of righteous judgment, blinded their eyes, that they could not see; this was their punishment.")],
        "medium",
        "Henry's sentence about 'senselessness and stupidity of spirit' equates blindness with mental dullness: it is "
        "a flagged line for what it assumes about the word, even though he means the figure. The rest of this "
        "passage in Henry speaks of 'the Jews' in terms that are not reproduced (see the digest). " + HENRY_NOTE,
    ),
    item(
        "Henry on 2 Corinthians 4:4 and 1 John 2:9-11. Paul's 'god of this world has blinded the minds of the unbelieving' "
        "is read as the devil darkening the understanding 'with ignorance, and error, and prejudices', which keeps the "
        "light of the gospel out of the heart. On 1 John 2:11, 'darkness hath blinded his eyes', Henry says the one who "
        "hates his brother 'knows not whither he goes' and 'the mind, the judgment, and the conscience will be "
        "darkened'.",
        HENRY + "2 Corinthians 4:1-7 and 1 John 2:7-11",
        [ev(H6, "They are under the influence and power of the devil, who is here called the god of this world"),
         ev(H6, "so he darkens the understandings of men, and increases their prejudices, and supports his interest by keeping them in the dark, blinding their minds with ignorance, and error, and prejudices"),
         ev(H6, "where that darkness dwells, the mind, the judgment, and the conscience will be darkened, and so will mistake the way to heavenly endless life")],
        "high",
        "Both are figurative uses about the mind and conscience; Henry does not discuss physical blindness at all in "
        "either place. " + HENRY_NOTE,
    ),
    item(
        "Henry on 2 Peter 1:9, 'he that lacketh these things is blind': he says 'blind, that is, as to spiritual and "
        "heavenly things, as the next words explain it'. The next words are 'cannot see afar off'; Henry reads that as a "
        "man who sees this present world and 'dotes upon' it but has no sense of the world to come. The 1915 "
        "encyclopaedia, in its Blindness entry, says the word is used as a verb ('as Jn 12 40') 'usually in the "
        "sense of obscuring spiritual perception', while for physical blindness it appears as a noun or adjective.",
        HENRY + "2 Peter 1:5-11; International Standard Bible Encyclopaedia (1915), 'Blindness' (Alex. Macalister)",
        [ev(H6, "blind, that is, as to spiritual and heavenly things, as the next words explain it: He cannot see far off."),
         ev(H6, "This present evil world he can see, and dotes upon, but has no discerning at all of the world to come"),
         ev(I1, "The word blind is used as a vb., as Jn 12 40, usually in the sense of ob scuring spiritual perception. In reference to physi cal blindness it is used as a noun frequently or else as an adj. with the noun man.")],
        "high",
        "The encyclopaedia's grammatical observation (verb for the figure, noun and adjective for the condition) is a "
        "statement about usage in its author's judgment, in the English Bible. It is not checked here against the Greek. "
        + OLD_OCR,
    ),
    item(
        "The contrast that matters for who is called blind. On Matthew 9:27 (the two blind men who call Jesus Son of "
        "David) Henry writes that while the chief priests and Pharisees would not see, 'They who, by the providence of "
        "God, are deprived of bodily sight, may yet, by the grace of God, have the eyes of their understanding so "
        "enlightened'. On John 9 he says the healed man, asking who the Son of God is, had received 'bodily "
        "sight' and that the 'greatest comfort of bodily eyesight is its serviceableness to our faith'; he "
        "adds 'If we apply this to the opening of the eyes of the mind' it means spiritual sight is given chiefly "
        "that we may see Christ.",
        HENRY + "Matthew 9:27-31 and John 9:35-38",
        [ev(H5, "They could not see him and his miracles, but faith comes by hearing. Note, They who, by the providence of God, are deprived of bodily sight, may yet, by the grace of God, have the eyes of their understanding so enlightened"),
         ev(H5, "Note, The Greatest comfort of bodily eyesight is its serviceableness to our faith and the interests of our souls."),
         ev(H5, "If we apply this to the opening of the eyes of the mind, it intimates that spiritual sight is given principally for this end, that we may see Christ")],
        "high",
        "Henry's second remark assumes sight's chief value is its use to faith, and he says the man 'might have returned "
        "contentedly to his former blindness': a line flagged in the digest, not quoted. The first remark is "
        "exactly the contrast: the physically blind see, the leaders do not. " + HENRY_NOTE,
    ),
]

# ================================================================= gods-people-called-blind
K["gods-people-called-blind"] = [
    item(
        "Henry on Isaiah 29:9-10, 'blind', 'drunken, but not with wine', 'a spirit of deep sleep'. He reads this as the "
        "prophets, rulers and seers 'themselves blindfolded' and adds 'it is easy to tell what the fatal consequences will be "
        "when the blind lead the blind', applying it to the chief priests, scribes and elders who opposed Christ. "
        "The sleep is God's judgment 'to punish them for their loving darkness rather than light, their loving sleep'.",
        HENRY + "Isaiah 29:9-16",
        [ev(H4, "that those who should have been their guides were themselves blindfolded; and it is easy to tell what the fatal consequences will be when the blind lead the blind."),
         ev(H4, "but it is in away of righteous judgment, to punish them for their loving darkness rather than light, their loving sleep."),
         ev(H4, "This was fulfilled when, in the latter days of the Jewish church, the chief priests, and the scribes, and the elders of the people, were the great opposers of Christ and his gospel")],
        "high",
        "Henry reads Isaiah 29:10 as already prophesying the leaders of Jesus's day, which is typology, not "
        "the verse's plain sense. The phrase 'blindfolded' is his and is the closest he comes here to a physical picture. "
        + HENRY_NOTE,
    ),
    item(
        "Isaiah's sealed scroll (29:11-12). Henry: 'the vision of all the prophets' had become to them 'as the words of a book "
        "that is sealed up': they knew it was a vision and prophecy but knew nothing of what was in it, 'any more than "
        "a man (though a good scholar) is for a book delivered to him sealed up'. He says the learned excused themselves "
        "as having a hard style and the unlearned as 'not learned'. In Luke 4 he adds that the books of the Old Testament "
        "were 'in a manner shut up till Christ opened them, Isa. xxix. 11'.",
        HENRY + "Isaiah 29:9-12 and Luke 4:16-21",
        [ev(H4, "any more than a man (though a good scholar) is for a book delivered to him sealed up, and which he must not open the seals of."),
         ev(H4, "So they knew that what Isaiah said was a vision and prophecy, but the meaning of it was hidden from them"),
         ev(H4, "The ordinary sort of people excused themselves from regarding what the prophets said with their want of learning"),
         ev(H5, "The books of the Old Testament were in a manner shut up till Christ opened them, Isa. xxix. 11.")],
        "high",
        "The sealed book is the verse's own image (a letter that cannot be read); the shelf has no first-century "
        "description of a sealed scroll. Henry's use of it for blindness is his link, since 29:10-12 speaks of "
        "closed eyes and a sealed book together. " + HENRY_NOTE,
    ),
    item(
        "Henry on Isaiah 42:18-20, 'Who is blind but my servant?'. Verse 18 may be spoken 'to the Gentile idolaters, whom he calls deaf and blind, because they worshipped gods that were so'; verse 19 is God's own people, "
        "'God's servants, and their priests and elders his messengers', who 'were deaf and blind'. Verse 20 "
        "(seeing many things but not observing) he describes as 'ruined for want of observing that which they cannot "
        "but see; they perish, not through ignorance, but mere carelessness'.",
        HENRY + "Isaiah 42:18-25",
        [ev(H4, "The verse before may be understood as spoken to the Gentile idolaters, whom he calls deaf and blind, because they worshipped gods that were so."),
         ev(H4, "The people of the Jews were in profession God's servants, and their priests and elders his messengers (Mal. ii. 7); but they were deaf and blind."),
         ev(H4, "Multitudes are ruined for want of observing that which they cannot but see; they perish, not through ignorance, but mere carelessness.")],
        "high",
        "Henry's notes on this chapter also contain harsh lines about the Jews 'dispersed unto this day' (see the digest) "
        "that are not used. His point that verse 18 may be addressed to idolaters and verse 19 to Israel matters to "
        "'who is called blind': both groups are, and neither is a person who cannot see. " + HENRY_NOTE,
    ),
    item(
        "Henry on Isaiah 43:8, 'Bring forth the blind people that have eyes': he reads it as a reference to Psalm 115:8, "
        "'the prophet seems here to refer when he calls idolaters blind people that have eyes', so that here the "
        "blind are idol-worshippers who 'have the shape, capacities, and faculties, of men' but lack 'reason and "
        "common sense'.",
        HENRY + "Isaiah 43:8-13",
        [ev(H4, "to which the prophet seems here to refer when he calls idolaters blind people that have eyes, and deaf people that have ears.")],
        "high",
        "Henry's 'blind people that have eyes' is the verse's phrase, so this is a figure by definition: eyes that "
        "work and do not see. His gloss that idolaters lack 'reason and common sense' is his reading of the "
        "picture, not a statement about anyone whose eyes do not work. " + HENRY_NOTE,
    ),
    item(
        "Henry on Revelation 3:17, Laodicea 'blind': 'they could not see their state, nor their way, nor their danger', "
        "and 'they thought they saw'. Then the clearest statement of how he reads the word: 'The riches of the body will not "
        "enrich the soul; the sight of the body will not enlighten the soul'. He also says the church 'could not see "
        "Christ, though evidently set forth'.",
        HENRY + "Revelation 3:14-22",
        [ev(H6, "They were blind; they could not see their state, nor their way, nor their danger; they could not see into themselves; they could not look before them; they were blind, and yet they thought they saw"),
         ev(H6, "The riches of the body will not enrich the soul; the sight of the body will not enlighten the soul; the most convenient house for the body will not afford rest nor safety to the soul."),
         ev(H6, "They could not see Christ, though evidently set forth, and crucified, before their eyes.")],
        "high",
        "Henry's 'the sight of the body will not enlighten the soul' places the figure on the soul's side: it "
        "says physical sight does not help. It also assumes that the body's sight is the lesser thing. " + HENRY_NOTE,
    ),
    item(
        "The Laodicea behind the 'eye-salve' (Revelation 3:18). The 1915 encyclopaedia: Laodicea became 'a great and wealthy "
        "center of industry', famous for black wool and for a Phrygian powder for the eyes made there; near it stood "
        "'a renowned school of medicine'; after the earthquake of A.D. 60 its citizens 'rejected the proffered aid "
        "of Rome, and quickly rebuilt it at their own expense' (it cites Rev 3:17). Its entry 'Eyesalve': 'A Phrygian powder mentioned by Galen, for which the medical school of "
        "Laodicea seems to have been famous... but the figurative reference is to the restoring of spiritual vision.' "
        "Henry says Laodicea was 'a once famous city', with a vast wall, three marble theatres and seven hills.",
        "International Standard Bible Encyclopaedia (1915), 'Laodicea' (E. J. Banks) and 'Eyesalve'; " + HENRY + "Revelation 3:14-22",
        [ev(I3, "great and wealthy center of industry"),
         ev(I3, "the fine black wool of its sheep"),
         ev(I3, "the Phrygian powder for the eyes"),
         ev(I3, "In the vicinity was the temple of Men Karou and a renowned school of medicine."),
         ev(I3, "so wealthy were its citizens that they rejected the proffered aid of Rome, and quickly rebuilt it at their own expense"),
         ev(I2, "A Phrygian powder mentioned by Galen, for which the medical school of Laodicea seems to have been famous"),
         ev(I2, "but the figurative reference is to the restoring of spiritual vision."),
         ev(H6, "This was a once famous city near the river Lycus, had a wall of vast compass, and three marble theatres, and, like Rome, was built on seven hills.")],
        "medium",
        "The encyclopaedia says the school of medicine was 'in the vicinity' and the powder was 'manufactured there'; "
        "its eyesalve entry says the school 'seems to have been famous', so the link between Rev. 3:18 and "
        "the local trade is probable, not proved; it refers to Ramsay, which is not on the shelf. Smith's and Easton's "
        "entries on Laodicea mention wealth but not the powder or the school. " + OLD_OCR,
    ),
    item(
        "Henry on the counsel of Revelation 3:18: 'they were blind; and he counsels them to buy of him eye-salve, that they "
        "might see, to give up their own wisdom and reason, which are but blindness in the things of God'. So the "
        "remedy is submission and a changed way of knowing, and then 'a new world furnished with the most beautiful "
        "and excellent objects'. On 1 John 2:20 he calls the anointing 'a spiritual eye-salve; it enlightens and strengthens the eyes of the understanding'.",
        HENRY + "Revelation 3:14-22 and 1 John 2:20",
        [ev(H6, "it is a spiritual eye-salve; it enlightens and strengthens the eyes of the understanding"),
         ev(H6, "They were blind; and he counsels them to buy of him eye-salve, that they might see, to give up their own wisdom and reason, which are but blindness in the things of God, and resign themselves to his word and Spirit, and their eyes shall be opened to see their way and their end")],
        "high",
        "Henry offers the 'eye-salve' as a figure and does not mention the medical trade at Laodicea in this "
        "passage. " + HENRY_NOTE,
    ),
]

# ================================================================= like-the-blind
K["like-the-blind"] = [
    item(
        "Henry on Deuteronomy 28:28-29, 'the Lord shall smite thee with madness and blindness... thou shalt grope at noonday'. "
        "He reads it as a judgment on the mind: 'God's judgments can reach the minds of men to fill them with darkness "
        "and horror', so that 'those that are wilfully blind to their duty deserve to be made blind to their interest', "
        "and 'let them grope at noon-day as in the dark'.",
        HENRY + "Deuteronomy 28:15-44",
        [ev(H1, "God's judgments can reach the minds of men to fill them with darkness and horror, as well as their bodies and estates"),
         ev(H1, "those that are wilfully blind to their duty deserve to be made blind to their interest, and, seeing they loved darkness rather than light, let them grope at noon-day as in the dark.")],
        "high",
        "Henry takes 'blindness' here as infatuation in counsel; he does not say whether the curse included loss of "
        "eyesight. The comparison 'as the blind gropeth in darkness' is the verse's own. " + HENRY_NOTE,
    ),
    item(
        "Henry on Isaiah 59:10, 'We grope for the wall like the blind': it is the people's own confession to God, and he "
        "glosses 'we see no way open for our relief, nor know which way to expect it, or what to do in order to it'. "
        "His principle: 'If we shut our eyes against the light of divine truth, it is just with God to hide from our "
        "eyes the things that belong to our peace'; 'Those that will not see their duty shall not see their interest.'",
        HENRY + "Isaiah 59:9-15",
        [ev(H4, "We grope for the wall like the blind; we see no way open for our relief, nor know which way to expect it, or what to do in order to it."),
         ev(H4, "If we shut our eyes against the light of divine truth, it is just with God to hide from our eyes the things that belong to our peace"),
         ev(H4, "Those that will not see their duty shall not see their interest.")],
        "high",
        "Henry reads the groping as being at a loss, a figure of helplessness; he does not describe how blind people "
        "actually move, though the wall image does. Right after, he adds a Latin maxim ('Quos Deus vult perdere') "
        "that is his, not Isaiah's. " + HENRY_NOTE,
    ),
    item(
        "Henry on Lamentations 4:13-15, 'They have wandered as blind men in the streets': the prophets and priests are "
        "the ones who 'wandered as blind men', that is they 'strayed from the paths of justice, were blind to every thing "
        "that is good, but to do evil they were quick-sighted'. On 'men could not touch their garments' he says good "
        "men 'were as shy of touching them as of touching a dead body'.",
        HENRY + "Lamentations 4:13-20",
        [ev(H4, "They strayed from the paths of justice, were blind to every thing that is good, but to do evil they were quick-sighted."),
         ev(H4, "so that good men were as shy of touching them as of touching a dead body, which contracted a ceremonial pollution")],
        "high",
        "The sentence about being 'blind to every thing that is good, but... quick-sighted' to evil is Henry's own "
        "turn and plays on sight and moral perception together. " + HENRY_NOTE,
    ),
    item(
        "Henry on Zephaniah 1:17, 'they shall walk like blind men': he reads the verse as the day of the Lord's distress, "
        "in which 'their hearts and hands shall fail them' and God will deliver them into the hands of cruel enemies "
        "'because they have sinned against the Lord'. Henry then adds a sentence about how a blind man walks, which "
        "is among the lines this digest flags as not used.",
        HENRY + "Zephaniah 1:14-18",
        [ev(H4, "I will bring distress upon men, the strongest and stoutest of men; their hearts and hands shall fail them; they shall walk like blind men, wandering endlessly, because they have sinned against the Lord."),
         ev(H4, "Because they have sinned against the Lord he will deliver them into the hands of cruel enemies")],
        "medium",
        "The first quote is the verse as Henry prints it inside his exposition, not his own comment. His following "
        "sentence ('Those that walk as bad men...') assumes what a blind man's walking is like and is "
        "flagged in the digest, with its offset, so Brian can look at it. " + HENRY_NOTE,
    ),
    item(
        "Blind people in the streets, and the law's protection of them, from the reference works. The 1915 encyclopaedia says "
        "'there is no reason to believe, as has been surmised, that blindness was any less rife in ancient times than "
        "it is now'; it adds that 'care of the blind was specially enjoined in the Law (Lev 19 14), and offences against them "
        "are regarded as breaches of Law (Dt 27 18)'. Easton: 'The blind are to be treated with compassion (Lev. 19:14; "
        "Deut. 27:18).' (Inference, not a source's statement: the writers of the similes lived among blind people whom the law already named.)",
        "International Standard Bible Encyclopaedia (1915), 'Blindness' (Alex. Macalister); Easton's Bible Dictionary (1897), 'Blind'",
        [ev(I1, "there is no reason to believe, as has been surmised, that blindness was any less rife in ancient times than it is now"),
         ev(I1, "care of the blind was specially enjoined in the Law (Lev 19 14), and offences against them are regarded as breaches of Law (Dt 27 18)"),
         ev(EAS, "The blind are to be treated with compassion (Lev. 19:14; Deut. 27:18).")],
        "medium",
        "The encyclopaedia's 'no reason to believe' is a claim without a figure; nothing on the shelf counts the "
        "blind of the biblical world. The same entry speaks harshly of the sight of diseased eyes in Palestinian "
        "crowds: flagged in the digest, not quoted. " + OLD_OCR,
    ),
]

# ================================================================= eyes-dim-with-grief
K["eyes-dim-with-grief"] = [
    item(
        "Henry on Job 17:7, 'My eye also is dim by reason of sorrow': 'He wept so much that he had almost lost his sight'. "
        "He adds 'The sorrow of the world thus works darkness and death'.",
        HENRY + "Job 17:1-9",
        [ev(H3, "He wept so much that he had almost lost his sight: My eye is dim by reason of sorrow, ch. xvi. 16. The sorrow of the world thus works darkness and death.")],
        "high",
        "Henry says 'almost lost his sight'; he takes the dimness as real, from weeping, and does not call "
        "it blindness. " + HENRY_NOTE,
    ),
    item(
        "Henry on Psalm 6:6-7, 'Mine eye is consumed because of grief': 'wept till he had almost wept his eyes out'; he "
        "says 'this not only kept his eyes waking, but kept his eyes weeping', and that 'true penitents weep in "
        "their retirements', setting David in contrast to the Pharisees who 'disguised their faces' to seem to mourn.",
        HENRY + "Psalm 6",
        [ev(H3, "wept till he had almost wept his eyes out (v. 7): My eye is consumed because of grief."),
         ev(H3, "This not only kept his eyes waking, but kept his eyes weeping."),
         ev(H3, "True penitents weep in their retirements."),
         ev(H3, "The Pharisees disguised their faces, that they might appear unto men to mourn")],
        "high",
        "Henry's 'almost wept his eyes out' is a figure of speech about weeping, not a diagnosis. " + HENRY_NOTE,
    ),
    item(
        "Henry on Psalm 38:10, 'the light of mine eyes, it also is gone from me': he offers three causes for the lost light: "
        "'either with much weeping or by a defluxion of rheum upon them, or perhaps through the lowness of his spirits and "
        "the frequent returns of fainting'. The shelf's commentator is therefore treating this as a real, physical "
        "failing of sight in the psalmist, with grief as one cause among several.",
        HENRY + "Psalm 38",
        [ev(H3, "As for the light of his eyes, that had gone from him, either with much weeping or by a defluxion of rheum upon them, or perhaps through the lowness of his spirits and the frequent returns of fainting.")],
        "high",
        "Henry's three causes are conjecture; the psalm names none, and the shelf does not define 'defluxion of rheum'. " + HENRY_NOTE,
    ),
    item(
        "Henry on Psalm 88:9, 'Mine eye mourneth by reason of affliction': 'Sometimes giving vent to grief by weeping gives "
        "some ease to a troubled spirit. Yet weeping must not hinder praying'. He ties it to 'My eye mourns, but I cry "
        "unto thee daily', so that 'prayers and tears go together, and they shall be accepted together'.",
        HENRY + "Psalm 88",
        [ev(H3, "Sometimes giving vent to grief by weeping gives some ease to a troubled spirit. Yet weeping must not hinder praying; we must sow in tears: My eye mourns, but I cry unto thee daily. Let prayers and tears go together, and they shall be accepted together.")],
        "high",
        "Henry reads the verse as weeping and praying together; he does not comment on the state of the speaker's "
        "sight here. " + HENRY_NOTE,
    ),
    item(
        "Henry on Lamentations 5:17, 'for these things our eyes are dim': 'our heart is faint... our eyes are dim, and "
        "our sight is gone, as is usual in a deliquium, or fainting fit'. He says the people grieved more for the ruin "
        "of the temple than for any other calamity: 'For other desolations our hearts grieve and our eyes weep; but "
        "for this our hearts faint and our eyes are dim.'",
        HENRY + "Lamentations 5:15-22",
        [ev(H4, "for these things our eyes are dim, and our sight is gone, as is usual in a deliquium, or fainting fit."),
         ev(H4, "For other desolations our hearts grieve and our eyes weep; but for this our hearts faint and our eyes are dim.")],
        "high",
        "Henry's own gloss is 'a deliquium, or fainting fit': he takes the dimness as the passing sight-failure of a faint. " + HENRY_NOTE,
    ),
    item(
        "The 1915 encyclopaedia's entry 'Eye' gathers the pattern: 'Eyes may grow dim with sorrow and tears (Job 17 7), "
        "they may \"waste away with griefs\" (Ps 6 7; 31 9; 88 9)'. In the same entry, the physical eye is distinguished "
        "from the figurative 'eye of the heart or mind, the organ of spiritual perception'.",
        "International Standard Bible Encyclopaedia (1915), 'Eye'",
        [ev(I2, "Eyes may grow dim with sorrow and tears (Job 17 7), they may \"waste away with griefs\" (Ps 6 7; 31 9; 88 9)."),
         ev(I2, "Figurative : The eye of the heart or mind, the organ of spiritual perception, which may be en- lightened or opened (Ps 119 IS).")],
        "high",
        "The reference list is a pattern, not a count of any disease. " + OLD_OCR,
    ),
]

# ================================================================= bribes-and-curses
K["bribes-and-curses"] = [
    item(
        "Henry on Exodus 23:8, 'the gift blindeth the wise': the judge 'must not so much as take a gift, lest it should have "
        "a bad influence upon them, and overrule them, contrary to their intentions; for it has a strange tendency to "
        "blind those that otherwise would do well'. So the blinding is a slow, unintended corruption of a good judge.",
        HENRY + "Exodus 23:1-9",
        [ev(H1, "but they must not so much as take a gift, lest it should have a bad influence upon them, and overrule them, contrary to their intentions; for it has a strange tendency to blind those that otherwise would do well.")],
        "high",
        "Henry reads the 'blinding' as an effect on judgment and says nothing here about physical blindness. "
        "The same law is quoted again in Deuteronomy 16:19. " + HENRY_NOTE,
    ),
    item(
        "Where the judges sat, and how many (Deuteronomy 16:18-20). Henry: 'the courts of judgment sat in the gates', and by "
        "this law, 'besides the great sanhedrim that sat at the sanctuary, consisting of seventy elders and a "
        "president, there was in the larger cities... a court of twenty-three judges, in the smaller cities a court "
        "of three judges'. He says Deuteronomy 16:19 repeats Exodus 23:8: 'This law had been given before'.",
        HENRY + "Deuteronomy 16:18-22",
        [ev(H1, "for the courts of judgment sat in the gates."),
         ev(H1, "besides the great sanhedrim that sat at the sanctuary, consisting of seventy elders and a president, there was in the larger cities, such as had in them above 120 families, a court of twenty-three judges, in the smaller cities a court of three judges"),
         ev(H1, "This law had been given before, Exod. xxiii. 8.")],
        "medium",
        "The figures (seventy elders, twenty-three, three) come from later Jewish practice as Henry reports it; he "
        "gives no source and attaches them to Moses's law. " + HENRY_NOTE,
    ),
    item(
        "How common bribery was, and what it meant for the blind picture. The 1915 encyclopaedia (Blindness, Judicial): 'the OT "
        "abounds with allusions to the corruption and venality of the magisterial bench'; Exodus 23:8 'a bribe blindeth "
        "the eyes of the open-eyed' marks 'a prolific cause of the miscarriage of justice'. Easton gives the Hebrew "
        "literally: 'the gift maketh open eyes blind'. Samuel, in 1 Samuel 12:3, asks whose bribe he took 'to blind mine "
        "eyes therewith'.",
        "International Standard Bible Encyclopaedia (1915), 'Blindness, Judicial' and 'Bribery'; Easton's Bible Dictionary (1897), 'Bribe'",
        [ev(I1, "According to the Book of the Covenant (Ex 23 8) 'a bribe blindeth the eyes of the open- eyed.'"),
         ev(EAS, "for the gift maketh open eyes blind, and perverteth the cause of the righteous"),
         ev(I1, "to blind mine eyes therewith?")],
        "high",
        "The encyclopaedia entry called 'Blindness, Judicial' is about courts of justice, not about blindness as a "
        "judgment; its title is the scholar's phrase and may confuse. " + OLD_OCR,
    ),
    item(
        "Henry on Zechariah 11:17, the idol shepherd whose right eye is 'utterly darkened': he reads the darkened eye as "
        "losing sight of danger ('he shall not discern the danger that his flock is in, nor know which way to look for "
        "relief'), says it was 'fulfilled when Christ said to the Pharisees, I have come that those who see may be made "
        "blind, John ix. 39', and adds that 'those that should have been watchmen, but were sleepy and would never look "
        "about them, will justly have their eye blinded'.",
        HENRY + "Zechariah 11:15-17",
        [ev(H4, "his right eye shall be utterly darkened, that he shall not discern the danger that his flock is in, nor know which way to look for relief."),
         ev(H4, "This was fulfilled when Christ said to the Pharisees, I have come that those who see may be made blind, John ix. 39."),
         ev(H4, "those that should have been watchmen, but were sleepy and would never look about them, will justly have their eye blinded.")],
        "high",
        "Henry says the shepherd's arm and eye are lost 'so that he shall quite lose the use of both', reading a "
        "physical penalty as a moral one. The link to John 9:39 is Henry's own. " + HENRY_NOTE,
    ),
    item(
        "The 1915 encyclopaedia on blinding as a punishment ('Eye'): 'A cruel custom therefore sanctioned among heathen nations "
        "the putting out of the eyes of an enemy', and 'Such blinding or putting out of the \"right eye\" was also "
        "considered a deep humiliation, as it robbed the victim of his beauty, and made him unfit to take his part in "
        "war (1 S 11 2; Zee 11 17)'.",
        "International Standard Bible Encyclopaedia (1915), 'Eye'",
        [ev(I2, "as it robbed the victim of his beauty, and made him unfit to take his part in war (1 S 11 2; Zee 11 17)."),
         ev(I2, "A cruel custom therefore sanc- tioned among heathen nat ions")],
        "high",
        "'Heathen nations' is the encyclopaedia's phrase for the surrounding peoples; the Hebrew texts it cites "
        "(Samson, Zedekiah) show Israel and Judah on the receiving end. The shelf does not describe how a blinded "
        "king or soldier lived afterward. " + OLD_OCR,
    ),
    item(
        "Henry on Zechariah 12:4, 'I will smite every horse of the people with blindness': 'so that they shall be no way "
        "serviceable to them; blinding the horses will be as bad as houghing them'. He reads the verse as God making the "
        "attackers' cavalry useless, the horses and horsemen 'forget the military exercise to which they were trained'.",
        HENRY + "Zechariah 12:1-9",
        [ev(H4, "I will smite every horse of the people with blindness, so that they shall be no way serviceable to them; blinding the horses will be as bad as houghing them.")],
        "high",
        "'Houghing' is Henry's word and the shelf does not define it. He reads the curse on the horses literally; "
        "the shelf has no further comment on it. " + HENRY_NOTE,
    ),
]

# ================================================================= eyes-opened
K["eyes-opened"] = [
    item(
        "Henry on Psalm 146:8, 'The Lord openeth the eyes of the blind': he reads it both ways at once. 'He gives sight to "
        "those that have been long deprived of it', as in Gen. 21:19 and 2 Kings 6:17, which he cites; 'But this has special reference to Christ', since 'since the world began was it not heard that "
        "any man opened the eyes of one that was born blind till Christ did it (John ix. 32) and thereby encouraged us "
        "to hope in him for spiritual illumination'. He also quotes Dr Hammond, who cites a rabbi that the last verse "
        "'belongs to the days of the Messiah' and ties verses 7-8 to Matthew 11:5.",
        HENRY + "Psalm 146:5-10",
        [ev(H3, "He gives sight to those that have been long deprived of it; The Lord can open the eyes of the blind, and has often given to his afflicted people to see that comfort which before they were not aware of"),
         ev(H3, "But this has special reference to Christ; for since the world began was it not heard that any man opened the eyes of one that was born blind till Christ did it (John ix. 32) and thereby encouraged us to hope in him for spiritual illumination."),
         ev(H3, "He quotes one of the rabbies, who says of v. 10 that it belongs to the days of the Messiah.")],
        "high",
        "Henry cites Genesis 21:19 and 2 Kings 6:17 as earlier instances and does not explain them. He applies the psalm to a physical healing "
        "('the blind receive their sight') and a spiritual one together, without ranking them. " + HENRY_NOTE,
    ),
    item(
        "Edersheim on how Isaiah 35:5-6 was read before and in Jesus's day. In an appendix of Rabbinic passages he notes "
        "'Is. xxxv. 5, 6 is repeatedly applied to Messianic times', in Yalkut, Bereshith Rabba and the Midrash on Psalm "
        "146:8. In the body of the book he says that when John the Baptist in prison needed an answer, Jesus 'points for "
        "the solution of his doubts to the well-remembered prophecies of Isaiah (Is. xxxv. 5, 6; lxi. 1...)'.",
        EDER + "Book III, ch. iii (footnote on the Baptist in prison) and Appendix IX (Old Testament passages Messianically applied in Rabbinic writings)",
        [ev(EDL, "Is. xxxv. 5, 6 is repeatedly applied to Messianic times. Thus, in Yalkut i. 78 c, and 157 a; in Ber. R. 95; and in Midrash on Ps. cxlvi. 8."),
         ev(EDL, "when our Lord would afterwards instruct him in his hour of darkness (St. Matt. xi. 2), He points for the solution of his doubts to the well-remembered prophecies of Isaiah (Is. xxxv. 5, 6; lxi. 1; viii. 14, 15).")],
        "medium",
        "The Rabbinic collections Edersheim cites (Yalkut, Midrash Rabbah) were compiled long after the first century, "
        "so they show how the verse was read later, not necessarily in Jesus's time. He does not say whether the "
        "Rabbinic readings took the eyes as physical or spiritual. " + EDER_NOTE,
    ),
    item(
        "Henry on Isaiah 35:5-6: 'Wonders shall be wrought on men's bodies (v. 5, 6): The eyes of the blind shall be opened'; he "
        "lists Christ's healing of the man 'born blind' (John 9:6), the deaf (Ephphatha) and the lame, as 'miracles Christ "
        "wrought to prove that he was sent of God', and then: 'Wonders, greater wonders, shall be wrought on men's "
        "souls', where 'those that were spiritually blind were enlightened (Acts xxvi. 18)'. He reads the verse as both "
        "bodies and souls, bodies first.",
        HENRY + "Isaiah 35:1-10",
        [ev(H4, "Wonders shall be wrought on men's bodies (v. 5, 6): The eyes of the blind shall be opened; this was often done by our Lord Jesus when he was here upon earth"),
         ev(H4, "These miracles Christ wrought to prove that he was sent of God"),
         ev(H4, "Wonders, greater wonders, shall be wrought on men's souls. By the word and Spirit of Christ those that were spiritually blind were enlightened (Acts xxvi. 18)")],
        "high",
        "This is the clearest place on the shelf where Henry reads one 'eyes of the blind' verse as physical and "
        "spiritual together; he ranks the spiritual as 'greater'. " + HENRY_NOTE,
    ),
    item(
        "Henry on Isaiah 29:18, 'the eyes of the blind shall see out of obscurity': he reads it as ignorance giving way to "
        "understanding: 'Those that were ignorant shall become intelligent', for those who did not understand the prophecy ('as "
        "a sealed book') will understand it when fulfilled, 'those that were blind shall see out of obscurity; for the "
        "gospel was sent to them to open their eyes, Acts xxvi. 18'. He says nothing here of physical sight.",
        HENRY + "Isaiah 29:17-24",
        [ev(H4, "Those that were ignorant shall become intelligent, v. 18."),
         ev(H4, "Those that understood not this prophecy (but it was to them as a sealed book, v. 11) shall, when it is accomplished, understand it"),
         ev(H4, "those that sat in darkness shall see a great light, those that were blind shall see out of obscurity; for the gospel was sent to them to open their eyes, Acts xxvi. 18.")],
        "high",
        "Henry's reading is spiritual only in this verse, in contrast to his reading of Isaiah 35. The phrase 'the "
        "poor Gentiles' that precedes the quote is his. " + HENRY_NOTE,
    ),
    item(
        "Henry on Isaiah 42:7, 'To open the blind eyes': Christ is 'given for a light to the Gentiles', not only to "
        "reveal what they needed to know 'but to open the blind eyes, that they might know it. By his Spirit in the word "
        "he presents the object; by his Spirit in the heart he prepared the organ'. Paul was sent to the Gentiles 'to "
        "open their eyes' (Acts 26:18). He reads the promise as about knowledge of God and the removal of spiritual "
        "blindness, with 'light and liberty'.",
        HENRY + "Isaiah 42:1-9",
        [ev(H4, "He is given for a light to the Gentiles, not only to reveal to them what they were concerned to know, and which otherwise they could not have known, but to open the blind eyes, that they might know it."),
         ev(H4, "By his Spirit in the word he presents the object; by his Spirit in the heart he prepared the organ."),
         ev(H4, "And St. Paul was sent to the Gentiles to open their eyes, Acts xxvi. 18."),
         ev(H4, "Two glorious blessings Christ, in his gospel, brings with him to the Gentile world--light and liberty.")],
        "high",
        "Henry's 'present the object... prepare the organ' picture treats the eye's working as a pair: something to see "
        "and an organ to see it; this phrase also appears in his John 9:39 exposition. " + HENRY_NOTE,
    ),
    item(
        "Henry on Isaiah 42:16, 'I will bring the blind by a way that they knew not': he writes 'Those who by nature were "
        "blind, and those who, being under convictions of sin and wrath are quite at a loss and know not what to do with "
        "themselves, God will lead by a way that they knew not'. He gives Paul as his example: 'in the conversion of Paul, "
        "he was struck blind first, and then God revealed his Son in him'. He reads 'darkness light' as 'knowledge "
        "shall be easy to them' and 'crooked things straight' as 'the yoke easy'.",
        HENRY + "Isaiah 42:10-17",
        [ev(H4, "Those who by nature were blind, and those who, being under convictions of sin and wrath are quite at a loss and know not what to do with themselves, God will lead by a way that they knew not"),
         ev(H4, "Thus, in the conversion of Paul, he was struck blind first, and then God revealed his Son in him, and made the scales to fall from his eyes."),
         ev(H4, "but God will make darkness light before them, and knowledge shall be easy to them."),
         ev(H4, "their way shall be plain, and the yoke easy")],
        "high",
        "Henry's 'by nature blind' means spiritually blind by nature (born in ignorance of God); he says nothing "
        "here of a promise of guidance to people who are physically blind. The promise of a guide, as a "
        "promise to the physically blind, is the page's own reading, not Henry's. " + HENRY_NOTE,
    ),
    item(
        "Henry on Luke 4:18, 'recovering of sight to the blind', preached at Nazareth: he says Christ came 'by the power of "
        "his grace to give sight to them that were blind; not only the Gentile world, but every unregenerate soul, that "
        "is not only in bondage, but in blindness, like Samson and Zedekiah', and has 'eye-salve for us, which we may have "
        "for the asking'. He adds that they had 'seven readers every sabbath, the first a priest, the second a Levite, and the "
        "other five Israelites of that synagogue'.",
        HENRY + "Luke 4:14-30",
        [ev(H5, "but by the power of his grace to give sight to them that were blind; not only the Gentile world, but every unregenerate soul, that is not only in bondage, but in blindness, like Samson and Zedekiah."),
         ev(H5, "Christ came to tell us that he has eye-salve for us, which we may have for the asking"),
         ev(H5, "They had in their synagogues seven readers every sabbath, the first a priest, the second a Levite, and the other five Israelites of that synagogue.")],
        "high",
        "Henry's two examples, Samson and Zedekiah, are named in the encyclopaedia's 'Eye' entry among those whose eyes "
        "were put out (Jgs 16:21; 2 K 25:7); he uses them as images of spiritual bondage. He does not mention "
        "the blind people Jesus healed in this passage. " + HENRY_NOTE,
    ),
    item(
        "Edersheim on the Nazareth synagogue (Luke 4:16-21). Jesus 'Himself read the concluding portion from the Prophets, or "
        "the so-called Haphtarah'; 'the minister delivered unto Him the book of the prophet Esaias', and when it was "
        "unrolled 'much more than the sixty-first chapter of Isaiah must have been within range of His eyes'. "
        "He thinks the verses read, Isaiah 61:1 with a clause from 58:6, were Jesus's introductory text, not the whole "
        "lesson, and reads 'the healing which He offers to those whom sin had blinded' as part of what the "
        "text announced.",
        EDER + "Book III, ch. xi (The First Galilean Ministry), text and footnotes [2177]-[2191]",
        [ev(EDL, "There is no reason to disturb the almost traditional idea, that Jesus Himself read the concluding portion from the Prophets, or the so-called Haphtarah."),
         ev(EDL, "When unrolling, and holding the scroll, much more than the sixty-first chapter of Isaiah must have been within range of His eyes."),
         ev(EDL, "the healing which He offers to those whom sin had blinded")],
        "medium",
        "Edersheim's reconstruction of the synagogue service rests on later Talmudic sources and he marks parts of it "
        "'we doubt not' or 'most likely'. His remark about 'those whom sin had blinded' is his summary, in which "
        "the physical healings are not mentioned. " + EDER_NOTE,
    ),
]

# ----------------------------------------------------------------------------
# Remarks on the relation between the figure and physical blindness.
# key: (who, locator, file, anchor-quote, one-line note)
REMARKS = [
    ("Henry", "Matthew 9:27 (the two blind men)", H5,
     "They who, by the providence of God, are deprived of bodily sight, may yet, by the grace of God, have the eyes of their understanding so enlightened",
     "the physically blind can see what the leaders cannot"),
    ("Henry", "Matthew 9:27-31 (the cure)", H5,
     "Lord, that the eyes of our mind may be opened! Many are spiritually blind, and yet say they see, John ix. 41.",
     "the blind men's request as a model for the spiritual one"),
    ("Henry", "Luke 18:35-43 (Bartimaeus, near Jericho)", H5,
     "As a token of this, he cured many of their bodily blindness",
     "the bodily healings are a 'token' of giving sight to 'blind souls'"),
    ("Henry", "John 9:35-38 (the healed man)", H5,
     "Note, The Greatest comfort of bodily eyesight is its serviceableness to our faith and the interests of our souls.",
     "physical sight valued for what it does for faith"),
    ("Henry", "John 9:39 ('those who see might be made blind')", H5,
     "This great truth he explains by a metaphor borrowed from the miracle which he had lately wrought.",
     "he says the verse is a metaphor taken from the healing"),
    ("Henry", "Isaiah 35:5", H4,
     "Wonders shall be wrought on men's bodies (v. 5, 6): The eyes of the blind shall be opened",
     "physical first, then 'greater wonders... on men's souls'"),
    ("Henry", "Psalm 146:8", H3,
     "But this has special reference to Christ; for since the world began was it not heard that any man opened the eyes of one that was born blind till Christ did it (John ix. 32) and thereby encouraged us to hope in him for spiritual illumination.",
     "reads the verse as both"),
    ("Henry", "Isaiah 29:18", H4,
     "Those that were ignorant shall become intelligent, v. 18.",
     "reads the verse as ignorance becoming understanding only"),
    ("Henry", "Isaiah 42:7", H4,
     "By his Spirit in the word he presents the object; by his Spirit in the heart he prepared the organ.",
     "the opened eye is a picture of an enlightened heart"),
    ("Henry", "Isaiah 42:16", H4,
     "Those who by nature were blind, and those who, being under convictions of sin and wrath are quite at a loss and know not what to do with themselves",
     "'blind by nature' = spiritually blind"),
    ("Henry", "Isaiah 42:18-19", H4,
     "The verse before may be understood as spoken to the Gentile idolaters, whom he calls deaf and blind, because they worshipped gods that were so.",
     "the blind in verse 18 may be idolaters (cf. Ps. 115:8)"),
    ("Henry", "Isaiah 43:8", H4,
     "to which the prophet seems here to refer when he calls idolaters blind people that have eyes, and deaf people that have ears.",
     "'blind people that have eyes': eyes that work and do not see"),
    ("Henry", "Luke 4:18", H5,
     "but by the power of his grace to give sight to them that were blind; not only the Gentile world, but every unregenerate soul, that is not only in bondage, but in blindness, like Samson and Zedekiah.",
     "the promise applied to souls, with two physically blinded men as examples"),
    ("Henry", "Romans 11:8", H6,
     "They had the faculties, but in the things that belonged to their peace they had not the use of those faculties",
     "eyes that work but do not see"),
    ("Henry", "2 Peter 1:9", H6,
     "blind, that is, as to spiritual and heavenly things, as the next words explain it: He cannot see far off.",
     "he says outright that 'blind' here is spiritual"),
    ("Henry", "Revelation 3:17", H6,
     "The riches of the body will not enrich the soul; the sight of the body will not enlighten the soul",
     "bodily sight is no help to the soul"),
    ("Henry", "Ecclesiastes 7:11", H3,
     "The clearness of the eye of the understanding is of greater use to us than bodily eye-sight.",
     "the eye of the understanding is better than bodily sight"),
    ("Henry", "Acts 9:8-9 (Paul)", H6,
     "Now Paul was thus struck with bodily blindness to make him sensible of his spiritual blindness",
     "a bodily blindness sent to teach him of the other kind"),
    ("Henry", "1 Kings 14:4 (Ahijah)", H2,
     "blind through age, yet still blest with the visions of the Almighty, which need not bodily eyes, but are rather favoured by the want of them",
     "a blind prophet sees better for it"),
    ("Edersheim", "John 9:41", EDL,
     "It was not the calamity of blindness; but it was a blindness in which they were guilty",
     "physical blindness is a calamity; the Pharisees' kind is guilt"),
    ("Edersheim", "John 9:2-3 (why was he born blind)", EDL,
     "There is a physical, natural reason for them.",
     "he separates the natural cause of blindness from the moral one"),
    ("Edersheim", "Matthew 9:27-31 (the two blind men)", EDL,
     "Yet the leprosy of Israel and the blindness of the Gentile world are equally removed by the touch of His Hand at the cry of faith.",
     "he uses 'the blindness of the Gentile world' as a figure beside the physical healing"),
    ("Edersheim", "Mark 8:22-26 (Bethsaida)", EDL,
     "Lastly, the confusedness of his sight, when first restored to him, surely conveyed, not only to him but to us all, both a spiritual lesson and a spiritual warning.",
     "he draws a spiritual lesson from the physical healing's two stages"),
    ("Edersheim", "Luke 4:18", EDL,
     "the healing which He offers to those whom sin had blinded",
     "summarises the Nazareth text as healing of sin-blindness"),
    ("ISBE 1915", "'Blindness'", I1,
     "The word blind is used as a vb., as Jn 12 40, usually in the sense of ob scuring spiritual perception.",
     "the verb is mostly spiritual; physical blindness is noun and adjective"),
    ("ISBE 1915", "'Blindness' (end)", I1,
     "Figuratively, blindness is used to represent want of mental perception, want of prevision, reckless ness, and incapacity to perceive moral distinctions (Isa 42 16.18.19; Mt 23 16 ff; Jn 9 39 ff).",
     "lists the figure's meanings and cites exactly the picture pages' texts"),
    ("ISBE 1915", "'Blindness': the 'scales' of Paul", I1,
     "The \"scales\" mentioned were not material but in the restoration of his sight it seemed as if scales had fallen from his eyes.",
     "the 'scales' are a figure inside a physical healing"),
    ("ISBE 1915", "'Eye' (2)", I2,
     "Figurative : The eye of the heart or mind, the organ of spiritual perception, which may be en- lightened or opened (Ps 119 IS).",
     "names the figurative eye as its own category"),
    ("ISBE 1915", "'Eyesalve'", I2,
     "but the figurative reference is to the restoring of spiritual vision.",
     "the medical detail serves a figurative reference"),
    ("Easton", "'Blind'", EAS,
     "Blindness denotes ignorance as to spiritual things (Isa. 6:10; 42:18, 19; Matt. 15:14; Eph. 4:18).",
     "a reference-work statement of the figure"),
    ("Easton", "'Blind'", EAS,
     "The opening of the eyes of the blind is peculiar to the Messiah (Isa. 29:18).",
     "treats the opening promise as a Messianic sign"),
    ("Smith's", "'Blindness'", SMI,
     "opening the eyes of the blind\" is mentioned in prophecy as a peculiar attribute of the Messiah.",
     "same, from Smith's"),
]

# Passages flagged (located and checked; not used as evidence). Short anchors only.
FLAGGED = [
    ("Henry", "Zephaniah 1:17", H4,
     "Those that walk as bad men will justly be left to walk as blind men",
     "describes how a blind man walks as dark, doubtful, dangerous and unguided, and ends in a fall; "
     "bears directly on what the picture assumes, so Brian may want to read the sentence"),
    ("Henry", "Luke 18 (Bartimaeus)", H5,
     "They that are poor and blind are wretched and miserable",
     "says of people who are poor and blind that they are wretched and miserable, citing Rev. 3:17, before "
     "calling them objects of compassion"),
    ("Henry", "Matthew 9:27-31", H5,
     "followed him, as beggars do, with their incessant cries",
     "treats the blind men's crying out as begging, a mild but real assumption"),
    ("Henry", "John 9:35-38", H5,
     "How contentedly might this man have returned to his former blindness",
     "says the healed man could have gone back to being blind content, having seen the Son of God"),
    ("Henry", "Acts 9:8-9", H6,
     "Condemned sinners are struck blind, as the Sodomites and Egyptians",
     "calls Israel's blindness lasting, and sets Sodom and Egypt beside the unbelieving Jews"),
    ("Henry", "Romans 11:7-10", H6,
     "His blood be upon us and upon our children",
     "presents the cry of Matthew 27:25 as a curse entailed on the Jews and their children"),
    ("Henry", "Romans 11:8", H6,
     "the obstinacy and unbelief go by succession from generation to generation",
     "says Jewish unbelief is inherited by succession"),
    ("Henry", "Isaiah 42:18-25", H4,
     "They were even worse than the Gentiles themselves.",
     "says Israel was worse than the Gentiles"),
    ("Henry", "Isaiah 42:18-25", H4,
     "remain dispersed unto this day",
     "says the Jews who rejected Christ are still scattered, under a curse, in his own day"),
    ("Henry", "Revelation 3:14-22", H6,
     "an awful monument of the wrath of the Lamb",
     "calls the ruins of Laodicea a monument to the wrath of Christ"),
    ("Henry", "Matthew 15:1-9 and Matthew 23", H5,
     "The Papists pretend",
     "uses Roman Catholics as the type of a church of tradition and 'church-oppressors' as the Pharisees' type"),
    ("Henry", "1 John 2:9-11", H6,
     "poor ignorant Samaritans",
     "calls Samaritans poor and ignorant in passing"),
    ("Edersheim", "Matthew 23:15 (third woe)", EDL,
     "Against this charge, rightly understood, Judaism has in vain sought to defend itself.",
     "polemical sentence about Judaism"),
    ("Edersheim", "Matthew 23 (before the woes)", EDL,
     "But perhaps the climax of blasphemous self-assertion is reached in the story",
     "polemical sentence about Rabbinic self-assertion"),
    ("Edersheim", "Matthew 15 (purification)", EDL,
     "These painful details, most reluctantly given",
     "apology for his own account of Rabbinic purity rules, with a nod to 'blindness in part'"),
    ("Edersheim", "Sketches, ch. on the Pharisees", EDS,
     "The result was a system of pure externalism",
     "polemical summary of the Pharisees' system and the 'blind guides'"),
    ("ISBE 1915", "'Blindness'", I1,
     "among the commonest and most disgusting sights",
     "calls the sight of diseased eyes in a Palestinian crowd 'disgusting'"),
    ("ISBE 1915", "'Eye'", I2,
     "A cruel custom therefore sanc- tioned among heathen nat ions",
     "'heathen nations' for the neighbours of Israel (used in an item, with a caution)"),
]

# ----------------------------------------------------------------------------
rem_out = []
for who, loc, f, q, note in REMARKS:
    rem_out.append({"who": who, "locator": loc, "note": note, **ev(f, q)})
flag_out = []
for who, loc, f, q, note in FLAGGED:
    flag_out.append({"who": who, "locator": loc, "note": note, **ev(f, q)})

if FAILS:
    print("QUOTES NOT FOUND:")
    for f, q in FAILS:
        print("  ", f, "|", q)
    sys.exit(1)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(K, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
OUT_REM.write_text(json.dumps({"remarks": rem_out, "flagged": flag_out}, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8", newline="\n")
print("wrote", OUT)
print("wrote", OUT_REM)
for k, v in K.items():
    print(k, len(v))
print("remarks", len(rem_out), "flagged", len(flag_out))
