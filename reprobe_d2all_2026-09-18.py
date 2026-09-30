#!/usr/bin/env python3
"""Re-probe d2all channel for all 35 apps (protocol: NEW-TEXT << pos+neg net increase).
Loads raw JSON, re-fetches d2all per app, patches in place."""
import json, time, urllib.request, urllib.parse

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-18_voice.json"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) player-voice-bot/1.0"}

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

def url(appid, lang, rtype, day=None, cursor=None):
    u = (f"https://store.steampowered.com/appreviews/{appid}?json=1"
         f"&language={lang}&review_type={rtype}&purchase_type=all&num_per_page=20")
    if day:
        u += f"&day_range={day}"
    if cursor:
        u += "&cursor=" + urllib.parse.quote(cursor)
    return u

def simplify(rev):
    return {
        "voted_up": rev.get("voted_up"),
        "playtime_min": rev.get("author", {}).get("playtime_forever", 0),
        "text": rev.get("review", ""),
        "ts": rev.get("timestamp_created", 0),
    }

def fetch_dN(appid, primary, day=2, max_pages=6):
    out, cursor, seen = [], None, set()
    for page in range(max_pages):
        data = fetch(url(appid, primary, "all", day=day, cursor=cursor))
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
            out.append(simplify(r))
        cursor = data.get("cursor")
        if not cursor or len(revs) < 20:
            break
    return out

raw = json.load(open(RAW))
for appid, e in raw.items():
    primary = "english" if e["lang_group"] == "en" else "schinese"
    old_n = e["samples"].get("d2all", {}).get("num_reviews", 0)
    d2 = fetch_dN(appid, primary, day=2)
    e["samples"]["d2all"] = {"num_reviews": len(d2), "reviews": d2}
    print(f"{e['title']}: d2all {old_n} -> {len(d2)}", flush=True)

with open(RAW, "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=1)
print("Patched ->", RAW)
