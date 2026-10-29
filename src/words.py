"""The word: for each Law page, the Hebrew word the law turns on, where else it appears, and what that does
to the law. Checked on every build against the tagged Hebrew text and Strong's dictionary (src/hebrew.py):
every verse listed under a word really uses that word.

Shape: slug -> list of words. Each word: the Strong's number, a plain spelling for the page and the voices,
the gloss (Strong's own words, shortened), the verses that use it, and the paragraphs that tell the story.
The English of every verse is the Berean Standard Bible, pulled in by the builder; nothing is retyped here.
"""

WORDS = {
    # ---- the stories of sight lost (October 2026) ----
    "isaac": [
        {"number": "H3543", "spelling": "kahah", "say": "kah-HAH",
         "gloss": "to be weak; of the eye, to be dim",
         "verses": [("Genesis", 27, 1), ("Deuteronomy", 34, 7), ("Job", 17, 7), ("Isaiah", 42, 4)],
         "text": [
             "Genesis does not say Isaac was blind. It says his eyes had grown weak, or dim: the verb kahah, which "
             "Strong's gives as to be weak, and of a light or an eye, to grow dim. It is the Bible's ordinary word for "
             "sight failing with age. The same verb is used of Moses to say the opposite, that at a hundred and twenty "
             "his eyes were not weak; Job uses it of eyes dimmed by grief; and Isaiah uses it of the Servant who will "
             "not grow weak. A form of the same root describes Eli's eyes in 1 Samuel 3. So the text puts Isaac among "
             "the old whose sight has gone, and leaves open how far it had gone; the story then turns on what he "
             "could not see."]},
        {"number": "H4959", "spelling": "mashash", "say": "mah-SHASH",
         "gloss": "to feel of; by implication, to grope",
         "verses": [("Genesis", 27, 12), ("Genesis", 27, 22), ("Deuteronomy", 28, 29), ("Job", 12, 25)],
         "text": [
             "The other word of the chapter is the one for what Isaac did with his hands. Jacob fears his father will "
             "feel him, and Isaac does: mashash, to feel over, and by extension to grope. Outside this chapter the "
             "word is mostly used of the blind groping, as in the curse of Deuteronomy 28, where people grope at noon "
             "as the blind grope in the dark. In Genesis 27 it is not groping. It is a careful man checking with the "
             "sense he trusts, and the one sense his family had prepared for."]},
    ],
    "jacob": [
        {"number": "H3513", "spelling": "kabed", "say": "kah-BAYD",
         "gloss": "to be heavy; of eyes or ears, dull",
         "verses": [("Genesis", 48, 10), ("Isaiah", 6, 10), ("Isaiah", 59, 1)],
         "text": [
             "Genesis uses a different word for Jacob's eyes than for his father's. Isaac's grew dim; Jacob's were "
             "kabed, heavy. It is the ordinary word for a heavy load, and the Bible uses it of eyes that are dull, ears "
             "that are dull, and hearts that are hard. The same root gives the word for glory, which is weight of a "
             "different kind. The Berean text's 'his eyesight was poor' is this word: eyes that had grown heavy with "
             "age, so that he could hardly see, though the next verses have him see two shapes and ask who they are."]},
        {"number": "H7919", "spelling": "sakal", "say": "sah-KAL",
         "gloss": "circumspect; to act wisely, with understanding",
         "verses": [("Genesis", 48, 14), ("1 Samuel", 18, 14), ("Psalm", 2, 10), ("Isaiah", 52, 13)],
         "text": [
             "The word for what Jacob did with his hands is not a word about hands at all. When he crossed them, "
             "Genesis says he did it sakal: the King James has 'guiding his hands wittingly', the Berean simply "
             "'crossing his hands'. Everywhere else the word means to act wisely, to prosper by understanding: David "
             "behaving wisely in all his ways, the kings of the earth told to be wise, the Servant who will act wisely. "
             "So the text answers Joseph before Joseph speaks. The blind man's hands were not confused. They were "
             "the wise part of the scene."]},
    ],
    "eli": [
        {"number": "H3544", "spelling": "keheh", "say": "kay-HEH",
         "gloss": "feeble, dim, faded",
         "verses": [("1 Samuel", 3, 2), ("Isaiah", 42, 3), ("Isaiah", 61, 3), ("Leviticus", 13, 39)],
         "text": [
             "Isaac's eyes were described with a verb, kahah, to grow dim. Eli's are described with the adjective "
             "from the same root, keheh: dim, faded, feeble. It is the word for a spot on the skin that has faded, for "
             "the smouldering wick the Servant will not put out, and for the faint spirit that is given a garment of "
             "praise. The picture is of something going out slowly, not gone. In chapter three Eli's eyes have begun "
             "to fade; by chapter four, at ninety-eight, the text says he could not see."]},
        {"number": "H6965", "spelling": "qum", "say": "koom",
         "gloss": "to rise, to stand; of eyes, to be set or fixed",
         "verses": [("1 Samuel", 4, 15), ("1 Kings", 14, 4)],
         "text": [
             "At the gate the text uses a stranger phrase: Eli's eyes 'stood', qum, the everyday verb for getting "
             "up. The Berean has 'his gaze was fixed'; the King James, 'his eyes were dim'. Only one other person in "
             "the Bible has eyes described this way, and he is in the next story: Ahijah, whose eyes were set because "
             "of his age. It is the Bible's picture of the fixed, unfocused look of eyes that no longer track what is "
             "in front of them, and it is used of two old men of Shiloh."]},
    ],
    "ahijah": [
        {"number": "H6965", "spelling": "qum", "say": "koom",
         "gloss": "to rise, to stand; of eyes, to be set or fixed",
         "verses": [("1 Kings", 14, 4), ("1 Samuel", 4, 15)],
         "text": [
             "Kings says Ahijah could not see because his eyes 'stood', qum, the common verb for rising up, used here "
             "of eyes that have set in place. The Berean gives it as 'his eyes were dim because of his age'. The only "
             "other eyes in the Bible described with this word are Eli's, in the same town, a century and more before. "
             "Shiloh had two blind old men in its story, and the text reaches for the same word for both."]},
        {"number": "H5234", "spelling": "nakar", "say": "nah-KAR",
         "gloss": "to scrutinize; to recognize, or in one form to disguise oneself",
         "verses": [("1 Kings", 14, 5), ("1 Kings", 14, 6), ("Genesis", 27, 23), ("Genesis", 37, 33), ("Genesis", 42, 8)],
         "text": [
             "The word for the queen's disguise is the word for recognizing. Nakar means to look closely and know "
             "someone; in one of its forms it turns inside out and means to make oneself unrecognizable, which is what "
             "the LORD tells Ahijah she will do, and what Ahijah names at the door. It is the word used when Isaac did "
             "not recognize Jacob, when Jacob recognized Joseph's robe, and when Joseph recognized his brothers and "
             "they did not recognize him. The whole family history of this series runs through it, and here, at its "
             "end, the blind man neither recognizes nor needs to. He is told, before her feet reach the door."]},
    ],
    "zedekiah": [
        {"number": "H5786", "spelling": "avar", "say": "ah-VAR",
         "gloss": "to blind",
         "verses": [("2 Kings", 25, 7), ("Jeremiah", 39, 7), ("Jeremiah", 52, 11), ("Exodus", 23, 8), ("Deuteronomy", 16, 19)],
         "text": [
             "Three times the Bible tells this and three times it uses the same verb: avar, to blind, the root under "
             "ivver, the plain word for a blind man. Zedekiah is the only person in the Old Testament of whom the "
             "verb is used literally. Its other two uses are in the Law, and they are about bribes: a bribe blinds "
             "those who see, a bribe blinds the eyes of the wise. The word that describes what Babylon did to the king "
             "is the word Moses used for what a gift in the wrong hand does to a judge."]},
        {"number": "H5178", "spelling": "nechosheth", "say": "neh-KHO-sheth",
         "gloss": "copper, hence something made of it: a fetter",
         "verses": [("2 Kings", 25, 7), ("Jeremiah", 39, 7), ("Jeremiah", 52, 11), ("Judges", 16, 21)],
         "text": [
             "The fetters are named in all three accounts, and the word, in its paired form, means two pieces of "
             "bronze: shackles. There is one other man in the Bible bound in the same word after being blinded, and "
             "he is Samson. The two men the Bible says were blinded by their enemies were both led away in bronze, a "
             "king and a judge, four hundred years apart."]},
    ],
    "samson": [
        {"number": "H5365", "spelling": "naqar", "say": "nah-KAR",
         "gloss": "to bore, to dig out, to quarry",
         "verses": [("Judges", 16, 21), ("1 Samuel", 11, 2), ("Isaiah", 51, 1), ("Job", 30, 17)],
         "text": [
             "The verb for what the Philistines did is naqar: to bore or dig out, the word for quarrying stone from "
             "a rock. Isaiah uses it for the quarry Israel was hewn from; Job for pain boring into his bones. The only "
             "other eyes it is used of are the right eyes Nahash the Ammonite demanded from the men of Jabesh-gilead, "
             "a story also on this site. It is a workman's word, and the text does not soften it."]},
        {"number": "H2912", "spelling": "tachan", "say": "tah-KHAN",
         "gloss": "to grind meal",
         "verses": [("Judges", 16, 21), ("Exodus", 32, 20), ("Isaiah", 47, 2), ("Job", 31, 10)],
         "text": [
             "What Samson did in the prison was tachan, to grind grain, the daily work of a hand mill. Elsewhere it is "
             "Moses grinding the golden calf to powder, and the daughter of Babylon told to take millstones and grind "
             "as a sign of her humiliation. Job swears that if he has sinned, his wife may grind for another man. It "
             "was the lowest household labour, usually done by women or slaves, and the strongest man in Israel was "
             "put to it, by touch, in the dark."]},
    ],
    "stumbling-block": [
        {"number": "H4383", "spelling": "mikshol", "say": "mik-SHOLE",
         "gloss": "a stumbling-block, literally or figuratively",
         "from": "The dictionary derives it from a verb meaning to totter or fall.",
         "verses": [("Leviticus", 19, 14), ("Jeremiah", 6, 21), ("Ezekiel", 3, 20), ("Isaiah", 8, 14),
                    ("Psalm", 119, 165)],
         "text": [
             "The word translated stumbling block is mikshol. Strong's dictionary gives it as a stumbling-block, "
             "literally or figuratively, and derives it from a verb meaning to totter or fall. The 1915 encyclopedia "
             "says its literal sense is an object which causes one to stumble or fall, and that Leviticus 19:14 is the "
             "one place the word is plainly literal. Everywhere else, it says, the word is used for what brings "
             "material ruin or spiritual downfall.",
             "Brian asked whether this is the stumble he knows, a foot catching a curb and a body that catches itself, "
             "or the fall he sees in other blind people, who go down and are hurt. The word's company answers. In "
             "Jeremiah, God lays stumbling blocks before the people, and friends and neighbours perish. In Ezekiel, "
             "a stumbling block is put before a man, and he will die. In Isaiah, the stone of stumbling is one that "
             "people fall over and are broken on. Only the psalm uses it gently, and there it is the thing that "
             "cannot happen to those who love God's law. On the words alone, the law is about the fall, and in the "
             "word's other uses, about worse than a fall. It is written for the people who do not catch themselves.",
             "Two more words in the same verse are worth hearing. The blind man is ivver, the ordinary word for "
             "blind, and the deaf man is cheresh. And the reason given, you shall fear your God, uses yare, the "
             "common word for fear and reverence. Hold on to that one. It is the word Malachi uses at the very end "
             "of the Old Testament's laws about the blind, on the page about blind animals: My name is to be feared.",
             "The curse in Deuteronomy 27:18 uses a different verb for what is done to the blind man. He is made to "
             "wander: shagah, to stray or be led astray, the word used elsewhere for going wrong without knowing it. "
             "That is Josephus's road again, and the joke played on someone who will not know who played it."]},
    ],
    "servant-blinded": [
        {"number": "H5869", "spelling": "ayin", "say": "AH-yin",
         "gloss": "an eye; by analogy, a fountain, as the eye of the landscape",
         "verses": [("Exodus", 21, 26), ("Judges", 16, 21), ("2 Kings", 25, 7)],
         "text": [
             "The word for eye is ayin. Strong's adds a detail that is easy to miss in English: the same word means "
             "a spring of water, the eye of the landscape. The 1915 encyclopedia calls the eye the lamp of the body, "
             "and goes on to say that putting out an enemy's eyes was a cruel custom among the nations around Israel, "
             "because it shattered a man's power most effectually. It gives three examples, and two of them are "
             "stories on this site: Samson, whose eyes the Philistines gouged out at Gaza, and Zedekiah, the last king "
             "of Judah, blinded at Riblah after watching his sons die. This law stands between those two men. It is "
             "the one place where the Law puts a price on an eye, and the price is paid to the man who lost it."]},
        {"number": "H2670", "spelling": "chophshi", "say": "khof-SHEE",
         "gloss": "exempt from bondage, tax or care",
         "verses": [("Exodus", 21, 26), ("Exodus", 21, 2), ("Deuteronomy", 15, 12), ("Jeremiah", 34, 9),
                    ("Isaiah", 58, 6)],
         "text": [
             "The word for free is chophshi, which Strong's glosses as exempt from bondage, tax or care. English has "
             "two kinds of free, free as in no charge and free as in no chains, and chophshi holds both: a man who is "
             "chophshi owes nothing more and belongs to no one. Read the law with that in mind. The master does not "
             "hand the servant money for the eye. He pays with the man himself, and whatever time the servant still "
             "owed is cancelled. Nor is this a new word made up for one law. It is the "
             "same word used a few verses earlier, in Exodus 21:2, for the Hebrew servant who goes free in the "
             "seventh year, and again in Deuteronomy 15:12, and in Jeremiah 34, where a king's broken promise to "
             "free the servants brings judgment on Jerusalem. Isaiah 58 uses it for the fast God chooses: to set the "
             "oppressed free. So the law does not invent a new kind of release for the blinded servant. It gives him "
             "the release the Law already knew, the seventh-year freedom, at once. An eye bought what six years "
             "of service bought."]},
        {"number": "H1865", "spelling": "deror", "say": "deh-RORE",
         "gloss": "freedom; liberty",
         "verses": [("Leviticus", 25, 10), ("Isaiah", 61, 1), ("Jeremiah", 34, 8), ("Jeremiah", 34, 17)],
         "text": [
             "The Law knew a second release besides the seventh year. Every fiftieth year was the Jubilee, when liberty "
             "was proclaimed in the land and anyone who had sold himself went home with his children, however long he "
             "had served. Its word for liberty is deror, not the servant's chophshi, and it is the word Isaiah uses for "
             "what the Anointed One comes to proclaim to the captives, in the passage Jesus read at Nazareth. Jeremiah "
             "34 holds both words: Zedekiah's people proclaimed deror and freed their servants, then took them back, "
             "and God answered with a freedom of His own, to fall by sword, plague and famine. The blinded servant's "
             "release did not wait for the seventh year or the fiftieth. It came that day."]},
    ],
    "priest": [
        {"number": "H3971", "spelling": "mum", "say": "moom",
         "gloss": "a blemish, physically or morally",
         "verses": [("Leviticus", 21, 17), ("Leviticus", 21, 18), ("Leviticus", 21, 21), ("Leviticus", 21, 23),
                    ("Leviticus", 22, 20), ("Deuteronomy", 17, 1), ("2 Samuel", 14, 25), ("Song of Solomon", 4, 7)],
         "text": [
             "The word translated defect is mum. Strong's gives it as a blemish, physically or morally. The 1915 "
             "encyclopedia says it names no particular disease but any disfiguring mark, even scratches and scars, "
             "and from there any moral fault. It is the word for what Absalom did not have, from the sole of his foot "
             "to the top of his head, and for what the bride in the Song of Solomon does not have: a single flaw.",
             "Here is the thing to notice. It is the same word in the next chapter, for the animal that may not be "
             "put on the altar. The priest with a mum does not approach; the lamb with a mum is not accepted. The Law "
             "asked the same thing of the man who offered and of the thing offered. The encyclopedia follows the word "
             "to its end: in the New Testament, Christ is presented as the pure and acceptable sacrifice, a lamb "
             "without blemish and without spot. The word that kept the blind priest from the altar is the word that "
             "describes the one who was offered on it.",
             "The list in Leviticus 21 opens with ivver, blind, the same ordinary word as in the stumbling block law. "
             "And it holds a second word about eyes. In verse 20 the man with an eye defect has a teballul, which "
             "Strong's and the encyclopedia both give as a cataract, a white spot in the eye. So the list reached past "
             "the man who could not see at all to the man whose sight was clouded. The spectrum of blindness, which "
             "the page on what blind means says the Bible rarely marks, is marked here, in the one law that limits "
             "what a blind person may do."]},
    ],
    "blind-animals": [
        {"number": "H8549", "spelling": "tamim", "say": "tah-MEEM",
         "gloss": "entire; whole, complete",
         "verses": [("Leviticus", 22, 19), ("Leviticus", 22, 21), ("Exodus", 12, 5), ("Deuteronomy", 18, 13),
                    ("Psalm", 15, 2)],
         "text": [
             "The law has a positive word as well as a negative one. The animal must be tamim, which the Berean text gives "
             "as unblemished and Strong's as entire, whole, complete. It is the Passover lamb's word in Exodus 12. And it "
             "is a word the Bible uses of people far more often than of animals. You must be tamim before the LORD your "
             "God, says Deuteronomy, where the English is blameless. The man who may dwell on God's holy hill walks "
             "tamim, says the psalm, where the English is with integrity. So the thing the altar asked of a lamb is the "
             "thing God asks of a person's walk, and in neither case does it have anything to do with eyes. A blind man "
             "can walk tamim. That is the whole of the Law's answer to the word defect."]},
        {"number": "H3971", "spelling": "mum", "say": "moom",
         "gloss": "a blemish, physically or morally",
         "verses": [("Leviticus", 22, 20), ("Leviticus", 22, 21), ("Deuteronomy", 15, 21), ("Deuteronomy", 17, 1),
                    ("Leviticus", 21, 17)],
         "text": [
             "The word for defect in these laws is mum, a blemish, and it is the word the previous page turns on. "
             "The animal that is not accepted and the priest who may not approach are described by one word. That "
             "is the plainest sign that this rule is about the gift and not about blindness: the Law used the same "
             "measure for the lamb and for the man, and in the end, the encyclopedia notes, for Christ, the lamb "
             "without blemish."]},
        {"number": "H5788", "spelling": "avveret", "say": "av-VEH-ret",
         "gloss": "blindness",
         "verses": [("Leviticus", 22, 22)],
         "text": [
             "Leviticus 22:22 does not say a blind animal; it says an animal with blindness, avveret, a noun formed "
             "from ivver. Blindness is listed as a thing an animal has, beside injury and sores. Deuteronomy 15:21 and "
             "Malachi 1:8 use the plain adjective, ivver, the same word as the blind man of Leviticus 19:14 and the "
             "blind priest of Leviticus 21. One word runs through all four of these pages."]},
        {"number": "H3372", "spelling": "yare", "say": "yah-RAY",
         "gloss": "to fear; morally, to revere",
         "verses": [("Malachi", 1, 14), ("Leviticus", 19, 14)],
         "text": [
             "Malachi closes with a word that opened this section. The deceiver who vows a sound animal and gives a "
             "blemished one is cursed, for I am a great King, and My name is to be feared. That is yare, to fear or "
             "revere, the word of the stumbling block law: you shall fear your God. The first law about the blind and "
             "the last both rest on it. Nobody would see the stone placed in the road; nobody at the altar could tell, "
             "once the animal was offered, whether a better one had been kept back. Both laws were written for the "
             "wrong that no one catches, and both give the same reason to keep them."]},
    ],
}
