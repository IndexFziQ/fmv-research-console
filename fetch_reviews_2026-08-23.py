#!/usr/bin/env python3
"""互动影游情报 · Steam 数据采集 (2026-08-23)
采集：① 28 个已追踪 appid 的评测 query_summary（schinese + all）+ 48h 增量
     ② 全语言商店页好评率基线（all）
     ③ Steam 搜索 FMV / 互动影游 / 真人互动 相关新上架 appid
输出：_raw_reviews_2026-08-23.json / _store_baseline_2026-08-23.json / _steam_search_2026-08-23.json
"""
import json, time, urllib.request, urllib.parse, re

OUT_R = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_raw_reviews_2026-08-23.json"
OUT_B = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_store_baseline_2026-08-23.json"
OUT_S = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/_steam_search_2026-08-23.json"

APPS = [
    ("3749320", "花满楼"),
    ("4292950", "绍宋:还我河山"),
    ("4855450", "不心动才有鬼"),
    ("3818020", "恶校游戏"),
    ("4412960", "光与影之恋"),
    ("4838470", "小小吸血姬"),
    ("4108460", "灭寇1939:上川往事"),
    ("3831120", "江山北望"),
    ("4148240", "女帝篇(女王的游戏)"),
    ("3478050", "媚娘篇(女王的游戏)"),
    ("3155310", "阴三国谋论:徐州篇"),
    ("4234260", "主角"),
    ("4699920", "天平游戏1:抉择"),
    ("3412900", "代号三国:龙起"),
    ("3711170", "冰点之下"),
    ("3987560", "盛夏离与合"),
    ("4740420", "雪落情书时"),
    ("4104120", "对不起我是警察"),
    ("3794770", "心之岛"),
    ("3447920", "The Run"),
    ("2993720", "Cage of Roses"),
    ("1188710", "Bloodholic"),
    ("1353270", "Five Dates"),
    ("1107790", "The Complex"),
    ("4868070", "Nocturne Hollow"),
    ("4902060", "Libera Nos a Malo"),
    ("2816920", "退婚后，宗主马甲藏不住"),
    ("3756870", "Project DeepWeb: Eternal Nightmare"),
]

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"}

def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", errors="replace")

def summary(appid, lang):
    """query_summary 全量 + filter=recent 时间窗 48h/7d 增量"""
    now = int(time.time()); d7 = now - 7*86400; d48 = now - 2*86400
    qs_url = (f"https://store.steampowered.com/appreviews/{appid}?json=1&language={lang}"
              f"&review_type=all&purchase_type=all&num_per_page=1")
    qs = json.loads(fetch(qs_url)).get("query_summary", {})
    allrevs, cursor, pages = [], "*", 0
    while cursor and pages < 20:
        cq = urllib.parse.quote(cursor, safe='')
        url = (f"https://store.steampowered.com/appreviews/{appid}?json=1&language={lang}"
               f"&review_type=all&purchase_type=all&num_per_page=100&filter=recent&cursor={cq}")
        d = json.loads(fetch(url))
        revs = d.get("reviews", [])
        if not revs:
            break
        allrevs.extend(revs)
        cursor = d.get("cursor", "")
        pages += 1
        if len(revs) < 100:
            break
    c7 = sum(1 for r in allrevs if r["timestamp_created"] >= d7)
    c48 = sum(1 for r in allrevs if r["timestamp_created"] >= d48)
    return {
        "total_reviews": qs.get("total_reviews"),
        "total_positive": qs.get("total_positive"),
        "total_negative": qs.get("total_negative"),
        "review_score_desc": qs.get("review_score_desc"),
        "cnt_7d": c7, "cnt_48h": c48,
    }

def search_ids(term):
    url = f"https://store.steampowered.com/search/?term={urllib.parse.quote(term)}&sort_by=Released_DESC&category1=998"
    html = fetch(url)
    ids = re.findall(r'data-ds-appid="(\d+)"', html)
    titles = re.findall(r'<span class="title">([^<]+)</span>', html)
    return [{"appid": i, "title": t} for i, t in zip(ids, titles)]

if __name__ == "__main__":
    reviews = {}
    for appid, title in APPS:
        entry = {"title": title}
        for lang, key in [("schinese", "zh"), ("all", "all")]:
            try:
                entry[key] = summary(appid, lang)
            except Exception as e:
                entry[key] = {"error": str(e)}
            time.sleep(0.6)
        reviews[appid] = entry
        zh = entry.get("zh", {}); al = entry.get("all", {})
        pct_zh = round(zh["total_positive"]/zh["total_reviews"]*100, 1) if zh.get("total_reviews") else None
        pct_all = round(al["total_positive"]/al["total_reviews"]*100, 1) if al.get("total_reviews") else None
        print(f"{appid} {title}: zh={zh.get('total_reviews')}/{pct_zh}% (48h={zh.get('cnt_48h')}) | all={al.get('total_reviews')}/{pct_all}% ({al.get('review_score_desc')})")
    with open(OUT_R, "w", encoding="utf-8") as f:
        json.dump(reviews, f, ensure_ascii=False, indent=1)
    print(f"saved -> {OUT_R}")

    # store baseline (all)
    base = {}
    for appid, title in APPS:
        try:
            base[appid] = summary(appid, "all")
        except Exception as e:
            base[appid] = {"error": str(e)}
        time.sleep(0.4)
    with open(OUT_B, "w", encoding="utf-8") as f:
        json.dump(base, f, ensure_ascii=False, indent=1)
    print(f"saved -> {OUT_B}")

    # search
    sres = {}
    for t in ["FMV", "真人互动", "互动影游", "interactive movie", "interactive fiction", "full motion video"]:
        try:
            sres[t] = search_ids(t)[:15]
        except Exception as e:
            sres[t] = {"error": str(e)}
        time.sleep(0.3)
    with open(OUT_S, "w", encoding="utf-8") as f:
        json.dump(sres, f, ensure_ascii=False, indent=1)
    print(f"saved -> {OUT_S}")
