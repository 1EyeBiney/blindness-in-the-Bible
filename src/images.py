"""Pictures on the site: which painting goes where, with its description and caption.

Each entry: slot on the page, the full-size source under audio/shots/images (kept out of git, too heavy),
the web file name under media/images (made by src/make_web_images.py, kept in git), the description read
by screen readers, and the short caption everyone sees. Nothing is said only in a picture.
"""

WIDTHS = (800, 1600)        # two sizes: phones and small windows, then everything else

# story slug -> pictures. Slots: banner (under the title), around, happens, shoes, place, map.
STORY_PICTURES = {
    "man-born-blind": [
        {"slot": "banner", "source": "ep01_man_born_blind/09_water.png", "name": "man-born-blind-water",
         "alt": "A man kneels at the edge of the pool, seen from behind, ripples spreading from his hands.",
         "caption": "He went and washed, and came back seeing. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "around", "source": "ep01_man_born_blind/03_temple_court.png", "name": "man-born-blind-temple-court",
         "alt": "The Temple's outer court, crowds of pilgrims, and a beggar seated against a column with his back to us.",
         "caption": "A beggar in the Temple courts, where a blind man could count on passers-by."},
        {"slot": "happens", "source": "ep01_man_born_blind/06_mud.png", "name": "man-born-blind-mud",
         "alt": "Two hands mixing earth into mud on a paving stone.",
         "caption": "Mud made on the ground, on the Sabbath."},
        {"slot": "shoes", "source": "ep01_man_born_blind/01_downhill.png", "name": "man-born-blind-downhill",
         "alt": "A lone man walks down a steep, narrow stone street, one hand on the wall, seen from behind.",
         "caption": "Downhill to Siloam with mud on his eyes, still blind."},
        {"slot": "place", "source": "ep01_man_born_blind/07_siloam_pool.png", "name": "man-born-blind-siloam-pool",
         "alt": "Wide stone steps in sets of five, descending to the still water of the Pool of Siloam.",
         "caption": "The Pool of Siloam, with its steps in sets of five."},
        {"slot": "map", "source": "maps/ep01.png", "name": "map-ep01",
         "alt": "The series map, with Jerusalem marked in gold.",
         "caption": "The map, in words. Jerusalem sits in the hills west of the north end of the Dead Sea. The Pool of Siloam is at the south end of the city, and the Temple Mount is on its east side."},
    ],
    "bartimaeus": [
        {"slot": "banner", "source": "ep02_bartimaeus/08_the_crowd_stops.png", "name": "bartimaeus-the-crowd-stops",
         "alt": "The whole crowd stands still, turned toward one figure at its centre; at the edge a beggar begins to rise.",
         "caption": "Jesus stopped, and the whole crowd stopped with Him. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "around", "source": "ep02_bartimaeus/03_pilgrim_road.png", "name": "bartimaeus-pilgrim-road",
         "alt": "A long line of pilgrims with mule carts walks a dirt road between palms toward the hills.",
         "caption": "Pilgrims on the road through Jericho, going up to Jerusalem for Passover."},
        {"slot": "happens", "source": "ep02_bartimaeus/09_cloak_left.png", "name": "bartimaeus-cloak-left",
         "alt": "A worn cloak lies in the dust with coins spilled on it, bare footprints leading away toward the crowd.",
         "caption": "The cloak he threw aside."},
        {"slot": "shoes", "source": "ep02_bartimaeus/01_roadside.png", "name": "bartimaeus-roadside",
         "alt": "A man in a ragged cloak sits in the dust beside an empty dirt road at the edge of a palm town, hills beyond.",
         "caption": "The roadside, before the crowd came."},
        {"slot": "place", "source": "ep02_bartimaeus/10_two_jerichos.png", "name": "bartimaeus-two-jerichos",
         "alt": "A wide view: the ruined mound of old Jericho by a spring, and across the palms the newer town's palace walls, a road between.",
         "caption": "Old Jericho by its spring, and Herod's newer town across the palms."},
        {"slot": "map", "source": "maps/ep02.png", "name": "map-ep02",
         "alt": "The series map, with Jericho marked in gold and a line joining it to Jerusalem.",
         "caption": "The map, in words. Jericho lies in the Jordan valley, north of the Dead Sea. Stand there facing north, and Jerusalem is about seven hours' walk away at eight o'clock, uphill all the way."},
    ],
    "bethsaida": [
        {"slot": "banner", "source": "ep03_bethsaida/10_there_is_the_lake.png", "name": "bethsaida-there-is-the-lake",
         "alt": "A man stands on the grass with his back to us, arms lifted a little, looking out at the whole lake in clear light.",
         "caption": "He saw everything clearly. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "around", "source": "ep03_bethsaida/05_boat.png", "name": "bethsaida-boat",
         "alt": "A fishing boat on open water with a dozen men aboard, one standing to speak, the shore ahead.",
         "caption": "The boat that brought Jesus and the disciples to Bethsaida."},
        {"slot": "happens", "source": "ep03_bethsaida/09_walking_out.png", "name": "bethsaida-walking-out",
         "alt": "Two men walk out of the village onto grass, hand in hand, the crowd left behind, the lake to the right.",
         "caption": "Led by the hand, out of the village."},
        {"slot": "shoes", "source": "ep03_bethsaida/11_trees_walking.png", "name": "bethsaida-trees-walking",
         "alt": "A blurred view: tall indistinct figures on a shore against bright water, their outlines soft like trees.",
         "caption": "People who look like trees, walking."},
        {"slot": "place", "source": "ep03_bethsaida/02_village_lanes.png", "name": "bethsaida-village-lanes",
         "alt": "A narrow lane of dark stone houses with nets drying on racks, a goat, baskets of fish, and the lake at the end of the lane.",
         "caption": "A fishing village of dark basalt stone."},
        {"slot": "map", "source": "maps/ep03.png", "name": "map-ep03",
         "alt": "The series map, with Bethsaida marked in gold at the north end of the Sea of Galilee.",
         "caption": "The map, in words. Bethsaida is at the top of the Sea of Galilee. Stand there facing north, and Jericho is about three days' walk at six o'clock, down the Jordan. Jerusalem is about three and a half days at seven o'clock."},
    ],
    "two-blind-men": [
        {"slot": "banner", "source": "ep04_the_ones_who_followed/06_following_down_the_street.png", "name": "two-blind-men-following-down-the-street",
         "alt": "Two men follow a crowd down a narrow lane of dark stone, one with a hand on the other's shoulder, gulls overhead, the lake to the left.",
         "caption": "Two blind men followed Him, calling out. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "around", "source": "ep04_the_ones_who_followed/05_leaving_the_house.png", "name": "two-blind-men-leaving-the-house",
         "alt": "A crowd outside the gate of a large stone house; a figure walks away from it with people following, seen from behind.",
         "caption": "Jesus leaving the ruler's house, the crowd going with Him."},
        {"slot": "happens", "source": "ep04_the_ones_who_followed/09_inside_the_house.png", "name": "two-blind-men-inside-the-house",
         "alt": "A dim crowded room lit by oil lamps; a figure at its centre has turned toward two men just inside the door, seen from behind.",
         "caption": "Indoors at last, and the question: do you believe?"},
        {"slot": "shoes", "source": "ep04_the_ones_who_followed/08_wall_of_backs.png", "name": "two-blind-men-wall-of-backs",
         "alt": "A dense crowd packed around a low doorway, a wall of backs; at the near edge two men stand close together, about to push in.",
         "caption": "The doorway, and a wall of backs."},
        {"slot": "place", "source": "ep04_the_ones_who_followed/07_capernaum.png", "name": "two-blind-men-capernaum",
         "alt": "Capernaum: clustered dark stone houses with flat roofs, a courtyard, narrow lanes running down to boats on the shore.",
         "caption": "Capernaum, where the old writers place this story."},
        {"slot": "map", "source": "maps/ep04.png", "name": "map-ep04",
         "alt": "The series map, with Capernaum marked in gold on the north shore of the Sea of Galilee.",
         "caption": "The map, in words. Capernaum is on the north shore of the Sea of Galilee. Stand there facing north, and Bethsaida is about two hours' walk at two o'clock. Straight behind, at six o'clock, are Jericho at about three days' walk and Jerusalem at about three and a half."},
    ],
    "blind-and-mute-man": [
        {"slot": "banner", "source": "ep04_the_ones_who_followed/11_brought_by_friends.png", "name": "blind-and-mute-man-brought-by-friends",
         "alt": "A man is led between two friends, each holding an arm, toward a waiting crowd, all seen from behind.",
         "caption": "He was brought to Jesus. Someone had to bring him. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "happens", "source": "ep04_the_ones_who_followed/12_the_argument.png", "name": "blind-and-mute-man-the-argument",
         "alt": "Men in prayer shawls argue with raised hands; across the square one man stands alone and unnoticed, his back to us.",
         "caption": "The argument about the healing, with the healed man forgotten."},
        {"slot": "shoes", "source": "ep04_the_ones_who_followed/13_hand_on_his_arm.png", "name": "blind-and-mute-man-hand-on-his-arm",
         "alt": "A close view of one person's hand resting on another man's forearm. Only hands and sleeves are shown.",
         "caption": "For a man who could not see or speak, touch was the way in."},
    ],
    "crowds-by-the-sea": [
        {"slot": "banner", "source": "ep05_the_blind_in_the_crowd/03_glad_crowd_above.png", "name": "crowds-by-the-sea-glad-crowd-above",
         "alt": "Looking up the slope at a great crowd along the crest of the hill, arms raised, with climbers on the path below seen from behind.",
         "caption": "The sound from higher up the hill. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "around", "source": "ep05_the_blind_in_the_crowd/05_seated_on_the_mountain.png", "name": "crowds-by-the-sea-seated-on-the-mountain",
         "alt": "A figure in a plain robe sits on a rock at the top of the hill, seen from behind, with a long line of people climbing toward him.",
         "caption": "He went up on a mountain and sat down."},
        {"slot": "happens", "source": "ep05_the_blind_in_the_crowd/06_laid_at_his_feet.png", "name": "crowds-by-the-sea-laid-at-his-feet",
         "alt": "People set down a stretcher and help others to sit on the ground before the seated figure, seen from behind the helpers.",
         "caption": "They laid them at His feet."},
        {"slot": "shoes", "source": "ep05_the_blind_in_the_crowd/09_carrying_each_other.png", "name": "crowds-by-the-sea-carrying-each-other",
         "alt": "On the steep path, four men carry a boy on a door, a woman leads a child by the hand, and a man guides another by the arm, all seen from behind.",
         "caption": "Nobody blind or lame climbed that hill alone."},
        {"slot": "place", "source": "ep05_the_blind_in_the_crowd/07_wall_of_hills.png", "name": "crowds-by-the-sea-wall-of-hills",
         "alt": "The eastern shore from the water: a high, steep wall of bare hills rising from a narrow shoreline, haze below and clear air above.",
         "caption": "The eastern shore of the Sea of Galilee, a wall of bare hills."},
        {"slot": "map", "source": "maps/ep05.png", "name": "map-ep05",
         "alt": "The series map, with the hills east of the Sea of Galilee marked in gold.",
         "caption": "The map, in words. The mountain is placed on the eastern shore of the Sea of Galilee. Stand there facing north, and Capernaum and Bethsaida are about five hours' walk at eleven o'clock, round the top of the lake. Jericho is about three days at six o'clock, and Jerusalem about three and a half days at seven o'clock."},
    ],
    "the-temple": [
        {"slot": "banner", "source": "ep05_the_blind_in_the_crowd/12_they_come_in.png", "name": "the-temple-they-come-in",
         "alt": "Tables overturned and coins scattered on the paving; through the gap come people led by the hand, on a crutch, and feeling the way with a staff, seen from behind.",
         "caption": "The blind and the lame came to Him at the Temple. The pictures on this page are paintings made for the episode. They are imagined, not records."},
        {"slot": "around", "source": "ep05_the_blind_in_the_crowd/11_temple_market.png", "name": "the-temple-temple-market",
         "alt": "The vast outer court of the Temple as a market: money changers at small tables, cages of doves, sheep and oxen, crowds between long colonnades.",
         "caption": "The outer court, turned into a market."},
        {"slot": "happens", "source": "ep05_the_blind_in_the_crowd/13_children_shouting.png", "name": "the-temple-children-shouting",
         "alt": "Children in the Temple court, seen from behind with arms raised, shouting; at the far side a few robed elders stand stiffly with folded arms.",
         "caption": "Children shouting Hosanna, and the elders indignant."},
        {"slot": "place", "source": "ep05_the_blind_in_the_crowd/10_davids_city.png", "name": "the-temple-davids-city",
         "alt": "An ancient walled fortress on a narrow ridge above a deep valley, an army camped far below: Jerusalem on the day David took it.",
         "caption": "The same city a thousand years earlier, on the day David took it."},
        {"slot": "map", "source": "maps/ep01.png", "name": "map-ep01",
         "alt": "The series map, with Jerusalem marked in gold.",
         "caption": "The map, in words. Jerusalem sits in the hills west of the north end of the Dead Sea. The Temple Mount is on the east side of the city. The road from Jericho comes in from two o'clock, about seven hours' walk."},
    ],
    "the-jebusite-taunt": [
        {"slot": "banner", "source": "ep05_the_blind_in_the_crowd/10_davids_city.png", "name": "the-temple-davids-city",
         "alt": "An ancient walled fortress on a narrow ridge above a deep valley, an army camped far below: Jerusalem on the day David took it.",
         "caption": "The fortress the Jebusites said even the blind and the lame could hold. The pictures on this page are paintings made for the episode. They are imagined, not records."},
    ],
}

