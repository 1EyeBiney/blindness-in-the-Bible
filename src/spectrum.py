"""What this site means by "blind": the spectrum of blindness, explained early for sighted readers.

Brian's swimming-pool picture is his (docs/BRIAN_NOTES.md, 6 October 2026), edited into page form
in his voice. The verse quotations are the Berean Standard Bible, checked word for word by the tests.
"""

TITLE = "What blind means here"
SLUG = "what-blind-means.html"

# verse references the page quotes; build_site pulls the text from the official BSB
VERSES = [("Genesis", 27, 1), ("Genesis", 48, 10), ("1 Kings", 14, 4), ("Mark", 8, 24)]

BODY = """<h1>What blind means here</h1>
<p class="lede">Most readers picture one thing when they read the word blind: no sight at all. That is the
picture the Bible's writers seem to have had too, and it is the picture most of this site works from. But
blindness in real life is a range, and this page is here to say so before you read anything else.</p>

<h2>The swimming pool</h2>
<p>From Brian: I tell people that blindness is kind of like a swimming pool, with people scattered all
through it. Some are just dipping their toes in the water. Those are the people who need reading glasses.
Some are in the shallow end and need corrective lenses to get through the day. Some are in the deep end,
and that is where I am. It is all right, though. There is plenty of room to swim about, because fewer than one in ten
of the people the world counts as blind have no sight at all. I have read a good many studies on that number
and they do not agree, but none that I would trust puts it above ten percent. And we are all still in the pool
together.</p>
<p>In my own blind community, many people do not need to feel along a wall to get around outside. Plenty
of low-vision people do not grope about the way I would have to without my cane. They may read large print,
or see shapes and light, or see well in daylight and nothing at dusk. Their hardships are just as real as
mine. They are simply different hardships, and a sighted reader who has only met blindness in books may not
know that.</p>

<h2>What the Bible means by it</h2>
<p>As best we can tell, when Scripture calls a person blind it means total blindness. The blind man in
John 9 had never seen. Bartimaeus asks to see again. The healed men see faces and trees. The law pairs the
blind with the lame, people who could not do the thing at all. Nothing in the text pictures someone who
reads with difficulty or sees only in good light. That is why the studies on this site generally assume the
blind person sees nothing, and why the "In their shoes" sections are written from Brian's own experience of
total blindness.</p>
<p>But the Bible does describe the shallower end of the pool. It just does not use the word blind for it.
Three old men are said to have eyes grown dim or weak, and one of them, Jacob, is plainly described as still
seeing a little:</p>
{verses}
<p>So Isaac, Jacob, Eli and Ahijah may well have had some remaining sight, and the pages about them say so
where it matters. Isaac tells his sons apart by voice and touch, not by looking. Jacob crosses his hands
on Joseph's sons knowingly. Eli knows Samuel by his voice. Ahijah is warned by God who is at the door, which
he would not have needed if he could see her face. The one place where the Bible shows us a man partway into
sight is the man at Bethsaida, who in the middle of his healing sees people as walking trees. That is a fair
description of what some low-vision people see every day.</p>

<h2>Why it matters for reading this site</h2>
<ul>
<li>When a page says "a blind person could not have done this," read it as "a person with no sight." Many
blind people today could.</li>
<li>When a page imagines feeling the way along a wall or counting steps, that is the deep end of the pool.
It is Brian's end, and it is the end the Bible's writers had in mind, but it is not everyone's.</li>
<li>When Scripture uses blindness as a picture of ignorance or hardness, it is drawing on total blindness,
and the <a href="picture/index.html">picture pages</a> read it that way.</li>
<li>If you meet a blind person after reading this site, do not assume you know how much they see. Ask, or
better, let them tell you.</li>
</ul>

<h2>Brian's words</h2>
<p>I was treating blindness as most readers do, as total blindness, until this came up, and I am totally
blind myself. It is an easy thing to forget even from inside the pool. Blindness is a visual spectrum, and
nearly everything on this site should be read with that in mind.</p>
"""


def render(bible: dict) -> str:
    from build_site import e
    items = []
    for book, ch, v in VERSES:
        items.append(f'<li><p class="verse"><b>{book} {ch}:{v}</b> {e(bible[(book, ch, v)])}</p></li>')
    return BODY.replace("{verses}", "<ul>\n" + "\n".join(items) + "\n</ul>")
