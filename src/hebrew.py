"""Look up the Hebrew behind a verse: which word, which Strong's number, and what Strong's says it means.

Two free sources on the shelf (data/raw/shelf, listed in SOURCE.md):
- The Open Scriptures Hebrew Bible (oshb_<Book>.xml): the Westminster Leningrad Codex with every word tagged
  with its Strong's number. CC BY 4.0.
- Strong's Hebrew dictionary of 1894 (strongs-hebrew-dictionary.js), in Open Scriptures' JSON edition.
  Public-domain text; the edition is CC BY-SA.

The site uses these to say, with a source, which Hebrew word a law uses and where else that word appears.
Nothing here is a translation: the English on the pages stays the Berean Standard Bible.
"""
from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
OSIS = {
        "Genesis": "Gen",
        "Exodus": "Exod",
        "Leviticus": "Lev",
        "Numbers": "Num",
        "Deuteronomy": "Deut",
        "Joshua": "Josh",
        "Judges": "Judg",
        "Ruth": "Ruth",
        "1 Samuel": "1Sam",
        "2 Samuel": "2Sam",
        "1 Kings": "1Kgs",
        "2 Kings": "2Kgs",
        "1 Chronicles": "1Chr",
        "2 Chronicles": "2Chr",
        "Ezra": "Ezra",
        "Nehemiah": "Neh",
        "Esther": "Esth",
        "Job": "Job",
        "Psalm": "Ps",
        "Proverbs": "Prov",
        "Ecclesiastes": "Eccl",
        "Song of Solomon": "Song",
        "Isaiah": "Isa",
        "Jeremiah": "Jer",
        "Lamentations": "Lam",
        "Ezekiel": "Ezek",
        "Daniel": "Dan",
        "Hosea": "Hos",
        "Joel": "Joel",
        "Amos": "Amos",
        "Obadiah": "Obad",
        "Jonah": "Jonah",
        "Micah": "Mic",
        "Nahum": "Nah",
        "Habakkuk": "Hab",
        "Zephaniah": "Zeph",
        "Haggai": "Hag",
        "Zechariah": "Zech",
        "Malachi": "Mal"}
NS = {"o": "http://www.bibletechnologies.net/2003/OSIS/namespace"}


@lru_cache(maxsize=None)
def strongs() -> dict:
    """The dictionary, keyed 'H4383' -> {lemma, xlit, pron, derivation, strongs_def, kjv_def}."""
    js = (SHELF / "strongs-hebrew-dictionary.js").read_text(encoding="utf-8")
    body = js[js.index("{"):js.rindex("}") + 1]
    return json.loads(body)


@lru_cache(maxsize=None)
def _book(book: str) -> ET.Element:
    return ET.parse(SHELF / f"oshb_{OSIS[book]}.xml").getroot()


def words(book: str, chapter: int, verse: int) -> list[dict]:
    """Every word of the verse: the Hebrew as written, its Strong's number(s) and its dictionary entry."""
    root = _book(book)
    vid = f"{OSIS[book]}.{chapter}.{verse}"
    v = root.find(f".//o:verse[@osisID='{vid}']", NS)
    if v is None:
        raise KeyError(vid)
    out = []
    for w in v.findall("o:w", NS):
        lemma = w.get("lemma", "")
        # 'c/7121' or '5787 a' or 'b/4383': prefixes before '/', the number is the last part, letters are senses
        nums = [re.sub(r"[^\d]", "", part) for part in lemma.split("/")]
        nums = [n for n in nums if n]
        key = f"H{nums[-1]}" if nums else ""
        out.append({"hebrew": "".join(w.itertext()).replace("/", ""), "lemma": lemma, "strongs": key,
                    "entry": strongs().get(key, {})})
    return out


def has(book: str, chapter: int, verse: int, number: str) -> bool:
    """Does the verse use the word with this Strong's number (e.g. 'H4383')?"""
    return any(w["strongs"] == number for w in words(book, chapter, verse))


def entry(number: str) -> dict:
    return strongs()[number]


if __name__ == "__main__":
    import sys
    book, ch, vs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    for w in words(book, ch, vs):
        e = w["entry"]
        print(f"{w['strongs']:>6}  {w['hebrew']:<14} {e.get('xlit', ''):<14} {e.get('strongs_def', '')[:70]}")
