#!/usr/bin/env python3
"""Daily intel fetch 2026-09-03: pull Steam reviews for all tracked apps.
Fetches: schinese lifetime, all-language lifetime, schinese day_range=7 (recent)."""
import json, time, urllib.request

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-09-03_pv.json"

# (appid, title, primary_lang)  cn=schinese-primary  en=english-primary
APPS = [
    ("1188710", "Bloodholic", "cn"),
    ("2993720", "Cage of Roses", "en"),
    ("3447920", "The Run", "en"),
    ("4234260", "主角", "cn"),
    ("3412900", "代号三国:龙起", "cn"),
    ("3711170", "冰点之下", "cn"),
    ("4104120", "对不起我是警察", "cn"),
    ("3794770", "心之岛", "cn"),
    ("3831120", "江山北望", "cn"),
    ("3987560", "盛夏离与合", "cn"),
    ("4740420", "雪落情书时", "cn"),
    ("1353270", "Five Dates", "en"),
    ("1107790", "The Complex", "en"),
    ("3818020", "恶校游戏", "cn"),
    ("4855450", "不心动才有鬼", "cn"),
    ("4902060", "Libera Nos a Malo", "en"),
    ("2816920", "退婚后,宗主马甲藏不住", "cn"),
    ("3478050", "女王的游戏:盛世天下 媚娘篇", "cn"),
    ("4148240", "女王的游戏:盛世天下 女帝篇", "cn"),
    ("3756870", "Project DeepWeb: Eternal Nightmare", "en"),
    ("4412960", "光与影之恋", "cn"),
    ("4292950", "绍宋:还我河山", "cn"),
    ("3749320", "花满楼", "cn"),
    ("4734650", "请去Bar,恋爱吧!", "cn"),
    ("4846800", "1000王子: ChouChou Condo", "cn"),
    ("3978240", "无言之林", "en"),
    ("4143220", "金宵公寓事件", "cn"),
    ("4699920", "天平游戏1:抉择", "cn"),
    ("4384120", "你好,你配吗?", "cn"),
    ("4108460", "灭寇1939:上川往事", "cn"),
    ("4056810", "东北往事", "cn"),
    ("3828610", "末日降临!被美女们关进避难所", "cn"),
    ("3155310", "阴三国谋论:徐州篇", "cn"),
    ("4867250", "夺命邂逅", "en"),
    ("4898630", "宗门最后的长老", "cn"),
]

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) intel-bot/1.0"}

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

def url(appid, lang, day=None):
    u = (f"https://store.steampowered.com/appreviews/{appid}?json=1"
         f"&language={lang}&review_type=all&purchase_type=all&num_per_page=20")
    if day:
        u += f"&day_range={day}"
    return u

def summarize(data):
    qs = data.get("query_summary", {})
    return {
        "num_reviews": qs.get("num_reviews"),
        "total_positive": qs.get("total_positive"),
        "total_negative": qs.get("total_negative"),
        "total_reviews": qs.get("total_reviews"),
        "desc": qs.get("review_score_desc"),
    }

results = {}
for appid, title, lang in APPS:
    entry = {"appid": appid, "title": title, "samples": {}}
    jobs = [
        ("zh_all", url(appid, "schinese")),
        ("all_all", url(appid, "all")),
        ("zh_7d", url(appid, "schinese", 7)),
    ]
    for key, u in jobs:
        data = fetch(u)
        time.sleep(1.0)
        if not data or data.get("success") != 1:
            entry["samples"][key] = {"error": True}
            continue
        entry["samples"][key] = summarize(data)
        qs = data.get("query_summary", {})
        print(f"{title}({appid}) {key}: n={qs.get('num_reviews')} pos={qs.get('total_positive')} neg={qs.get('total_negative')}")
    results[appid] = entry

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
print(f"\nSaved -> {OUT}")
