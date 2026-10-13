"""Make the web-sized pictures in media/images from the full-size paintings.

The paintings (audio/shots/images) are about 7 MB each and stay out of git. This writes each one listed in
src/images.py as a JPEG at each width in images.WIDTHS, a few hundred KB at most, and those are committed.
Run it after adding a picture to images.py:

    python src/make_web_images.py           # make what is missing
    python src/make_web_images.py --all     # remake everything
"""
import sys
from pathlib import Path

from PIL import Image

import images

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "audio" / "shots" / "images"
OUT = ROOT / "media" / "images"


def main(remake: bool = False) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    made = 0
    for pic in images.all_pictures():
        src = SRC / pic["source"]
        for w in images.widths(pic):
            dst = OUT / f"{pic['name']}-{w}.jpg"
            if dst.exists() and not remake:
                continue
            if not src.exists():
                raise SystemExit(f"missing source painting: {src}")
            im = Image.open(src).convert("RGB")
            if im.size != images.SOURCE_SIZE:
                raise SystemExit(f"{src.name} is {im.size}, expected {images.SOURCE_SIZE}")
            if "crop" in pic:
                im = im.crop(pic["crop"])
            h = round(im.height * w / im.width)
            im.resize((w, h), Image.LANCZOS).save(dst, "JPEG", quality=82, optimize=True, progressive=True)
            made += 1
            print(f"{dst.name}  {dst.stat().st_size // 1024} KB")
    print(f"{made} files written to {OUT}")


if __name__ == "__main__":
    main("--all" in sys.argv)
