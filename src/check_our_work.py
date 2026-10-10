"""Check our work: how to verify, reuse, rebuild and borrow from this project.

"How it was made" tells the story of the method. This page is the practical
companion: where the data is, how to check a claim, how to run it yourself,
and how to tell us we are wrong.
"""

TITLE = "Check our work"
SLUG = "check-our-work.html"

REPO = "https://github.com/1EyeBiney/blindness-in-the-Bible"

BODY = """<h1>Check our work</h1>
<p class="lede">Everything behind this site is public: the verses, the old books it quotes, the notes on what was
gathered and what was left out, the code that builds the pages, and the tests that check it. Nothing is held back,
and none of it costs anything. If you want to verify a claim, take the data, rebuild the site yourself, or do this
for a subject of your own, this page tells you how.</p>

<h2>The site checks its own quotations</h2>
<p>This is the part worth knowing first, because it is the part you do not have to take on trust.</p>
<p>Every verse quoted anywhere on this site is compared, automatically, against the official Berean Standard Bible
file as its publisher released it. Every passage quoted from the shelf of old books is compared against the exact
place in the source file it was taken from. Both checks run every time the site is built. <b>If a single word had
drifted, the site would not publish.</b></p>
<p>You can run those checks yourself in about a minute, and watch them pass or fail:</p>
<pre><code>git clone https://github.com/1EyeBiney/blindness-in-the-Bible
cd blindness-in-the-Bible
python -m pytest tests</code></pre>
<p>It needs Python 3.12 and pytest, and nothing else. No account, no key, no network once the clone is done.</p>

<h2>Checking a claim without installing anything</h2>
<p>If you only want to know whether one sentence is true, you do not need any of the above.</p>
<ul>
<li><b>Every background paragraph names its source on the page itself.</b> Where a page tells you what Jericho was
like, or how a blind beggar lived, the work it rests on is named underneath.</li>
<li><b>The catalog of every verse is a plain spreadsheet.</b>
<a href="data/catalog.csv">Download the catalog</a> and read it in anything. It lists every passage that speaks of
blindness, how it was found, how it is classified, and how confident that classification is.</li>
<li><b>Each source file carries its own record.</b> In the repository, beside every file on the shelf, is a note
giving the edition, the address it was downloaded from, the date, the licence, and the shape of the file. The
Berean text's record also states the verse count and the number of verses using the word blind, so you can confirm
nothing was trimmed.</li>
<li><b>The gathering notes are kept.</b> What was offered as a candidate passage, what was chosen, and what was
set aside and why, are all written down in the repository rather than thrown away.</li>
</ul>
<p>The whole repository is at <a href="REPO_URL">github.com/1EyeBiney/blindness-in-the-Bible</a>.</p>

<h2>If you think something here is wrong</h2>
<p>Please say so. That is not politeness; a mistake that nobody reports stays on the page.</p>
<p>This site was built by a blind reader of the Bible working with an AI, not by a scholar, and it says so plainly.
Where a page reads a verse one way and the commentators read it another, the page carries both and names whose
reading is whose. A correction from someone who knows the languages, the history or the literature is worth more
here than anywhere else on the site.</p>
<p>Write to <a href="mailto:brian@blindnessinthebible.com">brian@blindnessinthebible.com</a>. You do not need a
GitHub account, and you do not need to be gentle about it. If you would rather raise it in public, or you want to
propose the fix yourself, the <a href="REPO_URL/issues">issue tracker</a> is open.</p>
<p>The most useful corrections name the page and quote the sentence. A misquoted verse, a fact about the place or
the time that is wrong, a reading that misses what the text is doing: all three are welcome.</p>

<h2>Using the material yourself</h2>
<p>The writing on this site is under a Creative Commons Attribution 4.0 licence. You may copy it, republish it,
translate it, read it aloud, print it in a bulletin, build something else on top of it, and you may do all of that
commercially. The one thing asked in return is credit, so that a reader can find their way back to the sources.</p>
<p>The code is under the MIT licence. The sources on the shelf are not ours to give away and keep their own terms:
the Berean Standard Bible is in the public domain, the old commentaries and dictionaries are long out of copyright,
and the Wikipedia articles are under a share-alike licence that travels with them. The repository's
<a href="REPO_URL/blob/main/NOTICE">NOTICE</a> sets out each one.</p>

<h3>How to cite this</h3>
<p>For the site as a whole:</p>
<blockquote><p>Brian Clark, "Not By Sight: studies on blindness in the Bible",
https://blindnessinthebible.com, accessed <i>date</i>.</p></blockquote>
<p>For a single page, add the page's title and its address. For the catalog as data, cite
<code>data/catalog.csv</code> in the repository.</p>

<h2>Rebuilding the site yourself</h2>
<p>The site is plain HTML with no framework, generated from the catalog and the page modules by one script. After
the clone above:</p>
<pre><code>python src/build_site.py</code></pre>
<p>That writes the whole site into a <code>site</code> folder, which you can open from disk. It is the same command
the server runs on every publish, so what you get is what readers get.</p>

<h2>Doing this for a subject of your own</h2>
<p>If you want to work the way this project worked, <a href="how-it-was-made.html">How it was made</a> is the honest
account, including what went wrong. The rules that mattered most, in order:</p>
<ul>
<li><b>Quote the source word for word, and test that you did.</b> An automatic check against the publisher's own
file is what turns a claim into something a stranger can verify.</li>
<li><b>Keep gathering apart from judging.</b> One pass collects candidate passages with verbatim quotes and records
where each came from. A second pass chooses among them and writes down what it rejected. Doing both at once is how
a quotation quietly becomes a paraphrase.</li>
<li><b>Record provenance beside the file, not in your head.</b> Edition, address, date, licence, and the shape of
the file. A year later, that note is the difference between evidence and a rumour.</li>
<li><b>Read old books with their age in mind.</b> Use them for what their authors knew, not for what they assumed
about people.</li>
<li><b>Keep the human judgments human.</b> Which questions matter, what the work is for, what it may and may not
claim: those were not delegated.</li>
<li><b>Say what you are not.</b> The fastest way to lose a reader's trust is to claim an authority you do not
have.</li>
</ul>
"""

BODY = BODY.replace("REPO_URL", REPO)
