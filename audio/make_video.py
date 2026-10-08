"""Build the episode video: stills (or title cards) timed to the mix, with captions, as an MP4 for YouTube.

Run from audio/:
  python make_video.py man_born_blind_v2 renders/man_born_blind_v2/section_1/man_born_blind_v2.wav

Inputs:  deliver/<project>/timing.csv (from align_mix.py), shots/<project>.json, shots/images/<file>.png (optional),
         scripts/man_born_blind_02.txt (caption text per section).
Outputs: deliver/<project>/<project>.mp4 (1920x1080, H.264 + AAC), deliver/<project>/captions.srt,
         deliver/<project>/description.md (shot descriptions and credits for the YouTube description and the site).

Missing images fall back to a title card with the shot's 'card' text, so the chain can be tested before any
image exists. Every shot has a written description; nothing is said only in a picture.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
FONT = r"C:\Windows\Fonts\georgia.ttf"
FONT_UI = r"C:\Windows\Fonts\segoeui.ttf"
BG = (24, 20, 16)
FG = (240, 232, 214)
CAPTION_CHARS = 84          # per caption line
CAPTION_SECONDS = 6.0       # target length of one caption


def srt_time(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def title_card(text: str, path: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, 34) or [""])
    size = 96 if len(lines) <= 2 else 72
    font = ImageFont.truetype(FONT, size)
    total = sum(d.textbbox((0, 0), ln or " ", font=font)[3] + 18 for ln in lines)
    y = (H - total) // 2
    for ln in lines:
        box = d.textbbox((0, 0), ln or " ", font=font)
        d.text(((W - box[2]) // 2, y), ln, font=font, fill=FG)
        y += box[3] + 18
    img.save(path)


def fit_image(src: Path, path: Path) -> None:
    img = Image.open(src).convert("RGB")
    scale = max(W / img.width, H / img.height)
    img = img.resize((round(img.width * scale), round(img.height * scale)))
    left, top = (img.width - W) // 2, (img.height - H) // 2
    img.crop((left, top, left + W, top + H)).save(path)


def captions(sections: list[dict], texts: dict[str, str]) -> list[tuple[float, float, str]]:
    """Split each section's text into captions at sentence ends, spread over the section's time by word share."""
    out = []
    for s in sections:
        text = texts.get(s["id"], "")
        if not text:
            continue
        pieces = re.split(r"(?<=[.!?;:])\s+", text)
        chunks, cur = [], ""
        for pc in pieces:
            if cur and len(cur) + 1 + len(pc) > CAPTION_CHARS * 2:
                chunks.append(cur); cur = pc
            else:
                cur = f"{cur} {pc}".strip()
        if cur:
            chunks.append(cur)
        total_words = sum(len(c.split()) for c in chunks) or 1
        dur = s["end"] - s["start"]
        t = s["start"]
        for ch in chunks:
            d = dur * len(ch.split()) / total_words
            label = "" if s["speaker"] == "NARRATOR" else f"[{s['speaker'].title()}] "
            out.append((t, t + d - 0.05, "
".join(textwrap.wrap(label + ch, CAPTION_CHARS))))
            t += d
    return out


def main(project: str, mix: str) -> None:
    root = Path(__file__).resolve().parent
    out = root / "deliver" / project
    out.mkdir(parents=True, exist_ok=True)
    with (out / "timing.csv").open(encoding="utf-8") as fh:
        sections = [{"id": r["id"], "speaker": r["speaker"], "start": float(r["start_sec"]), "end": float(r["end_sec"])}
                    for r in csv.DictReader(fh)]
    shots = json.loads((root / "shots" / f"{project}.json").read_text(encoding="utf-8"))
    script = root / "scripts" / "man_born_blind_02.txt"
    texts, n = {}, 0
    for ln in script.read_text(encoding="utf-8").splitlines():
        if ln.startswith("[") and not ln.startswith(("[BREAK]", "[PAUSE")):
            n += 1
            texts[f"{n:03d}"] = re.match(r"^\[(\w+)\]\s*(?:\(([^)]*)\))?\s*(.*)$", ln).group(3)

    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mix],
                                 capture_output=True, text=True, check=True).stdout.strip())
    start_of = {s["id"]: s["start"] for s in sections}
    frames = out / "frames"
    frames.mkdir(exist_ok=True)
    cues = []
    for i, shot in enumerate(shots["shots"]):
        t0 = 0.0 if i == 0 else start_of[shot["from"]] - 0.3
        png = frames / f"shot_{i:02d}.png"
        src = root / "shots" / "images" / shot["image"]
        if src.exists():
            fit_image(src, png)
            kind = "image"
        else:
            title_card(shot["card"], png)
            kind = "card"
        cues.append((t0, png, kind, shot))
    # ffmpeg concat list of stills with durations
    lst = out / "frames.txt"
    with lst.open("w", encoding="utf-8") as fh:
        for i, (t0, png, _, _) in enumerate(cues):
            t1 = cues[i + 1][0] if i + 1 < len(cues) else total
            fh.write(f"file '{png.as_posix()}'\nduration {max(0.1, t1 - t0):.3f}\n")
        fh.write(f"file '{cues[-1][1].as_posix()}'\n")
    # captions
    srt = out / "captions.srt"
    with srt.open("w", encoding="utf-8") as fh:
        for k, (a, b, text) in enumerate(captions(sections, texts), 1):
            fh.write(f"{k}\n{srt_time(a)} --> {srt_time(b)}\n{text}\n\n")
    # description for YouTube and the site
    desc = [f"# {project}: shots and credits", "",
            "Each still, with its written description (for blind viewers and for the record):", ""]
    for t0, _, kind, shot in cues:
        m, s = divmod(int(t0), 60)
        desc.append(f"- {m:02d}:{s:02d}  {shot['description']}" + ("" if kind == "image" else "  (title card for now)"))
    desc += ["", "Scripture quotations are from the Holy Bible, Berean Standard Bible, BSB, public domain.",
             "Scenes introduced with the word 'imagine' are our own. Voices generated with ElevenLabs; mix by Brian Clark.",
             "Music: TO BE FILLED IN (title, artist, licence)."]
    (out / "description.md").write_text("\n".join(desc) + "\n", encoding="utf-8")
    # video: stills + mix, captions burned in from the SRT (YouTube also gets the SRT as a closed-caption track)
    mp4 = out / f"{project}.mp4"
    srt_f = srt.as_posix().replace(":", "\\:")
    vf = (f"subtitles='{srt_f}':force_style='FontName=Segoe UI,FontSize=22,PrimaryColour=&H00F0E8D6,"
          f"OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=0,MarginV=48'")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", mix,
                    "-vf", vf, "-r", "24", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", "-movflags", "+faststart", str(mp4)], check=True)
    print(f"wrote {mp4} ({mp4.stat().st_size / 1e6:.1f} MB), {len(cues)} shots "
          f"({sum(k == 'image' for _, _, k, _ in cues)} images, {sum(k == 'card' for _, _, k, _ in cues)} cards), "
          f"{srt.name}, {desc and 'description.md'}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
