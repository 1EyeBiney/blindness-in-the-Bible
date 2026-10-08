"""Write every episode script in audio/episodes/ to audio/scripts/, and the drafts file for Brian's review.

Run from the repository root:  python audio/build_episodes.py
"""
from __future__ import annotations

import importlib
import pkgutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import episode_lib  # noqa: E402
import episodes  # noqa: E402


def modules():
    out = []
    for info in sorted(pkgutil.iter_modules(episodes.__path__), key=lambda i: i.name):
        if info.name.startswith("ep"):
            out.append(importlib.import_module(f"episodes.{info.name}"))
    return sorted(out, key=lambda m: m.NUMBER)


def write_drafts(mods) -> Path:
    """Everything written in Brian's voice that he has not yet approved, in one file for him to read."""
    lines = ["# Drafts in Brian's voice, awaiting his approval", "",
             "Each paragraph below is in the scripts as a BRIAN line but was written by Claude from what Brian has "
             "said in conversation. Nothing renders in his voice until he approves, edits or strikes each one. "
             "Mark changes in this file or in the script; the generator is the source of truth.", ""]
    for m in mods:
        lines += [f"## Episode {m.NUMBER}: {m.TITLE}", ""]
        for i, p in enumerate(m.DRAFT_BRIAN, 1):
            lines += [f"{i}. {p}", ""]
    out = HERE.parent / "docs" / "BRIAN_DRAFTS.md"
    out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return out


def main() -> None:
    mods = modules()
    for m in mods:
        info = episode_lib.write_episode(m)
        print(f"ep{m.NUMBER:02d} {m.TITLE:32} {info['lines']:3} lines, {info['sections']:2} sections, "
              f"{info['words']:4} words, about {info['minutes']} min")
    print("drafts ->", write_drafts(mods))


if __name__ == "__main__":
    main()
