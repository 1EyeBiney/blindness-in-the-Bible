"""How this site was made: the method, written for readers of the site."""

TITLE = "How it was made"
SLUG = "how-it-was-made.html"

BODY = """<h1>How it was made</h1>
<p class="lede">One blind Christian with the questions and the life experience. One AI with the tools and a
shelf of old books. A few days of work, in October 2026. This page is about how that went, because the method
matters as much as the pages it produced.</p>

<h2>The division of labor</h2>
<p>Brian brought the questions and the experience. He has been blind since 2014, and he knows what
it is to find a grocery store five blocks away without sight, to tell a wife's footsteps from a stranger's, to
cook at a stove and keep well away from an open fire. Every "In their shoes" section on this site is checked
against that experience, and several were corrected by it. He also made the judgment calls: which stories to
tell, what the site is for, what it may and may not claim, and what he believes. Claude, an AI model made by
Anthropic, did the building: finding the verses, gathering and reading the reference works, drafting the pages,
writing the code that assembles them, and testing all of it. Brian's pastor, John, suggested the section on
blindness as a picture.</p>

<h2>The working rules</h2>
<ul>
<li><b>The Bible is quoted word for word.</b> Every verse on the site is the official Berean Standard Bible text,
downloaded once from its publisher, never retyped. An automated check compares every quoted verse against that file
on every build. If a word were changed, the site would not publish.</li>
<li><b>Every fact about the place and the time names its source.</b> The background paragraphs come from works
in the public domain or under a free licence: Edersheim, Josephus, Matthew Henry, the old Bible dictionaries,
Wikipedia for the archaeology. Each paragraph carries its source. Behind each one, in the repository, is the exact
passage it rests on, with its location in the source file, and a test that the passage is really there.</li>
<li><b>Gathering and judging are kept apart.</b> A smaller AI model read the shelf and gathered candidate passages
with verbatim quotes. The coordinating model then chose, trimmed and worded them, and recorded what it left out and
why. The gathering notes and the editorial decisions are both in the repository.</li>
<li><b>Old books are read with their age in mind.</b> The commentators of 1700 and 1880 wrote about blind people,
and about the Jewish people and teachers of Jesus's day, in ways we would not. Those lines were found, recorded with
their locations, and deliberately left off the pages. The site uses the old books for facts about places, customs
and daily life, not for their opinions of people.</li>
<li><b>Brian's words are his.</b> He writes his thoughts in plain text files as he reviews the pages. Those files are
kept verbatim in the project notes. What appears on the site under "From Brian" is edited for flow in his voice, at
his request, and he reads it afterward.</li>
<li><b>Brian is not a theologian, and the site does not pretend he is.</b> He is a blind reader of the Bible with
a pastor he trusts. Where a page reads a verse one way and the commentators read it another, the page says so and says
whose reading it is. Isaiah 42:16, heard by a blind man as a promise that God will guide him, is one example. The
commentators on the shelf hear it as a promise about souls. The page carries both and calls Brian's what it is: a
blind reader's perspective, not a claim to know better. Blind believers do the same with "we walk by faith, not by
sight," and he knows it.</li>
<li><b>Screen readers first.</b> Every page has one heading at the top, headings in order, a skip link, real tables
with headers, no scripts, and nothing said only in a picture. Where images come, every one will carry a description,
and the words will never depend on it. The author uses a screen reader, so the site is tested the way its first
reader will read it.</li>
<li><b>Ask before acting.</b> Publishing, creating the repository, downloading each new source: all waited for
Brian's go-ahead, and each source's licence was checked before it was fetched.</li>
</ul>

<h2>How the work flowed</h2>
<p>It began with a concept, written down before anything was built: who the site is for, which Bible, where to
start. Then a catalog of every verse that speaks of blindness, found first by searching for the word and then by
reading for the people the word is never used of. Then the stories, because Brian wanted the story behind each verse
and a way to put readers into the shoes of the blind people in them. Then, at his request, the shelf of old books,
so that each story could carry the place and the time the way his pastor teaches. Then the law, read as evidence of
how blind people were treated, and the pages on living blind in each kind of place, with his own answers. Then the
figurative verses, read plainly. Then, late and after a correction from Brian himself, the page on what blind
means, because the whole site had been quietly assuming total blindness.</p>

<h2>What was harder than expected</h2>
<p>Not the Bible. The verses are few and well known. The hard part was the shelf: finding editions that were truly in
the public domain, getting the text in a form a program could search, and keeping each quoted passage traceable to
an exact place in a file that would not shift. One early mismatch came from nothing more than the way Windows and
Linux end their lines. Harder still was the discipline of reading the old commentators for what they knew and not
for what they assumed.</p>

<h2>What was easier than expected</h2>
<p>Finding that the Bible itself is careful where its readers are not. The word blind never falls on a blind
person in the figurative verses. The law protects the blind by name when no older code on the shelf does. The
stories describe dim eyes and a man who sees people as walking trees, which is the spectrum of blindness, two
thousand years before anyone drew a chart of it.</p>

<h2>Everything is open</h2>
<p>The code, the catalog, the gathering notes, the editorial decisions, the tests and the shelf are all public, and
free for anyone to use. <a href="check-our-work.html">Check our work</a> is the practical guide: how to verify a
claim, take the data, rebuild the site yourself, and where to write if you think something here is wrong.</p>
"""
