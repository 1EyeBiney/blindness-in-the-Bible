"""Context pages beyond the stories: the law, living blind in each setting
Scripture shows, and Brian's verse.

Each page has the same bones as a story. `passages` are quoted in full.
`around` and `says` come from the text and its near context alone.
`notice` is what the passage may tell us about life at the time; it is a
reading, worded as one. `place_and_time` is filled from the reference
shelf (data/reference/law_and_life.json) with a source on every item.
`brian` holds Brian's own words when he gives them, and `voices` holds
other people's answers to the same question; both start empty and the
page shows an open slot until they are filled.
"""
from __future__ import annotations

SECTIONS = {
    "law": ("The law", "What God commanded about the blind. A law is evidence of a problem: nobody forbids what no one "
                       "is doing. Read that way, these verses are a window into how blind people were being treated."),
    "life": ("Living blind, then", "What daily life would have been like for a blind person in each kind of place "
                                   "Scripture shows. Written from what the text says and what the reference shelf "
                                   "adds, with room for the people who know: Brian and others who live without sight."),
}

LAW_PAGES = [
    {
        "slug": "stumbling-block", "section": "law", "title": "Do not put a stumbling block before the blind",
        "passages": [("Leviticus", 19, 9, 18), ("Deuteronomy", 27, 11, 19)],
        "around": "Leviticus 19 is a chapter of commands about ordinary life, given to the whole assembly of Israel at "
                  "Sinai. The verses around this one concern leaving gleanings for the poor, paying wages on time, "
                  "honest courts and loving your neighbor. Deuteronomy 27 belongs to a ceremony Moses commanded for "
                  "the day Israel crossed the Jordan: the tribes were to stand on two mountains while the Levites "
                  "called out twelve curses and all the people answered Amen.",
        "says": "The first law pairs the deaf and the blind: you must not curse one or trip the other, and the reason "
                "given is \"you shall fear your God.\" The second is a curse, spoken aloud by a whole nation, on "
                "anyone who lets a blind man wander off the road.",
        "notice": "Both wrongs are ones the victim cannot catch. A deaf man does not hear the curse; a blind man does "
                  "not see who moved the stone or who watched him walk the wrong way. That is why the first law "
                  "appeals to the fear of God rather than to any court: no witness would come forward, so only God "
                  "sees. The second law is among curses on secret murder, moving a boundary stone and cheating the "
                  "fatherless, which suggests that misleading a blind traveller was counted among the serious, "
                  "hidden cruelties. Laws like these are not written against things nobody does.",
        "brian": [
            "It doesn't look like Hammurabi's code has anything about the treatment of the blind. So is the Bible the "
            "first recorded anything that addresses the blind? And when was Hammurabi's code written compared with "
            "what Moses was doing in Leviticus and Deuteronomy?",
        ],
    },
    {
        "slug": "servant-blinded", "section": "law", "title": "The servant blinded by his master",
        "passages": [("Exodus", 21, 20, 27)],
        "around": "These laws follow the Ten Commandments in Exodus and deal with injuries: a servant beaten to death, "
                  "a pregnant woman struck in a fight, and the rule of equal measure, \"eye for eye, tooth for tooth.\"",
        "says": "If a master strikes a servant, male or female, and destroys an eye, the servant goes free. The eye "
                "is the price of freedom. The next verse says the same of a tooth.",
        "notice": "Two things stand out. The law assumes masters did strike servants, and that eyes were lost that "
                  "way. And it does not apply \"eye for eye\" to the master; instead the injured servant is set free. "
                  "Whether that was more or less protection than a slave had under neighboring law codes is a "
                  "question the reference shelf can help with, and the place-and-time section below takes it up.",
    },
    {
        "slug": "priest", "section": "law", "title": "The blind priest",
        "passages": [("Leviticus", 21, 16, 24)],
        "around": "Leviticus 21 sets rules for the priests, Aaron's descendants, who alone could offer sacrifice. The "
                  "chapter covers whom they may marry, whom they may mourn, and here, who among them may serve at "
                  "the altar.",
        "says": "A descendant of Aaron with a lasting physical defect, and blindness heads the list, may not approach "
                "to offer the food of his God or go near the veil. But the passage is careful to add that he may "
                "still eat the holy food, the most holy as well as the holy. He remains a priest and is fed as one; "
                "he does not perform the altar service.",
        "notice": "This is the one law that limits what a blind person may do, and it is worth reading exactly. It "
                  "concerns a few hundred men of one family and one duty, not blind people in general. It keeps the "
                  "blind priest inside the priesthood and at its table. And the reason given is about the holiness of "
                  "the sanctuary, not about the worth of the man. Many readers have still found it hard, and Brian's "
                  "thoughts on it belong here more than anyone's.",
        "brian": [
            "I need to know more about priestly duties. Would a blind priest accidentally touch things he should not? "
            "I have to touch things all the time to figure out what they are; would that factor in? And would trying "
            "to let the blind priest fit in have been a hindrance to the rest of the Levites?",
        ],
    },
    {
        "slug": "blind-animals", "section": "law", "title": "Blind animals and the altar",
        "passages": [("Leviticus", 22, 17, 25), ("Deuteronomy", 15, 19, 23), ("Malachi", 1, 6, 14)],
        "around": "Leviticus 22 gives the rules for what may be offered; Deuteronomy 15 applies them to the firstborn "
                  "of the flock, which belonged to God. Malachi, the last book of the Old Testament, speaks to priests "
                  "a thousand years later who were offering blind, lame and sick animals and calling the LORD's table "
                  "contemptible.",
        "says": "An animal that is blind, injured or diseased is not to be put on the altar. A blind firstborn is not "
                "sacrificed but eaten at home like ordinary meat. Malachi's test is blunt: try giving an animal like "
                "that to your governor and see whether he is pleased.",
        "notice": "These laws are about gifts to God, not about blind people, and they belong here only so the whole "
                  "list is honest. The principle is that God is given the best, not the leftover. Malachi shows what "
                  "happened when the rule was ignored: the blind animal became the sign of a gift given with contempt.",
    },
]

