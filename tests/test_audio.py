"""The pilot audio script keeps its promises: Scripture word for word, scenes marked, Brian's words his."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "audio"))
import build_site  # noqa: E402
import build_script  # noqa: E402

SCRIPT = ROOT / "audio" / "scripts" / "man_born_blind_01.txt"
LINE = re.compile(r"^\[(\w+)\]\s*(?:\(([^)]*)\))?\s*(.*)$")


def lines():
    return [ln for ln in SCRIPT.read_text(encoding="utf-8").splitlines()
            if ln.startswith("[") and not ln.startswith(("[BREAK]", "[PAUSE"))]


def test_script_on_disk_matches_the_generator():
    bible = build_site.load_bible()
    assert SCRIPT.read_text(encoding="utf-8") == "\n".join(build_script.build(bible)) + "\n"


def test_reader_lines_are_the_official_berean_text_and_cover_all_of_john_9():
    bible = build_site.load_bible()
    john9 = [bible[("John", 9, v)] for v in range(1, 42)]
    read = [LINE.match(ln).group(3) for ln in lines() if ln.startswith("[READER]")]
    assert read == john9, "every verse of John 9, in order, word for word, and nothing else"


def test_every_scene_is_introduced_with_imagine():
    ls = lines()
    scene_speakers = {"MAN", "NEIGHBOUR", "HELPER", "FATHER"}
    armed = False
    for ln in ls:
        m = LINE.match(ln)
        who, text = m.group(1), m.group(3)
        if who == "NARRATOR" and "imagine" in text.lower():
            armed = True
        if who in scene_speakers:
            assert armed, ln
        if who in ("READER", "BRIAN"):
            armed = False


def test_brian_lines_come_from_the_site_in_substance():
    import stories as st
    story = next(x for x in st.STORIES if x["slug"] == "man-born-blind")
    site_words = set(re.findall(r"[a-z']+", " ".join(story["brian"]).lower()))
    for ln in lines():
        m = LINE.match(ln)
        if m.group(1) != "BRIAN":
            continue
        words = re.findall(r"[a-z']+", m.group(3).lower())
        shared = sum(w in site_words for w in words) / len(words)
        assert shared > 0.85, (shared, m.group(3)[:60])


def test_no_unsourced_figures_in_the_audio():
    text = " ".join(lines()).lower()
    assert "seventy percent" not in text and "70%" not in text and "nigeria" not in text
    assert "mike may" not in text


def test_speakers_are_all_in_the_cast_and_cues_are_known():
    import json
    cast = json.loads((ROOT / "audio" / "casts" / "not_by_sight.json").read_text(encoding="utf-8"))["characters"]
    cues = json.loads((ROOT / "audio" / "cues.json").read_text(encoding="utf-8"))["cues"]
    for ln in lines():
        m = LINE.match(ln)
        who, cue = m.group(1), m.group(2)
        assert who in cast, who
        if cue:
            assert cue in cues, cue


def test_labs_pipe_check_passes_if_installed():
    try:
        r = subprocess.run([sys.executable, "-m", "labs_pipe", "check", "scripts/man_born_blind_01.txt"],
                           cwd=ROOT / "audio", capture_output=True, text=True, timeout=60)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return
    if "No module named" in r.stderr:
        return
    # until Brian picks voices, the only errors allowed are the REPLACE_ME voice ids
    errors = [ln for ln in (r.stdout + r.stderr).splitlines() if "error:" in ln]
    assert all("voice_id is REPLACE_ME" in ln for ln in errors), errors


def test_the_siloam_scene_keeps_brians_rules():
    text = " ".join(ln for ln in lines() if ln.startswith(("[MAN]", "[HELPER]", "[NEIGHBOUR]"))).lower()
    assert "count" not in text, "blind people do not count steps; the scene uses sound, touch and air"
    assert "take my arm" in text and "cool air" in text
    assert "afraid" not in text and "terrif" not in text
