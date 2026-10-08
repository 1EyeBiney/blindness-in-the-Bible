"""Episode 6: The answer to John (Matthew 11:2-6; Luke 7:18-23; Isaiah 35:4-6; Isaiah 61:1)."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "the_answer_to_john"
NUMBER = 6
TITLE = "The answer to John"
PASSAGES = [("Luke", 7, 18, 23), ("Isaiah", 35, 4, 6), ("Isaiah", 61, 1, 1), ("Matthew", 11, 2, 6)]

DRAFT_BRIAN = [
    "John the Baptist doubted. The man who pointed at Jesus and said, behold the Lamb of God, sat in a dungeon and "
    "sent people to ask, are you the one, or should we wait for somebody else. I find that enormously comforting. "
    "Doubt in a dark place is not a failure of faith. It is what faith sounds like when it is being tested, and it "
    "is allowed to ask.",
    "Jesus did not answer with a sermon. He answered with people. Luke says that at that very hour He healed many, "
    "and gave sight to many who were blind, and then told John's messengers, go tell him what you have seen. The "
    "first thing on the list was us. When the question was, who are you, the answer began with blind people "
    "seeing. I have read that verse a hundred times and it still stops me.",
    "I have to be honest about the other side of it. I am a blind believer, and my eyes have not been opened. "
    "The healings in these episodes were signs, and signs point to something. They pointed John to who Jesus was. "
    "They point me there too, without my sight coming back. I would be lying if I said I never asked for it. I "
    "would also be lying if I said that is what this verse is about. It is about who He is. I know who He is.",
    "Blessed is the one who does not fall away on account of me. That is the last line of the answer, and I think "
    "it was aimed at John, in prison, who was not going to be healed or rescued and knew it. Jesus was telling "
    "him: do not let what I am not doing for you make you doubt what I am. Every blind believer who has prayed for "
    "sight and gotten up the next morning still blind has heard that line.",
]


def build(bible: dict) -> list[str]:
    L = header("ep06_the_answer_to_john")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 6: The answer to John. Draft script.")
    add("# JOHN and DISCIPLE appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    add("[NARRATOR] (calm) A man in a fortress above the Dead Sea has a question, and he cannot go and ask it "
        "himself.")
    add("[NARRATOR] (beat) He is a prisoner. The walls are a hundred metres of sheer rock. He has heard things, "
        "secondhand, through the people allowed to visit him. And what he has heard does not sound like what he "
        "expected. So he sends two friends with one question.")
    add("[NARRATOR] (calm) The answer he gets back begins with blind people.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[NARRATOR] (calm) This is the last episode in our run through the healings in the Gospels, and it is the "
        "one where Jesus Himself tells us what the healings were for.")
    add("[BREAK]")

    add("[NARRATOR] (calm) First, where we are. John the Baptist baptised Jesus in the Jordan and pointed Him out "
        "to his own followers. Then John rebuked Herod Antipas for taking his brother's wife, and Herod put him in "
        "prison. Josephus, the Jewish historian, names the prison: Machaerus, a fortress east of the Dead Sea, on "
        "the frontier. Edersheim describes it as a stronghold on sheer cliffs, built by one Jewish king and enlarged "
        "by Herod the Great, with a palace at the top and dungeons cut into the rock below. John would die there.")
    add("[NARRATOR] (calm) From that place he sends his question. Luke tells it with the most detail.")
    ext(reader(bible, "Luke", 7, 18, 23))
    add("[NARRATOR] (calm) Are You the One who was to come, or should we look for someone else? That is the whole "
        "question. Henry offers three reasons John might have sent it: he wanted to be sure for himself; the long "
        "imprisonment had made him wonder why Jesus did not help him; or he sent his followers so that they would "
        "see for themselves and attach themselves to Jesus after he was gone. And Luke tells us what Jesus did "
        "before He answered a word. At that very hour He healed many, and gave sight to many who were blind. Henry "
        "takes the words literally: they stayed perhaps an hour, and in that hour saw enough. Then He told them what "
        "to say.")
    add("[BREAK]")

    add("[NARRATOR] (calm) To hear the answer the way John heard it, you have to know what John knew. Jesus's "
        "reply is built out of the prophet Isaiah. Here is the first passage, from a chapter about the day God "
        "Himself would come.")
    ext(reader(bible, "Isaiah", 35, 4, 6))
    add("[NARRATOR] (calm) And the second, the passage Jesus had already read aloud in the synagogue at Nazareth.")
    ext(reader(bible, "Isaiah", 61, 1, 1))
    add("[NARRATOR] (calm) The eyes of the blind will be opened. Good news to the poor. Jesus did not say, I am "
        "the one. He said, go and tell John what you see, and then He listed the things Isaiah had said would "
        "happen when God came. John, who had Isaiah by heart, would have needed no explanation. Smith's dictionary "
        "says opening the eyes of the blind was understood as a peculiar attribute of the promised one. Henry says "
        "the works spoke more plainly than any words could.")
    add("[BREAK]")

    add("[NARRATOR] (calm) Scripture gives us the question and the answer. It does not give us the messengers' "
        "return. We imagine two tired men climbing back up to Machaerus with something to tell. This is a scene, "
        "not Scripture.")
    add("[PAUSE 1.0]")
    add("[DISCIPLE] (calm) Teacher. We are back. Yes, it is us, both of us. Sit, please, you should sit.")
    add("[JOHN] (calm) Well? Did you ask him?")
    add("[DISCIPLE] (calm) We asked him exactly as you said. Are you the one who was to come, or do we wait for "
        "another.")
    add("[JOHN] (curious) And what did he say?")
    add("[DISCIPLE] (calm) At first, nothing. He went on with what he was doing. There was a crowd, as there "
        "always is, and people were being brought to him. We stood there an hour. A man who had been carried in "
        "walked out. A woman who was bent double stood up straight. And there was a blind man.")
    add("[JOHN] (calm) Go on.")
    add("[DISCIPLE] (excited) He was old, and someone had him by the arm, and Jesus touched his face, and the man "
        "looked up, and he started to cry and to laugh at the same time, and he kept looking at his own hands. "
        "More than one. Many. We lost count.")
    add("[JOHN] (whisper) The eyes of the blind will be opened.")
    add("[DISCIPLE] (calm) Then he turned to us and said, go back and tell John what you have seen and heard. The "
        "blind see. The lame walk. Lepers are cleansed, the deaf hear, the dead are raised, and the poor are told the "
        "good news. And then he said one more thing, and I think it was for you.")
    add("[JOHN] (calm) Say it.")
    add("[DISCIPLE] (calm) Blessed is the one who does not fall away on account of me.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) John stayed in Machaerus. He was not healed, and he was not rescued. The answer he got "
        "was other people's sight.")
    add("[BREAK]")

    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Matthew tells the same exchange more briefly, and we will hear it, because it adds "
        "one thing: Matthew says John heard in prison about the works of Christ. It was the works that reached him, "
        "through the walls.")
    ext(reader(bible, "Matthew", 11, 2, 6))
    add("[NARRATOR] (calm) Right after this, in both Gospels, Jesus turns to the crowd and praises John: among "
        "those born of women there is none greater. The doubt did not lower John in His eyes. The question was "
        "allowed. It was answered. And the man who asked it was called the greatest of the prophets in the same "
        "hour.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Look back over the six episodes. A man born blind sent to wash. Bartimaeus shouting by "
        "the road. A man at Bethsaida who saw trees walking and said so. Two men who followed by sound into a house, "
        "and one who could not speak for himself. Crowds on a mountain and in the Temple. And now this: when the "
        "greatest prophet asked who Jesus was, Jesus pointed at all of them. The blind receive sight. Not because "
        "blindness was the worst thing, and not because sight was the point, but because Isaiah had said that when "
        "God came, this is what it would look like. Blind people were not at the edge of that. We were the first "
        "thing on the list.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
