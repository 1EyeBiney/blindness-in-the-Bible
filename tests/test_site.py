"""Checks on the catalog and on the built site. No Bible text needed:
everything runs from the committed data/catalog.csv."""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import build_site  # noqa: E402


def rows():
    return list(csv.DictReader(open(ROOT / "data" / "catalog.csv", encoding="utf-8")))


def test_catalog_has_every_word_match_once_and_no_duplicates():
    r = rows()
    assert len({x["id"] for x in r}) == len(r)
    assert sum(x["found_by"] == "word" for x in r) == 86
    # every verse marked "word" really uses the word; none marked "described" does
    for x in r:
        has = bool(re.search(r"\bblind", x["text"], re.I))
        assert has == (x["found_by"] == "word"), x["reference"]


def test_every_row_is_fully_classified():
    for x in rows():
        assert x["kind"] in build_site.KIND_TITLES, x["reference"]
        assert x["sub"] in build_site.SUB_TITLES, x["reference"]
        assert x["confidence"] in build_site.CONF and x["text"].strip()
        assert not x["text"].startswith("-") and " ," not in x["text"] and " ." not in x["text"]


def test_text_is_the_official_berean_text_word_for_word():
    src = ROOT / "data" / "raw" / "berean" / "bsb.txt"
    official = dict(line.rstrip("\r").split("\t", 1) for line in src.read_text(encoding="utf-8-sig").split("\n")
                    if "\t" in line)
    for x in rows():
        assert official[x["reference"]].strip() == x["text"], x["reference"]


def test_blindfold_verses_are_set_aside():
    other = [x for x in rows() if x["kind"] == "other"]
    assert len(other) == 3 and all("blindfold" in x["text"].lower() for x in other)


def test_site_builds_and_is_accessible(tmp_path):
    build_site.render_all(tmp_path)
    assert sorted(p.name for p in tmp_path.glob("*.html")) == ["about.html", "accessibility.html", "catalog.html", "check-our-work.html", "episodes.html", "how-it-was-made.html", "index.html", "walk-by-faith.html", "what-blind-means.html"]
    pages = sorted(tmp_path.rglob("*.html"))
    for p in pages:
        h = p.read_text(encoding="utf-8")
        assert '<html lang="en">' in h and h.count("<h1>") == 1, p.name
        assert 'href="#main"' in h and 'id="main"' in h, p.name
        assert h.count('aria-current="page"') == 1, p.name
        # the only script is the reading-settings one, and every picture has a description (or alt="" if decorative)
        assert re.findall(r"<script[^>]*>", h) == [f'<script src="{"../" if p.parent != tmp_path else ""}static/display.js">'], p.name
        assert all(re.search(r'\balt="', m) for m in re.findall(r"<img[^>]*>", h)), p.name
        assert "style=" not in h, p.name
        for src in re.findall(r'<img[^>]*\bsrc="([^"]+)"', h):
            assert (p.parent / src).resolve().is_file(), f"{p.name}: missing picture {src}"
        for fig in re.findall(r"<figure.*?</figure>", h, flags=re.S):
            assert "<figcaption>" in fig and re.search(r'alt="[^"]{20,}"', fig), p.name   # described and captioned
        for m in re.finditer(r"<iframe[^>]*>", h):
            assert 'title="' in m.group(0) and "youtube-nocookie.com/embed/" in m.group(0), p.name
        for href in re.findall(r'href="([^"#]+)"', h):
            # Anything with a scheme points off the site; only relative links
            # name a file that has to exist in the build.
            if href.startswith(("http", "mailto:", "tel:")):
                continue
            assert (p.parent / href).resolve().exists(), f"{p.name}: broken link {href}"
        # headings do not skip levels
        levels = [int(x) for x in re.findall(r"<h([1-6])", h)]
        assert all(b - a <= 1 for a, b in zip(levels, levels[1:])), p.name
    cat = (tmp_path / "catalog.html").read_text(encoding="utf-8")
    assert cat.count("<table>") == cat.count("<caption>") and 'scope="col"' in cat and 'scope="row"' in cat
    assert cat.count('<th scope="row">') == len(rows())


