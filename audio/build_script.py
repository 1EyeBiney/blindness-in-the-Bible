"""Write the pilot audio script for "The man born blind" in labs_pipe format.

Run from the repository root:  python audio/build_script.py
Output: audio/scripts/man_born_blind_01.txt (labs_pipe script) and audio/scripts/man_born_blind_01.md
(the same words laid out for reading).

Rules this file keeps:
- Every READER line is the official Berean Standard Bible text, pulled from data/raw/berean/bsb.txt at build
  time, never retyped. The test in tests/test_audio.py checks it word for word.
- Every dramatized scene is introduced by the narrator with the word "imagine", so no listener mistakes
  drama for Scripture.
- BRIAN lines are Brian's own words from the site, in his voice, read by an ElevenLabs voice he picks (his
  decision, 7 October 2026). The narrator's introduction to that voice is one separate line, so it and the BRIAN
  lines can be swapped for his own recordings later without touching anything else.
- Facts about the place and the time are the ones on the story page, with their sources named in the narration.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
import build_site  # noqa: E402

OUT_DIR = ROOT / "audio" / "scripts"


def verses(bible: dict, book: str, ch: int, a: int, z: int) -> list[tuple[int, str]]:
    return [(v, bible[(book, ch, v)]) for v in range(a, z + 1)]


def reader(bible: dict, book: str, ch: int, a: int, z: int, cue: str = "plainly", lead: str = "") -> list[str]:
    """One READER line per verse, Scripture only, verse number spoken by the narrator beforehand."""
    out = [f"[NARRATOR] (calm) {lead}{book} chapter {ch}, verse{'s' if z > a else ''} {a}{f' to {z}' if z > a else ''}."]
    for v, text in verses(bible, book, ch, a, z):
        out.append(f"[READER] ({cue}) {text}")
    return out


def build(bible: dict) -> list[str]:
    L: list[str] = []
    add = L.append
    ext = L.extend

    add("@project: man_born_blind")
    add("@section: 1")
    add("@cast: casts/not_by_sight.json")
    add("@defaults: takes=1 keep=pick model=eleven_v3")
    add("@continuity: off")
    add("")
    add("# Not By Sight, episode 1: The man born blind (John 9). Pilot script.")
    add("# NARRATOR carries the story and the background. READER speaks Scripture only, word for word from the")
    add("# Berean Standard Bible. BRIAN is Brian Clark's words in a voice he picks. MAN, NEIGHBOUR and HELPER")
    add("# appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    # ---- Cold open ------------------------------------------------------------------------------
    add("[NARRATOR] (calm) A man is walking downhill through Jerusalem with mud on his eyes.")
    add("[NARRATOR] (beat) He cannot see. He has never seen. And yet a complete stranger has just given him shocking "
        "news about his blindness, and told him to go and wash in a pool at the bottom of the city.")
    add("[NARRATOR] (calm) And. He goes.")
    add("[PAUSE 1.5]")
    add("[NARRATOR] (calm) This is Not By Sight, a series on blindness in the Bible, made by a blind Christian for "
        "blind believers, their families, and the church. I am the narrator. The Scripture you will hear is the "
        "Berean Standard Bible, read word for word. The thoughts marked as Brian's are Brian Clark's own. "
        "And when we imagine a scene, we will tell you so.")
    add("[BREAK]")

    # ---- What led up to it ----------------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Jesus is in Jerusalem. The Feast of Tabernacles has just ended, "
        "and at the close of the previous chapter the crowd in the Temple picked up stones to throw at Him. "
        "He slipped away. Now, walking on, He sees a man who has been blind from birth, sitting and begging. "
        "It is the Sabbath.")
    ext(reader(bible, "John", 9, 1, 5))
    add("[NARRATOR] (calm) Notice who speaks first. Not the blind man. The disciples, about him, in front of him, "
        "as a question in theology. Alfred Edersheim, writing in 1883, says this was a common question in that "
        "day: rabbis meeting such a person would ask by what sin the affliction had come, and many believed the "
        "faults of parents showed in their children. Jesus cuts across both ideas with one sentence.")
    add("[NARRATOR] (dryly) A word about the voice you are about to hear. Brian decided he was too shy to record "
        "his own thoughts. We suspect he was being a scaredy cat. So, against our better judgment, we let him pick "
        "his own voice. Whenever you hear it, from here to the end, these are his words.")
    add("[PAUSE 1.0]")
    add("[BRIAN] (calm) This one makes me cry because of what Jesus first says. Neither this man nor his parents "
        "sinned, but this happened so that the works of God would be displayed in him. That is what I pray for "
        "daily: that God uses my blindness for His glory in the things I do, the things I say, and the way I treat "
        "others, especially those who need help the most and who have, according to many, absolutely nothing to "
        "give back.")
    add("[BREAK]")

    # ---- The healing and the walk ---------------------------------------------------------------
    ext(reader(bible, "John", 9, 6, 7))
    add("[NARRATOR] (calm) Saliva and mud. Edersheim notes that saliva was commonly thought to help diseases of "
        "the eye, and that making clay and anointing on the Sabbath were among the things the religious teachers "
        "counted as work. Hold on to that. It is why the day matters so much in the argument to come.")
    add("[NARRATOR] (calm) And the pool. Siloam lies at the south end of Jerusalem, the lowest point of the "
        "ancient city. Josephus, who knew the city before it fell, called it a fountain with sweet water in great "
        "plenty. Its water came from the Gihon spring through a tunnel King Hezekiah cut so that a besieging army "
        "could not reach the spring. The pool itself was lost for nineteen centuries, until 2004, when workers "
        "repairing a sewer uncovered stone steps. Archaeologists found a large stone-lined basin with steps on at "
        "least three sides, built in sets of five with landings between.")
    add("[NARRATOR] (calm) How far did he walk? From the Temple Mount down to the pool is about six hundred "
        "metres in a straight line, and more than a hundred metres downhill, through a valley Josephus describes "
        "with steep slopes on either side. Excavators have found a stepped street running down that valley to the "
        "pool. And at the end, a staircase down to the water.")
    add("[NARRATOR] (calm) Scripture does not tell us how he felt on that walk, or whether anyone helped him. "
        "It tells us he had just heard, for the first time in his life, a teacher say that his blindness was not "
        "a punishment. So we imagine a man who had been given a reason to hope. This is a scene, not Scripture.")
    add("[PAUSE 1.0]")
    add("[MAN] (whisper) Mud. Cool and wet and heavy on my eyes. His thumbs pressed it in. Go to Siloam, he said. "
        "Wash.")
    add("[MAN] (calm) I have sat at the top of this road all my life. I know it by the slope under my feet, by the "
        "street narrowing, by the bread ovens on the left and the sound of a side street opening on the right. "
        "I have never been to the bottom.")
    add("[NEIGHBOUR] (curious) Friend, your face. Where are you going like that, against all these people?")
    add("[MAN] (excited) Down to Siloam, to wash. A man put this on my eyes. They call him Jesus.")
    add("[NEIGHBOUR] (curious) Down? With the whole city coming up for the Sabbath? Do you know the way, and the "
        "steps at the bottom?")
    add("[MAN] (calm) I know the way I got here. People have told me all my life that my eyes were a punishment, "
        "mine or my parents'. He said no. He said it was so God could do something in me. I do not know what. "
        "But I am going to find out, and I am going to go the way he said.")
    add("[HELPER] (calm) I am going down to wash before I go up. Take my arm. The street steps down in a little "
        "while, and I will tell you when.")
    add("[MAN] (excited) Thank you. Thank you.")
    add("[PAUSE 1.0]")
    add("[MAN] (whisper) His arm is steady. The crowd parts around us, voices going up, ours going down. The "
        "paving changes under my sandals, smooth stone, then a step down. Another. The wall on my right gives "
        "way to open air. Somewhere below, water being poured.")
    add("[MAN] (whisper) And the air. Cool air rising up the street to meet us, wet, with the smell of stone that "
        "is always in shadow. I have felt that at the Temple when the water was carried up. Now I am walking into "
        "it.")
    add("[HELPER] (calm) Stairs here. The landing is wide. Then more stairs, and the water.")
    add("[MAN] (after a long pause) My foot finds the edge of the stone. The water is cold on my hands. I kneel "
        "beside him, and I wash.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) What happened next, Scripture gives in three words. He came back seeing.")
    add("[BRIAN] (calm) One of my first true walk-by-faith moments came during rehabilitation training at the Hines "
        "VA hospital outside Chicago. At the end of training I did a drop-off test. I was let out of a car in a "
        "suburban business district with the task of finding a grocery store about five blocks away, on my own. "
        "Unless I got into serious physical danger, I was not to be helped. I had to trust my new skills to make "
        "that trip without any sight. It was terrifying, exhilarating and liberating all at once. I think of the man "
        "born blind making his way to the Pool of Siloam, not using a fancy iPhone while using the latest in cane "
        "technology, but by faith.")
    add("[BREAK]")

    # ---- The neighbours -------------------------------------------------------------------------
    ext(reader(bible, "John", 9, 8, 12, lead="But it never goes easy, does it? "))
    add("[BRIAN] (calm) He was blind from birth and had never had sight. From a physiological standpoint his visual "
        "cortex would never have developed. It takes a child about six years of seeing to learn to tell faces "
        "apart. He washed the mud off and received sight. Jesus did not only heal the eyes. He must have given the "
        "man a way to process what his eyes were now sending to his brain.")
    add("[BREAK]")

    # ---- The Pharisees, round one ---------------------------------------------------------------
    ext(reader(bible, "John", 9, 13, 17))
    add("[BRIAN] (dryly) The Pharisees went straight to whether the healing was lawful, not whether it had "
        "happened.")
    add("[NARRATOR] (calm) Then they send for his parents.")
    ext(reader(bible, "John", 9, 18, 23))
    add("[BREAK]")

    # ---- The Pharisees, round two ---------------------------------------------------------------
    ext(reader(bible, "John", 9, 24, 34))
    add("[BRIAN] (calm) The way he argues with the Pharisees is simply amazing. He would never have had access to "
        "Scripture or learning, and yet with a plain explanation he cuts through the arguments of the experts, in "
        "Jerusalem, and wins. That he would even speak back to a Pharisee is remarkable. His parents were obviously "
        "terrified.")
    add("[NARRATOR] (calm) A word on begging, since this man had begged all his life. Edersheim says blind beggars "
        "were a familiar sight at the Temple entrance, that the blind were held to be specially entitled to "
        "charity, and that a common plea was, gain merit by me.")
    add("[BRIAN] (calm) How humbling, to call out in effect: I have so little to offer you that your kindness to me "
        "will gain you righteousness.")
    add("[BREAK]")

    # ---- Jesus finds him ------------------------------------------------------------------------
    add("[NARRATOR] (calm) They throw him out. And then the one sentence that holds the whole chapter.")
    ext(reader(bible, "John", 9, 35, 38))
    add("[NARRATOR] (calm) He had heard that voice once before, over the mud. He had never seen the face. Now he "
        "sees it.")
    add("[BRIAN] (calm) It is hard to express what that man must have felt when he finally recognised Jesus, after "
        "Jesus sought him out. I am so grateful to Jesus for what He did for that one blind man. Some day, I will see "
        "again, and I can't wait for my moment of seeing Jesus for the first time too.")
    ext(reader(bible, "John", 9, 39, 41))
    add("[NARRATOR] (calm) Notice where the word blind lands at the end of the chapter. Not on the man who was "
        "born blind. On the men who could see.")
    add("[BREAK]")

    # ---- Close ----------------------------------------------------------------------------------
    add("[NARRATOR] (calm) This has been Not By Sight. The full story, with every source named, is at "
        "one eye biney dot github dot i o, slash blindness in the Bible. Scripture quotations are from the Holy "
        "Bible, Berean Standard Bible, which is in the public domain. The scenes you heard marked as imagined are "
        "our own. Everything else is from the text and the old books.")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L


def to_markdown(lines: list[str]) -> str:
    out = ["# Not By Sight, episode 1: The man born blind", "",
           "Pilot script for reading. Speaker names in bold, cues in italics, Scripture indented.", ""]
    for ln in lines:
        if ln.startswith("@") or ln.startswith("#") or not ln.strip():
            continue
        if ln.startswith("[BREAK]"):
            out.append("---"); out.append(""); continue
        m = re.match(r"\[PAUSE ([\d.]+)\]", ln)
        if m:
            out.append(f"*(pause {m.group(1)} s)*"); out.append(""); continue
        m = re.match(r"\[(\w+)\]\s*(\(([^)]*)\))?\s*(.*)", ln)
        who, cue, text = m.group(1), m.group(3), m.group(4)
        cue_s = f" *({cue})*" if cue else ""
        if who == "READER":
            out.append(f"> **Reader**{cue_s} {text}")
        else:
            out.append(f"**{who.title()}**{cue_s} {text}")
        out.append("")
    return "\n".join(out)


def main() -> None:
    bible = build_site.load_bible()
    lines = build(bible)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "man_born_blind_01.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    (OUT_DIR / "man_born_blind_01.md").write_text(to_markdown(lines), encoding="utf-8", newline="\n")
    words = sum(len(re.sub(r"^\[\w+\]\s*(\([^)]*\))?", "", ln).split())
                for ln in lines if ln.startswith("[") and not ln.startswith(("[BREAK", "[PAUSE")))
    print(f"wrote {len(lines)} lines, about {words} spoken words, roughly {words / 150:.0f} minutes at 150 wpm")


if __name__ == "__main__":
    main()
