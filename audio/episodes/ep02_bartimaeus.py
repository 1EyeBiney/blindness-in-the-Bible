"""Episode 2: Bartimaeus at Jericho (Mark 10:46-52; Luke 18:35-43; Matthew 20:29-34)."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "bartimaeus"
NUMBER = 2
TITLE = "Bartimaeus at Jericho"
PASSAGES = [("Mark", 10, 32, 37), ("Mark", 10, 46, 52), ("Luke", 18, 35, 43), ("Luke", 19, 1, 11),
            ("Matthew", 20, 29, 34)]
MAX_WORDS = 3600   # Brian, 9 October 2026: no time limit on this one; the material carries it

# Written in Brian's voice from what he has told Claude, for his approval. Not his until he says so.
# APPROVED: indices Brian has read and edited himself (8 October 2026): 2, 3, 4. Still drafts: 0, 1, 5, 6.
APPROVED = {2, 3, 4}
DRAFT_BRIAN = [
    "Bartimaeus asks to see again. That one word is the whole difference between him and the man born blind. "
    "I lost my sight in 2014, after a lifetime of seeing. I know what a face looks like, what Jericho's palms would "
    "have looked like, what a road looks like going uphill into the distance. The man born blind had nothing to "
    "compare the dark to. Bartimaeus did. Every day he sat by that road he knew exactly what he was missing.",
    "He hears a crowd and has to ask what it is. I do that constantly. A room goes quiet, or everyone laughs, or "
    "chairs scrape, and I have to ask the person next to me what just happened. Most of the time people answer. "
    "Sometimes they are too busy to. Bartimaeus got an answer, and it was the most important sentence anyone ever "
    "said to him.",
    "People told him to be quiet. If you are blind and loud in public, people get uncomfortable, because you are "
    "the one making a scene and they cannot make eye contact to settle you down. He shouted louder. I love that. "
    "Then, the moment Jesus noticed him, he suddenly got encouragement from the crowd when they shouted for him to "
    "take courage, he is calling you. The crowd did not change. His standing in it did. Jesus lifts everyone up.",
    "He threw off his cloak. For a beggar that cloak was his bed, his coat, and the thing he spread out to collect "
    "coins. He left it in the dust because he was not planning to come back to that spot. My white cane is the "
    "thing I would never leave behind. So, for me, there would be a little pile of beat up white canes, and an "
    "iPhone. Yes, I would go back to Android.",
    "Jesus asks him what he wants. He does not assume. Every blind person I know has a story about someone who "
    "grabbed an arm and steered them somewhere they did not want to go. People mean well, but often assume. Jesus "
    "had a blind man standing in front of Him and still asked. Self-advocacy at its finest.",
    "Here is what gets me about Jericho. Jesus knew exactly where He was going and exactly what was waiting for Him. "
    "He had said it out loud three times. Most of us, with that ahead of us, would have put our heads down and "
    "walked. He stopped twice in one town. Once for a beggar who was shouting, and once for a little tax man up a "
    "tree that the whole city despised. Neither of them was on the way to anything. He was not teaching a crowd or "
    "healing a hundred people. He was being present for one person at a time, with the cross a few days off. That is "
    "the Jesus I want to follow, and honestly, it is the Jesus I want to be more like. I get busy and I get focused "
    "on where I am headed, and the man shouting by the road becomes an interruption. He never once treated anyone as "
    "an interruption.",
    "Bartimaeus and Zacchaeus could not see Him, and for opposite reasons. One had no eyes for it. One had a crowd "
    "in the way and was too short to see over it. I know both of those. I know the first one every day. And I know "
    "the second one from every church lobby and conference hall where the crowd between me and the person I want to "
    "reach is just people, standing, talking, not unkind, just in the way. Bartimaeus shouted. Zacchaeus climbed. "
    "Both of them did something a grown man is not supposed to do in public, and Jesus stopped for both. I take that "
    "as permission.",
]


def build(bible: dict) -> list[str]:
    L = header("ep02_bartimaeus")
    add = L.append
    ext = L.extend

    add("# Not By Sight, episode 2: Bartimaeus at Jericho. Draft script.")
    add("# BARTIMAEUS and VOICE appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    # ---- Cold open ------------------------------------------------------------------------------
    add("[NARRATOR] (calm) A man is sitting in the dust beside the busiest road in Judea, and he hears something "
        "change.")
    add("[NARRATOR] (beat) It's not the usual traffic. It's not the mule trains and the pilgrims and the tax men. "
        "No, it's a crowd. A big one. And it's moving as one thing. But there's a sound inside it he cannot place. "
        "He has sat by this road for years so he knows every sound it makes, but he can't quite place this one. He "
        "knows it is something he has not heard before.")
    add("[NARRATOR] (calm) So he does what blind people do so many times each day. He asks.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[BREAK]")

    # ---- Where we are ---------------------------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. It is spring, a few days before Passover, and Jesus is on His last "
        "journey to Jerusalem. He has told His disciples three times that He is going there to die, and yet He "
        "continues His work: teaching, ministering, being present in the moment.")
    add("[NARRATOR] (calm) A large crowd travels with Him, because everyone is going up to the feast, and the road "
        "from Galilee and from across the Jordan funnels through one city before the final climb. That city is "
        "Jericho.")
    add("[NARRATOR] (calm) Mark shows us the mood on that road just before Jericho. Listen for a question Jesus "
        "asks, because He is about to ask it again.")
    ext(reader(bible, "Mark", 10, 32, 37))
    add("[NARRATOR] (calm) What do you want Me to do for you? He asks it of James and John, who want the seats of "
        "honour in His kingdom. Hold on to that question. A few verses later, outside Jericho, He will ask it of a "
        "blind beggar, in the very same words, and get a very different answer.")
    add("[NARRATOR] (calm) Three Gospels tell the beggar's story. Mark tells it first and gives the man a name. We "
        "will hear Mark, then Luke, then Matthew, and notice where they differ. Mark first.")
    ext(reader(bible, "Mark", 10, 46, 52))
    add("[NARRATOR] (calm) Son of Timaeus. Bar means son, so Mark has told us his name twice. He is one of very few "
        "people Jesus healed whose name we know at all. Henry's guess is that Mark names him because he was a "
        "well known, much talked of beggar, the kind of man a whole city knew by his place on the road.")
    add("[BREAK]")

    # ---- The place and the time ------------------------------------------------------------------
    add("[NARRATOR] (calm) The place. Jericho lies in the Jordan Valley about two hundred and fifty metres below "
        "sea level, the lowest city in the world. It was warm when Jerusalem was cold, which is why Herod built "
        "palaces there and why Jerusalem's wealthy wintered there. Josephus called the plain the most fruitful "
        "country in Judea, with its palms and its balsam trees, whose sap was gathered as it dripped, he said, like "
        "tears. Smith's dictionary says that in Jesus's day Jericho was once more a city of palms.")
    add("[NARRATOR] (calm) Edersheim pictures its streets at Passover full of pilgrims from Galilee and from beyond "
        "the Jordan, priests going up to serve, traders, and the caravan traffic from Arabia and Damascus. It was "
        "also the central station for collecting taxes, which is why a chief tax collector named Zacchaeus lived "
        "there. Luke tells his story in the next breath after this one.")
    add("[NARRATOR] (calm) From Jericho the road to Jerusalem climbs about a thousand metres in roughly six hours of "
        "walking, through dry rocky hills with no town between. Edersheim, writing about the Good Samaritan, calls "
        "that road notoriously unsafe, the kind of country robbers hid in. Everyone leaving Jericho for the feast was "
        "about to start that climb together, for safety as much as company, and the edge of the city was the last "
        "place to sit and ask for help before the hills.")
    add("[NARRATOR] (calm) Smith's says that beggars in later times had fixed places, at street corners, at the "
        "Temple gates, at the gates of houses, and it cites this very verse. People who could not work were usually "
        "cared for by relatives. A man begging by the road may have had no one. Or he may have had someone who "
        "walked him to his place each morning and came back for him at dusk. The text does not say.")
    add("[BREAK]")

    # ---- Imagined scene -------------------------------------------------------------------------
    add("[NARRATOR] (calm) Scripture does not tell us what Bartimaeus heard before he heard the name, or who "
        "answered him. We imagine a man who knew his road by ear. This is a scene, not Scripture.")
    add("[PAUSE 1.0]")
    add("[BARTIMAEUS] (whisper) Hooves. A cart with one wheel that squeaks, the same cart every morning. Sandals, "
        "hundreds of them, going up. Pilgrims. They talk about the feast and about the price of lambs.")
    add("[BARTIMAEUS] (calm) But this is different. This crowd is slower, and it is turned inward, like people "
        "walking around something. And under the talk there is one voice they are all listening to.")
    add("[BARTIMAEUS] (curious) Friend. You, with the basket, I can hear it creak. What is this? Who is passing?")
    add("[VOICE] (calm) Jesus. The Nazarene. The teacher who healed in Galilee. He is going up to the feast.")
    add("[BARTIMAEUS] (excited) Jesus. Son of David. Son of David, have mercy on me!")
    add("[VOICE] (calm) Quiet. He is teaching. You will not be heard over this crowd anyway.")
    add("[BARTIMAEUS] (excited) Son of David! Have mercy on me!")
    add("[PAUSE 1.0]")
    add("[BARTIMAEUS] (whisper) The crowd stops. I hear it stop, the way a river sound stops when you put your "
        "hand over your ears. Feet shuffling. Someone far ahead has said something.")
    add("[VOICE] (excited) Take courage. Get up. He is calling you. Here, your hand, this way.")
    add("[BARTIMAEUS] (whisper) My cloak is on the ground with the morning's coins in it. Leave it. Leave all of "
        "it.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) Then the question. Jesus has a blind man standing in front of Him, and He asks what he "
        "wants. The same words He had just asked two disciples. James and John asked for glory. Bartimaeus asked to "
        "see. Henry says that although Christ knows our needs, He wants to hear them from us, and that having to "
        "say the thing plainly teaches us the worth of what we ask for. Edersheim notices what came after: the man "
        "did not go home. He followed Jesus on the way, glorifying God, and all the people praised God when they saw "
        "it.")
    add("[BREAK]")

    # ---- Brian ----------------------------------------------------------------------------------
    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add("[BREAK]")

    # ---- Luke -----------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Luke tells the same story, with one difference you will hear right at the start.")
    ext(reader(bible, "Luke", 18, 35, 43))
    add("[NARRATOR] (calm) Luke says as Jesus drew near to Jericho. Mark says as He was leaving. There were in "
        "fact two Jerichos in Jesus's day: the old city of Joshua's time lay in ruins near Elisha's spring, and the "
        "new town Herod and his son built, with palaces and gardens, stood a short distance off. Some readers since "
        "have used that to make the accounts agree, with the healing on the road between them. None of our old "
        "books does. Matthew Henry says only that Luke's word for near can mean leaving as well as arriving. "
        "Edersheim says plainly that it is better to admit the difficulty than to force a harmony. We will leave "
        "it where he left it.")
    add("[NARRATOR] (calm) Notice what Luke adds at the end. The man follows, glorifying God, and all the people, "
        "the same people who told him to be quiet, give praise to God. The crowd that shushed him ends up shouting "
        "with him.")
    add("[NARRATOR] (calm) And Luke is not finished with Jericho. In his telling, Jesus has just reached the edge "
        "of the city when Bartimaeus shouts. Now He walks on into it, with the healed man somewhere in the crowd "
        "behind Him, and stops again. Read straight on.")
    ext(reader(bible, "Luke", 19, 1, 11))
    add("[NARRATOR] (calm) Two stops in one town. Put them side by side. Bartimaeus could not see Jesus because of "
        "his eyes. Zacchaeus could not see Him because of the crowd, and because he was short. Both of them were "
        "blocked by the same crowd of pilgrims. Both did something a grown man did not do in public in that world: "
        "one shouted a Messianic title at the top of his lungs, the other ran ahead and climbed a tree. And Jesus "
        "stopped for both, and called each of them by what he was. The beggar had called Him Son of David. Jesus "
        "called the tax collector a son of Abraham, the one name the whole town had taken away from him.")
    add("[NARRATOR] (calm) The place fits. Edersheim says Jericho was the tax station for the Jordan crossing and "
        "for the balsam trade, which is why a chief tax collector was rich there and hated there. Sycamore figs lined "
        "the roads of the plain; the old dictionaries describe them as low-branched, spreading trees, the easiest "
        "tree in the country to climb. A man who wanted to see over a crowd could not have chosen better.")
    add("[NARRATOR] (calm) Then the line that ends the story, and names what Jesus had been doing all day in "
        "Jericho: the Son of Man came to seek and to save the lost. And look at the verse after it. Luke says Jesus "
        "went on to tell a parable because He was near Jerusalem and the people thought the kingdom was about to "
        "appear. He is teaching with the city in sight. He has told His disciples three times what waits for Him "
        "there, and on the last road up to it He heals a beggar, dines with a tax collector, and stops to teach a "
        "crowd who have misunderstood Him. The cross is days away and He is not hurrying past anyone.")
    add("[BREAK]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[5]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[6]}")
    add("[BREAK]")

    # ---- Matthew --------------------------------------------------------------------------------
    add("[NARRATOR] (calm) Matthew tells it last, and shortest, and he counts differently.")
    ext(reader(bible, "Matthew", 20, 29, 34))
    add("[NARRATOR] (calm) Two blind men. Mark and Luke have one, and Mark names him. Edersheim suggests "
        "Bartimaeus was the spokesman of two, the one whose voice carried and whose name was remembered. That is a "
        "reasonable guess and it is only a guess. What all three agree on is the shout, the crowd telling them to "
        "be quiet, Jesus stopping, and the question.")
    add("[NARRATOR] (calm) Matthew also adds a detail the others leave out. Jesus touched their eyes. In Mark and "
        "Luke the healing is by a word alone. Your faith has healed you. Receive your sight. In Matthew there is a "
        "hand on the face first.")
    add("[BREAK]")

    # ---- Brian, part two ------------------------------------------------------------------------
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add("[BREAK]")

    # ---- What the word tells us ----------------------------------------------------------------
    add("[NARRATOR] (calm) One more thing about the word. Bartimaeus asks to see again, and Luke's man asks the "
        "same, to receive his sight back. The man born blind, in our first episode, had never seen at all. Scripture "
        "does not tell us how Bartimaeus lost his sight, or when, or how much he had left. He may have seen light and "
        "shadow. He may have seen nothing. Blindness then, as now, was a range, and the Bible's one word covers all "
        "of it. What the text does tell us is that he knew what he had lost, and that when he could see again the "
        "first thing he chose to look at was the road to Jerusalem, following Jesus up it.")
    add("[BREAK]")

    # ---- Close ----------------------------------------------------------------------------------
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
