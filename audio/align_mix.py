"""Find where each rendered section sits inside Brian's Reaper mix, by cross-correlation.

Run from audio/:  python align_mix.py <project> <mix.wav> [script.txt]
  e.g. python align_mix.py ep02_bartimaeus_v2 renders/ep02_bartimaeus_v2/section_1/ep02_bartimaeus_v2.wav
Writes deliver/<project>/timing.csv: id, speaker, start_sec, end_sec, confidence, first words.

Why: the mix adds music and effects and may shift timing, so labs_pipe's markers.csv no longer applies.
Aligning the original per-section files against the mix recovers the timing without any export from Reaper.
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

SR = 8000  # alignment is done on a mono 8 kHz downmix; plenty for speech onsets


def load_mono(path: Path) -> np.ndarray:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.float32).astype(np.float64)
    return x / (np.abs(x).max() or 1.0)


def find(section: np.ndarray, mix: np.ndarray, lo: int, hi: int) -> tuple[int, float]:
    """Best offset of `section` within mix[lo:hi]; returns (offset_samples, peak-to-median ratio)."""
    win = mix[lo:hi]
    if len(win) < len(section):
        return lo, 0.0
    probe = section[: min(len(section), SR * 12)]           # the first 12 seconds carry the onset
    corr = fftconvolve(win, probe[::-1], mode="valid")
    k = int(np.argmax(corr))
    conf = float(corr[k] / (np.median(np.abs(corr)) + 1e-9))
    return lo + k, conf


def main(project: str, mix_path: str) -> None:
    root = Path(__file__).resolve().parent
    sel = root / "selected" / project / "section_1"
    files = sorted(p for p in sel.glob("*.mp3"))
    texts = {}
    script = root / "scripts" / (sys.argv[3] if len(sys.argv) > 3 else
                                 ("man_born_blind_02.txt" if project == "man_born_blind_v2" else project.replace("_v2", "_02") + ".txt"))
    n = 0
    for ln in script.read_text(encoding="utf-8").splitlines():
        if ln.startswith("[") and not ln.startswith(("[BREAK]", "[PAUSE")):
            n += 1
            m = re.match(r"^\[(\w+)\]\s*(?:\(([^)]*)\))?\s*(.*)$", ln)
            texts[f"{n:03d}"] = (m.group(1), m.group(3))
    mix = load_mono(Path(mix_path))
    rows = []
    cursor = 0
    for f in files:
        sid = f.name.split("_")[0]
        sec = load_mono(f)
        lo = max(0, cursor - SR * 5)
        hi = min(len(mix), cursor + len(sec) + SR * 90)   # sections stay in order; allow up to 90 s of inserted material
        off, conf = find(sec, mix, lo, hi)
        start, end = off / SR, (off + len(sec)) / SR
        who, text = texts.get(sid, (f.stem.split("_", 1)[1].upper(), ""))
        rows.append([sid, who, f"{start:.2f}", f"{end:.2f}", f"{conf:.1f}", " ".join(text.split()[:8])])
        cursor = off + len(sec)
    out = root / "deliver" / project / "timing.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "speaker", "start_sec", "end_sec", "confidence", "first_words"])
        w.writerows(rows)
    low = [r for r in rows if float(r[4]) < 8]
    print(f"wrote {out} ({len(rows)} sections); mix length {len(mix) / SR:.1f}s; "
          f"first section starts at {rows[0][2]}s; {len(low)} low-confidence matches")
    for r in low:
        print("  check:", r[0], r[1], r[2], r[5])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