def test_stories_quote_real_passages_and_cover_the_physical_catalog(tmp_path):
    import stories as st
    bible = build_site.load_bible()
    slugs = [x["slug"] for x in st.STORIES]
    assert len(slugs) == len(set(slugs))
    groups = {k for k, _, _ in st.GROUPS}
    for x in st.STORIES:
        assert x["group"] in groups and x["outcome"] in st.OUTCOMES, x["slug"]
        for book, ch, a, z in x["passages"]:
            assert (book, ch, a) in bible and (book, ch, z) in bible, (x["slug"], book, ch, a, z)
        for part in ("around", "happens", "shoes"):
            assert len(x[part]) > 80, (x["slug"], part)
    # every verse about a blind person or group in a narrative belongs to a story
    in_story = build_site.story_for_verses()
    loose = [r["reference"] for r in rows()
             if r["kind"] == "physical" and r["sub"] not in ("possible", "god_makes") and r["reference"] not in in_story]
    # three verses stand outside any story: Moses's undimmed eyes (a contrast), and two later
    # remarks in John that look back on the man born blind
    assert loose == ["Deuteronomy 34:7", "John 10:21", "John 11:37"], loose
    build_site.render_all(tmp_path)
    for x in st.STORIES:
        h = (tmp_path / "stories" / f"{x['slug']}.html").read_text(encoding="utf-8")
        assert x["title"] in h.replace("&#x27;", "'") and "In their shoes" in h and 'class="verse"' in h


def test_story_claims_that_rest_on_a_word_in_the_text():
    bible = build_site.load_bible()
    assert "see again" in bible[("Mark", 10, 51)] and "see again" in bible[("Luke", 18, 41)]
    assert "trees walking" in bible[("Mark", 8, 24)]
    assert "led him by the hand" in bible[("Acts", 9, 8)].replace("led him by the hand", "led him by the hand") or "by the hand" in bible[("Acts", 9, 8)]
    assert "by the hand" in bible[("Acts", 13, 11)] and "by the hand" in bible[("Acts", 22, 11)]
    assert "for my two eyes" in bible[("Judges", 16, 28)]
    assert "I know, my son, I know" in bible[("Genesis", 48, 19)]
    assert "sound of her feet" in bible[("1 Kings", 14, 6)]
    assert "The blind and the lame will never enter the palace" in bible[("2 Samuel", 5, 8)]
    assert "Sabbath" in bible[("John", 9, 14)] and "Brother Saul" in bible[("Acts", 9, 17)]
    assert "Having eyes, do you not see?" in bible[("Mark", 8, 18)]


def test_place_and_time_items_are_sourced_and_rest_on_the_shelf():
    import stories as st
    shelf = ROOT / "data" / "raw" / "shelf"
    squash = lambda x: re.sub(r"\s+", " ", x)          # noqa: E731
    eder = squash((shelf / "edersheim_life_and_times.txt").read_text(encoding="utf-8"))
    wars = squash((shelf / "josephus_wars_pg2850.txt").read_text(encoding="utf-8"))
    siloam = (shelf / "wikipedia_Pool_of_Siloam.wiki.txt").read_text(encoding="utf-8")
    for x in st.STORIES:
        for item in x.get("place_and_time", []):
            assert item["source"].strip() and len(item["text"]) > 40, x["slug"]
    # the quoted words really are in the sources
    assert "a fountain which hath sweet water in it" in wars
    for phrase in ("Gain merit by me", "specially entitled to charity", "made by King Hezekiah", "golden pitcher"):
        assert phrase in eder, phrase
    assert "2004" in siloam and "Shukron" in siloam


def test_every_story_has_a_sourced_place_and_time_section():
    import json
    import stories as st
    cands = json.loads((ROOT / "data" / "reference" / "place_and_time_candidates.json").read_text(encoding="utf-8"))
    final = json.loads((ROOT / "data" / "reference" / "place_and_time.json").read_text(encoding="utf-8"))
    for x in st.STORIES:
        assert x.get("place_and_time"), x["slug"]
        for item in x["place_and_time"]:
            assert item["source"].strip() and len(item["text"]) > 60, x["slug"]
    for slug, items in final.items():
        for item in items:
            assert item["from"], slug
            for key, idx in item["from"]:
                assert cands[key][idx]["evidence"], (slug, key, idx)


