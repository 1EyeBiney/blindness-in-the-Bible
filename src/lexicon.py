"""The words page: every Hebrew and Greek word the site follows, gathered in one place.

Each entry names a Strong's number (Hebrew) or a lemma (Greek), gives the plain spelling and how it is said, and
a few lines on what the word does. Counts and verse lists are not typed in: they are read from the tagged texts on
the shelf at build time (src/hebrew.py, src/greek.py), so "ivver appears 26 times" is checked, not quoted. The
sample verses are also checked; a sample verse that does not contain the word stops the build.
"""
from __future__ import annotations

import hebrew
import greek

TITLE = "The words"
SLUG = "words.html"
TYPHLOS = "τυφλός"
TYPHLOO = "τυφλόω"

INTRO = [
    "Every Hebrew word the pages of this site follow, and the New Testament's one word for blind, side by side. "
    "The pattern only shows when they are together: the words for sight going are words for fading and weight; the "
    "words for sight taken are a workman's words; and around the blind the Law uses words for stumbling, for "
    "flaws, for freedom and for fear.",
    "Each word is given with a plain spelling for saying aloud, its meaning from Strong's dictionary of 1894, how "
    "many times it occurs in the Bible, and a few verses. The counts and verses are not copied from a book. The "
    "build reads them from the tagged Hebrew and Greek texts on the bookshelf and checks every sample verse, so a "
    "verse that does not contain the word cannot appear here. The English is the Berean Standard Bible throughout. "
    "In the episodes the words are spoken the way they are spelled here, and the captions show them in quotation "
    "marks.",
]

