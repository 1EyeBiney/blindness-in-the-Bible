"""Join consecutive lines of the same speaker into one rendered section.

Brian, 7 October 2026: within one speaker's section the voice changed from line to line, as if different
speakers were alternating sentences. So each speaker's run renders as one request, and the voice holds steady
within it. Markers ([BREAK], [PAUSE]) end a run. The first line's cue is kept. Runs longer than MAX_CHARS are
split at line boundaries. Not a word changes; tests/test_audio.py checks that.
"""
from __future__ import annotations

import re

MAX_CHARS = 2800   # the v3 model takes about 3,000 characters per request
LINE = re.compile(r"^\[(\w+)\]\s*(?:\(([^)]*)\))?\s*(.*)$")


def is_marker(ln: str) -> bool:
    return ln.startswith(("[BREAK]", "[PAUSE"))


def is_line(ln: str) -> bool:
    return ln.startswith("[") and not is_marker(ln)


def merge_runs(lines: list[str], project: str) -> list[str]:
    out: list[str] = []
    run: list[tuple[str, str | None, str]] = []

    def emit(who: str, cue: str | None, texts: list[str]) -> None:
        body = " ".join(texts)
        out.append(f"[{who}] ({cue}) {body}" if cue else f"[{who}] {body}")

    def flush() -> None:
        nonlocal run
        if not run:
            return
        who, cue = run[0][0], run[0][1]
        chunk: list[str] = []
        for _, _, text in run:
            if chunk and len(" ".join(chunk)) + len(text) + 1 > MAX_CHARS:
                emit(who, cue, chunk)
                chunk = []
            chunk.append(text)
        emit(who, cue, chunk)
        run = []

    for ln in lines:
        if ln.startswith("@project:"):
            out.append(f"@project: {project}")
            continue
        if not is_line(ln):
            flush()
            out.append(ln)
            continue
        m = LINE.match(ln)
        who, cue, text = m.group(1), m.group(2), m.group(3)
        if run and run[0][0] != who:
            flush()
        run.append((who, cue, text))
    flush()
    return out


def section_index(lines: list[str]) -> str:
    """One row per rendered file: id (labs_pipe's numbering), speaker, word count, first words."""
    rows = ["id | speaker | words | first words", "-- | -- | -- | --"]
    n = 0
    for ln in lines:
        if is_line(ln):
            n += 1
            m = LINE.match(ln)
            words = m.group(3).split()
            rows.append(f"{n:03d} | {m.group(1)} | {len(words)} | {' '.join(words[:9])} ...")
    return "\n".join(rows) + "\n"
