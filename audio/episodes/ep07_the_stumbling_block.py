"""Episode 7, the first of four on the Law: The stumbling block (Leviticus 19:14; Deuteronomy 27:18).

The Law series has no imagined scenes. In their place: Brian's own question as the spine, the Hebrew word
followed to the other verses that use it, and the old books and the other law codes read aloud in their own
voice (BOOKS). Drafted 16 October 2026 to the shape Brian chose.
"""
from episode_lib import CLOSE, LAW_INTRO, SERIES_INTRO, header, reader

SLUG = "the_stumbling_block"
NUMBER = 7
TITLE = "The stumbling block"
# In the order the READER reads them: the law in its chapter, the curse, then the word's other verses.
PASSAGES = [("Leviticus", 19, 13, 18), ("Deuteronomy", 27, 11, 19),
            ("Jeremiah", 6, 21, 21), ("Ezekiel", 3, 20, 20), ("Isaiah", 8, 14, 15), ("Psalm", 119, 165, 165)]
MAX_WORDS = 3400   # Brian, 16 October 2026: the Law episodes should run 18 to 22 minutes like the later story episodes

# Brian's words on the page (law/stumbling-block), approved 14 October 2026. Both are his questions; the
# episode answers them and he does not need a new closing paragraph unless he wants one.
DRAFT_BRIAN = [
    "Reading that first section caused me to question a few things, and the answers are now on this page, in the "
    "sections on the word and on the place and the time. It doesn't look like Hammurabi's code has anything about "
    "the treatment of the blind. So is the Bible the first recorded anything that addresses the blind? And when was "
    "Hammurabi's code written compared with what Moses was doing in Leviticus and Deuteronomy?",
    "Then the stumbling block itself. For me, a stumbling block is an annoyance more than anything: something I would "
    "stumble over, but not necessarily fall down. I stumble over curbs and parking stops all the time and somehow "
    "always seem to catch myself. I am fortunate to have enough of a sense of balance and spatial awareness for this "
    "to work. Most blind people I know will easily trip over curbs and parking stops, usually resulting in serious "
    "pain of some sort. So is this notion of a stumbling block more like me tripping slightly, or more like a blind "
    "person falling down and breaking or spraining something?",
    # A closing paragraph drafted for him from what he has said; his to change or strike.
    "So now I have my answer, and it is not the one I expected. The word is about the fall, not the trip. The law was "
    "not written for people like me, who catch themselves. It was written for the people I know who do not, and for "
    "the man who moved the stone and walked away, sure that nobody saw. Somebody saw.",
]
APPROVED = {0, 1}


