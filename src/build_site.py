"""Build the Not By Sight site from data/catalog.csv.

Standard library only. Screen reader first: one h1 per page, headings in
order, a skip link, real tables with captions and scoped headers, no
images, no scripts, nothing conveyed by colour alone.

    python src/build_site.py        -> writes site/
"""
from __future__ import annotations

import csv
import html
import shutil
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
DATA = ROOT / "data" / "catalog.csv"
OUT = ROOT / "site"

SITE_NAME = "Not By Sight"
TAGLINE = "Studies on blindness in the Bible"

KIND_ORDER = ["physical", "legal", "promise", "figurative", "other"]
KIND_TITLES = {
    "physical": "Physical blindness",
    "legal": "The law",
    "promise": "Promises that the blind will see",
    "figurative": "Blindness as a picture",
    "other": "The word appears, but the verse is not about blindness",
}
KIND_INTRO = {
    "physical": "Blind people in the story of Scripture: sight lost in old age, sight taken, sight given back, "
                "and the blind named among those God gathers and Jesus welcomes.",
    "legal": "What God commands about blind people, about blinding someone, about priests, and about blind animals "
             "brought for sacrifice.",
    "promise": "Promises that God will open the eyes of the blind or lead them. These may be meant physically, "
               "figuratively, or both, and are kept apart for that reason.",
    "figurative": "Blindness used as a picture: of leaders who cannot guide, of unbelief, of what a bribe does, "
                  "of grief. This group is listed now and studied later.",
    "other": "Three verses use the word for a blindfold.",
}
SUB_TITLES = {
    "person": "A blind person", "group": "Blind people as a group", "healing": "Sight given or restored",
    "struck": "Sight taken", "age": "Sight lost in old age", "god_makes": "God as maker of sighted and blind",
    "care": "Care and welcome", "protection": "Protection", "injury": "Blinding someone",
    "priesthood": "Priests", "sacrifice": "Blind animals in sacrifice", "restoration": "The blind will see",
    "leaders": "Blind guides and leaders", "people_of_god": "God's people called blind",
    "unbelief": "Unbelief", "bribe": "A bribe blinds", "simile": "Like the blind",
    "curse": "Curse or judgment", "grief": "Eyes failing from grief", "threat": "A threat to blind",
    "blindfold": "Blindfold", "possible": "Possibly poor sight; uncertain",
}
FOUND = {"word": "Uses the word", "described": "Described without the word"}
CONF = {"high": "Clear", "medium": "Open to another reading", "low": "Uncertain"}

CSS = """
:root { --bg:#ffffff; --fg:#1a1a1a; --muted:#4a4a4a; --link:#0b3d91; --rule:#b8b8b8; --head:#f0f0f0; }
@media (prefers-color-scheme: dark) {
  :root { --bg:#121212; --fg:#f2f2f2; --muted:#cfcfcf; --link:#9cc4ff; --rule:#5a5a5a; --head:#222222; }
}
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font: 1.125rem/1.6 Georgia, "Times New Roman", serif; }
.wrap { max-width: 60rem; margin: 0 auto; padding: 0 1rem; }
a { color: var(--link); }
a:focus, summary:focus { outline: 3px solid var(--link); outline-offset: 2px; }
.skip { position:absolute; left:-999px; }
.skip:focus { position:static; display:inline-block; padding:.5rem; }
header.site { border-bottom: 2px solid var(--rule); padding: 1rem 0; }
header.site p.name { font-size: 1.5rem; font-weight: bold; margin: 0; }
header.site p.tag { margin: 0; color: var(--muted); }
nav ul { list-style: none; padding: 0; margin: .5rem 0 0; display: flex; flex-wrap: wrap; gap: 1rem; }
h1 { font-size: 2rem; line-height: 1.25; }
h2 { font-size: 1.5rem; margin-top: 2.5rem; border-top: 1px solid var(--rule); padding-top: 1rem; }
h3 { font-size: 1.2rem; }
.lede { font-size: 1.25rem; }
p.verse { margin: .5rem 0; }
p.slot { border: 1px dashed var(--rule); padding: .75rem; color: var(--muted); }
p.source { color: var(--muted); font-size: 1rem; margin: -.5rem 0 1.25rem 1rem; }
blockquote { margin: 1rem 0; padding: .25rem 1rem; border-left: 4px solid var(--rule); }
.table-scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
caption { text-align: left; font-weight: bold; padding: .5rem 0; }
th, td { border: 1px solid var(--rule); padding: .5rem; text-align: left; vertical-align: top; }
thead th { background: var(--head); }
footer { border-top: 2px solid var(--rule); margin-top: 3rem; padding: 1rem 0 2rem; color: var(--muted); font-size: 1rem; }
"""


