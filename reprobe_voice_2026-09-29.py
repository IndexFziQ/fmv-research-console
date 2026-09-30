#!/usr/bin/env python3
"""Reprobe v2 for 新世界 3319700 (2026-09-29): d2all pagination cap (6x20=120) missed ~47 texts.
Switch query shape: num_per_page=100, day_range=2, cursor pages <=4. Merge new texts into raw."""
import json, time, urllib.request, urllib.parse

RAW = "_raw_reviews_2026-09-29_voice.json"
CUTOFF = 1759008720  # not used here; filter in merge step by comparing existing

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 player-voice-bot/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print(f"retry {attempt+1}: {e}"); time.sleep(3)
    return None

def url(appid, cursor=None):
    u = ("https://store.steampowered.com/appreviews/3319700?json=1&language=schinese"
         "&review_type=all&purchase_type=all&num_per_page=100&day_range=2")
    if cursor: u += "&cursor=" + urllib.parse.quote(cursor)
    return u

out, cursor, seen = [], None, set()
for page in range(4):
    data = fetch(url(3319700, cursor))
    time.sleep(1.2)
    if not data or data.get("success") != 1: break
    revs = data.get("reviews", [])
    if not revs: break
    for r in revs:
        k = (r.get("timestamp_created", 0), r.get("review", "")[:80])
        if k in seen: continue
        seen.add(k)
        out.append({"voted_up": r.get("voted_up"), "playtime_min": r.get("author", {}).get("playtime_forever", 0),
                    "text": r.get("review", ""), "ts": r.get("timestamp_created", 0)})
    cursor = data.get("cursor")
    print(f"page {page+1}: {len(revs)} reviews")
    if not cursor or len(revs) < 100: break

print(f"total distinct trailing-2d: {len(out)}")

raw = json.load(open(RAW, encoding="utf-8"))
d2 = raw["3319700"]["samples"]["d2all"]
existing = {(r["ts"], r["text"][:80]) for r in d2["reviews"]}
added = [r for r in out if (r["ts"], r["text"][:80]) not in existing]
d2["reviews"].extend(added)
d2["num_reviews"] = len(d2["reviews"])
json.dump(raw, open(RAW, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"merged +{len(added)} new texts into d2all (now {len(d2['reviews'])})")
