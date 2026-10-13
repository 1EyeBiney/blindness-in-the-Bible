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
