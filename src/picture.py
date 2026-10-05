"""Blindness as a picture: the verses where Scripture uses blindness to mean
something else.

Brian's instructions (4 October 2026): do all three readings on every page,
read the hard words plainly with no softening, and leave the Other voices
slot open for his pastor, who suggested this study.

Each page carries:
  says     the plain meaning of the figure, from the text and its context
  assumes  what the figure takes for granted about blind people
  who      who is called blind in these verses, and who is not
The pages share the stories' shape (full passage, slots, place and time).
"""
from __future__ import annotations

SECTION = ("Blindness as a picture",
           "The Bible uses blindness most often as a picture of something else: not knowing, not believing, being "
           "misled, being judged. A blind reader knows that before opening the book. These pages read those verses "
           "anyway, plainly, and ask three things of each: what the picture means, what it takes for granted about "
           "blind people, and who is actually called blind.")

OPENING = {
    "slug": "index", "title": "Blindness as a picture",
    "intro": [
        "Of the 86 verses in the Bible that use the word blind, 36 use it as a figure of speech, and six more "
        "are promises that may be meant either way. This is the word's most common use, and the one a blind reader "
        "hears differently from everyone else. Every one of these verses makes blindness stand for something wrong.",
        "These pages do not soften that. Where Jesus says \"blind fools,\" the page says so. What the pages add is "
        "three questions put to every passage. What does the picture mean? What does it assume about blind "
        "people, and does the rest of Scripture agree? And who gets called blind, and who never does? The answer to "
        "the last one turns out to be the most interesting thing in this part of the Bible.",
        "The idea for this study came from Brian's pastor, John. The Other voices slot on each page is waiting for "
        "him.",
    ],
}

