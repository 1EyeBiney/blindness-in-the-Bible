"""The stories: catalog verses grouped into the passages they belong to.

A catalog row is one verse. A story is the whole passage around it: who
was there, what led up to it, what happened, and what came after. Each
story quotes the passage in full from the Berean Standard Bible.

Three kinds of writing sit in each story, and they are kept apart:

  around   what the surrounding chapters say led up to this moment
  happens  a short retelling of the passage itself
  shoes    what the text lets a reader notice from the blind person's side
  brian    (optional) Brian's own reflections, in his words, lightly
           edited for typing; kept verbatim in docs/BRIAN_NOTES.md
  place_and_time  (optional) the place and the time, drawn from the
           reference shelf (data/raw/shelf, see SOURCE.md there); each item
           names its source so a reader can go and check it

The first three parts are drawn from the passage and its near context
alone. The place-and-time part is the only one that uses outside works, and
every item in it is sourced. The "shoes" paragraphs are a first draft by
Claude for Brian to rework in his own voice.

`passages` are (book, chapter, first verse, last verse) and are quoted in
order. `outcome` is one of OUTCOMES.
"""
from __future__ import annotations

GROUPS = [
    ("not_restored", "Sight lost and not given back",
     "Six people who lost their sight and lived the rest of their lives without it. Four went blind in old age. "
     "Two were blinded by their enemies."),
    ("for_a_time", "Sight taken for a time",
     "Four accounts where sight is taken suddenly, and in three of them it returns."),
    ("given", "Sight given by Jesus",
     "The healing accounts in the Gospels, from single encounters told in detail to crowds mentioned in a line."),
    ("among", "Blind people among the crowd and at the table",
     "Passages where blind people are present, named as a group, threatened, cared for, or invited."),
]

OUTCOMES = {
    "not_restored": "Sight not restored",
    "restored": "Sight restored",
    "temporary": "Blind for a time",
    "prevented": "The blinding was prevented",
    "present": "No change in sight is described",
}