# Pictures on other pages, by page name. "crop" is the part of the source to keep (left, top, right, bottom, in
# source pixels) and "widths" overrides WIDTHS for a picture that is shown small.
PAGE_PICTURES = {
    "about": [
        {"slot": "portrait", "source": "ep01_man_born_blind/00_brian_navy.png", "name": "about-brian-navy",
         "crop": (860, 40, 1900, 1500), "widths": (400, 800),
         "alt": "An old photograph, softened to match the site's paintings. Brian as a young sailor in Navy whites "
                "and a white hat, smiling, with Patti beside him holding his arm. A small plate under the photograph "
                "reads Mister Scaredy Cat.",
         "caption": "Brian in his Navy days, with Patti. In the episodes, the voice that speaks Brian's words is "
                    "introduced as Mister Scaredy Cat, because he would not use his own."},
    ],
}

STORY_PICTURES["answer-to-john"] = [
    {"slot": "banner", "source": "ep06_the_answer_to_john/08_that_very_hour.jpg", "name": "answer-to-john-that-very-hour",
     "alt": "A crowd on a green hillside in Galilee. A figure in a plain robe, seen from behind, reaches out to an old man steadied by a friend, while two dusty travellers with staffs watch from the edge.",
     "caption": "He gave sight to many who were blind. From Luke 7:21. The pictures on this page are paintings made for the episode. They are imagined, not records."},
    {"slot": "around", "source": "ep06_the_answer_to_john/01_cell_dark.jpg", "name": "answer-to-john-cell-dark",
     "alt": "A small cell cut out of solid rock, almost dark. A man in a rough cloak sits on straw, seen from behind, his head tilted as if listening. The only light is a line under a heavy door.",
     "caption": "John heard in prison about the works of Christ."},
    {"slot": "happens", "source": "ep06_the_answer_to_john/07_two_on_the_road.jpg", "name": "answer-to-john-two-on-the-road",
     "alt": "Two men with staffs and small packs walk north along a dusty road in the Jordan valley, seen from behind, the river to one side and a long road ahead.",
     "caption": "Two friends, a walk of about four days, and one question."},
    {"slot": "shoes", "source": "ep06_the_answer_to_john/12_his_own_hands.jpg", "name": "answer-to-john-his-own-hands",
     "alt": "An old man with white hair, seen from behind his shoulder, holds up his two open hands and looks at them in bright daylight, a friend's hand on his arm.",
     "caption": "What the messengers were told to report: the blind receive sight."},
    {"slot": "place", "source": "ep06_the_answer_to_john/06_machaerus.jpg", "name": "answer-to-john-machaerus",
     "alt": "The fortress of Machaerus in daylight: a walled stronghold with a palace on top of a steep bare hill with sheer cliffs, the Dead Sea far below.",
     "caption": "Machaerus, the fortress east of the Dead Sea that Josephus names as John's prison."},
    {"slot": "map", "source": "maps/ep06.png", "name": "map-ep06",
     "alt": "The series map, with Machaerus marked in gold east of the Dead Sea.",
     "caption": "The map, in words. Machaerus stands east of the Dead Sea. Stand on its walls facing north. Jericho is at eleven o'clock and Jerusalem at ten, about two days' walk round the north end of the sea. Straight ahead at twelve o'clock is Galilee: Nazareth, Capernaum and Bethsaida are all about four days' walk."},
]

