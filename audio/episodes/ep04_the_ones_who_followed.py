"""Episode 4: The ones who followed (Matthew 9:27-34 and Matthew 12:22-28): two blind men, and a man blind and mute."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "the_ones_who_followed"
NUMBER = 4
TITLE = "The ones who followed"
PASSAGES = [("Matthew", 9, 27, 31), ("Matthew", 9, 32, 34), ("Matthew", 12, 22, 28)]

DRAFT_BRIAN = [
    "Two blind men following a crowd down a road and into a house. I want you to picture how that actually works, "
    "because it is not what sighted people imagine. You do not follow with your eyes. You follow the sound of the "
    "crowd, and you follow each other. One of them has a hand on the other's shoulder, or they are side by side "
    "with elbows touching, and whichever one hears better calls the turns. I have done exactly that with another "
    "blind friend in a convention hotel, and we got where we were going. It is slower, and it works.",
    "Jesus did not stop on the road. He let them follow Him all the way into the house. I used to think that was "
    "a little hard. Now I think He was letting them do the thing they could do. They could follow. Every step of "
    "that road was them saying we believe you are worth following, before He ever asked whether they believed.",
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
    "to ask for something nobody could give them. He met them where their faith had already taken them.",
]


def build(bible: dict) -> list[str]:
    L = header("ep04_the_ones_who_followed")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 4: The ones who followed. Draft script.")
    add("# MAN, FRIEND and VOICE appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    add("[NARRATOR] (calm) Two men are walking fast down a road they cannot see, after a crowd they can only hear, "
        "shouting a title at a man who will not turn around.")
    add("[NARRATOR] (beat) He keeps walking. They keep following. Into the town, down a street, through a doorway, "
        "into a house. Only then does He turn and speak to them, and what He says is a question.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[NARRATOR] (calm) This episode gathers two short accounts from Matthew, a few chapters apart, about blind "
        "people who did not wait by the road. In the first, two blind men follow Jesus. In the second, a man who "
        "can neither see nor speak is brought to Him, and an argument breaks out over his head.")
    add("[BREAK]")

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
    add("[NARRATOR] (calm) Where this happened is not certain. Edersheim places it on the way back into Capernaum, "
        "Jesus's home base on the north shore of the Sea of Galilee, a town of stone houses with flat roofs and "
        "narrow lanes running down to the water. The house would have been one of those: a courtyard, a doorway, a "
        "dim room. Elsewhere Edersheim wonders whether the details point somewhere else, and does not settle it. "
        "The place is uncertain. The path is not: road, street, door, house.")
    add("[BREAK]")

    add("[NARRATOR] (calm) Scripture tells us they followed and what they shouted. It does not tell us how two "
        "blind men kept up with a moving crowd. We imagine two men who had worked it out between them. This is a "
        "scene, not Scripture.")
    add("[PAUSE 1.0]")
    add("[MAN] (excited) He is coming out. The gate, the gate is opening, hear it? Hand on my shoulder, stay close.")
    add("[FRIEND] (excited) Son of David, have mercy on us!")
    add("[MAN] (calm) He is not stopping. The crowd is moving left, toward the lake road. Come on.")
    add("[FRIEND] (curious) How do you know it is left?")
    add("[MAN] (calm) The gulls are on the left. The lake is always on the left in this town. Son of David, have "
        "mercy on us!")
    add("[VOICE] (calm) Mind the step. There is a step down here. Are you two following the teacher? He has gone "
        "into Simon's house.")
    add("[MAN] (excited) Then so are we. Which door?")
    add("[VOICE] (calm) Here. Give me your hand. Low lintel.")
    add("[FRIEND] (whisper) Dark in here. Cooler. Oil lamps. A lot of people breathing, and then they go quiet.")
    add("[MAN] (whisper) He has turned around. I can feel it. He is looking at us.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) Do you believe I am able to do this? And they said, Yes, Lord.")
    add("[BREAK]")

    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Why did Jesus tell them sternly to keep quiet? Henry lists four reasons the "
        "commentators had offered: humility; a judgment on Capernaum, which had seen many miracles and not believed; "
        "caution, because the rulers were growing jealous; and so as not to stir the crowds before the time. "
        "Edersheim's reading is that a confession as far-reaching as theirs, calling Him Son of David and able to "
        "open blind eyes with a touch, was not yet to be shouted in public. The time for that would come, on a "
        "donkey, outside Jerusalem. The men did not keep quiet. They went out and spread the news through all that land, which, if you have "
        "ever been given back something you thought was gone for good, you will understand.")
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
        "separately again and again. This man is described as both. The 1915 encyclopedia notes that in the ancient Near East eye disease was widely thought to be a "
        "divine infliction. Matthew, for his part, gives no cause for this man's blindness at all. He gives the "
        "result: he could speak and see.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Put the two accounts side by side and notice the pattern. In both, the crowd asks the "
        "right question, could this be the Son of David, the very title the two blind men shouted in the street. In "
        "both, the Pharisees answer with the same charge. And in both, the blind people themselves are the ones who "
        "got it right first. The two men said it on the road. The crowd said it after the healing. The Pharisees "
        "never said it at all. By the end of chapter twelve, Jesus will tell them that their problem is not their "
        "eyes.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