PICTURE_PAGES = [
    {
        "slug": "blind-guides", "section": "picture", "title": "Blind guides",
        "passages": [("Matthew", 15, 12, 14), ("Matthew", 23, 13, 28), ("Luke", 6, 39, 42),
                     ("Isaiah", 56, 9, 11), ("Romans", 2, 17, 21)],
        "around": "Jesus's sharpest uses of the word all fall on religious teachers. In Matthew 15 the Pharisees have "
                  "just objected to His disciples eating with unwashed hands. In Matthew 23 He pronounces seven woes on "
                  "the scribes and Pharisees. Luke's saying sits among teachings on judging others. Isaiah had used the "
                  "same picture of Israel's watchmen six centuries earlier, and Paul turns it on anyone who is sure he "
                  "is \"a guide for the blind.\"",
        "says": "A blind guide is a leader who cannot see where he is taking people, so both fall into the pit. Jesus "
                "calls the Pharisees blind guides, blind fools, blind men, blind Pharisee, for straining out a gnat and "
                "swallowing a camel, for cleaning the outside of the cup and not the inside. Isaiah's watchmen are blind "
                "and asleep while the beasts come. Paul's point is that a man who is certain he can guide others may be "
                "the one who most needs to look at himself.",
        "assumes": "The figure assumes that a blind man cannot guide, that he has no business leading anyone anywhere. "
                   "That is the picture everyone in the crowd shared, and Jesus used it because it worked. The rest of "
                   "Scripture complicates it: blind Ahijah told the disguised queen who she was and what was coming, "
                   "blind Eli recognized the voice of God when the sighted boy did not, and Jacob, nearly blind, "
                   "crossed his hands on purpose while his sighted son tried to correct him. The figure is about sight "
                   "as knowledge. It is not a judgment on blind people, and it has often been read as one.",
        "who": "Every person called a blind guide in these passages could see. The scribes and Pharisees, the watchmen "
               "of Israel, the man who boasts of the law. Not one blind person is called a blind guide anywhere in "
               "Scripture. The insult is reserved for the sighted who will not look.",
        "brian": [
            "It does not trouble me when people use the word blind for someone cut off from the truth. I say \"See you "
            "later\" and \"It's good to see you\" all the time, with no physical vision at all. It is a statement of "
            "recognition, and recognition can be done in a lot of ways.",
            "I find it interesting to think about flatly disqualifying blind people from leading other blind people. "
            "We cannot cover every condition, but if we weigh what conditions were like back then, the statement is "
            "mostly true. I lead other blind people around all the time myself, but I do it with a white cane in my "
            "hand telling me what is around us.",
            "I also think the Bible's \"blind\" usually gets read as total blindness, like mine, rather than visual "
            "impairment. I know many people in our group whom I consider blind, across a very wide spectrum, who do "
            "not even need a cane to travel. Believe me, their hardships are just as real.",
        ],
    },
    {
        "slug": "eyes-that-cannot-see", "section": "picture", "title": "Eyes that cannot see",
        "passages": [("John", 9, 39, 41), ("John", 12, 37, 41), ("Romans", 11, 7, 10), ("2 Corinthians", 4, 3, 6),
                     ("2 Peter", 1, 5, 9), ("1 John", 2, 9, 11)],
        "around": "These are the verses where blindness stands for unbelief or a hardened heart. John 9 ends with "
                  "Jesus turning the healing of a blind man into a judgment on the sighted men who questioned him. John "
                  "12 and Romans 11 quote Isaiah on eyes that cannot see. Paul in 2 Corinthians speaks of minds blinded "
                  "by \"the god of this age.\" Peter and John use blindness for a believer who has stopped growing or "
                  "who hates his brother.",
        "says": "To be spiritually blind is to have eyes and not see what is in front of you: the signs Jesus did, the "
                "light of the gospel, the brother you hate. Some of these verses say God Himself blinds, as judgment on "
                "people who would not believe; others say the devil does; Peter says a Christian can do it to himself by "
                "neglect. In every case the blindness is a refusal before it is a condition.",
        "assumes": "The figure assumes that not seeing is a failure. Physical blindness is not a failure of anything; "
                   "spiritual blindness, in these verses, is always a failure of will. The two uses share a word and "
                   "nothing else. John 9 says exactly this: the man who was born unable to see is not the one who is "
                   "blind at the end of the chapter.",
        "who": "John 9:39 to 41 is the hinge of the whole subject. Jesus says He came \"so that the blind may see and "
               "those who see may become blind.\" The Pharisees ask, \"Are we blind too?\" and He answers that if they "
               "were blind they would not be guilty, but because they claim to see, their guilt remains. The man born "
               "blind is never called spiritually blind. The men with working eyes are. Across these six passages the "
               "word falls on unbelievers, hardened Israel, the perishing, the neglectful and the hateful, and never "
               "once on a person who cannot see.",
    },
    {
        "slug": "gods-people-called-blind", "section": "picture", "title": "God's own people called blind",
        "passages": [("Isaiah", 29, 9, 14), ("Isaiah", 42, 16, 20), ("Isaiah", 43, 8, 10), ("Revelation", 3, 14, 18)],
        "around": "Isaiah speaks to a people who worship with their lips while their hearts are far away. In chapter 42 "
                  "the promise to lead the blind sits two verses from the accusation that God's own servant is blind. "
                  "Revelation 3 is a letter to a comfortable church.",
        "says": "God calls His own people blind and deaf: they have eyes but do not watch, ears but do not hear. The "
                "church at Laodicea says, \"I am rich, I need nothing,\" and is told it is \"wretched, pitiful, poor, "
                "blind, and naked,\" and offered salve for its eyes. The blindness here is self-satisfaction: not seeing "
                "because you are sure there is nothing to see.",
        "assumes": "The figure assumes that blindness is a condition you can have without knowing it, which is true of "
                   "the spiritual kind and false of the physical. A blind man knows. Laodicea did not. The picture "
                   "works precisely because the hearers would have thought it obvious that a blind man knows he is "
                   "blind, and would have been stung to be told they did not.",
        "who": "The people called blind here are God's covenant partner, His servant, His witnesses, His church. The "
               "word is not aimed outward at pagans or unbelievers but inward, at the people who had the Scriptures "
               "and the Temple and the salve within reach. Isaiah 42 puts the two uses side by side: God will lead the "
               "blind by a way they do not know, and in the next breath asks who is blind but His own servant. The "
               "blind He leads and the blind He rebukes are not the same people.",
    },
    {
        "slug": "like-the-blind", "section": "picture", "title": "Like the blind",
        "passages": [("Deuteronomy", 28, 28, 29), ("Isaiah", 59, 9, 10), ("Lamentations", 4, 13, 15), ("Zephaniah", 1, 17, 17)],
        "around": "Four passages compare a people under judgment to blind people moving: groping at noon, feeling along "
                  "a wall, wandering the streets, walking like the blind. Deuteronomy's is a curse for breaking the "
                  "covenant; the others describe Jerusalem's fall or the day of the LORD.",
        "says": "These are similes, not statements about anyone's eyes. Judgment feels like this: you cannot find your "
                "way, you stumble in broad daylight, you feel along the wall of a city you used to know. The pictures "
                "are drawn from watching blind people move, and they are exact: the hand on the wall, the slow step, "
                "the midday that is no help.",
        "assumes": "The figure assumes that to move like a blind person is to be lost, slow and exposed, and it assumes "
                   "the writer has watched blind people do these things. The observation is accurate as far as it goes; "
                   "a blind reader will recognize the wall. What it leaves out is that the blind man feeling along the "
                   "wall knows where he is going. The people in these verses do not.",
        "who": "No blind person is the subject of any of these verses. The subjects are a nation under curse, a city "
               "whose prophets shed blood, mankind on the day of the LORD. The blind appear only as the image, which "
               "means they were familiar enough in the streets to serve as one.",
    },
    {
        "slug": "eyes-dim-with-grief", "section": "picture", "title": "Eyes dim with grief",
        "passages": [("Job", 17, 7, 7), ("Psalm", 6, 6, 7), ("Psalm", 38, 9, 10), ("Psalm", 88, 8, 9), ("Lamentations", 5, 15, 17)],
        "around": "Five laments, from Job, three psalms and the end of Lamentations, describe eyes failing from "
                  "weeping, waiting and grief.",
        "says": "These are the Bible's words for crying until you cannot see, and for the dimness that comes of long "
                "sorrow and long waiting. \"My eyes grow dim with grief. I call to You daily.\" They are not about "
                "blindness as a judgment or a figure of unbelief. They are about what grief does to the body.",
        "assumes": "Nothing about blind people, and that is why they belong here. They assume only that eyes and "
                   "sorrow are connected, which anyone who has wept knows. Some readers hear in them a possible "
                   "physical dimming as well; the catalog marks these as uncertain for that reason.",
        "who": "The speakers are the sufferers themselves: Job, David, the psalmist, the survivors of Jerusalem. These "
               "are the only verses in the catalog where the one whose eyes fail is also the one praying, and still "
               "praying.",
    },
    {
        "slug": "bribes-and-curses", "section": "picture", "title": "Bribes and curses",
        "passages": [("Exodus", 23, 6, 8), ("Deuteronomy", 16, 18, 20), ("Zechariah", 11, 15, 17), ("Zechariah", 12, 4, 4)],
        "around": "Two laws for judges say that a bribe blinds. Two oracles in Zechariah use blinding as a curse: on a "
                  "worthless shepherd, and on the horses of the nations that attack Jerusalem.",
        "says": "A bribe \"blinds those who see\": a judge who takes money stops seeing the case in front of him. The "
                "shepherd who deserts his flock is cursed with a withered arm and a blinded right eye, the eye a man "
                "aimed with. The horses are struck with blindness in battle, as armies were struck in 2 Kings 6.",
        "assumes": "That blinding is a disabling and a disgrace, which is how the ancient world used it on conquered "
                   "enemies and failed kings. The bribe verses assume something subtler: that a sighted man can be made "
                   "not to see by his own choice, and that this is worse than not seeing.",
        "who": "Judges who take bribes, a false shepherd, war horses. The curse of blindness in these verses falls on "
               "the powerful and the armed, never on the weak.",
    },
    {
        "slug": "eyes-opened", "section": "picture", "title": "The eyes of the blind will be opened",
        "passages": [("Psalm", 146, 7, 9), ("Isaiah", 29, 18, 19), ("Isaiah", 35, 4, 6), ("Isaiah", 42, 6, 7),
                     ("Isaiah", 42, 16, 16), ("Luke", 4, 16, 21)],
        "around": "The promises. The psalm lists opening the eyes of the blind among God's acts of care for the "
                  "oppressed, the hungry and the prisoner. Isaiah repeats it as a sign of the day of salvation and as "
                  "the servant's task. Jesus read Isaiah's words aloud in Nazareth and said they were fulfilled.",
        "says": "God opens the eyes of the blind. Whether Isaiah meant eyes or understanding is a question the text "
                "leaves open, and Jesus answered it both ways at once: He healed blind people, and He named the healing "
                "as the sign that the promise had come. Matthew 11 puts \"the blind receive sight\" first on the list "
                "of proofs.",
        "assumes": "The promise assumes that blindness is something God intends to undo, which cuts both ways for a "
                   "blind reader: it names the condition as part of a broken world, and it names the blind first among "
                   "those God remembers. The psalm's company is telling. The blind stand with the bowed down, the "
                   "hungry, the prisoner and the stranger: people God is for.",
        "who": "Here, finally, the word falls on blind people and means them. The promise is to those who cannot see, "
               "and Jesus kept it to actual men by actual roads. Isaiah 42:16 adds a second promise that is easy to "
               "miss: not sight, but a guide. \"I will lead the blind by a way they did not know.\" For a reader who has "
               "not been healed, that is the verse in this group that is addressed to him.",
        "brian": [
            "Isaiah 42:16. So many thoughts here. We have to be willing to be led sometimes. Every blind person needs "
            "to hear these words. For me personally, He has led me to places I never dreamed I would go.",
            "This is part of why I count blindness among the greatest gifts God has given me, behind my salvation and "
            "my wife Barb. Daily I have to rely on Him for so many obvious needs, let alone the things everyone takes "
            "for granted.",
        ],
    },
]


def by_section() -> list[dict]:
    return PICTURE_PAGES


# ---- the place and the time, from the reference shelf (edited in
# src/write_picture.py, evidence in picture_candidates.json)
import json as _json
from pathlib import Path as _Path

_PC = _Path(__file__).resolve().parents[1] / "data" / "reference" / "picture.json"
if _PC.exists():
    _extra = _json.loads(_PC.read_text(encoding="utf-8"))
    for _page in PICTURE_PAGES:
        for _item in _extra.get(_page["slug"], []):
            _page.setdefault("place_and_time", []).append({"text": _item["text"], "source": _item["source"]})