IMAGINED = " The picture is a painting, imagined, not a record."


def _site_batches() -> None:
    """The paintings made for the site itself, listed in audio/shots/site_batch*.json with their prompts. A page
    named stories/<slug> gets a story banner; any other page gets a banner under its heading."""
    import json
    from pathlib import Path
    shots = Path(__file__).resolve().parents[1] / "audio" / "shots"
    for f in sorted(shots.glob("site_batch*.json")):
        batch = json.loads(f.read_text(encoding="utf-8"))
        for x in batch["pictures"]:
            page = x["page"]
            pic = {"slot": "banner", "source": f"{batch['folder']}/{x['name']}.jpg",
                   "name": page.replace("/", "-") + "-banner", "alt": x["alt"], "caption": x["caption"] + IMAGINED}
            if page.startswith("stories/") and page != "stories/index":
                STORY_PICTURES[page.split("/", 1)[1]] = [pic]
            else:
                PAGE_PICTURES[page] = [pic]


_site_batches()

# The stories of sight lost: a map each, added after the site-batch banner (October 2026).
STORY_PICTURES["isaac"].append(
    {"slot": "map", "source": "maps/isaac.png", "name": "map-isaac",
     "alt": "The series map, with Beersheba marked in gold at the southern edge of the land.",
     "caption": "The map, in words. Beersheba lies at the southern limit of the land, about two days' walk south-west of "
                "Jerusalem, at seven o'clock with north at twelve. Isaac lived there, and Jacob left from there for Haran, "
                "far to the north-east beyond the map."})


