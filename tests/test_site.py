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
    assert sorted(p.name for p in tmp_path.glob("*.html")) == ["a-blind-mans-car.html", "about.html", "accessibility.html", "bookshelf.html", "brian-asks.html", "catalog.html", "check-our-work.html", "episodes.html", "how-it-was-made.html", "index.html", "walk-by-faith.html", "what-blind-means.html", "whats-new.html", "words.html"]
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
    assert story["listen"]["youtube"] == "zZlWP-E0rdU"
    assert (ROOT / "media" / story["listen"]["mp3"]).is_file()
    build_site.render_all(tmp_path)
    h = (tmp_path / "stories" / "man-born-blind.html").read_text(encoding="utf-8")
    assert "Listen to this story" in h and "<audio controls" in h and "embed/zZlWP-E0rdU" in h
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
        maps = sum(1 for x in images.PAGE_PICTURES[key] if x["slot"] == "map")   # a map is shown full width too
        assert h.count('<figure class="pic banner">') == 1 + maps, key
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
    """Every story or study page with an episode appears under exactly one episode, and each episode has its audio,
    its MP3, its YouTube link and links to its pages. Numbers run 1, 2, 3 with none skipped. A study page is named
    by its path (law/stumbling-block), a story by its slug."""
    import episode_list as ep
    import pages as pg
    import stories as st
    build_site.render_all(tmp_path)
    h = (tmp_path / "episodes.html").read_text(encoding="utf-8")
    assert [n for n, *_ in ep.EPISODES] == list(range(1, len(ep.EPISODES) + 1))
    covered = [slug for _, _, _, slugs, _ in ep.EPISODES for slug in slugs]
    by_slug = {s["slug"]: s for s in st.STORIES}
    by_slug.update({f'{p["section"]}/{p["slug"]}': p for p in pg.PAGES})
    assert sorted(covered) == sorted(k for k, s in by_slug.items() if s.get("listen"))
    for number, title, _, slugs, about in ep.EPISODES:
        listens = {(by_slug[x]["listen"]["youtube"], by_slug[x]["listen"]["mp3"]) for x in slugs}
        assert len(listens) == 1, title                       # the pages of one episode share one player
        yt, mp3 = listens.pop()
        assert f"_{number:02d}_" in mp3 and f"Episode {number}:" in by_slug[slugs[0]]["listen"]["title"], title
        assert f"<h2>Episode {number}: " in h and f"watch?v={yt}" in h, title
        assert h.count(f'src="media/{mp3}"') == 1 and (tmp_path / "media" / mp3).is_file(), title
        assert all(f'href="{x if "/" in x else "stories/" + x}.html"' in h for x in slugs) and len(about) > 80, title
    assert h.count("<audio controls") == len(ep.EPISODES) + 1 and "<iframe" not in h      # the episodes and the trailer
    story = (tmp_path / "stories" / "bartimaeus.html").read_text(encoding="utf-8")
    assert 'href="../episodes.html">All the episodes</a>' in story


def test_the_trailer_is_on_the_home_page_and_the_episodes_page(tmp_path):
    """The home page gains one short section and no more: a heading, the audio, the video, a link to the episodes."""
    import episode_list as ep
    build_site.render_all(tmp_path)
    t = ep.TRAILER
    assert (ROOT / "media" / t["mp3"]).is_file()
    home = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert home.count("<h2>Listen to the stories</h2>") == 1
    assert home.count("<audio controls") == 1 and home.count("<iframe") == 1
    assert f'embed/{t["youtube"]}' in home and f'src="media/{t["mp3"]}"' in home
    assert home.index("what blind means here") < home.index("Listen to the stories") < home.index("Where this stands")
    assert 'href="episodes.html">All the episodes</a>' in home
    eps = (tmp_path / "episodes.html").read_text(encoding="utf-8")
    assert eps.index("Start here: the trailer") < eps.index("Episode 1:") and f'watch?v={t["youtube"]}' in eps
    assert ep.PLAYLIST.startswith("https://www.youtube.com/playlist?list=") and eps.count(ep.PLAYLIST) == 1


