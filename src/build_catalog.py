"""Build the catalog of every passage about blindness.

Two passes over the Berean Standard Bible:

1. WORD: every verse containing "blind" in any form (86 verses). Each one
   is classified by hand in WORD_VERSES below.
2. DESCRIBED: passages that are about blindness or lost sight but never
   use the word (Isaac, Eli, Samson, Saul on the Damascus road, and so on).
   These were found by searching for phrases such as "could not see",
   "eyes were dim", "put out his eyes", "received his sight", then chosen
   by hand. They are listed in DESCRIBED_VERSES.

The classification is a judgment made by a reader, not a fact about the
text. Brian reviews it; `confidence` marks the calls most open to dispute.

Run from the project folder:
    python src/build_catalog.py
Reads the official Berean Standard Bible text (data/raw/berean/bsb.txt, see
SOURCE.md beside it) and writes data/catalog.csv. The site builds from that
committed file.
"""
from __future__ import annotations

import csv
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BSB_PATH = Path(os.environ.get("BSB_PATH", ROOT / "data" / "raw" / "berean" / "bsb.txt"))
OUT = ROOT / "data" / "catalog.csv"

# kind: the broad group. sub: the narrower one. who: the person or group.
KINDS = {
    "physical": "Physical blindness: blind people, sight lost, sight restored",
    "legal": "Law: commands about blind people, blinding, and blind animals",
    "promise": "Promise: God opening the eyes of the blind (may be physical, figurative, or both)",
    "figurative": "Figurative: blindness as a picture of something else",
    "other": "The word appears but the verse is not about blindness",
}
SUBS = {
    "person": "A blind person or people in a narrative",
    "group": "Blind people named as a group",
    "healing": "Sight given or restored",
    "struck": "Sight taken: by God, by enemies, or by injury",
    "age": "Sight lost in old age",
    "god_makes": "God as maker of the sighted and the blind",
    "care": "Care shown to blind people",
    "protection": "Command protecting blind people",
    "injury": "Law about blinding someone",
    "priesthood": "Rule about priests",
    "sacrifice": "Rule about blind animals offered in sacrifice",
    "restoration": "Promise that the blind will see or be led",
    "leaders": "Blind guides, watchmen, leaders",
    "people_of_god": "God's own people called blind",
    "unbelief": "Blindness as unbelief or hardness of heart",
    "bribe": "A bribe blinds",
    "simile": "Acting like the blind (groping, stumbling)",
    "curse": "Blindness as a curse or judgment in an oracle",
    "grief": "Eyes failing from grief or waiting",
    "threat": "A threat to blind, not carried out",
    "blindfold": "Blindfolded",
    "possible": "Possibly about poor sight; uncertain",
}

