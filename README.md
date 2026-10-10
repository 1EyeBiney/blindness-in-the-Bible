# Not By Sight

Studies on blindness in the Bible, by Brian Clark. "For we walk by faith, not by sight." (2 Corinthians 5:7)

**Live site: https://blindnessinthebible.com**

A blind reader of the Bible, working with an AI, gathering every verse that speaks of blindness and
reading it with the place, the time and the daily life around it. Everything behind the site is in
this repository, free for anyone to check, reuse or build on.

## The site checks its own quotations

Every verse quoted on the site is compared against the official Berean Standard Bible file as its
publisher released it. Every passage quoted from the shelf of older works is compared against the
exact place in the source file it came from. Both checks run on every build, and **the site will not
publish if a single word has drifted.**

You can run them yourself:

```
git clone https://github.com/1EyeBiney/blindness-in-the-Bible
cd blindness-in-the-Bible
python -m pytest tests
```

Python 3.12 and pytest. Nothing else, and no network once the clone is done.

To rebuild the whole site into a local `site/` folder:

```
python src/build_site.py
```

That is the same command the publish workflow runs, so what you get is what readers get.

## What is here

| Path | What it holds |
|---|---|
| `data/catalog.csv` | Every passage about blindness: reference, text, how it was found, how it is classified, how confident that is |
| `data/raw/berean/` | The official Berean Standard Bible text, with its source record |
| `data/raw/shelf/` | The reference works quoted for place and time, each with its source record |
| `data/reference/` | Gathering notes: candidate passages offered, what was chosen, what was set aside |
| `src/` | The build: catalog, pages, and `build_site.py` |
| `audio/` | Scripts and tools for the *Not By Sight* episodes |
| `docs/` | The concept, Brian's own notes, and the research digests |
| `tests/` | The checks described above |

## If you think something is wrong

Please say so. A mistake nobody reports stays on the page.

This site was built by a blind reader of the Bible working with an AI, not by a scholar, and it says
so plainly. Where a page reads a verse one way and the commentators read it another, the page carries
both and names whose reading is whose. A correction from someone who knows the languages, the history
or the literature is worth more here than anywhere else.

Write to **brian@blindnessinthebible.com** — no GitHub account needed — or open an
[issue](https://github.com/1EyeBiney/blindness-in-the-Bible/issues). The most useful corrections name
the page and quote the sentence.

## Licence

| What | Licence |
|---|---|
| The writing — site pages, stories, reflections, `docs/` | [CC BY 4.0](LICENSE) |
| The code — `src/`, `audio/*.py`, `tests/` | [MIT](LICENSE-CODE) |
| The sources in `data/raw/` | Each keeps its own terms — see [NOTICE](NOTICE) |

The writing may be copied, republished, adapted and sold, as long as you give credit. The sources are
not ours to relicense: the Berean Standard Bible is in the public domain, the old commentaries and
dictionaries are out of copyright, and the Wikipedia articles on the shelf are CC BY-SA, which travels
with them. [NOTICE](NOTICE) sets out every source and its terms.

### How to cite

> Brian Clark, "Not By Sight: studies on blindness in the Bible",
> https://blindnessinthebible.com, accessed *date*.

## More

- [Check our work](https://blindnessinthebible.com/check-our-work.html) — the same ground as this
  README, written for readers of the site.
- [How it was made](https://blindnessinthebible.com/how-it-was-made.html) — the method, the working
  rules, and what went wrong.
- `docs/CONCEPT.md` — the agreed concept and the decisions made so far.
- `docs/BRIAN_NOTES.md` — Brian's own words, used for the personal sections.