LIFE_PAGES = [
    {
        "slug": "camp", "section": "life", "title": "In a herding camp",
        "question": "What would have worried a blind person most, living in a family that moved with its flocks "
                    "between camps, as Isaac's did?",
        "passages": [("Genesis", 27, 1, 4), ("Genesis", 48, 8, 12)],
        "around": "Isaac and Jacob lived in tents and moved with their herds. Household and workplace were the same "
                  "camp, and the people around a blind man were his own family and servants.",
        "says": "Both blind patriarchs are shown at home, in their tents, surrounded by family. Isaac sends for Esau "
                "and is served a meal; Jacob is brought his grandsons and embraces them. Neither is described leaving "
                "the camp. Both are deceived or doubted by the people closest to them, and both still exercise the "
                "authority of the head of the family: the blessing is theirs to give.",
        "notice": "A camp has no fixed streets to learn, and it moves. Water, fire, animals and tent ropes are "
                  "everywhere. Everything a blind elder needed came through other hands. The text shows the two "
                  "sides of that: care, and the chance to take advantage. And their loss of usable vision did not "
                  "remove their responsibilities as heads of the family.",
        "brian": [
            "It troubles me greatly when things are not where I expect to find them, and it is worse when something "
            "has been moved, usually by accident. I can't imagine trying to learn where everything was in my "
            "three-bedroom tent if everything got moved all the time.",
            "When I walk outside my own home, I use familiar sounds to get my bearings, especially a little distance "
            "from the house, like taking the trash cans to the curb or checking the back gate. There is usually "
            "traffic on a four-lane road nearby. My neighbor used to have chickens, which I thought were an annoyance "
            "until they went away and I lost that auditory landmark. Sometimes there is Bruce, the friendly and loud "
            "retriever next door. If my sounds outside changed every day, I would not want to venture far from the "
            "house, especially without a cane to guide each step.",
            "Until the ground got packed down, it would be hard to use any sort of stick to help with walking. One of "
            "my least favorite tasks is walking through grass with my cane. I keep a cane by my back door with a large "
            "round ball on the end so it rolls through grass more easily, but it is heavy and hard to lug around. "
            "Walking through grass for hours while we moved pastures would be very difficult. You would likely need "
            "to be led by hand everywhere, and people would get tired of doing that for someone all the time.",
            "I am guessing it was hot much of the time, and at least for me, when my eyes were at their worst, heat "
            "was not a good idea. It could have been cataracts, glaucoma, macular degeneration or any of a number of "
            "eye diseases. They all hurt. They make your eyes water, itch and burn, and there were no artificial tears.",
        ],
    },
    {
        "slug": "village", "section": "life", "title": "In a hill-country village",
        "question": "What would have worried a blind person most in a small settlement like Shiloh, where Eli and "
                    "Ahijah lived, or any village of farmers in the hills?",
        "passages": [("1 Samuel", 3, 1, 10), ("1 Samuel", 4, 12, 18), ("1 Kings", 14, 4, 6)],
        "around": "Shiloh was a sanctuary town in the hills of Ephraim where the ark was kept; Eli served there as "
                  "priest and judge, and Ahijah the prophet lived there a century later. Both went blind in old age "
                  "and stayed where they were known.",
        "says": "Eli sits by the road at the city gate waiting for news and learns everything by what he hears. Ahijah "
                "is at home when the queen comes to his door, and God tells him who she is. Both men remain in their "
                "roles: Eli still judges and teaches Samuel, Ahijah still delivers the word of God.",
        "notice": "In a village everyone knew the blind man and the blind man knew the paths. The text shows blind "
                  "elders still at their work, placed where people came to them. What it does not show is how a blind "
                  "person who was not a priest or a prophet, and had no standing, lived in such a place.",
    },
    {
        "slug": "town-gate", "section": "life", "title": "In a walled town, at the gate",
        "question": "What would have worried a blind person most in a walled town, where life ran through the gate, "
                    "as at Jabesh-gilead or Jericho, or where Job sat in judgment?",
        "passages": [("Job", 29, 7, 17), ("1 Samuel", 11, 1, 3), ("Mark", 10, 46, 47)],
        "around": "The gate of a walled town was its public square: the place of trade, news, judgment and begging. "
                  "Job describes taking his seat there. Jabesh-gilead faced a siege at its gate. Bartimaeus sat by the "
                  "road outside Jericho.",
        "says": "Job sat in the gate and says he served as eyes to the blind there. Nahash's threat to Jabesh would "
                "have blinded every man in the town in one eye. Bartimaeus's place was beside the road where the "
                "crowds passed, and he lived on what they gave.",
        "notice": "A town gate concentrated people, which is where a beggar needed to be and where a judge like Job "
                  "could be found. Walls, steps and crowds are harder for a blind person than open ground, but a "
                  "fixed place by the gate was also a kind of standing: people knew where to find him. Whether that "
                  "was care or containment is the open question of these pages.",
    },
    {
        "slug": "jerusalem", "section": "life", "title": "In first-century Jerusalem",
        "question": "What would have worried a blind person most in a crowded city built on hills, with stepped "
                    "streets, pilgrim crowds and the Temple at the top?",
        "passages": [("John", 9, 1, 8), ("John", 5, 2, 7), ("Matthew", 21, 14, 14), ("Acts", 3, 1, 3)],
        "around": "Jesus's Jerusalem was a city of steep streets, large pools, pilgrim crowds at the feasts and a "
                  "Temple whose outer court held a market. Blind people appear at its Temple gate, on the covered "
                  "walkways of a pool, and sitting where neighbours passed every day.",
        "says": "The man born blind sat and begged where his neighbours knew him. The sick lay in the porches of "
                "Bethesda, where one man had no one to help him. The blind and the lame came to Jesus inside the "
                "Temple. A lame man was carried daily to the Temple gate to beg from those going in. Begging had its "
                "places, and the places were at the thresholds of the holy.",
        "notice": "The city gave a blind person two things a village did not: crowds large enough to beg from, and "
                  "a scale of streets, steps and pools that made moving alone much harder. The man born blind walked "
                  "the length of the city to Siloam on a stranger's word. That walk, and the daily walk to a begging "
                  "place and back, are the practical questions these pages want answered by people who have made "
                  "such walks.",
    },
]

