"""Find when each sentence of a rendered section starts, from the pauses in its own audio.

A rendered section is one clean voice file (no music), so the pauses between sentences can be detected. The
sentences of the script are then laid over those pauses: a small dynamic programme picks which pauses are the
sentence breaks, preferring long pauses and sentence lengths that fit the speaker's average pace. That gives caption
and picture timings that follow the voice, where spreading words evenly over the section could drift by ten seconds
in a long passage.

Returns None when the audio and the text cannot be reconciled; callers then fall back to spreading by word share.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

SENT = re.compile(r"(?<=[.!?”\"’])\s+(?=[A-Z“\"‘])")


def sentences(text: str) -> list[str]:
    return [s for s in SENT.split(text.strip()) if s]


def _silences(audio: Path) -> tuple[list[tuple[float, float]], float]:
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(audio), "-af", "silencedetect=noise=-36dB:d=0.12",
                        "-f", "null", "-"], capture_output=True, text=True)
    log = r.stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", log)
    total = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else (ends[-1] if ends else 0.0)
    return list(zip(starts, ends)), total


def sentence_starts(audio: Path, text: str) -> list[tuple[str, float]] | None:
    """[(sentence, start seconds from the beginning of the file)], or None if it cannot be worked out."""
    sents = sentences(text)
    if not audio.exists() or not sents:
        return None
    gaps, total = _silences(audio)
    lead = 0.0
    if gaps and gaps[0][0] < 0.08:            # leading silence
        lead = gaps[0][1]
        gaps = gaps[1:]
    tail = total
    if gaps and gaps[-1][1] > total - 0.08:   # trailing silence
        tail = gaps[-1][0]
        gaps = gaps[:-1]
    if len(sents) == 1:
        return [(sents[0], lead)]
    need = len(sents) - 1
    if len(gaps) < need or tail <= lead:
        return None
    chars = [max(4, len(s)) for s in sents]
    rate = (tail - lead - sum(e - s for s, e in gaps) * 0.5) / sum(chars)     # seconds of speech per character
    m = len(gaps)
    INF = float("inf")

    def cost(i: int, t0: float, t1: float) -> float:
        want = chars[i] * rate
        return (t1 - t0 - want) ** 2 / (want + 0.6)

    # dp[i][j]: best cost with sentence i+1 beginning after gap j (sentence breaks 0..i placed)
    dp = [[INF] * m for _ in range(need)]
    back = [[-1] * m for _ in range(need)]
    for j in range(m):
        if j <= m - need:
            dp[0][j] = cost(0, lead, gaps[j][0]) - 2.5 * (gaps[j][1] - gaps[j][0])
    for i in range(1, need):
        for j in range(i, m - (need - 1 - i)):
            best, arg = INF, -1
            for k in range(i - 1, j):
                if dp[i - 1][k] == INF:
                    continue
                c = dp[i - 1][k] + cost(i, gaps[k][1], gaps[j][0])
                if c < best:
                    best, arg = c, k
            if arg >= 0:
                dp[i][j] = best - 2.5 * (gaps[j][1] - gaps[j][0])
                back[i][j] = arg
    best, arg = INF, -1
    for j in range(need - 1, m):
        if dp[need - 1][j] == INF:
            continue
        c = dp[need - 1][j] + cost(need, gaps[j][1], tail)
        if c < best:
            best, arg = c, j
    if arg < 0:
        return None
    picks = [arg]
    for i in range(need - 1, 0, -1):
        picks.append(back[i][picks[-1]])
    picks.reverse()
    starts = [lead] + [gaps[j][1] for j in picks]
    # sanity: no sentence of any length may run at under 40% or over 250% of the average pace
    ends = [gaps[j][0] for j in picks] + [tail]
    for c, a, b in zip(chars, starts, ends):
        if c >= 30 and not (0.4 * c * rate <= b - a <= 2.5 * c * rate):
            return None
    return list(zip(sents, starts))


if __name__ == "__main__":
    import sys
    res = sentence_starts(Path(sys.argv[1]), Path(sys.argv[2]).read_text(encoding="utf-8") if len(sys.argv) > 2 else "")
    print(res)
