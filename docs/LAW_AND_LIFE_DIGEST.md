# Law and life: digest of the candidates

Written 3 October 2026 (the day Brian approved more downloads for the bookshelf). This goes with `data/reference/law_and_life_candidates.json`, which holds candidate items for three groups of pages: the seven law verses about the blind, four 'Living blind, then' pages, and 2 Corinthians 5:7 in its context. It is built by `src/build_law_candidates.py`, which refuses to write a quote it cannot find in the shelf, and is checked by `tests/test_law_candidates.py`.

Every item has a short paragraph, a citation as a reader would see it, one or more verbatim quotes with the file and character offset (line endings as LF), a confidence of `high` or `medium`, and often a `caution`. The test checks that each quote is really in its file at its offset. It does not check that the paragraph is a fair reading of the quote, and nothing here has been seen by Brian or a second reader yet. Read the `caution` lines before using an item.

Counts: 80 items across 10 keys. Nothing was taken from outside the shelf.

## New on the shelf for this pass

- Code of Hammurabi, translated by C. H. W. Johns (1903), from Project Gutenberg. L. W. King's 1910 translation was preferred but is not on Gutenberg, and the Yale Avalon site (where it is) is not in the host list that `tests/test_shelf.py` accepts, so it was not used. Johns's numbering differs a little from King's, and Johns omits the prologue and epilogue.
- Matthew Henry, volume 2 (Joshua to Esther) and volume 6 (Acts to Revelation), from CCEL; Rights line in both: public domain.
- Easton's Bible Dictionary (1897) from CCEL, found at the first try.
- Wikipedia (CC BY-SA 4.0, revisions recorded): Code of Hammurabi, Shiloh (biblical city), Jabesh-Gilead, City gate, Tabernacle, 'Lex talionis' (redirects to 'Eye for an eye'). 'Disability in the Bible' and 'Disability in ancient Israel' do not exist as Wikipedia articles. The Tabernacle article was fetched but nothing was used from it.

## Language flagged, not reproduced

- Matthew Henry on Leviticus 21 and 22 uses dated words for bodily differences ('deformed', 'disfigured', 'comely') and links Eli's failing sight to his sons' faults; Easton's and Smith's use 'deformity' and 'minor personal injury' for blemishes and loss of an eye. All are quoted only from after the word or described in the cautions.
- Henry uses 'the blind, and the lame, and the sick' as images of poor worship and 'spiritually blind' for sinful ministers; flagged in the cautions.
- The 1915 encyclopaedia's 'Blindness' entry has a passage on eye disease with disparaging language about crowds; its 'Beg, Beggar, Begging' entry ends with a passage about modern European Jewish beggars that is prejudiced. Neither passage is used. Edersheim (Life and Times, Book II) has a sentence calling a crowd of beggars 'unsightly from disease'; not used.
- Josephus's Antiquities (Whiston's footnotes) insult groups of Jews, as noted in `SHELF_REPORT.md`; only Josephus's own text is quoted.

## `law-stumbling-block`: Leviticus 19:14 and Deuteronomy 27:18, the stumbling-block and the wandering blind

Items: 7. Coverage: Good on how commentators read the two verses. Thin on how Israel's treatment of the blind compared with its neighbours': the only neighbour source is Hammurabi, and it does not mention the blind.

Matthew Henry reads Leviticus 19:14 as a command to take care of the blind person's safety, and says the ban on a stumbling-block also implies a duty to remove one. His reason for pairing the deaf and the blind is that neither can answer back, so the law leans on the fear of God, who sees and hears for them. On Deuteronomy 27:18 he reads the curse as aimed at an adviser who sends a trusting person the wrong way, and he links it to Jesus's saying about the blind leading the blind. He also says the Jews held that by saying Amen to these curses the people bound themselves to keep the laws and to hinder their neighbours from breaking them. The 1915 encyclopaedia sums up the Law's two sides: blindness barred a man from the priesthood, but care of the blind was specially enjoined. Smith's and Easton's say the same in a line each. Josephus, retelling the Law, adds the road: show the way to people who do not know it, and do not revile anyone blind or dumb. On the Hammurabi side, the Code's own prologue (per Wikipedia) claims the king rules to stop the strong oppressing the weak, and the epilogue (per the 1915 encyclopaedia) calls him a helper of the oppressed; but the English Code on the shelf (Johns, 1903) has no section about the blind, and Johns leaves out the prologue and epilogue.

1. [high] Matthew Henry reads Leviticus 19:14 as a command about the blind person's safety. To put a stumbling-block before a blind person, he says, is to add affliction to the afflicted and to make God's providence serve one's malice. He ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 19.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2978115; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2978327.
2. [high] Henry gives a reason the verse ends with 'fear thy God': the deaf and the blind cannot answer back or get even, so people who would never do this to someone who could retaliate need to be reminded that God sees and hears and ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 19.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2977986; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2978941.
   Caution: The second quotation is Henry quoting an unnamed Jewish saying; he does not say where it comes from.
3. [medium] For Deuteronomy 27:18 ('Cursed be he that maketh the blind to wander out of the way') Henry understands the offender as an adviser who, when asked the way, sends a trusting person somewhere that will harm him. He calls this ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Deuteronomy 27.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 4751269; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 4751689; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 4749382.
   Caution: Henry takes the verse as being about misleading advice; the verse in the King James text is about 'the blind' and the shelf does not say whether a literal blind traveller is meant. The 'Jews say' passage is Henry quoting Bishop Patrick quoting them.
4. [high] The 1915 Bible encyclopaedia sums up the Law's two sides in one sentence: blindness disqualified a man from the priesthood (Leviticus 21:18), but care of the blind was specially enjoined (Leviticus 19:14) and wrongs against them ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Blindness', vol 1, pp. 487-488.  
   Quotes: isbe_1915_vol1.txt @ 3980521.
5. [high] Smith's and Easton's dictionaries both say the Law commanded compassion toward the blind and cite Leviticus 19:14 and Deuteronomy 27:18.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Blindness'; Easton's Bible Dictionary (1897), entry 'Blind'.  
   Quotes: smiths_bible_dictionary.txt @ 382972; easton_ebd.txt @ 420153.
   Caution: Smith's prints the second reference as 'Leviticus 19:14; 27:18'; the second is plainly Deuteronomy 27:18.
6. [high] Josephus, retelling the Law in the first century, puts the same concern in everyday terms: it is a duty to show the road to people who do not know it and not to treat it as a joke to send them the wrong way; and 'let no one ...  
   Source: Josephus, Antiquities of the Jews (Whiston translation), Book IV, chapter 8, section 31-32.  
   Quotes: josephus_antiquities_pg2848.txt @ 576261.
   Caution: Josephus (about AD 93) is retelling, not translating; the sentence about the blind is his wording. 'Dumb' means unable to speak.
7. [medium] Hammurabi, king of Babylon, says in his prologue that the gods gave him his rule 'to prevent the strong from oppressing the weak', and the 1915 encyclopaedia says the epilogue calls him a helper of the oppressed and an adviser of ...  
   Source: Wikipedia, 'Code of Hammurabi', revision of 2 October 2026 (CC BY-SA 4.0); International Standard Bible Encyclopaedia (1915), entry 'Hammurabi', vol 2, p. 1331.  
   Quotes: wikipedia_Code_of_Hammurabi.wiki.txt @ 2603; isbe_1915_vol2.txt @ 5654132.
   Caution: Johns (1903) leaves out the prologue and epilogue (he says so), so the shelf has the king's own claims only at second hand. 'No mention of the blind' is based on a search of the Johns text, which found no occurrence of 'blind'.