LIFE_PAGES += [
    {
        "slug": "canes-and-guides", "section": "life", "title": "Canes, staffs and guides",
        "question": "How would you get around if there were no cane, only a stick or someone's hand?",
        "passages": [("Judges", 16, 25, 26), ("Mark", 8, 22, 23), ("Acts", 13, 11, 11), ("Zechariah", 8, 4, 5)],
        "around": "Brian asked whether blind people in Bible times used canes or walking sticks, or were simply led. "
                  "The passages gathered here are every place the text shows a blind person moving, plus one that "
                  "shows the staff as the ordinary companion of old age.",
        "says": "Samson is held by the hand by a boy. Jesus takes the blind man of Bethsaida by the hand and leads him "
                "out of the village. Elymas, struck blind, gropes about looking for someone to lead him. Zechariah "
                "pictures old men and women in the streets of Jerusalem, each with a staff in hand because of age.",
        "notice": "Scripture shows guides, not canes. That does not prove no blind person ever felt the way with a "
                  "stick; it means the writers mentioned the hand and not the stick. The place-and-time section below "
                  "gathers what else can be known, from the Temple's rule against staffs to the first blind writers "
                  "who described their own.",
    },
    {
        "slug": "through-history", "section": "life", "title": "The blind through history",
        "question": "Reading how blind people lived in later centuries, what rings true to your own life, and what "
                    "has changed?",
        "passages": [("Job", 29, 15, 16), ("Isaiah", 42, 16, 16)],
        "around": "Brian asked for the history of blind people in general, not only in the Bible. The shelf now holds "
                  "two 19th-century books, one of them by a blind author, and the sources they drew on. This page "
                  "gathers what they say and marks plainly how little reaches back to the ancient world.",
        "says": "Job claims to have been eyes to the blind. Isaiah promises that God will lead the blind by a way they "
                "did not know. Between those two sentences lies the whole question of who guided whom.",
        "notice": "Most of what the old books record is European and recent: a hospice in 1260, a school in 1785, a "
                  "stick technique written down in 1872. For the ancient Near East outside the Bible, the shelf has "
                  "almost nothing, and the pages say so.",
    },
]

