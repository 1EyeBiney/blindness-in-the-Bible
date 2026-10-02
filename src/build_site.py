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
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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
    nav = [("index.html", "Home"), ("catalog.html", "The catalog"), ("about.html", "About")]
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


def table(rows: list[dict], caption: str) -> str:
    head = "".join(f'<th scope="col">{h}</th>' for h in ("Reference", "Text", "Who", "How found", "How sure", "Note"))
    body = "".join(
        f'<tr><th scope="row">{e(r["reference"])}</th><td>{e(r["text"])}</td><td>{e(r["who"])}</td>'
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


def index_page(rows: list[dict]) -> str:
    counts = Counter(r["kind"] for r in rows)
    n_word = sum(r["found_by"] == "word" for r in rows)
    people = sorted({r["who"] for r in rows if r["kind"] == "physical" and r["who"]})
    return f"""<h1>Not By Sight</h1>
<blockquote><p>For we walk by faith, not by sight.</p><p>2 Corinthians 5:7</p></blockquote>
<p class="lede">A series of studies on blindness in the Bible, written by a blind Christian for blind believers,
their families, and the church.</p>

<h2>Where this stands</h2>
<p>This site has just begun. The first piece of work is done in draft: a <a href="catalog.html">catalog</a> of every
passage that speaks of blindness. The studies will be built on it.</p>
<ul>
<li>{n_word} verses in the Berean Standard Bible use the word blind in some form.</li>
<li>{len(rows) - n_word} more describe blindness or lost sight without using the word.</li>
<li>{counts['physical']} of the {len(rows)} are about physical blindness, which is where the studies begin.</li>
<li>{counts['legal']} are commands in the law, {counts['promise']} are promises that the blind will see, and
{counts['figurative']} use blindness as a picture of something else.</li>
</ul>

<h2>What is planned</h2>
<ol>
<li>The catalog: every passage, sorted and open to review.</li>
<li>The people: every blind person in Scripture, who was healed, who was not, and what the text says of each.</li>
<li>The healings: what the accounts share and where they differ.</li>
<li>The law: how God commands His people to treat the blind.</li>
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


if __name__ == "__main__":
    render_all()
    print(f"Site written to {OUT}")
