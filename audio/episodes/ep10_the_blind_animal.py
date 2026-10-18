"""Episode 10, the last of four on the Law: The blind animal and the altar (Leviticus 22; Deuteronomy 15; Malachi 1).

No imagined scenes. Brian's question is the spine; the words mum, tamim and yare are followed; BOOKS reads
Henry and Edersheim word for word; the episode closes the Law series with a look back through its four words.
Drafted 16 October 2026.
"""
from episode_lib import CLOSE, LAW_INTRO, SERIES_INTRO, header, reader

SLUG = "the_blind_animal"
NUMBER = 10
TITLE = "The blind animal and the altar"
PASSAGES = [("Leviticus", 22, 17, 25), ("Deuteronomy", 15, 19, 23), ("Exodus", 12, 5, 5),
            ("Deuteronomy", 18, 13, 13), ("Psalm", 15, 2, 2), ("Malachi", 1, 6, 14),
            ("Genesis", 4, 3, 5), ("2 Samuel", 24, 24, 24)]
MAX_WORDS = 3500

# Brian's words on the page (law/blind-animals), approved 16 October 2026.
DRAFT_BRIAN = [
    "This one was harder to read than I expected, and not because of what it asks of a lamb. It is because it puts "
    "blindness straight into the category of broken. In society's terms I am disabled. But when I hear of a disabled "
    "car, I can swap in the word broken without losing anything, and I most certainly do not feel broken. I do most "
    "tasks differently now, with a different set of skills and more steps. Yet I still carry nearly all the same "
    "obligations, responsibilities, enjoyments and pleasures that I had with full sight.",
    "If anything, I am better at the things God wants me to be better at. Fewer distractions means more focused "
    "attention on the people I love, and on the people I need to go and find to love.",
    "The law itself leaves me a door. The blind firstborn was not thrown away. Deuteronomy says to eat it at home, "
    "as you would a gazelle or a deer, and the page above says what that means: not fit for the altar is not the "
    "same as worthless. A thing with a defect still fed a family. I would not have chosen the word defect for "
    "myself. But I notice that even this law, the hardest one on these pages for me to read, does not call the blind "
    "animal broken. It calls it ordinary.",
]
APPROVED = {0, 1, 2}