# Each group: (heading, lead paragraph, entries). An entry: number or lemma, spelling, how it is said, text
# (a list of paragraphs), sample verses (book, chapter, verse), and optionally "also": pages that use the word
# which the automatic lookup in src/words.py would not find.
GROUPS = [
    ("The words for blind", "The plain words, which the rest of this site has used without ever stopping to explain them.", [
        {"key": "H5787", "spelling": "ivver", "say": "ih-VAIR",
         "text": ["The ordinary word. It is used of people, of animals brought to the altar, of a nation that will "
                  "not see, and once of God's own servant. The Law uses it twice to protect the blind and once to "
                  "limit a blind priest. Isaiah uses it most, and in him it turns from a condition into a promise: "
                  "the eyes of the blind will be opened. Exodus 4 puts the word in God's own mouth, as something He "
                  "makes."],
         "samples": [("Exodus", 4, 11), ("Leviticus", 19, 14), ("Job", 29, 15), ("Psalm", 146, 8), ("Isaiah", 42, 16), ("Isaiah", 42, 19)],
         "also": [("what-blind-means.html", "What blind means here")]},
        {"key": "H5786", "spelling": "avar", "say": "ah-VAR",
         "text": ["The verb: to make blind. The Old Testament uses it of one man, Zedekiah, in each of the three "
                  "accounts of his capture. Its only other uses are in the Law, and they are about bribes: a bribe "
                  "blinds those who see."],
         "samples": [("2 Kings", 25, 7), ("Exodus", 23, 8)]},
        {"key": "H5788", "spelling": "avveret", "say": "av-VEH-ret",
         "text": ["The noun, blindness, three times only: the blind animal that may not be offered, the blindness "
                  "named among the curses of Deuteronomy 28, and the blindness that will strike the horses of the "
                  "nations in Zechariah."],
         "samples": [("Leviticus", 22, 22), ("Deuteronomy", 28, 28), ("Zechariah", 12, 4)]},
        {"key": "H5575", "spelling": "sanverim", "say": "san-vay-REEM",
         "text": ["A different word, used only twice, for a blindness that comes suddenly and from God: on the men "
                  "at Lot's door, and on the Aramean soldiers at Dothan. Both times the men keep moving and cannot "
                  "find what they are looking for. It is the word behind the site's stories of sight taken for a "
                  "time, and the dictionaries differ on whether it means darkness or dazzle."],
         "samples": [("Genesis", 19, 11), ("2 Kings", 6, 18)]},
        {"key": TYPHLOS, "greek": "G5185", "spelling": "typhlos", "say": "toof-LOSS",
         "text": ["The New Testament's one word for blind. It is used fifty times, almost all of them in the "
                  "Gospels: John has it most, then Matthew. Nearly every blind person in the New Testament is met in "
                  "Jesus's company, and the word is also His for guides who cannot see where they lead. Outside the "
                  "Gospels it is rare: Paul's proud guide for the blind, Peter's man who cannot see far, and the church "
                  "at Laodicea that does not know it is blind."],
         "samples": [("Matthew", 11, 5), ("Matthew", 15, 14), ("John", 9, 1), ("Luke", 4, 18), ("Acts", 13, 11), ("Revelation", 3, 17)]},
        {"key": TYPHLOO, "greek": "G5186", "spelling": "typhloo", "say": "toof-LO-oh",
         "text": ["The verb, to blind, three times, and never of eyes. It is what hatred does to a brother, what the "
                  "god of this age does to minds, and what Isaiah's hard saying describes in John 12."],
         "samples": [("John", 12, 40), ("2 Corinthians", 4, 4), ("1 John", 2, 11)]},
    ]),
    ("Sight going", "The vocabulary of old age. Isaac, Jacob, Eli and Ahijah are never called ivver. Their eyes dim, grow heavy, or set.", [
        {"key": "H3543", "spelling": "kahah", "say": "kah-HAH",
         "text": ["To be weak; of a light or an eye, to grow dim. Isaac's word, and Job's for eyes dimmed by grief. "
                  "Deuteronomy uses it of Moses to say the opposite: at a hundred and twenty his eyes were not dim."],
         "samples": [("Genesis", 27, 1), ("Deuteronomy", 34, 7), ("Job", 17, 7)]},
        {"key": "H3544", "spelling": "keheh", "say": "kay-HEH",
         "text": ["The adjective from the same root: dim, faded, feeble. Eli's word in 1 Samuel 3, and the word for "
                  "a spot on the skin that has faded and for the smouldering wick the Servant will not put out. "
                  "Something going out slowly, not gone."],
         "samples": [("1 Samuel", 3, 2), ("Isaiah", 42, 3)]},
        {"key": "H3513", "spelling": "kabed", "say": "kah-BAYD",
         "text": ["Heavy. Jacob's eyes were heavy with age; the word is also used of ears that are dull and hearts that "
                  "are hard, and its root gives the word for glory, which is weight of another kind."],
         "samples": [("Genesis", 48, 10), ("Isaiah", 6, 10)]},
        {"key": "H6965", "spelling": "qum", "say": "koom",
         "text": ["The everyday verb for standing or rising up, used of eyes only twice in the Bible, and both times "
                  "in Shiloh: Eli at the gate, and Ahijah in his house. Eyes that have stood still and no longer "
                  "follow what is in front of them. The count below is of the verb in all its uses; the two verses "
                  "are the ones about eyes."],
         "samples": [("1 Samuel", 4, 15), ("1 Kings", 14, 4)]},
        {"key": "H2821", "spelling": "chashak", "say": "khah-SHAKH",
         "text": ["To be dark, to grow dark. Ecclesiastes 12 uses it of the old: 'those watching through windows see "
                  "dimly', in its picture of the body failing. Lamentations uses it of eyes dimmed by sorrow. The "
                  "Bible has no word for low vision; this and the words above are how it says it."],
         "samples": [("Ecclesiastes", 12, 3), ("Lamentations", 5, 17)]},
    ]),
    ("Sight taken", "Two men in the Bible are blinded by their enemies, Samson and Zedekiah, and the words for it are not gentle.", [
        {"key": "H5365", "spelling": "naqar", "say": "nah-KAR",
         "text": ["To bore, to dig out, to quarry. Samson's word. The only other eyes it is used of are the right eyes "
                  "Nahash the Ammonite demanded at Jabesh-gilead. Isaiah uses it for the quarry Israel was hewn from."],
         "samples": [("Judges", 16, 21), ("1 Samuel", 11, 2), ("Isaiah", 51, 1)]},
        {"key": "H5178", "spelling": "nechosheth", "say": "neh-KHO-sheth",
         "text": ["Copper or bronze, and in its paired form a pair of bronze fetters. Both blinded men were led away "
                  "in it. The count is of the metal in all its uses; the verses are the fetters."],
         "samples": [("Judges", 16, 21), ("2 Kings", 25, 7), ("Jeremiah", 39, 7)]},
        {"key": "H2912", "spelling": "tachan", "say": "tah-KHAN",
         "text": ["To grind grain, the daily work of the hand mill, usually done by women or slaves. Samson was put to "
                  "it in the prison at Gaza."],
         "samples": [("Judges", 16, 21), ("Exodus", 32, 20), ("Isaiah", 47, 2)]},
    ]),
    ("Around the blind", "The words the Law and the stories use when a blind person is in the room.", [
        {"key": "H4383", "spelling": "mikshol", "say": "mik-SHOLE",
         "text": ["A stumbling block, literal or figurative, from a verb meaning to totter or fall. Leviticus 19:14 is "
                  "the one place it is plainly literal; everywhere else it is what brings ruin."],
         "samples": [("Leviticus", 19, 14), ("Jeremiah", 6, 21), ("Psalm", 119, 165)]},
        {"key": "H4959", "spelling": "mashash", "say": "mah-SHASH",
         "text": ["To feel over, and so to grope. Isaac felt Jacob with it. Outside Genesis 27 it is mostly the blind "
                  "groping at noon in the curses and in Job."],
         "samples": [("Genesis", 27, 22), ("Deuteronomy", 28, 29), ("Job", 12, 25)]},
        {"key": "H1659", "spelling": "gashash", "say": "gah-SHASH",
         "text": ["A second word for groping, used once only, in Isaiah's confession: like the blind, we feel our "
                  "way along the wall."],
         "samples": [("Isaiah", 59, 10)]},
        {"key": "H5234", "spelling": "nakar", "say": "nah-KAR",
         "text": ["To look closely and recognize; in one form, to make oneself unrecognizable. Isaac did not recognize "
                  "Jacob; Jacob recognized Joseph's robe; the queen disguised herself and the blind prophet named her."],
         "samples": [("Genesis", 27, 23), ("Genesis", 42, 8), ("1 Kings", 14, 6)]},
        {"key": "H3971", "spelling": "mum", "say": "moom",
         "text": ["A blemish, physical or moral. The word that keeps the blind priest from the altar and the blind lamb "
                  "from being offered, and the word for what Absalom and the bride did not have."],
         "samples": [("Leviticus", 21, 18), ("Leviticus", 22, 20), ("2 Samuel", 14, 25)]},
        {"key": "H8549", "spelling": "tamim", "say": "tah-MEEM",
         "text": ["Entire, whole, complete: the Passover lamb's word, and far more often a word for people. A blind "
                  "man can walk tamim."],
         "samples": [("Exodus", 12, 5), ("Deuteronomy", 18, 13), ("Psalm", 15, 2)]},
        {"key": "H2670", "spelling": "chophshi", "say": "khof-SHEE",
         "text": ["Free, exempt: the word for the servant released in the seventh year, and for the servant whose "
                  "master blinded him."],
         "samples": [("Exodus", 21, 2), ("Exodus", 21, 26)]},
        {"key": "H1865", "spelling": "deror", "say": "deh-RORE",
         "text": ["Liberty: the Jubilee's word, and the word Jesus read at Nazareth from Isaiah 61."],
         "samples": [("Leviticus", 25, 10), ("Isaiah", 61, 1)]},
        {"key": "H3372", "spelling": "yare", "say": "yah-RAY",
         "text": ["To fear, or to revere. The reason the stumbling block law gives, and the word Malachi ends on. "
                  "The count is of the verb everywhere; the verses are the two laws."],
         "samples": [("Leviticus", 19, 14), ("Malachi", 1, 14)]},
        {"key": "H5869", "spelling": "ayin", "say": "AH-yin",
         "text": ["The eye, and by analogy a spring of water, the eye of the landscape. One of the commonest words "
                  "in the Bible. It is the eye of the servant in Exodus 21, the apple of God's eye in Deuteronomy 32, "
                  "and the eyes of the LORD that are on those who fear Him."],
         "samples": [("Exodus", 21, 26), ("Deuteronomy", 32, 10), ("Psalm", 33, 18)]},
        {"key": "H6491", "spelling": "paqach", "say": "pah-KAKH",
         "text": ["To open the eyes, or the ears. The Old Testament's word for sight given: the LORD opens the eyes of "
                  "the blind, Elisha's servant's eyes are opened on the hills full of horses, and Isaiah's Servant is "
                  "sent to open blind eyes. The verb used of God, never of a physician."],
         "samples": [("2 Kings", 6, 17), ("Psalm", 146, 8), ("Isaiah", 35, 5), ("Isaiah", 42, 7)]},
        {"key": "H7919", "spelling": "sakal", "say": "sah-KAL",
         "text": ["To act with understanding, to prosper by wisdom. The word for what Jacob did when he crossed his "
                  "hands on Joseph's sons: the King James has 'guiding his hands wittingly'. Everywhere else it is "
                  "David behaving wisely and the kings of the earth told to be wise."],
         "samples": [("Genesis", 48, 14), ("1 Samuel", 18, 14), ("Psalm", 2, 10)]},
        {"key": "H2388", "spelling": "chazaq", "say": "khah-ZAK",
         "text": ["To take hold, to be strong. The lad who led Samson 'held his hand' with this word. It is the same "
                  "verb as be strong and of good courage, and the Bible's plainest picture of a guide."],
         "samples": [("Judges", 16, 26)]},
    ]),
]

