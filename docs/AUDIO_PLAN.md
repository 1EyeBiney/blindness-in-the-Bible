# Not By Sight: audio and video plan

Started 7 October 2026 at Brian's request, after reviewing the YouTube channel Beyond the Verses. Brian's
aim: people in his church with reading difficulties should be able to share in what the site has found
without reading it. Audio first; video as a wrapper so sighted viewers stay and YouTube accepts it.

## Decisions (Brian, 7 October 2026)

- Try the recommendations as proposed: audio first, one episode per story page (10 to 15 minutes), three
  kept-apart voices (narrator, Scripture reader, Brian himself), fictional scenes allowed but always marked,
  host on YouTube with a player on each story page and a plain MP3 on the site as well.
- Pilot: the man born blind (John 9).
- Pipeline: labs_pipe (C:\nbs\labs_pipe) for voices and assembly; music, effects and video are added stages.

## What exists now

- `audio/` is a labs_pipe project root: `scripts/man_born_blind_01.txt` (the pilot), `casts/not_by_sight.json`
  (six characters, voice IDs still REPLACE_ME), `cues.json` (labs_pipe's lexicon plus a `plainly` cue for the
  Scripture reader), `config.json` (budget cap 15,000 credits per run).
- `audio/build_script.py` writes the script. Every READER line is pulled from the official Berean file at
  build time. `audio/scripts/man_born_blind_01.md` is the same words laid out for reading.
- `tests/test_audio.py` checks: the script on disk matches the generator; the READER lines are John 9:1-41
  word for word and nothing else; every scene character speaks only after the narrator has said "imagine";
  Brian's lines share more than 85 percent of their words with his words on the site; no unsourced figures
  (the Nigeria percentage, Mike May) are in the audio; every speaker and cue is known; labs_pipe check passes
  apart from the placeholder voice IDs.
- `labs_pipe check` on the pilot: 107 lines, 41 Scripture, 27 narrator, 11 Brian; 11,557 characters; one take
  per line costs about 11,600 credits; two takes about 23,100.

## Rules for every episode

1. Scripture is the Berean Standard Bible, word for word, read by its own voice, never mixed into narration.
2. Scenes are fiction and the narrator says "imagine" before each one. Scene characters never quote Scripture.
3. Brian's words are read by a voice Brian picks (his decision, 7 October 2026, for time's sake). The narrator
   introduces that voice once, with his joke about being too shy. Every BRIAN line and that introduction are
   separate files in `selected/`, so his own recordings can be spliced in later without re-rendering anything.
4. Facts about the place and the time are the ones on the page, with the author named in the narration.
5. Nothing goes into audio that the site cannot source. Figures Brian has not sourced stay off.
6. Everything audible must stand alone. The video layer may add but never carry meaning.

## Steps

1. Brian reads the script (`audio/scripts/man_born_blind_01.md`) and marks changes. Done when he says so.
2. Brian picks voices: `labs_pipe voices sync`, then `voices list --search`, and fills the six IDs in the cast.
3. Draft render, one take: `labs_pipe render scripts/man_born_blind_01.txt --dry-run`, then without
   `--dry-run`; `review man_born_blind/1`; `assemble man_born_blind/1`. Listen end to end.
4. (Later, optional) Brian records his lines. Files go to `selected/man_born_blind/section_1/<id>_brian.mp3`,
   replacing the rendered takes, and the narrator's introduction line is dropped; `assemble` picks it up unchanged.
5. Music and effects stage (new, small): a bed under the narrator, ducked under speech; silence under
   Scripture; footsteps and water for the Siloam scene. ffmpeg filter graph driven by `markers.csv`.
6. Video stage (new): one still per scene from an image model, captions from `markers.csv`, ffmpeg slideshow.
   Every still gets a written description in the episode notes. Brian chooses the casts of images as he did
   for Gridiron Greatness.
7. Publish: YouTube upload (label as AI-assisted where the form asks), MP3 in the repository or a release,
   a "Listen to this story" section on the story page with the YouTube embed and a plain audio element.
   The site test that forbids `<img>` and `<script>` will need to allow the embed and described images.

## Open questions for Brian

- Which ElevenLabs voices for narrator and reader. Male or female narrator?
- Length target: this draft runs about 15 minutes at 150 words per minute. Shorter?
- A music source with a licence we can show (public domain recordings, or a CC BY library), since nothing
  on the shelf covers music.

## Episodes 2 to 6: the healings (drafted overnight, 8 October 2026)

