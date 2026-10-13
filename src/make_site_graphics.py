"""Make the site's own graphics: the emblem, the browser-tab icons and the share card.

    python src/make_site_graphics.py

The emblem is a white cane, tip down, crossing a rising sun: the cane for blindness, the light for 2 Corinthians
5:7. It is drawn as SVG so it stays sharp at any text size, and rendered here to PNG and ICO for older browsers
and phones. The share card is the picture that appears when a link to the site is pasted into a message or a
social post. Outputs go to media/ and are committed.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "media"
NAVY, GOLD, WHITE, RED = "#0b3d91", "#f2b84b", "#ffffff", "#c8102e"

EMBLEM_SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="12" fill="{NAVY}"/>
<path d="M10 44a22 22 0 0 1 44 0z" fill="{GOLD}"/>
<rect x="6" y="44" width="52" height="3" fill="{WHITE}"/>
<path d="M45 9 20 55" stroke="{WHITE}" stroke-width="5" stroke-linecap="round"/>
<path d="M23.3 49 20 55" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>
</svg>
"""


def emblem_png(size: int) -> Image.Image:
    """The same emblem drawn with Pillow, four times oversize and scaled down for clean edges."""
    k = size * 4 / 64
    im = Image.new("RGBA", (size * 4, size * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 64 * k - 1, 64 * k - 1], radius=12 * k, fill=NAVY)
    d.pieslice([10 * k, 22 * k, 54 * k, 66 * k], 180, 360, fill=GOLD)
    d.rectangle([6 * k, 44 * k, 58 * k, 47 * k], fill=WHITE)
    w = round(5 * k)

    def stroke(x1, y1, x2, y2, colour):
        d.line([x1 * k, y1 * k, x2 * k, y2 * k], fill=colour, width=w)
        for x, y in ((x1, y1), (x2, y2)):
            d.ellipse([x * k - w / 2, y * k - w / 2, x * k + w / 2, y * k + w / 2], fill=colour)
    stroke(45, 9, 20, 55, WHITE)
    stroke(23.3, 49, 20, 55, RED)
    return im.resize((size, size), Image.LANCZOS)


def share_card() -> Image.Image:
    """1200 by 630: a painting from the series, darkened at the foot, with the site's name set over it."""
    src = ROOT / "audio" / "shots" / "images" / "ep03_bethsaida" / "10_there_is_the_lake.png"
    im = Image.open(src).convert("RGB")
    W, H = 1200, 630
    scale = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    left, top = (im.width - W) // 2, (im.height - H) // 2
    im = im.crop((left, top, left + W, top + H))
    shade = Image.new("L", (1, H), 0)
    for y in range(H):
        shade.putpixel((0, y), int(225 * max(0.0, (y - H * 0.38) / (H * 0.62)) ** 0.8))
    im.paste(Image.new("RGB", (W, H), (8, 16, 32)), (0, 0), shade.resize((W, H)))
    d = ImageDraw.Draw(im)
    fonts = Path("C:/Windows/Fonts")
    big = ImageFont.truetype(str(fonts / "georgiab.ttf"), 92)
    mid = ImageFont.truetype(str(fonts / "georgia.ttf"), 40)
    small = ImageFont.truetype(str(fonts / "georgiai.ttf"), 32)
    im.paste(emblem_png(96), (64, 372), emblem_png(96))
    d.text((184, 366), "Not By Sight", font=big, fill="#fff8e8")
    d.text((66, 490), "Studies on blindness in the Bible", font=mid, fill="#fff8e8")
    d.text((66, 548), "For we walk by faith, not by sight.   blindnessinthebible.com", font=small, fill="#f2d9a0")
    return im


def main() -> None:
    MEDIA.mkdir(exist_ok=True)
    (MEDIA / "emblem.svg").write_text(EMBLEM_SVG, encoding="utf-8", newline="\n")
    emblem_png(180).save(MEDIA / "apple-touch-icon.png")
    emblem_png(64).save(MEDIA / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
    share_card().save(MEDIA / "share-card.jpg", "JPEG", quality=86, optimize=True, progressive=True)
    for f in ("emblem.svg", "apple-touch-icon.png", "favicon.ico", "share-card.jpg"):
        print(f, (MEDIA / f).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
