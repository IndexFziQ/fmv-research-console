#!/usr/bin/env python3
"""Fetch store-page overall review summary (all languages) via appreviews query_summary (2026-08-27, _pv suffix).
New vs 08-26: + 3978240 (无言之林)."""
import json, time, urllib.request

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_store_baseline_2026-08-27_pv.json"
APPS = ["1188710","2993720","3447920","4234260","3412900","3711170","4104120","3794770",
        "3831120","3987560","4740420","1353270","1107790","3818020","4855450","4902060",
        "2816920","3478050","4148240","3756870","4412960","4292950","3749320","4734650",
        "4846800","3978240"]
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) player-voice-bot/1.0"}

out = {}
for appid in APPS:
    url = (f"https://store.steampowered.com/appreviews/{appid}?json=1&language=all"
           f"&review_type=all&purchase_type=all&num_per_page=1")
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode("utf-8"))
        qs = d.get("query_summary", {})
        out[appid] = {
            "total_positive": qs.get("total_positive"),
            "total_negative": qs.get("total_negative"),
            "total_reviews": qs.get("total_reviews"),
            "review_score_desc": qs.get("review_score_desc"),
        }
        tp, tn = qs.get("total_positive") or 0, qs.get("total_negative") or 0
        pct = round(tp / (tp + tn) * 100, 1) if (tp + tn) else None
        print(f"{appid}: {tp}/{tp+tn} = {pct}% ({qs.get('review_score_desc')})")
    except Exception as e:
        out[appid] = {"error": str(e)}
        print(f"{appid}: FAILED {e}")
    time.sleep(1.0)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"saved -> {OUT}")
