"""Editorial pass over data/reference/picture_candidates.json for the seven
"Blindness as a picture" pages. Same pattern as the other write_* files.

    python src/write_picture.py   -> data/reference/picture.json
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "data" / "reference" / "picture_candidates.json"
OUT = ROOT / "data" / "reference" / "picture.json"

ISBE = "International Standard Bible Encyclopedia (1915)"
EASTON = "Easton's Bible Dictionary (1897)"
ED = "Edersheim, The Life and Times of Jesus the Messiah (1883)"
HENRY = "Matthew Henry, Commentary on the Whole Bible (1706-1721)"


def item(text, source, *frm, caution=None):
    d = {"text": text, "source": source, "from": [list(f) for f in frm]}
    if caution:
        d["caution"] = caution
    return d


FINAL = {
    "blind-guides": [
        item("The commentators read \"blind guides\" as a picture of knowledge and pride, never of eyesight. Henry: the "
             "Pharisees were blind leaders because they did not understand the spiritual meaning of the law and were "
             "proud enough to lead anyway; had they owned their blindness and come to Christ for eye-salve, they might "
             "have seen. Edersheim calls the woe of Matthew 23:16 a rebuke of \"moral blindness.\"",
             f"{HENRY}, on Matthew 15 and Luke 6; {ED}, Book V, chapter IV.", ("blind-guides", 0), ("blind-guides", 1)),
        item("The setting of the woes, by Edersheim's reckoning, is the third day of the last week, \"the last day in "
             "the Temple,\" after the Sadducees' question and the great commandment. He and Henry both count eight woes "
             "set against the eight Beatitudes, though Edersheim doubts verse 14 belongs to the original text.",
             f"{ED}, Book V, chapter IV; {HENRY}, on Matthew 23.", ("blind-guides", 5)),
        item("Two of the figures rest on real practice. The oath: Henry explains that the teachers held an oath by the "
             "Temple did not bind, while an oath by the Temple's gold did, and he suspected the rule was meant to bring "
             "gold to the treasury. The gnat and the camel: Easton notes that wine was carefully strained because the "
             "law counted insects unclean, and Edersheim ties the saying to tithing extended even to garden herbs.",
             f"{HENRY}, on Matthew 23; {EASTON}, entries \"Gnat\" and \"Camel\"; {ED}, Book V, chapter IV.",
             ("blind-guides", 1), ("blind-guides", 3),
             caution="Henry states the oath rule without a source; Edersheim finds the allusion hard to pin down."),
        item("The quarrel behind Matthew 15 was hand-washing. Edersheim says it was openly admitted to be a tradition of "
             "the elders and not a law of Moses, and adds a detail that lands differently on this site: some rabbis "
             "defended washing after meals on health grounds, because something left on the hands might injure the eyes.",
             f"{HENRY}, on Matthew 15; {ED}, Book III, chapter XXXI.", ("blind-guides", 4)),
        item("Isaiah's watchmen, Henry says, should have been watchmen of the flock, posted to see the beasts coming; "
             "he allows that the phrase may mean the false prophets and priests of Isaiah's day, the wicked princes, "
             "or, in Jesus's time, the chief priests and scribes, and he ties it to Matthew 15:14. The 1915 "
             "encyclopedia gives the plain office: a watchman was a sentinel on the city wall. Paul's \"guide for the "
             "blind,\" Henry notes, was the boast the teachers made of themselves; Paul is quoting their self-image back.",
             f"{HENRY}, on Isaiah 56 and Romans 2; {ISBE}, entry \"Watchman.\"", ("blind-guides", 6), ("blind-guides", 2)),
        item("Henry himself supplies the counterexample to the figure. Of Ahijah of Shiloh, blind with age, he writes "
             "that the prophet was \"still blest with the visions of the Almighty, which need not bodily eyes, but are "
             "rather favoured by the want of them.\" A commentator who read \"blind guides\" as a charge of pride "
             "knew perfectly well that a blind man could see what the sighted missed.",
             f"{HENRY}, on 1 Kings 14.", ("blind-guides", 7)),
    ],
    "eyes-that-cannot-see": [
        item("Edersheim, on John 9:41, draws the line this page turns on: the Pharisees' blindness \"was not the "
             "calamity of blindness\" but a blindness in which they were guilty. He also places the whole chapter at the "
             "Temple entrance, where beggars sat, and records that the blind were regarded as specially entitled to "
             "charity. Henry calls verse 39 \"a metaphor borrowed from the miracle\" just performed.",
             f"{ED}, Book IV, chapter IX; {HENRY}, on John 9.", ("eyes-that-cannot-see", 2), ("eyes-that-cannot-see", 0)),
        item("On \"if you were blind you would have no sin,\" Henry gives two readings: real ignorance would have "
             "lessened their guilt, or, had they known they were blind, they would have accepted Christ as guide. His "
             "conclusion is a sentence for this whole section: \"those are most blind who will not see.\"",
             f"{HENRY}, on John 9.", ("eyes-that-cannot-see", 1)),
        item("The hard verse is John 12:39, \"they could not believe.\" Henry, with Chrysostom and Augustine, reads "
             "\"could not\" as \"would not,\" while allowing that God's hand confirms a blindness people have chosen. "
             "Edersheim says the same: it was not decreed beforehand regardless of conduct, but came after a long "
             "history of resistance. On Romans 11 Henry adds that they \"had the faculties\" but not the use of them: "
             "\"the same sun softens wax and hardens clay.\"",
             f"{HENRY}, on John 12 and Romans 11; {ED}, Book V, chapter III.", ("eyes-that-cannot-see", 3), ("eyes-that-cannot-see", 4),
             caution="Theology, not a statement about anyone's eyes; handled as such by both writers."),
        item("For the letters, the commentators are brief and consistent. Paul's \"god of this age has blinded the "
             "minds\" is the understanding darkened by ignorance, error and prejudice. John's hater who \"does not know "
             "where he is going\" has a mind in the dark. Peter's man \"nearsighted to the point of blindness\" sees "
             "this world and dotes on it with no sense of the next; \"blind, that is,\" Henry writes, \"as to spiritual "
             "and heavenly things.\" The 1915 encyclopedia notices the grammar: the Bible tends to use the verb, to "
             "blind, for the figure, and the noun and adjective for the condition.",
             f"{HENRY}, on 2 Corinthians 4, 1 John 2 and 2 Peter 1; {ISBE}, entry \"Blindness.\"",
             ("eyes-that-cannot-see", 5), ("eyes-that-cannot-see", 6)),
        item("Henry set the two kinds side by side on Matthew 9:27, where two blind men call Jesus Son of David while "
             "the leaders refuse to: \"They who, by the providence of God, are deprived of bodily sight, may yet, by "
             "the grace of God, have the eyes of their understanding so enlightened\" as to see great things. Of the "
             "man in John 9 asking who the Son of God is, he says the chief comfort of eyesight is its usefulness to "
             "faith. The second remark assumes what a blind reader may not grant; the first is the point.",
             f"{HENRY}, on Matthew 9 and John 9.", ("eyes-that-cannot-see", 7),
             caution="Henry's phrase 'deprived of bodily sight' is his; his remark that the healed man might have gone back to blindness is not reproduced."),
    ],
    "gods-people-called-blind": [
        item("Isaiah 29, in Henry's reading: the prophets, rulers and seers were themselves blindfolded, and the "
             "prophecy had become to them \"as the words of a book that is sealed up,\" known to be a vision but with "
             "nothing of its contents known, like a sealed letter in a scholar's hands. He adds the line that joins this "
             "page to the one before it: \"it is easy to tell what the fatal consequences will be when the blind lead the "
             "blind.\"",
             f"{HENRY}, on Isaiah 29.", ("gods-people-called-blind", 0), ("gods-people-called-blind", 1),
             caution="Henry reads Isaiah 29 as already pointing at the leaders of Jesus's day; that is typology."),
        item("On \"who is blind but My servant,\" Henry sorts the verses: verse 18 may be spoken to Gentile idolaters, "
             "blind and deaf like the gods they worshipped, but verse 19 is God's own people and their priests and "
             "elders, ruined, he says, for want of observing what they saw. On Isaiah 43:8 he hears an echo of Psalm "
             "115: idolaters are \"blind people that have eyes,\" with the shape and faculties of men and not the use "
             "of them. The phrase itself settles the matter: these blind have eyes.",
             f"{HENRY}, on Isaiah 42 and 43.", ("gods-people-called-blind", 2), ("gods-people-called-blind", 3)),
        item("Laodicea's eye-salve was a local trade. The 1915 encyclopedia says the city was a wealthy centre of "
             "industry, famous for black wool and for a Phrygian eye-powder made there, with a renowned school of "
             "medicine nearby; after the earthquake of AD 60 its citizens refused Rome's help and rebuilt at their own "
             "expense, which is the pride the letter answers. \"Buy from Me salve for your eyes\" was said to a city "
             "that sold it.",
             f"{ISBE}, entries \"Laodicea\" and \"Eyesalve.\"", ("gods-people-called-blind", 5),
             caution="The encyclopedia relies on Ramsay, who is not on the shelf."),
        item("Henry on Laodicea: they could not see their state, their way or their danger, \"and they thought they "
             "saw.\" Then the clearest sentence on the shelf about where this figure lives: \"the sight of the body will "
             "not enlighten the soul.\" The remedy he reads in the eye-salve is to give up one's own wisdom, \"which are "
             "but blindness in the things of God.\"",
             f"{HENRY}, on Revelation 3.", ("gods-people-called-blind", 4), ("gods-people-called-blind", 6)),
    ],
    "like-the-blind": [
        item("Henry reads every one of these similes as judgment on the mind or as helplessness. Deuteronomy 28: those "
             "\"wilfully blind to their duty deserve to be made blind to their interest,\" and so grope at noon. Isaiah "
             "59, the people's own confession: \"we see no way open for our relief, nor know which way to expect it.\" "
             "Lamentations 4, of the prophets and priests: \"blind to every thing that is good, but to do evil they were "
             "quick-sighted,\" and shunned like a corpse.",
             f"{HENRY}, on Deuteronomy 28, Isaiah 59 and Lamentations 4.", ("like-the-blind", 0), ("like-the-blind", 1), ("like-the-blind", 2),
             caution="Henry nowhere describes how an actual blind person walks; one sentence of his on Zephaniah that does is omitted."),
        item("Behind the similes stand real people. The 1915 encyclopedia sees \"no reason to believe, as has been "
             "surmised, that blindness was any less rife in ancient times than it is now,\" and both it and Easton's "
             "set the Law's protections beside the figures: care for the blind was specially commanded, and wrongs "
             "against them counted as breaches of the Law. The writers who said \"like the blind\" had watched blind "
             "neighbors feel their way along the walls of their own towns.",
             f"{ISBE}, entry \"Blindness\"; {EASTON}, entry \"Blind.\"", ("like-the-blind", 4)),
    ],
    "eyes-dim-with-grief": [
        item("Henry takes all five laments as real eyes. Job \"wept so much that he had almost lost his sight\"; David "
             "\"wept till he had almost wept his eyes out\"; for Psalm 38 Henry offers three causes, much weeping, a "
             "discharge in the eyes, or faintness from low spirits; Lamentations 5:17 he glosses as the sight failing "
             "in \"a fainting fit.\" On Psalm 88 he reads weeping and praying together: \"prayers and tears go together, "
             "and they shall be accepted together.\" The 1915 encyclopedia gathers the same verses under the physical "
             "eye, apart from the figurative \"eye of the heart.\"",
             f"{HENRY}, on Job 17, Psalms 6, 38 and 88, and Lamentations 5; {ISBE}, entry \"Eye.\"",
             ("eyes-dim-with-grief", 0), ("eyes-dim-with-grief", 1), ("eyes-dim-with-grief", 2), ("eyes-dim-with-grief", 3),
             ("eyes-dim-with-grief", 4), ("eyes-dim-with-grief", 5),
             caution="Henry's causes are conjecture; the texts name none."),
    ],
    "bribes-and-curses": [
        item("Henry on the bribe: a judge must not so much as take a gift, \"for it has a strange tendency to blind "
             "those that otherwise would do well.\" The blinding is a slow, unintended corruption of a good man. The "
             "courts sat in the gates; Henry reports the later Jewish arrangement of seventy elders at the sanctuary, "
             "twenty-three judges in the larger towns and three in the small. The 1915 encyclopedia says the Old "
             "Testament \"abounds with allusions\" to the venality of judges, and Easton gives the Hebrew literally: the "
             "gift \"maketh open eyes blind.\"",
             f"{HENRY}, on Exodus 23 and Deuteronomy 16; {ISBE}, entries \"Blindness, Judicial\" and \"Bribery\"; {EASTON}, entry \"Bribe.\"",
             ("bribes-and-curses", 0), ("bribes-and-curses", 1), ("bribes-and-curses", 2)),
        item("The curses. Henry reads the shepherd's darkened right eye as losing sight of danger, and ties it to John "
             "9:39. The 1915 encyclopedia explains why the right eye in particular: blinding it \"robbed the victim of "
             "his beauty, and made him unfit to take his part in war,\" and it names the custom of putting out enemies' "
             "eyes among the surrounding nations. Of the horses Henry says that blinding them \"will be as bad as "
             "houghing them,\" an old word for cutting the tendons of the leg; the cavalry is simply made useless.",
             f"{HENRY}, on Zechariah 11 and 12; {ISBE}, entry \"Eye.\"", ("bribes-and-curses", 3), ("bribes-and-curses", 4), ("bribes-and-curses", 5)),
    ],
    "eyes-opened": [
        item("Did the commentators read the promises as eyes or as understanding? Henry reads Psalm 146:8 and Isaiah "
             "35:5 both ways at once. On the psalm he says God \"gives sight to those that have been long deprived of "
             "it,\" and that the verse points to Christ, since no one had opened the eyes of a man born blind until He "
             "did. On Isaiah 35 he is plainest: \"Wonders shall be wrought on men's bodies: the eyes of the blind shall "
             "be opened,\" naming the man born blind, and then \"greater wonders\" on souls.",
             f"{HENRY}, on Psalm 146 and Isaiah 35.", ("eyes-opened", 0), ("eyes-opened", 2)),
        item("Isaiah 29:18, 42:7, 42:16 and Luke 4:18 Henry reads as spiritual only: ignorance becoming "
             "understanding, Christ presenting the object by His word and preparing the organ by His Spirit, those \"by "
             "nature blind\" led by a way they knew not, with Paul struck blind on the road as his example. Edersheim "
             "sums up the Nazareth reading as \"the healing which He offers to those whom sin had blinded.\" No "
             "commentator on the shelf reads Isaiah 42:16 as a promise of guidance to people who cannot see. That "
             "reading, on this page, is Brian's and the site's.",
             f"{HENRY}, on Isaiah 29 and 42 and Luke 4; {ED}, Book III, chapter XI.",
             ("eyes-opened", 3), ("eyes-opened", 4), ("eyes-opened", 5), ("eyes-opened", 6),
             caution="The site's reading of Isaiah 42:16 is marked as its own."),
        item("How these verses were heard in Jesus's day: Edersheim notes that the rabbinic collections apply Isaiah "
             "35:5-6 to the days of the Messiah, as does the Midrash on Psalm 146:8, which is why Jesus could answer "
             "John the Baptist by pointing to the blind who saw. At Nazareth, he says, Jesus read the prophetic lesson "
             "from the Isaiah scroll handed to Him by the attendant; unrolled, far more than the passage He read would "
             "have lain under His eyes.",
             f"{ED}, Book III, chapters III and XI, and Appendix IX.", ("eyes-opened", 1), ("eyes-opened", 7),
             caution="The rabbinic collections were compiled after the first century."),
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
