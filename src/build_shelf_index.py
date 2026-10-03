"""Build data/reference/shelf_index.csv: every paragraph in the shelf works that mentions a search term.

Plain regexes, no NLP. Offsets are character offsets into the raw file read as
UTF-8 (errors='replace', newline='' so line endings are untouched).
"""
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHELF = ROOT / "data" / "raw" / "shelf"
OUT = ROOT / "data" / "reference" / "shelf_index.csv"

TERMS = {
    "blind": re.compile(r"\bblind(?!ness)\w*", re.I),
    "blindness": re.compile(r"\bblindness", re.I),
    "born blind": re.compile(r"\bborn\s+blind", re.I),
    "Siloam": re.compile(r"\bsiloa[hm]\b", re.I),
    "Shiloah": re.compile(r"\bshi?loa?c?h\b", re.I),
    "Bethsaida": re.compile(r"\bbeths?aida", re.I),
    "Bethesda": re.compile(r"\bbethesda", re.I),
    "Bartimaeus": re.compile(r"\bbar-?tim(?:ae?|e)us", re.I),
    "Jericho": re.compile(r"\bjericho", re.I),
    "beggar": re.compile(r"\bbeggar\w*", re.I),
    "begging": re.compile(r"\bbegging", re.I),
    "alms": re.compile(r"\balms", re.I),
    "mikveh": re.compile(r"\bmikv(?:eh|ah|aot|oth|ehs)\b", re.I),
    "Gihon": re.compile(r"\bgihon", re.I),
    "Hezekiah's tunnel": re.compile(r"hezekiah[’']s\s+(?:tunnel|conduit)|tunnel\s+of\s+hezekiah", re.I),
}
EYES = re.compile(r"\beyes?\b", re.I)
SIGHT = re.compile(r"\bsight\b|\bblind", re.I)

WORKS = [
    # (file, label, kind)
    ("edersheim_sketches.txt", "Edersheim, Sketches of Jewish Social Life", "sketches"),
    ("edersheim_life_and_times.txt", "Edersheim, Life and Times of Jesus the Messiah", "lifetimes"),
    ("josephus_antiquities_pg2848.txt", "Josephus (Whiston), Antiquities of the Jews", "josephus"),
    ("josephus_wars_pg2850.txt", "Josephus (Whiston), Wars of the Jews", "josephus"),
    ("smiths_bible_dictionary.txt", "Smith's Bible Dictionary", "smith"),
    ("isbe_1915_vol1.txt", "ISBE 1915 vol 1", "isbe"),
    ("isbe_1915_vol2.txt", "ISBE 1915 vol 2", "isbe"),
    ("isbe_1915_vol3.txt", "ISBE 1915 vol 3", "isbe"),
    ("isbe_1915_vol4.txt", "ISBE 1915 vol 4", "isbe"),
    ("isbe_1915_vol5.txt", "ISBE 1915 vol 5", "isbe"),
    ("matthew_henry_vol1_genesis_to_deuteronomy.txt", "Matthew Henry vol 1 (Genesis-Deuteronomy)", "henry"),
    ("matthew_henry_vol5_matthew_to_john.txt", "Matthew Henry vol 5 (Matthew-John)", "henry"),
    ("wikipedia_Pool_of_Siloam.wiki.txt", "Wikipedia: Pool of Siloam", "wiki"),
    ("wikipedia_Siloam_tunnel.wiki.txt", "Wikipedia: Siloam tunnel", "wiki"),
    ("wikipedia_Bethsaida.wiki.txt", "Wikipedia: Bethsaida", "wiki"),
    ("wikipedia_Jericho.wiki.txt", "Wikipedia: Jericho", "wiki"),
    ("wikipedia_Second_Temple.wiki.txt", "Wikipedia: Second Temple", "wiki"),
    ("wikipedia_Pool_of_Bethesda.wiki.txt", "Wikipedia: Pool of Bethesda", "wiki"),
    ("wikipedia_Healing_the_blind_near_Jericho.wiki.txt", "Wikipedia: Healing the blind near Jericho (Bartimaeus)", "wiki"),
    ("wikipedia_Healing_the_man_blind_from_birth.wiki.txt", "Wikipedia: Healing the man blind from birth", "wiki"),
    ("wikipedia_Cultural_depictions_of_blindness.wiki.txt", "Wikipedia: Cultural depictions of blindness", "wiki"),
    ("wikipedia_Begging.wiki.txt", "Wikipedia: Begging", "wiki"),
    ("wikipedia_Mikveh.wiki.txt", "Wikipedia: Mikveh", "wiki"),
]

