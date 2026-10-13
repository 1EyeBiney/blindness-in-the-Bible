"""Episode 6: The answer to John (Matthew 11:2-6; Luke 7:18-23; Isaiah 35:4-6; Isaiah 61:1)."""
from episode_lib import BRIAN_VOICE_NOTE_SHORT, CLOSE, SERIES_INTRO, header, reader

SLUG = "the_answer_to_john"
NUMBER = 6
TITLE = "The answer to John"
PASSAGES = [("Luke", 7, 18, 23), ("Isaiah", 35, 4, 6), ("Isaiah", 61, 1, 1), ("Matthew", 11, 2, 6)]

MAX_WORDS = 3300   # Brian, 13 October 2026: longer opening, and three more paragraphs of his own at the end

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
    # Drafted 13 October 2026 from the "additional thoughts" Brian wrote at the foot of the reading script
    # (kept verbatim in docs/BRIAN_NOTES.md). His to change.
    "The part of this episode that comes closest to home for me is not about eyes at all. It is in the verse from "
    "Isaiah that Jesus read at Nazareth. He has sent Me to bind up the brokenhearted. The work that everyone in our "
    "house does puts us straight in the path of the brokenhearted. It is less a job than a way of life, and it is "
    "far harder than most people can imagine. But I am grateful for what it has done to my heart. It keeps me "
    "humble. It teaches me to honor other people the way God wants us to, because every one of us is made in His "
    "image.",
    "I know that someday I will see again. I have always known it, because I was blessed to have parents who led me "
    "to the Lord when I was very young.",
    "They say blindness is the second greatest fear people have. I take no comfort in that. But I can tell you, "
    "from inside it, that blindness is not something to fear at all. What scares me is something else. It is the "
    "people who have to carry this burden without knowing the grace and mercy of our Savior, and without knowing "
    "what lies ahead for those of us who belong to Him.",
]


def build(bible: dict) -> list[str]:
    L = header("ep06_the_answer_to_john")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 6: The answer to John. Draft script.")
    add("# JOHN and DISCIPLE appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    # ---- Cold open: inside the cell, by sound. Brian, 13 October 2026: keep it in one place, built from sounds
    # he can make (a drip, straw, far-off music, a guard's walk, a key and a heavy door), and shorter than before.
    add("[NARRATOR] (calm) A man is sitting in the dark, listening.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) Imagine the cell with him. It is cut out of solid rock, and rock keeps every sound. "
        "Water is dripping somewhere, slowly, always in the same place. When he shifts, the straw under him rustles, "
        "and the sound comes straight back off the walls. The air is cool and still, and it smells of damp stone.")
    add("[NARRATOR] (calm) From far above, through all that rock, comes something else. Music. Faint, like "
        "something half remembered. There is a palace up there, and people in it who have had plenty to eat.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) Then footsteps in the passage outside. A guard, in no hurry. They come closer, pass the "
        "door, and go on. He knows that walk by now. He was a man of the open air, who preached in the wilderness, "
        "beside a river, to crowds. Now the world reaches him the way it reaches a blind man: by sound, and by what "
        "other people tell him.")
    add("[NARRATOR] (calm) So there is one sound he listens for above all the rest. A key in the lock. A bolt drawn "
        "back. A door so heavy that it groans. That sound means a friend, let in for an hour, with news.")
    add("[NARRATOR] (calm) And it is the news that troubles him. He has been hearing things, secondhand, about a man "
        "he once pointed out to his own followers. What he hears does not sound like what he expected. He cannot go "
        "and see for himself. So he sends two friends, on a walk of four days, with one question.")
    add("[NARRATOR] (calm) The answer he gets back ... begins with blind people.")   # the pause is Brian's
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
    add("[NARRATOR] (calm) Where this is. Machaerus stands on the far side of the Dead Sea from everything else in "
        "this series, and it is the farthest south we go. Stand on its walls and face north, with north at twelve "
        "o'clock. Jericho is at eleven o'clock and Jerusalem at ten, and although both are close as the bird flies, "
        "the Dead Sea lies in between, so a messenger had to walk round its northern end: about two days to "
        "Jerusalem by way of Jericho. Straight ahead at twelve o'clock, up the whole length of the Jordan, is "
        "Galilee, where Jesus was. Nazareth, Capernaum and Bethsaida are all about four days' walk. That is how far "
        "John's two friends had to go to ask one question, and how far they had to come back with the answer.")
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
        "There were so many! More than one. So many. We lost count.")
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

    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE_SHORT}")
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
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[5]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[6]}")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