BOOK_ORDER = list(hebrew.OSIS) + list(greek.BOOKS.values())


def is_greek(entry: dict) -> bool:
    return "greek" in entry


def count_and_verses(entry: dict):
    """(word count, verse count, verses in Bible order) from the tagged texts."""
    if is_greek(entry):
        verses = greek.occurrences(entry["key"])
        return greek.count(entry["key"]), len(verses), verses
    verses = hebrew.occurrences(entry["key"])
    return hebrew.count(entry["key"]), len(verses), verses


def gloss(entry: dict) -> str:
    e = greek.entry(entry["greek"]) if is_greek(entry) else hebrew.entry(entry["key"])
    return e.get("strongs_def", "")


def check(entry: dict) -> None:
    for book, ch, v in entry["samples"]:
        ok = greek.has(book, ch, v, entry["key"]) if is_greek(entry) else hebrew.has(book, ch, v, entry["key"])
        if not ok:
            raise SystemExit(f"words page: {entry['spelling']} is not in {book} {ch}:{v}")


def pages_using(entry: dict) -> list[tuple[str, str]]:
    """Pages whose own word section follows this word (from src/words.py), plus any listed by hand."""
    import words as wd
    import stories as st
    import pages as pg
    titles = {s["slug"]: ("stories/" + s["slug"] + ".html", s["title"]) for s in st.STORIES}
    titles.update({p["slug"]: (f"{p['section']}/{p['slug']}.html", p["title"]) for p in pg.PAGES if p.get("section") in ("law", "life")})
    out = []
    for slug, entries in wd.WORDS.items():
        if any(w["number"] == entry["key"] for w in entries) and slug in titles:
            out.append(titles[slug])
    out += entry.get("also", [])
    return out
