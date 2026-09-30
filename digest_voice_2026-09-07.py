#!/usr/bin/env python3
"""Digest raw player-voice reviews (2026-09-07): API pct vs store baseline (today's intel all-lang),
72h delta vs 09-04 raw (weekend not run), full review texts."""
import json, datetime

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-07_voice.json"
PREV = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-04_voice.json"
INTEL = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_intel_steam_raw_2026-09-07.json"
POOL = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/products/_pool.json"
OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_digest_2026-09-07_voice.txt"

raw = json.load(open(RAW))
prev = json.load(open(PREV))
intel = json.load(open(INTEL)).get("reviews", {})
pool = {p["app_id"]: p for p in json.load(open(POOL))["products"]}

CUTOFF = int(datetime.datetime(2026, 9, 4, 8, 15).timestamp())  # last run window

def hrs(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M")

lines = []
total_new = 0
for appid, e in raw.items():
    p = pool.get(appid, {})
    s = e["samples"]
    prim_all = s.get("all", {})
    tot = prim_all.get("total_reviews")
    pos = prim_all.get("total_positive")
    api_pct = round(pos / tot * 100, 1) if tot else None
    # store baseline: today's intel all-language pct (freshest)
    it = intel.get(appid, {}).get("all", {})
    store_pct = it.get("pct")
    if store_pct is None:
        store_pct = p.get("review_pct")
    dev = round(api_pct - store_pct, 1) if api_pct is not None and store_pct else None

    prev_tot = None
    if appid in prev:
        pa = prev[appid]["samples"].get("all", {})
        prev_tot = pa.get("total_reviews")
    delta = (tot - prev_tot) if (tot is not None and prev_tot is not None) else None

    new_cnt = sum(1 for r in prim_all.get("reviews", []) if r["ts"] >= CUTOFF)
    total_new += new_cnt

    neg30 = s.get("neg30", {})
    neg30_n = len(neg30.get("reviews", []))

    lines.append("=" * 100)
    lines.append(f"### {e['title']} ({appid}) [{e['lang_group']}]")
    lines.append(f"API(primary) {api_pct}% (pos={pos}/n={tot}) | store-all {store_pct}% (intel 09-07, n={it.get('total_reviews')}) | dev {dev:+.1f} | 72h delta {delta} (prev {prev_tot} -> {tot}) | new-in-window {new_cnt} | neg30 sample {neg30_n} | score_desc {prim_all.get('review_score_desc')}")
    for key in ["neg30", "all", "neg30_cn", "all_cn", "neg30_en", "all_en", "neg30_all", "all_all"]:
        if key not in s or s[key].get("error"):
            continue
        revs = s[key].get("reviews", [])
        if not revs:
            continue
        lines.append(f"--- sample[{key}] n={len(revs)} ---")
        for r in revs:
            vote = "👍" if r["voted_up"] else "👎"
            pt = r["playtime_min"] / 60
            txt = r["text"].replace("\n", " ⏎ ")[:600]
            lines.append(f"[{vote} {pt:.1f}h {hrs(r['ts'])}] {txt}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Saved {OUT}; total new-in-window (primary lang): {total_new}")
