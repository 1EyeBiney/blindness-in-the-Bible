"""Write docs/LAW_AND_LIFE_DIGEST.md from data/reference/law_and_life_candidates.json.

The prose per key (coverage and digest) is written by hand below. The item lists, with
locators, are generated from the JSON so they cannot drift from it.

    python src/write_law_digest.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "data" / "reference" / "law_and_life_candidates.json").read_text(encoding="utf-8"))
OUT = ROOT / "docs" / "LAW_AND_LIFE_DIGEST.md"

TITLES = {
    "law-stumbling-block": "Leviticus 19:14 and Deuteronomy 27:18, the stumbling-block and the wandering blind",
    "law-servant-blinded": "Exodus 21:26-27, the servant whose eye is lost",
    "law-priest": "Leviticus 21:16-23, the priest with a blemish",
    "law-blind-animals": "Leviticus 22:22, Deuteronomy 15:21 and Malachi 1:8, blind animals",
    "life-camp": "Living blind, then: a herding family moving between camps (Isaac)",
    "life-village": "Living blind, then: a hill-country village and sanctuary town (Shiloh: Eli and Ahijah)",
    "life-town-gate": "Living blind, then: a walled town with a gate (Jabesh-gilead, Jericho, Job at the gate)",
    "life-jerusalem": "Living blind, then: first-century Jerusalem",
    "walk-by-faith": "2 Corinthians 5:7 in its context",
    "law-as-evidence": "A law as evidence of a problem; how neighbouring peoples treated the blind",
}

NOTES = {
    "law-stumbling-block": (
        "Good on how commentators read the two verses. Thin on how Israel's treatment of the blind compared with its neighbours': the only neighbour "
        "source is Hammurabi, and it does not mention the blind.",
        "Matthew Henry reads Leviticus 19:14 as a command to take care of the blind person's safety, and says the ban on a stumbling-block also implies a "
        "duty to remove one. His reason for pairing the deaf and the blind is that neither can answer back, so the law leans on the fear of God, who sees "
        "and hears for them. On Deuteronomy 27:18 he reads the curse as aimed at an adviser who sends a trusting person the wrong way, and he links it to "
        "Jesus's saying about the blind leading the blind. He also says the Jews held that by saying Amen to these curses the people bound themselves to "
        "keep the laws and to hinder their neighbours from breaking them. The 1915 encyclopaedia sums up the Law's two sides: blindness barred a man from the "
        "priesthood, but care of the blind was specially enjoined. Smith's and Easton's say the same in a line each. Josephus, retelling the Law, adds the "
        "road: show the way to people who do not know it, and do not revile anyone blind or dumb. On the Hammurabi side, the Code's own prologue (per Wikipedia) "
        "claims the king rules to stop the strong oppressing the weak, and the epilogue (per the 1915 encyclopaedia) calls him a helper of the oppressed; but "
        "the English Code on the shelf (Johns, 1903) has no section about the blind, and Johns leaves out the prologue and epilogue."),
    "law-servant-blinded": (
        "Rich. Hammurabi's eye and tooth sections are on the shelf in a public-domain translation, with the 1915 encyclopaedia and Wikipedia to compare "
        "them with Exodus. Henry and Smith's say what the Hebrew law did.",
        "Hammurabi's rules (Johns's numbering) turn on the victim's rank. Section 196: a man who destroys a gentleman's eye loses his own. Section 198: for "
        "a poor man's eye, one mina of silver. Section 199: for the eye of a gentleman's servant, half his price. Teeth follow the same pattern (sections 200 "
        "and 201). The Hebrew law of Exodus 21:26-27, by contrast, frees the servant whose eye or tooth the master destroys. Henry's reason: to keep masters "
        "from abusing servants (they would lose the service) and to give an abused servant liberty to set against the pain and disgrace. Smith's makes the "
        "same point twice. Wikipedia says the Exodus passage, like Hammurabi, applies reciprocity between equals and then gives a different rule for slaves, "
        "but its remark that the owner 'pays no other consequence' is the editors' reading. The 1915 encyclopaedia says the parallels with Hammurabi are not "
        "accidental and not direct borrowing, with 'numerous marked divergences'. Josephus adds that in his day the law of maiming allowed the injured person to "
        "take money instead. A side-find: Hammurabi's Code also fixes penalties for a surgeon who loses a patient's eye (hands cut off if the patient is a gentleman)."),
    "law-priest": (
        "Good. Henry, the 1915 encyclopaedia, Easton's, Josephus and Edersheim all speak; Henry is the only source that gives the reason for the ruling and "
        "the provision for eating the holy food.",
        "The text of Leviticus 21:16-23 sets out a list of blemishes that barred a descendant of Aaron from offering the food of God, and blindness heads the "
        "list. Verse 22 says that he 'shall eat the bread of his God, both of the most holy, and of the holy', but verse 23 forbids him to go in to the veil "
        "or come near the altar. Henry (the only commentator on the shelf for this passage) says the blemishes were ones the priest could not help, 'therefore, "
        "though they might not work, they must not starve'; he also gives a reason about appearance and the people's judgment which is the commentator's, not "
        "the text's. Josephus confirms the rule in the same form (a share among the priests, but not the altar or the holy house), and records a first-century BC case "
        "in which the rule was used: Antigonus cut off the ears of the high priest Hyrcanus to bar him. The 1915 encyclopaedia identifies the eye blemish "
        "in verse 20 as cataract or white spots. Later rules show the idea being worked into degrees: one source says a man blind of even one eye was "
        "excluded from pronouncing the blessing; Edersheim, in a passage on synagogue prayer, says those 'so blind as not to be able to discern daylight' could not. "
        "Henry's gospel application is that people with such blemishes are not excluded from spiritual sacrifice or ministry."),
    "law-blind-animals": (
        "Good on why a blemished animal could not be offered (honour to God, Christ as the unblemished lamb) and on the Malachi comparison. Nothing on the "
        "shelf connects the animal rule to how blind people were regarded.",
        "Henry on Leviticus 22: whatever was offered had to be without blemish, and the verse lists what counted: blind, lame, a wen, the mange. His reason is "
        "that what is given for God's honour should be the best of its kind, and that the unblemished sacrifices were types of Christ the lamb 'without blemish "
        "and without spot'. He says the neighbours' priests were less strict. On Deuteronomy 15:21 he says the blemished firstling was not wasted: it was eaten at home as ordinary "
        "food, clean and unclean alike (verse 22). For Malachi 1:8 the argument is the governor comparison: offer the blind and the lame to your governor, "
        "'will he be pleased with thee?' Henry reads it as 'would they dare to affront an earthly prince?'. Easton's and the 1915 encyclopaedia put priests and animals "
        "in a single sentence. Henry also uses 'the blind, and the lame, and the sick' as a picture of poor worship; that figure is flagged."),
    "life-camp": (
        "Fair for the tent, the move and the shepherd's work (Smith's), thinner for family care; nothing on a blind person's daily routine in a camp.",
        "Smith's gives the physical setting: black goat's-hair tents with nine poles, ropes tied to pegs driven with a mallet, a carpet partition, tents struck "
        "and packed on camels when the pasture is gone (citing Genesis 26, Isaac's chapter), camps near trees for shade, wells cut in limestone with steps and a curb. Every man from "
        "the sheikh to the slave is more or less a shepherd. Henry's Genesis 26 gives Isaac pushed by the Philistines from place to place and digging wells; his Genesis 27 comment places the "
        "adult sons within call. For family care Smith's has one sentence: those poor through bodily infirmity 'were usually taken care of by their kindred'. The 1915 encyclopaedia names "
        "sand, sun glare and flies as aggravating eye disease, and puts old-age blindness down to cataract. None of this says how a blind man walked a camp; the tent-rope and well-curb "
        "details are what a blind reader will want to think about, but no source on the shelf draws that link."),
    "life-village": (
        "Fair. The sanctuary town has Smith's, Wikipedia and Henry's text. Housing and roads are general statements from 19th-century dictionaries.",
        "Shiloh lay beside the highway from Bethel to Shechem; Elkanah came up yearly; the ark was there from Joshua's last days to Samuel's time. Wikipedia says "
        "pilgrims came for the feasts. For Eli, Henry's volume 2 supplies the texts and some comment: Samuel slept near, 'ready within call', in Henry's picture; "
        "at 98 Eli sat 'upon a seat by the wayside' watching, heard the crowd's noise and asked what it meant, and fell backward 'by the side of the gate'. For Ahijah the text has him unable to see "
        "'by reason of his age', and speaking when he 'heard the sound of her feet'. Smith's describes village houses of mud or stone, often one room, "
        "sometimes shared with cattle, with small high windows and flat roofs used for sleeping in summer. Henry's comment links Eli's dimness to his failings as a father; that idea is flagged "
        "and John 9:3 stands against it."),
    "life-town-gate": (
        "Good for the gate (the 1915 encyclopaedia's entry is full), fair for Jabesh and Jericho, thin for what a blind person did there.",
        "The gate is the public room of the town: most men passed through daily, it was the place for meeting, markets, courts and prophets' speeches (ISBE, Smith's, Easton's), "
        "closed at nightfall; streets were narrow, winding and locked at night. Job 29's 'eyes to the blind' is set at the gate; Henry reads it as counsel and says we best help people in the "
        "very thing they lack. Jabesh-gilead's elders were offered the loss of every right eye, which Henry says, for men who fought with a shield over the left eye, was in effect blinding them. "
        "Jericho has springs, and houses built on its walls (Smith's). Smith's says begging places were at street corners, temple gates and private houses in 'later times'. Josephus says the Jebusites "
        "set the blind and lame on the wall as derision; Henry thinks they were invalids or maimed soldiers; the 1915 encyclopaedia reads it as a mocking phrase."),
    "life-jerusalem": (
        "Rich on the Temple's steps and crowds, begging places and charity. Thin on housing and on the streets of the city itself.",
        "Edersheim thinks the man born blind of John 9 sat at the entrance to the Temple 'as objects of pity' did, probably calling 'Gain merit by me'. Smith's and the 1915 encyclopaedia both "
        "name the begging places: street corners, rich men's doors, the Temple gates, and the entrance to Jericho, a gateway for festival pilgrims. The encyclopaedia gives causes: no adequate relief, "
        "no medical science for eye disease like ophthalmia, and Roman taxes. Edersheim says alms were collected every week in money or food, two collecting and three distributing. "
        "For movement: fifteen (Edersheim) or fourteen (Josephus) steps up to the inner court, a Pool of Siloam stair of 34 steps, 'wide, stepped roads' for crowds (Wikipedia), "
        "valleys 'every where unpassable', an ascent 'perpetual' from three sides, and the Jericho road 'rough ... winding over rock and loose stones'. The crowd at Passover is estimated at "
        "300,000 to 400,000 (Wikipedia) or 'three millions' (Josephus)."),
    "walk-by-faith": (
        "Good from Henry; ISBE on faith helps. The shelf does not link the verse to blindness and does not say what eidos means in this verse.",
        "Henry places the verse in Paul's argument for why they did not faint under afflictions, and reads it: 'Faith is for this world, and sight is reserved for the other world', so we "
        "walk by faith 'till we come to live by sight'. His 'sight' is the vision of God after death, not eyesight, and he treats believers as 'pilgrims and strangers'. The 1915 encyclopaedia "
        "says faith in the New Testament mostly means reliance or trust and, on Hebrews 11:1, is 'simply reliance upon a God known to be trustworthy'; it lists 2 Corinthians 5:7 under figurative 'walk'. "
        "Easton's gives the same basic sense, trust. For the Greek word eidos in the verse, the shelf has only general glosses ('thing seen', 'external appearance')."),
    "law-as-evidence": (
        "Little. The commentators and dictionaries reason about purpose, not about what the laws show of practice. What exists: Henry on what each law was meant to prevent, the sources on "
        "neighbours' warfare, and Wikipedia and the 1915 encyclopaedia on the Code of Hammurabi.",
        "Brian's idea is that a law is evidence of a problem. The shelf gives two kinds of evidence against reading it too quickly. First, Henry says the Jewish writers found it impossible that anyone "
        "would literally put a stumbling-block before the blind, so read the law as about bad advice. Second, scholars of the Babylonian Code disagree about whether it was legislation, a record of cases, "
        "or a work of jurisprudence (Wikipedia), and its laws are all 'if ... then' cases, whereas Leviticus 19:14 is a general command. For the servant law, Henry's wording of the purpose ('to comfort them if "
        "they were abused') assumes the thing happened. The curses of Deuteronomy 27, Henry says, include wrongs the magistrate could not see. For practice: the priestly blemish rule was used in the first century BC "
        "(Josephus). The Old Testament is said to have no word for begging, though NT-era Jerusalem had begging places. For neighbours: Ammonites proposed taking every right eye in Jabesh; Easton's says "
        "conquerors blinded captives; the Jebusites placed the blind and lame on the wall; Greek stories give blindness as punishment and compensation (myth). Nothing on the shelf describes how a neighbouring "
        "people treated blind people day to day."),
}

NOT_ON_THE_SHELF = [
    ("Disability in the Hebrew Bible: Interpreting Mental and Physical Differences", "Saul M. Olyan", "2008"),
    ("Disability Studies and the Hebrew Bible: Figuring Mephibosheth in the David Story", "Jeremy Schipper", "2006"),
    ("Biblical Corpora: Representations of Disability in Hebrew Biblical Literature", "Rebecca Raphael", "2008"),
    ("This Abled Body: Rethinking Disabilities in Biblical Studies (edited volume)", "Hector Avalos, Sarah J. Melcher and Jeremy Schipper (eds.)", "2007"),
    ("Disability Studies and Biblical Literature (edited volume)", "Candida R. Moss and Jeremy Schipper (eds.)", "2011"),
    ("Judaism and Disability: Portrayals in Ancient Texts from the Tanach through the Bavli", "Judith Z. Abrams", "1998"),
    ("Disability in Antiquity (edited volume)", "Christian Laes (ed.)", "2017"),
    ("Law Collections from Mesopotamia and Asia Minor", "Martha T. Roth", "1995 (2nd ed. 1997)"),
    ("A History of Ancient Near Eastern Law (edited volume)", "Raymond Westbrook (ed.)", "2003"),
    ("King Hammurabi of Babylon: A Biography", "Marc Van De Mieroop", "2005"),
    ("Leviticus 17-22 (Anchor Bible)", "Jacob Milgrom", "2000"),
    ("Leviticus (JPS Torah Commentary)", "Baruch A. Levine", "1989"),
    ("Life in Biblical Israel", "Philip J. King and Lawrence E. Stager", "2001"),
    ("Daily Life in Biblical Times", "Oded Borowski", "2003"),
    ("Ancient Israel: Its Life and Institutions", "Roland de Vaux", "1961 (English)"),
    ("Jerusalem in the Time of Jesus", "Joachim Jeremias", "1969 (English)"),
    ("Poverty and Charity in Roman Palestine, First Three Centuries CE", "Gildas Hamel", "1990"),
    ("The Second Epistle to the Corinthians (New International Greek Testament Commentary)", "Murray J. Harris", "2005"),
    ("The Second Epistle to the Corinthians (New International Commentary on the New Testament)", "Paul Barnett", "1997"),
    ("II Corinthians (Anchor Bible)", "Victor Paul Furnish", "1984"),
]


def short(text, n=230):
    t = " ".join(text.split())
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + " ..."


def main():
    L = []
    w = L.append
    w("# Law and life: digest of the candidates")
    w("")
    w("Written 3 October 2026 (the day Brian approved more downloads for the bookshelf). This goes with `data/reference/law_and_life_candidates.json`, which holds candidate "
      "items for three groups of pages: the seven law verses about the blind, four 'Living blind, then' pages, and 2 Corinthians 5:7 in its context. "
      "It is built by `src/build_law_candidates.py`, which refuses to write a quote it cannot find in the shelf, and is checked by `tests/test_law_candidates.py`.")
    w("")
    w("Every item has a short paragraph, a citation as a reader would see it, one or more verbatim quotes with the file and character offset (line endings as LF), a confidence "
      "of `high` or `medium`, and often a `caution`. The test checks that each quote is really in its file at its offset. It does not check that the paragraph is a fair "
      "reading of the quote, and nothing here has been seen by Brian or a second reader yet. Read the `caution` lines before using an item.")
    w("")
    n = sum(len(v) for v in DATA.values())
    w(f"Counts: {n} items across {len(DATA)} keys. Nothing was taken from outside the shelf.")
    w("")
    w("## New on the shelf for this pass")
    w("")
    w("- Code of Hammurabi, translated by C. H. W. Johns (1903), from Project Gutenberg. L. W. King's 1910 translation was preferred but is not on Gutenberg, "
      "and the Yale Avalon site (where it is) is not in the host list that `tests/test_shelf.py` accepts, so it was not used. Johns's numbering differs a little from King's, "
      "and Johns omits the prologue and epilogue.")
    w("- Matthew Henry, volume 2 (Joshua to Esther) and volume 6 (Acts to Revelation), from CCEL; Rights line in both: public domain.")
    w("- Easton's Bible Dictionary (1897) from CCEL, found at the first try.")
    w("- Wikipedia (CC BY-SA 4.0, revisions recorded): Code of Hammurabi, Shiloh (biblical city), Jabesh-Gilead, City gate, Tabernacle, 'Lex talionis' (redirects to 'Eye for an eye'). "
      "'Disability in the Bible' and 'Disability in ancient Israel' do not exist as Wikipedia articles. The Tabernacle article was fetched but nothing was used from it.")
    w("")
    w("## Language flagged, not reproduced")
    w("")
    w("- Matthew Henry on Leviticus 21 and 22 uses dated words for bodily differences ('deformed', 'disfigured', 'comely') and links Eli's failing sight to his sons' faults; Easton's and Smith's use "
      "'deformity' and 'minor personal injury' for blemishes and loss of an eye. All are quoted only from after the word or described in the cautions.")
    w("- Henry uses 'the blind, and the lame, and the sick' as images of poor worship and 'spiritually blind' for sinful ministers; flagged in the cautions.")
    w("- The 1915 encyclopaedia's 'Blindness' entry has a passage on eye disease with disparaging language about crowds; its 'Beg, Beggar, Begging' entry ends with a passage "
      "about modern European Jewish beggars that is prejudiced. Neither passage is used. Edersheim (Life and Times, Book II) has a sentence calling a crowd of beggars 'unsightly from disease'; not used.")
    w("- Josephus's Antiquities (Whiston's footnotes) insult groups of Jews, as noted in `SHELF_REPORT.md`; only Josephus's own text is quoted.")
    w("")
    for key in DATA:
        cov, dig = NOTES[key]
        items = DATA[key]
        w(f"## `{key}`: {TITLES[key]}")
        w("")
        w(f"Items: {len(items)}. Coverage: {cov}")
        w("")
        w(dig)
        w("")
        for i, it in enumerate(items):
            locs = "; ".join(f"{e['file']} @ {e['offset']}" for e in it["evidence"])
            w(f"{i + 1}. [{it['confidence']}] {short(it['text'])}  ")
            w(f"   Source: {it['source']}.  ")
            w(f"   Quotes: {locs}.")
            if it.get("caution"):
                w(f"   Caution: {short(it['caution'], 300)}")
        w("")
    w("## What the shelf cannot tell us")
    w("")
    w("The shelf is nineteenth- and early twentieth-century reference works, an eighteenth-century commentary, Josephus and Wikipedia. It has no archaeology of ordinary houses after about 1900, "
      "no modern study of disability in the Bible, no recent edition of the Mesopotamian laws, and no modern commentary on 2 Corinthians. Specifically:")
    w("")
    w("- Anything about how a blind person actually got about, worked or was fed in a camp, village, gate or city. The sources describe the setting and the begging places; the connection "
      "to blind people is the reader's.")
    w("- Whether the begging places were chosen by the blind, by their families or by the town (care or containment). The sources name the places and the causes of begging; none says who decided.")
    w("- Whether the Hebrew laws about the blind answered a common wrong or a rare one. Henry reports that Jewish writers thought the literal act unthinkable; that is the only direct evidence.")
    w("- How Israel's neighbours treated blind people. Only warfare (blinding captives) and a taunt on a wall are on the shelf.")
    w("- What 'sight' (eidos) means in 2 Corinthians 5:7 and how the verse's context (a body as an 'earthly tent') relates to bodily weakness.")
    w("")
    w("These modern works might help. They are listed from the writer's general knowledge, not from the shelf and not quoted; check the details before citing any of them. Brian can decide whether to consult them.")
    w("")
    for title, author, year in NOT_ON_THE_SHELF:
        w(f"- {title}, {author}, {year}.")
    w("")
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(len(L), "lines")


if __name__ == "__main__":
    main()
