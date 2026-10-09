"""Collect sound effects from ElevenLabs by prompt, several variants at a time, filed for listening.

Run from audio/:
  python sfx.py "<slug>" "<prompt>" [--seconds 12] [--variants 4] [--influence 0.4] [--loop] [--dry-run]
  python sfx.py --batch sfx/requests.json          (a list of {slug, prompt, seconds, variants, influence, loop})
  python sfx.py --list                             (what has been collected, with prompts and lengths)

Files land in audio/sfx/<slug>/<slug>_v<n>.mp3 with a manifest.json beside them (prompt, seconds, date, size).
The key is read from audio/.env (ELEVENLABS_API_KEY=...) and is never printed. Each call prints the credits the
account reports as used, so the cost is visible per batch.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SFX = HERE / "sfx"
API = "https://api.elevenlabs.io/v1/sound-generation"
SUB = "https://api.elevenlabs.io/v1/user/subscription"


def key() -> str:
    env = HERE / ".env"
    for line in env.read_text(encoding="utf-8").splitlines() if env.exists() else []:
        if line.startswith("ELEVENLABS_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"')
    k = os.environ.get("ELEVENLABS_API_KEY", "")
    if not k:
        sys.exit("labs: no ELEVENLABS_API_KEY in audio/.env or the environment")
    return k


def credits_used(k: str) -> int | None:
    try:
        req = urllib.request.Request(SUB, headers={"xi-api-key": k})
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.load(r)
        return int(d.get("character_count", 0))
    except Exception:
        return None


def generate(k: str, prompt: str, seconds: float, influence: float, loop: bool) -> bytes:
    body = {"text": prompt, "duration_seconds": seconds, "prompt_influence": influence}
    if loop:
        body["loop"] = True
    req = urllib.request.Request(API, data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"xi-api-key": k, "Content-Type": "application/json",
                                          "Accept": "audio/mpeg"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:300]
            if e.code in (429, 500, 502, 503) and attempt < 3:
                time.sleep(3 * (attempt + 1))
                continue
            raise SystemExit(f"labs: HTTP {e.code}: {msg}")
    raise SystemExit("labs: gave up after retries")


def collect(k: str, slug: str, prompt: str, seconds: float, variants: int, influence: float, loop: bool,
            dry: bool) -> None:
    out = SFX / slug
    out.mkdir(parents=True, exist_ok=True)
    man_path = out / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {"slug": slug, "takes": []}
    start = len(man["takes"]) + 1
    print(f"{slug}: {variants} variant(s) x {seconds}s, influence {influence}{', loop' if loop else ''}"
          f"{' (dry run)' if dry else ''}")
    if dry:
        return
    before = credits_used(k)
    for n in range(start, start + variants):
        data = generate(k, prompt, seconds, influence, loop)
        f = out / f"{slug}_v{n}.mp3"
        f.write_bytes(data)
        man["takes"].append({"file": f.name, "prompt": prompt, "seconds": seconds, "influence": influence,
                             "loop": loop, "bytes": len(data), "made": dt.datetime.now().isoformat(timespec="seconds")})
        man_path.write_text(json.dumps(man, indent=2), encoding="utf-8")
        print(f"  saved {f.name} ({len(data) / 1000:.0f} KB)")
        time.sleep(1.0)
    after = credits_used(k)
    if before is not None and after is not None:
        print(f"  credits used by this batch: {after - before}")


def list_all() -> None:
    for man_path in sorted(SFX.glob("*/manifest.json")):
        man = json.loads(man_path.read_text(encoding="utf-8"))
        print(f"== {man['slug']} ({len(man['takes'])} takes)")
        for t in man["takes"]:
            print(f"   {t['file']:34} {t['seconds']:>5}s  {t['prompt'][:80]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?")
    ap.add_argument("prompt", nargs="?")
    ap.add_argument("--seconds", type=float, default=12.0, help="0.5 to 22")
    ap.add_argument("--variants", type=int, default=4)
    ap.add_argument("--influence", type=float, default=0.4, help="0 to 1; higher follows the prompt more literally")
    ap.add_argument("--loop", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--batch", help="JSON list of requests")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    if a.list:
        list_all(); return
    k = key()
    jobs = []
    if a.batch:
        for j in json.loads(Path(a.batch).read_text(encoding="utf-8")):
            jobs.append((j["slug"], j["prompt"], float(j.get("seconds", 12)), int(j.get("variants", 4)),
                         float(j.get("influence", 0.4)), bool(j.get("loop", False))))
    elif a.slug and a.prompt:
        jobs.append((a.slug, a.prompt, a.seconds, a.variants, a.influence, a.loop))
    else:
        ap.error("give a slug and a prompt, or --batch, or --list")
    for slug, prompt, seconds, variants, influence, loop in jobs:
        collect(k, slug, prompt, min(max(seconds, 0.5), 22.0), variants, influence, loop, a.dry_run)


if __name__ == "__main__":
    main()
