"""Brian asks: the questions Brian has put to the text while reading, with short answers and the pages that
answer them at length.

The page is an index into the site by curiosity rather than by book. Each entry is one question, in the third
person ("Brian asked..."), a short answer of two or three sentences lifted from the page it links to, and the links.
Nothing is answered here that is not answered on a linked page; a test checks that each link exists and that the
short answer's key phrase appears on that page. Questions with no answer on the site yet are kept at the foot, under
Open, until a page answers them; then they move up into their group and What's new says so.

Dates are when Brian asked, from docs/BRIAN_NOTES.md.
"""
from __future__ import annotations

TITLE = "Brian asks"
SLUG = "brian-asks.html"

INTRO = [
    "The questions Brian has asked while reading, gathered in one place, each with a short answer and a link to the "
    "page that answers it properly. He asks as a blind reader: what a priest did with his hands, whether a stumbling "
    "block means a trip or a fall, how anyone prices an eye. The answers come from the text, the old books on the "
    "bookshelf and the tagged Hebrew, and they are only summarised here.",
    "The questions still without an answer are listed at the foot, under Open. They stay there until a page answers "
    "them, and then they move up.",
]

# Each group: (heading, lead, entries). An entry: question (his words, lightly cleaned, in the third person), asked
# (date), answer (short, from the linked page), links [(href, title)], and check: a phrase that must appear on
# the first linked page, so the short answer cannot drift from the page.
GROUPS = [
    ("The law", "Asked while reading the four Law pages, in October 2026.", [
        {"q": "Is the Bible the first recorded text that addresses the blind? Hammurabi's code does not seem to say "
              "anything about them.",
         "asked": "2026-10-03",
         "a": "No, if addressing means mentioning eyes: the older codes of Ur-Nammu and Hammurabi price an eye that is "
              "knocked out, and Hammurabi uses the tearing out of an eye as a punishment. But none of them says a word "
              "to protect a blind person. The word blind does not occur in Hammurabi's laws at all. Israel's Law names "
              "the blind and the deaf by name, and that is the difference.",
         "links": [("law/stumbling-block.html", "Do not put a stumbling block before the blind")],
         "check": "The word \"blind\" does not occur anywhere in its laws"},
        {"q": "When was Hammurabi's code written, compared with what Moses was doing in Leviticus and Deuteronomy?",
         "asked": "2026-10-03",
         "a": "Hammurabi reigned about 1792 to 1750 BC. The Exodus is dated either around 1490 BC, from 1 Kings 6:1, "
              "or in the thirteenth century BC, so Hammurabi is three to five centuries before Moses on any reckoning. "
              "Many scholars date the writing down of Deuteronomy and Leviticus later still.",
         "links": [("law/stumbling-block.html", "Do not put a stumbling block before the blind")],
         "check": "Hammurabi reigned about 1792 to 1750 BC"},
        {"q": "Is the stumbling block more like Brian tripping slightly over a curb, or more like a blind person going "
              "down and breaking or spraining something?",
         "asked": "2026-10-14",
         "a": "The fall. The Hebrew word is mikshol, from a verb meaning to totter or fall, and everywhere else the "
              "Bible uses it, people are hurt or ruined: Jeremiah's neighbours perish on it, Ezekiel's man dies, "
              "Isaiah's stone breaks those who fall on it. Leviticus 19:14 is the one place the word is plainly literal.",
         "links": [("law/stumbling-block.html", "Do not put a stumbling block before the blind"), ("words.html", "The words")],
         "check": "Brian asked whether this is the stumble he knows"},
        {"q": "A servant with a loose tooth could be struck once and go free, and that is set equal to losing an eye?",
         "asked": "2026-10-16",
         "a": "Brian read it as the old commentators did. The tooth is not there because it equals an eye; it is "
              "there because it is the smallest lasting harm anyone would bother to name. If even that freed a servant, "
              "then nothing a master could do to a servant's body was free of cost. The eye was never in question.",
         "links": [("law/servant-blinded.html", "The servant blinded by his master")],
         "check": "the pairing of an eye with a tooth"},
        {"q": "How do you price reduced sight, or no sight at all? And is freedom worth the price of a servant's eye?",
         "asked": "2026-10-16",
         "a": "The Law of Moses does not try to answer in silver. Babylon did: a mina for a poor man's eye, half the "
              "servant's price paid to his owner. Moses names no sum and gives the servant the one thing the master "
              "cannot buy back, himself. Brian's own answer is on the page: freedom is not a price for an eye, and the "
              "law does not pretend it is, but freedom is not a small thing to hand a blind man either.",
         "links": [("law/servant-blinded.html", "The servant blinded by his master")],
         "check": "Freedom is not a price for an eye"},
        {"q": "What did a priest actually do? Would a blind priest accidentally touch things he should not, since a "
              "blind man touches things all day to know what they are?",
         "asked": "2026-10-03",
         "a": "Most of a priest's work was done with the hands: the altar fire, the lamp, the morning and evening "
              "sacrifices, the blood. The rules about touching holy things were for the Levites who carried them, not "
              "the priests who handled them daily. No old book connects the rule to accidental touching by a man who "
              "cannot see; that it happened to keep him clear of the fire and the knife is the site's observation.",
         "links": [("law/priest.html", "The blind priest")],
         "check": "Brian asked what a priest actually did with his hands"},
        {"q": "Would trying to let a blind priest fit in have been a hindrance to the rest of the Levites?",
         "asked": "2026-10-03",
         "a": "The numbers say not. The priests served in twenty-four courses, a week at a time, with about fifty on "
              "duty each weekday by Edersheim's reckoning. One man kept from the altar, but still fed from the "
              "offerings and still free to teach and to bless, was no burden on a body that size.",
         "links": [("law/priest.html", "The blind priest")],
         "check": "Would one blind priest have burdened the rest"},
    ]),
    ("The stories", "Asked while reading the pages on the blind of the Old Testament.", [
        {"q": "Had Isaac's sense of touch failed along with his sight? How else could goatskin pass for a man's hands?",
         "asked": "2026-10-20",
         "a": "Brian changed his own mind on this, and the reason is his hands. His sit on a keyboard in conditioned "
              "air; Isaac's had spent a hundred years among flocks, tents and wells. Calloused hands tell less than "
              "soft ones, and Esau's own hands were hairy enough that goat hair was the right disguise. Isaac's touch "
              "was working. It was answered with a lie prepared for it.",
         "links": [("stories/isaac.html", "Isaac and the stolen blessing")],
         "check": "Isaac's sense of touch must have failed along with his sight"},
        {"q": "Isaac had just picked out Jacob's voice through a disguise. Why, when Esau walked in moments later, "
              "did he ask \"Who are you?\"",
         "asked": "2026-10-20",
         "a": "Nothing was wrong with his ears. What had changed was what he expected: he had just blessed Esau and "
              "sent him out, so the man coming in could not be Esau. Brian calls this context, and says his own ears "
              "work the same way. The sound is only half of hearing; the other half is what you are listening for.",
         "links": [("stories/isaac.html", "Isaac and the stolen blessing")],
         "check": "What had changed was what he expected"},
        {"q": "The stolen blessing does not end well. Is there no consequence for it?",
         "asked": "2026-10-20",
         "a": "Genesis answers in Jacob's own currency. Seven years later, in the dark of a wedding night, Laban gives "
              "him Leah in place of Rachel, and when Jacob asks why he was deceived, the answer is that the younger "
              "does not go before the older. Matthew Henry put it in a sentence: Jacob was paid in his own coin.",
         "links": [("stories/isaac.html", "Isaac and the stolen blessing"), ("stories/jacob.html", "Jacob blesses Joseph's sons")],
         "check": "Brian asked whether the stolen blessing went unpunished"},
        {"q": "Eli and Ahijah both lived in Shiloh. How would each of their duties have been altered by losing their "
              "sight?",
         "asked": "2026-10-03",
         "a": "Eli held two offices, high priest and judge. A priest's duties were the altar fire, the lamp, the "
              "sacrifices and teaching the law; a judge's work was hearing, which blindness does not take. Both men "
              "stayed in their roles: Eli still judged and taught Samuel, Ahijah still delivered the word of God. "
              "Brian's own guess at which priestly tasks he could keep is on the page.",
         "links": [("life/village.html", "In a hill-country village"), ("stories/eli.html", "Eli at Shiloh")],
         "check": "Eli held two offices at once"},
    ]),
    ("Living blind, then", "The questions the Living blind pages were built to answer, asked on 2 and 3 October 2026.", [
        {"q": "What was it like to live blind in a herding camp, in tents that moved, like Isaac and Jacob?",
         "asked": "2026-10-02",
         "a": "A camp has no fixed streets to learn, and it moves. Tents of black goat's hair were held by ropes and "
              "pegs, struck and loaded on camels when the pasture gave out. Everything a blind elder needed came through "
              "other hands, which is where both the care and the deceit in Genesis come from.",
         "links": [("life/camp.html", "In a herding camp")],
         "check": "A camp has no fixed streets to learn"},
        {"q": "What was the gate of a walled town like, and what would have worried a blind person there?",
         "asked": "2026-10-02",
         "a": "The gate was the town's public square: trade, news, judgment and begging all happened there, and most "
              "men passed through it every day. A fixed place by the gate was a livelihood and a kind of standing, "
              "since people knew where to find a man. Brian's worry is the traffic, especially the loaded animals.",
         "links": [("life/town-gate.html", "In a walled town, at the gate")],
         "check": "The gate was the town's public square"},
        {"q": "Did blind people in Bible times use canes or walking sticks, or were they simply led?",
         "asked": "2026-10-03",
         "a": "Scripture shows guides, not canes. Every blind person who moves in the Bible is led by the hand: "
              "Samson, Elymas, Saul, the man of Bethsaida. Staffs were everyday equipment for everyone, so a stick was "
              "to hand, but no verse shows a blind man using one. The white cane itself is from 1921.",
         "links": [("life/canes-and-guides.html", "Canes, staffs and guides")],
         "check": "Scripture shows guides, not canes"},
        {"q": "How was Jerusalem laid out, and how did a blind beggar manage a city built on hills?",
         "asked": "2026-10-03",
         "a": "Josephus describes two hills facing each other with a valley between, and Temple gates reached by a "
              "great number of steps. Beggars had their places: the entrance to Jericho, the rich men's houses and "
              "above all the Temple gates. There was weekly organised alms as well as the crowd's loose change.",
         "links": [("life/jerusalem.html", "In first-century Jerusalem")],
         "check": "two hills facing each other with a valley between"},
        {"q": "What is known of the blind through history, before the modern schools and the white cane?",
         "asked": "2026-10-03",
         "a": "Less than one would hope, and the pages say so. Outside the Bible the shelf has almost nothing on the "
              "ancient Near East. The record thickens late: a house for three hundred blind people in Paris in 1260, "
              "the first school in 1785, and the first blind authors writing their own lives in the 1800s.",
         "links": [("life/through-history.html", "The blind through history")],
         "check": "a hospice in 1260, a school in 1785"},
    ]),
    ("The gospels", "Asked while reading the scripts of the first six episodes.", [
        {"q": "On the mountain by the sea, is the point that the blind received help to get their attention on Jesus?",
         "asked": "2026-10-12",
         "a": "The page reads it that way. No one on that mountainside has a name, and the text says nothing they said. "
              "What it does show is how they arrived: brought, carried or led up the hill by someone who decided to "
              "make the climb with them, and laid at His feet.",
         "links": [("stories/crowds-by-the-sea.html", "The crowds on the mountain")],
         "check": "Nobody blind or lame climbed that hill alone"},
    ]),
]

# Asked, and not yet answered anywhere on the site. Each: question, asked, and where the answer would go.
OPEN = [
    {"q": "How high was the mountain by the Sea of Galilee where the crowds brought the blind and the lame to Jesus?",
     "asked": "2026-10-12", "where": "stories/crowds-by-the-sea.html"},
    {"q": "Did the four thousand gather for three days like a festival? What did they eat before the loaves?",
     "asked": "2026-10-12", "where": "stories/crowds-by-the-sea.html"},
    {"q": "Is there any speculation in the old books that it was faith that got these people up the mountain?",
     "asked": "2026-10-12", "where": "stories/crowds-by-the-sea.html"},
    {"q": "How would you get around if there were no cane, only a stick or someone's hand? Brian's own answer, "
          "from experience, is still to come.",
     "asked": "2026-10-03", "where": "life/canes-and-guides.html"},
]


def all_links() -> list[str]:
    out = []
    for _, _, entries in GROUPS:
        for q in entries:
            out.extend(h for h, _ in q["links"])
    out.extend(q["where"] for q in OPEN)
    return out
