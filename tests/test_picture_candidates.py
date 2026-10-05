"""Checks on the picture candidates. No network: reads only files already in the repo.

data/reference/picture_candidates.json holds candidate items for the seven 'Blindness as a picture'
pages (src/picture.py): what the commentators on the shelf say about the passages, the place and time
behind them, and how they relate the figure to physical blindness. Every item must point to a quote
that really is in the reference shelf. data/reference/picture_remarks.json holds the remarks table and
the flagged passages behind docs/PICTURE_DIGEST.md, checked the same way.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
CANDIDATES = ROOT / "data" / "reference" / "picture_candidates.json"
REMARKS = ROOT / "data" / "reference" / "picture_remarks.json"
DIGEST = ROOT / "docs" / "PICTURE_DIGEST.md"
REQUIRED_KEYS = [
    "blind-guides", "eyes-that-cannot-see", "gods-people-called-blind", "like-the-blind",
    "eyes-dim-with-grief", "bribes-and-curses", "eyes-opened",
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


def all_evidence():
    for key, i, item in all_items():
        for j, ev in enumerate(item["evidence"]):
            yield f"{key}[{i}].evidence[{j}]", ev
    rem = json.loads(REMARKS.read_text(encoding="utf-8"))
    for group in ("remarks", "flagged"):
        for j, r in enumerate(rem[group]):
            yield f"{group}[{j}]", r


def test_json_parses_and_is_an_object_of_lists():
    data = load()
    assert isinstance(data, dict) and data
    for key, items in data.items():
        assert isinstance(items, list), key


def test_keys_are_exactly_the_seven_slugs_of_the_picture_pages():
    sys.path.insert(0, str(ROOT / "src"))
    import picture
    slugs = [p["slug"] for p in picture.PICTURE_PAGES]
    assert slugs == REQUIRED_KEYS, slugs
    assert set(load()) == set(REQUIRED_KEYS), set(load()) ^ set(REQUIRED_KEYS)


def test_item_counts_are_in_the_agreed_range():
    data = load()
    for key in REQUIRED_KEYS:
        assert 4 <= len(data[key]) <= 8, (key, len(data[key]))


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


def test_every_item_carries_a_caution():
    missing = [(k, i) for k, i, item in all_items() if not item.get("caution")]
    assert not missing, missing


def test_every_evidence_file_exists_and_the_offset_is_an_int():
    for where, ev in all_evidence():
        assert set(ev) >= {"file", "offset", "quote"}, where
        assert (SHELF / ev["file"]).is_file(), (where, ev["file"])
        assert isinstance(ev["offset"], int) and not isinstance(ev["offset"], bool), where
        assert ev["offset"] >= 0, where
        assert isinstance(ev["quote"], str) and ev["quote"].strip(), where
        assert len(ev["quote"].split()) < 60, (where, "quote is 60 words or more")


def test_every_quote_occurs_in_its_file_within_2000_characters_of_its_offset():
    for where, ev in all_evidence():
        text = shelf_text(ev["file"])
        off = ev["offset"]
        assert off <= len(text), where
        window = collapse(text[max(0, off - WINDOW): off + WINDOW])
        assert collapse(ev["quote"]) in window, (where, ev["quote"][:70])


def test_quotes_start_at_the_stated_offset():
    for where, ev in all_evidence():
        text = shelf_text(ev["file"])
        here = collapse(text[ev["offset"]: ev["offset"] + len(ev["quote"]) * 3 + 200])
        assert here.startswith(collapse(ev["quote"])), (where, ev["quote"][:60])


def test_shelf_files_are_in_source_md_and_in_the_index_works_list():
    source = (SHELF / "SOURCE.md").read_text(encoding="utf-8")
    works = (ROOT / "src" / "build_shelf_index.py").read_text(encoding="utf-8")
    for where, ev in all_evidence():
        assert f"`{ev['file']}`" in source, (where, ev["file"])
        assert f'"{ev["file"]}"' in works, (where, "not in WORKS", ev["file"])


def test_no_wikipedia_files_are_used_so_no_revision_citation_is_needed():
    # this pass drew only on Henry, Edersheim and the dictionaries; if a Wikipedia file is ever added,
    # the source line must name the revision and the licence as in the law-questions candidates
    for key, i, item in all_items():
        for ev in item["evidence"]:
            if ev["file"].startswith("wikipedia_"):
                assert "CC BY-SA 4.0" in item["source"] and "revision of" in item["source"], (key, i)


def test_every_item_cites_a_commentator_or_reference_work_in_its_source():
    names = ("Matthew Henry", "Edersheim", "Easton", "Smith", "International Standard Bible Encyclopaedia")
    for key, i, item in all_items():
        assert any(n in item["source"] for n in names), (key, i)


def test_each_page_has_at_least_one_item_from_henry_and_the_two_physical_figurative_pages_have_more():
    data = load()
    for key in REQUIRED_KEYS:
        assert any(ev["file"].startswith("matthew_henry_") for it in data[key] for ev in it["evidence"]), key
    # the pages Brian's question centres on carry Edersheim or the encyclopaedia as well
    for key in ("blind-guides", "eyes-that-cannot-see", "eyes-opened"):
        files = {ev["file"] for it in data[key] for ev in it["evidence"]}
        assert any(f.startswith(("edersheim", "isbe", "easton")) for f in files), key


def test_the_questions_in_the_brief_are_answered_somewhere():
    data = load()
    blob = " ".join(ev["quote"] for k in data for it in data[k] for ev in it["evidence"])
    for needle in [
        "an oath by the gold of the temple",       # the Temple gold oath
        "Phrygian powder",                          # Laodicean eye-salve
        "school of medicine",                       # the city's school
        "filtered their wine",                      # the gnat and camel
        "wash their hands",                         # the Pharisees' hand-washing
        "sealed up",                                # Isaiah's sealed scroll
        "sentinel on the city walls",               # who the watchmen were
        "the last day in the Temple",               # setting of the Matthew 23 woes
        "calamity of blindness",                    # John 9:39-41
        "they did not believe, because they could not believe",   # John 12:37-41
        "Haphtarah",                                # Luke 4
        "righteous hand of God",
    ]:
        assert needle.lower() in blob.lower(), needle


def test_the_remarks_cover_each_commentator_and_the_flagged_list_is_not_empty():
    rem = json.loads(REMARKS.read_text(encoding="utf-8"))
    who = {r["who"] for r in rem["remarks"]}
    assert {"Henry", "Edersheim", "ISBE 1915", "Easton"} <= who, who
    assert len(rem["remarks"]) >= 25
    assert len(rem["flagged"]) >= 10
    for r in rem["remarks"] + rem["flagged"]:
        assert r["note"].strip() and r["locator"].strip(), r


def test_flagged_passages_are_not_used_as_evidence_in_the_items():
    rem = json.loads(REMARKS.read_text(encoding="utf-8"))
    used = {(ev["file"], ev["offset"]) for _, _, item in all_items() for ev in item["evidence"]}
    # two flagged anchors are used on purpose, with a caution, as the digest says
    allowed = {"A cruel custom therefore sanc- tioned among heathen nat ions"}
    for r in rem["flagged"]:
        if r["quote"] in allowed:
            continue
        assert (r["file"], r["offset"]) not in used, r["quote"]


def test_digest_has_the_required_sections():
    digest = DIGEST.read_text(encoding="utf-8")
    for key in REQUIRED_KEYS:
        assert f"`{key}`" in digest, key
    assert "## What remains unknown" in digest
    assert "## Modern works Brian could consult" in digest
    assert "## Every place the commentators remark on physical versus figurative blindness" in digest
    assert "## Language flagged, not reproduced" in digest
    assert "## What the picture assumes about the blind" in digest
    low = digest.lower()
    assert "general knowledge" in low and "unverified" in low
    assert "what the shelf does not say" in low or "frank" in low or "plainly" in low


def test_digest_counts_match_the_json():
    digest = DIGEST.read_text(encoding="utf-8")
    data = load()
    total = sum(len(v) for v in data.values())
    assert f"Counts: {total} items across {len(data)} keys" in digest, (total, len(data))
    for key, items in data.items():
        assert f"`{key}` {len(items)}" in digest, key
        assert f"## `{key}` ({len(items)} items)" in digest, key


def test_digest_remark_and_flag_tables_list_every_entry():
    digest = DIGEST.read_text(encoding="utf-8")
    rem = json.loads(REMARKS.read_text(encoding="utf-8"))
    for r in rem["remarks"] + rem["flagged"]:
        assert f"@{r['offset']} |" in digest, r["locator"]


def test_digest_does_not_reproduce_the_flagged_quotes_at_length():
    digest = DIGEST.read_text(encoding="utf-8")
    rem = json.loads(REMARKS.read_text(encoding="utf-8"))
    for r in rem["flagged"]:
        assert r["quote"] not in digest, r["quote"][:50]
