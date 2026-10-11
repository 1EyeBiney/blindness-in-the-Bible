"""Draw the series base map and one highlighted map per episode, and describe each map in words.

Run from the repository root:  python audio/maps/make_map.py
Outputs: audio/shots/images/maps/base.png, audio/shots/images/maps/<ep>.png, audio/maps/descriptions.md

The map is schematic but true to the coordinates in places.json: water and the Jordan are drawn from approximate
outlines, every place sits at its real latitude and longitude, and the scale bar is real. Pillow only.
The written description is the map for a blind listener: for the episode's place, where it is and how far from
every place already visited, with compass directions, in the order of the journey.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT / "audio" / "shots" / "images" / "maps"
DATA = json.loads((HERE / "places.json").read_text(encoding="utf-8"))

W, H = 2752, 1536
PAD = 120
MAP_W = 1750   # the map uses the left part; the right panel carries the journey in words
FONT = r"C:\Windows\Fonts\georgia.ttf"
FONT_B = r"C:\Windows\Fonts\georgiab.ttf"
LAND = (214, 196, 160)
HILLS = (196, 176, 136)
WATER = (120, 160, 190)
SEA = (104, 146, 180)
INK = (60, 44, 30)
FAINT = (130, 112, 92)
GOLD = (190, 120, 30)
ROUTE = (150, 60, 40)

# approximate outlines (lat, lon)
COAST = [(31.05, 34.27), (31.3, 34.38), (31.52, 34.45), (31.8, 34.62), (32.1, 34.78), (32.45, 34.88), (32.75, 34.95),
         (32.95, 35.05), (33.1, 35.12), (33.27, 35.2), (33.56, 35.37), (33.65, 35.4)]
GALILEE = [(32.90, 35.60), (32.89, 35.64), (32.85, 35.66), (32.80, 35.65), (32.74, 35.63), (32.71, 35.59),
           (32.72, 35.55), (32.77, 35.53), (32.83, 35.53), (32.88, 35.56)]
DEAD = [(31.77, 35.52), (31.74, 35.56), (31.6, 35.58), (31.45, 35.56), (31.33, 35.52), (31.2, 35.47), (31.08, 35.42),
        (31.05, 35.40), (31.05, 35.35), (31.2, 35.40), (31.35, 35.44), (31.5, 35.46), (31.62, 35.47), (31.72, 35.48)]
JORDAN_N = [(33.25, 35.69), (33.1, 35.62), (32.95, 35.61), (32.90, 35.60)]
JORDAN_S = [(32.71, 35.58), (32.55, 35.56), (32.4, 35.55), (32.25, 35.57), (32.1, 35.53), (31.95, 35.54), (31.77, 35.52)]
RIDGE = [(31.3, 35.0), (31.7, 35.2), (32.0, 35.25), (32.3, 35.25), (32.6, 35.3), (32.9, 35.35)]  # central hills, faint

ROAD = [("jericho", "bethany"), ("bethany", "jerusalem"), ("capernaum", "bethsaida"), ("nazareth", "capernaum")]


def proj(lat: float, lon: float) -> tuple[float, float]:
    f = DATA["frame"]
    kx = math.cos(math.radians((f["lat_min"] + f["lat_max"]) / 2))
    span_x = (f["lon_max"] - f["lon_min"]) * kx
    span_y = f["lat_max"] - f["lat_min"]
    scale = min((MAP_W - 2 * PAD) / span_x, (H - 2 * PAD - 80) / span_y)
    x = PAD + (lon - f["lon_min"]) * kx * scale
    y = H - PAD + 20 - (lat - f["lat_min"]) * scale
    return x, y


def km(a: dict, b: dict) -> float:
    r = 6371.0
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dl = math.radians(b["lon"] - a["lon"])
    h = math.sin((p2 - p1) / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def walk_words(straight_km: float) -> str:
    """Straight-line km to spoken walking time. Roads wind, so the distance is lengthened by a quarter. Short
    stretches: 4 km an hour, which gives Edersheim's six hours from Jericho up to Jerusalem. Long journeys: 45 km
    a day, which gives Josephus's three days from Galilee to Jerusalem (Life 269) for a pilgrim walking hard."""
    road = straight_km * 1.25
    hours = road / 4.0
    if hours < 1:
        return "under an hour's walk"
    if hours < 1.5:
        return "about an hour's walk"
    if hours <= 9:
        return f"about {int(round(hours))} hours' walk"
    days = road / 45.0
    half = round(days * 2) / 2
    if half <= 1:
        return "about a day's walk"
    if half == int(half):
        return f"about {int(half)} days' walk"
    return f"about {int(half)} and a half days' walk"


def clock_word(a: dict, b: dict) -> str:
    """Direction from a to b as a clock face, north at twelve."""
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dl = math.radians(b["lon"] - a["lon"])
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    deg = (math.degrees(math.atan2(y, x)) + 360) % 360
    hour = int(round(deg / 30)) % 12
    return f"{12 if hour == 0 else hour} o'clock"


