#!/usr/bin/env python3
"""Daily player-voice fetcher: pull Steam reviews for all tracked apps (2026-08-26).
Note: outputs use _pv suffix to avoid collision with intel bot's same-day script.
New vs 08-25: + 无言之林 (3978240, en) first tracked 2026-08-25."""
import json, time, urllib.request

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-08-26_pv.json"

APPS = [
    ("1188710", "Bloodholic", "cn"),
    ("2993720", "Cage of Roses", "en"),
    ("3447920", "The Run", "en"),
    ("4234260", "主角", "cn"),
    ("3412900", "代号三国:龙起", "cn"),
    ("3711170", "冰点之下", "cn"),
    ("4104120", "对不起，我是警察", "cn"),
    ("3794770", "心之岛", "cn"),
    ("3831120", "江山北望", "cn"),
    ("3987560", "盛夏离与合", "cn"),
    ("4740420", "雪落情书时", "cn"),
    ("1353270", "Five Dates", "en"),
    ("1107790", "The Complex", "en"),
    ("3818020", "恶校游戏", "cn"),
    ("4855450", "不心动才有鬼", "cn"),
    ("4902060", "Libera Nos a Malo", "en"),
    ("2816920", "退婚后，宗主马甲藏不住", "cn"),
    ("3478050", "女王的游戏：盛世天下 媚娘篇", "cn"),
    ("4148240", "女王的游戏：盛世天下 女帝篇", "cn"),
    ("3756870", "Project DeepWeb: Eternal Nightmare", "en"),
    ("4412960", "光与影之恋", "cn"),
    ("4292950", "绍宋：还我河山", "cn"),
    ("3749320", "花满楼", "cn"),
    ("4734650", "请去Bar，恋爱吧！", "cn"),
    ("4846800", "1000王子: ChouChou Condo", "cn"),
    ("3978240", "无言之林", "en"),
]

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

def url(appid, lang, rtype, day=None):
    u = (f"https://store.steampowered.com/appreviews/{appid}?json=1"
         f"&language={lang}&review_type={rtype}&purchase_type=all&num_per_page=20")
    if day:
        u += f"&day_range={day}"
    return u

def simplify(rev):
    return {
        "voted_up": rev.get("voted_up"),
        "playtime_min": rev.get("author", {}).get("playtime_forever", 0),
        "text": rev.get("review", ""),
        "ts": rev.get("timestamp_created", 0),
    }

results = {}
for appid, title, lang in APPS:
    print(f"== {title} ({appid}) ==")
    primary = "english" if lang == "en" else "schinese"
    entry = {"app_id": appid, "title": title, "lang_group": lang, "samples": {}}
    jobs = [
        ("neg30", url(appid, primary, "negative", 30)),
        ("all", url(appid, primary, "all")),
    ]
    if lang == "en":
        jobs += [
            ("neg30_cn", url(appid, "schinese", "negative", 30)),
            ("all_cn", url(appid, "schinese", "all")),
        ]
    for key, u in jobs:
        data = fetch(u)
        time.sleep(1.2)
        if not data or data.get("success") != 1:
            entry["samples"][key] = {"error": True}
            print(f"  {key}: FAILED")
            continue
        qs = data.get("query_summary", {})
        entry["samples"][key] = {
            "num_reviews": qs.get("num_reviews"),
            "total_positive": qs.get("total_positive"),
            "total_negative": qs.get("total_negative"),
            "total_reviews": qs.get("total_reviews"),
            "review_score_desc": qs.get("review_score_desc"),
            "reviews": [simplify(r) for r in data.get("reviews", [])],
        }
        print(f"  {key}: {len(data.get('reviews', []))} reviews, pos={qs.get('total_positive')} neg={qs.get('total_negative')}")
    results[appid] = entry

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
print(f"\nSaved -> {OUT}")
