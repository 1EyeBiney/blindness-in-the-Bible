"""Episode 3: The blind man at Bethsaida (Mark 8:22-26), with the disciples' blindness in Mark 8:14-21."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "bethsaida"
NUMBER = 3
TITLE = "The blind man at Bethsaida"
PASSAGES = [("Mark", 8, 14, 21), ("Mark", 8, 22, 26), ("Matthew", 11, 20, 24)]

DRAFT_BRIAN = [
    "People like trees walking. Of every line about blindness in the Bible, this is the one my low-vision friends "
    "quote back to me. They know exactly what he means. Shapes that move, that are the right height to be people, "
    "but with no faces and no edges. You can see something, and you cannot trust it. The Bible has one word for "
    "blindness, and most of the time it means the deep end of the pool. This verse is the one time it describes "
    "the shallow end from the inside.",
    "Jesus asked him how it was going. Think about that. He had put His hands on the man's eyes, and instead of "
    "announcing a result, He asked. And the man told the truth. Not yet. It is better, but not yet. Half the "
    "trouble blind people get into with well-meaning helpers is that we are too polite to say not yet. The man "
    "at Bethsaida said it to Jesus, and Jesus did not mind. He put His hands on him again.",
    "Jesus led him by the hand. Not a disciple, not the friends who brought him. The same Jesus who was about to "
    "put mud on another man's eyes and send him walking across Jerusalem alone took this man by the hand and "
    "walked him out of the village Himself. Both are right. Some days you need to be sent, and some days you need "
    "an arm, and the trick is knowing which day it is. He knew.",
    "He knew what trees looked like. That means he had seen before. Like Bartimaeus, like me, he lost it. I have "
    "noticed that the Gospels never explain how anyone lost their sight, and I have come to be grateful for that. "
    "Nobody asked him what happened. Jesus just asked whether he could see.",
]


def build(bible: dict) -> list[str]:
    L = header("ep03_bethsaida")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 3: The blind man at Bethsaida. Draft script.")
    add("# MAN and FRIEND appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    add("[NARRATOR] (calm) Jesus has a man by the hand, and they are walking out of town.")
    add("[NARRATOR] (beat) Behind them, a crowd that wanted to watch. Ahead, open ground, the lake somewhere to "
        "the right, the smell of fish drying. The man cannot see any of it. He can feel the hand, and the ground "
        "changing from packed street to grass.")
    add("[NARRATOR] (calm) In a minute Jesus is going to do something He does nowhere else in the Gospels. He is "
        "going to heal a man, and then ask him whether it worked.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[BREAK]")

    add("[NARRATOR] (calm) First, where we are, and it matters more than usual for this one. Jesus has just fed four "
        "thousand people on the far side of the Sea of Galilee. He gets into a boat with His disciples, and on the "
        "water He has an argument with them. Mark tells it just before the healing, and the two belong together. "
        "Listen for the word eyes.")
    ext(reader(bible, "Mark", 8, 14, 21))
    add("[NARRATOR] (calm) Having eyes, do you not see? He says it to twelve sighted men. Then the boat lands at "
        "Bethsaida, and the first thing that happens is this.")
    ext(reader(bible, "Mark", 8, 22, 26))
    add("[NARRATOR] (calm) Mark puts the two stories side by side on purpose. Sighted men who cannot see what is in "
        "front of them, and a blind man who, halfway through, sees a little and says so honestly. We will come back "
        "to that.")
    add("[BREAK]")

    add("[NARRATOR] (calm) The place. Bethsaida means house of fish. It was a fishing town on the north shore of the "
        "Sea of Galilee, near where the Jordan runs in, and it was the home town of three of the twelve: Andrew, "
        "Peter and Philip. Philip the tetrarch, Herod's son, rebuilt it and renamed it Julias after the emperor's "
        "daughter, so in Jesus's day it was half village and half new Roman town.")
    add("[NARRATOR] (calm) Where exactly it stood is still argued. Archaeologists have dug two candidate ruins on "
        "that shore, and at both they have found fishing weights and the needles used for mending nets. Whichever "
        "ruin is right, the sounds would have been the same: water, boats being hauled, nets, gulls, and the "
        "particular silence of a lake in the early morning.")
    add("[NARRATOR] (calm) Edersheim calls this the only gradual cure in the Gospels, and notes that saliva was a "
        "well known Jewish remedy for the eyes. From the man's words about trees he infers that the blindness was "
        "not from birth but came from disease. That inference is his, not the text's, though a man who knows what a "
        "tree looks like has seen one.")
    add("[NARRATOR] (calm) Why did Jesus lead him out of the village? The text does not say. Matthew Henry "
        "suggests it was to teach us to be as Job was, eyes to the blind, by doing the leading Himself rather than "
        "leaving it to the man's friends. Edersheim connects it with the woes Jesus pronounced on Bethsaida, which "
        "Matthew records.")
    ext(reader(bible, "Matthew", 11, 20, 24))
    add("[NARRATOR] (calm) A town that had seen so much and believed so little. Jesus takes the man away from "
        "it, heals him outside it, and tells him not to go back into it. Whatever else that means, it means the "
        "healing was not a show for Bethsaida.")
    add("[BREAK]")

    add("[NARRATOR] (calm) Scripture tells us he was brought, that Jesus led him by the hand, and what he said "
        "halfway through. It does not tell us who brought him or what the walk was like. We imagine a man who had "
        "once seen and had learned to live without it. This is a scene, not Scripture.")
    add("[PAUSE 1.0]")
    add("[FRIEND] (excited) He is here. The boat is in. Come on, up, take my arm, they are all going down to the "
        "shore.")
    add("[MAN] (calm) Slow down. I know the way to the shore. Left at the net racks, the ground drops after the "
        "last house.")
    add("[FRIEND] (excited) Teacher! This man, our friend. Touch him. Please. Just touch him.")
    add("[PAUSE 1.0]")
    add("[MAN] (whisper) A hand takes mine. Not my friend's hand. Warmer, and not in a hurry. We walk. The crowd "
        "noise falls behind us like a door closing. Street, then dirt, then grass. The lake is on my right. I can "
        "smell it and hear it.")
    add("[MAN] (whisper) He stops. He touches my eyes, and his hands stay there. Then he asks me, do you see "
        "anything.")
    add("[MAN] (curious) I see. I see people. But they are like trees walking. Tall, moving, no faces.")
    add("[MAN] (whisper) He does not say anything. He puts his hands on my eyes again.")
    add("[PAUSE 2.0]")
    add("[MAN] (excited) Oh. Oh, there is the lake.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Mark says he looked intently and his sight was restored and he saw everything clearly. "
        "Three verbs for one moment of seeing.")
    add("[BREAK]")

    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Back to the boat for a moment, because Mark wants us there. Jesus asked His disciples, "
        "having eyes, do you not see? Then He lands and meets a man who, after the first touch, sees a little and "
        "says so. The disciples had seen two miracles of bread and still did not understand. The blind man had seen "
        "shapes like trees and understood exactly how much he could and could not see. Mark is making a point about "
        "which of them was really blind, and it is not the beggar.")
    add("[NARRATOR] (calm) The commentators have always read it that way. Henry calls the disciples' blindness a "
        "matter of dullness, not eyes. And the chapter does not end here. Right after this, Jesus asks the disciples "
        "who people say He is, and Peter answers, You are the Christ. Peter sees clearly. Then Jesus tells them He "
        "must suffer and die, and Peter rebukes Him. Trees walking. Peter, too, saw in two stages.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) A last word for anyone listening who lives in the middle of the pool, with some sight and "
        "not enough. The Bible notices you once, here, in one sentence, and the sentence is true. Men like trees "
        "walking. It does not pretend you see nothing and it does not pretend you see. And in the story, the man "
        "who said it was not told to be satisfied with it. Jesus put His hands on him again.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
