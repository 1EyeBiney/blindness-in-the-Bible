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
        "life": "Isaac is the son Abraham and Sarah waited twenty-five years for, the boy bound on the altar at "
                "Moriah and spared. At forty he married Rebekah, brought from Haran by his father's servant, and "
                "twenty more years passed before the twins came; before they were born Rebekah was told that the "
                "older would serve the younger (Genesis 25). Esau grew up a hunter and his father's favourite, Jacob "
                "stayed among the tents and was his mother's, and one day Esau came in famished and sold his "
                "birthright for a bowl of stew. Isaac's own life repeated his father's: a famine, a stay among the "
                "Philistines at Gerar, where he told the men that Rebekah was his sister, as Abraham had said of "
                "Sarah, and was found out when the king looked down from a window and saw him caressing her "
                "(Genesis 26). He reopened his father's wells, quarrelled over them, prospered, and settled at "
                "Beersheba. Esau married two Hittite women who were a grief to both parents. Then comes the chapter "
                "on this page. After it, Esau resolves to kill his brother once their father is dead; Rebekah sends "
                "Jacob to her brother Laban in Haran, telling Isaac it is to find a wife, and Isaac blesses Jacob "
                "again, this time knowing who he is (Genesis 28). Jacob is gone twenty years. When he comes back he "
                "finds his father at Hebron, and when Isaac dies at a hundred and eighty, Esau and Jacob bury him "
                "together (Genesis 35).",
        "threads": [("seen-and-unseen.html", "Seen and unseen: the deceits of Genesis")],
        "sight": "Genesis says Isaac's eyes were so weak that he could no longer see. That is the Bible's way of describing sight lost to age, and it may mean dim sight rather than none. Either way, the story turns on what he could not see, and the page reads it that way. See what blind means here.",
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
        "senses": "Count the senses in the room. Hearing: the voice is right, and Isaac says so; it is the one "
                  "sense that is not fooled, and he overrules it. Touch: the hands are hairy, as Esau's are, "
                  "because Rebekah has thought of touch before he has. Smell: the clothes are Esau's own, and the "
                  "smell of the field decides him. Taste: the meal is what he asked for. Four senses out of five "
                  "report Esau, and three of them have been dressed for the purpose. A blind person lives by exactly "
                  "this kind of cross-checking, and it works most days. This is the Bible's record of the day it "
                  "did not, and the reason it did not is not the man's senses. It is that every one of them was "
                  "being managed by people who knew him.",
        "before_after": "Isaac was sixty when the twins were born and lived to a hundred and eighty, so the blind "
                        "old man who said he did not know the day of his death had decades left. Esau was forty "
                        "when he married, before this chapter, which puts Isaac past a hundred here; Jacob's "
                        "twenty years with Laban all fell inside his father's lifetime, and when Jacob came home "
                        "Isaac was still alive to be buried by both sons together. Nothing in Genesis says his "
                        "sight ever came back.",
        "came_of_it": "Brian asked whether the stolen blessing went unpunished. Genesis answers in Jacob's own "
                      "currency. Seven years later, in the dark of a wedding night, Laban gives him Leah in place of "
                      "Rachel, and in the morning Jacob asks, \"Why have you deceived me?\" Laban's answer is that the "
                      "younger does not go before the older. Matthew Henry, around 1706, put it in a sentence: Jacob "
                      "was paid in his own coin; he had cheated his own father when he pretended to be Esau, and now "
                      "his father-in-law cheated him. Years after that, Jacob's sons bring him Joseph's robe dipped "
                      "in the blood of a goat, and he, like his father, is deceived by a garment and a goat. Rebekah "
                      "told Jacob she would send for him when Esau's anger passed; Genesis never records that she saw "
                      "him again. And Hebrews 12 says of Esau that he could find no ground for repentance, though he "
                      "sought the blessing with tears. None of this undoes what was done to Isaac. The blessing "
                      "stood, as he said it would. But the Bible does not let the deceit pass as if no one saw it.",
        "brian": [
            "This page brings home the reality of the trust we place in the people around us, especially as the other "
            "senses start to fail. Isaac did everything right. He asked, he listened, he reached out, he smelled the "
            "clothes. And the people he trusted had prepared for every one of those.",
            "When I first read this, my thought was that Isaac's sense of touch must have failed along with his sight, "
            "because how else could goatskin pass for a man's hands? I have changed my mind, and the reason is my own "
            "hands. Mine sit in conditioned air all day on a keyboard. My wife Barb says they are soft as a baby's "
            "bottom. Isaac's were not. He had spent a hundred years outdoors among flocks and tents and wells, doing "
            "hard work for meagre provision. Hands like that do not feel fine detail the way mine do. Josephus says the "
            "twins differed only in their hairiness. Put a goatskin under a hand like Isaac's and it is not the stretch "
            "it sounds.",
            "It helps to remember where he was. Beersheba was his place. He had reopened his father's well there and "
            "named it, and he was still there decades later when Jacob left. A blind man in a camp he has known for "
            "half a lifetime is a different man from one set down in a strange room. He would have known his tent, "
            "his way to the door, who usually came and went. That is part of why the deceit worked. Nothing about the "
            "day was strange except the one thing that mattered.",
            "The detail that stays with me is Esau's voice. A few minutes earlier Isaac had picked out Jacob's voice "
            "through a disguise, so his hearing was fine. Yet when Esau walked in, Isaac asked, \"Who are you?\" "
            "Nothing was wrong with his ears. What had changed was what he expected. He had just blessed Esau and sent "
            "him out, so the man coming in could not be Esau. I call this context. My ears tell me a great deal, but "
            "what I expect to hear tells me almost as much, and when the two disagree, expectation often wins. It won "
            "twice in one hour for Isaac.",
            "I asked whether all this went unpunished, and the answer is on this page now under What came of it. It "
            "does not undo what happened to Isaac. But it tells me that someone saw.",
            "One more thing. You hear it all day long: look before you leap, look both ways, watch out. Sight is the "
            "sense people trust without thinking. This chapter is about a man who had to trust the others instead, "
            "and who was let down not by his senses but by his family.",
        ],

    },
    {
        "slug": "jacob", "title": "Jacob blesses Joseph's sons", "who": "Jacob (Israel)", "group": "not_restored",
        "outcome": "not_restored",
        "passages": [("Genesis", 48, 8, 20)],
        "life": "Jacob left home as the deceiver of the Isaac page and spent twenty years with his uncle Laban in "
                "Haran. He worked seven years for Rachel and woke beside Leah, whom Laban had brought to him in the "
                "dark, then worked seven more (Genesis 29). Between the two sisters and their maids he had eleven "
                "sons and a daughter there; Rachel, long barren, bore Joseph last. He came home rich in flocks, "
                "wrestled through a night at the Jabbok and was given the name Israel and a limp, and met Esau, who "
                "ran to embrace him (Genesis 32 and 33). Rachel died on the road giving birth to Benjamin. Jacob "
                "favoured Joseph, Rachel's firstborn, and gave him the robe; Joseph's brothers sold him into Egypt "
                "and brought their father the robe dipped in a goat's blood, and Jacob mourned a living son for some "
                "twenty years (Genesis 37). Famine sent the brothers down to Egypt for grain, to a governor they did "
                "not recognise. When at last they came home saying Joseph was alive, Jacob did not believe them until "
                "he saw the wagons. He went down to Egypt at a hundred and thirty, Joseph wept on his neck, and he "
                "told Pharaoh his years had been few and hard (Genesis 46 and 47). He lived seventeen years in "
                "Goshen. Then comes the chapter on this page, his eyesight poor with age, and in the next he blesses "
                "all twelve sons and dies.",
        "threads": [("seen-and-unseen.html", "Seen and unseen: the deceits of Genesis")],
        "sight": "Genesis says Israel's eyesight was poor because of old age and that he could hardly see. That is low vision, not total blindness. Jacob may have seen two shapes in front of him and still not known which boy was which. See what blind means here.",
        "senses": "Jacob could see shapes. He saw that Joseph had brought two boys and asked who they were, but he "
                  "could not tell which was which, and that is the whole of the scene. What he had instead was his "
                  "hands, and the memory of hands. He kissed the boys and embraced them, as his own father had kissed "
                  "him on the day he was deceived. Then he did with his hands the one thing Isaac could not: he placed "
                  "them on purpose, crossed, knowing exactly whose head was under each. A blind man who has lived with "
                  "it for years does not grope. He arranges things, counts, and keeps track, and when a sighted hand "
                  "reaches in to correct him he has to say, as Jacob did, that he knows.",
        "before_after": "Jacob was a hundred and thirty when he came down to Egypt and told Pharaoh his years had been "
                        "few and hard; he lived seventeen more and died at a hundred and forty-seven. This scene comes "
                        "at the end of those seventeen years, when Joseph is told his father is ill and brings his sons. "
                        "After it, in the next chapter, Jacob gathers all twelve of his sons around the bed and speaks "
                        "to each one by name, blind, and then draws up his feet and dies. His body went home to the "
                        "cave at Machpelah near Hebron, where Isaac and Abraham lay.",
        "came_of_it": "The crossed hands held. When the tribes were counted in the wilderness, Ephraim outnumbered "
                      "Manasseh and carried the standard of their camp. Joshua came from Ephraim, and so, centuries "
                      "later, did the northern kingdom's first king. The man who could hardly see had seen further "
                      "than his son.",
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
        "brian": [
            "Joseph reached in to move his father's hand because he assumed that a man who could not see did not know what he was doing. Jacob's answer was two words, said twice: I know. The Hebrew verb there is yada, and the old dictionary says it means to know, properly to ascertain by seeing. Genesis gives the seeing-verb for knowing to a man who could hardly see, and it gives it to him about what his hands had told him. That is the whole page for me.",
            "Blind people are underestimated because sighted people tend to think sight is a vastly superior sense to all the others. I say touch is the most important sense. Think about how much of walking is the sense of touch through your feet, and how much of the rest of the day is your hands and your fingers. We move through this world by a combination of senses. When a fire truck comes along, you hear it long before you see it, and the hearing is what tells you to pull over. Our senses work together to get information to a brain that is locked away from the world behind a thick skull. Jacob's eyes had gone, and his hands, his memory and his judgment had not. He arranged the boys, crossed his arms on purpose, and when the sighted man in the room tried to correct him, he said what every blind person has had to say at some point: I know.",
            "Matthew Henry, writing about this verse three hundred years ago, said that the eye of faith may be very clear even when the eye of the body is very much clouded. I want that sentence on this page because it is what the story is about. Loss of sight does not take understanding with it. It does not take faith, or judgment, or memory, or kindness, or any of the many things that make a person who they are. The writer of Hebrews picked this scene, out of all of Jacob's long life, as his one act of faith: by faith Jacob, when he was dying, blessed each of Joseph's sons. Dying, nearly blind, and that is the moment chosen.",
            "One more thing I noticed. Genesis does not use the same word for Isaac's sight loss and for Jacob's. Isaac's eyes were kahah, weak, grown dim. Jacob's were kabed, heavy, which is the Bible's word for a burden. Henry noticed it too; just before the sentence I quoted, he says that those who have the honour of age must be content to take its burden. I know both of those. Some days sight loss is a dimming you learn to live around. Some days it is a weight you carry. Jacob carried his to the end of the chapter and blessed twelve sons by name with it on him.",
        ],
    },
    {
        "slug": "eli", "title": "Eli at Shiloh", "who": "Eli", "group": "not_restored", "outcome": "not_restored",
        "passages": [("1 Samuel", 3, 1, 18), ("1 Samuel", 4, 12, 18)],
        "sight": "Samuel says Eli's eyesight had grown so dim that he could not see, and later that at ninety-eight he could not see. Dim is the Bible's word for sight going, so Eli likely passed through years of low vision before this. The page reads him as he is described at the end. See what blind means here.",
        "senses": "The book of Samuel shows Eli at three stages, and the senses change with them. In chapter one, "
                  "still sighted, he watches Hannah's lips move without a sound and decides she is drunk: a sighted "
                  "man's mistake, made with his eyes. In chapter three his eyes have grown dim, and in the dark of the "
                  "house of the LORD it is the blind old man, not the sighted boy, who works out whose voice is "
                  "calling. In chapter four he sits by the road, his gaze fixed, and the news reaches him by sound and "
                  "in order: first the whole city crying out, then a question he has to ask, then a runner's words. "
                  "Everyone around him can read the torn clothes and the dust on the man's head. Eli is told last, and "
                  "the last thing he is told is the ark.",
        "before_after": "Eli had judged Israel forty years and was ninety-eight. He had heard, long before this, what "
                        "his sons were doing at the door of the Tent of Meeting, and a man of God had already told him "
                        "that judgment was coming on his house. The word Samuel carried to him in the night was the "
                        "second warning of the same thing. When it came true he was sitting at the gate waiting for it.",
        "came_of_it": "The same hour took his two sons, the ark, and Eli himself, and his daughter-in-law died in "
                      "childbirth naming her son Ichabod, the glory has departed. Shiloh never recovered as the place "
                      "of the ark. But the boy who ran to the blind man three times in the night became the prophet "
                      "who anointed Israel's first two kings, and Samuel's book begins with Eli.",
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
        "brian": [
            "Eli is the one in this series I would least like to be. Not because of how he went blind, which was slowly, with age, the way most people do. Because of the last scene. He is ninety-eight, he cannot see, and he is sitting in a chair by the road waiting for news that everyone around him will get before he does. The text says his heart trembled for the ark. He could do nothing about the battle, nothing about his sons, nothing but sit there and listen for it.",
            "That is the part of blindness that nobody warns you about: the patience you have to have whether you want it or not. Sighted people choose when to be patient. A blind person waits for the ride, waits for the person who said they would read the letter, waits to be told what everybody else in the room already knows. The city cried out before anyone told Eli why, and he had to ask. Why this commotion? I have asked that question, in those words or near enough, more times than I can count. Something has happened, the room knows it, and you are the last to be told, and usually the telling is the gentle version. Eli got the straight version, and the last thing in it was the ark.",
            "The frustration is not the waiting itself. It is not being able to do anything with what you hear. Eli had heard for years what his sons were doing. The text says so: I hear about your wicked deeds from all these people. He spoke to them and they would not listen, and the man of God came, and then the boy came in the night with the same word again. A blind man hears a great deal he cannot act on. I know the sound of a problem starting long before I can get to it, and getting to it is the whole difficulty.",
            "There are all kinds of things I hear that people think I do not. Usually it is when a person does not want to share. My wife Barb has a disability of her own, and it puts limits on a heart that was made for serving people. Some nights I hear her crying softly behind a door in another room, over what she can no longer do for others. Jimmy, who lives with us, spent years doing God's work and should be enjoying a peaceful retirement. Instead he has a job that wears his body down, and when he thinks the house is asleep I hear the muffled grunts of a tired man in pain. Neither of them is telling me. I hear it anyway. A sighted person can look away from something and believe it has not been seen. There is no looking away from a sound. So you carry what you heard, and you decide whether to say so, and that is its own kind of patience.",
            "What I want to hold onto from Eli is the night, not the gate. His eyes had gone dim and the word of the LORD was rare, and when the voice came it was the blind old priest, not the sighted boy, who knew what it was and told Samuel how to answer. In the morning he made the boy tell him all of it, though it was a judgment on his own house, and he did not argue with it. He is the LORD, he said. Let Him do what is good in His eyes.",
            "I have sat with that answer for a while. Eli could not change what was coming. He did not pretend he could, and he did not pretend it was not coming either. He heard the worst said plainly and handed it back to God. There is a patience that sits by the road because it has no choice, and I know that one well. There is another that hears everything, carries it, and still says He is the LORD. That is the one I am still learning, and it is the one I want from this story.",
        ],
    },
    {
        "slug": "ahijah", "title": "Ahijah and the disguised queen", "who": "Ahijah the prophet", "group": "not_restored",
        "outcome": "not_restored",
        "passages": [("1 Kings", 14, 1, 13)],
        "sight": "Kings says Ahijah could not see, for his eyes were dim because of his age. The verb under 'dim' is qum, "
                 "to stand: his eyes had set. It is the word used of Eli at the gate in the same town, and the translators "
                 "swap between the two men, giving Eli 'his gaze was fixed' and Ahijah 'his eyes were dim'. Brian reads it "
                 "as a blind man does: eyes that have stopped tracking are eyes that have stopped working, and he takes "
                 "Ahijah to have been blind, not low vision. It is also the one description of blindness in this series "
                 "written from the outside, what the queen saw when she walked in. The disguise was not aimed at him: "
                 "Jeroboam told her to disguise herself so that they, the people between Tirzah and the prophet's door, "
                 "would not recognize her. See what blind means here.",
        "life": "Ahijah appears twice in Kings, years apart. The first time he is on the road out of Jerusalem in "
                "Solomon's last years, a prophet from Shiloh in a new cloak, which he tears into twelve pieces, handing "
                "ten to Jeroboam: the kingdom, torn from Solomon's son. Shiloh by then was a backwater. The ark had left "
                "it in Eli's day, more than a century before, and never came back. Jeroboam got his ten tribes, set up "
                "golden calves at Bethel and Dan and made priests of men who were not Levites, and Kings records no visit "
                "to Ahijah about any of it. The next we hear of the prophet, he is old, he cannot see, and a woman in plain "
                "clothes is at his door with a sick boy's question. After this day he is not seen again, but his word is: "
                "Kings names it when Baasha wiped out Jeroboam's house, and Chronicles lists the Prophecy of Ahijah the "
                "Shilonite among the records of Solomon's reign.",
        "threads": [("seen-and-unseen.html", "Seen and unseen: the deceits of Genesis")],
        "senses": "This is the one story in the group where the text tells us straight out how the blind man knew. "
                  "Not by her voice, because she had not spoken. Not by her footsteps, though he heard them at the "
                  "door. He knew because the LORD had told him, before she arrived, who was coming and that she would "
                  "pretend to be someone else. The disguise was made for eyes, and Kings says his eyes had set with age; it was for the "
                  "road and the town, not for him. What it could not do was reach the sense he was actually using. Of everyone in the passage, "
                  "the one who cannot see well is the only one who is not fooled, and the reason is not sharper "
                  "hearing. He was told.",
        "before_after": "Years earlier, on the road out of Jerusalem, this same prophet had torn a new cloak into "
                        "twelve pieces and handed Jeroboam ten of them: the kingdom, torn from Solomon's son. Jeroboam "
                        "got the kingdom and then built his own shrines and calves. Now his child is sick, and he sends "
                        "his wife to the one man whose word about him has already come true, in disguise, with the "
                        "gifts of a poor woman.",
        "came_of_it": "She was told the child would die when her feet entered the city, and he did, as she stepped over "
                      "the threshold. He was the only one of Jeroboam's house to be mourned and buried, because, "
                      "Ahijah said, only in him had the LORD found anything good. The rest of what the blind prophet "
                      "said came true under the next dynasty, when Baasha destroyed everyone of Jeroboam's line who "
                      "breathed.",
        "around": "Ahijah is the prophet who years earlier told Jeroboam he would be king over the northern tribes. "
                  "Jeroboam has since led the people into idolatry. Now his son is sick, and he sends his wife to "
                  "Ahijah in disguise, with gifts, to learn whether the boy will live.",
        "happens": "Ahijah cannot see because of his age. Before the queen arrives, the LORD tells him who is coming, "
                   "why, and that she will be disguised. When he hears her footsteps at the door he greets her by "
                   "name and asks why she is pretending. Then he gives her the hard message for her husband.",
        "shoes": "The text is careful about how Ahijah knows. It does not say he recognized her footsteps; it says the "
                 "LORD had told him who was coming and that she would be disguised, and that he spoke when he heard "
                 "feet at the door. His eyes had set with age, and the disguise was ordered for the people she would "
                 "pass, not for him. Of everyone in the passage, the man who cannot see "
                 "well is the one who knows the situation as it is, and he knows it because he was told. The question "
                 "that runs through Genesis, whether a man can tell who is in front of him, stops mattering here: "
                 "Ahijah did not recognize her and did not need to.",
        "brian": [
            "It does not say that he recognized the sound of her feet. He likely did not, unless he had been doing this a long time. And the disguise was not really for him. Jeroboam told her to disguise herself so they would not recognize her, the people on the road and in Shiloh, not the prophet. I used to think Ahijah was probably low vision and could still see a little, and that the disguise might have been aimed at his eyes. Reading the word for his eyes has changed my mind on that, as I say below.",
            "I can tell Barb's sound if she wears certain shoes, but often in areas without context it is difficult to pick out her footsteps among others.",
            "When I started on this story I thought it would be the one where I talked about our other senses, and how much people underestimate what a blind man hears. The text turned that around on me. Ahijah did not hear who she was. He did not work it out from anything. The LORD told him before she arrived who was coming and that she would be disguised, and when he heard feet at the door he said her name. That is how he knew. Not sharper ears. He was told.",
            "The word for his eyes is the same one used for Eli at the gate in the same town: his eyes stood. Set. Still. The translators cannot settle on it, dim in one verse and set or fixed in the other, but the picture is plain enough to me. Eyes that are still are eyes that are not tracking anything, and are not seeing much or anything at all. I am getting more this way the longer I am blind. I do not use my eyes for anything now, and they have stopped moving the way eyes do when they are looking. It is the one description of blindness in this series written from the outside, of what another person sees when they look at a blind man's face. The queen saw that face when she walked in, and whatever her husband had told her, she would have known then that the disguise was wasted on him.",
            "This story also finishes something that starts back in Genesis. Isaac could not tell Jacob from Esau. Jacob could not tell Leah from Rachel in the dark. Joseph's brothers stood in front of him in broad daylight and did not recognize him. All through that family the question is whether a man can tell who is in front of him, and his eyes, when he has them, are no help. The queen came to Shiloh disguised so that nobody would recognize her, and the text never says the prophet did. It says he was told. He is the first one in the whole line who did not have to recognize anybody, and that is the point of him.",
            "Matthew Henry wrote that Ahijah lived obscurely and neglected in Shiloh, blind through age, yet still blest with the visions of the Almighty, which need not bodily eyes, but are rather favoured by the want of them, the eyes of the mind being then most intent and least diverted. I did not expect to agree with a line like that, but I do. My lack of vision gives me clarity in a great many areas. I am less distracted, in a world that is built to pull my attention away from Jesus, where it needs to be. Jeroboam had his eyes and his kingdom and his calves, and he never once sent to Ahijah to ask about any of that. He sent when his boy was sick. Henry puts it in one line: in trouble have those visited thee who before slighted thee. The blind man in Shiloh was the one person in the story who was not distracted, and when the hard word came he gave it straight.",
        ],
    },
    {
        "slug": "samson", "title": "Samson in Gaza", "who": "Samson", "group": "not_restored", "outcome": "not_restored",
        "passages": [("Judges", 16, 18, 31)],
        "senses": "Samson is the one man in Scripture blinded in the prime of his strength, in a moment, and the text "
                  "then follows him into the life every newly blind person learns: work done by feel at the mill, "
                  "being led by the hand, and being looked at by people he cannot see. In the temple he asks the boy "
                  "to put him where he can feel the pillars. That is a blind man orienting himself, by touch, in a "
                  "building full of noise. His hands find the two middle columns, one right and one left, and he knows "
                  "from that what holds the roof up. His last prayer names what he has lost in plain words, for my two "
                  "eyes, and God hears it.",
        "before_after": "Samson had judged Israel twenty years. The chapter that ends in Gaza begins in Gaza: he went "
                        "there to a prostitute, and carried the city gate away by night. Then came Delilah in the valley "
                        "of Sorek, the three false answers, the true one, and a sleep from which he woke not knowing the "
                        "LORD had left him. The text puts one line between the blinding and the temple: the hair of his "
                        "head began to grow back. Nobody in the prison noticed what that meant.",
        "came_of_it": "He died with the Philistines, and killed more in his death than in his life. His family came "
                      "down to Gaza, carried him home, and buried him between Zorah and Eshtaol in his father's tomb. "
                      "The New Testament remembers him once, in the list of those who lived by faith in Hebrews 11, "
                      "between Barak and Jephthah.",
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
        "brian": [
            "Samson lost his sight in the prime of his life. So do a lot of blind adults, and so did I. Most of the people in this series went blind slowly, with age. Samson went blind in a moment, at the height of his strength, and that puts him closer to me and to the people I work with than any of the others.",
            "What I think about first is the adjustment. He was the most physically gifted man in the Bible, and in one afternoon he was reduced to being led around by a hand, with his strength gone and his eyes gone with it. The transition was sudden. I had nine months between the diagnosis and the end of my sight, and that was hard. I work all the time with people who lose their vision in a matter of days or hours, and they are the hardest for me to work with, because they had no time to prepare. No time to get their last looks at the things they wanted to remember. Samson got none. The last thing he saw was Delilah's room, and the Philistines in it.",
            "The Hebrew word matters to me here in a way it may not to a sighted reader. Judges says the Philistines gouged out his eyes, and the verb is naqar, which the old dictionary defines as to bore, to penetrate, to quarry. Isaiah uses the same word for the quarry a stone is dug from. I have had both of my eyes enucleated, removed, because of the extreme pressure in them before the last surgeries. My doctor described what he was going to do as scooping out the inside of a melon. That is naqar. I want to say plainly that it was one of my better decisions in life. My eyes had stopped working completely and the pain and discomfort went with them. Samson had no say in it and no anaesthetic, and I know more than I would like about what was done to him.",
            "Then there is purpose. Samson had been the judge and protector of Israel for twenty years, and blindness did not end that. The text says his hair began to grow back, and then it shows him in the temple at Gaza, asking the servant who held his hand to put him where he could feel the pillars. With nobody left to help him, he asked God for help, and God gave him just enough strength, once more, to finish what he had been given to do. Blind, he still found his purpose and did it. The book says he did more in his death than in his life.",
            "I think about that as I get older. Living with a disability is a bit like dog years, seven to one, and the body spends itself faster. I have to ask God all the time for the strength to do what I think His purpose is for me. Samson's prayer is the shortest one I know for that: remember me, strengthen me, just once more.",
        ],
    },
    {
        "slug": "zedekiah", "title": "Zedekiah, the last king of Judah", "who": "Zedekiah", "group": "not_restored",
        "outcome": "not_restored",
        "listen": {"youtube": "Xhx44nR_OLM", "mp3": "not_by_sight_11_the_last_thing_he_saw.mp3", "minutes": 25,
                   "title": "Not By Sight, Episode 11: The Last Thing He Saw"},
        "passages": [("2 Kings", 25, 1, 7), ("Jeremiah", 39, 4, 7), ("Jeremiah", 52, 8, 11)],
        "senses": "There is no cross-checking of senses in this story, because Zedekiah was not blind until the end "
                  "of it. What the text does instead is arrange what he saw and heard in a deliberate order. He saw "
                  "his sons killed. Then his eyes were put out, so that sight ended on that. Then he was bound in "
                  "bronze and walked to Babylon, a journey of weeks, hearing a foreign army and a foreign city he "
                  "would never see, exactly as Ezekiel had said. Anyone who has lost sight as an adult knows the "
                  "strange permanence of the last things seen. Zedekiah's were chosen for him.",
        "before_after": "Jeremiah had told Zedekiah, in the siege, that he would see the king of Babylon face to face "
                        "and be taken there; Ezekiel, already in Babylon, had said the king would be brought to the land "
                        "of the Chaldeans yet would not see it, and would die there. Zedekiah himself told Jeremiah what "
                        "he was afraid of: being handed over to be abused. He fled the city by night through the gate "
                        "between the two walls, was caught in the plains of Jericho, and was taken north to the king of "
                        "Babylon at Riblah for sentence.",
        "came_of_it": "Both prophecies came true in one act, and Josephus and Matthew Henry both stopped to say so: he "
                      "was brought to Babylon, and he did not see it. Jeremiah had also promised him that he would not "
                      "die by the sword but in peace, and the record says he was kept in custody in Babylon until the "
                      "day of his death. The book of Jeremiah does not end on him. Its last paragraph is the release of "
                      "the king before him, Jehoiachin, lifted out of prison and given a seat at the king's table, a "
                      "small light at the end of a dark book.",
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
        "brian": [
            "Whatever we open the episode with, this is going to be a hard one to talk about.",
            "There are sounds you cannot unhear. I heard my dog cry out in pain when he jumped off the deck and tore his ACL. He went blind from the knee surgery that followed, which I thought was a little unfair. I heard my doctor curse while he was operating on my eye. That was the last day I had any usable vision. You cannot look away from a sound and pretend it is not there. A sighted person can turn their head. The sound comes in anyway, and it stays.",
            "Zedekiah brings back a lot of memories of pain and discomfort, too. People do not realise how violent the treatment of a failing eye is. Scraping the surface of it, replacing parts of it, putting needles into it. Such extreme measures for such a delicate instrument. I do not like to talk about the pain I went through, so I will say only this: there are a great many more nerves in the eye than most people know, and upsetting them was worse than anything else I have been through, and that includes heart bypass surgery. I do not have to worry about eye pain any more, and I am so grateful for that. Many people who lose their sight still live with discomfort and pain long after the sight is gone. So I know it could be worse.",
            "I do not even want to think about what Zedekiah faced. The last thing he saw was out of his worst nightmares, and then, with all of that pain, he was made to walk from Riblah to Babylon, a journey of weeks, to the prison where he would die. The text says it in a single verse and moves on. I cannot move on from it that quickly.",
            "I am fortunate. The last thing I saw was my wife Barb, shortly before the surgery.",
        ],
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
        "listen": {"youtube": "lVfm08wIBjE", "mp3": "not_by_sight_04_the_ones_who_followed.mp3", "minutes": 22,
                   "title": "Not By Sight, Episode 4: The Ones Who Followed"},
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
        "listen": {"youtube": "lVfm08wIBjE", "mp3": "not_by_sight_04_the_ones_who_followed.mp3", "minutes": 22,
                   "title": "Not By Sight, Episode 4: The Ones Who Followed"},
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
        "listen": {"youtube": "rQyPtBtnnt8", "mp3": "not_by_sight_03_the_blind_man_at_bethsaida.mp3", "minutes": 18,
                   "title": "Not By Sight, Episode 3: The blind man at Bethsaida"},
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
        "listen": {"youtube": "UJdeJ3C6j3A", "mp3": "not_by_sight_02_bartimaeus_at_jericho.mp3", "minutes": 22,
                   "title": "Not By Sight, Episode 2: Bartimaeus at Jericho"},
        "before_after": "Just before Jericho, Mark records James and John asking Jesus for the seats of honour, and "
                        "Jesus asking them, \"What do you want Me to do for you?\" A few verses later He asks a blind "
                        "beggar the very same words. And Luke carries the story straight on into the town: Jesus stops "
                        "a second time, for Zacchaeus the tax collector, who could not see Him over the crowd and "
                        "climbed a sycamore fig (Luke 19:1-10). Two men in one town who could not see Him, for opposite "
                        "reasons, and He stopped for both, a few days from the cross. Then He told a parable because He "
                        "was near Jerusalem (Luke 19:11). He was still teaching with the city in sight.",
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
        "listen": {"youtube": "zZlWP-E0rdU", "mp3": "not_by_sight_01_the_man_born_blind.mp3", "minutes": 16,
                   "title": "Not By Sight, Episode 1: The Man Born Blind"},
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
        "listen": {"youtube": "0wv608fgmPo", "mp3": "not_by_sight_05_the_blind_in_the_crowd.mp3", "minutes": 22,
               "title": "Not By Sight, Episode 5: The Blind in the Crowd"},
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
        "listen": {"youtube": "0wv608fgmPo", "mp3": "not_by_sight_05_the_blind_in_the_crowd.mp3", "minutes": 22,
               "title": "Not By Sight, Episode 5: The Blind in the Crowd"},
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
        "listen": {"youtube": "or8s4SUiSHQ", "mp3": "not_by_sight_06_the_answer_to_john.mp3", "minutes": 19,
               "title": "Not By Sight, Episode 6: The Answer to John"},
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


# ---- the place and the time, from the reference shelf (edited in
# src/write_place_and_time.py, evidence in place_and_time_candidates.json)
import json as _json
from pathlib import Path as _Path

_PT = _Path(__file__).resolve().parents[1] / "data" / "reference" / "place_and_time.json"
if _PT.exists():
    _extra = _json.loads(_PT.read_text(encoding="utf-8"))
    for _story in STORIES:
        for _item in _extra.get(_story["slug"], []):
            _story.setdefault("place_and_time", []).append({"text": _item["text"], "source": _item["source"]})