# (id, kind, sub, who, confidence, note)
H, M, L = "high", "medium", "low"
WORD_VERSES = [
    ("genesis_19_11", "physical", "struck", "The men of Sodom", H, "Struck so they could not find the door."),
    ("exodus_4_11", "physical", "god_makes", "", H, "God to Moses: who makes the sighted or the blind? Is it not I, the LORD?"),
    ("exodus_21_26", "legal", "injury", "", H, "A servant blinded in one eye by his master goes free."),
    ("exodus_23_8", "figurative", "bribe", "", H, ""),
    ("leviticus_19_14", "legal", "protection", "", H, "Do not put a stumbling block before the blind."),
    ("leviticus_21_18", "legal", "priesthood", "", H, "A blind descendant of Aaron may not approach to offer; verse 22 says he may still eat the holy food."),
    ("leviticus_22_22", "legal", "sacrifice", "", H, "Blind animals are not to be offered."),
    ("deuteronomy_15_21", "legal", "sacrifice", "", H, "Blind animals are not to be offered."),
    ("deuteronomy_16_19", "figurative", "bribe", "", H, ""),
    ("deuteronomy_27_18", "legal", "protection", "", H, "Cursed is he who lets a blind man wander in the road."),
    ("deuteronomy_28_28", "figurative", "curse", "", M, "Listed between madness and confusion of mind; could be read as physical."),
    ("deuteronomy_28_29", "figurative", "simile", "", H, "Groping at noon like a blind man in the darkness."),
    ("2samuel_5_6", "physical", "group", "The blind and the lame of Jerusalem", M, "A taunt by the Jebusites. A hard passage; readings differ."),
    ("2samuel_5_8", "physical", "group", "The blind and the lame of Jerusalem", M, "David's reply and the saying that followed. A hard passage; readings differ."),
    ("2kings_6_18", "physical", "struck", "The Aramean raiders", H, "Struck at Elisha's prayer; sight returns in verse 20."),
    ("job_9_24", "other", "blindfold", "", H, "Blindfolds judges: a picture of injustice, not blindness."),
    ("job_29_15", "physical", "care", "Job", H, "I served as eyes to the blind."),
    ("psalm_146_8", "promise", "restoration", "", M, "The LORD opens the eyes of the blind; set among acts of care for the oppressed."),
    ("isaiah_29_9", "figurative", "people_of_god", "", H, ""),
    ("isaiah_29_18", "promise", "restoration", "", M, ""),
    ("isaiah_35_5", "promise", "restoration", "", M, "Quoted by Jesus's answer to John the Baptist (Matthew 11:5)."),
    ("isaiah_42_7", "promise", "restoration", "", M, "The servant's task: to open the eyes of the blind."),
    ("isaiah_42_16", "promise", "restoration", "", M, "I will lead the blind by a way they did not know."),
    ("isaiah_42_18", "figurative", "people_of_god", "", H, ""),
    ("isaiah_42_19", "figurative", "people_of_god", "", H, ""),
    ("isaiah_43_8", "figurative", "people_of_god", "", H, "Eyes but blind."),
    ("isaiah_56_10", "figurative", "leaders", "", H, "Israel's watchmen are blind."),
    ("isaiah_59_10", "figurative", "simile", "", H, "Like the blind we feel our way along the wall."),
    ("jeremiah_31_8", "physical", "group", "The blind and the lame among the returning exiles", H, "God gathers them home with everyone else."),
    ("lamentations_4_14", "figurative", "simile", "", M, "They wandered blind in the streets."),
    ("zephaniah_1_17", "figurative", "simile", "", H, "They will walk like the blind."),
    ("zechariah_11_17", "figurative", "curse", "The worthless shepherd", M, "An oracle: may his right eye be blinded."),
    ("zechariah_12_4", "figurative", "curse", "The horses of the nations", M, "An oracle of battle: horses struck with blindness."),
    ("malachi_1_8", "legal", "sacrifice", "", H, "Blind animals offered in contempt."),
    ("matthew_9_27", "physical", "healing", "Two blind men (Galilee)", H, ""),
    ("matthew_9_28", "physical", "healing", "Two blind men (Galilee)", H, ""),
    ("matthew_11_5", "physical", "healing", "Jesus's answer to John the Baptist", H, "The blind receive sight; echoes Isaiah 35:5."),
    ("matthew_12_22", "physical", "healing", "A blind and mute man", H, ""),
    ("matthew_15_14", "figurative", "leaders", "", H, "Blind guides."),
    ("matthew_15_30", "physical", "healing", "Crowds by the Sea of Galilee", H, ""),
    ("matthew_15_31", "physical", "healing", "Crowds by the Sea of Galilee", H, ""),
    ("matthew_20_30", "physical", "healing", "Two blind men near Jericho", H, ""),
    ("matthew_21_14", "physical", "healing", "The blind and the lame in the temple", H, "Compare 2 Samuel 5:8."),
    ("matthew_23_16", "figurative", "leaders", "", H, ""),
    ("matthew_23_17", "figurative", "leaders", "", H, ""),
    ("matthew_23_19", "figurative", "leaders", "", H, ""),
    ("matthew_23_24", "figurative", "leaders", "", H, ""),
    ("matthew_23_26", "figurative", "leaders", "", H, ""),
    ("mark_8_22", "physical", "healing", "The blind man at Bethsaida", H, ""),
    ("mark_8_23", "physical", "healing", "The blind man at Bethsaida", H, ""),
    ("mark_10_46", "physical", "healing", "Bartimaeus", H, ""),
    ("mark_10_49", "physical", "healing", "Bartimaeus", H, ""),
    ("mark_10_51", "physical", "healing", "Bartimaeus", H, ""),
    ("mark_14_65", "other", "blindfold", "", H, "Jesus blindfolded and struck."),
    ("luke_4_18", "promise", "restoration", "", M, "Jesus reads Isaiah in Nazareth: recovery of sight to the blind."),
    ("luke_6_39", "figurative", "leaders", "", H, "Can a blind man lead a blind man?"),
    ("luke_7_21", "physical", "healing", "Jesus's answer to John the Baptist", H, ""),
    ("luke_7_22", "physical", "healing", "Jesus's answer to John the Baptist", H, ""),
    ("luke_14_13", "physical", "care", "Guests at the banquet", H, "Invite the poor, the crippled, the lame and the blind."),
    ("luke_14_21", "physical", "care", "Guests at the banquet", H, "Parable of the great banquet."),
    ("luke_18_35", "physical", "healing", "The blind man near Jericho", H, "Luke's account of the Jericho healing."),
    ("luke_22_64", "other", "blindfold", "", H, "Jesus blindfolded and struck."),
    ("john_5_3", "physical", "group", "The sick at the pool of Bethesda", H, ""),
    ("john_9_1", "physical", "healing", "The man born blind", H, ""),
    ("john_9_2", "physical", "healing", "The man born blind", H, "Who sinned? Jesus answers in verse 3: neither."),
    ("john_9_13", "physical", "healing", "The man born blind", H, ""),
    ("john_9_17", "physical", "healing", "The man born blind", H, ""),
    ("john_9_18", "physical", "healing", "The man born blind", H, ""),
    ("john_9_19", "physical", "healing", "The man born blind", H, ""),
    ("john_9_20", "physical", "healing", "The man born blind", H, ""),
    ("john_9_24", "physical", "healing", "The man born blind", H, ""),
    ("john_9_25", "physical", "healing", "The man born blind", H, "I was blind, but now I see."),
    ("john_9_32", "physical", "healing", "The man born blind", H, ""),
    ("john_9_39", "figurative", "unbelief", "", M, "The chapter turns here from physical to spiritual sight."),
    ("john_9_40", "figurative", "unbelief", "", H, ""),
    ("john_9_41", "figurative", "unbelief", "", H, ""),
    ("john_10_21", "physical", "healing", "The man born blind", H, "Looking back on John 9."),
    ("john_11_37", "physical", "healing", "The man born blind", H, "Looking back on John 9."),
    ("john_12_40", "figurative", "unbelief", "", H, "Quoting Isaiah 6:10."),
    ("acts_13_11", "physical", "struck", "Elymas the sorcerer", H, "Blind for a time."),
    ("acts_22_11", "physical", "struck", "Paul (Saul)", H, "Paul retells the Damascus road."),
    ("romans_2_19", "figurative", "leaders", "", H, "A guide for the blind."),
    ("2corinthians_4_4", "figurative", "unbelief", "", H, ""),
    ("2peter_1_9", "figurative", "unbelief", "", H, "Nearsighted to the point of blindness."),
    ("1john_2_11", "figurative", "unbelief", "", H, ""),
    ("revelation_3_17", "figurative", "people_of_god", "The church in Laodicea", H, ""),
]

