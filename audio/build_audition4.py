"""Fourth audition: one big list of voices for the sight-lost series (episodes 12 to 16).

Run from the repository root:  python audio/build_audition4.py
Then, in audio/:  labs_pipe render scripts/audition4_01.txt
Every voice reads the same two lines, Isaac's question (Genesis 27:21) and Eli's instruction (1 Samuel 3:9),
one gentle and one plain, so Brian compares tone and cadence like with like. Brian asked for voices that do not
sound young and American: older men from the account, plus six accented voices added from the ElevenLabs library
on 1 November 2026 (Middle Eastern, Turkish, Greek). Roles to fill: Isaac, young Jacob, Esau, old Jacob, Joseph,
Eli, Samuel (a boy), Ahijah, Samson.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (short name, voice_id, why it is here)
CANDIDATES = [
    ("GEORG", "LRpNiUBlcqgIsKUzcrlN", "German grandfather over ninety; the oldest voice on the account"),
    ("ANCIENT", "QPRY8gLO0Aik2vBYPfHe", "Bill the Ancient One, elderly absent-minded professor, kindly"),
    ("ERSAN", "jSLgazTuNHl5kcEiiHgd", "old Turkish teacher, warm; from the library"),
    ("MEKAWY", "uEs4hyGRdNLLJMFsxCkz", "calm Middle Eastern storyteller; from the library"),
    ("ALI", "JUSQMx5M1jCmDyepTElG", "Levantine Arabic accent, warm and authoritative; from the library"),
    ("SHREIF", "C5DUoxdM3kV00iwaR3sK", "deep and calm, Arabic accent; from the library"),
    ("NAFEES", "puDRtQWF8NtQiPMJygTb", "light Arabic accent, warm middle-aged; from the library"),
    ("PANOS", "z3zYFzY2KtTTLjvOecBO", "Greek, measured, mid-to-low; from the library"),
    ("DAVID", "5uEJotkO1FzLxXhXsgIv", "Turkish-labelled eastern voice, rich; already on the account"),
    ("BOBBY", "piOEaKYYZhntpHad74n2", "thick Eastern European, Romanian and Bulgarian; already on the account"),
    ("VLASOV", "txnCCHHGKmYIwrn7HfHQ", "Russian, rich and calm; already on the account"),
    ("SPURGEON", "fx8RiSGwEISGAZiVD71O", "mature British preacher's cadence, fifties"),
    ("JAMES", "JbFfo12yyR6B9R6hoMPM", "North-eastern English, bass, close to the ear"),
    ("FRED", "shtKeQ7Y43f4mGRm3LvL", "weathered, mildly grumpy man in his late fifties"),
    ("LYLE", "gVGjWWK84EKBTe4qMEgk", "medium-low, flat and dry, slow and deliberate"),
]

def verse(ref: str) -> str:
    for line in (ROOT / "data/raw/berean/bsb.txt").read_text(encoding="utf-8-sig").splitlines():
        if line.startswith(ref + "\t"):
            return line.split("\t", 1)[1].strip()
    raise SystemExit(f"verse not found: {ref}")

LINES = [
    ("calm", verse("Genesis 27:21")),
    ("calm", verse("1 Samuel 3:9")),
]


def main() -> None:
    script = ["@project: audition4", "@section: 1", "@cast: casts/audition4.json",
              "@defaults: takes=1 keep=pick model=eleven_v3", "@continuity: off", "",
              "# Fourth audition: fifteen voices for the sight-lost series, each reading Genesis 27:21 and 1 Samuel 3:9."]
    cast = {"cast_name": "audition4",
            "defaults": {"model": "eleven_v3", "stability": 0.7, "similarity_boost": 0.75, "style": 0.0,
                         "speed": 1.0, "use_speaker_boost": True, "output_format": "mp3_44100_192", "takes": 1},
            "characters": {}}
    for short, vid, why in CANDIDATES:
        tag = f"V_{short}"
        script += ["", f"# {short}: {why}"]
        for cue, text in LINES:
            script.append(f"[{tag}] ({cue}) {text}")
        cast["characters"][tag] = {"name": f"Candidate {short.title()}", "voice_id": vid,
                                   "description": f"Audition for the sight-lost series. {why}."}
    out = ROOT / "audio"
    (out / "scripts" / "audition4_01.txt").write_text("\n".join(script) + "\n", encoding="utf-8", newline="\n")
    (out / "casts" / "audition4.json").write_text(json.dumps(cast, indent=2) + "\n", encoding="utf-8", newline="\n")
    chars = sum(len(t) for _, t in LINES) * len(CANDIDATES)
    print(f"wrote audition4: {len(CANDIDATES)} candidates, {len(LINES)} lines each, about {chars:,} characters")


if __name__ == "__main__":
    main()