FAITH_PAGE = {
    "slug": "walk-by-faith", "section": "faith", "title": "We walk by faith, not by sight",
    "passages": [("2 Corinthians", 4, 16, 18), ("2 Corinthians", 5, 1, 10)],
    "around": "Paul is writing to the church at Corinth about hardship. In chapter 4 he has described being "
              "afflicted, perplexed, persecuted and struck down, and he turns from the outer self that is wasting "
              "away to the inner self renewed day by day.",
    "says": "The body is a tent that will be taken down; a building from God waits. While we live in the tent we "
            "groan, and we are away from the Lord. \"For we walk by faith, not by sight\" is Paul's reason for being "
            "confident anyway: what can be seen is temporary, and what cannot be seen is eternal.",
    "notice": "Paul is not writing about blindness. He is writing about living toward something you cannot yet see, "
              "with a body that is failing. A blind reader hears the verse with a second meaning laid over the "
              "first, and both are true to the text: faith is how anyone walks who cannot see where the road goes.",
    "brian": [
        "I have slowly come to having this as my verse, because it took a while to learn to walk by faith. This is "
        "true for those transitioning to non-visual means in life as well. It takes some time to learn to trust new "
        "methods and tools, like a white cane or a screen reader.",
        "One of my first true walk-by-faith moments came during rehabilitation training at the Hines VA hospital "
        "outside Chicago. At the end of training I did a drop-off test: I was let out of a car in a suburban business "
        "district with the task of finding a grocery store about five blocks away on my own. Unless I got into "
        "serious physical danger, I was not to be helped. I had to trust my new skills to make that trip without any "
        "sight. It was terrifying, exhilarating and liberating all at once.",
    ],
}

PAGES = LAW_PAGES + LIFE_PAGES + [FAITH_PAGE]


def by_section(section: str) -> list[dict]:
    return [p for p in PAGES if p["section"] == section]


# ---- the place and the time, from the reference shelf (edited in
# src/write_law_and_life.py, evidence in law_and_life_candidates.json)
import json as _json
from pathlib import Path as _Path

for _name in ("law_and_life.json", "followups.json", "law_questions.json"):
    _f = _Path(__file__).resolve().parents[1] / "data" / "reference" / _name
    if _f.exists():
        _extra = _json.loads(_f.read_text(encoding="utf-8"))
        for _page in PAGES:
            for _item in _extra.get(_page["slug"], []):
                _page.setdefault("place_and_time", []).append({"text": _item["text"], "source": _item["source"]})