# Pictures through the Law pages, from the Law episodes (Brian, 20 October 2026: the same pattern as the story pages).
# Page name -> pictures after the banner. Slots: around (What leads up to it), says (What it says), word (The word),
# place (The place and the time), map. The banner itself comes from the site batch.
LAW_PICTURES = {
    "law/stumbling-block": [
        {"slot": "around", "source": "ep07_the_stumbling_block/06_wages_at_sunset.jpg", "name": "law-stumbling-block-wages",
         "alt": "A harvested field at sunset with sheaves standing; a landowner, seen from behind, counts coins into a labourer's open hand, a village on the hill beyond.",
         "caption": "Wages paid at the end of the day: the law of the blind sits among laws like this one." + IMAGINED},
        {"slot": "says", "source": "ep07_the_stumbling_block/07_gerizim_and_ebal.jpg", "name": "law-stumbling-block-gerizim-ebal",
         "alt": "Two broad rounded mountains facing each other across a narrow green valley, a small walled town of stone houses between them, terraces and olive trees on the slopes.",
         "caption": "Mount Gerizim and Mount Ebal, where the tribes were to stand and answer the curses with Amen." + IMAGINED},
        {"slot": "word", "source": "ep07_the_stumbling_block/09_fallen_and_broken.jpg", "name": "law-stumbling-block-broken-jar",
         "alt": "A large clay water jar lying broken on a stone path, its pieces scattered and water spreading dark across the stones.",
         "caption": "Fallen and broken: the company the word for stumbling block keeps." + IMAGINED},
        {"slot": "place", "source": "ep07_the_stumbling_block/13_hammurabi.jpg", "name": "law-stumbling-block-hammurabi",
         "alt": "A tall black stone monument in a sunlit courtyard in Babylon, a carved king seated at its top and the rest of its surface covered in fine carved marks, palm trees and mud-brick walls around it.",
         "caption": "The kind of stone Hammurabi's laws were carved on, which price an eye but say nothing to protect the blind." + IMAGINED},
        {"slot": "map", "source": "maps/ep07.png", "name": "map-ep07",
         "alt": "The series map, with Jerusalem and Shechem marked in gold.",
         "caption": "The map, in words. Stand in Jerusalem and face north, with north at twelve o'clock. Shechem is at twelve o'clock, about a day and a half's walk, between Mount Gerizim and Mount Ebal. Mount Sinai, where the Law was given, lies far to the south, about eleven days' walk, off the bottom of the map."},
    ],
    "law/servant-blinded": [
        {"slot": "around", "source": "ep08_the_servants_eye/02_household_courtyard.jpg", "name": "law-servant-blinded-courtyard",
         "alt": "The stone courtyard of a large household: a servant woman carries a water jar across the yard, a man works at a grinding stone in the shade, and the master stands in a far doorway.",
         "caption": "A household with servants, the setting of the laws around this one." + IMAGINED},
        {"slot": "says", "source": "ep08_the_servants_eye/05_not_empty_handed.jpg", "name": "law-servant-blinded-not-empty-handed",
         "alt": "A freed man leads a donkey laden with sacks out through a farm gate, a few sheep walking beside him, while the farmer who freed him watches from the gate.",
         "caption": "A freed servant leaving with gifts from his master's flock and harvest." + IMAGINED},
        {"slot": "word", "source": "ep08_the_servants_eye/03_spring_in_the_rock.jpg", "name": "law-servant-blinded-spring",
         "alt": "A small spring of clear water falling from a crack in a rock face into a pool ringed with ferns and moss, in dry hill country.",
         "caption": "A spring in the rock: the Hebrew word for eye is also the word for a spring of water." + IMAGINED},
        {"slot": "place", "source": "ep08_the_servants_eye/08_silver_weighed.jpg", "name": "law-servant-blinded-silver",
         "alt": "Pieces of silver weighed on a bronze balance on a low wooden table, a clay tablet and a small lamp beside them, hands at the edges of the picture.",
         "caption": "Silver on the scales: in Babylon a servant's eye was priced, and the payment went to the owner." + IMAGINED},
    ],
    "law/priest": [
        {"slot": "around", "source": "ep09_the_blind_priest/08_priests_at_work.jpg", "name": "law-priest-at-work",
         "alt": "Priests in white linen at work around the bronze altar in the tabernacle courtyard, one carrying wood, one laying pieces on the fire, one pouring from a bowl.",
         "caption": "The altar service, most of it done with the hands." + IMAGINED},
        {"slot": "says", "source": "ep09_the_blind_priest/03_the_priests_table.jpg", "name": "law-priest-table",
         "alt": "Priests in white sit on mats around a shared evening meal by lamplight; in the foreground one priest is guided to his place by another, a hand on his shoulder.",
         "caption": "Still a priest, and fed as one, at the priests' table." + IMAGINED},
        {"slot": "word", "source": "ep09_the_blind_priest/06_the_lamb.jpg", "name": "law-priest-lamb",
         "alt": "A single spotless white lamb standing in fresh straw in a small stone pen, morning light, a hand resting on the gate.",
         "caption": "The same word for a defect keeps the priest and the lamb from the altar." + IMAGINED},
        {"slot": "place", "source": "ep09_the_blind_priest/10_the_lot.jpg", "name": "law-priest-lot",
         "alt": "Priests in white stand in a circle in a torchlit stone hall of the Temple at dawn, gathered to draw the lot for the day's tasks.",
         "caption": "The priests drawing lots for the day's work, a few of the fifty on duty." + IMAGINED},
    ],
    "law/blind-animals": [
        {"slot": "around", "source": "ep10_the_blind_animal/02_the_firstborn.jpg", "name": "law-blind-animals-firstborn",
         "alt": "A shepherd, seen from behind, kneels in a stone sheepfold among ewes and newborn lambs, lifting one small lamb, hills beyond.",
         "caption": "A firstborn lamb, which belonged to God." + IMAGINED},
        {"slot": "says", "source": "ep10_the_blind_animal/03_eaten_at_home.jpg", "name": "law-blind-animals-eaten-at-home",
         "alt": "Evening in a village courtyard: a family sits on mats around a shared meal of bread and roasted meat by the light of a clay lamp, children among them.",
         "caption": "Kept from the altar, not from the table: a blemished firstborn was eaten at home." + IMAGINED},
        {"slot": "word", "source": "ep10_the_blind_animal/04_walking_whole.jpg", "name": "law-blind-animals-walking-whole",
         "alt": "A man with a long staff, seen from behind, walks along a road through hill country at sunrise, his free hand trailing along a low stone wall.",
         "caption": "Whole is a word for how a person walks, and a blind man can walk whole." + IMAGINED},
        {"slot": "place", "source": "ep10_the_blind_animal/05_malachi.jpg", "name": "law-blind-animals-malachi",
         "alt": "The courtyard of the rebuilt Temple: a lean prophet in a rough cloak, seen from behind, speaks to a group of priests in white by the altar.",
         "caption": "Malachi before the priests who offered the blind, the lame and the sick." + IMAGINED},
    ],
}
for _page, _pics in LAW_PICTURES.items():
    PAGE_PICTURES.setdefault(_page, [])
    PAGE_PICTURES[_page] = [p for p in PAGE_PICTURES[_page] if p["slot"] == "banner"] + _pics


def thumbs() -> list[dict]:
    """Story banners, which are also made small for the list of stories."""
    return [pics[0] for pics in STORY_PICTURES.values()]


THUMB_WIDTH = 400
SOURCE_SIZE = (2752, 1536)   # every painting and map comes out of the tools at this size


def widths(pic: dict) -> tuple:
    return pic.get("widths", WIDTHS)


def size(pic: dict) -> tuple:
    """Width and height of the larger web file, so the page can reserve the space before the picture loads."""
    left, top, right, bottom = pic.get("crop", (0, 0) + SOURCE_SIZE)
    large = widths(pic)[-1]
    return large, round(large * (bottom - top) / (right - left))


def all_pictures() -> list[dict]:
    seen, found = set(), []
    for pics in list(STORY_PICTURES.values()) + list(PAGE_PICTURES.values()):
        for p in pics:
            if p["name"] not in seen:
                seen.add(p["name"])
                found.append(p)
    return found
