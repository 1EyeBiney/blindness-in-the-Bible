"""Quote specs for the SHELF_REPORT digest.

Each spec is (work label, file, anchor regex, max words). The quote is the text
starting at the anchor, whitespace collapsed, cut at max_words. Locators are
computed from the file by shelf_locate. Nothing here is paraphrased.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_shelf_index import SHELF, WORKS, locator_tracker  # noqa: E402

KIND = {f: (label, kind) for f, label, kind in WORKS}


def read(fname):
    return open(SHELF / fname, encoding="utf-8", errors="replace", newline="").read()


def clean_wiki(s):
    s = re.sub(r"<ref[^>/]*/>|<ref[^>]*>.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\{\{[Ll]ang\|[^|{}]*\|([^{}|]*)(?:\|[^{}]*)?\}\}", r"\1", s)
    for _ in range(3):
        s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", s)
    return re.sub(r"'{2,3}", "", s)


def locate(fname, offset, text):
    label, kind = KIND[fname]
    feed, render = locator_tracker(kind)
    vol = label.split()[-1] if kind == "isbe" else ""
    eol = text.find("\n", offset)
    for line in text[: eol if eol != -1 else len(text)].splitlines():
        feed(line.rstrip("\r"))
    loc = render(vol)
    if kind == "lifetimes":
        ms = list(re.finditer(r"CHAPTER ([IVXL]+)\.?\s*\n+\s*([^\n]+)", text[:offset]))
        if ms:
            loc += f" ({ms[-1].group(2).strip()[:70]})"
    if kind == "josephus":
        ms = list(re.finditer(r"(?:^|\n)\s*(\d+)\.\s", text[:offset]))
        if ms:
            loc += f", section {ms[-1].group(1)}"
    return loc


def quote(fname, anchor, nwords):
    text = read(fname)
    ms = list(re.finditer(anchor.replace(" ", r"\s+"), text))
    if not ms:
        return None
    # prefer the first match that is not in a table of contents / front matter
    m = ms[0]
    chunk = text[m.start(): m.start() + 3000]
    if KIND[fname][1] == "wiki":
        chunk = clean_wiki(chunk)
    words = re.sub(r"\s+", " ", chunk).strip().split(" ")
    q = " ".join(words[:nwords])
    if len(words) > nwords:
        q = q.rstrip(".,;:") + " ..."
    return q, locate(fname, m.start(), text), m.start()


E_LT = "edersheim_life_and_times.txt"
E_SK = "edersheim_sketches.txt"
J_AN = "josephus_antiquities_pg2848.txt"
J_WA = "josephus_wars_pg2850.txt"
SMITH = "smiths_bible_dictionary.txt"
H5 = "matthew_henry_vol5_matthew_to_john.txt"
I1 = "isbe_1915_vol1.txt"
I4 = "isbe_1915_vol4.txt"

TOPICS = [
    ("Blindness and blind people in first-century life", [
        (SMITH, r"Blindness is extremely common in the East", 48),
        (I1, r"The commonest disease is a purulent ophthalmia", 42),
        (I1, r"Blindness unfitted a man for the priesthood", 40),
        (E_LT, r"Indeed, the blind were regarded as specially", 22),
        (E_LT, r"and we constantly find Rabbis, when meeting", 40),
        (E_LT, r"It was a common Jewish view, that the merits", 30),
        (E_SK, r"The eulogies or \"tephillah\" proper", 50),
        (J_AN, r"In like manner, let no one revile a person blind", 12),
        (J_AN, r"shut their gates, and placed the blind", 45),
        (H5, r"These blind men were sitting by the way-side", 40),
    ]),
    ("Begging and alms in Jesus's day", [
        (I1, r"Begging was well known and beggars formed", 45),
        (I1, r"and in the accounts of beggars in connection with public places", 50),
        (I1, r"This prevalence of begging was due largely", 50),
        (I1, r"As to professional beggars", 45),
        (E_LT, r"Remembering, that the entrance to the Temple", 50),
        (E_LT, r"where this blind beggar was wont to sit", 50),
        (E_LT, r"For to persons so wretchedly poor as to allow", 28),
        (E_LT, r"the shrinking from receiving alms was in proportion", 50),
        (E_SK, r"Alms were collected at regular times every week", 45),
        (E_SK, r"Whenever,\" we read, \"a poor man stands at thy door", 52),
        ("wikipedia_Begging.wiki.txt", r"The \[\[New Testament\]\] contains several references", 40),
    ]),
    ("The Pool of Siloam and the water system", [
        (SMITH, r"Siloam is one of the few undisputed localities", 55),
        (SMITH, r"though Josephus tells us that in his day", 26),
        (SMITH, r"At the back part of this fountain a subterraneous", 50),
        (J_WA, r"extended as far as Siloam; for that is the name", 35),
        (E_LT, r"It was made by King Hezekiah, in order both", 50),
        (E_LT, r"at the Feast of Tabernacles, amidst universal rejoicing, water from Siloam", 40),
        (E_LT, r"saliva was commonly regarded as a remedy", 28),
        (E_LT, r"adding to it the direction to go and wash in the Pool of Siloam", 40),
        (I4, r"is a passive form and means", 28),
        ("wikipedia_Pool_of_Siloam.wiki.txt", r"The pool was rediscovered during an excavation work", 42),
        ("wikipedia_Pool_of_Siloam.wiki.txt", r"The pools were fed by the waters of the \[\[Gihon", 22),
        ("wikipedia_Siloam_tunnel.wiki.txt", r"Its popular name is due to the most common hypothesis", 27),
    ]),
    ("Bethsaida", [
        (SMITH, r"Bethsaida\s+\(house of fish\)", 50),
        (E_SK, r"also Bethsaida, \[12\] the name", 20),
        (E_LT, r"just as he changed the name of Bethsaida", 30),
        (H5, r"He led him out of the town\. Had he herein only", 52),
    ]),
    ("Jericho", [
        (SMITH, r"Under Herod the Great it again became an important place", 52),
        (SMITH, r"Thus Jericho was once more", 26),
        (E_SK, r"Flanked and defended by four surrounding forts", 50),
        (E_SK, r"Rome had made it a central station for the collection", 32),
        (E_SK, r"along the fifth great highway", 38),
        (J_WA, r"there is a fountain by Jericho, that runs plentifully", 38),
        (I1, r"BARTIMAEUS, bar-ti-me'us", 15),
    ]),
    ("The Temple and who could enter", [
        (J_WA, r"there was a partition made of stone all round", 55),
        (E_LT, r"Here also there lay about a crowd of noisy beggars", 30),
        (E_LT, r"and the child must be free from all such bodily blemishes", 32),
        (E_LT, r"According to the Mishnah, they who pronounce the benediction", 28),
        (I1, r"Blindness unfitted a man for the priesthood \(Lev 21 18\); but care", 30),
        ("wikipedia_Mikveh.wiki.txt", r"Hundreds of mikvot from the \[\[Second Temple period\]\]", 22),
    ]),
]

FLAGS = [
    (E_LT, r"so thoroughly Judaised were they by their late contact", 40,
     "Treats Jewish thought as something the disciples had to be freed from; 'Judaised' used as a criticism."),
    (E_LT, r"to which they sought to apply the common Jewish solution", 20,
     "Presents rabbinic reasoning about sin and disability as a 'solution' to be corrected."),
    (E_LT, r"despised them as cursed, ignorant country people", 30,
     "Contempt attributed to Jewish leaders, stated as a generalisation about their class."),
    (E_LT, r"Here also there lay about a crowd of noisy beggars, unsightly from disease", 20,
     "Not anti-Jewish, but the language about disabled and sick people is demeaning."),
    (E_SK, r"The result was a system of pure externalism", 25,
     "Sweeping verdict on Pharisaic Judaism; 'arrant hypocrisy' follows in the same passage."),
    (E_SK, r"despised, rejected, and delivered up unto death by the blind guides", 22,
     "Uses blindness as an insult and blames 'fellow-countrymen' collectively for the death of Jesus."),
    (E_SK, r"far more deeply tinged with superstition and error", 15,
     "Dismisses the Babylonian Talmud wholesale."),
    (J_AN, r"were taught Josephus by the Pharisees, a body of men", 22,
     "Whiston's own editorial footnote (footnotes are gathered at the end of Book 2), not Josephus's text; it calls the Pharisees 'very wicked'."),
    (I1, r"defective eyes and bleared, inflamed lids are among", 25,
     "Contemptuous about people with eye disease; also stereotypes crowds in Palestine."),
    (SMITH, r"indolent and licentious", 20,
     "Editor's remark about the people of modern Jericho (Riha); stereotyping of local people."),
]