STORIES = [
    # ------------------------------------------------------------ not restored
    {
        "slug": "isaac", "title": "Isaac and the stolen blessing", "who": "Isaac", "group": "not_restored",
        "outcome": "not_restored",
        "passages": [("Genesis", 27, 1, 4), ("Genesis", 27, 18, 27), ("Genesis", 27, 30, 35)],
        "around": "Isaac is the son of Abraham and the father of twins, Esau and Jacob. Esau is the firstborn and his "
                  "father's favourite; Jacob is his mother Rebekah's. Isaac is old, cannot see, and believes he may "
                  "die soon, so he prepares to give Esau the blessing of the firstborn. Rebekah overhears and sends "
                  "Jacob in first, dressed in Esau's clothes with goatskins on his hands and neck.",
        "happens": "Jacob brings the meal and says he is Esau. Isaac is not sure. He asks how the hunt went so "
                   "quickly, asks to touch him, says the voice is Jacob's but the hands are Esau's, asks again, and "
                   "finally smells his clothing. Then he gives the blessing. Esau comes in moments later, and Isaac "
                   "trembles violently when he understands what has happened.",
        "shoes": "Isaac does everything a blind man can do to be sure. He questions, he listens, he touches, he "
                 "smells. He notices that the voice is wrong and says so out loud. What defeats him is not his "
                 "blindness but his own family, who know exactly which senses he will rely on and prepare a "
                 "disguise for each one. The passage shows what it is to depend on the honesty of the people in "
                 "the room, and what it feels like when that trust is used against you.",
        "brian": [
            "Isaac suffered from more than vision loss if he could not tell the difference in a man's hands. His "
            "sense of touch must also have been affected. The voice he could tell apart, which is standard, and smell "
            "can be fooled by clothing, but feeling a person's hand, covered in wool or not, would be difficult to fool.",
            "Later, Jacob proves the point by knowingly placing his hands on the opposite sons of Joseph.",
        ],
    },
    {
        "slug": "jacob", "title": "Jacob blesses Joseph's sons", "who": "Jacob (Israel)", "group": "not_restored",
        "outcome": "not_restored",
        "passages": [("Genesis", 48, 8, 20)],
        "around": "Many years after deceiving his blind father, Jacob is himself old and can hardly see. He is in "
                  "Egypt, reunited with his son Joseph, whom he had long believed dead. Joseph brings his two sons, "
                  "Manasseh the elder and Ephraim the younger, to be blessed before Jacob dies.",
        "happens": "Joseph places the boys so that Jacob's right hand, the hand of the greater blessing, will fall on "
                   "the firstborn. Jacob crosses his arms and puts his right hand on the younger. Joseph thinks his "
                   "father has made a mistake and tries to move the hand. Jacob refuses: \"I know, my son, I know!\"",
        "shoes": "Joseph assumes that because his father cannot see, he does not know what he is doing. It is a "
                 "familiar moment: a sighted person reaching in to correct a blind person who has made a deliberate "
                 "choice. Jacob does not explain himself at length. He simply says that he knows. The man who once "
                 "took advantage of a blind father now shows that blindness and understanding are different things.",
    },
    {
        "slug": "eli", "title": "Eli at Shiloh", "who": "Eli", "group": "not_restored", "outcome": "not_restored",
        "passages": [("1 Samuel", 3, 1, 18), ("1 Samuel", 4, 12, 18)],
        "around": "Eli is the priest at Shiloh, where the ark of God is kept. He has raised the boy Samuel in the "
                  "house of the LORD. His own sons, also priests, have abused their office, and Eli has not stopped "
                  "them. A man of God has already told him that judgment is coming on his family.",
        "happens": "In the night the LORD calls Samuel three times, and each time the boy runs to Eli. It is Eli who "
                   "works out who is calling and tells Samuel how to answer. In the morning he insists on hearing the "
                   "message, though it is a judgment on his own house, and accepts it. Later, at ninety-eight, he "
                   "sits by the road waiting for news of the battle. He hears the city cry out, hears that his sons "
                   "are dead and the ark is taken, falls from his seat, and dies.",
        "shoes": "Twice the text places Eli by what he can and cannot do. In the night he cannot see, yet he is the "
                 "one who recognizes the voice of God when the sighted boy does not. At the gate he sits \"watching\" "
                 "with a fixed gaze, and everything reaches him by sound: first the outcry of the city, then the "
                 "runner's words. He has to ask what the commotion means. Waiting for news that everyone else can "
                 "already see on a messenger's torn clothes is its own kind of helplessness.",
    },
    {
        "slug": "ahijah", "title": "Ahijah and the disguised queen", "who": "Ahijah the prophet", "group": "not_restored",
        "outcome": "not_restored",
        "passages": [("1 Kings", 14, 1, 13)],
        "around": "Ahijah is the prophet who years earlier told Jeroboam he would be king over the northern tribes. "
                  "Jeroboam has since led the people into idolatry. Now his son is sick, and he sends his wife to "
                  "Ahijah in disguise, with gifts, to learn whether the boy will live.",
        "happens": "Ahijah cannot see because of his age. Before the queen arrives, the LORD tells him who is coming, "
                   "why, and that she will be disguised. When he hears her footsteps at the door he greets her by "
                   "name and asks why she is pretending. Then he gives her the hard message for her husband.",
        "shoes": "The text is careful about how Ahijah knows. It does not say he recognized her footsteps; it says the "
                 "LORD had told him who was coming and that she would be disguised, and that he spoke when he heard "
                 "feet at the door. His eyes were dim with age, which may mean low vision rather than none, so a "
                 "visual disguise might have had some point. Of everyone in the passage, the man who cannot see "
                 "well is the one who knows the situation as it is, and he knows it because he was told.",
        "brian": [
            "It does not say that he recognized the sound of her feet. He likely did not, unless he had been doing "
            "this a long time. Besides, he was probably low vision and could still see a little, and the disguise "
            "might have been visual enough to hide her true appearance.",
            "I can tell Barb's sound if she wears certain shoes, but often in areas without context it is "
            "difficult to pick out her footsteps among others.",
        ],
    },
    {
        "slug": "samson", "title": "Samson in Gaza", "who": "Samson", "group": "not_restored", "outcome": "not_restored",
        "passages": [("Judges", 16, 18, 31)],
        "around": "Samson has judged Israel for twenty years and has been the Philistines' great enemy. His strength "
                  "is bound up with a vow marked by his uncut hair. Delilah, paid by the Philistine lords, presses "
                  "him day after day until he tells her the secret.",
        "happens": "His hair is cut while he sleeps, and his strength is gone. The Philistines seize him, gouge out "
                   "his eyes, shackle him, and set him to grinding grain in prison. Later they bring him out to "
                   "entertain a crowd at a feast for their god. He asks the servant holding his hand to lead him to "
                   "the pillars, prays for strength once more, and brings the building down on himself and them.",
        "shoes": "Samson is the one person in Scripture who becomes blind in the prime of his strength, in a single "
                 "violent moment. The text follows what comes after: the prison, the repetitive labour, being led "
                 "by the hand by a servant, being put on display for people who are laughing. He has to ask to be "
                 "guided to where he can feel the pillars. His last prayer names his loss directly: he asks to be "
                 "avenged \"for my two eyes.\" He is never healed, and God still hears him.",
    },
    {
        "slug": "zedekiah", "title": "Zedekiah, the last king of Judah", "who": "Zedekiah", "group": "not_restored",
        "outcome": "not_restored",
        "passages": [("2 Kings", 25, 1, 7), ("Jeremiah", 39, 4, 7), ("Jeremiah", 52, 8, 11)],
        "around": "Zedekiah is the last king to reign in Jerusalem. He has rebelled against Babylon against the "
                  "repeated warnings of the prophet Jeremiah. Nebuchadnezzar's army has besieged the city for well "
                  "over a year, and the people are starving.",
        "happens": "The wall is breached and the king flees by night. He is caught near Jericho, his army scatters, "
                   "and he is taken before the king of Babylon. His sons are killed in front of him. Then his eyes "
                   "are put out, and he is taken in chains to Babylon, where he remains until he dies.",
        "shoes": "The order of events is the cruelty. The last thing Zedekiah is allowed to see is the death of his "
                 "sons, and then he is blinded so that it stays the last thing. Blinding here is a weapon, chosen by "
                 "a conqueror to break a man and to shame a nation. The account is told three times in Scripture, "
                 "in nearly the same words each time.",
    },
    # ------------------------------------------------------------ for a time
    {
        "slug": "men-of-sodom", "title": "The men at Lot's door", "who": "The men of Sodom", "group": "for_a_time",
        "outcome": "temporary",
        "passages": [("Genesis", 19, 1, 11)],
        "around": "Two angels arrive in Sodom in the evening and Lot takes them into his house. The men of the city "
                  "surround the house and demand that the visitors be handed over to them.",
        "happens": "Lot goes out and pleads with the crowd. They turn on him and press in to break down the door. "
                   "The visitors pull Lot inside and strike the men at the entrance with blindness, so that they "
                   "wear themselves out trying to find the door.",
        "shoes": "This is blindness used as a shield for the people inside, not as a description of anyone's life. "
                 "It is worth noticing what the men do: they keep groping for the door. The sudden loss of sight "
                 "does not change what they want.",
    },
    {
        "slug": "aramean-raiders", "title": "Elisha and the Aramean raiders", "who": "The Aramean raiders",
        "group": "for_a_time", "outcome": "restored",
        "passages": [("2 Kings", 6, 8, 23)],
        "around": "The king of Aram is at war with Israel, and the prophet Elisha keeps warning Israel's king where "
                  "the Aramean army will be. The king of Aram sends horses, chariots and a great army by night to "
                  "seize Elisha in the town of Dothan.",
        "happens": "Elisha's servant sees the army and is afraid. Elisha prays that the servant's eyes be opened, and "
                   "he sees the hills full of horses and chariots of fire. Then Elisha prays that the soldiers be "
                   "struck with blindness. He leads them to Samaria, the enemy capital, and prays that their eyes be "
                   "opened. The king of Israel wants to kill them. Elisha has them fed and sent home.",
        "shoes": "Sight and blindness trade places three times in a few verses. The servant can see and misses "
                 "what is there. The soldiers cannot see and are led, trusting the very man they came to capture. "
                 "When their sight returns they find themselves helpless, and they are given a feast. It is one of "
                 "the few places where being led while blind ends in mercy.",
    },
    {
        "slug": "saul-on-the-damascus-road", "title": "Saul on the road to Damascus", "who": "Paul (Saul)",
        "group": "for_a_time", "outcome": "restored",
        "passages": [("Acts", 9, 1, 19), ("Acts", 22, 6, 16)],
        "around": "Saul is a young Pharisee who has been arresting followers of Jesus. He is travelling to Damascus "
                  "with letters authorizing him to bring more of them back to Jerusalem as prisoners.",
        "happens": "A light from heaven flashes around him near the city. He falls, hears Jesus speak to him, and "
                   "gets up unable to see. His companions lead him by the hand into Damascus. For three days he is "
                   "without sight and does not eat or drink. A disciple named Ananias, afraid of him at first, is "
                   "sent to lay hands on him. Something like scales falls from his eyes, he sees again, and he is "
                   "baptized. Years later Paul tells the story himself in Acts 22.",
        "shoes": "A grown man, capable and in command of a mission, loses his sight in an instant and has to be led "
                 "by the hand. For three days he does not know whether it will come back. The text says only that "
                 "he was praying. He must then let a stranger, one of the people he came to arrest, put hands on "
                 "him. Ananias's first words are \"Brother Saul.\" Of all the accounts, this is the nearest to losing "
                 "sight in the middle of life, though for Saul it lasted three days.",
    },
    {
        "slug": "elymas", "title": "Elymas the sorcerer", "who": "Elymas (Bar-Jesus)", "group": "for_a_time",
        "outcome": "temporary",
        "passages": [("Acts", 13, 6, 12)],
        "around": "Paul and Barnabas are on Cyprus on their first journey. The Roman proconsul, Sergius Paulus, wants "
                  "to hear the word of God. His attendant, a sorcerer called Elymas, tries to turn him away from it.",
        "happens": "Paul confronts Elymas and tells him he will be blind for a time. Mist and darkness come over "
                   "him at once, and he gropes about looking for someone to lead him by the hand. The proconsul "
                   "believes.",
        "shoes": "Paul gives Elymas exactly what Paul himself was once given: blindness for a time, and the need "
                 "to be led by the hand. The same phrase is used of both men. The text does not say what became "
                 "of Elymas or whether, like Paul, it changed him.",
    },
    # ------------------------------------------------------------ given
    {
        "slug": "two-blind-men", "title": "Two blind men follow Jesus", "who": "Two blind men (Galilee)",
        "group": "given", "outcome": "restored",
        "passages": [("Matthew", 9, 27, 31)],
        "around": "Jesus has just raised a synagogue leader's daughter, and news of it is spreading through the "
                  "region. As He leaves, two blind men follow Him.",
        "happens": "They follow Him along the road calling out for mercy, and follow Him into the house. He asks "
                   "whether they believe He is able to do this. They say yes. He touches their eyes, and their eyes "
                   "are opened. He tells them sternly to keep it quiet. They tell everyone.",
        "shoes": "Two blind men following a moving crowd down a road and into a house are doing it by sound and by "
                 "each other. Jesus does not act on the road. He waits until they have come all the way in, then "
                 "asks them a question before He does anything: do you believe? They are treated as people with "
                 "something to say, not as a problem to be fixed in passing.",
    },
    {
        "slug": "blind-and-mute-man", "title": "A man who was blind and mute", "who": "A blind and mute man",
        "group": "given", "outcome": "restored",
        "passages": [("Matthew", 12, 22, 24)],
        "around": "Jesus is healing many and is in growing conflict with the Pharisees over the Sabbath.",
        "happens": "A man who is blind and mute, and described as demon-possessed, is brought to Jesus. He heals him "
                   "so that he can speak and see. The crowd wonders whether this is the Son of David. The Pharisees "
                   "say He does it by the prince of demons.",
        "shoes": "This man cannot see and cannot speak, so he cannot come on his own or ask for himself. Others "
                 "bring him. The whole account is one verse, and then the argument about Jesus takes over. The man "
                 "himself is never heard from, even after he can speak.",
    },
    {
        "slug": "bethsaida", "title": "The blind man at Bethsaida", "who": "The blind man at Bethsaida",
        "group": "given", "outcome": "restored",
        "passages": [("Mark", 8, 22, 26)],
        "around": "Jesus has just fed four thousand and has rebuked His disciples in the boat for not understanding: "
                  "\"Having eyes, do you not see?\" They land at Bethsaida.",
        "happens": "People bring a blind man and beg Jesus to touch him. Jesus takes him by the hand and leads him "
                   "out of the village. He puts saliva on his eyes, lays hands on him, and asks whether he can see "
                   "anything. The man says he sees people, but they look like trees walking. Jesus lays hands on "
                   "him again, and he sees clearly. Jesus sends him home and tells him not to go back into the "
                   "village.",
        "shoes": "This is the only healing told in two stages, and the only one where Jesus asks how it is going. "
                 "He leads the man by the hand Himself, away from the people watching. The man answers honestly "
                 "that it is not right yet. Anyone who has lived with partial or changing sight will recognize "
                 "\"people like trees walking\": seeing something, but not enough to trust. That he knows what trees "
                 "look like suggests he had once seen.",
    },
    {
        "slug": "bartimaeus", "title": "Bartimaeus at Jericho", "who": "Bartimaeus", "group": "given",
        "outcome": "restored",
        "passages": [("Mark", 10, 46, 52), ("Luke", 18, 35, 43), ("Matthew", 20, 29, 34)],
        "around": "Jesus is on His last journey to Jerusalem, a few days before His death, with a large crowd "
                  "travelling with Him. Three Gospels tell this account. Mark names the man. Matthew speaks of two "
                  "blind men. Luke places it as Jesus approaches Jericho, the others as He leaves.",
        "happens": "A blind beggar sitting by the road hears the crowd and asks what is happening. Told that Jesus "
                   "of Nazareth is passing, he shouts for mercy. People tell him to be quiet, and he shouts louder. "
                   "Jesus stops and has him called. He throws off his cloak, jumps up, and comes. Jesus asks, "
                   "\"What do you want Me to do for you?\" He answers, \"Let me see again.\" He receives his sight "
                   "and follows Jesus along the road.",
        "shoes": "Bartimaeus learns everything by ear. He hears a crowd, has to ask someone what it is, and has one "
                 "chance to be heard before it passes. The people around him try to silence him, and then, once "
                 "Jesus has noticed him, the same people tell him to take courage. He leaves his cloak behind, "
                 "which for a beggar may be most of what he owns. Jesus does not assume what he wants. He asks. "
                 "And the word \"again\" suggests a man who once could see and lost it.",
    },
    {
        "slug": "man-born-blind", "title": "The man born blind", "who": "The man born blind", "group": "given",
        "outcome": "restored",
        "passages": [("John", 9, 1, 41)],
        "around": "Jesus is in Jerusalem and has just escaped an attempt to stone Him in the temple. Walking along, "
                  "He sees a man who has been blind from birth and who sits and begs. It is the Sabbath.",
        "happens": "The disciples ask whose sin caused the blindness, the man's or his parents'. Jesus says neither. "
                   "He makes mud, puts it on the man's eyes, and sends him to wash in the Pool of Siloam. He comes "
                   "back seeing. His neighbours argue over whether he is the same man. The Pharisees question him, "
                   "then his parents, then him again. He will not say what they want him to say, and they throw him "
                   "out. Jesus goes and finds him, and the man believes and worships.",
        "shoes": "This is the longest account of a blind person in Scripture, and most of it happens after the "
                 "healing. While he is blind, people talk about him in front of him as a question in theology. "
                 "Once he can see, his neighbours doubt he is the same person, his parents are afraid to stand "
                 "with him, and the authorities call him a liar and a sinner. Through it all he holds to the one "
                 "thing he knows: \"I was blind, but now I see!\" He also walked to the pool with mud on his eyes, "
                 "still blind, on the word of a man he had never seen. And when everyone else has put him out, "
                 "Jesus comes looking for him.",
        "brian": [
            "This one makes me cry because of what Jesus first says: \"Neither this man nor his parents sinned, but "
            "this happened so that the works of God would be displayed in him.\" That is what I pray for daily: that "
            "God uses my blindness for His glory in the things I do, the things I say, and the way I treat others, "
            "especially those who need help the most and who have, according to many, absolutely nothing to give back.",
            "One of my first true walk-by-faith moments came during rehabilitation training at the Hines VA hospital "
            "outside Chicago. At the end of training I did a drop-off test: I was let out of a car in a suburban "
            "business district with the task of finding a grocery store about five blocks away on my own. Unless I got "
            "into serious physical danger, I was not to be helped. I had to trust my new skills to make that trip "
            "without any sight. It was terrifying, exhilarating and liberating all at once. I think of the man born "
            "blind making his way to the Pool of Siloam, on faith.",
            "He was blind from birth and had never had sight. From a physiological standpoint his visual cortex would "
            "never have developed; it takes a child about six years of seeing to learn to tell faces apart. He washed "
            "the mud off and \"received\" sight. Jesus did not only heal the eyes; He must have given the man a way to "
            "process what the eyes now sent. We have accounts of people who regained sight or got it for the first "
            "time and could not make sense of the images. Mike May, who had sight restored as an adult, still cannot "
            "recognize faces and still uses braille and mobility aids.",
            "People did not recognize him, and I think that is partly the sheer size of what had happened. If I walked "
            "up to someone who has only known me blind and suddenly I could see, I would talk differently and carry "
            "myself differently. I would still turn my head toward sounds, that is natural, but I would react to visual "
            "cues I do not react to now.",
            "The Pharisees went straight to whether the healing was lawful, not whether it had happened.",
            "When the parents said \"Ask him. He is old enough to speak for himself,\" it was for the wrong reason, "
            "fear, but notice what it is. Usually a blind person's escort gets asked what the blind person wants. This "
            "may be the first recorded moment of self-advocacy for a blind man, and it was unintentional.",
            "The way he argues with the Pharisees is simply amazing. He would never have had access to Scripture or "
            "learning, and yet with a plain explanation he cuts through the arguments of the experts, in Jerusalem, "
            "and wins. That he would even speak back to a Pharisee is remarkable. His parents were obviously terrified.",
            "It is hard to express what that man must have felt when he finally recognized Jesus, after Jesus sought "
            "him out. I am so grateful to Jesus for what He did for that one blind man.",
            "A common plea was \"Gain merit by me.\" How humbling, to call out in effect: I have so little to offer you "
            "that your kindness to me will gain you righteousness. In Nigeria today, by the figures I have seen, "
            "about seventy percent of blind people still have to beg to survive.",
        ],
        "place_and_time": [
            {"text": "The Pool of Siloam lies at the south end of Jerusalem, at the lowest point of the ancient city. "
                     "Josephus, who knew the city before it fell, calls Siloam \"a fountain which hath sweet water in it, "
                     "and this in great plenty also.\"",
             "source": "Josephus, The Wars of the Jews, Book V, chapter 4, section 1 (Whiston translation)."},
            {"text": "The water comes from the Gihon spring in the Kidron Valley through a tunnel cut by King Hezekiah, so "
                     "that a besieging army could not reach the spring and the city could still drink. Edersheim adds "
                     "that this explains the name: Siloam, \"sent,\" a conduit.",
             "source": "Edersheim, The Life and Times of Jesus the Messiah, Book IV, chapter VII; compare 2 Kings 20:20 "
                       "and 2 Chronicles 32:30."},
            {"text": "The pool Jesus sent the man to was lost for nineteen centuries. In 2004, workers repairing a sewer "
                     "uncovered stone steps, and archaeologists Ronny Reich and Eli Shukron identified the pool of the "
                     "Second Temple period: a large stone-lined basin with steps on at least three sides, built in sets "
                     "of five, apparently for changing water levels. It was destroyed when Jerusalem fell in 70 AD and "
                     "buried under silt. Pilgrims arriving for the feasts likely washed there before climbing to the "
                     "Temple, so it may have served as a ritual bath.",
             "source": "Wikipedia, \"Pool of Siloam,\" revision of 20 June 2026 (CC BY-SA 4.0)."},
            {"text": "Siloam had a place in the feast that frames John 7 to 9. At the Feast of Tabernacles a priest went "
                     "down in procession to the pool, filled a golden pitcher, and carried the water back up to pour on "
                     "the altar while the trumpets sounded. Edersheim places this healing on the Sabbath just after that "
                     "feast ended, with Jesus on His way into the Temple. The man was being sent to wash in water the "
                     "whole city had just watched carried up to God.",
             "source": "Edersheim, The Life and Times of Jesus the Messiah, Book IV, chapters VII and IX."},
            {"text": "Blind beggars were a familiar sight. The Temple entrance was the chosen place for those who asked "
                     "for alms, and a common plea was \"Gain merit by me.\" The blind were held to be specially entitled "
                     "to charity. Eye disease was common and there was no real treatment; the Bible encyclopedia of 1915 "
                     "names the lack of any remedy for ophthalmia as one reason begging was so widespread.",
             "source": "Edersheim, The Life and Times of Jesus the Messiah, Book IV, chapter IX; International Standard "
                       "Bible Encyclopedia (1915), entries \"Begging\" and \"Blindness.\""},
            {"text": "The disciples' question was a common one. Edersheim writes that rabbis meeting such a person "
                     "would ask by what sin the affliction had come, and that it was a widespread view that the merits "
                     "or faults of parents showed in their children. Jesus's answer in verse 3 cut across both ideas.",
             "source": "Edersheim, The Life and Times of Jesus the Messiah, Book IV, chapter IX."},
            {"text": "Jesus used saliva and mud. Edersheim notes that saliva was commonly thought to help diseases of the "
                     "eye, and that making clay and anointing on the Sabbath were among the things the religious teachers "
                     "counted as work, which is why the day matters so much in the argument that follows.",
             "source": "Edersheim, The Life and Times of Jesus the Messiah, Book IV, chapter IX."},
        ],
    },
    {
        "slug": "the-temple", "title": "The blind and the lame in the temple", "who": "The blind and the lame in the temple",
        "group": "given", "outcome": "restored",
        "passages": [("Matthew", 21, 12, 16)],
        "around": "Jesus has entered Jerusalem to shouts of \"Hosanna.\" He goes into the temple courts and drives out "
                  "those buying and selling.",
        "happens": "With the tables overturned, the blind and the lame come to Him in the temple, and He heals them. "
                   "Children shout His praise. The chief priests and scribes are indignant.",
        "shoes": "A thousand years earlier a saying had grown up in this same city: \"The blind and the lame will "
                 "never enter the palace\" (2 Samuel 5:8). Here they come to Him inside the temple itself, and He "
                 "receives them. Matthew sets the two groups side by side: those who had been kept at a distance "
                 "come in, and those in charge are angry about it.",
    },
    {
        "slug": "crowds-by-the-sea", "title": "The crowds on the mountain", "who": "Crowds by the Sea of Galilee",
        "group": "given", "outcome": "restored",
        "passages": [("Matthew", 15, 29, 31)],
        "around": "Jesus has returned from the region of Tyre and Sidon to the Sea of Galilee. He goes up a mountain "
                  "and sits down. The feeding of the four thousand follows.",
        "happens": "Large crowds bring the lame, the blind, the crippled, the mute and many others and lay them at "
                   "His feet. He heals them, and the crowd glorifies the God of Israel.",
        "shoes": "No one here has a name. What the text does show is how they arrived: brought by others, up a "
                 "mountain, and laid at His feet. Behind each of them is someone who decided to make that climb "
                 "with them.",
    },
    {
        "slug": "answer-to-john", "title": "Jesus's answer to John the Baptist", "who": "Jesus's answer to John the Baptist",
        "group": "given", "outcome": "restored",
        "passages": [("Matthew", 11, 2, 6), ("Luke", 7, 18, 23)],
        "around": "John the Baptist is in prison. He sends his disciples to ask Jesus whether He is the One who was "
                  "to come.",
        "happens": "Luke says that at that very hour Jesus healed many and gave sight to many who were blind. Then "
                   "He tells John's messengers to report what they have seen and heard, and the first thing on the "
                   "list is that the blind receive sight.",
        "shoes": "When asked for proof of who He is, Jesus points to what is happening to blind people, lame people, "
                 "deaf people and the poor. His words echo the promise in Isaiah 35:5. The blind are not at the "
                 "edge of His work. They are the first evidence He offers.",
    },
    # ------------------------------------------------------------ among
    {
        "slug": "pool-of-bethesda", "title": "The pool of Bethesda", "who": "The sick at the pool of Bethesda",
        "group": "among", "outcome": "present",
        "passages": [("John", 5, 1, 9)],
        "around": "Jesus is in Jerusalem for a feast. Near the Sheep Gate is a pool with five covered walkways.",
        "happens": "A great number of people lie there: the sick, the blind, the lame and the paralyzed. Jesus speaks "
                   "to one man, who has been unable to walk for thirty-eight years and has no one to help him into "
                   "the water. Jesus tells him to get up and walk, and he does.",
        "shoes": "The man healed here is lame, not blind. The blind are part of the crowd left lying on the "
                 "walkways. The passage gives a picture of where disabled people gathered in the city, and the "
                 "man's own words describe the place: no one to help, and someone else always getting there first. "
                 "It is a different town from Bethsaida, where the blind man of Mark 8 was healed; the names are "
                 "easily confused.",
    },
    {
        "slug": "the-banquet", "title": "The guests at the banquet", "who": "Guests at the banquet", "group": "among",
        "outcome": "present",
        "passages": [("Luke", 14, 12, 24)],
        "around": "Jesus is eating on the Sabbath at the house of a leading Pharisee, and the guests have been "
                  "choosing the places of honour.",
        "happens": "Jesus tells His host to invite the poor, the crippled, the lame and the blind, who cannot repay "
                   "him. Then He tells a parable of a great banquet whose invited guests make excuses. The master "
                   "sends his servant into the streets to bring in the poor, the crippled, the blind and the lame.",
        "shoes": "The same four groups are named twice, once as an instruction and once in a story. In both, blind "
                 "people are not objects of charity outside the door. They are guests at the table, wanted for "
                 "their company, with nothing expected in return.",
    },
    {
        "slug": "the-return", "title": "The blind and the lame come home", "who": "The blind and the lame among the returning exiles",
        "group": "among", "outcome": "present",
        "passages": [("Jeremiah", 31, 7, 9)],
        "around": "Jeremiah has spent years warning that Jerusalem will fall. In these chapters he speaks of what "
                  "comes after: God will bring His scattered people back.",
        "happens": "The LORD says He will gather them from the farthest parts of the earth, and He names who will be "
                   "in the company: the blind and the lame, pregnant women and women in labour. He will lead them "
                   "on a level path where they will not stumble.",
        "shoes": "A long journey on foot is hardest for exactly the people listed. God names them first, and then "
                 "describes the road He will make for them: level, beside water, with no stumbling. The pace of "
                 "the whole company is set by those who travel slowest.",
    },
    {
        "slug": "job", "title": "Job: eyes to the blind", "who": "Job", "group": "among", "outcome": "present",
        "passages": [("Job", 29, 11, 17)],
        "around": "Job has lost his children, his wealth and his health. In this speech he remembers his life "
                  "before, and defends how he lived it.",
        "happens": "Among the things he lists: he rescued the poor, helped the fatherless and the widow, took up the "
                   "stranger's case, and \"served as eyes to the blind and as feet to the lame.\"",
        "shoes": "This is the view from the other side: what a good neighbour to a blind person looks like, in the "
                 "words of a man Scripture calls blameless. He does not say he pitied the blind. He says he "
                 "served as their eyes.",
    },
    {
        "slug": "jabesh-gilead", "title": "The threat at Jabesh-gilead", "who": "The men of Jabesh-gilead",
        "group": "among", "outcome": "prevented",
        "passages": [("1 Samuel", 11, 1, 11)],
        "around": "Saul has just been chosen as Israel's first king, and not everyone accepts him. An Ammonite king, "
                  "Nahash, besieges the town of Jabesh-gilead.",
        "happens": "The town offers to surrender. Nahash agrees on one condition: that he put out the right eye of "
                   "every man, to bring shame on all Israel. They ask for seven days. When Saul hears, he raises "
                   "an army and destroys the Ammonite camp before the sentence can be carried out.",
        "shoes": "Like Zedekiah's story, this shows blinding used deliberately as humiliation. All Israel weeps at "
                 "the news. The threat is what first moves Saul to act as king.",
    },
    {
        "slug": "the-jebusite-taunt", "title": "The taunt at Jerusalem", "who": "The blind and the lame of Jerusalem",
        "group": "among", "outcome": "present",
        "passages": [("2 Samuel", 5, 6, 10)],
        "around": "David has just become king over all Israel and marches on Jerusalem, a fortress still held by the "
                  "Jebusites.",
        "happens": "The Jebusites mock him: even the blind and the lame could keep him out. David takes the city, "
                   "and a saying follows: \"The blind and the lame will never enter the palace.\"",
        "shoes": "This is a hard passage, and readers do not agree on what it means. Blind and lame people are used "
                 "as an insult by one side and named with contempt by the other. It is included because it is in "
                 "the text, and because of what happens in the same city in Matthew 21:14, when the blind and the "
                 "lame come to Jesus in the temple and He heals them.",
    },
]