Brian asked for the whole "Sight given by Jesus" group as scripts, 10 to 18 minutes each, drafts only, no
rendering, using my judgment and noting decisions. Decisions:

- Five episodes, not seven (Brian agreed): 2 Bartimaeus; 3 Bethsaida (with the disciples' "having eyes, do you
  not see?" from the same chapter); 4 The ones who followed (Matthew 9's two blind men and Matthew 12's blind
  and mute man); 5 The blind in the crowd (the mountain in Matthew 15 and the Temple in Matthew 21, with
  2 Samuel 5:6-8 read for the saying about the blind and the lame); 6 The answer to John (Luke 7, Isaiah 35 and
  61, Matthew 11), which closes the run by letting Jesus say what the healings were for.
- Extra Scripture read to reach length honestly rather than padding: Mark 8:14-21, Matthew 11:20-24, Matthew
  12:25-28, 2 Samuel 5:6-8, Isaiah 35:4-6 and 61:1. Every READER line is tested against the Berean file.
- One imagined scene per episode, under the Siloam rules: announced, hopeful, by ear and touch, no step
  counting, a guide's arm where one is natural. New scene voices: BARTIMAEUS, VOICE, FRIEND, JOHN, DISCIPLE
  (cast entries added, voice ids REPLACE_ME).
- Brian's sections are DRAFTS written in his voice from what he has told Claude (2014, the cane, Barb's
  footsteps, leading other blind people, being asked through an escort, the spectrum, the drop-off test). They
  are collected in docs/BRIAN_DRAFTS.md and a test refuses any BRIAN line that is not either his words from the
  site or a listed draft. He approves, edits or strikes each before anything renders.
- Episode 6 carries the hardest draft: a blind believer whose eyes have not been opened, and what the signs are
  for. Written carefully, flagged for his judgment above all the others.
- Generator split into audio/episode_lib.py (shared rules), audio/episodes/epNN_*.py (one per episode),
  audio/build_episodes.py (writes scripts and the drafts file); tests/test_episodes.py runs the rules over every
  episode. Episode 1 keeps its own builder for now.
- Place-and-time: a Sonnet subagent gathered new shelf quotes into data/reference/episode_candidates.json; the
  scripts use what the story pages already carried plus that material where it checked out.

## State at the end of 11 October 2026

Published: episodes 1 (y-fccElFytM), 2 (zzAgXrX9NEM), 3 (M_LW64UXuxY), 4 (kOQtHFpQvzs), each embedded on its story
page with its MP3 in media/. Episode 4 is on two pages: two-blind-men and blind-and-mute-man.

Decisions Brian made today:

- Episodes 1 to 3 stay as published. They are NOT being re-uploaded. That means their burned-in captions stay as
  they are (each picture holds one caption; found and fixed in make_video.py on 11 October), and they get no map
  and no photograph. Episode 3 has an uploaded closed-caption track; 1 and 2 have YouTube's automatic one.
- The series map is standard from episode 4 on: one base map (audio/maps/), the episode's place in gold, earlier
  places joined in episode order, described in walking time and clock-face directions, with a "Where this is"
  passage read by the narrator in the place section.
- Brian's Navy photograph with the "Mister Scaredy Cat" plate is standard from episode 4 on, shown on the short
  introduction line: "... Around here we call it Mister Scaredy Cat. The voice is not his, but the words are."
- Assets may be reused freely between episodes (sound beds, music families, the scroll, the pew).

The rule that must not be broken: Brian edits audio/scripts/epNN_*_01.md by hand. Fold his edits into
audio/episodes/epNN_*.py and commit BEFORE any rebuild. episode_lib refuses to overwrite a reading file that has
uncommitted edits; do not bypass it.

Next, in order:

1. Episode 5, The blind in the crowd: Brian's read-through of the script and its draft paragraphs; add the "Where
   this is" passage (two places: the mountain by the lake, and Jerusalem); add the last-week finding (Bartimaeus on
   the road and the blind in the Temple both fall in the final week, and the Temple healing is the last healing
   Matthew records). Do not say "three healings in ten days"; the shelf does not support it.
2. Episode 6, The answer to John: read-through, "Where this is" (Machaerus, and Nazareth for Isaiah 61).
3. Sound-effect request lists for 5 and 6 (audio/sfx.py, 200 credits a clip), shot lists, Gemini stills, video.
4. Open slots on the site that still wait for Brian, and Pastor John's voice memo.
