"""Look up the Greek behind a New Testament verse: the lemma of each word, and what Strong's says a word means.

Two free sources on the shelf (data/raw/shelf, listed in SOURCE.md):
- MorphGNT (morphgnt_<nn-Book>.txt): the SBL Greek New Testament, one word per line, with its lemma. The
  parsing data is CC BY-SA 3.0; the site does not republish the Greek text, it only counts and locates lemmas.
- Strong's Greek dictionary of 1894 (strongs-greek-dictionary.js), in Open Scriptures' JSON edition.

Unlike the Hebrew files, MorphGNT carries no Strong's numbers, so verses are matched by lemma (for example
"τυφλός" for blind). The English on the pages stays the Berean Standard Bible.
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
# MorphGNT book codes (the first two digits of each line) -> the names used on the site
BOOKS = {"01": "Matthew", "02": "Mark", "03": "Luke", "04": "John", "05": "Acts", "06": "Romans",
         "07": "1 Corinthians", "08": "2 Corinthians", "09": "Galatians", "10": "Ephesians", "11": "Philippians",
         "12": "Colossians", "13": "1 Thessalonians", "14": "2 Thessalonians", "15": "1 Timothy", "16": "2 Timothy",
         "17": "Titus", "18": "Philemon", "19": "Hebrews", "20": "James", "21": "1 Peter", "22": "2 Peter",
         "23": "1 John", "24": "2 John", "25": "3 John", "26": "Jude", "27": "Revelation"}


@lru_cache(maxsize=None)
def strongs() -> dict:
    """The dictionary, keyed 'G5185' -> {lemma, translit, strongs_def, kjv_def, derivation}."""
    js = (SHELF / "strongs-greek-dictionary.js").read_text(encoding="utf-8")
    body = js[js.index("{"):js.rindex("}") + 1]
    return json.loads(body)


def entry(number: str) -> dict:
    return strongs().get(number, {})


@lru_cache(maxsize=None)
def _rows() -> list[tuple[str, int, int, str, str]]:
    """Every word of the New Testament as (book, chapter, verse, word as written, lemma)."""
    out = []
    for f in sorted(SHELF.glob("morphgnt_[0-9]*.txt")):
        for ln in f.read_text(encoding="utf-8").splitlines():
            parts = ln.split()
            if len(parts) < 7:
                continue
            code, text, lemma = parts[0], parts[3], parts[6]
            out.append((BOOKS[code[:2]], int(code[2:4]), int(code[4:6]), text, lemma))
    return out


def occurrences(lemma: str) -> list[tuple[str, int, int]]:
    """Every verse in which the lemma occurs, in Bible order, once per verse."""
    seen, out = set(), []
    for book, ch, v, _, lem in _rows():
        if lem == lemma and (book, ch, v) not in seen:
            seen.add((book, ch, v))
            out.append((book, ch, v))
    return out


def count(lemma: str) -> int:
    """How many times the lemma occurs as a word (not verses)."""
    return sum(1 for *_, lem in _rows() if lem == lemma)


def has(book: str, chapter: int, verse: int, lemma: str) -> bool:
    return any(b == book and c == chapter and v == verse and lem == lemma for b, c, v, _, lem in _rows())