def build(bible: dict) -> list[str]:
    L = header("ep07_the_stumbling_block")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 7: The stumbling block. Draft script. First of four on the Law.")
    add("# BOOKS reads the old commentators and the other law codes, word for word. No imagined scenes in this series.")
    add("")

    # ---- Cold open: the law itself, then Brian's question -----------------------------------------------
    add("[NARRATOR] (calm) One sentence of law. Thirty-one words in English, given at Sinai, more than three "
        "thousand years ago.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (plainly) You must not curse the deaf or place a stumbling block before the blind, but you shall "
        "fear your God. I am the LORD.")
    add("[PAUSE 1.5]")
    add("[NARRATOR] (calm) Brian read that sentence and asked a question that nobody sighted would think to ask.")
    add("[NARRATOR] (dryly) And now, Mister Scaredy Cat. Not Brian's voice, but his words.")
    add("[PAUSE 1.0]")
    add("[BRIAN] (calm) For me, a stumbling block is an annoyance more than anything: something I would stumble over, "
        "but not necessarily fall down. I stumble over curbs and parking stops all the time and somehow always seem "
        "to catch myself. I am fortunate to have enough of a sense of balance and spatial awareness for this to work. "
        "Most blind people I know will easily trip over curbs and parking stops, usually resulting in serious pain of "
        "some sort. So is this notion of a stumbling block more like me tripping slightly, or more like a blind "
        "person falling down and breaking or spraining something?")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) That is the question this episode answers. A trip, or a fall. The answer is in the word "
        "itself, and in where else the Bible uses it.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add(f"[NARRATOR] (calm) {LAW_INTRO}")
    add("[BREAK]")

    # ---- Where and when -----------------------------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Leviticus chapter nineteen is a chapter of commands about ordinary "
        "life, given to the whole assembly of Israel at Mount Sinai, in the first year after they came out of Egypt. "
        "The verses around our verse are about leaving gleanings for the poor, paying a hired man on time, honest "
        "courts, and loving your neighbor as yourself. The law about the blind sits in the middle of them, between "
        "wages and justice.")
    add("[NARRATOR] (calm) Where this is. Sinai lies far to the south of everything else in this series, off the "
        "bottom edge of our map. From Jerusalem it is about eleven days' walk, down through the desert. The second "
        "passage we will hear was spoken by Moses on the plains east of the Jordan, forty years later, and it looks "
        "forward to a place inside the land: two mountains facing each other across a narrow valley, with the town "
        "of Shechem between them. Stand in Jerusalem and face north, with north at twelve o'clock. Shechem is at "
        "twelve o'clock, about a day and a half's walk, in the hill country that would become Samaria.")
    ext(reader(bible, "Leviticus", 19, 13, 18, lead="Hear the law in its place. "))
    add("[NARRATOR] (calm) Notice the company it keeps. Wages. Fair courts. Slander. Grudges. Love your neighbor. "
        "The blind man and the deaf man are not set apart in a chapter of their own. They are in the chapter about "
        "how to treat the people next to you.")
    add("[NARRATOR] (calm) Now the second passage. Moses is commanding a ceremony for the day Israel crosses the "
        "Jordan. Six tribes are to stand on one mountain and six on the other, and the Levites are to call out "
        "twelve curses, and the whole nation is to answer each one. The blind man is in the list.")
    ext(reader(bible, "Deuteronomy", 27, 11, 19))
    add("[NARRATOR] (calm) Think about the sound of that. A valley with a mountain on either side, and on the slopes, "
        "a whole people. The Levites call out, and the answer comes back from both sides at once. Amen. Twelve times. "
        "And one of the twelve is for the man who lets a blind traveller wander off the road. Look at who his "
        "neighbours are in that list: the man who makes an idol in secret, the man who moves a boundary stone, the "
        "man who cheats the foreigner, the fatherless and the widow. Hidden wrongs, every one. Wrongs that no court "
        "would ever hear about.")
    add("[BREAK]")

    # ---- The word -------------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the word. The Hebrew behind stumbling block is mikshol. Say it with me: mik-shole. "
        "Strong's dictionary, from 1894, gives it as a stumbling-block, literally or figuratively, and derives it "
        "from a verb that means to totter or fall. The 1915 encyclopedia says its literal sense is an object which "
        "causes one to stumble or fall, and it says something else that matters for Brian's question. Leviticus "
        "nineteen fourteen, it says, is the one place in the Bible where the word is plainly literal. Everywhere "
        "else it is used for what brings material ruin or spiritual downfall.")
    add("[NARRATOR] (calm) So let us go everywhere else. Here is the same word, mikshol, in four other places. "
        "Listen to what happens to the people in them.")
    ext(reader(bible, "Jeremiah", 6, 21, 21))
    add("[NARRATOR] (beat) Friends and neighbors will perish.")
    ext(reader(bible, "Ezekiel", 3, 20, 20))
    add("[NARRATOR] (beat) He will die.")
    ext(reader(bible, "Isaiah", 8, 14, 15))
    add("[NARRATOR] (beat) They will fall and be broken.")
    ext(reader(bible, "Psalm", 119, 165, 165))
    add("[NARRATOR] (calm) Only the psalm is gentle, and there the stumbling block is the thing that cannot happen "
        "to those who love God's law. Perish. Die. Fall and be broken. That is the company this word keeps. So "
        "here is the answer to Brian's question, on the words alone. The law is about the fall, not the trip. And "
        "in the word's other uses, about worse than a fall. It was written for the people who do not catch "
        "themselves.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Two more words from the same verse. The blind man is ivver, the plain word for blind, the "
        "one you will hear in all four of these episodes. And the reason the law gives, you shall fear your God, "
        "uses yare. Yah-ray. To fear, or to revere. Hold on to that word. It opens the Law's care for the blind "
        "here, and in the fourth episode you will hear it close the Law's last word on the subject, a thousand "
        "years later.")
    add("[NARRATOR] (calm) And the curse in Deuteronomy uses a different verb for what is done to the blind man. "
        "He is made to wander: shagah, to stray, or to be led astray. The word for going wrong without knowing it.")
    add("[BREAK]")

    # ---- The old books ------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the old books. In these episodes they speak for themselves, in a voice of their own, "
        "and I will tell you who is speaking and when. First, Matthew Henry, a pastor writing in England in "
        "seventeen hundred and six, on this verse.")
    add("[BOOKS] (calm) The safety of the blind we must likewise be tender of, and not put a stumbling-block before "
        "them; for this is to add affliction to the afflicted, and to make God's providence a servant to our malice.")
    add("[BOOKS] (calm) This prohibition implies a precept to help the blind, and remove stumbling-blocks out of "
        "their way.")
    add("[NARRATOR] (calm) And on the words, you shall fear your God, Henry gives the reason that still holds.")
    add("[BOOKS] (calm) Thou dost not fear the deaf and blind, they cannot right themselves; but remember it is the "
        "glory of God to help the helpless, and he will plead their cause.")
    add("[NARRATOR] (calm) That is the heart of it. Both wrongs in this verse are wrongs the victim cannot catch. The "
        "deaf man does not hear the curse. The blind man does not see who moved the stone, or who stood and "
        "watched him take the wrong road. No witness is coming forward. So the law does not appeal to a court. It "
        "appeals to the one who saw.")
    add("[NARRATOR] (calm) Now Josephus, a Jewish historian writing for Roman readers about the year ninety-three, "
        "retelling the Law in everyday terms.")
    add("[BOOKS] (calm) It is also a duty to show the roads to those who do not know them, and not to esteem it a "
        "matter for sport, when we hinder others' advantages, by setting them in a wrong way. In like manner, let "
        "no one revile a person blind or dumb.")
    add("[NARRATOR] (calm) Three things in that are his, not Leviticus's. The law only forbids; Josephus adds a duty, "
        "to show the way to anyone who does not know it. The law gives no motive; Josephus names one. Sport. The "
        "pleasure of watching somebody go wrong. And he pairs the blind with the dumb, those who cannot speak, as "
        "Leviticus pairs the blind with the deaf: people who cannot catch you, and cannot answer back. So this is "
        "what a Jewish writer in the first century thought the law was guarding against. Not an accident on the "
        "road. A cruel joke, played on someone who would never know who played it.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) One honest counterweight, from Henry again. He reports that the Jewish commentators "
        "before him found the literal act unthinkable.")
    add("[BOOKS] (calm) The Jewish writers, thinking it impossible that any should be so barbarous as to put a "
        "stumbling-block in the way of the blind, understood it figuratively, that it forbids giving bad counsel to "
        "those that are simple and easily imposed upon.")
    add("[NARRATOR] (calm) Both readings have been held for a very long time. A law is not proof that a thing was "
        "common. It is a sign that someone thought it worth forbidding, and here, worth a curse said aloud by a "
        "whole nation.")
    add("[BREAK]")

    # ---- The other codes: Brian's first question ---------------------------------------------------------
    add("[NARRATOR] (calm) Brian had an earlier question too, and it is a good one.")
    add("[BRIAN] (calm) It doesn't look like Hammurabi's code has anything about the treatment of the blind. So is "
        "the Bible the first recorded anything that addresses the blind? And when was Hammurabi's code written "
        "compared with what Moses was doing in Leviticus and Deuteronomy?")
    add("[NARRATOR] (calm) Hammurabi was king of Babylon from about seventeen ninety-two to seventeen fifty before "
        "Christ. For Moses there are two main datings, one around fourteen ninety and one around twelve fifty, so "
        "Hammurabi comes first by three to five centuries. His code is the most famous law code of the ancient "
        "world, and its prologue makes a large claim. Here is the king himself, as the 1915 encyclopedia renders "
        "him.")
    add("[BOOKS] (calm) As a helper of the oppressed, as an adviser of widows and orphans, in short, as the father of "
        "his people.")
    add("[NARRATOR] (calm) But when you look for the blind in his two hundred and eighty-two laws, you find eyes "
        "only as injuries to be priced. We will hear those laws in the next episode. There is no law in Hammurabi "
        "protecting a blind person. Nor in the older code of Ur-Nammu, three centuries before him, which prices a "
        "knocked-out eye at half a mina of silver and says nothing else. So is the Bible first? Not quite. One text "
        "from Egypt does show regard, the Instruction of Amenemope, dated somewhere between thirteen hundred and ten "
        "seventy-five before Christ. In Budge's translation of 1924 it reads:")
    add("[BOOKS] (calm) Make not a laughing-stock of the blind man. Vex not the dwarf. And frustrate not the plans "
        "of the afflicted.")
    add("[NARRATOR] (calm) Notice what Amenemope forbids. Laughter. The same thing Josephus heard in the law of "
        "Moses, sport at a blind man's expense, was worth a warning on the Nile too. But it is advice from a wise "
        "man to his son. It is not law, and it carries no curse and no God who sees. As far as the shelf can tell, "
        "Leviticus nineteen fourteen is the first law in the ancient world written to protect a blind person, rather "
        "than to price his eye.")
    add("[BREAK]")

    # ---- Reasoning it through -----------------------------------------------------------------------------
    add("[NARRATOR] (calm) Let me put the two laws together and reason it through, with no story and nobody "
        "invented. Suppose a stone is moved into a path a blind man walks every day. He falls. Who saw it? Perhaps "
        "nobody. Perhaps one man, who is not going to speak. The blind man cannot say who did it. There is no case. "
        "That is exactly why the first law says, you shall fear your God. It names the only witness there is. And "
        "suppose a traveller asks the way, and is pointed wrong, for sport, and walks an hour into the wrong valley. "
        "Who would ever prove it? Nobody. That is why the second law is not a fine. It is a curse, said by the whole "
        "nation at once, so that every man in Israel had stood on a mountainside and said Amen to it before he was "
        "ever tempted.")
    add("[NARRATOR] (calm) The Law did what law can do for a wrong that leaves no witness. It made the whole "
        "people the witness, and God the judge.")
    add("[BREAK]")

    # ---- From Brian ---------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Brian, with the last word.")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add("[BREAK]")

    # ---- Close --------------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Next time, the one law in the Bible that puts a price on an eye, and what the price "
        "turns out to be. The servant blinded by his master.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
