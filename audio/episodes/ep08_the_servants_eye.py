"""Episode 8, the second of four on the Law: The servant's eye (Exodus 21:26-27).

No imagined scenes. Brian's question is the spine; the Hebrew words ayin, chophshi and deror are followed to the
other verses that use them; BOOKS reads Hammurabi, Henry and Josephus word for word. Drafted 16 October 2026.
"""
from episode_lib import CLOSE, LAW_INTRO, SERIES_INTRO, header, reader

SLUG = "the_servants_eye"
NUMBER = 8
TITLE = "The servant's eye"
PASSAGES = [("Exodus", 21, 20, 27), ("Judges", 16, 21, 21), ("2 Kings", 25, 7, 7),
            ("Exodus", 21, 2, 2), ("Deuteronomy", 15, 12, 15), ("Leviticus", 25, 10, 10),
            ("Leviticus", 25, 39, 41), ("Isaiah", 61, 1, 1)]
MAX_WORDS = 3400

# Brian's words on the page (law/servant-blinded), approved 16 October 2026.
DRAFT_BRIAN = [
    "Reading this law, the first thing that struck me was the pairing of an eye with a tooth. I have lost two teeth "
    "since I lost my two eyes, and the adjustment was not remotely the same. Put plainly: a servant with a loose "
    "tooth could be struck once and walk out free, and the law sets that beside a man who will never see again. It "
    "seemed unbalanced. Then I read it as the old commentators did. The tooth is not there because it equals an eye. "
    "It is there because it is the smallest lasting harm anyone would bother to name. If even that freed a servant, "
    "then nothing a master could do to a servant's body was free of cost. The eye was never in question.",
    "The second thing was the money. The tables from Babylon on this page put silver on an eye, less silver on a "
    "tooth, and for a servant's eye, a payment to the owner. How do you price reduced sight, or no sight at all? I "
    "would guess that some of these servants were left completely blind. Is that worth the price of freedom? The Law "
    "of Moses does not try to answer in silver. It names no sum. It gives the servant the one thing the master cannot "
    "keep back, which is himself.",
    "Here is the other side of it, and I mean this. I have lived without light since 2014. My freedom, and above all "
    "my freedom to worship God in the way I choose, is worth more to me than my sight ever was. I have adapted, "
    "adjusted, and found God's purpose for me. In so many ways my blindness has been a gift from God, the third "
    "greatest after my salvation and my wife. It has brought us more blessings than I can list, and it has shaped my "
    "character to fit His purposes better than it did.",
    "So I read this law two ways at once. Freedom is not a price for an eye, and the law does not pretend it is. But "
    "freedom is also not a small thing to hand a blind man, and I know that from the inside.",
]
APPROVED = {0, 1, 2, 3}


