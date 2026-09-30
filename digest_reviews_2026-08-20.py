#!/usr/bin/env python3
"""Digest raw reviews into readable per-app summary (2026-08-20)."""
import json

RAW = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-08-20.json"
OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_digest_2026-08-20.txt"

data = json.load(open(RAW, encoding="utf-8"))
lines = []
for appid, e in data.items():
    s = e["samples"]
    lines.append(f"\n{'='*80}\n### {e['title']} ({appid}) lang={e['lang_group']}")
    a = s.get("all", {})
    if not a.get("error"):
        tp, tn = a.get("total_positive"), a.get("total_negative")
        lines.append(f"[API query_summary all] pos={tp} neg={tn} -> {round(tp/(tp+tn)*100)}% (sample of {a.get('num_reviews')})")
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
            mark = "👍" if r["voted_up"] else "👎"
            hrs = round(r["playtime_min"]/60, 1)
            txt = r["text"].replace("\n", " ⏎ ").strip()
            lines.append(f"{mark} [{hrs}h] {txt}")

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print(f"digest -> {OUT}, {len(lines)} lines")