## `law-servant-blinded`: Exodus 21:26-27, the servant whose eye is lost

Items: 9. Coverage: Rich. Hammurabi's eye and tooth sections are on the shelf in a public-domain translation, with the 1915 encyclopaedia and Wikipedia to compare them with Exodus. Henry and Smith's say what the Hebrew law did.

Hammurabi's rules (Johns's numbering) turn on the victim's rank. Section 196: a man who destroys a gentleman's eye loses his own. Section 198: for a poor man's eye, one mina of silver. Section 199: for the eye of a gentleman's servant, half his price. Teeth follow the same pattern (sections 200 and 201). The Hebrew law of Exodus 21:26-27, by contrast, frees the servant whose eye or tooth the master destroys. Henry's reason: to keep masters from abusing servants (they would lose the service) and to give an abused servant liberty to set against the pain and disgrace. Smith's makes the same point twice. Wikipedia says the Exodus passage, like Hammurabi, applies reciprocity between equals and then gives a different rule for slaves, but its remark that the owner 'pays no other consequence' is the editors' reading. The 1915 encyclopaedia says the parallels with Hammurabi are not accidental and not direct borrowing, with 'numerous marked divergences'. Josephus adds that in his day the law of maiming allowed the injured person to take money instead. A side-find: Hammurabi's Code also fixes penalties for a surgeon who loses a patient's eye (hands cut off if the patient is a gentleman).

1. [high] Matthew Henry puts Exodus 21:26-27 under 'the care God took of servants'. If a master maimed a servant, even by striking out a tooth, the servant went free. Henry gives two purposes: to keep masters from abusing servants, since ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Exodus 21.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2127107; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2127418.
2. [high] Smith's Bible Dictionary says in two places that the master's power over a servant was limited by this law: in 'Law of Moses' that maiming gave liberty at once, and in 'Slave' that provision was made for the protection of the ...  
   Source: Smith's Bible Dictionary (1884 edition), entries 'Law of Moses' and 'Slave'.  
   Quotes: smiths_bible_dictionary.txt @ 1420240; smiths_bible_dictionary.txt @ 2737812; smiths_bible_dictionary.txt @ 2737988.
   Caution: The 'Slave' entry calls the loss of an eye or tooth a 'minor personal injury'. That phrase is not suitable to repeat; the second quotation is cut to start after it.
3. [high] Hammurabi's law for an eye lost between equals: 'If a man has caused the loss of a gentleman's eye, his eye one shall cause to be lost.' The class is part of the rule. The 1915 encyclopaedia quotes the same section with 'a free ...  
   Source: C. H. W. Johns (translator), The Oldest Code of Laws in the World (1903), Code of Hammurabi, section 196; International Standard Bible Encyclopaedia (1915), entry 'Hammurabi', vol 2, p. 1331.  
   Quotes: hammurabi_johns_pg17150.txt @ 51708; isbe_1915_vol2.txt @ 5658252.
   Caution: Johns renders the class term 'gentleman'; later translations use other words ('free man', 'awilum').
4. [high] Hammurabi sets lower penalties for the same injury when the victim is of lower rank. For a poor man who loses an eye the payment is one mina of silver (section 198); for the eye of a gentleman's servant the payment is half his ...  
   Source: C. H. W. Johns (translator), The Oldest Code of Laws in the World (1903), Code of Hammurabi, sections 198-199.  
   Quotes: hammurabi_johns_pg17150.txt @ 51893; hammurabi_johns_pg17150.txt @ 52017.
   Caution: Johns writes 'servant' where the 1915 encyclopaedia and Wikipedia write 'slave'.
5. [high] The same graded pattern holds for teeth, the other injury named in Exodus 21:27. Between equals the offender loses his tooth (section 200); for a poor man's tooth the fine is one-third of a mina of silver (section 201).  
   Source: C. H. W. Johns (translator), The Oldest Code of Laws in the World (1903), Code of Hammurabi, sections 200-201.  
   Quotes: hammurabi_johns_pg17150.txt @ 52175.
6. [high] The 1915 encyclopaedia (article by A. Ungnad) says Hammurabi's rules on wounding begin with the 'jus talionis', an eye for an eye, a bone for a bone, a tooth for a tooth, and that persons lower in the social grade usually ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Hammurabi', vol 2, p. 1330.  
   Quotes: isbe_1915_vol2.txt @ 5649404.
7. [medium] Wikipedia's article on 'an eye for an eye' says that in Exodus 21, as in Hammurabi's Code, reciprocal justice seems to apply between social equals, and that Exodus then gives a different rule for a slave-owner who blinds a ...  
   Source: Wikipedia, 'Eye for an eye', revision of 2 October 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_Eye_for_an_eye.wiki.txt @ 15997; wikipedia_Eye_for_an_eye.wiki.txt @ 16367.
   Caution: The words 'pays no other consequence' are the Wikipedia editors' reading (they cite Michael Coogan, 2009); the shelf has no commentary that says whether freedom was the whole remedy.
8. [medium] Josephus's version of the law of maiming (about AD 93) is that the offender suffers the same loss 'unless he that is maimed will accept of money instead of it', because the law lets the injured person judge the value of the loss.  
   Source: Josephus, Antiquities of the Jews (Whiston translation), Book IV, chapter 8, section 35.  
   Quotes: josephus_antiquities_pg2848.txt @ 577647; josephus_antiquities_pg2848.txt @ 577841.
   Caution: This is Josephus's summary of the law for free persons and does not mention servants or eyes by name.
9. [medium] Hammurabi's Code also deals with eye operations. A doctor who opens an abscess of the eye with a bronze lancet and cures it takes ten shekels of silver (section 215); if the eye is lost, a doctor's hands are cut off when the ...  
   Source: C. H. W. Johns (translator), The Oldest Code of Laws in the World (1903), Code of Hammurabi, sections 215, 218, 220; International Standard Bible Encyclopaedia (1915), entry 'Hammurabi', vol 2, p. 1331.  
   Quotes: hammurabi_johns_pg17150.txt @ 54106; hammurabi_johns_pg17150.txt @ 54690; hammurabi_johns_pg17150.txt @ 54925; isbe_1915_vol2.txt @ 5650686.
   Caution: A side-find, not part of Exodus 21. The point for Brian is only that eyes were already being operated on, and sight lost in the operating room had a penalty that depended on rank.

## `law-priest`: Leviticus 21:16-23, the priest with a blemish

Items: 9. Coverage: Good. Henry, the 1915 encyclopaedia, Easton's, Josephus and Edersheim all speak; Henry is the only source that gives the reason for the ruling and the provision for eating the holy food.

The text of Leviticus 21:16-23 sets out a list of blemishes that barred a descendant of Aaron from offering the food of God, and blindness heads the list. Verse 22 says that he 'shall eat the bread of his God, both of the most holy, and of the holy', but verse 23 forbids him to go in to the veil or come near the altar. Henry (the only commentator on the shelf for this passage) says the blemishes were ones the priest could not help, 'therefore, though they might not work, they must not starve'; he also gives a reason about appearance and the people's judgment which is the commentator's, not the text's. Josephus confirms the rule in the same form (a share among the priests, but not the altar or the holy house), and records a first-century BC case in which the rule was used: Antigonus cut off the ears of the high priest Hyrcanus to bar him. The 1915 encyclopaedia identifies the eye blemish in verse 20 as cataract or white spots. Later rules show the idea being worked into degrees: one source says a man blind of even one eye was excluded from pronouncing the blessing; Edersheim, in a passage on synagogue prayer, says those 'so blind as not to be able to discern daylight' could not. Henry's gospel application is that people with such blemishes are not excluded from spiritual sacrifice or ministry.

