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
3. Brian's words are recorded by Brian. The BRIAN cast entry is a placeholder for hearing the draft only.
4. Facts about the place and the time are the ones on the page, with the author named in the narration.
5. Nothing goes into audio that the site cannot source. Figures Brian has not sourced stay off.
6. Everything audible must stand alone. The video layer may add but never carry meaning.

## Steps

1. Brian reads the script (`audio/scripts/man_born_blind_01.md`) and marks changes. Done when he says so.
2. Brian picks voices: `labs_pipe voices sync`, then `voices list --search`, and fills the six IDs in the cast.
3. Draft render, one take: `labs_pipe render scripts/man_born_blind_01.txt --dry-run`, then without
   `--dry-run`; `review man_born_blind/1`; `assemble man_born_blind/1`. Listen end to end.
4. Brian records his eleven lines. Files go to `selected/man_born_blind/section_1/<id>_brian.mp3`, replacing
   the placeholder takes, so `assemble` picks them up unchanged. (Line IDs are in the render manifest.)
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
- Does he want the narrator to say his name ("Brian's words") before each of his sections, or let the voice
  change carry it?
- Length target: this draft runs about 15 minutes at 150 words per minute. Shorter?
- A music source with a licence we can show (public domain recordings, or a CC BY library), since nothing
  on the shelf covers music.