DESCRIBED_VERSES = [
    ("genesis_27_1", "physical", "age", "Isaac", H, "Eyes so weak he could no longer see."),
    ("genesis_29_17", "physical", "possible", "Leah", L, "Leah's eyes; the meaning of the Hebrew is disputed."),
    ("genesis_48_10", "physical", "age", "Jacob (Israel)", H, "Could hardly see, yet blesses Ephraim and Manasseh knowingly."),
    ("judges_16_21", "physical", "struck", "Samson", H, "Eyes gouged out by the Philistines."),
    ("judges_16_28", "physical", "struck", "Samson", H, "His last prayer mentions his two eyes."),
    ("1samuel_3_2", "physical", "age", "Eli", H, ""),
    ("1samuel_4_15", "physical", "age", "Eli", H, "Ninety-eight years old and could not see."),
    ("1samuel_11_2", "physical", "threat", "The men of Jabesh-gilead", H, "Nahash demands every right eye; Saul prevents it."),
    ("1kings_14_4", "physical", "age", "Ahijah the prophet", H, "Could not see, yet knows who is at the door (verses 5 and 6)."),
    ("2kings_6_20", "physical", "healing", "The Aramean raiders", H, "Their sight returns at Elisha's prayer."),
    ("2kings_25_7", "physical", "struck", "Zedekiah", H, "Eyes put out by the Babylonians."),
    ("jeremiah_39_7", "physical", "struck", "Zedekiah", H, ""),
    ("jeremiah_52_11", "physical", "struck", "Zedekiah", H, ""),
    ("deuteronomy_34_7", "physical", "age", "Moses", H, "The contrast: at 120 his eyes were not weak."),
    ("matthew_9_29", "physical", "healing", "Two blind men (Galilee)", H, ""),
    ("matthew_9_30", "physical", "healing", "Two blind men (Galilee)", H, ""),
    ("matthew_20_33", "physical", "healing", "Two blind men near Jericho", H, ""),
    ("matthew_20_34", "physical", "healing", "Two blind men near Jericho", H, ""),
    ("mark_8_24", "physical", "healing", "The blind man at Bethsaida", H, "Healed in two stages."),
    ("mark_8_25", "physical", "healing", "The blind man at Bethsaida", H, ""),
    ("mark_10_52", "physical", "healing", "Bartimaeus", H, "Your faith has healed you."),
    ("luke_18_41", "physical", "healing", "The blind man near Jericho", H, ""),
    ("luke_18_42", "physical", "healing", "The blind man near Jericho", H, ""),
    ("luke_18_43", "physical", "healing", "The blind man near Jericho", H, ""),
    ("john_9_3", "physical", "healing", "The man born blind", H, "Neither this man nor his parents sinned."),
    ("john_9_6", "physical", "healing", "The man born blind", H, ""),
    ("john_9_7", "physical", "healing", "The man born blind", H, ""),
    ("john_9_11", "physical", "healing", "The man born blind", H, ""),
    ("john_9_15", "physical", "healing", "The man born blind", H, ""),
    ("john_9_30", "physical", "healing", "The man born blind", H, ""),
    ("acts_9_8", "physical", "struck", "Paul (Saul)", H, "Could not see a thing; led by the hand."),
    ("acts_9_9", "physical", "struck", "Paul (Saul)", H, "Three days without sight."),
    ("acts_9_12", "physical", "healing", "Paul (Saul)", H, ""),
    ("acts_9_17", "physical", "healing", "Paul (Saul)", H, ""),
    ("acts_9_18", "physical", "healing", "Paul (Saul)", H, "Something like scales fell from his eyes."),
    ("acts_22_13", "physical", "healing", "Paul (Saul)", H, ""),
    ("galatians_4_15", "physical", "possible", "Paul", L, "You would have torn out your eyes and given them to me. Some read this as a sign of an eye condition."),
    ("galatians_6_11", "physical", "possible", "Paul", L, "See what large letters I use. Some read this as a sign of poor sight."),
    ("psalm_6_7", "figurative", "grief", "", M, "My eyes fail from grief."),
    ("psalm_38_10", "figurative", "grief", "", M, "The light of my eyes has faded."),
    ("psalm_88_9", "figurative", "grief", "", M, "My eyes grow dim with grief."),
    ("job_17_7", "figurative", "grief", "Job", M, "My eyes have grown dim with grief."),
    ("lamentations_5_17", "figurative", "grief", "", M, "Our eyes grow dim."),
    ("romans_11_8", "figurative", "unbelief", "", H, "Eyes that could not see."),
]


