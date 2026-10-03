"""Checks on the reference shelf. No network: reads only files already in the repo."""
import csv
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
INDEX = ROOT / "data" / "reference" / "shelf_index.csv"
ALLOWED = ("gutenberg.org", "ccel.org", "biblehub.com", "en.wikipedia.org", "archive.org", "raw.githubusercontent.com")


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


def test_source_md_lists_every_file():
    source = (SHELF / "SOURCE.md").read_text(encoding="utf-8")
    files = [p.name for p in SHELF.iterdir() if p.is_file() and p.name not in ("request_log.txt", "SOURCE.md")]
    assert files
    missing = [f for f in files if f"`{f}`" not in source]
    assert not missing, missing


def test_source_md_gives_licence_for_every_entry():
    source = (SHELF / "SOURCE.md").read_text(encoding="utf-8")
    entries = [e for e in source.split("\n## ")[1:] if "- File:" in e]
    assert entries
    for e in entries:
        assert "- Licence basis:" in e and "- Source URL:" in e and "- Retrieved:" in e, e[:80]


def test_index_rows_point_to_real_text():
    texts = {}
    n = 0
    for row in csv.DictReader(open(INDEX, encoding="utf-8", newline="")):
        n += 1
        f = SHELF / row["file"]
        assert f.exists(), row["file"]
        if row["file"] not in texts:
            texts[row["file"]] = open(f, encoding="utf-8", errors="replace", newline="").read()
        off = int(row["char_offset"])
        window = collapse(texts[row["file"]][max(0, off - 50): off + 600])
        assert row["excerpt"] and row["excerpt"] in window, (row["file"], off)
        assert row["terms_matched"] and row["locator"] and row["work"]
    assert n > 1000


def test_request_log_hosts_and_count():
    lines = (SHELF / "request_log.txt").read_text(encoding="utf-8").splitlines()
    assert 0 < len(lines) <= 60
    for ln in lines:
        t, status, url, size = ln.split("\t")
        host = urlparse(url).hostname or ""
        assert any(host == a or host.endswith("." + a) for a in ALLOWED), url
        assert "sports-reference" not in url
