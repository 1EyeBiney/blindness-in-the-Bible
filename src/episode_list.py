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
]

INTRO = [
    "Each story of sight given by Jesus is also an episode of about twenty minutes, made for listening. You will "
    "hear the passage read word for word from the Berean Standard Bible, the place and the time, an imagined scene "
    "or two, and Brian's own thoughts, with his music.",
    "Every episode plays here as a plain audio file, or downloads as an MP3 to keep. The same episode is on YouTube "
    "with pictures and captions. Start anywhere. Each one stands by itself.",
]
