"""Episode 9, the third of four on the Law: The blind priest (Leviticus 21:16-24).

No imagined scenes. Brian's three questions are the spine and are answered from the old books; the word mum is
followed to Absalom, the bride, and the lamb; BOOKS reads Henry, Josephus, Edersheim and the encyclopedia word
for word. Drafted 16 October 2026.
"""
from episode_lib import CLOSE, LAW_INTRO, SERIES_INTRO, header, reader

SLUG = "the_blind_priest"
NUMBER = 9
TITLE = "The blind priest"
PASSAGES = [("Leviticus", 21, 16, 24), ("2 Samuel", 14, 25, 25), ("Song of Solomon", 4, 7, 7),
            ("Leviticus", 22, 20, 20), ("1 Peter", 1, 18, 19)]
MAX_WORDS = 3400

# Brian's words on the page (law/priest), approved 16 October 2026.
DRAFT_BRIAN = [
    "Reading this law, I had three questions, and the section on the place and the time now answers them. I wanted "
    "to know what a priest actually did, and it turns out that most of it was done with the hands: the fire, the "
    "lamp, the sacrifices, the blood. I wondered whether a blind priest would touch things he should not, since I "
    "touch things all day to know what they are, and I learned that the rules about touching holy things were for "
    "the Levites who carried them, not for the priests who handled them. And I asked whether fitting a blind priest "
    "in would have burdened the rest, and the numbers say no. Twenty-four courses, a week each, fifty men on duty at "
    "a time. One blind man among them would hardly have been noticed.",
    "I find it hard to weigh this law as if it were mine to keep. We live on the far side of the cross. Our worship "
    "is not built around one altar and one family of priests, and the sacrifice this law guarded has been made once "
    "and for all. The word section above says it better than I can: the word that kept the blind priest from the "
    "altar is the word for the lamb that was offered on it. So I read this law as what it was, a rule for a few "
    "hundred men and one duty, and I do not read it as a word about what blind people are worth. The text itself "
    "takes care of that. He stayed a priest, and he ate at the table.",
    "What I can speak to is now. I know quite a few blind pastors and spiritual leaders, and I am grateful beyond "
    "words that they are allowed to minister and to do God's work with the talents and abilities they have. Nobody "
    "keeps them from the pulpit for a defect. I am glad we do not have that requirement.",
    "But we do have something else, and in some ways it is more shackling, because nobody wrote it down. It is low "
    "expectations. A rule can be read and argued with. An expectation just sits there, in the way people hesitate "
    "before handing you a task, or thank you too much for doing an ordinary thing. The old rabbis, arguing about "
    "whether a one-eyed priest could give the blessing, worried that the people would stare. One of them allowed it "
    "if the town was used to him. That is still the whole question. Not what the blind man can do, but what the "
    "people around him expect.",
    "So the blind priest of Leviticus and the blind pastor I know are in the same place after all. Both are kept, or "
    "freed, less by a law than by what the people in front of them are used to.",
    # The three questions as he first asked them on the page (3 October 2026), for the opening.
    "I need to know more about priestly duties. Would a blind priest accidentally touch things he should not? I have "
    "to touch things all the time to figure out what they are; would that factor in? And would trying to let the "
    "blind priest fit in have been a hindrance to the rest of the Levites?",
]
APPROVED = {0, 1, 2, 3, 4, 5}


