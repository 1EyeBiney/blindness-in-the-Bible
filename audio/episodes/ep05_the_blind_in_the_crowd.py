"""Episode 5: The blind in the crowd (Matthew 15:29-38, the mountain; Matthew 21:12-16, the Temple; 2 Samuel 5:6-8)."""
from episode_lib import BRIAN_VOICE_NOTE_SHORT, CLOSE, SERIES_INTRO, header, reader

SLUG = "the_blind_in_the_crowd"
NUMBER = 5
TITLE = "The blind in the crowd"
PASSAGES = [("Matthew", 15, 29, 31), ("Matthew", 15, 32, 38), ("2 Samuel", 5, 6, 8), ("Matthew", 21, 12, 16)]
MAX_WORDS = 3700   # Brian, 12 October 2026: longer opening, the mountain explored, the map; the ending untouched

# Written in Brian's voice from his notes of 12 October 2026. He read and edited the whole script that day:
# he struck the "Laid at His feet" paragraph and reworded the closing line (the ellipsis is his, on purpose).
DRAFT_BRIAN_COUNT = 9
APPROVED = set(range(DRAFT_BRIAN_COUNT))
DRAFT_BRIAN = [
    "Nobody on that mountain has a name. That is most of us. Most blind people in history did not get a verse of "
    "their own. They got carried up a hill by a brother or a daughter or a neighbor who decided that day was the "
    "day, and they were laid down at somebody's feet, and that was that. I think about the carriers as much as the "
    "carried. Every one of those people had someone who said, I will get you there.",
    "The blind and the lame will never enter the palace. For a thousand years that saying hung around Jerusalem, "
    "and whether or not it was ever an actual rule at the Temple, people repeated it. Then Jesus clears the "
    "market out of the Temple courts, and the first people through the gap are the blind and the lame. I do not "
    "think that is an accident of timing. I think He made room and they knew it.",
    "The leaders were angry about the children shouting. Matthew puts the healing and the anger in the same "
    "breath. The blind could see, the lame could walk, kids were singing, and the men in charge were indignant. "
    "When something good happens to people who are usually kept at the edges, somebody in charge is usually "
    "annoyed. That has not changed much in two thousand years.",
    "Here is what I take from these two crowds. The mountain was Gentile country, and the people glorified the "
    "God of Israel. The Temple was the holiest place in the Jewish world, and the people who had been shut out came "
    "in. Blind people were in the middle of both. We were never just simply the edge of what Jesus was doing. "
    "We ... were the evidence.",
    "Up a mountain. That sounds awfully scary to most blind people not named Lonnie Bedwell, who is a blind Navy "
    "veteran and climbs the kind of mountains the rest of us read about. I can tell when I have come to a place "
    "that is not usual. Up high it would feel very different. The air is cooler. The wind blows with nothing to "
    "slow it down. The sounds change, because there is nothing around you for them to bounce off. And I would get "
    "more nervous the higher we went, because I would know there was an edge somewhere and not know where.",
    "So think about what it took. A blind person going up that mountain is trusting two things at once. He is "
    "trusting the person on his arm, every single step. And he is trusting that at the top there is someone worth "
    "the climb. I think what would have carried me up is the sound. If people were being healed up there for three "
    "days, it was not quiet. I would have heard shouting and laughing and crying coming down the hill toward me, "
    "and that would have done more for my nerves than anything my guide could say.",
    "I keep asking myself whether this is about needing help in order to get our attention on Jesus. Every one of "
    "those people had to be brought. Not one of them could have done it alone. I did not choose blindness, but I "
    "know that needing an arm has pointed me toward Him more times than being able to manage on my own ever did. "
    "I do not say that is why any of us is blind. I only say it is what happened on that mountain, and it is what "
    "happens to me.",
    "There is another thing sighted people may not think of. I have lost a lot of endurance and stamina since I "
    "went blind, because I do not get to do the physical things I used to do. A long walk on flat ground is harder "
    "for me than it was. An uneven, unpaved road is harder still. So walking up a mountain over rough ground would "
    "have been very difficult for a blind person, and that is before you remember that nobody thought to bring "
    "food. And yet if I had been given my sight up there, I sure would have hung around. I would not have missed a "
    "moment of it. It would have been a sight to behold.",
    "I wrote a song recently, and one of the lines goes, I will sing before I see. It is about trusting Jesus, and "
    "the people on that mountain were doing just that. They were singing and praising without knowing where their "
    "next meal was coming from, and He fed them afterward. And I think of the joy of the companions. The people who "
    "help us are carrying our burdens too. They made that climb with somebody on their arm or on their back, and they "
    "went hungry for three days alongside us. When their friend stood up healed, they must have felt great joy "
    "too.",
]


