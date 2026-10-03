"""Fetch Wikipedia wikitext (with revision ids) for the shelf, via the API in batches."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from shelf_fetch import SHELF, fetch  # noqa: E402

from urllib.parse import quote

TITLES = ["Pool of Siloam", "Siloam tunnel", "Bethsaida", "Jericho", "Second Temple",
          "Pool of Bethesda", "Bartimaeus", "Healing the man blind from birth",
          "Blindness in literature", "Begging", "Mikveh"]


def main():
    url = ("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=ids%7Ctimestamp%7Ccontent"
           "&rvslots=main&redirects=1&format=json&formatversion=2&titles=" + quote("|".join(TITLES), safe=""))
    r = fetch(url, "wikipedia_batch.json")
    print(r.status_code, len(r.content))
    data = json.loads(r.text)
    for p in data["query"]["pages"]:
        if p.get("missing"):
            print("MISSING", p["title"])
            continue
        rev = p["revisions"][0]
        name = "wikipedia_" + p["title"].replace(" ", "_").replace("'", "") + ".wiki.txt"
        head = f"<!-- title: {p['title']}; revid: {rev['revid']}; timestamp: {rev['timestamp']} -->\n"
        (SHELF / name).write_text(head + rev["slots"]["main"]["content"], encoding="utf-8")
        print(name, rev["revid"])
    print(data["query"].get("redirects"))


main()
