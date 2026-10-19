"""The Episodes page: every episode in one place, each with its audio, its MP3 and its YouTube link.

The player details (YouTube id, MP3 file, length) are not repeated here. They are read from the story each
episode belongs to, in src/stories.py, so the two can never disagree.
"""

TITLE = "Episodes"
SLUG = "episodes.html"

# number, title, passage as spoken, the story pages it covers (the first one supplies the player and the picture),
# and a short description. Add a new episode at the end.
EPISODES = [
    (1, "The Man Born Blind", "John 9", ["man-born-blind"],
     "Jesus makes mud, puts it on a blind beggar's eyes, and sends him to wash in the Pool of Siloam. The man comes "
     "back seeing, and then has to answer for it to his neighbours, his parents and the Pharisees."),
    (2, "Bartimaeus at Jericho", "Mark 10, Luke 18 to 19", ["bartimaeus"],
     "A blind beggar at the roadside hears that Jesus of Nazareth is passing and will not be quieted. Jesus stops, "
     "the whole crowd stops with Him, and He asks, \"What do you want Me to do for you?\""),
    (3, "The Blind Man at Bethsaida", "Mark 8", ["bethsaida"],
     "Jesus takes a blind man by the hand and leads him out of the village. This is the one healing in the Gospels "
     "that comes in two stages: first he sees people who look like trees, walking, and then he sees everything clearly."),
    (4, "The Ones Who Followed", "Matthew 9 and 12", ["two-blind-men", "blind-and-mute-man"],
     "Two blind men follow Jesus down the street, calling out, and keep following right into the house. Then a man "
     "who is both blind and mute is brought to Him by others, and the argument that follows forgets the man it was about."),
    (5, "The Blind in the Crowd", "Matthew 15 and 21", ["crowds-by-the-sea", "the-temple"],
     "Twice the blind are healed as part of a crowd, with no names given. Once on a mountain above the Sea of Galilee, "
     "where people carried each other up the hill and stayed three days. Once in the Temple at Jerusalem, in Jesus's "
     "last week."),
    (6, "The Answer to John", "Matthew 11 and Luke 7", ["answer-to-john"],
     "John the Baptist, in prison at Machaerus, sends two friends to ask Jesus one question: are You the One who was "
     "to come? The answer he gets back begins with blind people. This is the episode where Jesus Himself says what "
     "the healings were for."),
    (7, "The Stumbling Block", "Leviticus 19 and Deuteronomy 27", ["law/stumbling-block"],
     "The first of four on the Law. One sentence given at Sinai: you must not curse the deaf or place a stumbling "
     "block before the blind. Brian read it and stopped at one word. Is the law about a trip, or a fall? The Hebrew "
     "word, and every other place the Bible uses it, gives the answer."),
    (8, "The Servant's Eye", "Exodus 21", ["law/servant-blinded"],
     "The second of four on the Law, and the only price the Bible ever puts on an eye. If a master blinds his "
     "servant, the servant goes free; if he knocks out a tooth, the servant goes free. Why should an eye and a tooth "
     "cost the same? Two Hebrew words, one for eye and one for free, and the laws of Babylon give the answer."),
]

# The trailer: a short taste of the episodes, on the home page and at the top of the Episodes page.
TRAILER = {"youtube": "2TDaUBlFbgc", "mp3": "not_by_sight_00_trailer.mp3", "minutes": 4,
           "title": "Not By Sight: the trailer"}

# The YouTube playlist that joins the trailer and every episode, in order.
PLAYLIST = "https://www.youtube.com/playlist?list=PLSZO9vlYl7pE"

INTRO = [
    "Each story of sight given by Jesus is also an episode of about twenty minutes, made for listening. You will "
    "hear the passage read word for word from the Berean Standard Bible, the place and the time, an imagined scene "
    "or two, and Brian's own thoughts, with his music.",
    "From episode 7 the series turns to the Law: four episodes on what God commanded about the blind. They have no "
    "imagined scenes. In their place are the Hebrew words the laws turn on, followed through the rest of the Bible, "
    "and the old books read in their own voices.",
    "Every episode plays here as a plain audio file, or downloads as an MP3 to keep. The same episode is on YouTube "
    "with pictures and captions. Start anywhere. Each one stands by itself.",
]
