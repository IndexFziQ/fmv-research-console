#!/usr/bin/env python3
"""Re-probe d2all (protocol: NEW-TEXT << pos+neg delta) for apps with capture gaps, 2026-09-18 issue #27.
Gap apps: 幸存者(+27/cap14) 女帝(+7/cap3) 媚娘(+4/cap1) 恶校(+5/cap4) 绍宋(+8/cap6) 主角(+1/cap0).
Uses day_range=3, cursor <=8 pages, merges new texts into raw JSON under d3reprobe."""
import json, time, urllib.request, urllib.parse

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-18_voice.json"
CUTOFF = 1789604640  # 2026-09-17 08:24 CST
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) player-voice-bot/1.0"}

APPS = [
    ("4354460", "schinese"),
    ("4148240", "schinese"),
    ("3478050", "schinese"),
    ("3818020", "schinese"),
    ("4292950", "schinese"),
    ("4234260", "schinese"),
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print(f"  retry {attempt+1}: {e}")
            time.sleep(3)
    return None

def fetch_dN(appid, lang, day=3, max_pages=8):
    out, cursor, seen = [], None, set()
    for page in range(max_pages):
        u = (f"https://store.steampowered.com/appreviews/{appid}?json=1"
             f"&language={lang}&review_type=all&purchase_type=all&num_per_page=20&day_range={day}")
        if cursor:
            u += "&cursor=" + urllib.parse.quote(cursor)
        data = fetch(u)
        time.sleep(1.2)
        if not data or data.get("success") != 1:
            break
        revs = data.get("reviews", [])
        if not revs:
            break
        for r in revs:
            k = (r.get("timestamp_created", 0), r.get("review", "")[:80])
            if k in seen:
                continue
            seen.add(k)
            out.append({
                "voted_up": r.get("voted_up"),
                "playtime_min": r.get("author", {}).get("playtime_forever", 0),
                "text": r.get("review", ""),
                "ts": r.get("timestamp_created", 0),
            })
        cursor = data.get("cursor")
        if not cursor or len(revs) < 20:
            break
    return out

raw = json.load(open(RAW))
for appid, lang in APPS:
    title = raw[appid]["title"]
    revs = fetch_dN(appid, lang)
    new_revs = [r for r in revs if r["ts"] >= CUTOFF]
    # dedup against existing d2all captures
    existing = {(r["ts"], r["text"][:80]) for r in raw[appid]["samples"].get("d2all", {}).get("reviews", [])}
    fresh = [r for r in new_revs if (r["ts"], r["text"][:80]) not in existing]
    raw[appid]["samples"]["d3reprobe"] = {"num_reviews": len(revs), "reviews": fresh}
    print(f"== {title} ({appid}): d3 scan {len(revs)}, window-new {len(new_revs)}, fresh-vs-d2all {len(fresh)}")

with open(RAW, "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=1)
print("Merged ->", RAW)
