"""Checks on the law-and-life candidates. No network: reads only files already in the repo.

data/reference/law_and_life_candidates.json holds candidate items for the law pages, the
"Living blind, then" pages and the 2 Corinthians 5:7 page. Every item must point to a quote
that really is in the reference shelf.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
CANDIDATES = ROOT / "data" / "reference" / "law_and_life_candidates.json"
DIGEST = ROOT / "docs" / "LAW_AND_LIFE_DIGEST.md"
REQUIRED_KEYS = [
    "law-stumbling-block", "law-servant-blinded", "law-priest", "law-blind-animals",
    "life-camp", "life-village", "life-town-gate", "life-jerusalem",
    "walk-by-faith", "law-as-evidence",
]
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


def test_every_required_key_is_present_with_items_or_a_note_in_the_digest():
    data = load()
    digest = DIGEST.read_text(encoding="utf-8")
    for key in REQUIRED_KEYS:
        assert key in data, key
        if len(data[key]) < 2:
            # an explicit empty (or one-item) list needs a note in the digest
            assert f"`{key}`" in digest and "no items" in digest.lower(), key
    assert set(data) <= set(REQUIRED_KEYS), set(data) - set(REQUIRED_KEYS)


def test_item_counts_are_in_the_agreed_ranges():
    data = load()
    for key in ("life-camp", "life-village", "life-town-gate", "life-jerusalem"):
        assert 3 <= len(data[key]) <= 8, (key, len(data[key]))
    assert 3 <= len(data["walk-by-faith"]) <= 6


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


def test_quotes_start_at_the_stated_offset():
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


def test_new_shelf_files_are_in_the_index_and_source_md():
    source = (SHELF / "SOURCE.md").read_text(encoding="utf-8")
    for key, i, item in all_items():
        for ev in item["evidence"]:
            assert f"`{ev['file']}`" in source, (key, ev["file"])
