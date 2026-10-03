"""Write data/raw/shelf/SOURCE.md and docs/SHELF_REPORT.md from the shelf files, index and quote specs."""
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shelf_quotes as sq  # noqa: E402
from build_shelf_index import ROOT, SHELF, TERMS, WORKS  # noqa: E402

RETRIEVED = "2026-10-03"
PG = "Public domain in the United States (pre-1930 text); distributed under the Project Gutenberg License, header kept intact in the file."
CCEL = "Public domain (pre-1930 text; CCEL header in the file says \"Rights: Public Domain\")."
WIKI = "CC BY-SA 4.0 (Wikipedia text; attribution to the Wikipedia article and its revision is required, and reuse must be share-alike)."

SOURCES = [
    ("edersheim_sketches.txt", "Sketches of Jewish Social Life", "Alfred Edersheim", "1876 (CCEL print basis: Hodder and Stoughton, 1904)",
     "https://www.ccel.org/ccel/e/edersheim/sketches/cache/sketches.txt", CCEL,
     "Not on Project Gutenberg, so taken from CCEL. Footnotes are inline; chapter headings are 'Chapter N'."),
    ("edersheim_life_and_times.txt", "The Life and Times of Jesus the Messiah", "Alfred Edersheim", "1883 (CCEL print basis: Eerdmans, 1953)",
     "https://www.ccel.org/ccel/e/edersheim/lifetimes/cache/lifetimes.txt", CCEL,
     "Two volumes in one file, Books I-V; footnote numbers appear as [1234] in the text and the notes are gathered at the end of each chapter. Hebrew shows as {hebrew}. The text is from an 1883 work; the 1953 print basis is a reprint."),
    ("josephus_antiquities_pg2848.txt", "Antiquities of the Jews", "Flavius Josephus, translated by William Whiston", "Whiston translation 1737",
     "https://www.gutenberg.org/cache/epub/2848/pg2848.txt", PG,
     "Project Gutenberg eBook #2848. Includes Whiston's own footnotes and dissertations, which reflect an 18th-century view and sometimes insult groups of Jews (see SHELF_REPORT). A few characters show as U+FFFD."),
    ("josephus_wars_pg2850.txt", "The Wars of the Jews", "Flavius Josephus, translated by William Whiston", "Whiston translation 1737",
     "https://www.gutenberg.org/cache/epub/2850/pg2850.txt", PG,
     "Project Gutenberg eBook #2850. Whiston's footnotes are gathered at the end of each book."),
    ("smiths_bible_dictionary.txt", "Smith's Bible Dictionary", "William Smith", "1863 (CCEL print basis: 1884 American edition, with editors' additions marked --ED.)",
     "https://www.ccel.org/ccel/s/smith_w/bibledict/cache/bibledict.txt", CCEL,
     "Chosen over Easton's (not available as text on the allowed sites that were tried). Entries are headword lines indented three spaces."),
    ("isbe_1915_vol1.txt", "The International Standard Bible Encyclopaedia, vol. 1 (A to Clemency)", "James Orr, general editor", "1915",
     "https://archive.org/download/bibleencyclopaed01unknuoft/bibleencyclopaed01unknuoft_djvu.txt",
     "Public domain in the United States (published 1915). Archive.org scan from the University of Toronto; plain OCR text only.",
     "OCR text with errors (Greek and Hebrew garbled, hyphenated line-breaks, running heads mixed into the text). Volume numbers here are those of the 1915 five-volume edition; pagination is continuous across volumes."),
    ("isbe_1915_vol2.txt", "The International Standard Bible Encyclopaedia, vol. 2", "James Orr, general editor", "1915",
     "https://archive.org/download/bibleencyclopedi02orruoft/bibleencyclopedi02orruoft_djvu.txt",
     "Public domain in the United States (published 1915). Archive.org scan from the University of Toronto; plain OCR text only.", "OCR text, as vol. 1."),
    ("isbe_1915_vol3.txt", "The International Standard Bible Encyclopaedia, vol. 3", "James Orr, general editor", "1915",
     "https://archive.org/download/bibleencyclopedi03orruoft/bibleencyclopedi03orruoft_djvu.txt",
     "Public domain in the United States (published 1915). Archive.org scan from the University of Toronto; plain OCR text only.", "OCR text, as vol. 1."),
    ("isbe_1915_vol4.txt", "The International Standard Bible Encyclopaedia, vol. 4 (Naarah to Socho)", "James Orr, general editor", "1915",
     "https://archive.org/download/bibleencyclopedi04orruoft/bibleencyclopedi04orruoft_djvu.txt",
     "Public domain in the United States (published 1915). Archive.org scan from the University of Toronto; plain OCR text only.",
     "OCR text, as vol. 1. Contains the SILOAM entry. The Siloam heading itself is lightly garbled."),
    ("isbe_1915_vol5.txt", "The International Standard Bible Encyclopaedia, vol. 5 (Socho to Zuzim, with index)", "James Orr, general editor", "1915",
     "https://archive.org/download/bibleencyclopedi05orruoft/bibleencyclopedi05orruoft_djvu.txt",
     "Public domain in the United States (published 1915). Archive.org scan from the University of Toronto; plain OCR text only.", "OCR text, as vol. 1."),
    ("matthew_henry_vol5_matthew_to_john.txt", "Commentary on the Whole Bible, vol. 5 (Matthew to John)", "Matthew Henry", "1706-1721",
     "https://www.ccel.org/ccel/h/henry/mhc5/cache/mhc5.txt", CCEL.replace("Rights: Public Domain", "Rights: Public domain. May be copied and distributed freely"),
     "Only this volume and vol. 1 were taken, as the brief asked for at least the Gospels and Pentateuch. Verse text is the King James Version, so the old spelling 'Bartimeus' appears."),
    ("matthew_henry_vol1_genesis_to_deuteronomy.txt", "Commentary on the Whole Bible, vol. 1 (Genesis to Deuteronomy)", "Matthew Henry", "1706-1721",
     "https://www.ccel.org/ccel/h/henry/mhc1/cache/mhc1.txt", CCEL.replace("Rights: Public Domain", "Rights: Public domain. May be copied and distributed freely"),
     "CCEL header says this version 'may be from the Revell edition'. Running heads such as 'G E N E S I S' repeat through the text."),
    ("_page_lifetimes.html", "CCEL work page for Life and Times (record of the licence check)", "CCEL", "-",
     "https://www.ccel.org/ccel/edersheim/lifetimes", "Not a work; kept as evidence. The page states no rights line; the rights line is in the downloaded text's header.", ""),
    ("_page_sketches.html", "CCEL work page for Sketches (record of the licence check)", "CCEL", "-",
     "https://www.ccel.org/ccel/edersheim/sketches", "Not a work; as above.", ""),
    ("_page_bibledict.html", "CCEL work page for Smith's Bible Dictionary (record of the licence check)", "CCEL", "-",
     "https://www.ccel.org/ccel/smith_w/bibledict", "Not a work; as above.", ""),
    ("_page_mhc5.html", "CCEL work page for Matthew Henry vol. 5 (record of the licence check)", "CCEL", "-",
     "https://www.ccel.org/ccel/henry/mhc5", "Not a work; as above.", ""),
    ("wikipedia_batch.json", "Wikipedia API response (all eleven articles, with revision ids and timestamps)", "Wikipedia contributors", "retrieved 2026-10-03",
     "https://en.wikipedia.org/w/api.php (action=query, prop=revisions, rvprop=ids|timestamp|content, redirects=1)", WIKI,
     "Raw JSON from the API. Used instead of action=raw because it returns the revision id in the same request. The .wiki.txt files are the wikitext cut out of this JSON."),
]
WIKI_PAGES = [
    ("wikipedia_Pool_of_Siloam.wiki.txt", "Pool of Siloam"), ("wikipedia_Siloam_tunnel.wiki.txt", "Siloam tunnel (also called Hezekiah's Tunnel)"),
    ("wikipedia_Bethsaida.wiki.txt", "Bethsaida"), ("wikipedia_Jericho.wiki.txt", "Jericho"),
    ("wikipedia_Second_Temple.wiki.txt", "Second Temple"), ("wikipedia_Pool_of_Bethesda.wiki.txt", "Pool of Bethesda"),
    ("wikipedia_Healing_the_blind_near_Jericho.wiki.txt", "Healing the blind near Jericho (the redirect target of 'Bartimaeus')"),
    ("wikipedia_Healing_the_man_blind_from_birth.wiki.txt", "Healing the man blind from birth"),
    ("wikipedia_Cultural_depictions_of_blindness.wiki.txt", "Cultural depictions of blindness (the redirect target of 'Blindness in literature')"),
    ("wikipedia_Begging.wiki.txt", "Begging"), ("wikipedia_Mikveh.wiki.txt", "Mikveh"),
]