1. [high] Matthew Henry's text of Leviticus 21:22-23 shows what the priest with a blemish kept and what he lost: he 'shall eat the bread of his God, both of the most holy, and of the holy', but shall not go in to the veil or come near the ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 21 (text of verses 22-23 as printed by Henry).  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3041231.
2. [high] On the same verses Henry says the priest with a blemish was entitled to his share of the sacrifices, even the most holy things such as the show-bread and sin-offerings. His reason: the blemishes were ones the priest could not ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 21.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3042285; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3042534.
   Caution: Henry goes on to say 'the deformed child in the family must have its child's part'; 'deformed' is dated wording and is not reproduced.
3. [medium] Henry notes that the list of blemishes mixed lasting ones, 'as blindness', with passing ones such as a scab, where the disability ceased when the condition cleared. His reason for the rule is about public appearance: it was ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 21.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3041976; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3043183.
   Caution: The second quotation gives Henry's own reason (appearance and reputation of the sanctuary); the Bible text does not give a reason in these verses. Henry's wording ('comely', 'disfigured') should not be adopted.
4. [high] Henry's gospel application: people who live with such blemishes 'have reason to thank God that they are not thereby excluded from offering spiritual sacrifices to God', nor, if otherwise qualified, from the ministry.  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 21.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3043821.
   Caution: In the next sentences Henry uses 'spiritually blind, and lame' as pictures of sinful ministers. That figure runs the two senses of blindness together and is not repeated.
5. [high] The 1915 encyclopaedia says the existence of a blemish in a man of priestly descent kept him from the priestly office, and that the same held for animals fit for sacrifice. It identifies the eye blemish of Leviticus 21:20 as ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Blemish', vol 1, pp. 486-487.  
   Quotes: isbe_1915_vol1.txt @ 3969400; isbe_1915_vol1.txt @ 3970237.
   Caution: The identification with cataract is the encyclopaedia's (the Hebrew word is uncertain).
6. [high] Josephus, giving the law, says a priest with any blemish 'should have his portion indeed among the priests', but was forbidden to go up to the altar or into the holy house.  
   Source: Josephus, Antiquities of the Jews (Whiston translation), Book III, chapter 12, section 2.  
   Quotes: josephus_antiquities_pg2848.txt @ 434606.
7. [medium] Later rules about sight and the blessing. The 1915 encyclopaedia says that among those excluded from pronouncing the priestly blessing was one who 'was blind even of one eye'. Edersheim, describing synagogue worship, says the ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Benediction', vol 1, p. 435; Edersheim, Sketches of Jewish Social Life (1876), chapter 17.  
   Quotes: isbe_1915_vol1.txt @ 3555856; edersheim_sketches.txt @ 496220; edersheim_sketches.txt @ 497064.
   Caution: The two sources disagree on how much sight was required (one eye versus daylight); neither says which period it describes. Edersheim's sentence is in his chapter on synagogue prayer, so it may concern leading prayer there and not the Temple. He is reporting rabbinic rules written down after the New ...
8. [medium] Edersheim adds a related rule from the Mishnah: priests with blemishes on their hands, face or feet were not to pronounce the blessing, 'so as not to attract attention'; he adds that this 'presumably refers to those officiating ...  
   Source: Edersheim, The Life and Times of Jesus the Messiah (1883), Book III, chapter X.  
   Quotes: edersheim_life_and_times.txt @ 1385650.
   Caution: Rabbinic rules, not the text of Leviticus. Edersheim writes of the Temple practice of the first century AD from later records.
9. [medium] Josephus records that the priestly blemish rule was used in his own history: in the first century BC Antigonus, brought back into Judea by the king of the Parthians, cut off the ears of his rival, the high priest Hyrcanus, so ...  
   Source: Josephus, Antiquities of the Jews (Whiston translation), Book XIV, chapter 13, section 10.  
   Quotes: josephus_antiquities_pg2848.txt @ 2117488.
   Caution: The man was not blind, and the injury was inflicted to bar him, but it shows the law about the priesthood was still read literally in the first century BC.

## `law-blind-animals`: Leviticus 22:22, Deuteronomy 15:21 and Malachi 1:8, blind animals

Items: 7. Coverage: Good on why a blemished animal could not be offered (honour to God, Christ as the unblemished lamb) and on the Malachi comparison. Nothing on the shelf connects the animal rule to how blind people were regarded.

Henry on Leviticus 22: whatever was offered had to be without blemish, and the verse lists what counted: blind, lame, a wen, the mange. His reason is that what is given for God's honour should be the best of its kind, and that the unblemished sacrifices were types of Christ the lamb 'without blemish and without spot'. He says the neighbours' priests were less strict. On Deuteronomy 15:21 he says the blemished firstling was not wasted: it was eaten at home as ordinary food, clean and unclean alike (verse 22). For Malachi 1:8 the argument is the governor comparison: offer the blind and the lame to your governor, 'will he be pleased with thee?' Henry reads it as 'would they dare to affront an earthly prince?'. Easton's and the 1915 encyclopaedia put priests and animals in a single sentence. Henry also uses 'the blind, and the lame, and the sick' as a picture of poor worship; that figure is flagged.

1. [high] Matthew Henry on Leviticus 22: the first of the four laws is that whatever was offered had to be without blemish, and the chapter now says what counted as a blemish: if the beast 'was blind, or lame, had a wen, or the mange' ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 22.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3059647; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3059854.
2. [high] Henry gives the reason as honour to God: everything used for his honour should be the best of its kind, 'he that is the best must have the best'. He adds that the law made the sacrifices fitter to be types of Christ, 'a Lamb ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 22.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3062372; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3062842.
3. [medium] Henry sets Israel's rule beside the neighbours' practice: 'The heathen priests were many of them not so strict in this matter, but would receive sacrifices for their gods that were ever so scandalous; but let strangers know that ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 22.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3062019.
   Caution: Henry's claim about 'the heathen priests' is a general statement with no source given; the shelf has nothing to check it against.
4. [high] Henry on Deuteronomy 15:21 ('if there be any blemish therein, as if it be lame, or blind'): a blemished firstling 'must not be brought near the sanctuary' but 'must not be reared, but killed and eaten at their own houses as ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Deuteronomy 15.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 4483925; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 4485606.
5. [high] Malachi 1:8 and Henry's reading. The prophet says: 'if ye offer the blind for sacrifice, is it not evil? ... offer it now unto thy governor; will he be pleased with thee?' Henry reads it as an argument from honour: would they ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Malachi 1.  
   Quotes: matthew_henry_vol4.txt @ 8585932; matthew_henry_vol4.txt @ 8601785.
6. [high] Easton's dictionary groups the two rules in one entry: 'Blemish' is an imperfection 'excluding men from the priesthood, and rendering animals unfit to be offered in sacrifice (Lev. 21:17-23; 22:19-25)'. The 1915 encyclopaedia ...  
   Source: Easton's Bible Dictionary (1897), entry 'Blemish'; International Standard Bible Encyclopaedia (1915), entry 'Blemish', vol 1, pp. 486-487.  
   Quotes: easton_ebd.txt @ 418271; isbe_1915_vol1.txt @ 3969539.
   Caution: Easton's opening word for a blemish is a dated term for a bodily difference and is cut from the quotation.
