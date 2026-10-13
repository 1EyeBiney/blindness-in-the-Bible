# Pictures on Not By Sight: the house style

One look across the episodes and the site, so a visitor never feels two hands at work.

## The standing prompt

Every picture is asked for with this opening, word for word, followed by the scene:

> Generate a 16:9 image. Painterly oil-sketch look, visible brushwork, warm natural light, the land and
> buildings of ancient Israel and its neighbours. No faces shown close up: people are seen from behind or at
> a distance. No text or lettering anywhere in the image. No modern objects. Calm and hopeful in mood, never
> frightening or graphic.

## The rules

1. **Painted, not photographic.** The one photograph on the site, Brian in his Navy whites, is softened to match.
2. **No faces close up.** Figures are seen from behind or far off. Nobody has to decide what Jesus, or a blind
   man, looked like.
3. **No words in a picture.** Words are set as real text on the page, where a screen reader and a magnifier
   can reach them. The series map is the one exception, and its caption gives the whole map in words.
4. **Hopeful, never frightening.** Hard stories (Samson, Zedekiah, Sodom) are shown before or after the harm,
   or from a distance. Nothing graphic.
5. **Imagined scenes are announced.** A story page's first caption says the pictures are paintings, imagined,
   not records.
6. **Every picture has a description and a caption.** The description (alt text) says what is in the picture
   for someone who cannot see it. The caption ties it to the story. They are never the same sentence, and
   nothing is said only in a picture.
7. **One size.** Paintings come out at 2752 by 1536. `src/make_web_images.py` makes the web copies.

## Where pictures go

- **Story pages:** a banner under the title, then at most one picture each beside What led up to it, What
  happens, In their shoes, and The place and the time, then the series map if the story has one.
- **Other pages:** one banner.
- **Site graphics:** the emblem (a white cane crossing a rising sun), the tab icon, and the share card, all
  made by `src/make_site_graphics.py`.

## How a new picture is made

1. Add it to a batch file in `audio/shots/` with its name, scene prompt, description and caption.
2. Run the prompt in Gemini. Brian downloads the results by hand into the batch folder under
   `audio/shots/images/`, and they are renamed in order.
3. Look at each one against the rules above. Remake any that break them.
4. List it in `src/images.py`, run `python src/make_web_images.py`, run the tests, publish.