def size(f):
    return (SHELF / f).stat().st_size


def revinfo(f):
    head = open(SHELF / f, encoding="utf-8").readline()
    m = re.search(r"revid: (\d+); timestamp: (\S+) ", head)
    return m.group(1), m.group(2)


def write_source():
    out = ["# Reference shelf: sources and licences", "",
           f"Everything in this folder was retrieved on {RETRIEVED} with Brian's approval, "
           "using the User-Agent \"NotBySight-research/1.0 (1eyebiney@gmail.com; non-commercial Bible study)\", "
           "at most one request per second. Every request is in `request_log.txt` (time, status, url, bytes). "
           "Only works that are public domain in the United States (published before 1930) or under a free licence were taken.", ""]
    for f, title, author, year, url, lic, odd in SOURCES:
        out += [f"## {title}", "", f"- File: `{f}`", f"- Author: {author}", f"- Year: {year}", f"- Source URL: {url}",
                f"- Retrieved: {RETRIEVED}", f"- Licence basis: {lic}", f"- Size: {size(f):,} bytes"]
        if odd:
            out.append(f"- Odd things: {odd}")
        out.append("")
    for f, title in WIKI_PAGES:
        rid, ts = revinfo(f)
        out += [f"## Wikipedia: {title}", "", f"- File: `{f}`", "- Author: Wikipedia contributors", f"- Year: revision of {ts}",
                f"- Source URL: https://en.wikipedia.org/w/index.php?oldid={rid}",
                f"- Retrieved: {RETRIEVED}", f"- Licence basis: {WIKI}", f"- Revision id: {rid}", f"- Size: {size(f):,} bytes",
                "- Odd things: raw wikitext (templates, [[links]] and <ref> tags left in). First line of the file is a comment giving title, revision id and timestamp.", ""]
    out += ["## Not taken", "",
            "- Easton's Bible Dictionary: the CCEL address tried returned 404 and Gutenberg's search found nothing; Smith's covers the same ground.",
            "- Matthew Henry volumes 2, 3, 4 and 6: not needed for the brief (Gospels and Pentateuch were asked for).",
            "- Edersheim on Project Gutenberg: not there (search found no records); taken from CCEL instead.",
            "- ISBE on CCEL: the address tried returned 404; taken from archive.org scans instead.", ""]
    (SHELF / "SOURCE.md").write_text("\n".join(out), encoding="utf-8")


