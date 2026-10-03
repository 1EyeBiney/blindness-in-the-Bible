"""Law-questions Wikipedia batches (two API calls)."""
import json, sys
from pathlib import Path
from urllib.parse import quote
sys.path.insert(0, str(Path(__file__).resolve().parent))
from shelf_fetch import SHELF, fetch

BATCHES = [
    ("wikipedia_batch6.json", ["Hittite laws", "Code of Ur-Nammu", "Laws of Eshnunna", "Code of Lipit-Ishtar",
        "Middle Assyrian Laws", "Instruction of Amenemope", "Ebers Papyrus", "Harper's Songs", "Dating the Exodus",
        "The Exodus", "Documentary hypothesis", "Mosaic authorship"]),
    ("wikipedia_batch7.json", ["Priestly divisions", "Showbread", "Altar of Incense", "Uzzah", "Nadab and Abihu",
        "Laver", "Leviticus 21", "Moses", "Hammurabi"]),
]
for fname, titles in BATCHES:
    url = ("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=ids%7Ctimestamp%7Ccontent"
           "&rvslots=main&redirects=1&format=json&formatversion=2&titles=" + quote("|".join(titles), safe=""))
    r = fetch(url, fname)
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
        print(name, rev["revid"], rev["timestamp"], len(txt.encode("utf-8")))
    print(data["query"].get("redirects"))