def e(s) -> str:
    return html.escape(str(s), quote=True)


def page(title: str, body: str, current: str, root: str = "") -> str:
    nav = [("index.html", "Home"), ("stories/index.html", "The stories"), ("law/index.html", "The law"),
           ("life/index.html", "Living blind, then"), ("walk-by-faith.html", "Walk by faith"),
           ("catalog.html", "The catalog"), ("about.html", "About")]
    links = "".join(
        f'<li><a href="{root}{href}"{" aria-current=\"page\"" if href == current else ""}>{e(label)}</a></li>'
        for href, label in nav)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | {SITE_NAME}</title>
<meta name="description" content="{e(TAGLINE)}. For we walk by faith, not by sight.">
<link rel="stylesheet" href="{root}static/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
<header class="site"><div class="wrap">
<p class="name">{SITE_NAME}</p>
<p class="tag">{e(TAGLINE)}</p>
<nav aria-label="Site"><ul>{links}</ul></nav>
</div></header>
<main id="main"><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
<p>Scripture quotations are from the Holy Bible, Berean Standard Bible, BSB, which has been dedicated to the public
domain. The text is used exactly as published at <a href="https://berean.bible">berean.bible</a>.</p>
<p>Not By Sight is a work in progress by Brian Clark.</p>
</div></footer>
</body>
</html>
"""


def load() -> list[dict]:
    return list(csv.DictReader(open(DATA, encoding="utf-8")))


def load_bible() -> dict:
    """(book, chapter, verse) -> text, from the official Berean file."""
    import re
    out = {}
    src = ROOT / "data" / "raw" / "berean" / "bsb.txt"
    for line in src.read_text(encoding="utf-8-sig").split("\n"):
        m = re.match(r"^((?:[1-3] )?[A-Za-z ]+?) (\d+):(\d+)\t(.*)$", line.rstrip("\r"))
        if m:
            out[(m.group(1), int(m.group(2)), int(m.group(3)))] = m.group(4).strip()
    return out


def passage_label(p) -> str:
    book, ch, a, z = p
    return f"{book} {ch}:{a}-{z}" if z > a else f"{book} {ch}:{a}"


def story_for_verses() -> dict:
    """reference -> story, for every verse inside a story's passages."""
    import stories as st
    out = {}
    for story in st.STORIES:
        for book, ch, a, z in story["passages"]:
            for v in range(a, z + 1):
                out.setdefault(f"{book} {ch}:{v}", story)
    return out


