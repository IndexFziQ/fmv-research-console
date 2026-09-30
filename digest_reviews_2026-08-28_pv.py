#!/usr/bin/env python3
"""Digest raw reviews into readable per-app summary (2026-08-28, _pv) + day-over-day delta vs 08-27_pv."""
import json

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-08-28_pv.json"
PREV = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-08-27_pv.json"
OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_digest_2026-08-28_pv.txt"

data = json.load(open(RAW, encoding="utf-8"))
prev = json.load(open(PREV, encoding="utf-8"))

lines = []
# delta header: main-language pool totals
lines.append("### DAY-OVER-DAY (main-language pool: 08-27 -> 08-28)")
for appid, e in data.items():
    pe = prev.get(appid)
    key = "all"
    s = e["samples"].get(key, {})
    if not pe or s.get("error") or not s.get("total_reviews"):
        pct = round((s.get("total_positive") or 0) / s["total_reviews"] * 100, 1) if s.get("total_reviews") else None
        lines.append(f"  {e['title']}: NEW/NO-PREV {s.get('total_reviews')} | {pct}%")
        continue
    ps = pe["samples"].get(key, {})
    if ps.get("error") or not ps.get("total_reviews"):
        continue
    tot, ptot = s["total_reviews"], ps["total_reviews"]
    if tot != ptot:
        pct = round((s.get("total_positive") or 0) / tot * 100, 1)
        ppct = round((ps.get("total_positive") or 0) / ptot * 100, 1)
        lines.append(f"  {e['title']}: {ptot}->{tot} ({tot-ptot:+d}) | {ppct}% -> {pct}%")
    else:
        pct = round((s.get("total_positive") or 0) / tot * 100, 1) if tot else None
        lines.append(f"  {e['title']}: {ptot} (unchanged) | {pct}%")
lines.append("")

for appid, e in data.items():
    s = e["samples"]
    lines.append(f"\n{'='*80}\n### {e['title']} ({appid}) lang={e['lang_group']}")
    a = s.get("all", {})
    if not a.get("error"):
        tp, tn = a.get("total_positive"), a.get("total_negative")
        if tp is not None and (tp + tn):
            lines.append(f"[API query_summary all] pos={tp} neg={tn} -> {round(tp/(tp+tn)*100,1)}% (sample of {a.get('num_reviews')})")
    for key in ["neg30", "all", "neg30_cn", "all_cn"]:
        smp = s.get(key)
        if not smp or smp.get("error"):
            continue
        lines.append(f"\n--- {key} ({len(smp['reviews'])} reviews) ---")
        seen = set()
        for r in smp["reviews"]:
            if r["text"] in seen:
                continue
            seen.add(r["text"])
            mark = "+" if r["voted_up"] else "-"
            hrs = round(r["playtime_min"]/60, 1)
            txt = r["text"].replace("\n", " | ").strip()
            lines.append(f"{mark} [{hrs}h] {txt}")

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"digest -> {OUT}, {len(lines)} lines")
