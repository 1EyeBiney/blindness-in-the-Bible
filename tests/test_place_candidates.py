"""Checks on the place-and-time candidates. No network: reads only files already in the repo.

data/reference/place_and_time_candidates.json holds candidate "place and time" items
for the stories that do not have one yet, and answers to Brian's requests. Every
item must point to a quote that really is in the reference shelf.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import stories  # noqa: E402

SHELF = ROOT / "data" / "raw" / "shelf"
CANDIDATES = ROOT / "data" / "reference" / "place_and_time_candidates.json"
REQUEST_KEYS = ["luke-14-parable", "jeremiah-31", "job-29-15", "siloam-walk"]
WINDOW = 2000

_cache = {}


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def shelf_text(name):
    if name not in _cache:
        # newline=None (the default) normalises line endings, as the offsets assume
        _cache[name] = (SHELF / name).read_text(encoding="utf-8")
    return _cache[name]


def load():
    return json.loads(CANDIDATES.read_text(encoding="utf-8"))


def all_items():
    for key, items in load().items():
        for i, item in enumerate(items):
            yield key, i, item


def test_json_parses_and_is_an_object_of_lists():
    data = load()
    assert isinstance(data, dict) and data
    for key, items in data.items():
        assert isinstance(items, list), key


def test_every_story_without_place_and_time_has_a_key_and_the_requests_are_there():
    data = load()
    # every story except the one written by hand first (the man born blind) drew on the candidates
    needed = [s["slug"] for s in stories.STORIES if s["slug"] != "man-born-blind"]
    assert len(needed) == 23
    for slug in needed:
        assert slug in data, slug
        # the gatherer was budgeted at seven per story; Job later gained two more by hand (Henry on Mark 8, Pulpit)
        assert 3 <= len(data[slug]) <= (9 if slug == 'job' else 7), (slug, len(data[slug]))
    for key in REQUEST_KEYS:
        assert key in data and data[key], key
    # no key for a story that already has its own place and time, and no unknown keys
    known = set(needed) | set(REQUEST_KEYS)
    assert set(data) <= known, set(data) - known


def test_every_item_has_text_source_evidence_and_confidence():
    for key, i, item in all_items():
        where = f"{key}[{i}]"
        assert isinstance(item.get("text"), str) and item["text"].strip(), where
        assert isinstance(item.get("source"), str) and item["source"].strip(), where
        assert item.get("confidence") in ("high", "medium"), where
        assert isinstance(item.get("evidence"), list) and item["evidence"], where
        if "caution" in item:
            assert isinstance(item["caution"], str) and item["caution"].strip(), where
        extra = set(item) - {"text", "source", "evidence", "confidence", "caution"}
        assert not extra, (where, extra)


def test_every_evidence_file_exists_and_the_offset_is_an_int():
    for key, i, item in all_items():
        for j, ev in enumerate(item["evidence"]):
            where = f"{key}[{i}].evidence[{j}]"
            assert (SHELF / ev["file"]).is_file(), (where, ev["file"])
            assert isinstance(ev["offset"], int) and not isinstance(ev["offset"], bool), where
            assert ev["offset"] >= 0, where
            assert isinstance(ev["quote"], str) and ev["quote"].strip(), where
            assert len(ev["quote"].split()) < 60, (where, "quote is 60 words or more")


def test_every_quote_occurs_in_its_file_within_2000_characters_of_its_offset():
    for key, i, item in all_items():
        for j, ev in enumerate(item["evidence"]):
            where = f"{key}[{i}].evidence[{j}]"
            text = shelf_text(ev["file"])
            off = ev["offset"]
            assert off <= len(text), where
            window = collapse(text[max(0, off - WINDOW): off + WINDOW])
            assert collapse(ev["quote"]) in window, (where, ev["quote"][:70])


def test_quotes_are_checked_against_the_exact_spot_not_just_the_window():
    # Tighter check: the quote starts at the stated offset (whitespace-insensitive)
    for key, i, item in all_items():
        for j, ev in enumerate(item["evidence"]):
            text = shelf_text(ev["file"])
            here = collapse(text[ev["offset"]: ev["offset"] + len(ev["quote"]) * 3 + 200])
            assert here.startswith(collapse(ev["quote"])), (key, i, j, ev["quote"][:60])


def test_wikipedia_sources_name_a_revision_and_the_licence():
    for key, i, item in all_items():
        uses_wiki = any(ev["file"].startswith("wikipedia_") for ev in item["evidence"])
        if uses_wiki:
            assert "Wikipedia" in item["source"], (key, i)
            assert "CC BY-SA 4.0" in item["source"], (key, i)
            assert "revision of" in item["source"], (key, i)