def table(rows: list[dict], caption: str) -> str:
    in_story = story_for_verses()
    head = "".join(f'<th scope="col">{h}</th>' for h in ("Reference", "Text", "Who", "Story", "How found", "How sure", "Note"))

    def story_cell(r):
        st_ = in_story.get(r["reference"])
        return f'<a href="stories/{st_["slug"]}.html">{e(st_["title"])}</a>' if st_ else ""
    body = "".join(
        f'<tr><th scope="row">{e(r["reference"])}</th><td>{e(r["text"])}</td><td>{e(r["who"])}</td>'
        f'<td>{story_cell(r)}</td>'
        f'<td>{e(FOUND[r["found_by"]])}</td><td>{e(CONF[r["confidence"]])}</td><td>{e(r["note"])}</td></tr>'
        for r in rows)
    return (f'<div class="table-scroll"><table><caption>{e(caption)}</caption>'
            f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>")


def catalog_page(rows: list[dict]) -> str:
    counts = Counter(r["kind"] for r in rows)
    n_word = sum(r["found_by"] == "word" for r in rows)
    n_desc = len(rows) - n_word
    parts = [
        "<h1>The catalog</h1>",
        f'<p class="lede">Every passage found so far that speaks of blindness: {len(rows)} verses. '
        f"{n_word} use the word blind in some form. {n_desc} more describe blindness or lost sight without the word.</p>",
        "<p>The sorting below is a reader's judgment, not a fact about the text. The column headed How sure marks "
        "the calls most open to another reading. This is a first draft for review.</p>",
        "<h2>Jump to a group</h2><ul>",
    ]
    for k in KIND_ORDER:
        parts.append(f'<li><a href="#{k}">{e(KIND_TITLES[k])}</a>: {counts[k]} verses</li>')
    parts.append("</ul>")
    for k in KIND_ORDER:
        group = [r for r in rows if r["kind"] == k]
        parts.append(f'<h2 id="{k}">{e(KIND_TITLES[k])}</h2><p>{e(KIND_INTRO[k])}</p>')
        subs = OrderedDict()
        for r in group:
            subs.setdefault(r["sub"], []).append(r)
        for sub, items in sorted(subs.items(), key=lambda kv: -len(kv[1])):
            title = SUB_TITLES[sub]
            parts.append(f"<h3>{e(title)}</h3>")
            parts.append(table(items, f"{KIND_TITLES[k]}: {title} ({len(items)} verses)"))
    parts.append('<h2>Download</h2><p><a href="data/catalog.csv">The whole catalog as a spreadsheet file (CSV)</a>.</p>')
    return "\n".join(parts)


def stories_index() -> str:
    import stories as st
    parts = ["<h1>The stories</h1>",
             f'<p class="lede">The verses in the catalog are not scattered sayings. Most belong to a story: a person, '
             f"a place, something that led up to the moment and something that came after. Here are "
             f"{len(st.STORIES)} of them, each with the full passage.</p>",
             "<p>Every story has three parts besides the passage itself: what led up to it, what happens, and what "
             "the text lets us notice from the blind person's side. That last part is an invitation to stand where "
             "they stood.</p>"]
    for key, title, intro in st.GROUPS:
        group = [x for x in st.STORIES if x["group"] == key]
        parts.append(f"<h2>{e(title)}</h2><p>{e(intro)}</p><ul>")
        for x in group:
            refs = "; ".join(passage_label(p) for p in x["passages"])
            parts.append(f'<li><a href="{x["slug"]}.html">{e(x["title"])}</a>. {e(refs)}. '
                         f'{e(st.OUTCOMES[x["outcome"]])}.</li>')
        parts.append("</ul>")
    return "\n".join(parts)


def story_page(story: dict, bible: dict, order: list[dict]) -> str:
    import stories as st
    i = order.index(story)
    prev_, next_ = (order[i - 1] if i > 0 else None), (order[i + 1] if i + 1 < len(order) else None)
    group_title = next(t for k, t, _ in st.GROUPS if k == story["group"])
    parts = ['<p><a href="index.html">All the stories</a></p>',
             f"<h1>{e(story['title'])}</h1>",
             f'<p class="lede">{e(group_title)}. {e(st.OUTCOMES[story["outcome"]])}. '
             f'{e("; ".join(passage_label(p) for p in story["passages"]))}.</p>',
             f"<h2>What led up to it</h2><p>{e(story['around'])}</p>",
             f"<h2>What happens</h2><p>{e(story['happens'])}</p>",
             f"<h2>In their shoes</h2><p>{e(story['shoes'])}</p>"]
    if story.get("brian"):
        parts.append("<h2>From Brian</h2>")
        parts.extend(f"<p>{e(para)}</p>" for para in story["brian"])
    if story.get("place_and_time"):
        parts.append("<h2>The place and the time</h2>")
        parts.append("<p>What the old books and the archaeologists can add. Each paragraph names its source.</p>")
        for item in story["place_and_time"]:
            parts.append(f"<p>{e(item['text'])}</p><p class=\"source\">Source: {e(item['source'])}</p>")
    parts.append("<h2>The passage</h2>")
    for p in story["passages"]:
        book, ch, a, z = p
        parts.append(f"<h3>{e(passage_label(p))}</h3>")
        for v in range(a, z + 1):
            text = bible.get((book, ch, v))
            if text:
                parts.append(f'<p class="verse"><b>{v}</b> {e(text)}</p>')
    nav = []
    if prev_:
        nav.append(f'Previous: <a href="{prev_["slug"]}.html">{e(prev_["title"])}</a>')
    if next_:
        nav.append(f'Next: <a href="{next_["slug"]}.html">{e(next_["title"])}</a>')
    parts.append("<h2>More stories</h2><ul>" + "".join(f"<li>{n}</li>" for n in nav) +
                 '<li><a href="index.html">All the stories</a></li></ul>')
    return "\n".join(parts)


def slot_html(page: dict) -> str:
    """Brian's words and other voices, or the open slots where they will go."""
    parts = ["<h2>From Brian</h2>"]
    if page.get("brian"):
        parts.extend(f"<p>{e(p)}</p>" for p in page["brian"])
    else:
        q = page.get("question") or "What this passage says to someone who lives without sight."
        parts.append(f'<p class="slot">Open for Brian: {e(q)}</p>')
    parts.append("<h2>Other voices</h2>")
    if page.get("voices"):
        for v in page["voices"]:
            parts.append(f"<p>{e(v['text'])}</p><p class=\"source\">{e(v['who'])}</p>")
    else:
        parts.append('<p class="slot">Open: other blind people and their families will be asked the same question, '
                     'and their answers will appear here with their permission.</p>')
    return "\n".join(parts)


def context_page(page: dict, bible: dict, root: str, back: tuple[str, str]) -> str:
    parts = [f'<p><a href="{back[0]}">{e(back[1])}</a></p>', f"<h1>{e(page['title'])}</h1>"]
    if page.get("question"):
        parts.append(f'<p class="lede">{e(page["question"])}</p>')
    parts.append(f'<p class="lede">{e("; ".join(passage_label(p) for p in page["passages"]))}.</p>')
    parts.append(f"<h2>What leads up to it</h2><p>{e(page['around'])}</p>")
    parts.append(f"<h2>What it says</h2><p>{e(page['says'])}</p>")
    parts.append(f"<h2>What it may tell us</h2><p>{e(page['notice'])}</p>")
    parts.append(slot_html(page))
    if page.get("place_and_time"):
        parts.append("<h2>The place and the time</h2>")
        parts.append("<p>What the old books and the archaeologists can add. Each paragraph names its source.</p>")
        for item in page["place_and_time"]:
            parts.append(f"<p>{e(item['text'])}</p><p class=\"source\">Source: {e(item['source'])}</p>")
    parts.append("<h2>The passage</h2>")
    for p in page["passages"]:
        book, ch, a, z = p
        parts.append(f"<h3>{e(passage_label(p))}</h3>")
        for v in range(a, z + 1):
            text = bible.get((book, ch, v))
            if text:
                parts.append(f'<p class="verse"><b>{v}</b> {e(text)}</p>')
    parts.append(f'<p><a href="{back[0]}">{e(back[1])}</a></p>')
    return "\n".join(parts)


def section_index(section: str) -> str:
    import pages as pg
    title, intro = pg.SECTIONS[section]
    parts = [f"<h1>{e(title)}</h1>", f'<p class="lede">{e(intro)}</p>', "<ul>"]
    for p in pg.by_section(section):
        refs = "; ".join(passage_label(x) for x in p["passages"])
        line = f'<li><a href="{p["slug"]}.html">{e(p["title"])}</a>. {e(refs)}.'
        if p.get("question"):
            line += f" {e(p['question'])}"
        parts.append(line + "</li>")
    parts.append("</ul>")
    if section == "life":
        parts.append("<p>Each page ends with two open spaces: one for Brian's answer to the question at the top, and "
                     "one for other people who live without sight. The point of these pages is to be filled in by "
                     "people who know.</p>")
    return "\n".join(parts)


def index_page(rows: list[dict]) -> str:
    counts = Counter(r["kind"] for r in rows)
    n_word = sum(r["found_by"] == "word" for r in rows)
    people = sorted({r["who"] for r in rows if r["kind"] == "physical" and r["who"]})
    return f"""<h1>Not By Sight</h1>
<blockquote><p>For we walk by faith, not by sight.</p><p>2 Corinthians 5:7</p></blockquote>
<p class="lede">A series of studies on blindness in the Bible, written by a blind Christian for blind believers,
their families, and the church.</p>

<h2>Where this stands</h2>
<p>This site is being built in the open. The <a href="stories/index.html">stories</a> gather the verses into the
passages they belong to, with what led up to each, what it was like to be there, and what the old books and the
archaeologists can add. <a href="law/index.html">The law</a> reads what God commanded about the blind as evidence of
how they were treated. <a href="life/index.html">Living blind, then</a> asks what daily life was like for a blind
person in each kind of place Scripture shows, and leaves room for the people who know to answer.
<a href="walk-by-faith.html">Walk by faith</a> is the verse this whole site is named for. The
<a href="catalog.html">catalog</a> lists every verse that speaks of blindness.</p>
<ul>
<li>{n_word} verses in the Berean Standard Bible use the word blind in some form.</li>
<li>{len(rows) - n_word} more describe blindness or lost sight without using the word.</li>
<li>{counts['physical']} of the {len(rows)} are about physical blindness, which is where the studies begin.</li>
<li>{counts['legal']} are commands in the law, {counts['promise']} are promises that the blind will see, and
{counts['figurative']} use blindness as a picture of something else.</li>
</ul>

<h2>What is planned</h2>
<ol>
<li>The catalog: every passage, sorted and open to review. Done in draft.</li>
<li>The stories, with the place and the time behind each. Done in draft and reviewed by Brian.</li>
<li>The law, read as evidence of how blind people were treated. Pages built; place and time to follow.</li>
<li>Living blind, then: four settings, with Brian's answers and other voices still to come.</li>
<li>Blindness as a picture, and the wider themes of sight, light and darkness. Later.</li>
</ol>

<h2>People and groups found so far</h2>
<p>{len(people)} people and groups appear in the passages about physical blindness.</p>
<ul>
{''.join(f'<li>{e(p)}</li>' for p in people)}
</ul>
"""


ABOUT = """<h1>About</h1>
<p class="lede">Why this exists, and how it is being made.</p>

<h2>The verse</h2>
<p>Walking by faith took time to learn. The same is true for anyone moving to life without sight: it takes time to
trust new methods and new tools, like a white cane or a screen reader. That is why 2 Corinthians 5:7 has slowly
become my verse.</p>
<p>Brian Clark</p>

<h2>How the work is done</h2>
<ul>
<li>Every study starts from the text. The catalog lists each passage so that any reader can check it.</li>
<li>Sorting passages into groups is a judgment. Where a passage could be read another way, the catalog says so.</li>
<li>Physical blindness comes first. Blindness as a picture, and the wider themes of sight, light and darkness,
come later.</li>
<li>The site is built for screen readers first: plain headings, real tables, no images that carry meaning.</li>
</ul>

<h2>The text</h2>
<p>Scripture is quoted from the Holy Bible, Berean Standard Bible, BSB, produced in cooperation with Bible Hub,
Discovery Bible, OpenBible.com, and the Berean Bible Translation Committee. It was dedicated to the public domain on
April 30, 2023. The official text is used word for word, as published at
<a href="https://berean.bible">berean.bible</a>.</p>

<h2>The reference shelf</h2>
<p>For the place and the time behind each story, the site draws on works that are in the public domain or freely
licensed, and names the source beside every statement taken from them:</p>
<ul>
<li>Alfred Edersheim, <cite>Sketches of Jewish Social Life in the Days of Christ</cite> (1876) and <cite>The Life and
Times of Jesus the Messiah</cite> (1883).</li>
<li>Josephus, <cite>The Antiquities of the Jews</cite> and <cite>The Wars of the Jews</cite>, translated by William
Whiston.</li>
<li><cite>Smith's Bible Dictionary</cite> (1884 edition) and the <cite>International Standard Bible Encyclopedia</cite>
(1915).</li>
<li>Matthew Henry's <cite>Commentary</cite>, the volumes on Genesis to Deuteronomy and Matthew to John.</li>
<li>Wikipedia articles on the places, under the Creative Commons Attribution-ShareAlike 4.0 license, cited by
revision date.</li>
</ul>
<p>These older works carry the assumptions of their time, and some speak of the Jewish people and teachers of Jesus's
day in ways we would not. They are used for facts about places, customs and daily life, read with that in mind.</p>

<h2>Made with help</h2>
<p>The research and the site are built by Brian Clark working with Claude, an AI model made by Anthropic. Brian
decides what the studies conclude.</p>
"""


def render_all(out: Path = OUT) -> None:
    rows = load()
    out.mkdir(parents=True, exist_ok=True)
    for sub in ("static", "data"):
        (out / sub).mkdir(exist_ok=True)
    (out / "static" / "style.css").write_text(CSS, encoding="utf-8")
    shutil.copy(DATA, out / "data" / "catalog.csv")
    (out / "index.html").write_text(page("Home", index_page(rows), "index.html"), encoding="utf-8")
    (out / "catalog.html").write_text(page("The catalog", catalog_page(rows), "catalog.html"), encoding="utf-8")
    (out / "about.html").write_text(page("About", ABOUT, "about.html"), encoding="utf-8")
    import stories as st
    bible = load_bible()
    (out / "stories").mkdir(exist_ok=True)
    (out / "stories" / "index.html").write_text(
        page("The stories", stories_index(), "stories/index.html", root="../"), encoding="utf-8")
    import pages as pg
    for section in ("law", "life"):
        (out / section).mkdir(exist_ok=True)
        (out / section / "index.html").write_text(
            page(pg.SECTIONS[section][0], section_index(section), f"{section}/index.html", root="../"), encoding="utf-8")
        for p_ in pg.by_section(section):
            (out / section / f"{p_['slug']}.html").write_text(
                page(p_["title"], context_page(p_, bible, "../", ("index.html", pg.SECTIONS[section][0])),
                     f"{section}/index.html", root="../"), encoding="utf-8")
    (out / "walk-by-faith.html").write_text(
        page(pg.FAITH_PAGE["title"], context_page(pg.FAITH_PAGE, bible, "", ("index.html", "Home")),
             "walk-by-faith.html", root=""), encoding="utf-8")
    order = [x for key, _, _ in st.GROUPS for x in st.STORIES if x["group"] == key]
    for story in st.STORIES:
        (out / "stories" / f"{story['slug']}.html").write_text(
            page(story["title"], story_page(story, bible, order), "stories/index.html", root="../"), encoding="utf-8")


if __name__ == "__main__":
    render_all()
    print(f"Site written to {OUT}")
