#!/usr/bin/env python3
"""Digest raw player-voice reviews (2026-09-15): API pct vs store baseline,
24h weekday delta vs 09-14 raw, new review texts from d1all channel (ts >= CUTOFF).
Store baseline: TODAY's intel 2026-09-15 steam_reviews store_pct (all-language);
fallback to _pool.json (09-14 snapshot) if intel not yet on disk — noted in output."""
import json, datetime, os

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-15_voice.json"
PREV = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-14_voice.json"
INTEL = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/intel/2026-09-15.json"
POOL = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/products/_pool.json"
OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_digest_2026-09-15_voice.txt"

raw = json.load(open(RAW))
prev = json.load(open(PREV))
intel = {}
intel_src = "pool0914-fallback"
if os.path.exists(INTEL):
    intel = json.load(open(INTEL))
    intel_src = "intel0915"
istore = {r["appid"]: r for r in intel.get("steam_reviews", [])}
pool = {p["app_id"]: p for p in json.load(open(POOL))["products"]}

CUTOFF = int(datetime.datetime(2026, 9, 14, 8, 5).timestamp())  # last run window start

def hrs(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%m-%d %H:%M")

lines = [f"# BASELINE SOURCE: {intel_src}"]
total_new = 0
total_delta = 0
total_delta_pos = 0
total_delta_neg = 0
for appid, e in raw.items():
    p = pool.get(appid, {})
    s = e["samples"]
    prim_all = s.get("all", {})
    tot = prim_all.get("total_reviews")
    pos = prim_all.get("total_positive")
    neg = prim_all.get("total_negative")
    api_pct = round(pos / tot * 100, 1) if tot else None

    # store baseline: today's intel (all-language store pct)
    ir = istore.get(appid, {})
    store_pct = ir.get("store_pct", p.get("review_pct"))
    store_src = "intel0915" if ir else "pool"
    dev = round(api_pct - store_pct, 1) if api_pct is not None and store_pct else None

    prev_tot = None
    prev_pos = None
    prev_neg = None
    if appid in prev:
        pa = prev[appid]["samples"].get("all", {})
        prev_tot = pa.get("total_reviews")
        prev_pos = pa.get("total_positive")
        prev_neg = pa.get("total_negative")
    delta = (tot - prev_tot) if (tot is not None and prev_tot is not None) else None
    dpos = (pos - prev_pos) if (pos is not None and prev_pos is not None) else None
    dneg = (neg - prev_neg) if (neg is not None and prev_neg is not None) else None
    prev_pct = round(prev_pos / prev_tot * 100, 1) if (prev_pos and prev_tot) else None
    if delta and delta > 0:
        total_delta += delta
    if dpos: total_delta_pos += dpos
    if dneg: total_delta_neg += dneg

    # new reviews: d1all channel post-filtered by CUTOFF (weekday window 09-14 -> 09-15)
    d1 = s.get("d1all", {}).get("reviews", [])
    new_revs = [r for r in d1 if r["ts"] >= CUTOFF]
    total_new += len(new_revs)

    neg30 = s.get("neg30", {})
    neg30_n = len(neg30.get("reviews", []))

    lines.append("=" * 100)
    lines.append(f"### {e['title']} ({appid}) [{e['lang_group']}]")
    dev_s = f"{dev:+.1f}" if dev is not None else "n/a"
    lines.append(f"API(primary) {api_pct}% (pos={pos}/n={tot}) | store({store_src}) {store_pct}% | dev {dev_s} | 24h delta {delta} (posΔ{dpos}/negΔ{dneg}; prev {prev_tot} -> {tot}, prev_pct {prev_pct}) | NEW-TEXT captured {len(new_revs)} | neg30 sample {neg30_n} | score_desc {prim_all.get('review_score_desc')}")
    if new_revs:
        lines.append(f"--- NEW IN WINDOW (d1all, {len(new_revs)}) ---")
        for r in new_revs:
            vote = "👍" if r["voted_up"] else "👎"
            pt = r["playtime_min"] / 60
            txt = r["text"].replace("\n", " ⏎ ")
            lines.append(f"[{vote} {pt:.1f}h {hrs(r['ts'])}] FULLTEXT: {txt}")
    for key in ["neg30", "all", "neg30_cn", "all_cn", "neg30_en", "all_en", "neg30_all", "all_all"]:
        if key not in s or s[key].get("error"):
            continue
        revs = s[key].get("reviews", [])
        if not revs:
            continue
        lines.append(f"--- sample[{key}] n={len(revs)} ---")
        for r in revs:
            vote = "👍" if r["voted_up"] else "👎"
            pt = (r.get("playtime_min") or 0) / 60
            txt = r["text"].replace("\n", " ⏎ ")[:600]
            lines.append(f"[{vote} {pt:.1f}h {hrs(r['ts'])}] {txt}")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Saved {OUT}; baseline={intel_src}; total NEW-TEXT captured: {total_new}; primary-lang deltas: pos {total_delta_pos} / neg {total_delta_neg}")
