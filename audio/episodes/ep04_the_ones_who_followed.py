"""Episode 4: The ones who followed (Matthew 9:27-34 and Matthew 12:22-28): two blind men, and a man blind and mute."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "the_ones_who_followed"
NUMBER = 4
TITLE = "The ones who followed"
PASSAGES = [("Matthew", 9, 27, 31), ("Matthew", 9, 32, 34), ("Matthew", 12, 22, 28)]
MAX_WORDS = 3200   # Brian, 11 October 2026: the opening and the scene were stretched on purpose

# Written in Brian's voice from what he has told Claude, for his approval. Not his until he says so.
# APPROVED: none yet. Brian asked (11 October) that his dialogue here be adjusted freely; he will edit.
APPROVED = set()
DRAFT_BRIAN = [
    "Two blind men following a crowd down a road and into a house. I want you to picture how that actually works, "
    "because it is not what sighted people imagine. You do not follow with your eyes. You follow the sound of the "
    "crowd, and you follow each other. One of them has a hand on the other's shoulder, or they are side by side "
    "with elbows touching, and whichever one hears better calls the turns. I have done exactly that with another "
    "blind friend in a convention hotel, and we got where we were going. It is slower, and it works.",
    "Finding the crowd was never going to be their problem. A crowd that size is the loudest thing in a town, and "
    "a house with a crowd inside it leaks noise out of every door and window. Two blind men could have walked "
    "straight to it. The problem is the last ten feet. I have stood at the edge of a packed room more times than I "
    "can count, and what I do is stop. I stand still, because if I move I bump into people, and if I bump into "
    "people I am the blind man knocking into everyone. Standing still is safe. Those two men were desperate to get "
    "to Jesus, and they could not get to Him by standing still. So they went into the crowd. That is the bravest "
    "thing in the whole story and it gets no verse at all.",
    "Jesus did not stop on the road. He let them follow Him all the way into the house. I used to think that was "
    "a little hard. Now I think He was letting them do the thing they could do, and maybe testing it. They could "
    "follow. Every step of that road was them saying we believe you are worth following, before He ever asked "
    "whether they believed. By the time He asked the question, they had already answered it with their feet.",
    "Then He asked. Do you believe I am able to do this? He asked two blind men a question and waited for the "
    "answer. He did not ask the crowd about them. He did not ask whoever was with them. He asked them. In my "
    "experience that is rarer than healing.",
    "The second man could not see and could not speak. Somebody had to bring him, and somebody had to speak for "
    "him, and then once he could speak, the argument started over his head and he never got a line. I notice that "
    "every time I read it. The man gets his sight and his voice, and the Pharisees immediately make it about "
    "themselves. I have been in that room. Not healed, but talked over. It is a particular feeling.",
    "According to your faith it will be done to you. I do not read that as a formula, as if the right amount of "
    "faith buys the right amount of sight. If it were, I would have been seeing years ago, and so would a lot of "
    "people I know who have more faith than I do. I read it as Jesus honoring what those two men had already done "
    "with their faith, which was follow Him down a road they could not see, into a house they had never been in, "
    "through a crowd they could not push past, to ask for something nobody could give them. He met them where their "
    "faith had already taken them.",
]


def build(bible: dict) -> list[str]:
    L = header("ep04_the_ones_who_followed")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 4: The ones who followed. Draft script.")
    add("# MAN, FRIEND and VOICE appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    # ---- Cold open: two men at the roadside hear the crowd come past -----------------------------
    add("[NARRATOR] (calm) Two men are sitting at the side of a road, and a crowd is coming.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) Stay with them a moment, because they will hear it long before anyone could see it. A "
        "crowd in a small town is not one sound. It is a hundred. Sandals on packed earth, first a few and then so "
        "many that the footsteps blur into one long shuffle. Voices on top of voices, nobody shouting yet, everybody "
        "talking at once, the way people talk when something has just happened and they were there. A child being "
        "carried and complaining about it. A dog. And somewhere in the middle of it all, one quieter space, where "
        "the talking stops for a step or two as people pass whoever it is they are following.")
    add("[NARRATOR] (calm) Two blind men know what that sound means before anyone tells them. A crowd like that "
        "has a centre, and the centre is moving. They have heard the news for days, the synagogue ruler's daughter, "
        "dead and then not dead. Now the man who did it is walking past them, close enough to hear His sandals, "
        "and He is not stopping.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) So they do the thing a blind man in a crowd almost never does. They get up and walk into "
        "it.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[NARRATOR] (calm) This episode gathers two short accounts from Matthew, a few chapters apart, about blind "
        "people who did not wait by the road. In the first, two blind men follow Jesus. In the second, a man who "
        "can neither see nor speak is brought to Him, and an argument breaks out over his head.")
    add("[BREAK]")

    # ---- Where we are, and Matthew 9 ------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Matthew chapter nine. Jesus has just done something that has set "
        "the whole region talking: He has gone into the house of a synagogue leader named Jairus and raised his "
        "daughter from the dead. Matthew says the news spread through all that land. As Jesus leaves that house, two "
        "men who cannot see have heard the news, and they do not intend to let Him pass.")
    ext(reader(bible, "Matthew", 9, 27, 31))
    add("[NARRATOR] (calm) Son of David. Matthew Henry notes that this was the common name for the Messiah, the "
        "King promised to David's line. These two were not calling a healer. They were naming who they believed He "
        "was, in the street, in a town where that was a dangerous thing to say. Henry pictures them following Him "
        "through the streets as beggars did, with their incessant cries. He also notices the pronoun. They did not each "
        "say have mercy on me. They said have mercy on us. Two men in the same trouble, with one prayer between "
        "them.")
    add("[NARRATOR] (calm) And notice what Jesus does with their shouting. Nothing. He keeps walking. Matthew says "
        "they followed Him, and only when He had gone into the house did He turn and speak. Henry says it plainly: "
        "He did not take notice of them at first, for He would try their faith, which He knew to be strong. And "
        "when they pushed into the house after Him, which Henry admits looked rude, they were, in his words, not "
        "more bold than welcome. A faith that walks after Him down a street and through a door is a different thing "
        "from a faith that shouts from the roadside. The healing waited until they had followed Him all the way in.")
    add("[NARRATOR] (calm) Where this happened is not certain. Edersheim places it on the way back into Capernaum, "
        "Jesus's home base on the north shore of the Sea of Galilee, a town of stone houses with flat roofs and "
        "narrow lanes running down to the water. The house would have been one of those: a courtyard, a doorway, a "
        "dim room. Elsewhere Edersheim wonders whether the details point somewhere else, and does not settle it. "
        "The place is uncertain. The path is not: road, street, door, house.")
    add("[BREAK]")

    # ---- Imagined scene -------------------------------------------------------------------------
    add("[NARRATOR] (calm) Scripture tells us they followed and what they shouted. It does not tell us how two "
        "blind men kept up with a moving crowd, or how they got through it at the door. We imagine two men who had "
        "worked the first part out long ago, and had to work the second part out that day. This is a scene, not "
        "Scripture.")
    add("[PAUSE 1.0]")
    add("[MAN] (whisper) Here they come. Hear it? That is not market noise. That is one crowd, all going the same "
        "way.")
    add("[FRIEND] (whisper) There is a gap in it. A quiet place in the middle. Somebody they are all walking "
        "around.")
    add("[MAN] (excited) It is him. Up. Hand on my shoulder, stay close. Son of David, have mercy on us!")
    add("[FRIEND] (excited) Son of David, have mercy on us!")
    add("[MAN] (calm) He is not stopping. The crowd is moving left, toward the lake road. Come on. We do not need "
        "eyes for this part. The loudest thing in this town is going exactly where we want to go.")
    add("[FRIEND] (curious) How do you know it is left?")
    add("[MAN] (calm) The gulls are on the left. The lake is always on the left in this town. Son of David, have "
        "mercy on us!")
    add("[FRIEND] (whisper) Street now. Walls close on both sides, the sound bounces. The crowd is bunching up ahead. "
        "They have stopped. A doorway, it must be. They are all trying to get in.")
    add("[MAN] (whisper) And here is the hard part. Not the road. This. A crowd standing still is a wall of backs "
        "and elbows, and if we push, we are the blind men knocking into everyone. Every day of my life I would stop "
        "right here and wait.")
    add("[FRIEND] (calm) Not today.")
    add("[MAN] (calm) No. Not today. Keep your hand on me. Pardon us. Pardon us, we are going in. Son of David!")
    add("[VOICE] (calm) Mind the step. There is a step down here. Are you two following the teacher? He has gone "
        "inside. Here. Give me your hand. Low lintel.")
    add("[FRIEND] (whisper) Dark in here. Cooler. Oil lamps. A lot of people breathing, and then they go quiet.")
    add("[MAN] (whisper) He has turned around. I can feel it. He is looking at us.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) Do you believe I am able to do this? And they said, Yes, Lord.")
    add("[BREAK]")

    # ---- Brian ----------------------------------------------------------------------------------
    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")

    # ---- The command to silence, and the mute man ----------------------------------------------
    add("[NARRATOR] (calm) Why did Jesus tell them sternly to keep quiet? Henry lists four reasons the "
        "commentators had offered: humility; a judgment on Capernaum, which had seen many miracles and not believed; "
        "caution, because the rulers were growing jealous; and so as not to stir the crowds before the time. "
        "Edersheim's reading is that a confession as far-reaching as theirs, calling Him Son of David and able to "
        "open blind eyes with a touch, was not yet to be shouted in public. The time for that would come, on a "
        "donkey, outside Jerusalem. The men did not keep quiet. They went out and spread the news through all that "
        "land, which, if you have ever been given back something you thought was gone for good, you will "
        "understand.")
    add("[NARRATOR] (calm) Matthew does not pause. In the very next verse, as those two are going out, another man "
        "is being brought in.")
    ext(reader(bible, "Matthew", 9, 32, 34))
    add("[NARRATOR] (calm) Hold on to those two reactions, the crowd's and the Pharisees', because Matthew is "
        "going to show them to us again, louder, three chapters later, with a man who is both blind and mute.")
    add("[BREAK]")

    add("[NARRATOR] (calm) Matthew chapter twelve. By now the conflict with the Pharisees has hardened. Jesus has "
        "healed on the Sabbath and defended it, and Matthew says they have begun to plot how to destroy Him. Into "
        "that, a man is brought who cannot see and cannot speak.")
    ext(reader(bible, "Matthew", 12, 22, 28))
    add("[NARRATOR] (calm) One verse for the healing. Six, and the rest of the chapter, for the argument. Edersheim "
        "is careful to keep this man separate from the mute man of chapter nine; this one, told also in Luke, came "
        "much later, when the charge that Jesus worked by the prince of demons had taken shape. That is why the man "
        "himself disappears from the story the moment he can speak.")
    add("[NARRATOR] (calm) A word about the word demon-possessed, since a blind listener may hear it with a wince. "
        "Edersheim points out that the Gospels do not actually use that phrase; they say demonised, and the phrase "
        "possession comes from Josephus. He also shows that the Gospels keep illness and this condition apart: being "
        "blind, deaf, mute or paralysed was not, on its own, called being demonised, and the two are listed "
        "separately again and again. This man is described as both. The 1915 encyclopedia notes that in the "
        "ancient Near East eye disease was widely thought to be a divine infliction. Matthew, for his part, gives no "
        "cause for this man's blindness at all. He gives the result: he could speak and see.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Put the two accounts side by side and notice the pattern. In both, the crowd asks the "
        "right question, could this be the Son of David, the very title the two blind men shouted in the street. In "
        "both, the Pharisees answer with the same charge. And in both, the blind people themselves are the ones who "
        "got it right first. The two men said it on the road. The crowd said it after the healing. The Pharisees "
        "never said it at all. By the end of chapter twelve, Jesus will tell them that their problem is not their "
        "eyes.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[5]}")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
