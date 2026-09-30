#!/usr/bin/env python3
"""Reprobe gap apps 2026-09-25: NEW-TEXT captured (24) < net delta (+39).
Gap apps: 媚娘 3478050 (+7), 女帝 4148240 (+5), 冰点 3711170 (+1), 江山 3831120 (+1),
雪落 4740420 (+1), 不心动 4855450 (+1). Per 09-17 protocol: full re-probe via
day_range=5 cursor pagination (fresh shards), then patch raw JSON and re-run digest."""
import json, time, urllib.request, urllib.parse

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-25_voice.json"
GAP_APPS = ["3478050", "4148240", "3711170", "3831120", "4740420", "4855450"]

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

def fetch_dN(appid, primary, day=5, max_pages=8):
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
for appid in GAP_APPS:
    e = raw[appid]
    primary = "schinese" if e["lang_group"] == "cn" else "english"
    d5 = fetch_dN(appid, primary, day=5)
    old_d3 = e["samples"].get("d3all", {}).get("reviews", [])
    old_keys = {(r["ts"], r["text"][:80]) for r in old_d3}
    merged = list(old_d3)
    added = 0
    for r in d5:
        if (r["ts"], r["text"][:80]) not in old_keys:
            merged.append(r)
            added += 1
    e["samples"]["d3all"] = {"num_reviews": len(merged), "reviews": merged}
    print(f"{e['title']}: d5 reprobe {len(d5)} revs, +{added} new merged (d3all total {len(merged)})")

with open(RAW, "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=1)
print(f"Patched -> {RAW}")