LINE_RES = {
    "josephus": [("book", re.compile(r"^BOOK ([IVXL]+)\b", re.I)),
                 ("chapter", re.compile(r"^CHAPTER (\d+)", re.I))],
    "lifetimes": [("book", re.compile(r"^\s*BOOK ([IVX]+)\s*$")),
                  ("chapter", re.compile(r"^\s*CHAPTER ([IVXL]+)\.?\s*$"))],
    "sketches": [("chapter", re.compile(r"^Chapter (\d+)\s*$"))],
    "henry": [("book", re.compile(r"^((?:[A-Z] )+[A-Z])\.?\s*$")),
              ("chapter", re.compile(r"^\s*CHAP\. ([IVXLC]+)\.?\s*$"))],
    "wiki": [("section", re.compile(r"^=+\s*(.*?)\s*=+\s*$"))],
}
ISBE_PAGE = re.compile(r"(\d{3,4})\s+(?:THE\s+)?(?:INTERNATIONAL|NATIONAL)\s+STANDARD|ENCYCL\S*\s+(?:.{0,30}?\s)?(\d{3,4})\s*$")
# ISBE (OCR text): an entry starts 'HEADWORD, pronunciation (' or 'HEAD, HEAD2 :'; page numbers sit in running heads.
ISBE_ENTRY = re.compile(r"([A-Z][A-Z'\-]{2,}(?:, [A-Z][A-Z'\-]{2,})*)(?:,\s+[a-z][^\s(]{2,}\S*\s*\(|\s*:\s)")
SECT_NUM = re.compile(r"^\s*(\d+)\.\s")


def split_paragraphs(text):
    """Yield (start, end) for blank-line separated paragraphs; long ones are cut at line breaks."""
    for m in re.finditer(r"(?:[^\n]+\n?)+", text):
        s, e = m.start(), m.end()
        if e - s <= 2500:
            yield s, e
            continue
        cur = s
        for lm in re.finditer(r"[^\n]*\n?", text[s:e]):
            ls = s + lm.start()
            le = s + lm.end()
            if le - cur > 1500 and ls > cur:
                yield cur, ls
                cur = ls
        if cur < e:
            yield cur, e


def locator_tracker(kind):
    state = {}
    def feed(line):
        if kind in LINE_RES:
            for key, rx in LINE_RES[kind]:
                m = rx.match(line)
                if m:
                    state[key] = m.group(1)
                    if key == "book":
                        state.pop("chapter", None)
                    if kind == "wiki":
                        state[key] = m.group(1)
        elif kind == "smith":
            if re.match(r"^   \S", line) and not line.startswith("    "):
                state["entry"] = line.strip()
        elif kind == "isbe":
            if "STANDARD" in line and "BIBLE" in line and "ENCYCL" in line:
                pm = ISBE_PAGE.search(line)
                if pm:
                    state["page"] = pm.group(1) or pm.group(2)
            for em in ISBE_ENTRY.finditer(line):
                state["entry"] = em.group(1)
    def render(vol=""):
        if kind == "josephus":
            return ", ".join(f"{k} {state[k]}" for k in ("book", "chapter") if k in state) or "front matter"
        if kind == "lifetimes":
            return ", ".join(f"{k} {state[k]}" for k in ("book", "chapter") if k in state) or "front matter"
        if kind == "sketches":
            return f"Chapter {state['chapter']}" if "chapter" in state else "front matter"
        if kind == "henry":
            b = state.get("book", "").replace(" ", "")
            return (f"{b.title()} " if b else "") + (f"chap. {state['chapter']}" if "chapter" in state else "intro")
        if kind == "wiki":
            return "section: " + state.get("section", "lead")
        if kind == "smith":
            return "entry: " + state.get("entry", "front matter")
        if kind == "isbe":
            page = f", p. {state['page']}" if "page" in state else ""
            return f"vol {vol}{page}, entry: " + state.get("entry", "front matter")
    return feed, render


def main():
    rows = []
    occ = defaultdict(Counter)
    para_hits = defaultdict(Counter)
    for fname, label, kind in WORKS:
        path = SHELF / fname
        if not path.exists():
            continue
        text = open(path, encoding="utf-8", errors="replace", newline="").read()
        for term, rx in TERMS.items():
            occ[label][term] = len(rx.findall(text))
        # line starts for locator tracking
        feed, render = locator_tracker(kind)
        vol = label.split()[-1] if kind == "isbe" else ""
        pos = 0
        n_eyes = 0
        for s, e in split_paragraphs(text):
            # feed every line between pos and e to the tracker (headings come before paragraphs)
            for line in text[pos:e].splitlines():
                feed(line.rstrip("\r"))
            pos = e
            para = text[s:e]
            matched = [t for t, rx in TERMS.items() if rx.search(para)]
            em = EYES.search(para)
            if em:
                w = para[max(0, em.start() - 150): em.end() + 150]
                if SIGHT.search(w) and "eyes+sight" not in matched:
                    matched.append("eyes+sight")
                    n_eyes += 1
            if not matched:
                continue
            for t in matched:
                para_hits[label][t] += 1
            loc = render(vol)
            sm = SECT_NUM.match(para) if kind == "josephus" else None
            if sm:
                loc += f", section {sm.group(1)}"
            rows.append({"work": label, "locator": loc, "terms_matched": "; ".join(matched),
                         "excerpt": re.sub(r"\s+", " ", text[s:s + 400]).strip(), "char_offset": s,
                         "file": fname})
        occ[label]["eyes+sight"] = n_eyes
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["work", "locator", "terms_matched", "excerpt", "char_offset", "file"])
        w.writeheader()
        w.writerows(rows)
    # counts table for the report
    cnt = ROOT / "data" / "reference" / "shelf_counts.csv"
    with open(cnt, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["work", "term", "occurrences", "paragraphs"])
        for label in occ:
            for t in list(TERMS) + ["eyes+sight"]:
                w.writerow([label, t, occ[label][t], para_hits[label][t]])
    print(len(rows), "rows")


if __name__ == "__main__":
    main()