def test_context_pages_build_with_open_slots(tmp_path):
    import pages as pg
    build_site.render_all(tmp_path)
    assert len(pg.LAW_PAGES) == 4 and len(pg.LIFE_PAGES) == 6
    for p in pg.PAGES:
        path = tmp_path / ("walk-by-faith.html" if p["section"] == "faith" else f"{p['section']}/{p['slug']}.html")
        h = path.read_text(encoding="utf-8")
        assert "From Brian" in h and "Other voices" in h and 'class="verse"' in h, p["slug"]
        if not p.get("brian"):
            assert "Open for Brian" in h, p["slug"]
    faith = (tmp_path / "walk-by-faith.html").read_text(encoding="utf-8")
    assert "drop-off test" in faith and "Open for Brian" not in faith
    for section in ("law", "life"):
        idx = (tmp_path / section / "index.html").read_text(encoding="utf-8")
        assert all(f'{p["slug"]}.html' in idx for p in pg.by_section(section))


def test_context_pages_have_sourced_place_and_time_traced_to_candidates():
    import json
    import pages as pg
    cands = json.loads((ROOT / "data" / "reference" / "law_and_life_candidates.json").read_text(encoding="utf-8"))
    final = json.loads((ROOT / "data" / "reference" / "law_and_life.json").read_text(encoding="utf-8"))
    for p in pg.PAGES:
        assert p.get("place_and_time"), p["slug"]
        for item in p["place_and_time"]:
            assert item["source"].strip() and len(item["text"]) > 60
    for slug, items in final.items():
        for item in items:
            for key, idx in item["from"]:
                assert cands[key][idx]["evidence"], (slug, key, idx)
    # Hammurabi's eye laws really say what the servant page says they say
    ham = re.sub(r"\s+", " ", (ROOT / "data" / "raw" / "shelf" / "hammurabi_johns_pg17150.txt").read_text(encoding="utf-8"))
    assert "his eye one shall cause to be lost" in ham and "one mina of silver" in ham


def test_followup_items_trace_to_candidates_and_the_hand_led_claim_holds():
    import json
    cands = json.loads((ROOT / "data" / "reference" / "followup_candidates.json").read_text(encoding="utf-8"))
    final = json.loads((ROOT / "data" / "reference" / "followups.json").read_text(encoding="utf-8"))
    for slug, items in final.items():
        for item in items:
            for key, idx in item["from"]:
                assert cands[key][idx]["evidence"], (slug, key, idx)
    bible = build_site.load_bible()
    assert "by the hand" in bible[("Acts", 13, 11)] and "hand" in bible[("Judges", 16, 26)] and "hand" in bible[("Mark", 8, 23)]
    assert "staff" in bible[("Zechariah", 8, 4)]


def test_law_question_items_trace_to_candidates_and_key_quotes_exist():
    import json
    cands = json.loads((ROOT / "data" / "reference" / "law_questions_candidates.json").read_text(encoding="utf-8"))
    final = json.loads((ROOT / "data" / "reference" / "law_questions.json").read_text(encoding="utf-8"))
    for slug, items in final.items():
        for item in items:
            for key, idx in item["from"]:
                assert cands[key][idx]["evidence"], (slug, key, idx)
    shelf = ROOT / "data" / "raw" / "shelf"
    budge = re.sub(r"\s+", " ", (shelf / "budge_amenemopet_1924.txt").read_text(encoding="utf-8", errors="replace"))
    assert "laughing-stock of the blind" in budge
    ham = re.sub(r"\s+", " ", (shelf / "hammurabi_johns_pg17150.txt").read_text(encoding="utf-8"))
    assert "half his price" in ham


