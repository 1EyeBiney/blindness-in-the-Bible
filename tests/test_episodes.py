"""Every episode script keeps the series' promises. See audio/episode_lib.py for the rules."""
import importlib
import json
import pkgutil
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "audio"))
import build_site  # noqa: E402
import episode_lib  # noqa: E402
import episodes  # noqa: E402
import stories as st  # noqa: E402
from merge_runs import is_line, merge_runs  # noqa: E402

LINE = episode_lib.LINE
SCENE_SPEAKERS = {"MAN", "NEIGHBOUR", "HELPER", "BARTIMAEUS", "VOICE", "FRIEND", "JOHN", "DISCIPLE"}
MODS = sorted((importlib.import_module(f"episodes.{i.name}") for i in pkgutil.iter_modules(episodes.__path__)
               if i.name.startswith("ep")), key=lambda m: m.NUMBER)
BIBLE = build_site.load_bible()


def lines_of(mod):
    return mod.build(BIBLE)


def spoken(ls):
    return [ln for ln in ls if is_line(ln)]


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_script_on_disk_matches_the_generator(mod):
    base = f"ep{mod.NUMBER:02d}_{mod.SLUG}"
    ls = lines_of(mod)
    assert (episode_lib.OUT_DIR / f"{base}_01.txt").read_text(encoding="utf-8") == "\n".join(ls) + "\n"
    merged = merge_runs(ls, f"{base}_v2")
    assert (episode_lib.OUT_DIR / f"{base}_02.txt").read_text(encoding="utf-8") == "\n".join(merged) + "\n"


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_reader_lines_are_the_official_text_for_the_declared_passages_in_order(mod):
    expected = [BIBLE[(b, c, v)] for b, c, a, z in mod.PASSAGES for v in range(a, z + 1)]
    read = [LINE.match(ln).group(3) for ln in spoken(lines_of(mod)) if ln.startswith("[READER]")]
    assert read == expected, "every declared verse, in order, word for word, and nothing else"
    for b, c, a, z in mod.PASSAGES:
        for v in range(a, z + 1):
            assert (b, c, v) in BIBLE


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_every_scene_is_introduced_with_imagine_and_scene_voices_never_quote_scripture(mod):
    armed = False
    for ln in spoken(lines_of(mod)):
        m = LINE.match(ln)
        who, text = m.group(1), m.group(3)
        if who == "NARRATOR" and "imagine" in text.lower():
            armed = True
        if who in SCENE_SPEAKERS:
            assert armed, ln
            # a scene character may echo a phrase, but never a whole verse
            for b, c, a, z in mod.PASSAGES:
                for v in range(a, z + 1):
                    assert BIBLE[(b, c, v)] not in text, ln
        if who in ("READER", "BRIAN"):
            armed = False


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_brian_lines_are_his_words_or_listed_drafts(mod):
    site_words = " ".join(p for s in st.STORIES for p in s.get("brian", []))
    drafts = " ".join(mod.DRAFT_BRIAN)
    for ln in spoken(lines_of(mod)):
        m = LINE.match(ln)
        if m.group(1) != "BRIAN":
            continue
        text = m.group(3)
        assert text in drafts or text in site_words, text[:80]
    # and the drafts file for Brian carries every draft
    doc = (ROOT / "docs" / "BRIAN_DRAFTS.md").read_text(encoding="utf-8")
    for p in mod.DRAFT_BRIAN:
        assert p in doc


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_length_is_between_ten_and_eighteen_minutes(mod):
    words = episode_lib.spoken_words(lines_of(mod))
    ceiling = getattr(mod, "MAX_WORDS", 2700)   # Brian may lift the ceiling for an episode whose material carries it
    assert 1500 <= words <= ceiling, f"{words} words is about {words / 150:.1f} minutes"


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_speakers_are_in_the_cast_and_cues_are_known(mod):
    cast = json.loads((ROOT / "audio" / "casts" / "not_by_sight.json").read_text(encoding="utf-8"))["characters"]
    cues = json.loads((ROOT / "audio" / "cues.json").read_text(encoding="utf-8"))["cues"]
    for ln in spoken(lines_of(mod)):
        m = LINE.match(ln)
        assert m.group(1) in cast, m.group(1)
        if m.group(2):
            assert m.group(2) in cues, m.group(2)


@pytest.mark.parametrize("mod", MODS, ids=lambda m: f"ep{m.NUMBER:02d}")
def test_scenes_keep_brians_rules(mod):
    text = " ".join(ln for ln in spoken(lines_of(mod)) if LINE.match(ln).group(1) in SCENE_SPEAKERS).lower()
    assert "count the steps" not in text and "counting steps" not in text
    assert "terrif" not in text
    for forbidden in ("nigeria", "70%", "seventy percent", "mike may"):
        assert forbidden not in " ".join(spoken(lines_of(mod))).lower()
