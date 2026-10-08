"""Shared pieces for every Not By Sight episode script.

Every episode module in audio/episodes/ defines:
    SLUG, NUMBER, TITLE, PASSAGES (list of (book, chapter, first, last) the READER reads, in order),
    DRAFT_BRIAN (list of paragraphs written in Brian's voice but not yet his; they render only after he approves),
    build(bible) -> list[str]  (labs_pipe lines)

Rules kept here, checked by tests/test_episodes.py:
- READER lines are the official Berean text, one verse per line, never retyped.
- Scene characters speak only after the narrator says "imagine".
- Each BRIAN line is either verbatim from the site (stories.py) or listed in DRAFT_BRIAN, so nothing is put in
  Brian's mouth that he has not seen.
- Length: 1,500 to 2,700 spoken words, about 10 to 18 minutes at 150 words a minute.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "audio"))
import build_site  # noqa: E402
from merge_runs import is_line, merge_runs, section_index  # noqa: E402

OUT_DIR = ROOT / "audio" / "scripts"
LINE = re.compile(r"^\[(\w+)\]\s*(?:\(([^)]*)\))?\s*(.*)$")

SERIES_INTRO = ("This is Not By Sight, a series on blindness in the Bible, made by a blind Christian for blind "
                "believers, their families, and the church. The Scripture you will hear is the Berean Standard Bible, "
                "read word for word. The thoughts marked as Brian's are Brian Clark's own. And when we imagine a "
                "scene, we will tell you so.")

BRIAN_VOICE_NOTE = ("A word about the voice you are about to hear. Brian decided he was too shy to record his own "
                    "thoughts. We suspect he was being a scaredy cat. So, against our better judgment, we let him pick "
                    "his own voice. Whenever you hear it, from here to the end, these are his words.")

CLOSE = ("This has been Not By Sight. The full story, with every source named, is at one eye biney dot github dot "
         "i o, slash blindness in the Bible. Scripture quotations are from the Holy Bible, Berean Standard Bible, "
         "which is in the public domain. The scenes you heard marked as imagined are our own. Everything else is "
         "from the text and the old books.")


def header(project: str, cast: str = "casts/not_by_sight.json") -> list[str]:
    return [f"@project: {project}", "@section: 1", f"@cast: {cast}",
            "@defaults: takes=1 keep=pick model=eleven_v3", "@continuity: off", ""]


def reader(bible: dict, book: str, ch: int, a: int, z: int, cue: str = "plainly", lead: str = "") -> list[str]:
    """Narrator announces the reference, then one READER line per verse, Scripture only."""
    ref = f"{book} chapter {ch}, verse{'s' if z > a else ''} {a}{f' to {z}' if z > a else ''}."
    out = [f"[NARRATOR] (calm) {lead}{ref}"]
    for v in range(a, z + 1):
        out.append(f"[READER] ({cue}) {bible[(book, ch, v)]}")
    return out


def spoken_words(lines: list[str]) -> int:
    return sum(len(LINE.match(ln).group(3).split()) for ln in lines if is_line(ln))


def to_markdown(lines: list[str], title: str, number: int) -> str:
    out = [f"# Not By Sight, episode {number}: {title}", "",
           "Script for reading. Speaker names in bold, cues in italics, Scripture indented.", ""]
    for ln in lines:
        if ln.startswith("@") or ln.startswith("#") or not ln.strip():
            continue
        if ln.startswith("[BREAK]"):
            out += ["---", ""]
            continue
        m = re.match(r"\[PAUSE ([\d.]+)\]", ln)
        if m:
            out += [f"*(pause {m.group(1)} s)*", ""]
            continue
        m = LINE.match(ln)
        who, cue, text = m.group(1), m.group(2), m.group(3)
        cue_s = f" *({cue})*" if cue else ""
        out.append(f"> **Reader**{cue_s} {text}" if who == "READER" else f"**{who.title()}**{cue_s} {text}")
        out.append("")
    return "\n".join(out)


def write_episode(mod) -> dict:
    """Write <slug>_01.txt/.md (line by line), <slug>_02.txt (speaker runs merged) and the section index."""
    bible = build_site.load_bible()
    lines = mod.build(bible)
    base = f"ep{mod.NUMBER:02d}_{mod.SLUG}"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"{base}_01.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    (OUT_DIR / f"{base}_01.md").write_text(to_markdown(lines, mod.TITLE, mod.NUMBER), encoding="utf-8", newline="\n")
    merged = merge_runs(lines, f"{base}_v2")
    (OUT_DIR / f"{base}_02.txt").write_text("\n".join(merged) + "\n", encoding="utf-8", newline="\n")
    (OUT_DIR / f"{base}_02_sections.md").write_text(
        f"# Episode {mod.NUMBER}: rendered sections\n\nOne row per rendered file.\n\n" + section_index(merged),
        encoding="utf-8", newline="\n")
    words = spoken_words(lines)
    return {"base": base, "lines": len(lines), "sections": sum(1 for ln in merged if is_line(ln)),
            "words": words, "minutes": round(words / 150, 1)}
