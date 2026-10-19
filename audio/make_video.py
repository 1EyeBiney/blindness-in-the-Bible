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


# Caption labels for speakers whose cast tag is not a plain name (Law series, 18 October 2026).
LABELS = {"HENRY": "Matthew Henry", "BOOKS": "The old books"}


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


def _chunks(pieces: list[str]) -> list[list[int]]:
    """Group consecutive pieces into captions of at most two lines."""
    groups, cur, n = [], [], 0
    for i, pc in enumerate(pieces):
        if cur and n + 1 + len(pc) > CAPTION_CHARS * 2:
            groups.append(cur)
            cur, n = [], 0
        cur.append(i)
        n += len(pc) + 1
    if cur:
        groups.append(cur)
    return groups


def captions(sections: list[dict], texts: dict[str, str], sent_times: dict | None = None) -> list[tuple[float, float, str]]:
    """Captions of at most two lines. Where the sentence starts are known from the voice file's pauses
    (speech_times.py) each caption begins with its sentence; otherwise the section's time is shared out by words."""
    out = []
    for s in sections:
        text = texts.get(s["id"], "")
        if not text:
            continue
        label = "" if s["speaker"] == "NARRATOR" else f"[{LABELS.get(s['speaker'], s['speaker'].title())}] "
        known = (sent_times or {}).get(s["id"])
        if known:
            sents = [k[0] for k in known]
            starts = [k[1] for k in known] + [s["end"]]
            for g in _chunks(sents):
                a, b = starts[g[0]], starts[g[-1] + 1]
                body = " ".join(sents[i] for i in g)
                parts = [body]
                if len(body) > CAPTION_CHARS * 2:       # one very long sentence: break at clause ends, by length
                    bits = re.split(r"(?<=[,;:])\s+", body)
                    parts = [" ".join(bits[i] for i in gg) for gg in _chunks(bits)]
                tot = sum(len(x) for x in parts) or 1
                t = a
                for x in parts:
                    d = (b - a) * len(x) / tot
                    out.append((t, t + d - 0.05, "\n".join(textwrap.wrap(label + x, CAPTION_CHARS, break_on_hyphens=False))))
                    t += d
            continue
        pieces = re.split(r"(?<=[.!?;:])\s+", text)
        chunks = [" ".join(pieces[i] for i in g) for g in _chunks(pieces)]
        total_words = sum(len(c.split()) for c in chunks) or 1
        dur = s["end"] - s["start"]
        t = s["start"]
        for ch in chunks:
            d = dur * len(ch.split()) / total_words
            out.append((t, t + d - 0.05, "\n".join(textwrap.wrap(label + ch, CAPTION_CHARS, break_on_hyphens=False))))
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
    script = root / "scripts" / ("man_born_blind_02.txt" if project == "man_born_blind_v2" else project.replace("_v2", "_02") + ".txt")
    texts, n = {}, 0
    for ln in script.read_text(encoding="utf-8").splitlines():
        if ln.startswith("[") and not ln.startswith(("[BREAK]", "[PAUSE")):
            n += 1
            texts[f"{n:03d}"] = re.match(r"^\[(\w+)\]\s*(?:\(([^)]*)\))?\s*(.*)$", ln).group(3)
            # the script spells the address the way it is spoken; a caption shows it the way it is typed
            texts[f"{n:03d}"] = texts[f"{n:03d}"].replace("blindness in the Bible dot com", "blindnessinthebible.com")

    total = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mix],
                                 capture_output=True, text=True, check=True).stdout.strip())
    start_of = {s["id"]: s["start"] for s in sections}
    span_of = {s["id"]: (s["start"], s["end"]) for s in sections}
    import speech_times
    sel = root / "selected" / project / "section_1"
    sent_times = {}
    for sec in sections:
        f = sel / f"{sec['id']}_{sec['speaker'].lower()}.mp3"
        got = speech_times.sentence_starts(f, texts.get(sec["id"], "")) if f.exists() else None
        if got:
            sent_times[sec["id"]] = [(snt, sec["start"] + t) for snt, t in got]
    print(f"sentence timing from pauses: {len(sent_times)} of {len(sections)} sections")

    def shot_time(shot: dict) -> float:
        """A shot starts with its section, or, with 'at_phrase', partway through it: the phrase is found in the
        section's text and placed by its share of the words, which is close enough for a still."""
        a, b = span_of[shot["from"]]
        phrase = shot.get("at_phrase")
        if shot.get("at_seconds") is not None:           # a fixed offset into the section, for a map after the first sentence
            return min(a + float(shot["at_seconds"]), b - 1.0)
        if not phrase:
            return a - 0.3
        text = texts[shot["from"]]
        pos = text.find(phrase)
        if pos < 0:
            raise SystemExit(f"shot at_phrase not found in section {shot['from']}: {phrase!r}")
        for snt, t in sent_times.get(shot["from"], []):
            if snt.startswith(phrase[:40]) or phrase in snt:
                return t - 0.3
        frac = len(text[:pos].split()) / max(1, len(text.split()))
        return a + (b - a) * frac - 0.3

    frames = out / "frames"
    frames.mkdir(exist_ok=True)
    cues = []
    for i, shot in enumerate(shots["shots"]):
        t0 = 0.0 if i == 0 else shot_time(shot)
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
    burn = out / "captions_burn.ass"
    caps = captions(sections, texts, sent_times)
    shot_starts = [c[0] for c in cues] + [total]

    def panel(t: float) -> bool:
        for i, (t0, _, _, sh) in enumerate(cues):
            if t0 <= t < shot_starts[i + 1]:
                return sh.get("captions") == "panel" or sh["image"].startswith("maps/")
        return False

    def ass_time(t: float) -> str:
        cs = int(round(max(0.0, t) * 100))
        h, cs = divmod(cs, 360000)
        m, cs = divmod(cs, 6000)
        sec, cs = divmod(cs, 100)
        return f"{h}:{m:02d}:{sec:02d}.{cs:02d}"

    # The burned-in captions are written as an ASS file so their place and size are ours to set: large, light
    # and outlined along the bottom of a painting; on a map, dark and smaller in the lower half of the side panel,
    # so nothing on the map is covered. captions.srt stays plain, for YouTube's closed-caption track.
    panel_left = int(W * 1750 / 2752) + 44
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Segoe UI,64,&H00F0E8D6,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,5,0,2,90,90,60,1
Style: Panel,Georgia,44,&H001E2C3C,&H000000FF,&H00CCE2EC,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,{panel_left},44,{int(H * 0.60)},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    with srt.open("w", encoding="utf-8") as fh, burn.open("w", encoding="utf-8") as fb:
        fb.write(head)
        for k, (a, b, text) in enumerate(caps, 1):
            fh.write(f"{k}\n{srt_time(a)} --> {srt_time(b)}\n{text}\n\n")
            style = "Panel" if panel((a + b) / 2) else "Default"
            flat = text.replace("\n", " ").replace("{", "(").replace("}", ")")
            fb.write(f"Dialogue: 0,{ass_time(a)},{ass_time(b)},{style},,0,0,0,,{flat}\n")
    # description for YouTube and the site
    desc = [f"# {project}: shots and credits", "",
            "Each still, with its written description (for blind viewers and for the record):", ""]
    for t0, _, kind, shot in cues:
        m, s = divmod(int(t0), 60)
        desc.append(f"- {m:02d}:{s:02d}  {shot['description']}" + ("" if kind == "image" else "  (title card for now)"))
    desc += ["", "Scripture quotations are from the Holy Bible, Berean Standard Bible, BSB, public domain.",
             "Scenes introduced with the word 'imagine' are our own. Voices generated with ElevenLabs; mix by Brian Clark.",
             "Original music by Brian Clark, made with Suno. All rights held by the author."]
    (out / "description.md").write_text("\n".join(desc) + "\n", encoding="utf-8")
    # video: stills + mix, captions burned in from the SRT (YouTube also gets the SRT as a closed-caption track)
    mp4 = out / f"{project}.mp4"
    srt_f = burn.as_posix().replace(":", "\\:")
    # fps first: a still arrives as ONE frame, and a caption burned onto it would be frozen for the whole shot
    # (that was the case in episodes 1 to 3 as first published). Making 24 frames a second before the subtitles
    # filter lets every caption appear and leave on time.
    vf = f"fps=24,subtitles='{srt_f}'"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", mix,
                    "-vf", vf, "-r", "24", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", "-movflags", "+faststart", str(mp4)], check=True)
    print(f"wrote {mp4} ({mp4.stat().st_size / 1e6:.1f} MB), {len(cues)} shots "
          f"({sum(k == 'image' for _, _, k, _ in cues)} images, {sum(k == 'card' for _, _, k, _ in cues)} cards), "
          f"{srt.name}, {desc and 'description.md'}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