def bearing_word(a: dict, b: dict) -> str:
    p1, p2 = math.radians(a["lat"]), math.radians(b["lat"])
    dl = math.radians(b["lon"] - a["lon"])
    y = math.sin(dl) * math.cos(p2)
    x = math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl)
    deg = (math.degrees(math.atan2(y, x)) + 360) % 360
    names = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"]
    return names[int((deg + 22.5) // 45) % 8]


def base(draw: ImageDraw.ImageDraw, font_s, font_xs) -> None:
    draw.rectangle([0, 0, W, H], fill=LAND)
    # sea to the west of the coast
    coast = [proj(la, lo) for la, lo in COAST]
    draw.polygon([(0, 0)] + [(0, coast[0][1])] + coast + [(coast[-1][0], 0)], fill=SEA)
    # faint central ridge
    draw.line([proj(la, lo) for la, lo in RIDGE], fill=HILLS, width=70, joint="curve")
    # lakes and river
    draw.polygon([proj(la, lo) for la, lo in GALILEE], fill=WATER, outline=(90, 120, 150))
    draw.polygon([proj(la, lo) for la, lo in DEAD], fill=WATER, outline=(90, 120, 150))
    draw.line([proj(la, lo) for la, lo in JORDAN_N], fill=WATER, width=9, joint="curve")
    draw.line([proj(la, lo) for la, lo in JORDAN_S], fill=WATER, width=12, joint="curve")
    x, y = proj(32.66, 35.59); draw.text((x, y), "Sea of Galilee", font=font_xs, fill=(40, 60, 90), anchor="mt")
    x, y = proj(31.3, 35.49); draw.text((x, y), "Dead Sea", font=font_xs, fill=(40, 60, 90), anchor="mm")
    x, y = proj(32.3, 35.56); draw.text((x + 40, y), "the Jordan", font=font_xs, fill=(40, 60, 90), anchor="lm")
    x, y = proj(32.3, 34.55); draw.text((x, y), "The Great Sea", font=font_xs, fill=(230, 236, 240), anchor="mm")
    # roads
    for a, b in ROAD:
        pa, pb = DATA["places"][a], DATA["places"][b]
        draw.line([proj(pa["lat"], pa["lon"]), proj(pb["lat"], pb["lon"])], fill=(170, 150, 115), width=6)
    # scale bar: 50 km
    a = {"lat": 31.2, "lon": 35.8}; b = {"lat": 31.2, "lon": 35.8 + 50 / (111.32 * math.cos(math.radians(31.2)))}
    (x1, y1), (x2, y2) = proj(a["lat"], a["lon"]), proj(b["lat"], b["lon"])
    draw.line([(x1, y1), (x2, y2)], fill=INK, width=8)
    draw.text(((x1 + x2) / 2, y1 - 20), "50 km", font=font_xs, fill=INK, anchor="mb")
    # north arrow
    x, y = MAP_W - PAD, PAD + 20
    draw.line([(x, y + 110), (x, y)], fill=INK, width=8)
    draw.polygon([(x, y - 10), (x - 22, y + 40), (x + 22, y + 40)], fill=INK)
    draw.text((x, y + 130), "N", font=font_s, fill=INK, anchor="mt")


def dot(draw, p, r, fill, outline=INK, width=4):
    x, y = proj(p["lat"], p["lon"])
    draw.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=outline, width=width)


OFFSETS = {"bethsaida": (30, -34, "lm"), "capernaum": (-34, 18, "rm"), "mountain_decapolis": (30, 26, "lm"),
           "sea_of_galilee": (0, 0, "mm"), "bethany": (26, 30, "lm"), "jerusalem": (-30, 0, "rm"),
           "machaerus": (30, 0, "lm"), "dothan": (-28, 0, "rm"), "samaria": (-28, 0, "rm"), "shiloh": (-28, 0, "rm")}


def label(draw, p, font, fill, dx=26, dy=0, anchor="lm", key=None):
    if key in OFFSETS:
        dx, dy, anchor = OFFSETS[key]
    x, y = proj(p["lat"], p["lon"])
    draw.text((x + dx, y + dy), p["name"], font=font, fill=fill, anchor=anchor)


def render(ep_key: str | None) -> tuple[Path, str]:
    img = Image.new("RGB", (W, H), LAND)
    d = ImageDraw.Draw(img)
    f_l, f_m, f_s, f_xs = (ImageFont.truetype(FONT_B, 64), ImageFont.truetype(FONT, 46),
                           ImageFont.truetype(FONT, 38), ImageFont.truetype(FONT, 32))
    base(d, f_s, f_xs)
    places = DATA["places"]
    towns = {k: v for k, v in places.items() if v["kind"] not in ("water", "river")}
    ep = DATA["episodes"].get(ep_key) if ep_key else None
    focus = {ep["focus"], ep.get("focus2")} - {None} if ep else set()
    visited = ep["visited"] if ep else []
    # all places, faint
    for k, p in towns.items():
        if k in focus or k in visited:
            continue
        dot(d, p, 10, (200, 186, 160), outline=FAINT, width=3)
        if k != "bethany":
            label(d, p, f_xs, FAINT, key=k)
    # the journey so far: route through visited places in order, then to the focus
    if ep:
        chain = [places[k] for k in visited] + [places[ep["focus"]]]
        pts = [proj(p["lat"], p["lon"]) for p in chain]
        if len(pts) > 1:
            d.line(pts, fill=ROUTE, width=7, joint="curve")
        for k in visited:
            dot(d, places[k], 16, (235, 225, 200), outline=ROUTE, width=5)
            label(d, places[k], f_s, INK, key=k)
        for k in focus:
            dot(d, places[k], 30, GOLD, outline=INK, width=6)
            label(d, places[k], f_m, INK, dx=44, key=k)
        title = f"Episode {int(ep_key[2:])}: {ep['title']}"
    else:
        for k, p in towns.items():
            dot(d, p, 14, (235, 225, 200), outline=INK, width=4)
            label(d, p, f_s, INK, key=k)
        title = "Not By Sight: the places in the stories"
    # right panel: the journey in words, the same facts the narrator reads
    d.rectangle([MAP_W, 0, W, H], fill=(236, 226, 204))
    d.line([(MAP_W, 0), (MAP_W, H)], fill=(190, 172, 140), width=4)
    import textwrap
    yy = PAD
    for ln in textwrap.wrap(title, 26):
        d.text((MAP_W + 70, yy), ln, font=f_l, fill=INK); yy += 80
    yy += 20
    for para in (describe(ep_key).split(chr(10))[1:] if ep_key else describe(None).split(chr(10))[1:8]):
        for ln in textwrap.wrap(para, 44):
            d.text((MAP_W + 70, yy), ln, font=f_xs, fill=INK); yy += 44
        yy += 18
    for o in ([] if ep_key else DATA["off_map"][:2]):   # episode panels keep their lower half free for captions
        for ln in textwrap.wrap(f"{o['name']}: {o['direction']}, beyond the map.", 44):
            d.text((MAP_W + 70, yy), ln, font=f_xs, fill=FAINT); yy += 44
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"{ep_key or 'base'}.png"
    img.save(out)
    return out, describe(ep_key)


def describe(ep_key: str | None) -> str:
    places = DATA["places"]
    jer = places["jerusalem"]
    if not ep_key:
        lines = ["Base map. The Great Sea lies to the west. The Jordan runs south from the Sea of Galilee to the Dead "
                 "Sea. Jerusalem sits in the hills west of the Dead Sea's north end. Distances from Jerusalem:"]
        for k, p in places.items():
            if p["kind"] in ("water", "river") or k == "jerusalem":
                continue
            lines.append(f"- {p['name']}: {walk_words(km(jer, p))}, at {clock_word(jer, p)} from Jerusalem. "
                         f"{p.get('note', '')}".rstrip())
        for o in DATA["off_map"]:
            lines.append(f"- {o['name']}: {o['direction']}, beyond the map. {o['note']}")
        return "\n".join(lines)
    ep = DATA["episodes"][ep_key]
    fp = places[ep["focus"]]
    lines = [f"Episode {int(ep_key[2:])}, {ep['title']}. The map highlights {fp['name']} in gold. {fp.get('note', '')}".rstrip()]
    if ep.get("focus2"):
        p2 = places[ep["focus2"]]
        lines.append(f"A second gold mark is {p2['name']}, {walk_words(km(fp, p2))} from {fp['name']}, at "
                     f"{clock_word(fp, p2)}. {p2.get('note', '')}".rstrip())
    if ep["visited"]:
        lines.append(f"Stand at {fp['name']} and face north; north is twelve o'clock. The places already visited "
                     "in the series are marked and joined by a line, in the order of the episodes:")
        for k in ep["visited"]:
            p = places[k]
            lines.append(f"- {p['name']}: {walk_words(km(fp, p))}, at {clock_word(fp, p)}.")
    lines.append(f"From {fp['name']}, Jerusalem is {walk_words(km(fp, jer))}, at {clock_word(fp, jer)}."
                 if ep["focus"] != "jerusalem" else "Jerusalem is the city itself.")
    return "\n".join(lines)


def main() -> None:
    md = ["# The series map, in words", "",
          "Each map is drawn from real coordinates (audio/maps/places.json). The description below each one is the "
          "map for a listener who cannot see it. Distances are given as walking time on the roads of the day, and directions as a clock face with north at twelve.", ""]
    out, text = render(None)
    md += [f"## base.png", "", text, ""]
    print("wrote", out.name)
    for ep_key in DATA["episodes"]:
        out, text = render(ep_key)
        md += [f"## {ep_key}.png", "", text, ""]
        print("wrote", out.name)
    (HERE / "descriptions.md").write_text("\n".join(md), encoding="utf-8", newline="\n")
    print("wrote descriptions.md")


if __name__ == "__main__":
    main()