def load_bsb() -> list[dict]:
    """The official Berean Standard Bible text, one verse per line as
    "Book C:V<TAB>text", from bereanbible.com/bsb.txt (public domain).
    The words and punctuation are used exactly as published."""
    verses = []
    for line in BSB_PATH.read_text(encoding="utf-8-sig").split("\n"):
        m = re.match(r"^((?:[1-3] )?[A-Za-z ]+?) (\d+):(\d+)\t(.*)$", line.rstrip("\r"))
        if not m:
            continue
        book, ch, vs, text = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4).strip()
        verses.append({"id": f"{book.lower().replace(' ', '')}_{ch}_{vs}", "book_name": book, "chapter": ch,
                       "verse": vs, "text": text, "reference": f"{book} {ch}:{vs}",
                       "testament": "OT" if len({v["book_name"] for v in verses} | {book}) <= 39 else "NT"})
    return verses


def build() -> list[dict]:
    all_verses = load_bsb()
    verses = {v["id"]: v for v in all_verses}
    order = {vid: i for i, vid in enumerate(verses)}
    rows = []
    for found_by, items in (("word", WORD_VERSES), ("described", DESCRIBED_VERSES)):
        for vid, kind, sub, who, conf, note in items:
            v = verses[vid]
            assert kind in KINDS and sub in SUBS, (vid, kind, sub)
            rows.append({
                "order": order[vid], "id": vid, "reference": v["reference"], "testament": v["testament"],
                "book": v["book_name"], "chapter": v["chapter"], "verse": v["verse"],
                "found_by": found_by, "kind": kind, "sub": sub, "who": who, "confidence": conf,
                "note": note, "text": v["text"],
            })
    rows.sort(key=lambda r: r["order"])
    return rows


def word_search_ids() -> list[str]:
    return [v["id"] for v in load_bsb() if re.search(r"\bblind", v["text"], re.I)]


def main() -> None:
    rows = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    by_kind: dict[str, int] = {}
    for r in rows:
        by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + 1
    print(f"{len(rows)} verses -> {OUT}")
    print("by kind:", by_kind)
    print("by search:", {k: sum(r["found_by"] == k for r in rows) for k in ("word", "described")})


if __name__ == "__main__":
    main()