def test_the_word_sections_rest_on_the_tagged_hebrew_text(tmp_path):
    """Every verse listed under a Hebrew word really uses that word, by Strong's number, in the tagged text; the
    gloss is Strong's own; and the section sits on each Law page between What to notice and From Brian."""
    import hebrew
    import pages as pg
    import words as wd
    import stories as st
    law = {p["slug"] for p in pg.by_section("law")}
    assert law <= set(wd.WORDS) and set(wd.WORDS) - law <= {s["slug"] for s in st.STORIES}
    bible = build_site.load_bible()
    for slug, entries in wd.WORDS.items():
        for w in entries:
            entry = hebrew.entry(w["number"])
            first = w["gloss"].split(",")[0].split(";")[0].split(" from ")[0].strip().lower()
            assert first in entry["strongs_def"].lower(), (w["number"], first)
            for book, ch, v in w["verses"]:
                assert hebrew.has(book, ch, v, w["number"]), (slug, w["spelling"], book, ch, v)
                assert (book, ch, v) in bible, (book, ch, v)
    build_site.render_all(tmp_path)
    for slug in law:
        h = (tmp_path / "law" / f"{slug}.html").read_text(encoding="utf-8")
        assert h.count("<h2>The word</h2>") == 1, slug
        assert h.index("What it may tell us") < h.index("<h2>The word</h2>") < h.index("<h2>From Brian</h2>"), slug

        assert h.count("entry H") == len(wd.WORDS[slug]), slug
    sb = (tmp_path / "law" / "stumbling-block.html").read_text(encoding="utf-8")
    assert "mikshol" in sb and "parking stops" in sb and sb.index("mikshol") < sb.index("parking stops")


def test_bookshelf_lists_every_source_with_its_pages(tmp_path):
    """Every text source on the shelf appears on the bookshelf page, every main work is cited by at least one page,
    every cited page exists, and the record's licence is shown for each work."""
    import bookshelf as bs
    build_site.render_all(tmp_path)
    h = (tmp_path / "bookshelf.html").read_text(encoding="utf-8")
    shown = {f for w in bs.works() for d in w["entries"] for f in d["files"]}
    shown |= {f for d in bs.entries() for f in d["files"] if f.startswith("wikipedia_") and f.endswith(".wiki.txt")}
    for d in bs.entries():
        for f in d["files"]:
            if not f.endswith(bs.SKIP) and f != "oshb_README.md":
                assert f in shown, f"{f} is on the shelf but not on the bookshelf page"
    for w in bs.works():
        assert build_site.e(w["title"]) in h and "<b>Terms:</b>" in h
        if not w["title"].startswith(("The Pulpit", "Easton")):
            assert w["pages"], w["title"]
        for href, _ in w["pages"]:
            assert (tmp_path / href).is_file(), href
    assert sum(1 for a in bs.wikipedia() if a["pages"]) >= 10
    assert h.index("The books") < h.index("Wikipedia articles") < h.index("The full record")


def test_whats_new_is_dated_linked_and_fed(tmp_path):
    """Entries run newest first with valid dates, every link points at a real page, the feed is well-formed XML with
    one item per entry, the menu link carries the newest date for the script, and the page reads as a plain list."""
    import datetime
    import xml.etree.ElementTree as ET
    import whats_new as wn
    build_site.render_all(tmp_path)
    dates = [datetime.date.fromisoformat(d) for d, *_ in wn.ENTRIES]
    assert dates == sorted(dates, reverse=True) and len(wn.ENTRIES) >= 5
    for date, title, text, href in wn.ENTRIES:
        assert (tmp_path / href).is_file(), href
        assert title and len(text) > 30 and not text.endswith(" ")
    h = (tmp_path / "whats-new.html").read_text(encoding="utf-8")
    assert h.count('<li data-date="') == len(wn.ENTRIES) and 'role="status"' in h and "feed.xml" in h
    assert 'id="nav-whats-new" data-latest="' + wn.ENTRIES[0][0] + '"' in h
    root = ET.fromstring((tmp_path / "feed.xml").read_text(encoding="utf-8"))
    assert len(root.findall("./channel/item")) == len(wn.ENTRIES)
    home = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert 'type="application/rss+xml"' in home and "nbs-visit" in (tmp_path / "static" / "display.js").read_text(encoding="utf-8")
    about = (tmp_path / "about.html").read_text(encoding="utf-8")
    assert 'href="bookshelf.html"' in about


