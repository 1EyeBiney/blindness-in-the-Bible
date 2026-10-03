"""Write docs/LAW_QUESTIONS_DIGEST.md from data/reference/law_questions_candidates.json (counts) and the prose below."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "reference" / "law_questions_candidates.json").read_text(encoding="utf-8"))
n = {k: len(v) for k, v in data.items()}
total = sum(n.values())
per_key = ", ".join(f"`{k}` {v}" for k, v in n.items())

DOC = f"""# Law questions: digest of the candidates

Written 3 October 2026. This goes with `data/reference/law_questions_candidates.json`, which holds candidate items for Brian's two questions from reading the law pages: (A) whether Hammurabi's Code and the Bible compare on the blind, and when each was written; (B) what priests and Levites did, whether a blind priest would touch what he should not, and whether fitting him in would have burdened the other Levites. It is built by `src/build_law_questions_candidates.py`, which refuses to write a quote it cannot find in the shelf, and is checked by `tests/test_law_questions_candidates.py`.

Every item has a short paragraph, a citation as a reader would see it, one or more verbatim quotes with the file and character offset (line endings as LF), a confidence of `high` or `medium`, and a `caution`. The test checks that each quote is really in its file at its offset. It does not check that the paragraph is a fair reading of the quote, and nothing here has been seen by Brian or a second reader. Read the `caution` lines before using an item. Nothing in the JSON was filled from memory. Where I know something from general knowledge that the shelf does not contain, it is said in the item as unverified, or kept for this digest and marked.

Counts: {total} items across {len(n)} keys. Per key: {per_key}.

## What was added to the shelf for this pass

Five requests (the budget was 40; the log now has 47 lines in all). Everything is in `data/raw/shelf/SOURCE.md` with licence basis.

- Wikipedia (CC BY-SA 4.0, revisions recorded), two API calls: Hittite laws, Code of Ur-Nammu, Laws of Eshnunna, Code of Lipit-Ishtar, Assyrian law (asked for as 'Middle Assyrian Laws'), Instruction of Amenemope, Ebers Papyrus, Harper's Songs, The Exodus (asked for as 'Dating the Exodus'), Documentary hypothesis, Mosaic authorship, Priestly divisions, Showbread, Uzzah, Nadab and Abihu, Emor (asked for as 'Leviticus 21'; it carries the Mishnah and Talmud rules on blemished priests), Hammurabi, Moses, Laver. Not found: 'Altar of Incense' (no such title). 'Laver' is only a disambiguation page and is not used. 'Moses' was fetched for dating context and is not quoted.
- E. A. Wallis Budge, *The Teaching of Amen-em-apt, Son of Kanekht* (London, 1924), the OCR text from archive.org (public domain in the US, published before 1930). It contains the line about the blind man.
- Hittite laws: no public-domain translation was found. The archive.org search returned only Hoffner (1997) and Neufeld (1951); neither was taken. So the Hittite sections on blinding, which I recall from general knowledge, are not on the shelf and could not be checked.
- Not fetched: Edersheim, *The Temple* (public domain, on archive.org; it would have been the next request), Josephus *Against Apion*, and Griffith's 1926 article on Amenemope. Edersheim's *Life and Times of Jesus* (already on the shelf) turned out to carry a useful account of the daily incense service and a footnote on the number of priests, and Josephus *Antiquities* III and VII covered the priestly duties and the twenty-four courses.
- Mined from what was already on the shelf: Smith's and Easton's entries on Priest, Levites, Candlestick, Incense, Shewbread and Laver; the 1915 encyclopaedia on Priests and Levites, Blemish and Hammurabi; Matthew Henry on Leviticus 1, 6, 9, 10, 13, 19, 21, 24, Numbers 4, 6, 18, Deuteronomy 27, 2 Samuel 6, 1 Chronicles 24 and Luke 1; Levy (1872) for the Egyptian painting.

## Brian's question A: is the Bible the first recorded anything about the blind, and how do Hammurabi and Moses compare?

