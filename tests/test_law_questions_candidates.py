"""Checks on the law-questions candidates. No network: reads only files already in the repo.

data/reference/law_questions_candidates.json holds candidate items for Brian's two questions
from reading the law pages (Hammurabi against Moses and the blind; priestly duties, touch, and
the other Levites). Every item must point to a quote that really is in the reference shelf.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
CANDIDATES = ROOT / "data" / "reference" / "law_questions_candidates.json"
DIGEST = ROOT / "docs" / "LAW_QUESTIONS_DIGEST.md"
REQUIRED_KEYS = [
    "dating", "earlier-texts-blinding", "earlier-texts-regard", "priest-duties",
    "touching-holy-things", "blemished-priest-provision", "priestly-numbers",
]
NEW_FILES = ["budge_amenemopet_1924.txt"] + [
    f"wikipedia_{t}.wiki.txt" for t in (
        "Hittite_laws", "Code_of_Ur-Nammu", "Laws_of_Eshnunna", "Code_of_Lipit-Ishtar", "Assyrian_law",
        "Instruction_of_Amenemope", "Ebers_Papyrus", "Harpers_Songs", "The_Exodus", "Documentary_hypothesis",
        "Mosaic_authorship", "Priestly_divisions", "Showbread", "Uzzah", "Nadab_and_Abihu", "Laver", "Emor",
        "Moses", "Hammurabi")]
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


def test_item_counts_are_in_the_agreed_range():
    data = load()
    for key in REQUIRED_KEYS:
        assert 3 <= len(data[key]) <= 10, (key, len(data[key]))


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
    # the brief for this pass: say what each item does not show
    missing = [(k, i) for k, i, item in all_items() if not item.get("caution")]
    assert not missing, missing


def test_every_evidence_file_exists_and_the_offset_is_an_int():
    for key, i, item in all_items():
        for j, ev in enumerate(item["evidence"]):
            where = f"{key}[{i}].evidence[{j}]"
            assert set(ev) == {"file", "offset", "quote"}, where
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


def test_wikipedia_revision_dates_match_the_files():
    # 'revision of 25 September 2026' must agree with the timestamp in the file's first line
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    for key, i, item in all_items():
        for ev in item["evidence"]:
            if not ev["file"].startswith("wikipedia_"):
                continue
            head = shelf_text(ev["file"]).splitlines()[0]
            m = re.search(r"title: (.*?); revid: \d+; timestamp: (\d{4})-(\d\d)-(\d\d)T", head)
            assert m, ev["file"]
            y, mo, d = int(m.group(2)), int(m.group(3)), int(m.group(4))
            want = f"revision of {d} {months[mo - 1]} {y}"
            assert want in item["source"], (key, i, ev["file"], want)


def test_shelf_files_are_in_source_md_and_in_the_index_works_list():
    source = (SHELF / "SOURCE.md").read_text(encoding="utf-8")
    works = (ROOT / "src" / "build_shelf_index.py").read_text(encoding="utf-8")
    for key, i, item in all_items():
        for ev in item["evidence"]:
            assert f"`{ev['file']}`" in source, (key, ev["file"])
            assert f'"{ev["file"]}"' in works, (key, "not in WORKS", ev["file"])
    for name in NEW_FILES:
        assert f"`{name}`" in source, name
        assert f'"{name}"' in works, name


def test_the_new_book_has_a_licence_basis_and_is_lf_normalised():
    source = (SHELF / "SOURCE.md").read_text(encoding="utf-8")
    name = "budge_amenemopet_1924.txt"
    entry = [e for e in source.split("\n## ")[1:] if f"`{name}`" in e]
    assert len(entry) == 1, name
    assert "Public domain" in entry[0] and "- Licence basis:" in entry[0], name
    assert "archive.org" in entry[0], name
    assert b"\r" not in (SHELF / name).read_bytes(), f"{name} is not LF-normalised"


def test_new_wikipedia_files_are_lf_normalised_and_have_a_header_line():
    for name in NEW_FILES:
        if not name.startswith("wikipedia_"):
            continue
        raw = (SHELF / name).read_bytes()
        assert b"\r" not in raw, name
        assert raw.startswith(b"<!-- title: "), name


def test_request_budget_for_this_pass():
    # the pass was allowed at most 40 new requests; the log held 42 lines before it began
    lines = (SHELF / "request_log.txt").read_text(encoding="utf-8").splitlines()
    assert len(lines) <= 42 + 40


def test_digest_has_the_required_sections():
    digest = DIGEST.read_text(encoding="utf-8")
    for key in REQUIRED_KEYS:
        assert f"`{key}`" in digest, key
    assert "## What remains unknown" in digest
    assert "## Modern works Brian could consult" in digest
    low = digest.lower()
    assert "general knowledge" in low and "unverified" in low
    assert "## Language flagged, not reproduced" in digest
    assert "what the shelf does not say" in low or "frank" in low
    assert "Brian's question A" in digest and "Brian's question B" in digest


def test_digest_counts_match_the_json():
    digest = DIGEST.read_text(encoding="utf-8")
    data = load()
    total = sum(len(v) for v in data.values())
    assert f"Counts: {total} items across {len(data)} keys" in digest, (total, len(data))
    for key, items in data.items():
        assert f"`{key}` {len(items)}" in digest, key