def test_brian_after_the_study_closes_the_page(tmp_path):
    """Brian, 17 October 2026: his thought once the study was done belongs after the whole study, so it is the last
    section on the stumbling-block page, after The passage, and only pages that have one show the heading."""
    build_site.render_all(tmp_path)
    h = (tmp_path / "law" / "stumbling-block.html").read_text(encoding="utf-8")
    assert h.index("<h2>The passage</h2>") < h.index("<h2>Brian, after the study</h2>")
    assert "He is always watching, even when nobody else is, and He knows." in h
    assert "<h2>Brian, after the study</h2>" not in (tmp_path / "law" / "servant-blinded.html").read_text(encoding="utf-8")


def test_law_pages_carry_pictures_from_their_episodes(tmp_path):
    """Brian, 20 October 2026: each Law page has a banner and four pictures from its episode, one under each main
    section, like the story pages; the stumbling-block page also has its map. Each is described, captioned, made at
    both web sizes, and announced as imagined."""
    import images
    build_site.render_all(tmp_path)
    order = ["<h2>What leads up to it</h2>", "<h2>What it says</h2>", "<h2>The word</h2>", "<h2>The place and the time</h2>"]
    for page, pics in images.LAW_PICTURES.items():
        h = (tmp_path / f"{page}.html").read_text(encoding="utf-8")
        assert h.count("<figure") == len(pics) + 1, page            # plus the banner
        for slot, head in zip(("around", "says", "word", "place"), order):
            p = next(x for x in pics if x["slot"] == slot)
            assert h.index(head) < h.index(p["name"]), (page, slot)
        for p in pics:
            assert len(p["alt"]) >= 30 and p["alt"] != p["caption"] and p["caption"].endswith("."), p["name"]
            assert p["slot"] == "map" or "imagined, not a record" in p["caption"], p["name"]
            for w in images.widths(p):
                f = ROOT / "media" / "images" / f"{p['name']}-{w}.jpg"
                assert f.is_file() and f.stat().st_size < 600_000, f.name
    assert "map-ep07" in (tmp_path / "law" / "stumbling-block.html").read_text(encoding="utf-8")


def test_words_page_counts_and_verses_rest_on_the_tagged_texts(tmp_path):
    """Every word on the words page has a real count from the tagged Hebrew or Greek text, every sample verse
    contains the word, every number used by a page's own word section is on the page, and the Greek sources
    are cited."""
    import lexicon as lx
    import words as wd
    build_site.render_all(tmp_path)
    h = (tmp_path / "words.html").read_text(encoding="utf-8")
    keys = set()
    for _, _, entries in lx.GROUPS:
        for w in entries:
            lx.check(w)
            n, nv, verses = lx.count_and_verses(w)
            assert n >= nv >= len(w["samples"]) >= 1, w["spelling"]
            assert f'id="{w["spelling"]}"' in h and w["say"] in h, w["spelling"]
            keys.add(w["key"])
    for slug, entries in wd.WORDS.items():
        for w in entries:
            assert w["number"] in keys, (slug, w["number"])
    assert "MorphGNT" in h and "Strong's Greek" in h and 'href="what-blind-means.html"' in h
    assert h.index("The words for blind") < h.index("Sight going") < h.index("Sight taken") < h.index("Around the blind")


