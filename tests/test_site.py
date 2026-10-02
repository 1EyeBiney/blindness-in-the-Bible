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
    pages = sorted(tmp_path.glob("*.html"))
    assert [p.name for p in pages] == ["about.html", "catalog.html", "index.html"]
    for p in pages:
        h = p.read_text(encoding="utf-8")
        assert '<html lang="en">' in h and h.count("<h1>") == 1, p.name
        assert 'href="#main"' in h and 'id="main"' in h, p.name
        assert h.count('aria-current="page"') == 1, p.name
        assert "<img" not in h and "<script" not in h, p.name
        for href in re.findall(r'href="([^"#]+)"', h):
            if href.startswith("http"):
                continue
            assert (tmp_path / href).exists(), f"{p.name}: broken link {href}"
        # headings do not skip levels
        levels = [int(x) for x in re.findall(r"<h([1-6])", h)]
        assert all(b - a <= 1 for a, b in zip(levels, levels[1:])), p.name
    cat = (tmp_path / "catalog.html").read_text(encoding="utf-8")
    assert cat.count("<table>") == cat.count("<caption>") and 'scope="col"' in cat and 'scope="row"' in cat
    assert cat.count('<th scope="row">') == len(rows())
