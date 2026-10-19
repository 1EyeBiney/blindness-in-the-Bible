"""Third audition: candidates for BOOKS, the voice that reads the old books in the Law series.

Run from the repository root:  python audio/build_audition3.py
Then, in audio/:  labs_pipe render scripts/audition3_01.txt
Each candidate reads the same two passages (Henry on Leviticus 19:14, and Josephus), so Brian compares like with
like. Stability is set as it will be for the role. Voices already cast in not_by_sight.json are left out.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (short name, voice_id, why it is here), from the synced account list, none already cast
CANDIDATES = [
    ("GEORGE", "JBFqnCBsd6RMkjVDRZzb", "British, warm storyteller; the bookish sound, distinct from Nathan and Bill"),
    ("ARTHUR", "C1npRmjB19a6yNkEucvx", "American audiobook narrator, clear and even"),
    ("JOHNDOE", "EiNlNiXeDU1pqqOPrYMO", "American, deep and slow; the old-book weight"),
    ("ERIC", "cjVigY5qzO86Huf0OWal", "American, smooth and plain; the lightest of the men"),
    ("MIHAI", "8WRfTpaUoqZSfTerOXzI", "Romanian-accented English, rich and warm; a voice from somewhere else"),
    ("ALICE", "Xb7hH8MSUJpSbSDYk0k2", "British woman, clear educator; the only way to make BOOKS unmistakable among three men"),
    ("LILY", "pFZP5JQG7iQjIQuC4Bku", "British woman, lower and softer than Alice"),
]

LINES = [
    ("calm", "The safety of the blind we must likewise be tender of, and not put a stumbling-block before them; for "
             "this is to add affliction to the afflicted, and to make God's providence a servant to our malice."),
    ("calm", "It is also a duty to show the roads to those who do not know them, and not to esteem it a matter for "
             "sport, when we hinder others' advantages, by setting them in a wrong way. In like manner, let no one "
             "revile a person blind or dumb."),
]


def main() -> None:
    script = ["@project: audition3", "@section: 1", "@cast: casts/audition3.json",
              "@defaults: takes=1 keep=pick model=eleven_v3", "@continuity: off", "",
              "# Third audition: candidates for BOOKS, each reading Henry and then Josephus."]
    cast = {"cast_name": "audition3",
            "defaults": {"model": "eleven_v3", "stability": 0.7, "similarity_boost": 0.75, "style": 0.0,
                         "speed": 1.0, "use_speaker_boost": True, "output_format": "mp3_44100_192", "takes": 1},
            "characters": {}}
    for short, vid, why in CANDIDATES:
        tag = f"BOOKS_{short}"
        script += ["", f"# {short}: {why}"]
        for cue, text in LINES:
            script.append(f"[{tag}] ({cue}) {text}")
        cast["characters"][tag] = {"name": f"Books candidate {short.title()}", "voice_id": vid,
                                   "description": f"Audition for the old-books reader. {why}."}
    out = ROOT / "audio"
    (out / "scripts" / "audition3_01.txt").write_text("\n".join(script) + "\n", encoding="utf-8", newline="\n")
    (out / "casts" / "audition3.json").write_text(json.dumps(cast, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"wrote audition3: {len(CANDIDATES)} candidates, {len(LINES)} lines each")


if __name__ == "__main__":
    main()
