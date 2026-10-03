"""Polite cached fetcher for the reference shelf.

usage: python shelf_fetch.py URL OUTNAME
Rules: allowed hosts only, 1 request/second, max 60 requests, log everything.
"""
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests

SHELF = Path(__file__).resolve().parents[1] / "data" / "raw" / "shelf"
LOG = SHELF / "request_log.txt"
UA = "NotBySight-research/1.0 (1eyebiney@gmail.com; non-commercial Bible study)"
ALLOWED = ("gutenberg.org", "ccel.org", "biblehub.com", "en.wikipedia.org",
           "archive.org", "raw.githubusercontent.com")
MAX = 60


def host_ok(url):
    h = urlparse(url).hostname or ""
    return any(h == a or h.endswith("." + a) for a in ALLOWED)


def fetch(url, outname):
    SHELF.mkdir(parents=True, exist_ok=True)
    n = len(LOG.read_text(encoding="utf-8").splitlines()) if LOG.exists() else 0
    if n >= MAX:
        raise SystemExit("request budget used up")
    if not host_ok(url):
        raise SystemExit("host not allowed")
    time.sleep(1.1)
    r = requests.get(url, headers={"User-Agent": UA}, timeout=120)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')}\t{r.status_code}\t{url}\t{len(r.content)}\n")
    if r.status_code == 200 and outname != "-":
        (SHELF / outname).write_bytes(r.content)
    return r


if __name__ == "__main__":
    r = fetch(sys.argv[1], sys.argv[2])
    print(r.status_code, len(r.content), r.headers.get("content-type"))
    if sys.argv[2] == "-" or "--show" in sys.argv:
        print(r.text[:3000])
