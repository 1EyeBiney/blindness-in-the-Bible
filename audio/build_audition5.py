"""Fifth audition: the nine new sight-lost characters on Eleven v3 against Eleven v4, each on their own lines.

Run from the repository root:  python audio/build_audition5.py
Then, in audio/:  labs_pipe render scripts/audition5_v3_01.txt  and  labs_pipe render scripts/audition5_v4_01.txt
The voices are the ones Brian cast on 1 November 2026 (casts/not_by_sight.json). The lines are each character's
actual lines from episodes 12 to 16, with their cues, so the two models are compared on the words that will be
used. The established voices (Narrator, Reader, Brian, Henry, Books) stay on v3 and are not in this audition.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIO = ROOT / "audio"
SPEAKER = re.compile(r"^(?:> )?\*\*([A-Za-z ]+)\*\*\s*(?:\*\(([^)]*)\)\*)?\s*(.*)$")
ROLES = ["ISAAC", "JACOB", "ESAU", "ISRAEL", "JOSEPH", "ELI", "SAMUEL", "AHIJAH", "SAMSON"]
SCRIPTS = ["ep12_the_voice_and_the_hands_01.md", "ep13_i_know_my_son_01.md", "ep14_the_voice_in_the_night_01.md",
           "ep15_the_sound_of_her_feet_01.md", "ep16_between_the_pillars_01.md"]


def main() -> None:
    cast_all = json.loads((AUDIO / "casts/not_by_sight.json").read_text(encoding="utf-8"))
    lines: list[tuple[str, str, str, str]] = []  # tag, cue, text, episode
    for name in SCRIPTS:
        for ln in (AUDIO / "scripts" / name).read_text(encoding="utf-8").splitlines():
            m = SPEAKER.match(ln.strip())
            if not m:
                continue
            tag = m.group(1).strip().upper().replace(" ", "_")
            if tag in ROLES:
                lines.append((tag, (m.group(2) or "calm").strip(), m.group(3).strip(), name[:4]))
    for model in ("eleven_v3", "eleven_v4"):
        short = model.replace("eleven_", "")
        script = [f"@project: audition5_{short}", "@section: 1", f"@cast: casts/audition5_{short}.json",
                  f"@defaults: takes=1 keep=pick model={model}", "@continuity: off", "",
                  f"# Fifth audition: the new characters on {model}, each on their own lines."]
        cast = {"cast_name": f"audition5_{short}",
                "defaults": dict(cast_all["defaults"], model=model, takes=1), "characters": {}}
        for tag in ROLES:
            cast["characters"][tag] = dict(cast_all["characters"][tag])
            script.append("")
            script.append(f"# {tag}: {cast_all['characters'][tag]['_voice']}")
            for t, cue, text, ep in lines:
                if t == tag:
                    script.append(f"[{tag}] ({cue}) {text}")
        (AUDIO / "scripts" / f"audition5_{short}_01.txt").write_text("\n".join(script) + "\n", encoding="utf-8", newline="\n")
        (AUDIO / "casts" / f"audition5_{short}.json").write_text(json.dumps(cast, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    chars = sum(len(t) for _, _, t, _ in lines)
    print(f"wrote audition5 v3 and v4: {len(lines)} lines, about {chars:,} characters each")


if __name__ == "__main__":
    main()