Brian's observation is right as far as the shelf goes: the English Code of Hammurabi on the shelf (Johns, 1903) never uses the word 'blind' (a search of the file finds none). But the Code does have eyes in it, and that changes the question.

### The dates (`dating`, {n['dating']} items)

- Hammurabi: about 1792 to 1750 BC (Wikipedia, 2 October 2026; `dating[0]`). The 1915 encyclopaedia dates him about 2100 BC, which is three centuries earlier than today's figure and a reminder that older books on the shelf use older chronologies (`dating[1]`).
- Moses and the Exodus: the shelf holds both camps. The older books give the early date: Easton (1897) 'about B.C. 1490, and four hundred and eighty years (1 Kings 6:1) before the building of Solomon's temple', and Henry heads the laws of Leviticus 24 with 'b. c. 1490' (`dating[2]`). The 1446 BC figure usually given for the early date today is not on the shelf; I know it only from general knowledge (unverified). The late date appears in Easton's article on Egypt (Rameses II as the Pharaoh of the Oppression, the Exodus under a successor) and in Wikipedia's 'The Exodus', where scholars who accept a historical core place Exodus-group activity in the thirteenth century BCE, with some at the twelfth (`dating[3]`). I take about 1250 BC from your brief; Wikipedia gives only the century.
- Writing of Deuteronomy and Leviticus: a third question, separate from when Moses lived. The tradition is that Moses wrote the law (Deuteronomy 31:9 says so of 'this law'). Wikipedia says scholars generally agree Deuteronomy was composed in Josiah's reform in the late seventh century BCE, and the documentary hypothesis dates the Priestly source (most of Leviticus) to the sixth to fifth century BCE, though it also says the classical consensus 'has now faltered' (`dating[4]`, `dating[5]`). The 1915 encyclopaedia lays out the old belief, the Wellhausen view and its author's own view, which accepts Mosaic authenticity (`dating[6]`).
- Arithmetic from those figures (mine, not a source's): Hammurabi's reign ended about 300 years before an Exodus at 1446 (about 260 on the shelf's own 1490), and about 500 years before a late-date Exodus. If Leviticus was written down in the sixth or fifth century BCE, the Code is more than 1,100 years older than the written book. On any of these figures Hammurabi comes first.
- Other texts on the shelf, by date (`dating[7]`): Ur-Nammu about 2100 BC; Eshnunna about 1930 BC; Hittite laws 1650 to 1500 BCE; Ebers Papyrus about 1550 BCE; Middle Assyrian laws developed 1450 to 1250 BCE; Amenemope most likely 1300 to 1075 BCE (Budge in 1924 put its author under the Eighteenth Dynasty, which is earlier).

### Which earlier texts price or punish blinding (`earlier-texts-blinding`, {n['earlier-texts-blinding']} items)

- Ur-Nammu (about 2100 BC), the oldest law code known: section 15, 'If a man knocks out the eye of another man, he shall weigh out half a mina of silver' (`earlier-texts-blinding[3]`).
- Hammurabi, Johns's numbering: section 196 (a gentleman's eye for a gentleman's eye), 198 (a poor man's eye, one mina of silver), 199 (a gentleman's servant's eye, half his price), 193 (the eye torn out of an adopted son who goes back to his birth father's house), and 215 to 220 (a doctor who opens an eye abscess is paid ten shekels if the eye is saved, loses his hands if a gentleman loses the eye, pays money for a slave's eye) (`earlier-texts-blinding[0]` to `[2]`).
- The Middle Assyrian laws (1450 to 1250 BCE, a span that covers both Exodus dates) include 'they shall destroy both of her eyes' as a penalty, per Wikipedia's incomplete excerpt (`earlier-texts-blinding[4]`).
- Laws of Eshnunna (about 1930 BC) price injuries in silver (Wikipedia's example is a nose); the Wikipedia summaries of Eshnunna and Lipit-Ishtar mention no eye or blind section, which is weak evidence of absence (`earlier-texts-blinding[6]`).
- Hittite laws (1650 to 1500 BCE): the shelf shows only that they price injuries. I recall that they have sections on blinding a free man or a slave. That is general knowledge, unverified, and nothing on the shelf can confirm it (`earlier-texts-blinding[5]`).

So the answer to 'which earlier texts price or punish blinding' is: all the Mesopotamian codes the shelf can show, from about 2100 BC on. They treat the loss of an eye as an injury with a tariff or a mirrored penalty, depending on rank. None of them, on what the shelf holds, says anything about the person who has lost sight, afterwards.

### Which earlier texts protect or show regard for blind persons (`earlier-texts-regard`, {n['earlier-texts-regard']} items)

- Egypt, the Instruction of Amenemope, line 478 in Budge's 1924 numbering: 'Make not a laughing-stock of the blind man', beside 'Vex (or, browbeat) not the dwarf' and a line for the afflicted or lame (`earlier-texts-regard[0]`, `[1]`). This is the one text on the shelf that singles out the blind man for protection and may be as early as, or earlier than, Leviticus 19:14. Wikipedia dates the Instruction most likely to 1300 to 1075 BCE; on a late Exodus date that is roughly Moses's time, on an early date it is one to three centuries later, and on the critical date for the writing of Leviticus it is centuries earlier. Budge, in 1924, put it under the Eighteenth Dynasty (earlier). It is advice to a reader, not a law with a penalty.
- Egyptian images of blind harpists: Middle Kingdom tomb walls (about 2040 to 1640 BCE) and an Eighteenth Dynasty mural of the fifteenth century BC; Levy (1872, quoting Kitto) describes a painting of a blind harper with seven blind singers, 'evidently professional musicians' (`earlier-texts-regard[2]`, `[3]`). These show a role, not a regard.
- Wider care for the weak: Ur-Nammu's orphan, widow and poor man (`[4]`), Hammurabi's prologue 'to prevent the strong from oppressing the weak' (`[5]`), Amenemope's defence of the weaker classes (`[6]`). None names the blind. The Ebers Papyrus has eye remedies (`[7]`), which shows concern with the eye, not with the person.
- The Hebrew texts for comparison: Leviticus 19:14 and Deuteronomy 27:18, laws with a fear-of-God sanction and a curse (`[8]`).

### A frank answer to question A

- Is the Bible the first recorded anything that addresses the blind? On the shelf, no for 'anything': the Mesopotamian codes address blinding, centuries earlier. And no for 'protects': Amenemope's line on the blind man is as old as or older than Leviticus 19:14, depending on which dates you take.
- Is it the first *law* that commands protection of the blind? That is the strongest claim the shelf supports: among the legal texts on the shelf (Ur-Nammu, Eshnunna, Lipit-Ishtar, Hammurabi, the Assyrian excerpts, the Hittite summary), only Leviticus 19:14 and Deuteronomy 27:18 name the blind for protection. But the shelf lacks the Hittite laws in translation, and Wikipedia's summaries of the other codes are not the codes. It is a claim about what the shelf holds, not about the ancient world.
- How the Bible's laws differ in kind: the earlier laws deal with the blinded person as the object of a tariff paid by the one who caused the loss. Leviticus 19:14 and Deuteronomy 27:18 forbid wronging a blind person who is still there, in the road, trusting someone's advice. The shelf cannot prove that no earlier law did this (Amenemope is close, though it is advice); it does show that Hammurabi's Code did not.
- Whether Moses or Hammurabi came first is not in doubt on any of the figures on the shelf. Whether the Bible's text or Amenemope's came first is open.

## Brian's question B: priests, touch and the other Levites

### What priests and Levites did (`priest-duties`, {n['priest-duties']} items)

Sorted by what the work demands, which is an analysis of the sources, not a finding in them:

- Touch and heat: tending the altar fire (it was to burn day and night), clearing the ashes each morning in a linen garment, sprinkling the blood, putting fire and wood on the altar and laying the parts, flaying and cutting up the offering, washing the inwards and legs (`priest-duties[0]` to `[2]`).
- Touch and handling at the lampstand: trimming the seven lamps with golden snuffers and filling them with oil, morning and evening, in a tent with no windows (`priest-duties[3]`).
- Sight appears in the sources for the incense (a signal, waiting until the incense was seen kindling, in the light of the lampstand) and for skin inspection (the priest 'shall look on', 'in sight be not deeper than the skin') (`priest-duties[4]`, `[7]`).
- Handling food and bread: renewing the showbread every Sabbath, by a team in a set order (`priest-duties[5]`).
- Speech: blessing the people, teaching the statutes, acting as a court of appeal (`priest-duties[6]`).
- The Levites: carrying the covered holy things, moving the tent, and later gatekeeping, singing, vergers' work and assisting at offerings (`priest-duties[8]`).

### Would a blind priest accidentally touch things he should not? (`touching-holy-things`, {n['touching-holy-things']} items; `blemished-priest-provision`, {n['blemished-priest-provision']} items)

What the sources say, plainly:

- The touching rules in the sources are rules for the Levites, mostly the Kohathites who carried the sanctuary: they 'shall not touch any holy thing, lest they die' and 'shall not go in to see when the holy things are covered' (Numbers 4:15, 4:20). The priests, Aaron's sons, covered the things first. Henry's comment: 'Even those that bore the vessels of the Lord saw not what they bore' (`touching-holy-things[0]` to `[2]`). The system was built so that the people who carried the holiest things neither saw nor touched them.
- Uzzah (2 Samuel 6:6-7) is the one case of a fatal touch. On Henry's reading he was a Levite, he grasped the ark deliberately to stop it falling, and he meant well; it was still fatal (`touching-holy-things[3]`). Nadab and Abihu (Leviticus 10) died for offering unauthorised fire, which is about the fire, not about touching (`[4]`).
- What Leviticus 21:16-23 lets the blemished priest do, and not do: he shall not 'approach to offer the bread of his God', nor 'go in unto the vail, nor come nigh unto the altar'; but he may eat 'both of the most holy, and of the holy'. So he stays a priest, keeps his share, and is kept away from the altar and the veil, the places where the severest touching and fire rules applied (`blemished-priest-provision[0]`, `[1]`, `[2]`). The reason the verse gives is 'that he profane not my sanctuaries'. Josephus, the 1915 encyclopaedia and Henry restate the rule (`[2]`, `[3]`, `[7]`).
- The skin-disease helper rule, which you asked about, is as Henry reports it, from an unnamed Jewish source: any priest 'though disabled by a blemish to attend the sanctuary' may judge leprosy 'provided the blemish were not in his eye', and he may 'take a common person to assist him in the search, but the priest only must pronounce the judgment' (`blemished-priest-provision[4]`). By the rule's wording, then, a priest with a blemish in the eye could not judge skin disease; the helper was for the searching, and the priest had to see. The shelf has no source for the rule's origin or date.

What is inference, mine and not sourced: Leviticus 21:23 keeps a blind priest away from the altar, the veil and the Holy Place, the same places where the touching, fire and incense dangers sit; so his own habit of touching to find out what things are would, under the rule, not be exercised on the holy things. That is an observation about where the boundary falls. It is not a claim that the rule was made for that reason, and it does not say what a blind priest did at the table, in the court, in teaching, or in daily life. No source on the shelf says a blind priest existed under Moses, or how any blemished priest managed. The sources are silent on accidental touching by someone who cannot see, so the honest answer to the question is: the shelf does not say.

### Would fitting in a blind priest have burdened the other Levites? (`priestly-numbers`, {n['priestly-numbers']} items)

- Who did the work: priests (Aaron's family) served in twenty-four courses, one week at a time, set by lot in David's time (1 Chronicles 24; Easton, Smith's, Josephus, Henry; `priestly-numbers[0]` to `[2]`). The lot fixed the order, not who was in or out (Henry; `[1]`). Zechariah (Luke 1:5-9) was of the eighth course, and Edersheim says that in his long priesthood he had never before been chosen to incense, which was assigned by lot (`[3]`). Edersheim reckons about fifty priests on duty each weekday and the whole course on the Sabbath, a number he calls more than was needed; Smith's cites Jewish writers for 24,000 at Jerusalem and 12,000 at Jericho; they do not agree (`[4]`, `[5]`). Wikipedia notes that many scholars date the course system after the exile (`[6]`).
- The Levites were not the priests' substitutes. They carried, guarded, sang and assisted (`priest-duties[8]`), and the Mishnah, as reported by Wikipedia's 'Emor', says the disabilities that bar a priest do not bar a Levite, who is barred only by age (and only for carrying) (`blemished-priest-provision[5]`). On that reading a Levite's blindness was not a Levitical bar at all, and a blind priest is not a burden transferred to the Levites.
- The provision itself carries the answer the sources give: Leviticus 21 does not ask the blemished priest to 'fit in' to the altar service; it removes that duty and keeps his place at the table. Henry: 'though they might not work, they must not starve' (`blemished-priest-provision[1]`). The cost to others was his portion of the offerings, which the priests and Levites already shared by the tithes (Smith's lists the support; the shelf does not say how many blemished priests there were).
- No source on the shelf says a blind priest burdened the Levites, or the opposite. That the work was shared by rotation among thousands, with numbers in the tens of thousands on the Jewish writers' count, is the only support for the suggestion that one priest's absence from the altar would have been absorbed. It is a reading of the numbers, with large uncertainties (the figures belong to the Second Temple, not the wilderness; the system itself is dated late by many scholars).

## What remains unknown

- Whether anyone blind was a priest, and what he did. The shelf has the rule, not a case, and no instance of a named blemished priest.
- The text of the Hittite laws on blinding, and whether the Middle Assyrian laws have other eye sections. These need a translation (Hoffner 1997; Roth 1995 and 1997) that is not on the shelf and is under copyright.
- The date of the Instruction of Amenemope against the date of Leviticus 19:14. They depend on the Exodus date and on the date of the Priestly source, both disputed.
- Whether the Egyptian line was law or advice in practice, and how blind people in Egypt and Babylon were actually treated. The pictures show roles; no text on the shelf shows what regard they had.
- The origin and date of the 'skin-disease helper' rule Henry reports. The Mishnah and Talmud (Negaim, Bekhorot, Tamid, Yoma) are not on the shelf.
- The actual number of priests and Levites in any period. The shelf has three sets of figures that do not agree, all late.
- Whether the blessing, teaching and judging duties were open to a priest who could not see. The Emor article reports Talmudic rules on one-eyed priests and the blessing, which are rulings of later centuries.
- How a blind person, then or now, would manage the sanctuary tasks without touching what should not be touched. The sources do not speak to it. Brian's own account of working out an unfamiliar room by touch is the relevant evidence, and it is his to give.

## Language flagged, not reproduced

- Matthew Henry on Leviticus 21 gives an appearance-based reason for the blemish rule (the altar's credit needing attractive ministers) and uses dated words for bodily differences. He also uses 'blind' and 'lame' as figures for sinful ministers, and calls the moral vice of Hophni and Phinehas a worse deformity. Quoted only for the clauses on feeding and on not working, and for his gospel remark (`blemished-priest-provision[1]`, `[7]`).
- Henry on Leviticus 13 says lepers were seen as marked by God's justice. Not quoted. It is the same passage in which the helper rule is reported, so the rule is quoted without it.
- Smith's on the priests of the late Temple uses harsh words for their condition and end. Not quoted.
- Edersheim's passages on the Pharisee, Essene and publican use disdainful words; only the neutral account of the incense is used.
- Levy (1872) uses a loaded adverb for the number of blind people in Egypt. Not quoted. He also has long passages on blinding as punishment with graphic detail; none quoted.
- The Hammurabi, Ur-Nammu and Assyrian items include graphic penalties (tearing out an eye, destroying both eyes, cutting off hands). They are quoted only to show what the text prices or punishes, in as few words as the question needs.
- The Wikipedia 'Emor' article reports rabbinic rules about the hands of a priest and about a man blind in one eye not lifting his hands for the blessing so that the congregation not look at him. These are reported with their stated reason because they bear on the question; the digest does not endorse them.
- Wikipedia's article on Moses carries a view that the historical Moses is 'legend'; it is not used.

## Modern works Brian could consult

From my general knowledge, not from the shelf and not checked against any library catalogue: titles, authors and years may be slightly wrong, and I have not read most of them. Treat every line as unverified until Brian or a librarian has confirmed it.

Near Eastern law and the blind:
- Martha T. Roth, *Law Collections from Mesopotamia and Asia Minor* (1995, 2nd ed. 1997): translations of Ur-Nammu, Lipit-Ishtar, Eshnunna, Hammurabi, the Middle Assyrian laws and the Hittite laws. The Wikipedia articles on Ur-Nammu and others cite it.
- Harry A. Hoffner Jr., *The Laws of the Hittites: A Critical Edition* (1997). Archive.org lists it, but it is under copyright and was not taken.
- Miriam Lichtheim, *Ancient Egyptian Literature*, vol. 2 (1976): a translation of Amenemope and the Harper's Songs. Wikipedia cites Lichtheim 1976.
- Margret A. Winzer, *The History of Special Education* (1993): Wikipedia cites it for ancient Egyptian social care of the blind.
- Saul M. Olyan, *Disability in the Hebrew Bible* (2008): on the blemish rules and the status of blind people.
- Candida R. Moss and Jeremy Schipper (eds.), *Disability Studies and Biblical Literature* (2011).
- Hector Avalos, Sarah Melcher and Jeremy Schipper (eds.), *This Abled Body* (2007).

Dating:
- Kenneth A. Kitchen, *On the Reliability of the Old Testament* (2003): an argument for a thirteenth-century Exodus and for the antiquity of the legal texts.
- James K. Hoffmeier, *Israel in Egypt* (1997) and *Ancient Israel in Sinai* (2005): for the Exodus date.
- Baruch A. Levine, *Leviticus* (JPS Torah Commentary, 1989) and Jacob Milgrom, *Leviticus 1-16* (1991), *Leviticus 17-22* (2000), *Leviticus 23-27* (2001): the date and the blemish rule.

Priests, Levites and the Temple:
- Alfred Edersheim, *The Temple: Its Ministry and Services* (1874): public domain, on archive.org, and the obvious next shelf item for the Temple routine.
- Menahem Haran, *Temples and Temple-Service in Ancient Israel* (1978).
- Roland de Vaux, *Ancient Israel: Its Life and Institutions* (English translation 1961), the chapters on priests and Levites.
- Joachim Jeremias, *Jerusalem in the Time of Jesus* (English translation 1969): numbers and divisions of priests and Levites in the late Second Temple.
- The Mishnah, tractates Tamid, Yoma, Bekhorot, Negaim and Middot (English by Herbert Danby, 1933), and Josephus, *Against Apion* (public domain, not on the shelf; Edersheim cites its figure for the priesthood).

## Method and checks

- Each item's quotes were written from the shelf and located by `src/build_law_questions_candidates.py`, which stops if a quote is not found. Where a source breaks a word across a line (OCR text) the quote keeps the break ('Penta- teuchal' appears in the scan).
- `tests/test_law_questions_candidates.py` checks structure, that all seven keys are present with 3 to 10 items, that each quote is in its file within 2,000 characters of its offset and starts at the offset, that Wikipedia items name their revision date and licence, that the new shelf files are in `SOURCE.md` and the index, and that this digest carries its required sections and counts.
- The old shelf files were not changed. `data/raw/shelf/SOURCE.md` and `request_log.txt` were appended to, and the new works were added to `WORKS` in `src/build_shelf_index.py`, which was re-run.
- Revision dates for the Wikipedia items come from the first line of each file. Wikipedia's articles are summaries, and several are edited continually; a later revision may differ.
"""
(ROOT / "docs" / "LAW_QUESTIONS_DIGEST.md").write_text(DOC, encoding="utf-8", newline="\n")
print("wrote digest", total)
