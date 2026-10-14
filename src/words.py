"""The word: for each Law page, the Hebrew word the law turns on, where else it appears, and what that does
to the law. Checked on every build against the tagged Hebrew text and Strong's dictionary (src/hebrew.py):
every verse listed under a word really uses that word.

Shape: slug -> list of words. Each word: the Strong's number, a plain spelling for the page and the voices,
the gloss (Strong's own words, shortened), the verses that use it, and the paragraphs that tell the story.
The English of every verse is the Berean Standard Bible, pulled in by the builder; nothing is retyped here.
"""

WORDS = {
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
             "The word for free is chophshi, which Strong's glosses as exempt from bondage, tax or care. It is the "
             "same word used a few verses earlier, in Exodus 21:2, for the Hebrew servant who goes free in the "
             "seventh year, and again in Deuteronomy 15:12, and in Jeremiah 34, where a king's broken promise to "
             "free the servants brings judgment on Jerusalem. Isaiah 58 uses it for the fast God chooses: to set the "
             "oppressed free. So the law does not invent a new kind of release for the blinded servant. It gives him "
             "the release the Law already knew, the seventh-year freedom, at once. An eye bought what six years "
             "of service bought."]},
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
