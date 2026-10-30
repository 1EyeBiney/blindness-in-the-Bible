"""Turn a hand-written reading script (the _01.md file) into the labs_pipe render files.

Episodes 2 to 10 were generated from Python modules in audio/episodes/. From episode 11 on, the reading file is
the source: Brian edits it directly, so the words there are the words that render. This script reads it and
writes <base>_01.txt (line by line), <base>_02.txt (speaker runs merged, the one to render) and the section
index, exactly as episode_lib.write_episode does.

Run from the repository root:  python audio/md_to_script.py audio/scripts/ep11_the_last_thing_he_saw_01.md

Mapping:
  **Narrator** *(cue)* text      -> [NARRATOR] (cue) text        (any bold speaker; Reader lines are quoted)
  > **Reader** *(cue)* text      -> [READER] (cue) text
  *(pause 1.5 s)*                -> [PAUSE 1.5]
  ---                            -> [BREAK]
  *(SFX ...)*                    -> # SFX ...   (a comment; it ends a speaker run so the cue falls between takes)
Lines before the first speaker (title, notes) become header comments. Not a spoken word is changed; the check at
the end compares the words of every spoken line.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from merge_runs import is_line, merge_runs, section_index  # noqa: E402
from episode_lib import header, spoken_words  # noqa: E402

SPEAKER = re.compile(r"^(?:> )?\*\*([A-Za-z ]+)\*\*\s*(?:\*\(([^)]*)\)\*)?\s*(.*)$")
PAUSE = re.compile(r"^\*\(pause ([\d.]+) s\)\*$")
SFX = re.compile(r"^\*\((SFX[^)]*)\)\*$")


def convert(md: str) -> tuple[list[str], list[str]]:
    lines: list[str] = []
    notes: list[str] = []
    started = False
    for raw in md.splitlines():
        ln = raw.strip()
        if not ln:
            continue
        if ln == "---":
            lines.append("[BREAK]")
            continue
        m = PAUSE.match(ln)
        if m:
            lines.append(f"[PAUSE {m.group(1)}]")
            continue
        m = SFX.match(ln)
        if m:
            lines.append(f"# {m.group(1)}")
            continue
        m = SPEAKER.match(ln)
        if m:
            started = True
            who = m.group(1).strip().upper().replace(" ", "_")
            cue = m.group(2)
            text = m.group(3).strip()
            lines.append(f"[{who}] ({cue}) {text}" if cue else f"[{who}] {text}")
            continue
        if not started:
            notes.append(ln.lstrip("# ").strip())
            continue
        raise SystemExit(f"md_to_script: line not understood: {ln[:80]}")
    return lines, notes


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    md_path = Path(sys.argv[1]).resolve()
    base = md_path.name[:-len("_01.md")]
    md = md_path.read_text(encoding="utf-8")
    body, notes = convert(md)
    head = header(base) + [f"# {n}" for n in notes] + [""]
    lines = head + body
    out = md_path.parent
    (out / f"{base}_01.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    merged = merge_runs(lines, f"{base}_v2")
    (out / f"{base}_02.txt").write_text("\n".join(merged) + "\n", encoding="utf-8", newline="\n")
    (out / f"{base}_02_sections.md").write_text(
        f"# {base}: rendered sections\n\nOne row per rendered file.\n\n" + section_index(merged),
        encoding="utf-8", newline="\n")
    # the words of the spoken lines must be the words of the reading file
    md_words = " ".join(SPEAKER.match(l.strip()).group(3) for l in md.splitlines() if SPEAKER.match(l.strip())).split()
    txt_words = " ".join(re.match(r"^\[\w+\]\s*(?:\([^)]*\))?\s*(.*)$", l).group(1) for l in lines if is_line(l)).split()
    merged_words = " ".join(re.match(r"^\[\w+\]\s*(?:\([^)]*\))?\s*(.*)$", l).group(1) for l in merged if is_line(l)).split()
    assert md_words == txt_words == merged_words, "words differ between the reading file and the render files"
    w = spoken_words(lines)
    print(f"{base}: {sum(1 for l in lines if is_line(l))} lines, {sum(1 for l in merged if is_line(l))} merged sections, "
          f"{w} spoken words, about {w / 150:.0f} minutes before pauses and sound")


if __name__ == "__main__":
    main()
