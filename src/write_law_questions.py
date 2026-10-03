"""Editorial pass over data/reference/law_questions_candidates.json: Brian's
two law questions (is the Bible the first text about the blind, and how
Hammurabi dates against Moses; and what a blind priest would have touched).

    python src/write_law_questions.py   -> data/reference/law_questions.json
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data" / "reference" / "law_questions_candidates.json"
OUT = ROOT / "data" / "reference" / "law_questions.json"

ISBE = "International Standard Bible Encyclopedia (1915)"
SMITH = "Smith's Bible Dictionary (1884 edition)"
EASTON = "Easton's Bible Dictionary (1897)"
ED = "Edersheim, The Life and Times of Jesus the Messiah (1883)"
HENRY = "Matthew Henry, Commentary on the Whole Bible (1706-1721)"
JOS = "Josephus, Antiquities of the Jews (Whiston translation)"
HAM = "The Code of Hammurabi, translated by C. H. W. Johns (1903)"
HARPERS = "Harper's Songs"
BUDGE = "E. A. Wallis Budge, The Teaching of Amen-em-apt, Son of Kanekht (1924)"


def item(text, source, *frm, caution=None):
    d = {"text": text, "source": source, "from": [list(f) for f in frm]}
    if caution:
        d["caution"] = caution
    return d


def wiki(title, date):
    return f"Wikipedia, \"{title},\" revision of {date} (CC BY-SA 4.0)"


FINAL = {
    "stumbling-block": [
        item("Brian asked how Hammurabi dates against Moses. Hammurabi reigned about 1792 to 1750 BC. For the Exodus "
             "there are two main views: an early date around 1490 BC, which the shelf's older books give from 1 Kings "
             "6:1, and a late date in the thirteenth century BC. Many scholars also hold that Deuteronomy was written "
             "down in the seventh century and most of Leviticus later still, against the tradition that Moses wrote "
             "both. On any of these figures Hammurabi comes first: by about three centuries on the early date, five "
             "on the late one, and more than a thousand years if Leviticus is dated late. The 1915 encyclopedia put "
             "Hammurabi three centuries earlier than today's figure, so older books on the shelf place him earlier "
             "still.",
             f"{wiki('Hammurabi', '2 October 2026')}; {EASTON}, entry \"Exodus\"; {wiki('The Exodus', '2026')}; "
             f"{wiki('Documentary hypothesis', '2026')}; {ISBE}, entry \"Hammurabi.\"",
             ("dating", 0), ("dating", 1), ("dating", 2),
             caution="Ancient dates are conventions and the Exodus date is disputed; the arithmetic is ours."),
        item("Is the Bible the first text to address the blind? No. Earlier law codes deal with eyes, but as injuries "
             "to be priced or punished. Ur-Nammu, about 2100 BC and the oldest code known, sets half a mina of silver "
             "for knocking out a man's eye. Hammurabi prices an eye by the victim's rank, uses the tearing out of an "
             "eye as a punishment for an ungrateful adopted son, and sets surgeons' fees and penalties for eye "
             "operations. The Middle Assyrian laws, from the centuries around the Exodus, include blinding as a "
             "penalty. None of these names the blind as people to be protected.",
             f"{wiki('Code of Ur-Nammu', '8 September 2026')}; {HAM}, sections 193, 196 to 199 and 215 to 220; "
             f"{wiki('Assyrian law', '15 December 2025')}.",
             ("earlier-texts-blinding", 3), ("earlier-texts-blinding", 1), ("earlier-texts-blinding", 0), ("earlier-texts-blinding", 4)),
        item("One earlier text does show regard. The Egyptian Instruction of Amenemope, dated between about 1300 and "
             "1075 BC, says in Budge's 1924 translation: \"Make not a laughing-stock of the blind man,\" alongside "
             "\"vex not the dwarf\" and a warning not to frustrate the plans of a lame man. That is roughly contemporary "
             "with the late date of the Exodus, and older than any late dating of Leviticus. So the honest finding is "
             "this: Israel's Law was not the first text to protect the blind, but Leviticus 19:14 and Deuteronomy "
             "27:18 are the only laws on the shelf that name the blind for protection rather than price their eyes. "
             "Amenemope is wisdom advice to a son; the Law is a command to a nation, with God as witness.",
             f"{BUDGE}, lines 478 to 480 and introduction; {wiki('Instruction of Amenemope', '20 May 2026')}; {HENRY}, on Leviticus 19.",
             ("earlier-texts-regard", 0), ("earlier-texts-regard", 1), ("earlier-texts-regard", 6), ("earlier-texts-regard", 8)),
        item("Egypt also shows blind people at work. Tomb paintings from the Middle Kingdom, before 1640 BC, show blind "
             "harpists, and an eighteenth-dynasty mural of the fifteenth century BC shows another. Levy in 1872 "
             "described a painting of a blind harper attended by seven blind singers keeping time with their hands, "
             "\"evidently professional musicians.\" These show a role blind people held, which is a different thing from "
             "a law protecting them, and the shelf has nothing on how Egypt or Babylon treated a blind beggar.",
             f"{wiki(HARPERS, '1 June 2026')}; {wiki('Blind musicians', '28 June 2026')}; W. H. Levy, Blindness and the Blind (1872).",
             ("earlier-texts-regard", 2), ("earlier-texts-regard", 3)),
    ],
    "priest": [
        item("Brian asked what a priest actually did with his hands. Most of it. Smith's lists the duties: keep the altar "
             "fire burning day and night, feed the lamp with oil, offer the morning and evening sacrifices, teach the "
             "law, and judge hard cases. Leviticus 1 has the priests catch and sprinkle the blood, flay and cut up the "
             "animal, lay the wood in order and set the pieces on the fire. Every morning a priest in linen took up the "
             "ashes from the altar and carried them out. The lamps were trimmed with golden snuffers. These are tasks of "
             "touch and heat, done around an open fire and sharp tools.",
             f"{SMITH}, entry \"Priest\"; {HENRY}, on Leviticus 1 and 6; {EASTON}, entry \"Candlestick.\"",
             ("priest-duties", 0), ("priest-duties", 1), ("priest-duties", 2), ("priest-duties", 3)),
        item("Other duties needed eyes. Leviticus 13 has the priest \"look on\" a skin disease again and again and judge "
             "whether it is deeper than the skin. Burning the incense meant standing alone in the Holy Place and, as "
             "Edersheim describes Zechariah's turn in Luke 1, waiting \"until he saw the incense kindling.\" The "
             "blessing and the teaching, on the other hand, were spoken, and Henry calls lifting hands to bless the "
             "people \"one part of the priest's work\" that a blind man could do as well as any.",
             f"{HENRY}, on Leviticus 9 and 13 and Numbers 6; {ED}, Book II, chapter IV; {EASTON}, entry \"Incense.\"",
             ("priest-duties", 7), ("priest-duties", 4), ("priest-duties", 6)),
        item("On touching holy things, the rules in the text are for the Levites, not the priests. When the camp moved, "
             "Aaron's sons covered the ark and the vessels first; only then could the Kohathites carry them, \"but they "
             "shall not touch any holy thing, lest they die,\" nor go in to watch the covering. Uzzah died for grabbing "
             "the ark; Nadab and Abihu for offering fire God had not commanded, not for touching. Priests themselves "
             "handled the holy things constantly, after washing hands and feet at the laver. So Brian's question has an "
             "edge the sources did not see: a priest's whole work was touching what Levites were forbidden to touch.",
             f"{HENRY}, on Numbers 4 and 18, 2 Samuel 6 and Leviticus 10; {ISBE}, entry \"Priests and Levites\"; "
             f"{SMITH}, entry \"Priest\"; {EASTON}, entry \"Laver.\"",
             ("touching-holy-things", 0), ("touching-holy-things", 1), ("touching-holy-things", 3), ("touching-holy-things", 4), ("touching-holy-things", 5)),
        item("Leviticus 21 keeps the blemished priest from exactly the two places where the fire and the touching were: "
             "\"he shall not go in unto the veil, nor come nigh unto the altar.\" The reason the text gives is that the "
             "sanctuary not be profaned. No source on the shelf says anything about accidental touching by a man who "
             "cannot see; that the rule happened to keep him clear of the hazards is our observation, not theirs. The "
             "one accommodation on record is the skin-disease rule reported by Henry: a blemished priest could still "
             "examine, with a helper's eyes, unless the blemish was in his own eye.",
             f"{HENRY}, on Leviticus 13 and 21.", ("touching-holy-things", 7), ("blemished-priest-provision", 4),
             caution="The link between the rule and the hazards is our inference."),
        item("Would one blind priest have burdened the rest? The numbers suggest not. The priests served in twenty-four "
             "courses, each on duty one week in turn, with the lot deciding order rather than who served; Zechariah, "
             "a man of at least sixty, had never before drawn the incense. Edersheim reckons about fifty priests on "
             "duty each weekday; Smith's reports Jewish writers claiming many thousands at Jerusalem and Jericho. In a "
             "body that size, a priest who ate at the table but did not serve at the altar cost his brothers little. "
             "The Mishnah adds that a bodily blemish barred a priest but not a Levite; for Levites only age counted, "
             "and only for carrying.",
             f"{EASTON} and {SMITH}, entries \"Priest\"; {HENRY}, on 1 Chronicles 24 and Luke 1; {ED}, Book II, chapter I; "
             f"{wiki('Emor', '14 May 2026')}.",
             ("priestly-numbers", 0), ("priestly-numbers", 3), ("priestly-numbers", 4), ("priestly-numbers", 5), ("blemished-priest-provision", 5),
             caution="The headcounts are ancient claims the sources themselves distrust."),
        item("Later rabbis argued about the blind priest and the blessing. One ruled that a priest blind in one eye "
             "should not lift his hands to bless; the Talmud adds that if the townspeople were used to him, he was "
             "allowed. The stated worry was that people would stare. It is a small window onto the real question, "
             "which was never the man's ability but the congregation's eyes.",
             f"{wiki('Emor', '14 May 2026')}, reporting the Talmud.", ("blemished-priest-provision", 6),
             caution="Rabbinic discussion centuries after Leviticus."),
    ],
}


def main() -> None:
    cands = json.loads(CANDIDATES.read_text(encoding="utf-8"))
    for slug, items in FINAL.items():
        for it in items:
            for key, idx in it["from"]:
                assert key in cands and idx < len(cands[key]), (slug, key, idx)
    OUT.write_text(json.dumps(FINAL, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{sum(len(v) for v in FINAL.values())} items for {len(FINAL)} pages -> {OUT}")


if __name__ == "__main__":
    main()
