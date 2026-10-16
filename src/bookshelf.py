"""The bookshelf page: every source on the reference shelf, built from the shelf's own record (SOURCE.md), with
the pages that use each one. Because it is read from the record, it cannot fall behind the shelf.

SOURCE.md has one "## Title" entry per file with lines "- File:", "- Author:", "- Year:", "- Source URL:",
"- Retrieved:", "- Licence basis:" and "- Odd things:". Several files make one work (six volumes of Henry, five of
the encyclopedia, twelve tagged books), so entries are grouped into works here. Helper files (fetched HTML pages,
request batches) are left off the page.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "raw" / "shelf" / "SOURCE.md"

TITLE = "The bookshelf"
SLUG = "bookshelf.html"

# How each work is shown, and how to tell which pages cite it: a key found in the first file name, the display
# title, what the site uses it for, how to read it, and the words that appear in a page's source line for it.
WORKS = [
    ("edersheim_sketches", "Alfred Edersheim, Sketches of Jewish Social Life in the Days of Christ (1876)",
     "Daily life in Jesus's day: houses, roads, trades, the synagogue, the Temple.",
     "A careful Victorian scholar, Jewish by birth and a Christian by conviction, who knew the rabbinic sources. Read for customs, not for his "
     "judgments of people.", ["Sketches of Jewish Social Life"]),
    ("edersheim_life_and_times", "Alfred Edersheim, The Life and Times of Jesus the Messiah (1883)",
     "Where each Gospel story happened, and what the rabbis of the day thought about blindness, sin and healing.",
     "The same author at full length. His placings of unnamed towns are his opinions and are marked as such.",
     ["Life and Times"]),
    ("josephus_antiquities", "Josephus, The Antiquities of the Jews (Whiston's translation, 1737)",
     "A first-century Jewish retelling of the Law and of Israel's history, with the places and rulers named.",
     "Josephus wrote for Roman readers and smooths things. Whiston's notes are eighteenth-century and sometimes "
     "unkind; they are not used.", ["Antiquities"]),
    ("josephus_wars", "Josephus, The Wars of the Jews (Whiston's translation, 1737)",
     "Jerusalem, its pools and walls, and the fortress of Machaerus, by a man who saw them.",
     "The one eyewitness on the shelf for first-century Jerusalem.", ["Wars of the Jews"]),
    ("smiths_bible_dictionary", "Smith's Bible Dictionary (1884 edition)",
     "Places, people and things: what a city gate was for, what a priest did, where Dothan lay.",
     "Short, factual entries. Its archaeology is out of date and is checked against Wikipedia.", ["Smith's"]),
    ("easton_ebd", "Easton's Bible Dictionary (1897)",
     "Brief entries on people and places, used beside Smith's.",
     "Plainer than Smith's and more pious in tone; used for facts.", ["Easton's"]),
    ("isbe_1915", "The International Standard Bible Encyclopedia (1915), five volumes",
     "Longer articles: blindness and eye disease in the ancient Near East, the Hebrew words, the law codes, slavery.",
     "Written by specialists, including an Assyriologist and a doctor who had practised in Palestine. The best "
     "of the shelf for the Law pages.", ["International Standard Bible Encyclopedia", "1915 encyclopedia"]),
    ("matthew_henry", "Matthew Henry, Commentary on the Whole Bible (1706 to 1721), six volumes",
     "What a careful reader three hundred years ago made of each passage, and the purposes he saw in each law.",
     "A pastor, not a historian. Quoted for his readings, which are always marked as his.", ["Matthew Henry", "Henry"]),
    ("pulpit_commentary", "The Pulpit Commentary, on Job 29:15 (1880 to 1919)",
     "One passage only: Job as eyes to the blind.",
     "Fetched for a single question Brian asked.", ["Pulpit"]),
    ("hammurabi", "The Code of Hammurabi, translated by C. H. W. Johns (1903)",
     "The Babylonian law code, for comparison with the Law of Moses on eyes, servants and injury.",
     "Johns's translation is old but public domain, and the laws cited are checked against it word for word.",
     ["Hammurabi, translated"]),
    ("budge_amenemopet", "The Instruction of Amenemope, translated by E. A. Wallis Budge (1924)",
     "An Egyptian wisdom text that tells its reader not to laugh at a blind man.",
     "Budge's translation; the dating of the text is given as a range because scholars disagree.", ["Budge"]),
    ("wilson_biography", "James Wilson, Biography of the Blind (1838)",
     "Lives of blind people through history, by a blind author.",
     "Early and partial, and says so.", ["Wilson"]),
    ("levy_blindness", "W. Hanks Levy, Blindness and the Blind (1872)",
     "How blind people lived and worked in the nineteenth century, and what was known of earlier times.",
     "Levy was himself blind. His history of the ancient world is thin, and the page that uses him says so.", ["Levy"]),
    ("strongs-hebrew", "Strong's Hebrew dictionary (1894), Open Scriptures edition",
     "The meaning of the Hebrew word behind each law about the blind.",
     "A concordance dictionary: brief glosses, not a modern lexicon. Used for the plain sense of a word.",
     ["Strong's"]),
    ("oshb_", "The Open Scriptures Hebrew Bible: the Hebrew text, every word tagged",
     "Which Hebrew word stands in each verse, so that the pages can say where else a word is used.",
     "The Westminster Leningrad Codex with each word tagged with its Strong's number. Every claim on the pages "
     "about a word is checked against it on each build.", ["Open Scriptures Hebrew Bible"]),
]
SKIP = (".json", ".html")       # working files, not sources


def entries() -> list[dict]:
    out = []
    for block in SOURCE.read_text(encoding="utf-8").split("\n## ")[1:]:
        title, _, body = block.partition("\n")
        d = {"title": title.strip()}
        for key in ("File", "Files", "Author", "Year", "Source URL", "Retrieved", "Licence basis", "Size", "Odd things"):
            m = re.search(rf"^- {re.escape(key)}: (.*)$", body, flags=re.M)
            if m:
                d[key.lower().replace(" ", "_")] = m.group(1).strip()
        files = re.findall(r"`([^`]+)`", d.get("file", "") + " " + d.get("files", ""))
        d["files"] = files
        out.append(d)
    return out


def _pages_citing(words_: list[str]) -> list[tuple[str, str]]:
    """(href, title) of every page whose place-and-time sources, or word sections, mention any of the words."""
    import pages as pg
    import picture as pic
    import stories as st
    found = []
    for s in st.STORIES:
        if any(w in it["source"] for it in s.get("place_and_time", []) for w in words_):
            found.append((f"stories/{s['slug']}.html", s["title"]))
    for p in pg.PAGES:
        if any(w in it["source"] for it in p.get("place_and_time", []) for w in words_):
            href = "walk-by-faith.html" if p["slug"] == "walk-by-faith" else f"{p['section']}/{p['slug']}.html"
            found.append((href, p["title"]))
    for p in pic.PICTURE_PAGES:
        if any(w in it["source"] for it in p.get("place_and_time", []) for w in words_):
            found.append((f"picture/{p['slug']}.html", p["title"]))
    if any(w in ("Strong's", "Open Scriptures Hebrew Bible") for w in words_):
        import words as wd
        for p in pg.by_section("law"):
            if p["slug"] in wd.WORDS:
                found.append((f"law/{p['slug']}.html", p["title"]))
    return found


def works() -> list[dict]:
    """The books, grouped, each with its record and the pages that cite it."""
    ents = entries()
    out = []
    for key, title, used_for, read_as, cite_words in WORKS:
        mine = [d for d in ents if any(f.startswith(key) or key in f for f in d["files"])]
        if not mine:
            continue
        out.append({"title": title, "used_for": used_for, "read_as": read_as, "entries": mine,
                    "pages": _pages_citing(cite_words)})
    return out


def wikipedia() -> list[dict]:
    """Every Wikipedia article on the shelf, with its revision date and the pages that cite it."""
    out = []
    for d in entries():
        if not any(f.startswith("wikipedia_") and f.endswith(".wiki.txt") for f in d["files"]):
            continue
        name = re.sub(r"^Wikipedia:?\s*", "", d["title"]).strip(' "')
        m = re.search(r"revision of ([^)]+)", d.get("year", "") + " " + d.get("odd_things", ""))
        pages_ = _pages_citing([f'Wikipedia, "{name}'])
        out.append({"name": name, "revision": m.group(1) if m else d.get("retrieved", ""), "url": d.get("source_url", ""),
                    "pages": pages_})
    return sorted(out, key=lambda x: x["name"].lower())


INTRO = [
    "Every fact on this site about the place and the time comes from a book on this shelf, and every paragraph "
    "that uses one names it. This page lists the whole shelf: what each work is, what the site uses it for, how "
    "to read it, under what terms it may be copied, and which pages cite it.",
    "The rules for the shelf are simple. Only works in the public domain or under a free licence are used, so "
    "that anyone may check them. Every quotation is compared against the source file each time the site is "
    "built. And the old books are read for what they knew about places, customs and daily life, not for their "
    "opinions of people, which are sometimes ones we would not share.",
]