def counts():
    occ = defaultdict(dict)
    for r in csv.DictReader(open(ROOT / "data" / "reference" / "shelf_counts.csv", encoding="utf-8")):
        occ[r["work"]][r["term"]] = int(r["occurrences"])
    rows = Counter(r["work"] for r in csv.DictReader(open(ROOT / "data" / "reference" / "shelf_index.csv", encoding="utf-8")))
    return occ, rows


def write_report():
    nreq = len((SHELF / "request_log.txt").read_text(encoding="utf-8").splitlines())
    occ, rows = counts()
    terms = list(TERMS) + ["eyes+sight"]
    short = {"blind": "blind", "blindness": "blindness", "born blind": "born blind", "Siloam": "Siloam/Siloah", "Shiloah": "Shiloah",
             "Bethsaida": "Bethsaida", "Bethesda": "Bethesda", "Bartimaeus": "Bartimaeus", "Jericho": "Jericho", "beggar": "beggar",
             "begging": "begging", "alms": "alms", "mikveh": "mikveh", "Gihon": "Gihon", "Hezekiah's tunnel": "Hezekiah's tunnel",
             "eyes+sight": "eyes near sight/blind"}
    L = ["# Reference shelf report", "",
         f"Written {RETRIEVED}. A shelf of public-domain and freely licensed background works, so that each story on the site can gain a "
         "section on the place and the time. The files are in `data/raw/shelf/` (licences and sources in `SOURCE.md` there). "
         "The passage index is `data/reference/shelf_index.csv`. Everything in the digest below is a quotation, with the work and a "
         "locator so a writer can go to the source; nothing is from memory.", "",
         "## What was obtained", "",
         "| Work | Licence basis | File |", "|---|---|---|"]
    for f, title, author, year, url, lic, odd in SOURCES:
        if f.startswith("_page") or f.endswith(".json"):
            continue
        L.append(f"| {title}, {author} ({year}) | {lic.split(';')[0].split('(')[0].strip()}; see SOURCE.md | `{f}` |")
    L.append("| Eleven Wikipedia articles (see SOURCE.md for revision ids) | CC BY-SA 4.0 | `wikipedia_*.wiki.txt` |")
    L += ["", f"Requests made: {nreq} of the 60 allowed (log: `data/raw/shelf/request_log.txt`). "
          "Wikipedia was fetched with one API call (revisions with content and revision ids) instead of eleven action=raw calls.", "",
          "## What was not obtained, and why", "",
          "- **Easton's Bible Dictionary**: not found as text (CCEL address 404, Gutenberg search empty). Smith's was taken instead, as the brief allowed.",
          "- **Matthew Henry, complete**: only volume 1 (Genesis to Deuteronomy) and volume 5 (Matthew to John) were taken. Volumes 2, 3, 4 and 6 were not requested; that was a choice, not a licence problem.",
          "- **Edersheim on Project Gutenberg**: not there; both books came from CCEL, whose files carry \"Rights: Public Domain\".",
          "- **Wikipedia, 'Blindness in literature'** redirects to \"Cultural depictions of blindness\"; **'Bartimaeus'** redirects to \"Healing the blind near Jericho\"; the Siloam tunnel article is the same as 'Hezekiah's Tunnel'. All taken under their target names.",
          "- Nothing was left out for an unclear licence.", "",
          "## Notes on quality", "",
          "- The ISBE (1915) text is raw OCR. Words are sometimes split or garbled and Greek and Hebrew are mostly unreadable. Locators for ISBE are the entry headword as found in the OCR; page numbers could not be read reliably. Every digest line also gives a file offset.",
          "- Edersheim's footnote numbers appear inline as [1234]. Whiston's notes in Josephus are his own 18th-century comments, not Josephus.",
          "- None of the old works use the word mikveh; the Wikipedia Mikveh article is the only source of that word.",
          "- The index holds one row per paragraph (long paragraphs are cut into chunks of about 1,500 characters) that contains a search term. 'eyes near sight/blind' means 'eye' or 'eyes' within 150 characters of 'sight' or 'blind'.", "",
          "## Hits per work and term", "",
          "Raw occurrences of each term (regular expressions, case-insensitive). 'Siloam/Siloah' and 'Shiloah' are separate counts (Shiloah includes Shiloach). 'blind' counts blind, blinded, blinding and so on but not blindness. Index rows per work are in the last column.", "",
          "| Work | " + " | ".join(short[t] for t in terms) + " | index rows |",
          "|---|" + "---|" * (len(terms) + 1)]
    for f, label, kind in WORKS:
        if label in occ:
            L.append(f"| {label} | " + " | ".join(str(occ[label].get(t, 0)) for t in terms) + f" | {rows.get(label, 0)} |")
    L += ["", "## Digest by topic", "",
          "Each line is a short quotation (under 60 words, whitespace tidied, wikitext markup removed, OCR errors left as they are), "
          "the work, and a locator. The file offset is the character position in the raw file (read as UTF-8) where the quotation begins.", ""]
    for title, items in sq.TOPICS:
        L += [f"### {title}", ""]
        for f, anchor, n in items:
            r = sq.quote(f, anchor, n)
            if r is None:
                raise SystemExit(f"missing quote {f} {anchor}")
            q, loc, off = r
            work = sq.KIND[f][0]
            if f.startswith("isbe"):
                work = "ISBE 1915 " + work.split()[-2] + " " + work.split()[-1]
            L.append(f"- \"{q}\" ({work}; {loc}; file `{f}`, offset {off})")
        L.append("")
    L += ["### Things the digest suggests for the stories (pointers only)", "",
          "- John 9: Edersheim's chapter IX, 'The Healing of the Man Born Blind' (offset about 2,635,000 onward in `edersheim_life_and_times.txt`) treats the whole chapter: the begging spot at the Temple entrance, the saliva-and-clay detail, the Pool of Siloam, and the parents' fear of being put out of the synagogue.",
          "- Mark 10 and Matthew 20: ISBE (entry BARTIMAEUS and entry BEGGING) and Matthew Henry vol. 5 on Matthew 20 and Mark 10 give the Jericho setting; Smith's and Edersheim's Sketches give Herod's Jericho; Josephus Wars 4.8.3 gives the spring.",
          "- Mark 8: Matthew Henry vol. 5 on Mark 8 for Bethsaida, Smith's for the two Bethsaidas.", ""]
    L += ["## Statements in the old sources that read as prejudiced", "",
          "These are flagged so they are not repeated without thought. The works are from 1706 to 1915 and reflect their own times. "
          "Several treat 'the Jews', or 'the Pharisees', as one block, set Jewish learning against Christian teaching as 'error' or 'externalism', "
          "or use blindness as an insult. The review below is of the passages found through this index; the books were not read through for prejudice, "
          "so more will exist (Matthew Henry and Whiston's notes especially).", ""]
    for f, anchor, n, why in sq.FLAGS:
        r = sq.quote(f, anchor, n)
        if r is None:
            raise SystemExit(f"missing flag {f} {anchor}")
        q, loc, off = r
        work = sq.KIND[f][0]
        if "footnote" in why:
            loc = "Whiston's footnotes after " + loc.split(",")[0]
        L.append(f"- \"{q}\" ({work}; {loc}; offset {off}). {why}")
    L += ["", "Two more cautions that are not about any single quote:", "",
          "- Edersheim calls the disciples' question in John 9 'thoroughly Jewish' (Life and Times) and 'a strictly Jewish question' (Sketches). "
          "The question is in the Gospel text as the disciples asked it; it should not be attached to Jewish people as a whole.",
          "- Several sources (ISBE, Smith's, Edersheim) describe disabled or poor people in the language of disgust. A writer should keep the facts (how common eye disease was, how begging worked) and drop the tone.", ""]
    (ROOT / "docs" / "SHELF_REPORT.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    write_source()
    write_report()
    print("done")
