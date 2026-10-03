"""Third follow-up Wikipedia batch (one API call)."""
import json, sys
from pathlib import Path
from urllib.parse import quote
sys.path.insert(0, str(Path(__file__).resolve().parent))
from shelf_fetch import SHELF, fetch

TITLES = ["Stepped street (Jerusalem)", "Hulda Gates", "Antonia Fortress", "Book of Tobit", "Sheep Gate"]

url = ("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=ids%7Ctimestamp%7Ccontent"
       "&rvslots=main&redirects=1&format=json&formatversion=2&titles=" + quote("|".join(TITLES), safe=""))
r = fetch(url, "wikipedia_batch5.json")
print(r.status_code, len(r.content))
data = json.loads(r.text)
for p in data["query"]["pages"]:
    if p.get("missing"):
        print("MISSING", p["title"]); continue
    rev = p["revisions"][0]
    name = "wikipedia_" + p["title"].replace(" ", "_").replace("'", "").replace("(", "").replace(")", "") + ".wiki.txt"
    head = f"<!-- title: {p['title']}; revid: {rev['revid']}; timestamp: {rev['timestamp']} -->\n"
    txt = (head + rev["slots"]["main"]["content"]).replace("\r\n", "\n")
    (SHELF / name).write_bytes(txt.encode("utf-8"))
    print(name, rev["revid"], rev["timestamp"], len(txt))
print(data["query"].get("redirects"))
