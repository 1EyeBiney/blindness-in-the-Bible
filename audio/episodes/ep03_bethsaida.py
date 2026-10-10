"""Episode 3: The blind man at Bethsaida (Mark 8:22-26), with the disciples' blindness in Mark 8:14-21."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "bethsaida"
NUMBER = 3
TITLE = "The blind man at Bethsaida"
PASSAGES = [("Mark", 8, 14, 21), ("Mark", 8, 22, 26), ("Matthew", 11, 20, 24)]
MAX_WORDS = 3000   # Brian, 10 October 2026: the trust material is worth the extra minutes

# APPROVED: Brian read the whole script and approved every line in his voice
# (10 October 2026). Nothing here is a draft any more.
APPROVED = set(range(len(DRAFT_BRIAN)))

DRAFT_BRIAN = [
    "People like trees walking. Of every line about blindness in the Bible, this is the one my low-vision friends "
    "can relate to most. They know exactly what he means. Shapes that move, that are the right height to be people, "
    "but with no faces and no edges. You can see something, and you cannot trust it. The Bible has one word for "
    "blindness, and most of the time it means the deep end of the pool, where I swim. This verse is the one time "
    "it describes the middle.",
    "Jesus asked him how it was going. Think about that. He had put His hands on the man's eyes, and instead of "
    "announcing a result, He asked. And the man told the truth. Not yet. It is better, but not yet. Half the "
    "trouble blind people get into with well-meaning helpers is that we are too polite to say not yet. The man "
    "at Bethsaida said it to Jesus, and Jesus did not mind. He put His hands on him again.",
    "Jesus led him by the hand. Not a disciple, not the friends who brought him. The same Jesus who was about to "
    "put mud on another man's eyes and send him walking across Jerusalem alone took this man by the hand and "
    "walked him out of the village Himself. Both are right. Some days you need to be sent, and some days you need "
    "a hand or an arm, and the real trick is knowing which days you need a hand and which days you don't.",
    "He knew what trees looked like. That means he had seen before. Like Bartimaeus, like me, he lost it. I have "
    "noticed that the Gospels never explain how anyone lost their sight, and I have come to be grateful for that. "
    "Nobody asked him what happened. Jesus just asked whether he could see.",
    # Brian's own words, written 10 October 2026.
    "I am saying this next part while being in the middle of something, not from having reached the far shore. "
    "Something we depend on has broken this week, we cannot fix it, and we do not yet know how it gets replaced. "
    "So take what follows as a report, not as advice. My family is three disabled people, and since going blind "
    "12 years ago, I have not watched a need go unmet. Not once. And it has even been a time of great plenty. It "
    "was only after going blind that I was given my own home and many of the comforts we enjoy.",
    "Looking back, I can see God's providence as clearly as the man saw the lake at the end of this story. Looking "
    "forward, from where I am standing this week, I see only trees. That is the honest position, and I have come "
    "to think it is the one this story is actually about.",
    "I may not always be able to see the path clearly, but I always know I can put my hand in His and trust Him to "
    "lead the way.",
    # Drafted from what Brian said about being guided, 10 October 2026, and approved
    # by him the same day with one change: "the alternative is not moving".
    "Let me tell you what it is actually like to take a stranger's arm. You do not know how they walk. You do not "
    "know whether they will tell you about the kerb or let you find it. Most people mean well and have no idea how "
    "to do it, and you spend the whole walk managing them, a half step behind, reading the arm for what the mouth "
    "forgot to say. Every blind person knows that walk. It is not restful. You are trusting someone who has not "
    "earned it yet, because the alternative is not moving.",
    "Now think about this man. He had a town he could cross without help, and he let go of it. He let a man he had "
    "never touched take his hand and walk him out past the last house, onto ground he had never learned. And I do "
    "not think he spent that walk managing anybody. I think he knew, the way you know, that this hand was not "
    "going to let him trip. That is the part that undoes me. Not the eyes. The hand.",
]


def build(bible: dict) -> list[str]:
    L = header("ep03_bethsaida")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 3: The blind man at Bethsaida. Draft script.")
    add("# MAN and FRIEND appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    add("[NARRATOR] (calm) Jesus has a man by the hand, and they are walking out of town.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) Before that, though, stand in the town a while, because the man we are following knew "
        "it without seeing any of it.")
    add("[NARRATOR] (calm) Bethsaida is a fishing town, and a fishing town tells you what it is before you look at "
        "it. Gulls, all day. Water slapping the hulls of the boats drawn up on the shingle. Men calling to each "
        "other across the beach about the night's catch, in that flat, tired half-shout of people who have been "
        "working since before dawn. The long dry rasp of a net dragged over stone. Wood knocking against wood "
        "somewhere behind you.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) And the smell of the place, which is two smells at once. Fish in the water, and fish "
        "drying on the racks in the sun. They are not the same smell. Anyone who lived there could tell you which "
        "way the wind had turned without lifting their head.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) A blind man in a town like that is not lost, and he is not helpless. He knows it the "
        "way you know your own house in the dark. The street is packed earth, beaten hard by every foot that has "
        "gone down it since morning. He knows where it narrows and where it opens out again. He knows which wall "
        "throws his footsteps back at him and which doorway swallows them. He knows the turns by what he can smell "
        "at each one.")
    add("[NARRATOR] (beat) He is not feeling his way along. He is walking a road he has walked more times than he "
        "could count, in a town that has been telling him where he is for as long as he has needed it to.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Hold on to that, because he is about to let go of it. He is about to put his hand into "
        "the hand of a man he has never touched, and be walked out past the last house, onto ground he has never "
        "learned, where not one of those things helps him any more.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Today there is something else in it. A crowd, somewhere down the hill, and a crowd "
        "moves all one way, and the noise of this one is going toward the water.")
    add("[PAUSE 1.5]")
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
    add("[NARRATOR] (calm) Having eyes, do you not see? He says it to His disciples, men whose eyes worked "
        "perfectly well. Then the boat lands at "
        "Bethsaida, and the first thing that happens is this.")
    ext(reader(bible, "Mark", 8, 22, 26))
    add("[NARRATOR] (calm) Mark puts the two stories side by side on purpose. Sighted men who cannot see what is in "
        "front of them, and a blind man who, halfway through, sees a little and says so honestly. We will come back "
        "to that.")
    add("[BREAK]")

    add("[NARRATOR] (calm) The place. Bethsaida means house of fish. It was a fishing town on the north shore of the "
        "Sea of Galilee, near where the Jordan runs in, and it was the home town of three of the twelve: Andrew, "
        "Peter and Philip. Philip the tetrarch, Herod's son, raised it to the rank of a city and renamed it Julias "
        "after a woman of the emperor's family, Josephus says his daughter, so in Jesus's day it was half fishing "
        "village and half new Roman town.")
    add("[NARRATOR] (calm) Where exactly it stood is still argued. Archaeologists have dug two candidate ruins on "
        "that shore, and at both they have found fishing weights and the needles used for mending nets. Whichever "
        "ruin is right, the sounds would have been the same: water, boats being hauled, nets, gulls, and the "
        "particular silence of a lake in the early morning.")
    add("[NARRATOR] (calm) Edersheim calls this the only gradual cure in the Gospels, and notes that saliva was a "
        "well known Jewish remedy for the eyes. From the man's words about trees he infers that the blindness was "
        "not from birth but came from disease. That inference is his, not the text's, though a man who knows what a "
        "tree looks like has seen one.")
    add("[NARRATOR] (calm) Why did Jesus lead him out of the village? The text does not say. Matthew Henry "
        "points out that Jesus could have healed him privately in a house, so the walk out of town must mean "
        "something, and suggests two things: that Jesus did the leading Himself to teach us to be as Job was, eyes "
        "to the blind, and that Bethsaida had forfeited the sight of another miracle. Edersheim adds that the many "
        "steps, the leading, the saliva, the hands laid on twice, were there to rule out any idea of a magic cure; "
        "everything centred on the person doing it. And both of them connect the walk with the woes Jesus "
        "pronounced on Bethsaida, which Matthew records.")
    add("[NARRATOR] (calm) One thing to have straight before we read it. These woes are not about the man we are "
        "following. Matthew says what they are about: the towns where most of Jesus's miracles had already been "
        "done. Bethsaida had seen many of them, and almost none of them were written down anywhere. Whatever the "
        "healing on the road was for, it was not the evidence against the town. That evidence was already in.")
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
    add("[PAUSE 1.5]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[7]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[8]}")
    add("[PAUSE 1.5]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[5]}")
    add("[PAUSE 1.5]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[6]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) A last word for anyone listening who lives in the middle of the pool, with some sight and "
        "not enough. The Bible notices you once, here, in one sentence, and the sentence is true. Men like trees "
        "walking. It does not pretend you see nothing, and it does not pretend you see well. And in the story, the "
        "man who said his sight was not yet right was not told to be satisfied with it. Jesus laid His hands on him "
        "again, the same hands that would soon be nailed to a cross, and made his sight whole.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (calm) Jesus makes it right.")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