def test_brian_asks_answers_rest_on_the_pages_they_link(tmp_path):
    """Every question links to pages that exist, the first linked page carries the phrase the short answer rests on,
    every open question names a real page, and the Open section comes last."""
    import questions as qs
    build_site.render_all(tmp_path)
    h = (tmp_path / qs.SLUG).read_text(encoding="utf-8")
    import html as _html
    for heading, _, entries in qs.GROUPS:
        assert f'id="{build_site.slugify(heading)}"' in h
        for q in entries:
            assert q["links"] and q["asked"] and q["check"], q["q"]
            for href, title in q["links"]:
                assert (tmp_path / href).is_file(), href
            first = _html.unescape(re.sub(r"<[^>]+>", " ", (tmp_path / q["links"][0][0]).read_text(encoding="utf-8")))
            assert q["check"] in first, (q["q"], q["check"])
            assert "I " not in q["q"] and "Brian asked" not in q["q"], q["q"]   # third person, no narration
    for q in qs.OPEN:
        assert (tmp_path / q["where"]).is_file(), q["where"]
    assert h.rindex('<h2 id="open">') > max(h.index(f'id="{build_site.slugify(g[0])}"') for g in qs.GROUPS)
    assert 'href="brian-asks.html"' in (tmp_path / "index.html").read_text(encoding="utf-8")


def test_brians_car_story_is_built_but_unlinked_until_he_says(tmp_path):
    """The page exists at its address with every section, carries Brian's text unchanged, and while LINKED is
    False it has a no-index tag and no other page links to it."""
    import brian_story as bst
    build_site.render_all(tmp_path)
    h = (tmp_path / bst.SLUG).read_text(encoding="utf-8")
    secs = bst.sections()
    assert len(secs) >= 8 and all(f'id="{build_site.slugify(hd)}"' in h for hd, _ in secs[1:])
    import html as _html
    text = _html.unescape(h)
    for _, paras in secs:
        for p in paras:
            assert p in text, p[:60]
    linked = [f for f in tmp_path.rglob("*.html") if f.name != bst.SLUG and bst.SLUG in f.read_text(encoding="utf-8")]
    if bst.LINKED:
        assert 'name="robots"' not in h and linked
    else:
        assert '<meta name="robots" content="noindex">' in h and not linked


def test_threads_follow_the_text_and_are_linked_from_the_stories(tmp_path):
    import threads as th
    build_site.render_all(tmp_path)
    bible = build_site.load_bible()
    idx = (tmp_path / "stories" / "index.html").read_text(encoding="utf-8")
    for t in th.THREADS:
        h = (tmp_path / "stories" / f"{t['slug']}.html").read_text(encoding="utf-8")
        assert f'href="{t["slug"]}.html"' in idx and 'aria-current="page"' in h
        for s in t["sections"]:
            assert f'id="{build_site.slugify(s["heading"])}"' in h, s["heading"]
            assert all(bible.get((b, c, a)) for b, c, a, _ in s["passages"]), s["heading"]
            if s.get("see"):
                assert (tmp_path / "stories" / s["see"][0]).is_file()
    seen = (tmp_path / "stories" / "seen-and-unseen.html").read_text(encoding="utf-8")
    assert "they did not recognize him" in seen and "I know, my son, I know" in seen
    assert "did not recognize him, because his hands were hairy" in bible[("Genesis", 27, 23)]
    assert "Examine it" in bible[("Genesis", 37, 32)] and "examine them" in bible[("Genesis", 38, 25)]
    for slug in ("isaac", "jacob"):     # the two Genesis stories carry the frame and point at the thread
        h = (tmp_path / "stories" / f"{slug}.html").read_text(encoding="utf-8")
        assert "Where this falls in his life" in h and 'href="seen-and-unseen.html"' in h
        assert h.index("Where this falls in his life") < h.index("What led up to it")


def test_the_thread_verb_nakar_is_in_every_verse_the_page_says_it_is():
    import hebrew as hb
    for ch, vs, n in [(27, 23, 1), (37, 32, 1), (37, 33, 1), (38, 25, 1), (38, 26, 1), (42, 7, 2), (42, 8, 2)]:
        assert sum(w["strongs"] == "H5234" for w in hb.words("Genesis", ch, vs)) == n, (ch, vs)
    assert "scrutinize" in hb.entry("H5234")["strongs_def"] and "look intently" in hb.entry("H5234")["strongs_def"]
    assert hb.has("Genesis", 29, 17, "H7390")    # Leah's eyes: rak, tender, by implication weak