def build(bible: dict) -> list[str]:
    L = header("ep05_the_blind_in_the_crowd")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 5: The blind in the crowd. Draft script.")
    add("# MAN and FRIEND appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    # ---- Cold open: the climb, by everything but sight -------------------------------------------
    add("[NARRATOR] (calm) Somebody is being led up a mountain.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) Start at the bottom with them, at the edge of the lake, where the air is hot and close "
        "and smells of water and reeds. Then the path turns uphill and everything a blind person steers by begins "
        "to change. The ground goes from sand to stone. The lake, which was beside you, is now below you, and its "
        "sound thins out and drops away. There are no walls up here, no doorways, nothing for a voice to bounce off, "
        "so the world goes wide and far and hard to read.")
    add("[NARRATOR] (calm) Then the air. It cools as you climb, and it starts to move. Down at the shore the wind "
        "came in pieces, round a house, through a lane. Up here it comes all at once across open ground with "
        "nothing to slow it. Anyone who cannot see knows what that means without being told. It means height. It "
        "means there is an edge somewhere, and no way of knowing where.")
    add("[PAUSE 1.0]")
    add("[NARRATOR] (beat) And then, from higher up, another sound comes down the hill. Not one voice. Hundreds. "
        "Shouting, and laughing, and somebody crying the way people cry when they cannot believe what has just "
        "happened to them. It has been going on for three days.")
    add("[NARRATOR] (calm) That sound is the reason for the climb. Dozens are making it: the lame on stretchers, the "
        "crippled on backs, the mute led by the hand, and the blind, who can walk perfectly well, holding on to an "
        "arm because the path is rock and they have never been here. At the top a man is sitting down, waiting for "
        "them.")
    add("[NARRATOR] (calm) Nobody in this crowd gets a name. This episode is about them, and about another crowd "
        "like them, in the Temple, a few days before the end.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[BREAK]")

    # ---- Where we are, and Matthew 15 -----------------------------------------------------------
    add("[NARRATOR] (calm) First, where we are. Matthew chapter fifteen. Jesus has been away in the far north, in "
        "the region of Tyre and Sidon, where He healed a Gentile woman's daughter. Now He comes back toward the Sea "
        "of Galilee, goes up a mountain, and sits down. Matthew Henry says He sat on a mountain so that all might "
        "see Him and have free access to Him, and he calls Him an open Saviour. He sat there, Henry says, like a "
        "host waiting to welcome guests, waiting to be gracious.")
    ext(reader(bible, "Matthew", 15, 29, 31))
    add("[NARRATOR] (calm) Three verses, and in them the lame, the blind, the crippled, the mute and many others. "
        "Then Matthew tells us how long they had been up there, and what happened next.")
    ext(reader(bible, "Matthew", 15, 32, 38))
    add("[BREAK]")

    # ---- The place: how high, how long, and what got them up there -------------------------------
    add("[NARRATOR] (calm) The place. Edersheim puts this scene on the eastern side of the lake, in the Decapolis, "
        "the ten Greek cities, among people who were not strictly Jewish. That fits the last line of the healing, "
        "which says they glorified the God of Israel, the way outsiders speak of someone else's God. Other "
        "commentators put it on the western shore. Matthew says only the Sea of Galilee and a mountain.")
    add("[NARRATOR] (calm) How high was it? Nobody knows. Matthew does not name the mountain and no one has "
        "identified it. What the old dictionaries can tell us is what any climb from that shore was like. The "
        "surface of the lake lies nearly seven hundred feet below the level of the sea. Smith's dictionary says it "
        "is surrounded by a high and almost unbroken wall of hills, and that the deep hollow makes the climate of "
        "the shore almost tropical, with intense heat in summer. So whichever hill this was, going up it meant "
        "climbing out of the heat into cooler, moving air, with the lake falling away below. And Matthew adds one "
        "detail himself. The disciples call it a desolate place. There was no village at the top, and no bread to "
        "be had.")
    add("[NARRATOR] (calm) Three days. What were those days like? Not a feast, at least not until the end. Henry "
        "says the people went without their natural rest and lay like soldiers in the field, and that they had "
        "scarcely enough food to keep life and soul together. Edersheim says whatever they had brought with them "
        "must have run out. But it was not a grim camp either. Matthew says the crowd was amazed, and that they "
        "glorified God. Every time a lame man stood up, or a mute woman spoke, or a blind man looked around him, "
        "several thousand people saw it happen. Hungry, sleeping on the ground, and loud with wonder: that is the "
        "mountain. Then, at the end of it, He fed them all.")
    add("[NARRATOR] (calm) Was it faith that got them up there? Notice what the text leaves out. In our last "
        "episode Jesus asked two blind men, do you believe I am able to do this? On the mountain He asks no one "
        "anything. Henry noticed it. The people brought their sick relations and friends along with them and laid "
        "them down at His feet, and, he says, we read not of any thing they said to Him. Their condition spoke for "
        "them. No commentator on our shelf says in so many words that faith carried them up the hill. But the "
        "climb is the only statement these people make, and they made it carrying each other. Every blind person "
        "on that hillside had been led up it by someone.")
    add("[NARRATOR] (calm) Where this is. Take Edersheim's placing, on the hills east of the lake. Stand there and "
        "face north, with north at twelve o'clock. Capernaum and Bethsaida, from our last two episodes, are about "
        "five hours' walk at eleven o'clock, round the top of the lake. Behind you, down the Jordan valley, Jericho "
        "is about three days' walk at six o'clock, and Jerusalem about three and a half days at seven o'clock. "
        "Hold on to Jerusalem. The second half of this episode happens there.")
    add("[BREAK]")

    # ---- Imagined scene -------------------------------------------------------------------------
    add("[NARRATOR] (calm) Scripture gives us the crowd and the mountain and the three days. It does not give us "
        "one pair of them. We imagine a blind man and the friend who got him there. This is a scene, not Scripture.")
    add("[PAUSE 1.0]")
    add("[FRIEND] (calm) Rock here, big one, step up. Good. Now it levels off for a while.")
    add("[MAN] (whisper) The air has changed. It is cooler, and the wind is coming from everywhere at once. I "
        "cannot hear the lake beside me any more. I can hear it under me.")
    add("[MAN] (calm) How high are we? Tell me the truth.")
    add("[FRIEND] (calm) High enough that I am not looking down either. Keep hold of me. The path is wide.")
    add("[MAN] (curious) Wait. Listen. What is that, up ahead?")
    add("[FRIEND] (excited) That is them. That is the crowd. Somebody up there has just started shouting, and now "
        "the rest of them have joined in.")
    add("[MAN] (calm) They sound glad. How many are up there? It sounds like a market on a feast day.")
    add("[FRIEND] (calm) Thousands. More coming up behind us. There are men carrying a boy on a door. A woman with "
        "a child who does not talk. Everybody.")
    add("[MAN] (curious) And him?")
    add("[FRIEND] (calm) Sitting on a rock at the top, like he has all day. People go up to him one at a time and "
        "then they, I do not know how to say it. They stand up different.")
    add("[MAN] (whisper) Thyme crushed under everyone's feet. Smoke from somebody's fire. We have been walking "
        "since before dawn and my friend has not let go of my arm once. I was nervous at the bottom. I am not now.")
    add("[FRIEND] (calm) Nearly there. I am going to sit you down right in front of him. Then I will step back.")
    add("[MAN] (calm) Do not go far.")
    add("[FRIEND] (calm) I am not going anywhere. I did not walk you up a mountain to lose you at the top.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) Matthew says they laid them at His feet, and He healed them.")
    add("[BREAK]")

    # ---- Brian ----------------------------------------------------------------------------------
    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE_SHORT}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[7]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[5]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[8]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[6]}")
    add("[BREAK]")

    # ---- The second crowd: the Temple. From here to the end the episode is as Brian first read it, ----
    # ---- with two narrator passages added: where this is, and when. --------------------------------
    add("[NARRATOR] (calm) Now the second crowd, and to understand it we have to go back a thousand years, to the "
        "day David took Jerusalem.")
    ext(reader(bible, "2 Samuel", 5, 6, 8))
    add("[NARRATOR] (calm) The Jebusites taunted David: even the blind and the lame could keep you out. David took "
        "the city anyway, and a saying grew up from the insult. The blind and the lame will never enter the palace. "
        "Henry notes that the blind and the lame in the Jebusites' taunt may even have meant their idols, and he is "
        "the one who reads the saying as a bar on blind and lame people entering the Temple. Our shelf has no "
        "rabbinic rule that says so, and we found none. What is certain is that the saying was remembered, and that "
        "Matthew, who knew his Scriptures, chose to tell us exactly who came into the Temple on this day.")
    add("[NARRATOR] (calm) Matthew chapter twenty-one. Jesus has ridden into Jerusalem on a donkey to shouts of "
        "Hosanna. He goes straight to the Temple.")
    ext(reader(bible, "Matthew", 21, 12, 16))
    add("[NARRATOR] (calm) Where this is. We are back in the city where this series began, three and a half days' "
        "walk south of that mountain. The Temple Mount stands on the east side of Jerusalem. The Pool of Siloam, "
        "where the man born blind washed in our first episode, is a short walk downhill from it, at the south end "
        "of the city. And the road Bartimaeus's crowd climbed in our second episode comes in from Jericho, about "
        "six hours' walk away at two o'clock.")
    add("[NARRATOR] (calm) And notice when this is. Bartimaeus was healed on that road, on the way up to this "
        "Passover. Now, within a day or so of Jesus riding into the city, the blind come to Him in the Temple and "
        "He heals them. Two healings of blind people in His last week, with the cross a few days off. In Matthew's "
        "Gospel this one in the Temple is the last healing of all.")
    add("[NARRATOR] (calm) The place. The outer court of Herod's Temple, the Court of the Gentiles, worked as a "
        "market. Edersheim describes the official money changers who, for a fee, turned foreign coins into the "
        "Temple's own coin, and what he calls that great mart for sacrificial animals. Herod had doubled the size "
        "of the Temple Mount to about fourteen hectares, and the long porches around the edge were where the "
        "business was done. Into that noise of coins and cattle Jesus walks and turns the tables over.")
    add("[NARRATOR] (calm) As the traders are driven out, Edersheim pictures the blind and the lame coming in from "
        "the porches and the Temple Mount to be healed, and the children taking up the shout of Hosanna from the "
        "road. He guesses the children may have been sons of the Levites who sang in the Temple choir, which would "
        "explain why they were there and why they knew what to sing.")
    add("[NARRATOR] (calm) Matthew Henry set the scene against David's saying. The blind and the lame had been shut "
        "out of David's palace, and here they were received in God's house. The Temple, he said, was profaned when "
        "it was made a market and honoured when it was made a hospital. And he answers the crowd's question from the "
        "day before, who is this, with the healings: Christ's works, he says, testified more than the hosannas.")
    add("[NARRATOR] (calm) One more thing from the Law. A blind descendant of Aaron could not serve at the altar, "
        "Leviticus says, though he was still fed from the holy offerings. So blind men had always been in the "
        "Temple, as priests' sons who could not serve and as beggars at the gates. What was new on this day was not "
        "that they were present. It was that they were the point.")
    add("[BREAK]")

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Set the two crowds side by side. On the mountain, in Gentile country, people laid their "
        "blind at His feet and glorified the God of Israel. In the Temple, the holiest ground in the Jewish world, "
        "the blind came to Him through the space where the market had been, and the men in charge were indignant. "
        "Different ground, different crowd, same thing in the middle: blind people, brought or coming, and Jesus "
        "healing them in front of everyone. Matthew wants us to see that it happened everywhere He went, and that "
        "the only people who minded were the ones who had been keeping the gate.")
    add("[BREAK]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
