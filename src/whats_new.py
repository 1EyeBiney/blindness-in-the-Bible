"""What's new: the changes a returning reader would notice, by date, newest first; and an RSS feed of the same.

Entries are written by hand, for readers, not copied from commit messages. Each one: the date (YYYY-MM-DD), a
short title, a sentence or two, and the page to go to (relative to the site root). Add new entries at the top.

A small script (static/display.js) remembers the date of the reader's last visit in their own browser and marks
the entries newer than that. With the script off, the page is simply the dated list.
"""

TITLE = "What's new"
SLUG = "whats-new.html"
FEED = "feed.xml"
SITE = "https://blindnessinthebible.com/"

ENTRIES = [
    ("2026-10-19", "Episode 8: The servant's eye",
     "The second episode on the Law: the one law that puts a price on an eye, and pays it to the man who lost it. "
     "It plays on the servant-blinded page, where Brian's closing thoughts on the shackles of blindness are now "
     "added, and on the Episodes page.", "law/servant-blinded.html"),
    ("2026-10-19", "Episode 7: The stumbling block",
     "The first of four episodes on the Law. One sentence given at Sinai, a word Brian stopped at, and the Hebrew "
     "behind it followed through the Bible, with Matthew Henry, Josephus and the oldest law codes read in their own "
     "voices. It plays on the stumbling-block page and on the Episodes page.", "law/stumbling-block.html"),
    ("2026-10-17", "All six episodes re-mixed with quieter music",
     "After listeners said the music was too loud on phone speakers, Brian re-mixed every episode with the music set "
     "lower under the voices. Episodes 1 to 3 also gain the series map, Brian's photograph and the new closing words, "
     "and every episode now ends on a card with the site address. The YouTube addresses have changed; the old copies "
     "point to the new ones.", "episodes.html"),
    ("2026-10-16", "A new last line on every page",
     "The footer now says what the site is and what you may do with it: Brian's work, counted a gift from God through "
     "him, and given on, free to copy, quote and share under a Creative Commons Attribution licence.", "check-our-work.html"),
    ("2026-10-16", "Blind animals and the altar: Brian's thoughts, and more on the page",
     "Brian on the word broken, on doing the same things by different steps, and on the blind firstborn that was eaten "
     "at home as ordinary meat. The page also gains the word tamim, whole; the Temple market that this law created, "
     "which Jesus cleared; Malachi's argument in order; and what a gift cost the giver, from Abel to the widow's two "
     "coins. All four Law pages now carry Brian's thoughts.", "law/blind-animals.html"),
    ("2026-10-16", "The blind priest: Brian's thoughts",
     "Brian's three questions about the blind priest, now answered on the page, and his thoughts on blind pastors "
     "today and on the low expectations that shackle more than any law did.", "law/priest.html"),
    ("2026-10-16", "The servant blinded by his master: Brian's thoughts, and the Jubilee",
     "Brian on the eye and the tooth, on pricing sight, and on what freedom is worth to a blind man. The page's word "
     "section adds deror, the Jubilee's word for liberty, which is also Isaiah's word for what the Anointed One "
     "proclaims.", "law/servant-blinded.html"),
    ("2026-10-16", "The bookshelf, and this page",
     "A page listing every source on the reference shelf, what it is for and which pages cite it; and this page, "
     "which remembers your last visit on your own device and marks what is new since.", "bookshelf.html"),
    ("2026-10-14", "The Hebrew word behind each law",
     "Each of the four Law pages now has a section called The word: the Hebrew word the law turns on, what it means, "
     "and where else the Bible uses it. On the stumbling block page it answers Brian's question about whether a "
     "stumbling block means a trip or a fall.", "law/stumbling-block.html"),
    ("2026-10-14", "The Law pages read more carefully",
     "The section front now says the reading is Brian's and claims less for it. Josephus's retelling of the "
     "stumbling block law is quoted in full.", "law/index.html"),
    ("2026-10-13", "Episode 6: The answer to John",
     "John the Baptist, in prison, sends two friends with one question, and the answer he gets back begins with "
     "blind people. The last of the six episodes on sight given by Jesus.", "stories/answer-to-john.html"),
    ("2026-10-13", "The trailer, the Episodes page and a playlist",
     "A four-minute trailer on the home page; a page with every episode to play or download; and a YouTube playlist "
     "that runs the trailer and all six episodes in order.", "episodes.html"),
    ("2026-10-12", "Pictures on every page",
     "A painting on every story and study page, in one style, each with a written description and a caption. The "
     "list of stories shows a small picture beside each one.", "stories/index.html"),
    ("2026-10-12", "Text size and colours",
     "A panel near the top of every page for larger text, several colour sets including high contrast and low "
     "glare, a plainer letter style and wider spacing. Choices stay on your device.", "accessibility.html"),
    ("2026-10-12", "Episode 5: The blind in the crowd",
     "Two crowds, on a mountain above the Sea of Galilee and in the Temple at Jerusalem, where the blind were healed "
     "with no names given.", "stories/crowds-by-the-sea.html"),
    ("2026-10-11", "Episode 4: The ones who followed",
     "Two blind men who followed Jesus by sound into a house, and a man who was both blind and mute. From this "
     "episode on, each one carries a map in words.", "stories/two-blind-men.html"),
    ("2026-10-10", "Episode 3: The blind man at Bethsaida",
     "The one healing in the Gospels that comes in two stages.", "stories/bethsaida.html"),
    ("2026-10-10", "Check our work",
     "A page on how to verify any claim on the site, take the data, and rebuild the site yourself. The whole work "
     "is now under open licences.", "check-our-work.html"),
    ("2026-10-09", "Episode 2: Bartimaeus at Jericho",
     "A blind beggar at the roadside who would not be quieted.", "stories/bartimaeus.html"),
    ("2026-10-08", "The first episode, for listening",
     "The man born blind, as an episode of about sixteen minutes: the passage read word for word, the place and the "
     "time, an imagined walk down to the Pool of Siloam, and Brian's own thoughts.", "stories/man-born-blind.html"),
    ("2026-10-06", "What blind means here, and how it was made",
     "A page on the spectrum of blindness, read before the studies; and a page on how the site is made and why its "
     "quotations can be trusted.", "what-blind-means.html"),
    ("2026-10-05", "Blindness as a picture",
     "Seven pages reading the verses where blindness stands for something else, plainly, asking who is actually "
     "called blind.", "picture/index.html"),
    ("2026-10-03", "The law, living blind then, and the place and the time",
     "Four pages on what God commanded about the blind; six on daily life without sight in each kind of place; and "
     "a sourced section on the place and the time for every story.", "law/index.html"),
    ("2026-10-02", "The site begins",
     "The catalog of every verse that speaks of blindness, and the stories, each with the full passage from the "
     "Berean Standard Bible.", "index.html"),
]

INTRO = [
    "What has changed on the site, newest first, for readers coming back. Each entry links to the page to go to.",
    "If your browser allows it, the site remembers the date of your last visit on this device only, and marks the "
    "entries newer than that. Nothing is sent anywhere. A different computer or browser will not know when you were "
    "last here, so the dates are always shown.",
]
