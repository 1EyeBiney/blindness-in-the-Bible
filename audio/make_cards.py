"""Lettered title and closing cards for an episode, in the style of episode 6 and the trailer.

    python make_cards.py <episode image folder> <title background> <close background> "<Episode N: Title>" "<passage>"

Writes title_card.jpg and close_card.jpg into shots/images/<folder>/. The title card carries the series name,
the episode title and the passage; the closing card carries the verse, its reference and the site address, so the
address is on screen at the end of every episode, not only spoken.
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent
FONTS = Path("C:/Windows/Fonts")
CREAM, GOLD, NIGHT = "#fff8e8", "#f2d9a0", (6, 10, 24)


def _card(src: Path, dst: Path, lines: list[tuple[str, str, int, str]], top_frac: float = 0.07,
          shade_to: float = 0.46) -> None:
    im = Image.open(src).convert("RGB")
    W, H = im.size
    shade = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shade).rectangle([0, 0, W, int(H * shade_to)], fill=150)
    shade = shade.filter(ImageFilter.GaussianBlur(70))
    im.paste(Image.new("RGB", (W, H), NIGHT), (0, 0), shade)
    d = ImageDraw.Draw(im)
    y = int(H * top_frac)
    for text, font, size, fill in lines:
        f = ImageFont.truetype(str(FONTS / font), size)
        w = d.textlength(text, font=f)
        d.text(((W - w) / 2, y), text, font=f, fill=fill)
        y += int(size * 1.35)
    im.save(dst, quality=93)


def make(folder: str, title_bg: str, close_bg: str, episode_title: str, passage: str) -> tuple[Path, Path]:
    out = ROOT / "shots" / "images" / folder
    t = out / "title_card.jpg"
    c = out / "close_card.jpg"
    _card(out / title_bg, t, [("Not By Sight", "georgiab.ttf", 210, CREAM), (episode_title, "georgia.ttf", 96, CREAM),
                              (passage, "georgiai.ttf", 70, GOLD)])
    _card(out / close_bg, c, [("For we walk by faith, not by sight.", "georgiab.ttf", 120, CREAM),
                              ("2 Corinthians 5:7", "georgiai.ttf", 76, CREAM),
                              ("blindnessinthebible.com", "georgiab.ttf", 104, GOLD)])
    return t, c


if __name__ == "__main__":
    print(make(*sys.argv[1:6]))
