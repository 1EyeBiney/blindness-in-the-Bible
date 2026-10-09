"""Second audition: candidates for the five new scene roles in episodes 2 to 6.

Run from the repository root:  python audio/build_audition2.py
Then, in audio/:  labs_pipe render scripts/audition2_01.txt ; labs_pipe review audition2/1
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "audio"))

# role -> [(short name, voice_id)], from the synced account list, none already cast
CANDIDATES = {
    "BARTIMAEUS": [("WILL", "bIHbv24MWmeRgasZH58o"), ("JERRY", "XA2bIQ92TabjGbpO2xRr"),
                   ("CHARLIE", "IKne3meq5aSn9XLyUdCD"), ("ERIC", "cjVigY5qzO86Huf0OWal")],
    "VOICE": [("RIVER", "SAz9YHcvj6GT2YYXdXww"), ("JUNIPER", "aMSt68OGf4xUZAnLpTU8"),
              ("SARAH", "EXAVITQu4vr4xnSDxMaL")],
    "FRIEND": [("ROGER", "CwhRBWXzGAHq8TQ4Fs17"), ("ARTHUR", "C1npRmjB19a6yNkEucvx"),
               ("HECTOR", "dgkKQcJqyy5AP0dqleUU")],
    "JOHN": [("GEORGE", "JBFqnCBsd6RMkjVDRZzb"), ("JOHNDOE", "EiNlNiXeDU1pqqOPrYMO"),
             ("ADAM", "pNInz6obpgDQGcFmaJgB"), ("DANIEL", "onwK4e9ZLuTAKqWW03F9")],
    "DISCIPLE": [("RUSS", "HKFOb9iktHA85uKXydRT"), ("JERRY2", "XA2bIQ92TabjGbpO2xRr"),
                 ("ARTHUR2", "C1npRmjB19a6yNkEucvx")],
}

LINES = {
    "BARTIMAEUS": ("excited", "Friend. You, with the basket, I can hear it creak. What is this? Who is passing? "
                               "Jesus. Son of David. Son of David, have mercy on me!"),
    "VOICE": ("calm", "Take courage. Get up. He is calling you. Here, your hand, this way."),
    "FRIEND": ("calm", "Nearly there. I am going to sit you down right in front of him. Then I will step back. I am "
                       "not going anywhere. I did not carry you up a mountain to lose you at the top."),
    "JOHN": ("calm", "Well? Did you ask him? And what did he say? Say it."),
    "DISCIPLE": ("calm", "Then he turned to us and said, go back and tell John what you have seen and heard. The "
                         "blind see. The lame walk. And then he said one more thing, and I think it was for you."),
}


def main() -> None:
    script = ["@project: audition2", "@section: 1", "@cast: casts/audition2.json",
              "@defaults: takes=1 keep=pick model=eleven_v3", "@continuity: off", "",
              "# Second audition: each candidate reads one line of its intended role."]
    cast = {"cast_name": "audition2",
            "defaults": {"model": "eleven_v3", "stability": 0.55, "similarity_boost": 0.75, "style": 0.0,
                         "speed": 1.0, "use_speaker_boost": True, "output_format": "mp3_44100_192", "takes": 1},
            "characters": {}}
    for role, cands in CANDIDATES.items():
        cue, text = LINES[role]
        script += ["", f"# {role}"]
        for short, vid in cands:
            tag = f"{role}_{short}"
            script.append(f"[{tag}] ({cue}) {text}")
            cast["characters"][tag] = {"name": f"{role.title()} candidate {short.title()}", "voice_id": vid,
                                       "description": f"Audition for the {role.lower()} role."}
    out = ROOT / "audio"
    (out / "scripts" / "audition2_01.txt").write_text("\n".join(script) + "\n", encoding="utf-8", newline="\n")
    (out / "casts" / "audition2.json").write_text(json.dumps(cast, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote audition2: {sum(len(c) for c in CANDIDATES.values())} candidates across {len(CANDIDATES)} roles")


if __name__ == "__main__":
    main()