7. [medium] Henry also reads the verse as a rule for worship: 'If our devotions are ignorant, and cold, and trifling, and full of distractions, we offer the blind, and the lame, and the sick, for sacrifice'. Here blindness stands for a poor ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 22.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 3063657.
   Caution: This is the commentator's figure for poor worship. It uses 'the blind' as an image of something second-rate and should not be carried over to people; included so Brian can see how the verse was applied.

## `life-camp`: Living blind, then: a herding family moving between camps (Isaac)

Items: 8. Coverage: Fair for the tent, the move and the shepherd's work (Smith's), thinner for family care; nothing on a blind person's daily routine in a camp.

Smith's gives the physical setting: black goat's-hair tents with nine poles, ropes tied to pegs driven with a mallet, a carpet partition, tents struck and packed on camels when the pasture is gone (citing Genesis 26, Isaac's chapter), camps near trees for shade, wells cut in limestone with steps and a curb. Every man from the sheikh to the slave is more or less a shepherd. Henry's Genesis 26 gives Isaac pushed by the Philistines from place to place and digging wells; his Genesis 27 comment places the adult sons within call. For family care Smith's has one sentence: those poor through bodily infirmity 'were usually taken care of by their kindred'. The 1915 encyclopaedia names sand, sun glare and flies as aggravating eye disease, and puts old-age blindness down to cataract. None of this says how a blind man walked a camp; the tent-rope and well-curb details are what a blind reader will want to think about, but no source on the shelf draws that link.

1. [high] Smith's dictionary says that when the pasture near an encampment is used up the tents are taken down, packed on camels and moved, citing Genesis 26:17, 22 and 25, which are the passages about Isaac's moves.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Tent'.  
   Quotes: smiths_bible_dictionary.txt @ 2925648.
2. [medium] Smith's describes the tent itself: a covering of black goat's hair, usually nine tent-poles in three groups, ropes fastened to pins driven in with a mallet, and a carpet partition dividing the tent in two. It also says that Arabs ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Tent'.  
   Quotes: smiths_bible_dictionary.txt @ 2924612; smiths_bible_dictionary.txt @ 2924767; smiths_bible_dictionary.txt @ 2925217; smiths_bible_dictionary.txt @ 2925469; smiths_bible_dictionary.txt @ 2925810.
   Caution: Describes the modern Arab tent as known to the 19th-century editors. Nothing on the shelf says what the layout, the ropes or the pins meant for someone who could not see; that is for Brian or a later source.
3. [high] Smith's on shepherds: in a nomadic society 'every man, from the sheikh down to the slave, is more or less a shepherd', and the work meant exposure to heat and cold, wild beasts and raiders.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Shepherd'.  
   Quotes: smiths_bible_dictionary.txt @ 2650599; smiths_bible_dictionary.txt @ 2651588; smiths_bible_dictionary.txt @ 2651983; smiths_bible_dictionary.txt @ 2652195.
4. [medium] Smith's on wells: they are usually cut into solid limestone, 'sometimes with steps to descend into them', with a stone curb or low wall round the mouth, and water is drawn with a rope and bucket or waterskin among other methods.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Well'.  
   Quotes: smiths_bible_dictionary.txt @ 3167018; smiths_bible_dictionary.txt @ 3167169; smiths_bible_dictionary.txt @ 3167756.
   Caution: Describes wells of Palestine as seen in the 19th century. Genesis 26 is about wells in the Philistine country around Gerar and Beersheba.
5. [medium] Henry on Genesis 26: when the Philistines expelled Isaac and gave him 'continual molestation' and forced him to move from place to place, God visited him; Isaac 'pitched his tent there: and there Isaac's servants digged a well'. ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Genesis 26.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 950986; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 957421.
   Caution: The first quotation is the King James text as printed by Henry; the second is Henry's comment. The link to Genesis 27 is the writer's.
6. [medium] Henry on Genesis 27:1: Esau 'though married, had not yet removed', and his parents had not expelled him despite grief over his marriage, so the blind father's household still had grown sons near it.  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Genesis 27.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 968893.
   Caution: Henry is explaining why Esau was within call; he says nothing about daily care of a blind man.
7. [medium] Smith's on caring for the infirm in Israel: 'Those who were indigent through bodily infirmities were usually taken care of by their kindred.' This is a general statement about the Hebrews, not about camps.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Beggar, Begging'.  
   Quotes: smiths_bible_dictionary.txt @ 326448.
   Caution: General statement; 'usually' is Smith's hedge. Smith's gives no source for it.
8. [medium] The 1915 encyclopaedia on the setting for eye disease: the diseases are 'aggravated by sand, and the sun glare', purulent eye disease is spread by flies, and the blindness of old age 'probably from senile cataract' is named in ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Blindness', vol 1, pp. 487-488.  
   Quotes: isbe_1915_vol1.txt @ 3978064; isbe_1915_vol1.txt @ 3977076; isbe_1915_vol1.txt @ 3978973.
   Caution: Written by a physician in 1915 who describes some conditions in language not repeated here; the medical claims are a century old.

## `life-village`: Living blind, then: a hill-country village and sanctuary town (Shiloh: Eli and Ahijah)

Items: 8. Coverage: Fair. The sanctuary town has Smith's, Wikipedia and Henry's text. Housing and roads are general statements from 19th-century dictionaries.

Shiloh lay beside the highway from Bethel to Shechem; Elkanah came up yearly; the ark was there from Joshua's last days to Samuel's time. Wikipedia says pilgrims came for the feasts. For Eli, Henry's volume 2 supplies the texts and some comment: Samuel slept near, 'ready within call', in Henry's picture; at 98 Eli sat 'upon a seat by the wayside' watching, heard the crowd's noise and asked what it meant, and fell backward 'by the side of the gate'. For Ahijah the text has him unable to see 'by reason of his age', and speaking when he 'heard the sound of her feet'. Smith's describes village houses of mud or stone, often one room, sometimes shared with cattle, with small high windows and flat roofs used for sleeping in summer. Henry's comment links Eli's dimness to his failings as a father; that idea is flagged and John 9:3 stands against it.

1. [high] Smith's on Shiloh: it lay 'on the north side of Bethel, on the east side of the highway that goeth up from Bethel to Shechem and on the south of Lebonah' (Judges 21:19); the ark was kept there 'from the last days of Joshua to the ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Shiloh'.  
   Quotes: smiths_bible_dictionary.txt @ 2663811; smiths_bible_dictionary.txt @ 2663090.
2. [high] Wikipedia's article says people made pilgrimages to Shiloh for major feasts and sacrifices and that Judges 21 records an annual dance of maidens among the vineyards there.  
   Source: Wikipedia, 'Shiloh (biblical city)', revision of 26 September 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_Shiloh_biblical_city.wiki.txt @ 10593.
   Caution: Wikipedia's account of the site's history is partly disputed in the article itself (it notes disagreement over the date and cause of its destruction).
3. [high] Henry's text of 1 Samuel 1:3 shows the yearly rhythm of the sanctuary town: Elkanah 'went up out of his city yearly to worship and to sacrifice unto the Lord of hosts in Shiloh'; Hannah brought Samuel's little coat 'from year to ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 1 Samuel 1-2 (text of the verses).  
   Quotes: matthew_henry_vol2.txt @ 1580521; matthew_henry_vol2.txt @ 1646155.
   Caution: Both quotations are the King James text as printed in Henry's volume, not Henry's own words.
4. [medium] Henry on 1 Samuel 3 pictures young Samuel sleeping 'in some closet near to Eli's room, as his page of the back-stairs, ready within call if the old man should want any thing in the night, perhaps to read to him if he could not ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 1 Samuel 3.  
   Quotes: matthew_henry_vol2.txt @ 1686892; matthew_henry_vol2.txt @ 1686807.
   Caution: The arrangement is Henry's picture, not stated in the text. In the sentence before it Henry says Eli's dim eyes 'came justly upon him for winking at his sons' faults'; that links blindness to the person's sin and is the idea John 9:3 rejects. It is not repeated.
5. [high] The text of 1 Samuel 4:13-18 as printed by Henry shows Eli at the town's entrance: he 'sat upon a seat by the wayside watching', heard the crying and asked 'What meaneth the noise of this tumult?', and 'fell from off the seat ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 1 Samuel 4 (text of the verses).  
   Quotes: matthew_henry_vol2.txt @ 1730743; matthew_henry_vol2.txt @ 1731066; matthew_henry_vol2.txt @ 1730920; matthew_henry_vol2.txt @ 1731615.
   Caution: King James text as printed in Henry. 'Heard the noise' is what the verse says; the verse does not say who led or seated him.
6. [high] Henry's text of 1 Kings 14:4-6 for Ahijah of Shiloh: 'Ahijah could not see; for his eyes were set by reason of his age', and 'when Ahijah heard the sound of her feet, as she came in at the door', he spoke before she did.  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 1 Kings 14 (text of the verses).  
   Quotes: matthew_henry_vol2.txt @ 3684349; matthew_henry_vol2.txt @ 3684702.
   Caution: King James text as printed in Henry. Brian has pointed out that the verse does not say he recognised her footsteps; the verse leaves it open how he knew.
7. [medium] Smith's on the rural house: 'mere huts of mud or sunburnt bricks', usually one storey and often one room, sometimes with the cattle in the same building; windows 'small apertures high up in the walls'; flat roofs where booths of ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'House'.  
   Quotes: smiths_bible_dictionary.txt @ 1035143; smiths_bible_dictionary.txt @ 1035459; smiths_bible_dictionary.txt @ 1035639; smiths_bible_dictionary.txt @ 1035820; smiths_bible_dictionary.txt @ 1036060.
   Caution: Describes village houses of the 19th-century East; the Shiloh of Eli is some three thousand years earlier.
8. [medium] Smith's on roads: in the East 'the eastern roads are more like our paths', and on villages: Arab villages 'are often mere collections of stone huts'.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Road; Village'.  
   Quotes: smiths_bible_dictionary.txt @ 2427037; smiths_bible_dictionary.txt @ 3125715.
   Caution: Dictionary of 1863; general statement, not about Shiloh.

## `life-town-gate`: Living blind, then: a walled town with a gate (Jabesh-gilead, Jericho, Job at the gate)

Items: 8. Coverage: Good for the gate (the 1915 encyclopaedia's entry is full), fair for Jabesh and Jericho, thin for what a blind person did there.

The gate is the public room of the town: most men passed through daily, it was the place for meeting, markets, courts and prophets' speeches (ISBE, Smith's, Easton's), closed at nightfall; streets were narrow, winding and locked at night. Job 29's 'eyes to the blind' is set at the gate; Henry reads it as counsel and says we best help people in the very thing they lack. Jabesh-gilead's elders were offered the loss of every right eye, which Henry says, for men who fought with a shield over the left eye, was in effect blinding them. Jericho has springs, and houses built on its walls (Smith's). Smith's says begging places were at street corners, temple gates and private houses in 'later times'. Josephus says the Jebusites set the blind and lame on the wall as derision; Henry thinks they were invalids or maimed soldiers; the 1915 encyclopaedia reads it as a mocking phrase.

1. [high] The 1915 encyclopaedia on the gate: 'most of the men passed through the gate every day, and the gate was the place for meeting others and for assemblages'; open places near it were 'the centers of the public life', markets were ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Gate', vol 2, p. 1170.  
   Quotes: isbe_1915_vol2.txt @ 4338900; isbe_1915_vol2.txt @ 4339477.
2. [medium] Smith's on the gate: it was a place for public deliberation and justice and for markets, and gates 'were carefully guarded, and closed at nightfall'. Easton's adds that courts were 'frequently held' at the gates of cities, and ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Gate'; Easton's Bible Dictionary (1897), entry 'Gate'; International Standard Bible Encyclopaedia (1915), entry 'Jerusalem', vol 3, p. 1614.  
   Quotes: smiths_bible_dictionary.txt @ 823642; smiths_bible_dictionary.txt @ 823841; smiths_bible_dictionary.txt @ 824031; easton_ebd.txt @ 1156544; easton_ebd.txt @ 1156715; isbe_1915_vol3.txt @ 2018440; isbe_1915_vol3.txt @ 2018601.
   Caution: The Jerusalem quotation is the 1915 writer's inference about the pre-Davidic city, not a statement about Israelite towns generally; the OCR has the page's side-headings run into the sentence ('3. Site of ... the Jebu-').
3. [medium] Wikipedia's article on city gates: they were built 'to provide a point of controlled access to and departure from a walled city for people, vehicles, goods and animals', and also displayed public information such as announcements ...  
   Source: Wikipedia, 'City gate', revision of 27 September 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_City_gate.wiki.txt @ 596; wikipedia_City_gate.wiki.txt @ 956.
   Caution: A general article on city gates in many countries and periods; only the opening description is used.
4. [high] Henry on Job 29: Job's 'I was eyes to the blind' comes within a passage about the gate, the 'place of judgment', where 'judgment was administered in the gate, in the street, in the places of concourse, to which every man might ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Job 29.  
   Quotes: matthew_henry_vol3.txt @ 942222; matthew_henry_vol3.txt @ 950629; matthew_henry_vol3.txt @ 950857.
   Caution: Henry reads 'the blind' figuratively (people without direction) and does not discuss a person who cannot see.
5. [medium] Henry on 1 Samuel 11: the Ammonite king offered the men of Jabesh-gilead a covenant if they would 'thrust out all your right eyes'. Henry explains the purpose: to disable them for war, because soldiers fought with shields in the ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 1 Samuel 11; Wikipedia, 'Jabesh-Gilead', revision of 15 July 2026 (CC BY-SA 4.0); Smith's Bible Dictionary (1884 edition), entry 'Jabesh'.  
   Quotes: matthew_henry_vol2.txt @ 1927810; matthew_henry_vol2.txt @ 1928061; wikipedia_Jabesh-Gilead.wiki.txt @ 3867.
   Caution: Henry's explanation of the military reason is his own; the text says only that it was to be 'a reproach upon all Israel'.
6. [high] Smith's on Jericho: its walls 'were so considerable that houses were built upon them'; Wikipedia says 'copious springs in and around the city have attracted human habitation for thousands of years'.  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Jericho'; Wikipedia, 'Jericho', revision of 23 September 2026 (CC BY-SA 4.0).  
   Quotes: smiths_bible_dictionary.txt @ 1197951; wikipedia_Jericho.wiki.txt @ 6319.
7. [medium] Smith's on the street and the beggar's place: streets of an eastern town are 'generally narrow, tortuous and gloomy' and each street 'is locked up at night'; beggars 'were accustomed, it would seem, to have a fixed place at the ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Street'; Smith's Bible Dictionary (1884 edition), entry 'Beggar, Begging'.  
   Quotes: smiths_bible_dictionary.txt @ 2799297; smiths_bible_dictionary.txt @ 2800652; smiths_bible_dictionary.txt @ 326673.
   Caution: Smith's describes 'a modern Oriental town' of 1863 for the first quotation; the second is about 'later times', meaning New Testament times, not Job's or Jabesh's.
8. [medium] Josephus on the Jebusite walls: the inhabitants 'shut their gates, and placed the blind, and the lame, and all their maimed persons, upon the wall, in way of derision of the king'. Henry's alternative is that the blind and lame ...  
   Source: Josephus, Antiquities of the Jews (Whiston translation), Book VII, chapter 3, section 1; Matthew Henry, Commentary on the Whole Bible (1706-1721), on 2 Samuel 5; International Standard Bible Encyclopaedia (1915), entry 'Jerusalem', vol 3, p. 1614.  
   Quotes: josephus_antiquities_pg2848.txt @ 950769; matthew_henry_vol2.txt @ 2667413; isbe_1915_vol3.txt @ 2019477.
   Caution: This is a contested verse; the sources do not agree on whether real blind people were on the wall. Josephus is a late retelling.

## `life-jerusalem`: Living blind, then: first-century Jerusalem

Items: 8. Coverage: Rich on the Temple's steps and crowds, begging places and charity. Thin on housing and on the streets of the city itself.

Edersheim thinks the man born blind of John 9 sat at the entrance to the Temple 'as objects of pity' did, probably calling 'Gain merit by me'. Smith's and the 1915 encyclopaedia both name the begging places: street corners, rich men's doors, the Temple gates, and the entrance to Jericho, a gateway for festival pilgrims. The encyclopaedia gives causes: no adequate relief, no medical science for eye disease like ophthalmia, and Roman taxes. Edersheim says alms were collected every week in money or food, two collecting and three distributing. For movement: fifteen (Edersheim) or fourteen (Josephus) steps up to the inner court, a Pool of Siloam stair of 34 steps, 'wide, stepped roads' for crowds (Wikipedia), valleys 'every where unpassable', an ascent 'perpetual' from three sides, and the Jericho road 'rough ... winding over rock and loose stones'. The crowd at Passover is estimated at 300,000 to 400,000 (Wikipedia) or 'three millions' (Josephus).

1. [medium] Edersheim on where the man born blind of John 9 probably sat: the entrance to the Temple 'was then ... the chosen spot for those who, as objects of pity, solicited charity', and he thinks the miracle took place at the entering to ...  
   Source: Edersheim, The Life and Times of Jesus the Messiah (1883), Book IV, chapter IX.  
   Quotes: edersheim_life_and_times.txt @ 2635977; edersheim_life_and_times.txt @ 2637150.
   Caution: Edersheim says 'presumably' and 'we can scarcely doubt'; it is his inference, not stated in John. 'Objects of pity' is his phrase.
2. [medium] Smith's on begging places: 'in later times beggars were accustomed ... to have a fixed place at the corners of the streets, ... or at the gates of the temple, or of private houses' (Mark 10:46, Acts 3:2, Luke 16:20). Smith's also ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Beggar, Begging'.  
   Quotes: smiths_bible_dictionary.txt @ 326448; smiths_bible_dictionary.txt @ 326554; smiths_bible_dictionary.txt @ 326673.
   Caution: 'Abhorred as a vagabond' is Smith's gloss on Psalm 109:10 and describes the Old Testament view of the wicked's children, not the blind. Care or containment: the sources describe the places but do not say who chose them.
3. [high] The 1915 encyclopaedia (article 'Begging', by Geo. B. Eager) says begging grew with the larger cities, that 'beggars formed a considerable class in the gospel age', and names the places: the entrance to Jericho, 'a gateway to ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Beg, Beggar, Begging', vol 1, pp. 425-426.  
   Quotes: isbe_1915_vol1.txt @ 3476422; isbe_1915_vol1.txt @ 3478674; isbe_1915_vol1.txt @ 3479072; isbe_1915_vol1.txt @ 3479295; isbe_1915_vol1.txt @ 3479567.
   Caution: The same entry goes on to describe modern European Jewish beggars in language that is prejudiced; none of that is used here.
4. [medium] Edersheim on charity in the Jewish towns: 'Alms were collected at regular times every week, either in money or in victuals', two people collecting and three distributing, 'so as to avoid the suspicion of dishonesty or ...  
   Source: Edersheim, Sketches of Jewish Social Life (1876), chapters 4 and 18.  
   Quotes: edersheim_sketches.txt @ 509231; edersheim_sketches.txt @ 88089.
   Caution: Rabbinic sources written down after the New Testament; Edersheim writes that 'such collectors' were not employed in every synagogue.
5. [medium] Steps and courts of the Temple. Edersheim: 'Fifteen steps led up to the Upper Court' from the Court of the Women, where the Nicanor Gate was; Josephus: the second court 'was ascended to by fourteen steps from the first court', ...  
   Source: Edersheim, The Life and Times of Jesus the Messiah (1883), Book II chapter X, Book IV chapter VI and Book V chapter III; Josephus, The Wars of the Jews (Whiston translation), Book V, chapter 5, section 2; Easton's Bible Dictionary (1897), entry 'Gate'.  
   Quotes: edersheim_life_and_times.txt @ 798196; josephus_wars_pg2850.txt @ 921345; edersheim_life_and_times.txt @ 2553504; edersheim_life_and_times.txt @ 3233154.
   Caution: The two accounts disagree on the number of steps (fifteen, fourteen); both describe the Temple before AD 70. Edersheim's layout is a reconstruction from rabbinic and Josephus sources, and the exact position of the 'Beautiful Gate' was disputed.
6. [medium] Pool and stair. Wikipedia says archaeologists in the 1880s found 'a stairway of 34 rock-hewn steps to the west of the Pool of Siloam leading up from a court in front of the Pool', and that the pool 'would have been a major ...  
   Source: Wikipedia, 'Pool of Siloam', revision of 20 June 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_Pool_of_Siloam.wiki.txt @ 9362; wikipedia_Pool_of_Siloam.wiki.txt @ 6707.
   Caution: The stair is described from 19th-century excavation of a pool that was rebuilt in the Roman era; its date is not given in these sentences.
7. [medium] Crowds and stepped approaches. Wikipedia says the Hasmoneans 'built wide, stepped roads designed to control the massive crowds and guide them smoothly toward the Temple gates', and that at Passover Jerusalem was packed with ...  
   Source: Wikipedia, 'Second Temple', revision of 19 September 2026 (CC BY-SA 4.0); Josephus, The Wars of the Jews (Whiston translation), Book II, chapter 14, section 3.  
   Quotes: wikipedia_Second_Temple.wiki.txt @ 20989; wikipedia_Second_Temple.wiki.txt @ 39226; josephus_wars_pg2850.txt @ 400765.
   Caution: The crowd numbers disagree by a factor of ten and are estimates; Josephus's are probably exaggerated.
8. [medium] Roads, terrain and the sound of crowds. Smith's quotes Dean Stanley that Jerusalem's ascent from any side but the south is 'perpetual'; Josephus says the hills around are 'surrounded by deep valleys' that are 'every where ...  
   Source: Smith's Bible Dictionary (1884 edition), entry 'Jerusalem'; Josephus, The Wars of the Jews (Whiston translation), Book V, chapter 4, section 1; Edersheim, The Life and Times of Jesus the Messiah (1883), Book V chapter I and Book IV chapter XXIV.  
   Quotes: smiths_bible_dictionary.txt @ 1207861; josephus_wars_pg2850.txt @ 907721; edersheim_life_and_times.txt @ 3175838; edersheim_life_and_times.txt @ 3151536.
   Caution: Edersheim describes the road as a traveller saw it in the 19th century and applies it to Jesus's last journey; his Jericho sentence is a retelling of Luke 18:36-37 with the sounds added, and the verses do not say who told the blind men.

## `walk-by-faith`: 2 Corinthians 5:7 in its context

Items: 6. Coverage: Good from Henry; ISBE on faith helps. The shelf does not link the verse to blindness and does not say what eidos means in this verse.

Henry places the verse in Paul's argument for why they did not faint under afflictions, and reads it: 'Faith is for this world, and sight is reserved for the other world', so we walk by faith 'till we come to live by sight'. His 'sight' is the vision of God after death, not eyesight, and he treats believers as 'pilgrims and strangers'. The 1915 encyclopaedia says faith in the New Testament mostly means reliance or trust and, on Hebrews 11:1, is 'simply reliance upon a God known to be trustworthy'; it lists 2 Corinthians 5:7 under figurative 'walk'. Easton's gives the same basic sense, trust. For the Greek word eidos in the verse, the shelf has only general glosses ('thing seen', 'external appearance').

1. [high] Matthew Henry on 2 Corinthians 5:7: 'We have not the vision and fruition of God, as of an object that is present with us ... Faith is for this world, and sight is reserved for the other world: and it is our duty, and will be our ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 2 Corinthians 5:7.  
   Quotes: matthew_henry_vol6.txt @ 3645737; matthew_henry_vol6.txt @ 3645576.
   Caution: Henry's 'sight' means the vision of God, not physical sight; he does not discuss blindness here. His 'opening our eyes in a world of glory' language is his picture of death and is not used.
2. [medium] Henry sets the verse in Paul's argument: the chapter gives reasons they did not faint under afflictions, namely their 'expectation, desire, and assurance of happiness after death'. Believers, he says, 'are pilgrims and strangers ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 2 Corinthians 5.  
   Quotes: matthew_henry_vol6.txt @ 3637856; matthew_henry_vol6.txt @ 3645213; matthew_henry_vol6.txt @ 3646881.
   Caution: Henry reads the passage mostly as about death and the life to come; the letter's wider context (afflictions, the 'earthly tent') is the part that speaks of weakness.
3. [medium] The 1915 encyclopaedia on faith: pistis in the New Testament normally means 'reliance', 'trust'. On Hebrews 11:1 it denies that faith is 'a faculty of second sight' and says the faith of Abraham, Moses and Rahab 'was simply ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Faith', vol 2, pp. 1087-1088.  
   Quotes: isbe_1915_vol2.txt @ 3593412; isbe_1915_vol2.txt @ 3595584; isbe_1915_vol2.txt @ 3595874.
   Caution: The entry explains Hebrews 11:1; it does not discuss 2 Corinthians 5:7. The OCR reads 'Cod' for 'God'.
4. [high] Easton's dictionary: faith's 'primary idea is trust. A thing is true, and therefore worthy of trust.'  
   Source: Easton's Bible Dictionary (1897), entry 'Faith'.  
   Quotes: easton_ebd.txt @ 1044899.
5. [high] The 1915 encyclopaedia's entry 'Walk' lists 2 Corinthians 5:7 under the figurative use of 'walk' for 'conduct and of spiritual states', next to 'walk in the light', 'walk in newness of life' and 'walk by the Spirit'.  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Walk', vol 5.  
   Quotes: isbe_1915_vol5.txt @ 2085935; isbe_1915_vol5.txt @ 2086629.
6. [medium] On the word for 'sight': the 1915 encyclopaedia glosses the Greek eidos as 'thing seen', 'external appearance', 'shape' and, in its entry 'Appearance', gives 'eidos = "sight"' for a verse in 1 Thessalonians. Neither entry ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Fashion', vol 2, p. 1099; International Standard Bible Encyclopaedia (1915), entry 'Appearance', vol 1.  
   Quotes: isbe_1915_vol2.txt @ 3692549; isbe_1915_vol1.txt @ 1784207.
   Caution: The shelf does not tell us what eidos means in 2 Corinthians 5:7. These are general glosses of the word elsewhere; the OCR prints the 1 Thessalonians reference as '6 22' for 5:22.

## `law-as-evidence`: A law as evidence of a problem; how neighbouring peoples treated the blind

Items: 10. Coverage: Little. The commentators and dictionaries reason about purpose, not about what the laws show of practice. What exists: Henry on what each law was meant to prevent, the sources on neighbours' warfare, and Wikipedia and the 1915 encyclopaedia on the Code of Hammurabi.

Brian's idea is that a law is evidence of a problem. The shelf gives two kinds of evidence against reading it too quickly. First, Henry says the Jewish writers found it impossible that anyone would literally put a stumbling-block before the blind, so read the law as about bad advice. Second, scholars of the Babylonian Code disagree about whether it was legislation, a record of cases, or a work of jurisprudence (Wikipedia), and its laws are all 'if ... then' cases, whereas Leviticus 19:14 is a general command. For the servant law, Henry's wording of the purpose ('to comfort them if they were abused') assumes the thing happened. The curses of Deuteronomy 27, Henry says, include wrongs the magistrate could not see. For practice: the priestly blemish rule was used in the first century BC (Josephus). The Old Testament is said to have no word for begging, though NT-era Jerusalem had begging places. For neighbours: Ammonites proposed taking every right eye in Jabesh; Easton's says conquerors blinded captives; the Jebusites placed the blind and lame on the wall; Greek stories give blindness as punishment and compensation (myth). Nothing on the shelf describes how a neighbouring people treated blind people day to day.

1. [high] Henry says the Jewish writers thought it impossible that anyone would be 'so barbarous as to put a stumbling-block in the way of the blind', and so read Leviticus 19:14 as a figure for giving bad advice. That is a reading in ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Leviticus 19.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2978430.
   Caution: Henry reports this; the shelf does not say who the 'Jewish writers' were or how early.
2. [medium] Henry on the servant's law: it was intended 'to prevent their being abused' and 'to comfort them if they were abused'. The second purpose assumes abuse happened; the first assumes masters could be deterred.  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Exodus 21.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2127262; matthew_henry_vol1_genesis_to_deuteronomy.txt @ 2127418.
   Caution: This is Henry's reading of purpose; it is an argument from the law's wording, not evidence from a case.
3. [medium] Henry on the curses of Deuteronomy 27 says that some of them cover wrongs a magistrate 'could not take cognizance of', which God, 'who knows the heart', judges. The curse on those who make the blind wander is in the same list, ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on Deuteronomy 27.  
   Quotes: matthew_henry_vol1_genesis_to_deuteronomy.txt @ 4750797.
   Caution: Henry says this about the curse on contempt of parents (verse 16), not about the blind; the use here is by analogy and is the writer's.
4. [high] What neighbouring peoples did: Henry on 1 Samuel 11:2 says the Ammonites asked for the right eye of every man in Jabesh-gilead and explains that 'a soldier without his right eye was in effect blind'. Easton's says 'Conquerors ...  
   Source: Matthew Henry, Commentary on the Whole Bible (1706-1721), on 1 Samuel 11; Easton's Bible Dictionary (1897), entry 'Blind'; Smith's Bible Dictionary (1884 edition), entry 'Blindness'.  
   Quotes: matthew_henry_vol2.txt @ 1928061; easton_ebd.txt @ 420406; smiths_bible_dictionary.txt @ 383094.
   Caution: Evidence for neighbours' warfare, not for how they treated blind people in daily life.
5. [high] Hammurabi's Code and Moses: the 1915 encyclopaedia (A. Ungnad) says the parallels between Exodus and the Code are not accidental, 'but just as little could one say that they are directly taken from the Code', and that 'numerous ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Hammurabi', vol 2, p. 1332.  
   Quotes: isbe_1915_vol2.txt @ 5660744; isbe_1915_vol2.txt @ 5660188.
   Caution: A 1915 scholar's view; later scholarship has revised dating and relationships and none of that is on the shelf.
6. [medium] Wikipedia on what the Babylonian Code was: scholars have disputed whether it was legislation, a 'law report' of past cases, or 'an abstract work of jurisprudence', the last having 'gained much support within Assyriology'. It also ...  
   Source: Wikipedia, 'Code of Hammurabi', revision of 2 October 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_Code_of_Hammurabi.wiki.txt @ 31216; wikipedia_Code_of_Hammurabi.wiki.txt @ 31478; wikipedia_Code_of_Hammurabi.wiki.txt @ 34300.
   Caution: If the Code is a scholarly work and not enforced legislation, then its sections are weaker evidence of Babylonian practice than once thought. Wikipedia presents this as a debate.
7. [medium] The 1915 encyclopaedia's entry 'Beg, Beggar, Begging' opens by saying it is significant that the Mosaic law 'contains no enactment concerning beggars, or begging', and that this omission 'certainly is not accidental'. It adds ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Beg, Beggar, Begging', vol 1, p. 425; Easton's Bible Dictionary (1897), entry 'Beg'.  
   Quotes: isbe_1915_vol1.txt @ 3475391; isbe_1915_vol1.txt @ 3475845; isbe_1915_vol1.txt @ 3476422; easton_ebd.txt @ 367585.
   Caution: Both entries are from 1897-1915; they argue from the absence of a law or a word, which is a weak sort of proof.
8. [medium] The same entry says the Mosaic provisions 'as far as actually practised, have always virtually done away with beggars and begging among the Jews', and that the spirit of the law is shown in the rule against driving a beggar away ...  
   Source: International Standard Bible Encyclopaedia (1915), entry 'Beg, Beggar, Begging', vol 1, p. 425.  
   Quotes: isbe_1915_vol1.txt @ 3476287; isbe_1915_vol1.txt @ 3478558.
   Caution: 'Always virtually' is more than a 1915 encyclopaedia could know, and the entry itself later records begging among the Jews in the gospel age.
9. [medium] The Talmud, as described by Wikipedia, reasoned about the blind within the law: it rejected a literal reading of 'an eye for an eye' partly because it would be 'inapplicable to blind or eyeless offenders', and the Torah 'requires ...  
   Source: Wikipedia, 'Eye for an eye', revision of 2 October 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_Eye_for_an_eye.wiki.txt @ 10408.
   Caution: A late rabbinic argument, summarised by Wikipedia; it shows blind people were a thinkable test case for the law, not how they were treated.
10. [medium] Greek stories, as Wikipedia summarises them: gods inflict blindness as punishment, and 'sometimes, blind people in Greek mythology are granted special abilities by way of compensation', such as prophecy.  
   Source: Wikipedia, 'Cultural depictions of blindness', revision of 13 August 2026 (CC BY-SA 4.0).  
   Quotes: wikipedia_Cultural_depictions_of_blindness.wiki.txt @ 5266.
   Caution: Myth is not evidence of practice. The shelf has nothing on how any neighbouring people actually treated blind persons.

## What the shelf cannot tell us

The shelf is nineteenth- and early twentieth-century reference works, an eighteenth-century commentary, Josephus and Wikipedia. It has no archaeology of ordinary houses after about 1900, no modern study of disability in the Bible, no recent edition of the Mesopotamian laws, and no modern commentary on 2 Corinthians. Specifically:

- Anything about how a blind person actually got about, worked or was fed in a camp, village, gate or city. The sources describe the setting and the begging places; the connection to blind people is the reader's.
- Whether the begging places were chosen by the blind, by their families or by the town (care or containment). The sources name the places and the causes of begging; none says who decided.
- Whether the Hebrew laws about the blind answered a common wrong or a rare one. Henry reports that Jewish writers thought the literal act unthinkable; that is the only direct evidence.
- How Israel's neighbours treated blind people. Only warfare (blinding captives) and a taunt on a wall are on the shelf.
- What 'sight' (eidos) means in 2 Corinthians 5:7 and how the verse's context (a body as an 'earthly tent') relates to bodily weakness.

These modern works might help. They are listed from the writer's general knowledge, not from the shelf and not quoted; check the details before citing any of them. Brian can decide whether to consult them.

- Disability in the Hebrew Bible: Interpreting Mental and Physical Differences, Saul M. Olyan, 2008.
- Disability Studies and the Hebrew Bible: Figuring Mephibosheth in the David Story, Jeremy Schipper, 2006.
- Biblical Corpora: Representations of Disability in Hebrew Biblical Literature, Rebecca Raphael, 2008.
- This Abled Body: Rethinking Disabilities in Biblical Studies (edited volume), Hector Avalos, Sarah J. Melcher and Jeremy Schipper (eds.), 2007.
- Disability Studies and Biblical Literature (edited volume), Candida R. Moss and Jeremy Schipper (eds.), 2011.
- Judaism and Disability: Portrayals in Ancient Texts from the Tanach through the Bavli, Judith Z. Abrams, 1998.
- Disability in Antiquity (edited volume), Christian Laes (ed.), 2017.
- Law Collections from Mesopotamia and Asia Minor, Martha T. Roth, 1995 (2nd ed. 1997).
- A History of Ancient Near Eastern Law (edited volume), Raymond Westbrook (ed.), 2003.
- King Hammurabi of Babylon: A Biography, Marc Van De Mieroop, 2005.
- Leviticus 17-22 (Anchor Bible), Jacob Milgrom, 2000.
- Leviticus (JPS Torah Commentary), Baruch A. Levine, 1989.
- Life in Biblical Israel, Philip J. King and Lawrence E. Stager, 2001.
- Daily Life in Biblical Times, Oded Borowski, 2003.
- Ancient Israel: Its Life and Institutions, Roland de Vaux, 1961 (English).
- Jerusalem in the Time of Jesus, Joachim Jeremias, 1969 (English).
- Poverty and Charity in Roman Palestine, First Three Centuries CE, Gildas Hamel, 1990.
- The Second Epistle to the Corinthians (New International Greek Testament Commentary), Murray J. Harris, 2005.
- The Second Epistle to the Corinthians (New International Commentary on the New Testament), Paul Barnett, 1997.
- II Corinthians (Anchor Bible), Victor Paul Furnish, 1984.