def test_picture_pages_build_cover_the_figurative_catalog_and_keep_slots_open(tmp_path):
    import picture as pic
    build_site.render_all(tmp_path)
    covered = set()
    for p in pic.PICTURE_PAGES:
        h = (tmp_path / "picture" / f"{p['slug']}.html").read_text(encoding="utf-8")
        assert "What the picture assumes about the blind" in h and "Who is called blind" in h
        assert ("Open for Brian" in h) == (not p.get("brian")) and "Other voices" in h
        for book, ch, a, z in p["passages"]:
            covered |= {f"{book} {ch}:{v}" for v in range(a, z + 1)}
    loose = [r["reference"] for r in rows() if r["kind"] in ("figurative", "promise") and r["reference"] not in covered]
    assert loose == [], loose
    idx = (tmp_path / "picture" / "index.html").read_text(encoding="utf-8")
    assert all(f'{p["slug"]}.html' in idx for p in pic.PICTURE_PAGES)
    # the claim that no blind person is called a blind guide or spiritually blind: every subject in these
    # passages is sighted; the man born blind is not among the "who" of John 9:39-41
    bible = build_site.load_bible()
    assert "Are we blind too" in bible[("John", 9, 40)] and "Pharisees" in bible[("John", 9, 40)]


def test_picture_place_and_time_traces_to_candidates():
    import json
    import picture as pic
    cands = json.loads((ROOT / "data" / "reference" / "picture_candidates.json").read_text(encoding="utf-8"))
    final = json.loads((ROOT / "data" / "reference" / "picture.json").read_text(encoding="utf-8"))
    for p in pic.PICTURE_PAGES:
        assert p.get("place_and_time"), p["slug"]
    for slug, items in final.items():
        for item in items:
            for key, idx in item["from"]:
                assert cands[key][idx]["evidence"], (slug, key, idx)


def test_spectrum_page_quotes_the_dim_eyes_verses(tmp_path):
    import spectrum
    bible = build_site.load_bible()
    assert "could hardly see" in bible[("Genesis", 48, 10)] and "eyes were dim" in bible[("1 Kings", 14, 4)]
    assert "so weak that he could no longer see" in bible[("Genesis", 27, 1)]
    build_site.render_all(tmp_path)
    h = (tmp_path / spectrum.SLUG).read_text(encoding="utf-8")
    assert "swimming pool" in h and h.count('class="verse"') == len(spectrum.VERSES)
    home = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert spectrum.SLUG in home


def test_dim_eyes_stories_say_how_much_he_could_see(tmp_path):
    import stories as st
    by = {x["slug"]: x for x in st.STORIES}
    assert all(by[k].get("sight") for k in ("isaac", "jacob", "eli", "ahijah"))
    assert sum(1 for x in st.STORIES if x.get("sight")) == 4
    build_site.render_all(tmp_path)
    h = (tmp_path / "stories" / "jacob.html").read_text(encoding="utf-8")
    assert "How much could he see?" in h and 'href="../what-blind-means.html"' in h


def test_the_man_born_blind_has_its_episode(tmp_path):
    import stories as st
    story = next(x for x in st.STORIES if x["slug"] == "man-born-blind")
    assert story["listen"]["youtube"] == "y-fccElFytM"
    assert (ROOT / "media" / story["listen"]["mp3"]).is_file()
    build_site.render_all(tmp_path)
    h = (tmp_path / "stories" / "man-born-blind.html").read_text(encoding="utf-8")
    assert "Listen to this story" in h and "<audio controls" in h and "embed/y-fccElFytM" in h
    assert (tmp_path / "media" / story["listen"]["mp3"]).is_file()
    assert h.index("Listen to this story") < h.index("What led up to it")


