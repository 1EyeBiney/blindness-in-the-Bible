"""Turn a photograph into a warm, painterly still framed on the series matte, to sit beside the Gemini artwork.

Run from the repository root:  python audio/stylize_photo.py <input photo> <output png>
Used for Brian's Navy photograph (audio/shots/images/ep01_man_born_blind/00_brian_navy.png), which introduces his
sections from episode 4 on and can be dropped into episodes 1 to 3 later.
"""
from __future__ import annotations

import sys

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

W, H = 2752, 1536
MATTE = (214, 196, 160)


def stylize(src: Image.Image) -> Image.Image:
    im = src.convert("RGB").filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.SMOOTH)
    im = im.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).convert("RGB")
    im = im.filter(ImageFilter.GaussianBlur(0.6))
    arr = np.asarray(im).astype(np.float32)
    warm = arr @ np.array([[1.05, 0.03, 0.0], [0.03, 0.97, 0.0], [0.0, 0.02, 0.86]]).T
    im = Image.fromarray(np.clip(warm * 0.97 + np.array([14, 8, -4]), 0, 255).astype(np.uint8))
    im = ImageEnhance.Color(im).enhance(0.85)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    w, h = im.size
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.12 - 0.3 * r ** 2, 0.65, 1.0)
    grain = np.random.default_rng(7).normal(0, 4, (h, w, 1))
    return Image.fromarray(np.clip(np.asarray(im) * vig[..., None] + grain, 0, 255).astype(np.uint8))


def frame(pic: Image.Image) -> Image.Image:
    w, h = pic.size
    pic = pic.resize((int(w * (H - 160) / h), H - 160), Image.LANCZOS)
    out = Image.new("RGB", (W, H), MATTE)
    sh = Image.new("L", (pic.width + 80, pic.height + 80), 0)
    ImageDraw.Draw(sh).rectangle([40, 40, 40 + pic.width, 40 + pic.height], fill=110)
    sh = sh.filter(ImageFilter.GaussianBlur(28))
    out.paste(Image.new("RGB", sh.size, (90, 70, 50)), ((W - sh.width) // 2, (H - sh.height) // 2 + 12), sh)
    out.paste(pic, ((W - pic.width) // 2, 80))
    return out


if __name__ == "__main__":
    frame(stylize(Image.open(sys.argv[1]))).save(sys.argv[2])
    print("wrote", sys.argv[2])
