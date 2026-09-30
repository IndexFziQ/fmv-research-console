#!/usr/bin/env python3
"""Daily player-voice fetcher 2026-09-25 (Friday, issue #29): 36-pool / 35 collected.
Context: 09-24 (Thursday) full pipeline did not fire -> today's window spans 2 days:
last successful fetch completed 09-23 08:20. Rescue the Hostages 4619230 stays on
monthly scan (downgraded 09-23, English pool still 0; next scan ~10-23).
SOP: neg30 (day_range=30, review_type=negative) + all, primary lang per game;
english-group games also get schinese; 1000王子 supplements english+all-language pools.
Channels: neg30 / all / d3all (day_range=3 cursor-paginated <=8 pages, post-filtered by
CUTOFF 2026-09-23 08:20 in digest step) to capture 48h new-review full texts."""
import json, time, urllib.request, urllib.parse

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-25_voice.json"

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
    ("4143220", "金宵公寓事件", "cn"),
    ("4699920", "天平游戏1:抉择", "cn"),
    ("4384120", "你好，你配吗？", "cn"),
    ("4108460", "灭寇1939：上川往事", "cn"),
    ("4056810", "东北往事", "cn"),
    ("3828610", "末日降临！被美女们关进避难所!?", "cn"),
    ("3155310", "阴三国谋论: 徐州篇", "cn"),
    ("4920100", "列车怪谈：虚像之境", "cn"),
    ("4354460", "幸存者笔记", "cn"),
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

def fetch_dN(appid, primary, day=3, max_pages=8):
    """day_range=N channel: trailing-N-day reviews, cursor-paginated, dedup by ts+text prefix.
    NOTE: when window is empty API falls back to all-time list -> post-filter by CUTOFF in digest."""
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

results = {}
for appid, title, lang in APPS:
    print(f"== {title} ({appid}) ==", flush=True)
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
    if appid == "4846800":
        jobs += [
            ("neg30_en", url(appid, "english", "negative", 30)),
            ("all_en", url(appid, "english", "all")),
            ("neg30_all", url(appid, "all", "negative", 30)),
            ("all_all", url(appid, "all", "all")),
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
    # d3 channel: new review texts in trailing 3 days (window 09-23 08:20 -> 09-25)
    d3 = fetch_dN(appid, primary, day=3)
    entry["samples"]["d3all"] = {"num_reviews": len(d3), "reviews": d3}
    print(f"  d3all: {len(d3)} reviews in trailing 3d")
    results[appid] = entry

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
print(f"\nSaved -> {OUT}")