def build(bible: dict) -> list[str]:
    L = header("ep10_the_blind_animal")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 10: The blind animal and the altar. Draft script. Last of four on the Law.")
    add("# BOOKS reads the old commentators word for word. No imagined scenes.")
    add("")

    # ---- Cold open ----------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) The last law in this series is not about blind people. It is about lambs. It is here "
        "because the list would not be honest without it, and because Brian found it the hardest of the four to "
        "read.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (plainly) You are not to present to the LORD any animal that is blind, injured, or maimed.")
    add("[PAUSE 1.5]")
    add("[NARRATOR] (dryly) One last time in this series, Mister Scaredy Cat. Brian still will not use his own voice, so this one speaks for him. Every word is his.")
    add("[PAUSE 1.0]")
    add("[BRIAN] (calm) This one was harder to read than I expected, and not because of what it asks of a lamb. It "
        "is because it puts blindness straight into the category of broken.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Broken. That is the word this episode has to answer. We will answer it with two Hebrew "
        "words, a market in the Temple, a prophet's test, and a look back over everything the Law said about the "
        "blind.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add(f"[NARRATOR] (calm) {LAW_INTRO}")
    add("[BREAK]")

    # ---- Where and when, and the passages -------------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Three places and a thousand years. Leviticus chapter twenty-two, at "
        "Sinai, gives the rule for what may be offered. Deuteronomy chapter fifteen, on the plains east of the "
        "Jordan forty years later, applies it to the firstborn of the flock, which belonged to God. And Malachi, "
        "the last book of the Old Testament, speaks in Jerusalem a thousand years after Sinai, to priests of the "
        "second Temple who were offering blind, lame and sick animals and calling the LORD's table contemptible.")
    ext(reader(bible, "Leviticus", 22, 17, 25))
    add("[NARRATOR] (calm) Blind heads the list in verse twenty-two, as it did in the list of the priest's defects. "
        "Now Deuteronomy, and what became of a blind firstborn.")
    ext(reader(bible, "Deuteronomy", 15, 19, 23))
    add("[NARRATOR] (calm) Eat it within your gates, as you would a gazelle or a deer. Henry puts it in a sentence: "
        "it was killed and eaten at their own houses as common food. The blemish kept it from the altar, not from "
        "the table. Remember that. Brian will come back to it.")
    add("[BREAK]")

    # ---- The words: mum and tamim ---------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the words, and this law has two, a negative and a positive. The negative is one you "
        "heard last time. The animal must not have a mum, a blemish. It is exactly the word of the blind priest. "
        "The priest with a mum does not approach; the lamb with a mum is not accepted. The Law used the same "
        "measure for the man and for the lamb, and in the end, as the encyclopedia notes, for Christ, the lamb "
        "without blemish.")
    add("[NARRATOR] (calm) The positive word is tamim. Tah-meem. The animal must be tamim, which the Berean text "
        "gives as unblemished and Strong's as entire, whole, complete. It is the Passover lamb's word.")
    ext(reader(bible, "Exodus", 12, 5, 5))
    add("[NARRATOR] (calm) But here is what the dictionary cannot tell you and the Bible can. Tamim is a word used of "
        "people far more often than of animals. Listen.")
    ext(reader(bible, "Deuteronomy", 18, 13, 13))
    add("[NARRATOR] (beat) Blameless. Tamim.")
    ext(reader(bible, "Psalm", 15, 2, 2))
    add("[NARRATOR] (beat) With integrity. Tamim.")
    add("[NARRATOR] (calm) So the thing the altar asked of a lamb is the thing God asks of a person's walk. Whole. "
        "And in neither case does it have anything to do with eyes. A blind man can walk tamim. That is the whole "
        "of the Law's answer to the word defect, and it is the beginning of the answer to Brian's word, broken.")
    add("[BREAK]")

    # ---- The old books: the market this law made ------------------------------------------------------------
    add("[NARRATOR] (calm) Now the old books, and a connection you may not expect. This law is why there was a "
        "market in the Temple. Here is Edersheim, writing in eighteen eighty-three, on what happened when a "
        "worshipper arrived with an animal.")
    add("[BOOKS] (calm) When an animal was brought, it had to be examined as to its Levitical fitness by persons "
        "regularly qualified and appointed.")
    add("[NARRATOR] (calm) Qualified examiners, who charged a fee. And so, Edersheim says, a shortcut appeared.")
    add("[BOOKS] (calm) All trouble and difficulty would be avoided by a regular market within the Temple-enclosure, "
        "where sacrificial animals could be purchased, having presumably been duly inspected, and all fees paid "
        "before being offered for sale.")
    add("[BOOKS] (calm) Most improper transactions were carried on, to the taking undue advantage of the poor people "
        "who came to offer their sacrifices.")
    add("[NARRATOR] (calm) He gives a case from the rabbis of a pair of pigeons run up to the price of a gold coin. "
        "Now think back to episode five. The tables Jesus overturned in the Temple court, on the day the blind and "
        "the lame came to Him there, were this market. The rule that God be given the best had become a trade that "
        "took the most from the poor. The law was good. What people built on it was not.")
    add("[BREAK]")

    # ---- Malachi, in order ----------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Which brings us to Malachi, who saw the same thing happen a thousand years after Sinai, "
        "and four hundred before the tables were overturned. His argument builds by steps, and the order matters. "
        "Hear it whole.")
    ext(reader(bible, "Malachi", 1, 6, 14))
    add("[NARRATOR] (calm) Hear the steps. A son honors his father and a servant his master; then, where is My "
        "honor, and where is your fear of Me? You call My table contemptible. You say, what a nuisance, and turn up "
        "your nose. You bring the stolen, the lame and the sick. Only then the test: try offering that to your "
        "governor. And last, the curse on the man who had a sound animal in his flock, vowed it, and gave a "
        "blemished one instead. Henry, on this chapter:")
    add("[BOOKS] (calm) The prophet is here, by a special commission, calling the priests to account, though they "
        "were themselves appointed judges, to call the people to an account.")
    add("[BOOKS] (calm) Would they, durst they, affront an earthly prince thus?")
    add("[NARRATOR] (calm) And Henry adds that what is said to the priests is said to all. The blind animal in "
        "Malachi is not about blindness. It is the sign of a gift given with contempt, by people who had something "
        "better and kept it back.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) The rest of the Bible puts the measure exactly where Malachi puts it: not on what the "
        "gift was worth, but on what it cost the giver. Two verses.")
    ext(reader(bible, "Genesis", 4, 3, 5))
    ext(reader(bible, "2 Samuel", 24, 24, 24, lead="And David, offered a threshing floor for nothing: "))
    add("[NARRATOR] (calm) Burnt offerings that cost me nothing. Jesus said the same of a widow's two coins: that she "
        "had put in more than all the others, because they gave from their surplus and she from her poverty. The "
        "lamb was never the point. The giver was.")
    add("[BREAK]")

    # ---- From Brian ---------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Brian, on the word broken.")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add("[BREAK]")

    # ---- The frame closes: yare, and the look back ---------------------------------------------------------
    add("[NARRATOR] (calm) One last word, and it is the one we planted in the first episode. Malachi ends his charge "
        "with, My name is to be feared among the nations. That is yare. Yah-ray. To fear, or to revere. It is the "
        "word of the stumbling block law: you shall fear your God. The first law about the blind and the last both "
        "rest on it. And look at why. Nobody would see the stone placed in the road. Nobody at the altar could tell, "
        "once the animal was offered, whether a better one had been kept back at home. Both laws were written for "
        "the wrong that no one catches, and both give the same reason to keep them. God saw.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Look back over the four. Mikshol, the stumbling block: a word about the fall, not the trip, "
        "and a law written for the people who do not catch themselves. Ayin and chophshi, the eye and the freedom: "
        "the one price the Law ever put on an eye, and it was paid to the man who lost it, in the coin of the "
        "seventh year. Mum and tamim, the blemish and the whole: one measure for the priest and the lamb, and a word "
        "for wholeness that a blind man can walk in as well as anyone. And yare, the fear of God, at the beginning "
        "and the end.")
    add("[NARRATOR] (calm) Four laws. Not one of them calls a blind person broken. One protects him by name. One "
        "frees him. One keeps him in the priesthood and at the table. And one, about lambs, says that God is given "
        "the best, and then lets the blind animal feed a family. Read as a whole, the Law's word on the blind is "
        "not a word about what they lack. It is a word to everyone else, about how to treat them, and about who is "
        "watching.")
    add("[BREAK]")

    # ---- Close --------------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) This has been the Law. The stories of the Old Testament are still to come: Isaac, Jacob, "
        "Eli, Samson, and the rest.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