def _luminance(hex_colour):
    def chan(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hex_colour[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def _contrast(a, b):
    hi, lo = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def test_every_colour_set_meets_enhanced_contrast():
    """WCAG AAA asks 7 to 1 for text. Every colour set meets it for text, quiet text and links, on the page
    background and on the table-head background. Rules and borders meet the 3 to 1 asked of non-text parts."""
    import display
    for name, t in display.THEMES.items():
        for part in ("fg", "muted", "link"):
            for ground in ("bg", "head"):
                assert _contrast(t[part], t[ground]) >= 7, f"{name}: {part} on {ground} is {_contrast(t[part], t[ground]):.2f}"
        assert _contrast(t["rule"], t["bg"]) >= 3, f"{name}: rule on bg"
    for name in ("contrast-light", "contrast-dark", "yellow"):
        assert _contrast(display.THEMES[name]["fg"], display.THEMES[name]["bg"]) >= 15, name


def test_reading_settings_panel_is_on_every_page_and_is_labelled(tmp_path):
    import display
    build_site.render_all(tmp_path)
    js = (tmp_path / "static" / "display.js").read_text(encoding="utf-8")
    css = (tmp_path / "static" / "style.css").read_text(encoding="utf-8")
    for key, (legend, choices) in display.OPTIONS.items():
        assert choices[0][0] == "", key              # the first choice is always the standard one
        for value, _ in choices[1:]:
            assert f'data-{key}="{value}"' in css, (key, value)   # every choice offered does something
    assert set(v for v, _ in display.OPTIONS["theme"][1] if v) == set(display.THEMES)
    assert "localStorage" in js and "http" not in js  # kept on the device, sent nowhere
    for p in tmp_path.rglob("*.html"):
        h = p.read_text(encoding="utf-8")
        panel = h[h.index('<details class="display"'):h.index("</details>", h.index('<details class="display"'))]
        assert " hidden>" in panel.split("<summary>")[0], p.name      # hidden until the script is known to run
        assert panel.count("<fieldset>") == panel.count("<legend>") == len(display.OPTIONS), p.name
        assert panel.count("<label>") == panel.count('type="radio"'), p.name
        assert 'role="status"' in panel and "accessibility.html" in panel, p.name
        assert h.index("</nav>") < h.index('<details class="display"') < h.index('<main id="main">'), p.name
    cat = (tmp_path / "catalog.html").read_text(encoding="utf-8")
    assert cat.count('class="table-scroll" role="region" tabindex="0" aria-label="') == cat.count("<table>")


def test_story_pictures_are_described_made_and_placed(tmp_path):
    """Every picture listed has a real description, a caption, both web sizes on disk, and a place on its page.
    Stories with every slot filled never carry more than a banner, four pictures and a map."""
    import images
    import stories as st
    slugs = {s["slug"] for s in st.STORIES}
    build_site.render_all(tmp_path)
    for slug, pics in images.STORY_PICTURES.items():
        assert slug in slugs, slug
        slots = [p["slot"] for p in pics]
        assert slots[0] == "banner" and len(slots) == len(set(slots)), slug
        assert set(slots) <= {"banner", "around", "happens", "shoes", "place", "map"}, slug
        h = (tmp_path / "stories" / f"{slug}.html").read_text(encoding="utf-8")
        assert h.count("<figure") == len(pics), slug
        assert h.index("<figure") < h.index("What led up to it"), slug
        assert h.count('loading="lazy"') >= len(pics) - 1, slug
        for p in pics:
            assert len(p["alt"]) >= 30 and p["caption"].endswith((".", "?")), p["name"]
            assert p["alt"] != p["caption"], p["name"]
            for w in images.widths(p):
                f = ROOT / "media" / "images" / f"{p['name']}-{w}.jpg"
                assert f.is_file() and f.stat().st_size < 600_000, f.name
                assert (tmp_path / "media" / "images" / f.name).is_file(), f.name
        assert "imagined, not" in pics[0]["caption"], slug   # paintings are announced as imagined


def test_every_page_has_its_icons_and_a_share_picture_that_exists(tmp_path):
    build_site.render_all(tmp_path)
    for p in tmp_path.rglob("*.html"):
        h = p.read_text(encoding="utf-8")
        og = re.search(r'<meta property="og:image" content="https://blindnessinthebible.com/([^"]+)">', h)
        assert og and (tmp_path / og.group(1)).is_file(), p.name
        assert re.search(r'<meta property="og:image:alt" content="[^"]{30,}">', h), p.name
        assert h.count('class="emblem"') == 1 and 'class="emblem" src' in h and 'alt="" width="48"' in h, p.name
    story = (tmp_path / "stories" / "bartimaeus.html").read_text(encoding="utf-8")
    assert "media/images/bartimaeus-the-crowd-stops-1600.jpg" in story.split("</head>")[0]
    about = (tmp_path / "about.html").read_text(encoding="utf-8")
    assert about.count("<figure") == 1 and "Mister Scaredy Cat" in about and "BRIAN_PORTRAIT" not in about


def test_every_story_and_every_study_page_has_a_banner(tmp_path):
    """Every story, every page under the law, living blind and blindness as a picture, the section fronts, the
    home page and the walk by faith page open with a described, captioned painting. The list of stories shows a
    small picture beside each story, with no description, because the link beside it already names the story."""
    import images
    import pages as pg
    import picture as pic
    import stories as st
    build_site.render_all(tmp_path)
    assert {s["slug"] for s in st.STORIES} == set(images.STORY_PICTURES)
    want = ["index", "stories/index", "law/index", "life/index", "picture/index", "walk-by-faith"]
    want += [f"{sec}/{p['slug']}" for sec in ("law", "life") for p in pg.by_section(sec)]
    want += [f"picture/{p['slug']}" for p in pic.PICTURE_PAGES]
    assert set(want) == set(images.PAGE_PICTURES) - {"about"}
    for key in want:
        h = (tmp_path / f"{key}.html").read_text(encoding="utf-8")
        assert h.count('<figure class="pic banner">') == 1, key
        assert h.index("<h1>") < h.index("<figure") and "imagined, not a record" in h, key
        b = images.PAGE_PICTURES[key][0]
        assert f"media/images/{b['name']}-1600.jpg" in h.split("</head>")[0], key     # shared with its own picture
        if "<h2" in h:
            assert h.index("<figure") < h.index("<h2"), key
    idx = (tmp_path / "stories" / "index.html").read_text(encoding="utf-8")
    assert idx.count('-400.jpg" alt=""') == len(st.STORIES)
    names = [p["name"] for p in images.all_pictures()]
    assert len(names) == len(set(names))
    for b in images.thumbs():
        assert (ROOT / "media" / "images" / f"{b['name']}-{images.THUMB_WIDTH}.jpg").is_file(), b["name"]


def test_episodes_page_lists_every_episode_once_with_audio_mp3_and_youtube(tmp_path):
    """Every story with an episode appears under exactly one episode, and each episode has its audio, its MP3,
    its YouTube link and links to its story pages. Numbers run 1, 2, 3 with none skipped."""
    import episode_list as ep
    import stories as st
    build_site.render_all(tmp_path)
    h = (tmp_path / "episodes.html").read_text(encoding="utf-8")
    assert [n for n, *_ in ep.EPISODES] == list(range(1, len(ep.EPISODES) + 1))
    covered = [slug for _, _, _, slugs, _ in ep.EPISODES for slug in slugs]
    assert sorted(covered) == sorted(s["slug"] for s in st.STORIES if s.get("listen"))
    by_slug = {s["slug"]: s for s in st.STORIES}
    for number, title, _, slugs, about in ep.EPISODES:
        listens = {(by_slug[x]["listen"]["youtube"], by_slug[x]["listen"]["mp3"]) for x in slugs}
        assert len(listens) == 1, title                       # the pages of one episode share one player
        yt, mp3 = listens.pop()
        assert f"_{number:02d}_" in mp3 and f"Episode {number}:" in by_slug[slugs[0]]["listen"]["title"], title
        assert f"<h2>Episode {number}: " in h and f"watch?v={yt}" in h, title
        assert h.count(f'src="media/{mp3}"') == 1 and (tmp_path / "media" / mp3).is_file(), title
        assert all(f'href="stories/{x}.html"' in h for x in slugs) and len(about) > 80, title
    assert h.count("<audio controls") == len(ep.EPISODES) and "<iframe" not in h
    story = (tmp_path / "stories" / "bartimaeus.html").read_text(encoding="utf-8")
    assert 'href="../episodes.html">All the episodes</a>' in story
