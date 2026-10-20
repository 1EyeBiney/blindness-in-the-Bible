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
            ("Genesis", 4, 3, 5), ("2 Samuel", 24, 24, 24), ("Mark", 12, 43, 44)]
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
    "as you would a gazelle or a deer, and Matthew Henry says what that means: not fit for the altar is not the "
    "same as worthless. A thing with a defect still fed a family. I would not have chosen the word defect for "
    "myself. But I notice that even this law, the hardest one in this series for me to read, does not call the blind "
    "animal broken. It calls it ordinary.",
]
APPROVED = {0, 1, 2}


def build(bible: dict) -> list[str]:
    L = header("ep10_the_blind_animal")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 10: The blind animal and the altar. Draft script. Last of four on the Law.")
    add("# HENRY reads Matthew Henry; BOOKS reads the other old commentators word for word. No imagined scenes.")
    add("")

    # ---- A word about words (Brian, 17 October 2026: settle the audience before the law is read) -------
    add("[NARRATOR] (calm) One last time, before the law, a word about words.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Take the word blind. A blind corner. A blind spot. A blind date. Blind faith. Not one of "
        "those is about a person's eyes, and yet you understood every one of them. Words do that. They carry more "
        "than one meaning, and we pick the right one without noticing we have chosen.")
    add("[NARRATOR] (calm) This series has followed four words. Three of them you had probably never asked about. The "
        "fourth is the one the series is named for, and in this last law it is used in a way we have not met yet. "
        "Not of a man. Of a lamb, at the head of a list of things that are wrong with it. Brian read that list and "
        "reached for a word of his own. The word is broken.")
    add("[PAUSE 1.5]")

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
    add("[NARRATOR] (calm) Eat it within your gates, as you would a gazelle or a deer. Matthew Henry, a pastor in "
        "England who wrote his commentary on the whole Bible beginning in seventeen hundred and six, puts it in one "
        "sentence: it was killed and eaten at their own houses as common food. The blemish kept it from the altar, not from "
        "the table. Remember that. Brian will come back to it.")
    add("[BREAK]")

    # ---- The words: \"moom\" and \"tah-meem\" ---------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the words, and this law has two, a negative and a positive. The negative is one you "
        "heard last time. The animal must not have a \"moom\", a blemish. It is exactly the word of the blind priest. "
        "The priest with a \"moom\" does not approach; the lamb with a \"moom\" is not accepted. The Law used the same "
        "measure for the man and for the lamb, and in the end, as the encyclopedia notes, for Christ, the lamb "
        "without blemish.")
    add("[NARRATOR] (calm) The positive word is \"tah-meem.\" The animal must be \"tah-meem\", which the Berean text "
        "gives as unblemished and Strong's as entire, whole, complete. It is the Passover lamb's word.")
    ext(reader(bible, "Exodus", 12, 5, 5))
    add("[NARRATOR] (calm) But here is what the dictionary cannot tell you and the Bible can. \"Tah-meem\" is a word used of "
        "people far more often than of animals. Listen.")
    ext(reader(bible, "Deuteronomy", 18, 13, 13))
    add("[NARRATOR] (beat) Blameless. \"Tah-meem\".")
    ext(reader(bible, "Psalm", 15, 2, 2))
    add("[NARRATOR] (beat) With integrity. \"Tah-meem\".")
    add("[NARRATOR] (calm) So the thing the altar asked of a lamb is the thing God asks of a person's walk. Whole. "
        "And in neither case does it have anything to do with eyes. A blind man can walk \"tah-meem\". That is the whole "
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
    add("[NARRATOR] (calm) Hear how the argument builds. It goes step by step.")
    add("[NARRATOR] (calm) It starts with family. A son honors his father, and a servant his master. So if God is a "
        "father, where is His honor? If He is a master, where is the respect?")
    add("[NARRATOR] (calm) Then the charge. The priests have called the LORD's table contemptible. They bring blind "
        "animals, and lame ones, and sick ones, and lay them on the altar.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Then the test, and it is a sharp one. Try offering that to your governor. Would he be "
        "pleased with you? Matthew Henry puts the question plainly: would these priests dare to insult an earthly "
        "ruler like that? Of course not. No one brings a sick animal as a gift to the man who governs him. Yet they "
        "brought it to God.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Then the weariness. You say, what a nuisance, and you turn up your nose at it. The worship "
        "itself has become a chore.")
    add("[NARRATOR] (calm) And last, the curse. It does not fall on the poor man who had nothing better to give. It "
        "falls on the man who had a good animal in his flock, promised it to God, and then brought a blemished one "
        "instead.")
    add("[NARRATOR] (calm) Henry sums up what the prophet is doing.")
    add("[HENRY] (calm) The prophet is here, by a special commission, calling the priests to account, though they "
        "were themselves appointed judges, to call the people to an account.")
    add("[NARRATOR] (calm) In other words, the priests were the ones meant to judge the people's offerings. Now God "
        "judges theirs. And Henry adds that what is said to the priests is said to all of us. The blind animal in "
        "Malachi is not about blindness. It is the sign of a gift given with contempt, by people who had something "
        "better and kept it back.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) That last point is the key to this whole law. God was never really measuring the animal. "
        "He was measuring the giver.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) The rest of the Bible keeps the same measure. It never asks how much a gift was worth. It "
        "asks what the gift cost the one who gave it. You can hear that in two places. The first is the very first "
        "offering in the Bible, from two brothers, Cain and Abel.")
    ext(reader(bible, "Genesis", 4, 3, 5))
    add("[NARRATOR] (calm) Abel brought the best of the firstborn of his flock. Cain brought some of what he had. The "
        "second place is King David. A man named Araunah offered him a threshing floor, and oxen for the sacrifice, "
        "as a free gift. David would not take them.")
    ext(reader(bible, "2 Samuel", 24, 24, 24))
    add("[NARRATOR] (calm) Burnt offerings that cost me nothing. David would not give God something that had cost "
        "him nothing.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) A thousand years later, Jesus sat in the Temple, opposite the treasury, and watched people "
        "putting in their money. Many rich people put in large amounts. Then a poor widow came and put in two small "
        "copper coins.")
    ext(reader(bible, "Mark", 12, 43, 44))
    add("[NARRATOR] (calm) All she had to live on. That is the measure the Law was teaching with every lamb. The "
        "lamb was never the point. The giver was.")
    add("[BREAK]")

    # ---- From Brian ---------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Brian, on the word broken.")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add("[BREAK]")

    # ---- The frame closes: \"yah-ray\", and the look back ---------------------------------------------------------
    add("[NARRATOR] (calm) One last word, and it is the one we planted in episode seven. Malachi ends his charge "
        "with, My name is to be feared among the nations. That is \"yah-ray.\" To fear, or to revere. It is the "
        "word of the stumbling block law: you shall fear your God. The first law about the blind and the last both "
        "rest on it. And look at why. Nobody would see the stone placed in the road. Nobody at the altar could tell, "
        "once the animal was offered, whether a better one had been kept back at home. Both laws were written for "
        "the wrong that no one catches, and both give the same reason to keep them. God saw.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Now look back over the whole series, one law at a time.")
    add("[NARRATOR] (calm) First, the stumbling block, in episode seven. The word was \"mik-shole.\" Brian asked "
        "whether it meant a trip or a fall, and the word answered: a fall, and worse. That law was written for the "
        "people who do not catch themselves, and against the man who thought nobody saw.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Second, the servant's eye, in episode eight. Two words: \"ah-yin,\" the eye, and "
        "\"khof-shee,\" free. It was the one price the Law ever put on an eye, and the price went to the man who lost "
        "it. Not silver, but freedom, the same freedom as the seventh year, given that very day.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Then the blind priest, in episode nine, and the blind animal, in this one. They share one "
        "word, \"moom,\" a blemish, and one answer to it, \"tah-meem,\" whole. The same measure kept both the priest "
        "and the lamb from the altar. But \"tah-meem\" turned out to be a word for how a person walks, and a blind "
        "man can walk whole as well as anyone.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) And holding all four together is one more word: \"yah-ray,\" the fear of God. It was "
        "there at the beginning, in the stumbling block law, and it is here at the end, in Malachi.")
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
