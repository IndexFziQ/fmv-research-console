#!/usr/bin/env python3
"""Reprobe gap apps 2026-09-28: NEW-TEXT captured (57 old-pool) < net delta (+85).
Gap apps: 媚娘 3478050 (+11), 江山 3831120 (+7), 女帝 4148240 (+5), 恶校 3818020 (+2),
不心动 4855450 (+2), 雪落 4740420 (+1). Per 09-25 protocol v2: same-form reprobe often
hits stale shards; switch query shape (num_per_page=100, day_range=7) to hit fresh shards,
then patch raw JSON d5all channel and re-run digest."""
import json, time, urllib.request, urllib.parse

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-28_voice.json"
GAP_APPS = ["3478050", "3831120", "4148240", "3818020", "4855450", "4740420"]

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

def url100(appid, primary, day=7, cursor=None):
    u = (f"https://store.steampowered.com/appreviews/{appid}?json=1"
         f"&language={primary}&review_type=all&purchase_type=all&num_per_page=100"
         f"&day_range={day}")
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

raw = json.load(open(RAW))
for appid in GAP_APPS:
    e = raw[appid]
    primary = "schinese" if e["lang_group"] == "cn" else "english"
    out, cursor, seen = [], None, set()
    for page in range(3):
        data = fetch(url100(appid, primary, day=7, cursor=cursor))
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
        if not cursor or len(revs) < 100:
            break
    old_d5 = e["samples"].get("d5all", {}).get("reviews", [])
    old_keys = {(r["ts"], r["text"][:80]) for r in old_d5}
    merged = list(old_d5)
    added = 0
    for r in out:
        if (r["ts"], r["text"][:80]) not in old_keys:
            merged.append(r)
            added += 1
    e["samples"]["d5all"] = {"num_reviews": len(merged), "reviews": merged}
    print(f"{e['title']}: num100/d7 reprobe {len(out)} revs, +{added} new merged (d5all total {len(merged)})")

with open(RAW, "w", encoding="utf-8") as f:
    json.dump(raw, f, ensure_ascii=False, indent=1)
print(f"Patched -> {RAW}")
