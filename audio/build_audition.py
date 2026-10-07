"""Write a short audition script: each candidate voice reads one line of its intended role.

Run from the repository root:  python audio/build_audition.py
Then, in audio/:  labs_pipe render scripts/audition_01.txt --dry-run   (and without --dry-run to hear them)
                  labs_pipe review audition/1

Each candidate is its own cast character (labs_pipe maps one voice per character), named ROLE_NAME so the
reviewer announces the role and the voice together. Voice IDs come from the synced account list.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import build_site  # noqa: E402

# role -> [(short name, voice_id)], all from casts/elevenlabs-voices.json on Brian's account
CANDIDATES = {
    "NARRATOR": [("RUSS", "HKFOb9iktHA85uKXydRT"), ("NATHAN", "lWDDHwXsJXJM7nv2YgHY"),
                 ("ARTHUR", "C1npRmjB19a6yNkEucvx"), ("GEORGE", "JBFqnCBsd6RMkjVDRZzb"),
                 ("HOPE", "iCrDUkL56s3C8sCRl7wb")],
    "READER": [("BILL", "pqHfZKP75CvOlQylNhV4"), ("DANIEL", "onwK4e9ZLuTAKqWW03F9"),
               ("ERIC", "cjVigY5qzO86Huf0OWal"), ("ALICE", "Xb7hH8MSUJpSbSDYk0k2")],
    "BRIAN": [("CHRIS", "iP95p4xoKVk53GoZ742B"), ("ROGER", "CwhRBWXzGAHq8TQ4Fs17"),
              ("BRIANEL", "nPczCjzI2devNBz1zQrb"), ("JOHNDOE", "EiNlNiXeDU1pqqOPrYMO")],
    "MAN": [("WILL", "bIHbv24MWmeRgasZH58o"), ("JERRY", "XA2bIQ92TabjGbpO2xRr"),
            ("LIAM", "TX3LPaxmHKxFdv7VOQHJ")],
    "NEIGHBOUR": [("JUNIPER", "aMSt68OGf4xUZAnLpTU8"), ("RIVER", "SAz9YHcvj6GT2YYXdXww"),
                  ("MATILDA", "XrExE9yKIg1WjnnlVkGX")],
    "HELPER": [("HECTOR", "dgkKQcJqyy5AP0dqleUU"), ("CALLUM", "N2lVS1w4EtoT3dr4eOWO"),
               ("ADAM", "pNInz6obpgDQGcFmaJgB")],
}


def lines(bible: dict) -> dict[str, tuple[str, str]]:
    """role -> (cue, text): the audition line for that role, taken from the pilot script."""
    return {
        "NARRATOR": ("calm", "A man is walking downhill through Jerusalem with mud on his eyes. He cannot see. He has "
                             "never seen. A stranger he will not recognise, because he has never seen a face, has just "
                             "told him to go and wash in a pool at the bottom of the city. He goes."),
        "READER": ("plainly", bible[("John", 9, 3)]),
        "BRIAN": ("calm", "One of my first true walk-by-faith moments came during rehabilitation training at the Hines "
                          "VA hospital outside Chicago. At the end of training I did a drop-off test. It was terrifying, "
                          "exhilarating and liberating all at once."),
        "MAN": ("calm", "I know the way I got here. People have told me all my life that my eyes were a punishment, mine "
                        "or my parents'. He said no. He said it was so God could do something in me."),
        "NEIGHBOUR": ("curious", "Down? With the whole city coming up for the Sabbath? Do you know the way, and the steps "
                                 "at the bottom?"),
        "HELPER": ("calm", "I am going down to wash before I go up. Take my arm. The street steps down in a little "
                           "while, and I will tell you when."),
    }


def main() -> None:
    bible = build_site.load_bible()
    L = lines(bible)
    script = ["@project: audition", "@section: 1", "@cast: casts/audition.json",
              "@defaults: takes=1 keep=pick model=eleven_v3", "@continuity: off", "",
              "# Audition: each candidate voice reads one line of its intended role. Cheap by design."]
    cast = {"cast_name": "audition",
            "defaults": {"model": "eleven_v3", "stability": 0.6, "similarity_boost": 0.75, "style": 0.0,
                         "speed": 1.0, "use_speaker_boost": True, "output_format": "mp3_44100_192", "takes": 1},
            "characters": {}}
    for role, cands in CANDIDATES.items():
        cue, text = L[role]
        script.append("")
        script.append(f"# {role}")
        for short, vid in cands:
            tag = f"{role}_{short}"
            script.append(f"[{tag}] ({cue}) {text}")
            cast["characters"][tag] = {"name": f"{role.title()} candidate {short.title()}", "voice_id": vid,
                                       "description": f"Audition for the {role.lower()} role.",
                                       **({"stability": 0.8, "speed": 0.95} if role == "READER" else {})}
    out = ROOT / "audio"
    (out / "scripts" / "audition_01.txt").write_text("\n".join(script) + "\n", encoding="utf-8", newline="\n")
    (out / "casts" / "audition.json").write_text(json.dumps(cast, indent=2) + "\n", encoding="utf-8", newline="\n")
    n = sum(len(c) for c in CANDIDATES.values())
    print(f"wrote audition: {n} candidate voices across {len(CANDIDATES)} roles")


if __name__ == "__main__":
    main()