def build(bible: dict) -> list[str]:
    L = header("ep08_the_servants_eye")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 8: The servant's eye. Draft script. Second of four on the Law.")
    add("# HENRY reads Matthew Henry; BOOKS reads the other old commentators and the other law codes, word for word. No imagined scenes.")
    add("")

    # ---- A word about words (Brian, 17 October 2026: settle the audience before the law is read) -------
    add("[NARRATOR] (calm) Before the law, a word about words.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Some words we have heard so often that we no longer hear them. Say an eye for an eye, and "
        "nearly everyone will tell you what it means: revenge, measured out exactly. Say the word free, and you will "
        "have to ask which kind. Free as in no charge, or free as in no chains. The first costs nothing. The second "
        "can cost everything.")
    add("[NARRATOR] (calm) Last time, one word in a law turned out to mean a fall and not a trip. This law has both of "
        "these in it. An eye, and free. And one of them does not mean what most people think.")
    add("[PAUSE 1.5]")

    # ---- Cold open ----------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Two verses of law, and in them the only price the Bible ever puts on an eye.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (plainly) If a man strikes and blinds the eye of his manservant or maidservant, he must let the "
        "servant go free as compensation for the eye. And if he knocks out the tooth of his manservant or "
        "maidservant, he must let the servant go free as compensation for the tooth.")
    add("[PAUSE 1.5]")
    add("[NARRATOR] (dryly) And now, Mister Scaredy Cat. Shy Brian is back, with his own words and another man's voice.")
    add("[PAUSE 1.0]")
    add("[BRIAN] (calm) Reading this law, the first thing that struck me was the pairing of an eye with a tooth. I "
        "have lost two teeth since I lost my two eyes, and the adjustment was not remotely the same. Put plainly: a "
        "servant with a loose tooth could be struck once and walk out free, and the law sets that beside a man who "
        "will never see again. It seemed unbalanced.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) An eye and a tooth, side by side, with the same price. This episode is about why, and "
        "about what the price is, and what it is not.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add(f"[NARRATOR] (calm) {LAW_INTRO}")
    add("[BREAK]")

    # ---- Where and when, and the passage ------------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Exodus chapter twenty-one. Israel is at Sinai, in the first year "
        "out of Egypt, and these are the laws that follow straight after the Ten Commandments. They are case laws: "
        "if this happens, then that. This stretch of them deals with injuries. A servant beaten to death. A pregnant "
        "woman struck in a fight. And the rule of equal measure that everyone has heard of, eye for eye, tooth for "
        "tooth. Our two verses come right after it.")
    ext(reader(bible, "Exodus", 21, 20, 27))
    add("[NARRATOR] (calm) Two things stand out before we go any further. The law assumes that masters did strike "
        "servants, and that eyes were lost that way. And it does not apply eye for eye to the master. The master "
        "does not lose his eye. The servant gains his freedom. Whether that was more or less protection than a "
        "servant had in the lands around Israel is a question the old books can answer, and we will get to it.")
    add("[BREAK]")

    # ---- The word: ayin -------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the words. There are two in these verses worth following, and a third that the Law "
        "adds from elsewhere. The first is the word for eye: ayin. Ah-yin. Strong's dictionary gives it as an eye, "
        "and then adds something easy to miss in English. By analogy, it says, a fountain. The eye of the landscape. "
        "The same word is a spring of water. The 1915 encyclopedia calls the eye the lamp of the body, and then says "
        "this:")
    add("[BOOKS] (calm) A cruel custom therefore sanctioned among heathen nations the putting out of the eyes of an "
        "enemy or a rival, because thus his power was most effectually shattered.")
    add("[NARRATOR] (calm) The encyclopedia gives three examples from the Bible, and two of them are stories on our "
        "site. The first is Samson.")
    ext(reader(bible, "Judges", 16, 21, 21))
    add("[NARRATOR] (calm) The second is Zedekiah, the last king of Judah, after the fall of Jerusalem.")
    ext(reader(bible, "2 Kings", 25, 7, 7))
    add("[NARRATOR] (calm) Gouged out. Put out. Those are the eyes of the Old Testament outside this law: taken by "
        "enemies, to break a man. The law of the servant stands between those two men. It is the one place where "
        "the Law of Moses puts a price on an eye, and the price is paid to the man who lost it.")
    add("[BREAK]")

    # ---- The word: chophshi ---------------------------------------------------------------------------------
    add("[NARRATOR] (calm) The second word is the word for free. Chophshi. Khof-shee. Strong's glosses it as exempt, "
        "from bondage, tax or care. And here is the thing. It is not a new word made for this law. It is the word "
        "used a few verses earlier in the same chapter, for the Hebrew servant who goes free in the seventh year.")
    ext(reader(bible, "Exodus", 21, 2, 2))
    add("[NARRATOR] (calm) Deuteronomy repeats the seventh-year rule forty years later, and adds something.")
    ext(reader(bible, "Deuteronomy", 15, 12, 15))
    add("[NARRATOR] (calm) Remember that you were slaves in Egypt. That is the reason the Law gives for freeing a "
        "servant at all. So when the law of the blinded servant says he goes free, chophshi, it is not inventing a "
        "new kind of release. It is giving him the release the Law already knew, the seventh-year freedom, at "
        "once. An eye bought what six years of service bought. A tooth bought it too.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Brian remembered, while reading this, that there was a second release in the Law besides "
        "the seventh year, and he was right. Every fiftieth year was the Jubilee.")
    ext(reader(bible, "Leviticus", 25, 10, 10))
    ext(reader(bible, "Leviticus", 25, 39, 41, lead="And for the man who had sold himself: "))
    add("[NARRATOR] (calm) The word for liberty there is a third word, deror. Deh-rore. Not the servant's chophshi. "
        "And deror is the word in one more verse, the one Jesus stood up and read in the synagogue at Nazareth, "
        "which listeners to episode six will remember.")
    ext(reader(bible, "Isaiah", 61, 1, 1))
    add("[NARRATOR] (calm) To proclaim liberty to the captives. Deror. The Jubilee's word. The blinded servant's "
        "release did not wait for the seventh year or the fiftieth. It came that day.")
    add("[BREAK]")

    # ---- The other codes ------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the other law codes, because this is the one law where the comparison is exact. "
        "Hammurabi of Babylon, some three to five centuries before Moses, wrote laws about eyes and teeth too. Here "
        "they are, in Johns's translation of 1903, read in order.")
    add("[BOOKS] (plainly) Section 196. If a man has caused the loss of a gentleman's eye, his eye one shall cause to "
        "be lost.")
    add("[BOOKS] (plainly) Section 198. If he has caused a poor man to lose his eye or shattered a poor man's limb, he "
        "shall pay one mina of silver.")
    add("[BOOKS] (plainly) Section 199. If he has caused the loss of the eye of a gentleman's servant or has shattered "
        "the limb of a gentleman's servant, he shall pay half his price.")
    add("[BOOKS] (plainly) Section 200. If a man has made the tooth of a man that is his equal to fall out, one shall "
        "make his tooth fall out. Section 201. If he has made the tooth of a poor man to fall out, he shall pay "
        "one-third of a mina of silver.")
    add("[NARRATOR] (calm) Hear the scale. A gentleman's eye costs you your own eye. A poor man's eye costs one mina "
        "of silver. A servant's eye costs half the servant's price, and nothing in the text says the servant sees any "
        "of it. The money goes where the loss was counted, and the loss was counted to the owner. The 1915 "
        "encyclopedia, in an article by an Assyriologist, weighed Exodus against Babylon and said this:")
    add("[BOOKS] (calm) One can hardly assert that the parallels quoted are accidental, but just as little could one "
        "say that they are directly taken from the Code; for they bear quite a definite impression due to the "
        "Israelitish culture, and numerous marked divergences also exist.")
    add("[NARRATOR] (calm) The servant's freedom is one of those divergences, and the largest. In Babylon a servant's "
        "eye was priced. In Israel it was freed.")
    add("[BREAK]")

    # ---- The old books on the tooth: Brian's question answered --------------------------------------------
    add("[NARRATOR] (calm) Now to Brian's question. Why the tooth? Matthew Henry, in seventeen hundred and six, read "
        "the two verses together and saw it.")
    add("[HENRY] (calm) The care God took of servants. If their masters maimed them, though it was only striking out "
        "a tooth, that should be their discharge.")
    add("[HENRY] (calm) To comfort them if they were abused; the loss of a limb should be the gaining of their "
        "liberty, which would do something towards balancing both the pain and disgrace they underwent.")
    add("[NARRATOR] (calm) Though it was only striking out a tooth. The tooth is not in the law because it equals an "
        "eye. It is in the law because it is the smallest lasting harm anyone would bother to name. Set the "
        "threshold there, and every harm above it, the eye above all, is beyond doubt. Smith's dictionary reads it "
        "the same way: the master's power over the servant's body was so far limited that maiming gave liberty at "
        "once, by the fact itself.")
    add("[NARRATOR] (calm) And by the first century, Josephus says, even eye for eye among free men had become a "
        "matter of money, at the choice of the one who was hurt.")
    add("[BOOKS] (calm) He that maimeth any one, let him undergo the like himself, and be deprived of the same member "
        "of which he hath deprived the other, unless he that is maimed will accept of money instead of it; for the "
        "law makes the sufferer the judge of the value of what he hath suffered.")
    add("[NARRATOR] (calm) The sufferer the judge of the value. Keep that phrase. It is what Brian is about to do.")
    add("[BREAK]")

    # ---- From Brian ---------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Brian, on the tooth, on the money, and on the other side of it.")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")

    # ---- Close --------------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Next time, the one law that limits what a blind man may do: the blind priest, who could "
        "not go near the altar, and who ate at the table all the same.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
