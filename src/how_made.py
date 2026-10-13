"""How this site was made: the method, written for readers of the site."""

TITLE = "How it was made"
SLUG = "how-it-was-made.html"

BODY = """<h1>How it was made</h1>
<p class="lede">One blind Christian with the questions and the life experience. One AI with the tools and a
shelf of old books. The work began in October 2026. First the pages, then episodes to listen to, then
pictures. This page is about how that went, because the method matters as much as what it produced.</p>

<h2>The division of labor</h2>
<p>Brian brought the questions and the experience. He has been blind since 2014, and he knows what
it is to find a grocery store five blocks away without sight, to tell a wife's footsteps from a stranger's, to
cook at a stove and keep well away from an open fire. Every "In their shoes" section on this site is checked
against that experience, and several were corrected by it. He also made the judgment calls: which stories to
tell, what the site is for, what it may and may not claim, and what he believes. Claude, an AI model made by
Anthropic, did the building: finding the verses, gathering and reading the reference works, drafting the pages,
writing the code that assembles them, and testing all of it. Brian's pastor, John, suggested the section on
blindness as a picture.</p>
<p>When the site grew episodes and pictures, the division stayed the same and other tools joined. The voices and
sound effects come from ElevenLabs. The music is Brian's own, made with Suno. The paintings were made with Google
Gemini. Brian mixes every episode himself, by ear, in an audio program called Reaper.
The episodes are hosted on his YouTube channel.</p>

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
with headers, and nothing said only in a picture. Every picture carries a description, and the words never depend
on it. The one script on the site runs the panel for text size and colours, and the pages read the same with it
switched off. The author uses a screen reader, so the site is tested the way its first reader will read it. The
<a href="accessibility.html">accessibility page</a> has the details.</li>
<li><b>Imagined things are called imagined.</b> The Bible says very little about what a blind man heard or felt on
the way to the pool. The episodes fill some of that in, and every such scene begins with the word imagine. The
paintings are the same. Each page says its pictures are paintings, not records.</li>
<li><b>A machine's voice is called a machine's voice.</b> Brian chose not to record his own words. A voice he picked
speaks them, and each episode says so before it does. Around here that voice is called Mister Scaredy Cat.</li>
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
means, because the whole site had been quietly assuming total blindness. Then the episodes, because a study
of blindness that could only be read had left out the people it was for. Then the settings for low-vision readers.
Last of all the pictures, for sighted visitors, added only once the words could stand without them.</p>

<h2>How an episode is made</h2>
<p>Some people in Brian's church find reading hard. A site about blindness that could only be read was missing
the point, so the stories became episodes of about twenty minutes each, made for listening first.</p>
<ol>
<li><b>The script.</b> Claude drafts it from the story page: the passage, the place and the time from the shelf,
an imagined scene or two, and a draft of Brian's sections. Brian then edits the script by hand, and his sections
are his.</li>
<li><b>The Scripture.</b> The passage is read word for word in its own voice, so a listener always knows when
they are hearing the Bible and when they are hearing us. A test checks the script against the official text.</li>
<li><b>The voices.</b> Brian chose each one by ear: a narrator, a Scripture reader, a voice for his own words, and
voices for the people in the imagined scenes. Each speaker's lines are made as one piece, because he noticed
that a voice drifted when it was made a line at a time.</li>
<li><b>The mix.</b> Brian lays the voices out in Reaper and adds his music and the sound effects: a crowd on a
road, wind on a hill, water at a pool. This is his work from start to finish.</li>
<li><b>The pictures and captions.</b> A program lines the finished mix up with the script, times each caption
to the sentence being spoken, and places the paintings. The result goes to YouTube with captions for viewers
who are deaf or hard of hearing.</li>
<li><b>The page.</b> The episode goes back onto its story page, first as a plain audio file that plays or
downloads, then as the video.</li>
</ol>
<p>From the fourth episode on, each one also carries a map in words. Distances are given as walking time and
directions as hours on a clock face, the way a blind traveller is given directions today: Jericho is about seven
hours' walk from Jerusalem, at two o'clock.</p>

<h2>How the pictures are made</h2>
<p>The pictures were made by a man who cannot see them. Claude wrote a description of each scene and gave it
to an image tool. Brian saved each result by hand. Claude then looked at every painting against a short list of
rules, and wrote its description for screen readers from what the painting actually shows, not from what was
asked for. Three were sent back. In one, Jacob's arms were not crossed, which is the whole point of that story.
In another, a woman at a doorway had come out looking sinister.</p>
<p>The rules are few. One painted look across the whole site. No faces close up, so nobody has to decide what
Jesus or a blind beggar looked like. No words inside a picture, because words in a picture cannot be enlarged or
read aloud. Nothing frightening, even in the hard stories. And every picture has two pieces of text, a description
of what is in it and a caption that ties it to the story.</p>

<h2>Making it work for low vision</h2>
<p>The site was built for screen readers, and it worked with one from the first day. But most blind people have
some sight, as the page on <a href="what-blind-means.html">what blind means</a> says, and a site that only served
the totally blind would have repeated the mistake it was written to correct. So every page now offers larger text,
several sets of colours including high contrast and low glare, a plainer letter style and wider spacing. Every
colour set is measured by a test, and the site will not publish one that falls short.</p>

<h2>What was harder than expected</h2>
<p>Not the Bible. The verses are few and well known. The hard part was the shelf: finding editions that were truly in
the public domain, getting the text in a form a program could search, and keeping each quoted passage traceable to
an exact place in a file that would not shift. One early mismatch came from nothing more than the way Windows and
Linux end their lines. Harder still was the discipline of reading the old commentators for what they knew and not
for what they assumed.</p>
<p>The episodes brought their own lessons. Twice, rebuilding a script wiped out edits Brian had made by hand,
and he said so plainly. The program now refuses to overwrite a script that holds changes it has not saved. The
first three videos went out with captions that stuck on the screen instead of following the voice, which nobody
caught until afterward. They were left as published, and the fault was fixed for every episode since. A blind
author cannot check a video by watching it, so the checks have to be built into the tools.</p>

<h2>What was easier than expected</h2>
<p>Finding that the Bible itself is careful where its readers are not. The word blind never falls on a blind
person in the figurative verses. The law protects the blind by name when no older code on the shelf does. The
stories describe dim eyes and a man who sees people as walking trees, which is the spectrum of blindness, two
thousand years before anyone drew a chart of it.</p>
<p>The other surprise was how much of the work a blind man could do himself. Choosing voices, editing scripts,
writing music and mixing sound are all work for the ear. The pictures were the only part Brian had to take on
trust, and that is why each one comes with its description.</p>

<h2>Everything is open</h2>
<p>The code, the catalog, the gathering notes, the editorial decisions, the episode scripts, the picture
prompts, the tests and the shelf are all public, and
free for anyone to use. <a href="check-our-work.html">Check our work</a> is the practical guide: how to verify a
claim, take the data, rebuild the site yourself, and where to write if you think something here is wrong.</p>
"""
