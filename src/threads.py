"""Threads: pages that follow one idea across several stories, rather than one person through one scene.

The first is "Seen and unseen", the deceits of Genesis, which nearly all work on what the eye cannot check.
Each section quotes the Berean text word for word and adds only what can be seen in it. Brian's thoughts are
added by him later, as on the story pages.
"""
from __future__ import annotations

THREADS = [
    {
        "slug": "seen-and-unseen",
        "title": "Seen and unseen: the deceits of Genesis",
        "lede": "Two of the six people on this site who lost their sight and never had it back are father and son, "
                "Isaac and Jacob. Both were deceived. So was nearly everyone else in their family, and most of them "
                "could see. This page follows the deceits of Genesis in order and asks one question of each: what did "
                "the eye have to do with it?",
        "intro": [
            "Read the family's story from Genesis 26 to 48 and a pattern comes up that a sighted reader can easily miss, "
            "because to a sighted reader deception is simply something that happens. Almost every deceit in these "
            "chapters works on what the eye cannot check: a darkened tent, a veil, a hand that feels like another man's, "
            "a garment that looks like proof. And when the eye can check, it is wrong anyway. The two blind men in the "
            "family were deceived no more often, and no more badly, than the sighted ones. That is worth knowing on a "
            "site about blindness in the Bible, where the stories of Isaac and Jacob are too often read as if blindness "
            "were the weakness that let the lie in.",
            "The passages are given word for word from the Berean Standard Bible. The comments under each say only what "
            "is in the text. The Hebrew verb that runs through several of them, nakar, to recognise or to make out, is "
            "named where it occurs, and will be checked against the tagged Hebrew text when that is added to the site.",
        ],
        "sections": [
            {
                "heading": "Isaac at Gerar, with his sight",
                "passages": [("Genesis", 26, 7, 9)],
                "note": "The first deceiver in this thread is Isaac himself, years before his eyes failed. He tells the "
                        "men of Gerar that Rebekah is his sister, as his father Abraham had twice said of Sarah. The lie "
                        "rests on what the Philistines cannot see: how the two of them are together when no one is "
                        "watching. It is found out by a man at a window. Abimelech looks down, sees, and knows. The "
                        "sighted Isaac deceived others, and sight undid him.",
            },
            {
                "heading": "Isaac in the tent, without it",
                "passages": [("Genesis", 27, 21, 23)],
                "note": "The scene this site tells on the Isaac page. He questions, touches, listens and smells, and "
                        "names the one thing that is wrong: the voice. The text says he did not recognise him, and gives "
                        "the reason, the hairy hands. Everything about the disguise was built for the senses he had "
                        "left. The blind man was not careless. He was outmatched by people who knew him.",
                "see": ("isaac.html", "Isaac and the stolen blessing"),
            },
            {
                "heading": "Jacob in the dark",
                "passages": [("Genesis", 29, 21, 25)],
                "note": "Seven years after deceiving his father, Jacob is deceived in his turn, and the text makes the "
                        "means plain: evening came, and in the morning, there was Leah. Jacob could see perfectly well. "
                        "Night did to him what age had done to Isaac, and a veil and a quiet bride did the rest. His own "
                        "words are \"Why have you deceived me?\", the question Esau might have asked him. Laban's "
                        "answer, that the younger is not given before the older, lands on the man who had just taken "
                        "an older brother's blessing. Four verses earlier Genesis says that Leah had weak eyes. The Hebrew "
                        "word is disputed and the site records it in the catalog as possible rather than certain; "
                        "whatever it means, it is Jacob's eyes, not Leah's, that the night defeats.",
            },
            {
                "heading": "Rachel on the saddlebag",
                "passages": [("Genesis", 31, 33, 35)],
                "note": "Laban comes looking for his stolen household gods and searches with his eyes, tent by tent. "
                        "Rachel sits on them and gives him a reason not to make her stand. He looks at everything and "
                        "finds nothing. It is the plainest case in the thread: a sighted man, searching in daylight, "
                        "deceived by what he was not allowed to look under.",
            },
            {
                "heading": "The robe and the goat",
                "passages": [("Genesis", 37, 31, 33)],
                "note": "Now Jacob is the father, and sighted, and his sons do to him what he did to Isaac. A goat "
                        "serves again. His sons say \"Examine it\", and the Hebrew is the same verb, nakar, that said "
                        "Isaac did not recognise Jacob; here Jacob does recognise the robe, and that is exactly how he "
                        "is deceived. He sees the evidence with his own eyes, draws the obvious conclusion, and mourns "
                        "a living son for some twenty years. The lie that lasted longest in this family was told to a "
                        "man who could see.",
            },
            {
                "heading": "Tamar at the roadside",
                "passages": [("Genesis", 38, 14, 15), ("Genesis", 38, 25, 26)],
                "note": "Judah, one of the brothers who sent the robe, is deceived by a veil. The text says he saw her "
                        "and thought she was a prostitute because her face was covered: his eyes worked, and led him "
                        "wrong. Months later Tamar sends him his own seal, cord and staff with the same words his "
                        "brothers used to their father, \"examine\", and the same verb. This time Judah recognises "
                        "them and says she is more righteous than he. Recognising is the hinge of this whole thread, and "
                        "it has little to do with how well a person sees.",
            },
            {
                "heading": "Joseph before his brothers",
                "passages": [("Genesis", 42, 7, 8)],
                "note": "Ten men stand in front of their brother in full daylight. He recognises them; they do not "
                        "recognise him. Nothing is hidden but the years and an Egyptian's dress and language. Genesis "
                        "says it twice in two verses, with the verb nakar both times. The brothers who deceived their "
                        "father with a garment are now deceived by one.",
            },
            {
                "heading": "Jacob, who could hardly see, and knew",
                "passages": [("Genesis", 48, 10, 10), ("Genesis", 48, 17, 19)],
                "note": "The thread ends where the Jacob page begins. The old man's eyesight is poor with age. His "
                        "sighted son sets the boys so that the right hand will fall on the elder, and when the hands "
                        "cross, reaches in to correct a blind man's mistake. There is no mistake. \"I know, my son, I "
                        "know.\" In a family where the sighted were deceived by veils, robes and daylight, the last word "
                        "goes to a man who can barely see and is not deceived at all.",
                "see": ("jacob.html", "Jacob blesses Joseph's sons"),
            },
        ],
        "close": [
            "Set the eight scenes side by side and the lesson is not that blind people are easily fooled. Isaac in the "
            "tent and Jacob in the dark were deceived by the same means: someone they trusted arranged what they could "
            "not check. Laban, Jacob with the robe, Judah and the ten brothers were all deceived with their eyes open, "
            "and in three of those cases it was precisely what they saw that misled them. The only person in the thread "
            "who is offered a correction and does not need it is the one who can hardly see.",
            "That matters for how the Isaac and Jacob episodes will be told. Isaac's blindness is the occasion of the "
            "deceit, not its cause. The cause is in the people around him, and Genesis spends the next twenty chapters "
            "showing that sight would not have saved him. Nothing on this page is imagined. It is only the order the "
            "stories come in, read by someone who has reason to notice.",
        ],
        "brian": [],
    },
]


def by_slug(slug: str) -> dict:
    return next(t for t in THREADS if t["slug"] == slug)