def build(bible: dict) -> list[str]:
    L = header("ep09_the_blind_priest")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 9: The blind priest. Draft script. Third of four on the Law.")
    add("# HENRY reads Matthew Henry; BOOKS reads the other old commentators word for word. No imagined scenes.")
    add("")

    # ---- A word about words (Brian, 17 October 2026: settle the audience before the law is read) -------
    add("[NARRATOR] (calm) Before the law, a word about words.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Take the word fit. A key fits a lock. A coat fits a man. A man is fit for a job, or he is "
        "not. A pilot whose eyes fail is unfit to fly, and nobody hears that and thinks the pilot is unfit to live.")
    add("[NARRATOR] (calm) That is because fit always asks a question with two parts: fit for what? A key that will "
        "not open this lock is not a bad key. It is the wrong key for this door. A pilot who can no longer fly is "
        "still the same man he was yesterday. He is still a husband, a father and a friend. Only the cockpit has "
        "changed its answer. When we say unfit, we are talking about the task. We are not passing judgment on the "
        "person.")
    add("[NARRATOR] (calm) Every law in this series so far has turned on a word. This one turns on a word for a flaw, "
        "and on what a flaw disqualifies a man from. For three thousand years people have read it as a verdict on "
        "the man. The text reads it as a measure against one task. Those are not the same, and the difference is "
        "the whole of this episode.")
    add("[PAUSE 1.5]")

    # ---- Cold open ----------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Of all the laws in the Bible that mention the blind, this is the only one that limits what "
        "a blind person may do. It is worth reading exactly.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (plainly) No man who has any defect may approach. No man who is blind, lame, disfigured, or "
        "deformed.")
    add("[PAUSE 1.5]")
    add("[NARRATOR] (calm) When Brian first read it, he did not argue with it. He asked three practical questions, "
        "the kind only a blind man would ask.")
    add("[NARRATOR] (dryly) Here is Mister Scaredy Cat again. The voice is borrowed. The words are Brian's.")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[5]}")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) What did a priest do with his hands. Would a blind priest touch what he should not. Would "
        "he be a burden to the rest. This episode answers all three, from the old books, and then asks the question "
        "underneath them, which is what this law says about what a blind person is worth.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add(f"[NARRATOR] (calm) {LAW_INTRO}")
    add("[BREAK]")

    # ---- Where and when, and the passage ------------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Leviticus chapter twenty-one, at Sinai. This chapter is not for "
        "Israel in general. It is for the priests, the descendants of Aaron, the one family who could offer "
        "sacrifice. It covers whom a priest may marry, whom he may mourn, and, in our verses, who among them may "
        "serve at the altar. Keep the size of this in mind. It concerns a few hundred men of one family and one "
        "duty, not blind people as a whole.")
    ext(reader(bible, "Leviticus", 21, 16, 24))
    add("[NARRATOR] (calm) Hear what the passage is careful to say. He may not approach to offer the food of his "
        "God. He may not go near the veil or the altar. But he may eat the most holy food as well as the holy. He "
        "remains a priest and is fed as one. He does not perform the altar service. And the reason given is the "
        "holiness of the sanctuary, not the worth of the man. Many readers have still found it hard, and Brian's "
        "thoughts on it belong here as much as anyone's. We will come to them.")
    add("[BREAK]")

    # ---- The word: \"moom\" ------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Now the word. The Hebrew translated defect is \"moom.\" Strong's gives it as a "
        "blemish, physically or morally. The 1915 encyclopedia says it names no particular disease but any "
        "disfiguring mark, even scratches and scars, and from there, any moral fault. Listen to where else the "
        "Bible uses it. Here is Absalom, David's son.")
    ext(reader(bible, "2 Samuel", 14, 25, 25))
    add("[NARRATOR] (calm) Not a single flaw. That is \"moom\". And here is the bride in the Song of Solomon.")
    ext(reader(bible, "Song of Solomon", 4, 7, 7))
    add("[NARRATOR] (calm) No flaw. \"Moom\" again. So the word that keeps the blind priest from the altar is the word "
        "for what the most beautiful man and the most beloved woman in the Old Testament did not have. It is a word "
        "about appearance before it is a word about anything else. Hold that thought, because Henry will come back "
        "to it.")
    add("[NARRATOR] (calm) And here is the thing to notice above all. It is the same word in the very next chapter, "
        "for the animal that may not be put on the altar.")
    ext(reader(bible, "Leviticus", 22, 20, 20))
    add("[NARRATOR] (calm) The priest with a \"moom\" does not approach. The lamb with a \"moom\" is not accepted. The Law "
        "asked the same thing of the man who offered and of the thing he offered. And the encyclopedia follows the "
        "word all the way to its end, in the New Testament.")
    ext(reader(bible, "1 Peter", 1, 18, 19))
    add("[NARRATOR] (calm) A lamb without blemish or spot. The word that kept the blind priest from the altar is the "
        "word that describes the one who was offered on it.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Two more words from that list are worth stopping on.")
    add("[NARRATOR] (calm) The list opens with the word for blind: \"ih-vair.\" It is the plain, everyday word, the "
        "same one we heard in the stumbling block law. It means a man who cannot see.")
    add("[NARRATOR] (calm) Now look further down, to verse twenty, and the man who has an eye defect. The Hebrew there "
        "is \"teh-bal-lool.\" Strong's dictionary and the 1915 encyclopedia both explain it as a cataract: a white "
        "spot, a clouding in the eye. That man is not blind. He can see, but not clearly.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) So this one list names both: the man who cannot see at all, and the man whose sight is "
        "clouded. That matters, because the Bible almost never draws that line. Nearly everywhere else, a person is "
        "simply blind or not. Here, in the one law that limits what a blind person may do, the Law notices that "
        "sight comes in degrees.")
    add("[BREAK]")

    # ---- The old books: the three questions -----------------------------------------------------------------
    add("[NARRATOR] (calm) Now Brian's three questions, in order. First: what did a priest actually do? Most of it "
        "with his hands. Smith's dictionary lists the duties: keep the altar fire burning day and night, feed the "
        "lamp with oil, offer the morning and evening sacrifices, teach the law, and judge hard cases. Leviticus "
        "chapter one has the priests catch and sprinkle the blood, flay and cut up the animal, and lay the pieces "
        "on the fire. Touch, all of it. But some duties needed eyes. Leviticus thirteen has the priest look on a skin "
        "disease, again and again, and judge whether it is deeper than the skin. And burning the incense meant "
        "standing alone in the Holy Place and watching. Edersheim describes Zechariah's turn at it, in the first "
        "chapter of Luke, waiting until he saw the incense kindling.")
    add("[NARRATOR] (calm) Second: would a blind priest touch what he should not? Brian touches things all day to "
        "know what they are. Here is the surprise. The rules about touching holy things are for the Levites, not "
        "the priests. When the camp moved, Aaron's sons covered the ark and the vessels first, and only then could "
        "the Kohathites carry them, and they were told not to touch any holy thing, lest they die. The priests "
        "handled the holy things. The carriers were forbidden to. And Leviticus twenty-one keeps the blemished "
        "priest from exactly the two places where the fire and the handling were: the veil and the altar. No source "
        "on the shelf says a word about accidental touching by a man who cannot see. That worry is Brian's, and it "
        "is a good one, but the text does not share it.")
    add("[NARRATOR] (calm) Third: would one blind priest have been a burden on the rest? The numbers say no, and "
        "here is why.")
    add("[NARRATOR] (calm) The priests were divided into twenty-four groups, called courses. Each course served at "
        "the Temple for one week, then went home while the others took their turns. So each course came round about "
        "twice a year.")
    add("[NARRATOR] (calm) When a course was on duty, about fifty priests served each day, by Edersheim's count. And "
        "no one chose his own task. The jobs were handed out by lot, every morning. The greatest honour, burning the "
        "incense, came so rarely that a man could do it only once in his life. Zechariah, the father of John the "
        "Baptist, was at least sixty when his lot finally fell.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Now put one blind priest in that picture. He is one man among fifty, there two weeks a "
        "year. He is kept from just two places, the veil and the altar, and welcome everywhere else. In a system run "
        "by lot, where most men waited a lifetime for the best task, he would hardly have been noticed.")
    add("[BREAK]")

    # ---- The old books: why the rule at all -----------------------------------------------------------------
    add("[NARRATOR] (calm) Now the harder question, the one under Brian's three. Why the rule at all? Leviticus "
        "gives no reason beyond the holiness of the sanctuary. Here is Matthew Henry, in seventeen hundred and six, "
        "first on what the law protected.")
    add("[HENRY] (calm) The blemishes were such as they could not help, and therefore, though they might not work, "
        "they must not starve. Note, None must be abused for their natural infirmities.")
    add("[NARRATOR] (calm) And then Henry supplies a reason of his own, and it is not about the man.")
    add("[HENRY] (calm) But it was especially requisite that comely men should be chosen to minister about holy "
        "things, for the sake of the people, who were apt to judge according to outward appearance, and to think "
        "meanly of the service.")
    add("[NARRATOR] (calm) For the sake of the people, who judge by appearance. Notice that this is Henry's reason, "
        "not the Bible's. Leviticus itself says only that the sanctuary is holy. Henry is guessing at why, and his "
        "guess is about the crowd, not the priest.")
    add("[NARRATOR] (calm) And his guess fits the word. Remember Absalom, without a single flaw, and the bride in whom "
        "there was no flaw. \"Moom\" is a word about how a thing looks. Henry is saying the rule protected the "
        "people from their own habit of judging by the eye.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Josephus, writing in the first century, puts the law's two sides in a single sentence. The "
        "blemished priest keeps his share, but he does not go up to the altar.")
    add("[BOOKS] (calm) He ordered that the priest who had any blemish, should have his portion indeed among the "
        "priests, but he forbade him to ascend the altar, or to enter into the holy house.")
    add("[NARRATOR] (calm) The rule was still read literally a thousand years after Sinai.")
    add("[NARRATOR] (calm) Josephus tells a story from about forty years before Christ. Two men of the same royal "
        "family were fighting over Judea. One was Hyrcanus, an old man who had served as high priest. The other was "
        "Antigonus, who came back into the land with a foreign army behind him and took Hyrcanus prisoner.")
    add("[NARRATOR] (calm) But Antigonus had a fear. The people might rise up and make Hyrcanus their ruler again. So "
        "he did something that only makes sense if everyone knew this law. Here is Josephus.")
    add("[BOOKS] (calm) He cut off his ears, and thereby took care that the high priesthood should never come to him "
        "any more, because he was maimed, while the law required that this dignity should belong to none but such "
        "as had all their members entire.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Later rules went further than Leviticus. The 1915 encyclopedia says a priest blind even in "
        "one eye was not to pronounce the priestly blessing. Edersheim, describing the synagogue, says the blessing "
        "could not be given by those so blind as not to be able to discern daylight, and he gives the reason the "
        "rabbis gave.")
    add("[BOOKS] (calm) According to the Mishnah, they who pronounce the benediction must have no blemish on their "
        "hands, face, or feet, so as not to attract attention.")
    add("[NARRATOR] (calm) So as not to attract attention. The Talmud adds that if the townspeople were used to the "
        "man, he was allowed. The worry was that people would stare. It is a small window onto the real question, "
        "which was never the man's ability. It was what the people in front of him were used to. Brian is about "
        "to say that this has not changed.")
    add("[BREAK]")

    # ---- From Brian ---------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Brian, with the last word. His three questions answered, and then what he can speak to.")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add("[BREAK]")

    # ---- Close --------------------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Next time, the last of the four, and the one that is not about blind people at all: the "
        "blind animal and the altar. The same word, \"moom\", a market in the Temple, a prophet's test, and a look back "
        "over everything the Law said about the blind.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
