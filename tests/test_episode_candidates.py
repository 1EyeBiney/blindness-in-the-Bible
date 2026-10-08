"""The episode research file: every quote really is in its shelf file at its offset, and every item is sourced."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
DATA = json.loads((ROOT / "data" / "reference" / "episode_candidates.json").read_text(encoding="utf-8"))
_cache = {}


def shelf_text(name):
    if name not in _cache:
        _cache[name] = (SHELF / name).read_text(encoding="utf-8")
    return _cache[name]


def collapse(s):
    return re.sub(r"\s+", " ", s)


def items():
    for key, lst in DATA.items():
        for i, it in enumerate(lst):
            yield key, i, it


def test_keys_are_the_seven_healing_stories_with_enough_items():
    assert set(DATA) == {"bartimaeus", "bethsaida", "two-blind-men", "blind-and-mute-man", "the-temple",
                         "crowds-by-the-sea", "answer-to-john"}
    for key, lst in DATA.items():
        assert len(lst) >= 8, key


def test_every_item_is_sourced_and_shaped():
    for key, i, it in items():
        assert it["text"].strip() and it["source"].strip(), (key, i)
        assert it["confidence"] in ("high", "medium"), (key, i)
        assert it["evidence"], (key, i)
        assert not set(it) - {"text", "source", "evidence", "confidence", "caution"}, (key, i)


def test_every_quote_starts_at_its_offset():
    for key, i, it in items():
        for j, ev in enumerate(it["evidence"]):
            text = shelf_text(ev["file"])
            assert len(ev["quote"].split()) < 60, (key, i, j)
            here = collapse(text[ev["offset"]: ev["offset"] + len(ev["quote"]) * 3 + 200])
            assert here.startswith(collapse(ev["quote"])), (key, i, j, ev["quote"][:60])


def test_prejudiced_wording_stays_out_of_the_text_fields():
    for key, i, it in items():
        low = it["text"].lower()
        for word in ("heathen", "poor sufferers", "mass of misery", "the herd", "diabolism"):
            assert word not in low, (key, i, word)
