#!/usr/bin/env python3
"""Reprobe v2 for 2026-09-30: gap apps (NEW-TEXT 14 < net +57, gap ~46).
Switch query shape: num_per_page=100, day_range=3, cursor pages <=4. Merge new texts into raw."""
import json, time, urllib.request, urllib.parse

RAW = "_raw_reviews_2026-09-30_voice.json"
GAP_APPS = [
    ("3319700", "schinese"),  # 新世界 gap 30
    ("4354460", "schinese"),  # 幸存者 gap 5
    ("3478050", "schinese"),  # 媚娘 gap 4
    ("4148240", "schinese"),  # 女帝 gap 3
    ("3831120", "schinese"),  # 江山 gap 2
    ("4699920", "schinese"),  # 天平 gap 1
    ("4734650", "schinese"),  # 请去Bar gap 1
]

def fetch(u):
    req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 player-voice-bot/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print(f"retry {attempt+1}: {e}"); time.sleep(3)
    return None

def build(appid, cursor=None):
    u = (f"https://store.steampowered.com/appreviews/{appid}?json=1&language=schinese"
         "&review_type=all&purchase_type=all&num_per_page=100&day_range=3")
    if cursor: u += "&cursor=" + urllib.parse.quote(cursor)
    return u

raw = json.load(open(RAW, encoding="utf-8"))
for appid, lang in GAP_APPS:
    out, cursor, seen = [], None, set()
    for page in range(4):
        data = fetch(build(appid, cursor))
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
        if not cursor or len(revs) < 100: break
    d2 = raw[appid]["samples"]["d2all"]
    existing = {(r["ts"], r["text"][:80]) for r in d2["reviews"]}
    added = [r for r in out if (r["ts"], r["text"][:80]) not in existing]
    d2["reviews"].extend(added)
    d2["num_reviews"] = len(d2["reviews"])
    print(f"{appid}: trailing-3d distinct {len(out)}, merged +{len(added)} (d2all now {len(d2['reviews'])})")

json.dump(raw, open(RAW, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved raw")
