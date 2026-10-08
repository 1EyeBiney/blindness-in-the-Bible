"""Episode 5: The blind in the crowd (Matthew 15:29-31, the mountain; Matthew 21:12-16, the Temple; 2 Samuel 5:6-8)."""
from episode_lib import BRIAN_VOICE_NOTE, CLOSE, SERIES_INTRO, header, reader

SLUG = "the_blind_in_the_crowd"
NUMBER = 5
TITLE = "The blind in the crowd"
PASSAGES = [("Matthew", 15, 29, 31), ("2 Samuel", 5, 6, 8), ("Matthew", 21, 12, 16)]

DRAFT_BRIAN = [
    "Nobody on that mountain has a name. That is most of us. Most blind people in history did not get a verse of "
    "their own. They got carried up a hill by a brother or a daughter or a neighbor who decided that day was the "
    "day, and they were laid down at somebody's feet, and that was that. I think about the carriers as much as the "
    "carried. Every one of those people had someone who said, I will get you there.",
    "Laid at His feet. I have been laid at people's feet, in a manner of speaking. Sat down in a chair at a party "
    "and left there, because the person who brought me had to go do something and I did not know the room. It is "
    "not a bad feeling if you trust the person. The crowd on the mountain trusted Him enough to set their people "
    "down and step back.",
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
    "in. Blind people were in the middle of both. We were never the edge of what Jesus was doing. We were the "
    "evidence.",
]


def build(bible: dict) -> list[str]:
    L = header("ep05_the_blind_in_the_crowd")
    add = L.append
    ext = L.extend
    add("# Not By Sight, episode 5: The blind in the crowd. Draft script.")
    add("# MAN and FRIEND appear only inside scenes the narrator introduces with the word 'imagine'.")
    add("")

    add("[NARRATOR] (calm) Somebody is being carried up a mountain.")
    add("[NARRATOR] (beat) Not one somebody. Dozens. The lame on stretchers, the crippled on backs, the mute led by "
        "the hand, and the blind, who can walk perfectly well, holding an arm because the path is rock and they have "
        "never been here. At the top a man is sitting down, waiting for them.")
    add("[NARRATOR] (calm) Nobody in this crowd gets a name. This episode is about them, and about another crowd "
        "like them, in the Temple, a few days before the end.")
    add("[PAUSE 1.5]")
    add(f"[NARRATOR] (calm) {SERIES_INTRO}")
    add("[BREAK]")

    add("[NARRATOR] (calm) First, where we are. Matthew chapter fifteen. Jesus has been away in the far north, in "
        "the region of Tyre and Sidon, where He healed a Gentile woman's daughter. Now He comes back toward the Sea "
        "of Galilee, goes up a mountain, and sits down. Henry says He sat there like a host waiting to welcome "
        "guests, waiting to be gracious. In the Gospels, when Jesus sits down on a mountain, something is about to "
        "happen.")
    ext(reader(bible, "Matthew", 15, 29, 31))
    add("[NARRATOR] (calm) Three verses, and in them the lame, the blind, the crippled, the mute and many others. "
        "Then, straight after, the feeding of the four thousand, because these people had been with Him three days "
        "and had nothing to eat.")
    add("[NARRATOR] (calm) The place. Edersheim puts this scene on the eastern side of the lake, in the Decapolis, "
        "the ten Greek cities, among people who were not strictly Jewish. That fits the last line, which says they "
        "glorified the God of Israel, the way outsiders speak of someone else's God. Other commentators put it on "
        "the western shore. Matthew says only the Sea of Galilee and a mountain. Either way it was steep, rocky "
        "ground above the water, and these people climbed it carrying each other.")
    add("[NARRATOR] (calm) Matthew Henry noticed two things. The people brought their sick relations and friends "
        "along with them and cast them down at Jesus's feet, and, he says, we read not of any thing they said to "
        "him. Their condition spoke for them. Every blind person on that hillside had been led up it by someone.")
    add("[BREAK]")

    add("[NARRATOR] (calm) Scripture gives us the crowd and the mountain and the three days. It does not give us "
        "one pair of them. We imagine a blind man and the friend who got him there. This is a scene, not Scripture.")
    add("[PAUSE 1.0]")
    add("[FRIEND] (calm) Rock here, big one, step up. Good. Now it levels off for a while.")
    add("[MAN] (calm) How many are up there? It sounds like a market.")
    add("[FRIEND] (calm) Hundreds. More coming up behind us. There are men carrying a boy on a door. A woman with "
        "a child who does not talk. Everybody.")
    add("[MAN] (curious) And him?")
    add("[FRIEND] (calm) Sitting on a rock at the top, like he has all day. People go up to him one at a time and "
        "then they, I do not know how to say it. They stand up different.")
    add("[MAN] (whisper) Wind up here. Thyme crushed under everyone's feet. The lake below, I can hear it even "
        "over the crowd. We have been walking since before dawn and my friend has not let go of my arm once.")
    add("[FRIEND] (calm) Nearly there. I am going to sit you down right in front of him. Then I will step back.")
    add("[MAN] (calm) Do not go far.")
    add("[FRIEND] (calm) I am not going anywhere. I did not carry you up a mountain to lose you at the top.")
    add("[PAUSE 2.0]")
    add("[NARRATOR] (calm) Matthew says they laid them at His feet, and He healed them.")
    add("[BREAK]")

    add(f"[NARRATOR] (dryly) {BRIAN_VOICE_NOTE}")
    add("[PAUSE 1.0]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[0]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[1]}")
    add("[BREAK]")

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

    add(f"[BRIAN] (calm) {DRAFT_BRIAN[2]}")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[3]}")
    add("[BREAK]")

    add("[NARRATOR] (calm) Set the two crowds side by side. On the mountain, in Gentile country, people laid their "
        "blind at His feet and glorified the God of Israel. In the Temple, the holiest ground in the Jewish world, "
        "the blind came to Him through the space where the market had been, and the men in charge were indignant. "
        "Different ground, different crowd, same thing in the middle: blind people, brought or coming, and Jesus "
        "healing them in front of everyone. Matthew wants us to see that it happened everywhere He went, and that "
        "the only people who minded were the ones who had been keeping the gate.")
    add("[BREAK]")
    add(f"[BRIAN] (calm) {DRAFT_BRIAN[4]}")
    add("[BREAK]")
    add(f"[NARRATOR] (calm) {CLOSE}")
    add("[NARRATOR] (after a long pause) For we walk by faith, not by sight.")
    return L
