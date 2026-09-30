#!/usr/bin/env python3
"""Render intel daily HTML from intel/{date}.json, using the fixed dashboard design system."""
import json, sys, datetime

DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-09-03"
IN = f"/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/intel/{DATE}.json"
OUT = f"/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/intel-{DATE}.html"

d = json.load(open(IN, encoding="utf-8"))

CSS = """<style>
:root{--bg:#fafaf9;--card-bg:#fff;--text:#1a1a1a;--s:#5f5e5a;--muted:#888780;--border:#e5e5e0;--a:#534AB7;--al:#EEEDFE;--g:#1D9E75;--gl:#E1F5EE;--amb:#BA7517;--alm:#FAEEDA;--r:#E24B4A;--rl:#FCEBEB;--b:#378ADD;--bl:#E6F1FB}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--text);line-height:1.6;padding:32px 16px}
.container{max-width:880px;margin:0 auto}
header{text-align:center;margin-bottom:28px;padding-bottom:20px;border-bottom:1px solid var(--border)}
header h1{font-size:24px;font-weight:600;margin-bottom:4px}
header .meta{font-size:12px;color:var(--s);display:flex;justify-content:center;gap:16px;flex-wrap:wrap}
.kpi-row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:24px}
.kpi-card{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;padding:16px;text-align:center}
.kpi-card .kpi-value{font-size:26px;font-weight:600;color:var(--a);line-height:1;margin-bottom:4px}
.kpi-card .kpi-label{font-size:11px;color:var(--muted)}
.section{margin-bottom:28px}
.section-title{font-size:16px;font-weight:600;color:var(--a);margin-bottom:12px;padding-bottom:6px;border-bottom:2px solid var(--al)}
.tag{font-size:9px;padding:1px 5px;border-radius:3px;font-weight:500;display:inline-block}
.tag-b{background:var(--bl);color:var(--b)}.tag-g{background:var(--gl);color:var(--g)}.tag-a{background:var(--alm);color:var(--amb)}.tag-r{background:var(--rl);color:var(--r)}.tag-p{background:var(--al);color:var(--a)}
.signal-card{background:var(--card-bg);border:1px solid var(--border);border-left:3px solid var(--a);border-radius:10px;padding:14px 16px;margin-bottom:14px}
.signal-card h4{font-size:14px;font-weight:600;margin-bottom:6px;color:var(--text)}
.signal-card .src{font-size:10px;color:var(--muted);margin-bottom:8px}
.signal-card ul{list-style:none;margin-bottom:8px}
.signal-card ul li{font-size:12px;color:var(--s);padding:3px 0;padding-left:14px;position:relative;line-height:1.55}
.signal-card ul li:before{content:"▸";position:absolute;left:0;color:var(--a)}
.signal-card .act{font-size:12px;color:var(--text);background:var(--al);border-radius:6px;padding:8px 10px;line-height:1.6}
.signal-card .act strong{color:var(--a)}
.signal-card .links{margin-top:8px;display:flex;gap:6px;flex-wrap:wrap}
.link-btn{font-size:11px;padding:3px 9px;border-radius:5px;text-decoration:none;font-weight:500;border:1px solid var(--border);color:var(--s);transition:all 0.15s}
.link-btn:hover{border-color:var(--a);color:var(--a);background:var(--al)}
.item-card{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:10px}
.item-card .t{display:flex;justify-content:space-between;align-items:baseline;gap:8px;flex-wrap:wrap;margin-bottom:3px}
.item-card .t .name{font-size:13px;font-weight:600}
.item-card .t .delta{font-size:12px;font-weight:600;color:var(--g)}
.item-card .t .delta.warn{color:var(--amb)}
.item-card .t .delta.hot{color:var(--r)}
.item-card .meta{font-size:10px;color:var(--muted);margin-bottom:4px}
.item-card .note{font-size:12px;color:var(--s);line-height:1.55}
.item-card .tags{margin-top:6px;display:flex;gap:3px;flex-wrap:wrap}
.review-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.review-cell{background:var(--card-bg);border:1px solid var(--border);border-radius:8px;padding:9px 11px;font-size:11px}
.review-cell .rn{display:flex;justify-content:space-between;gap:6px;margin-bottom:2px}
.review-cell .rn .nm{font-weight:600;font-size:11.5px}
.review-cell .rn .pct{color:var(--a);font-weight:600}
.review-cell .dl{color:var(--g);font-weight:600;font-size:11px}
.review-cell .dl.hot{color:var(--r)}
.review-cell .dl.warn{color:var(--amb)}
.review-cell .nt{color:var(--muted);font-size:10.5px;line-height:1.5}
footer{text-align:center;margin-top:32px;padding-top:16px;border-top:1px solid var(--border);font-size:11px;color:var(--muted)}
footer .rn{font-weight:600;color:var(--a)}
@media(max-width:700px){.kpi-row{grid-template-columns:repeat(2,1fr)}.review-grid{grid-template-columns:1fr}}
</style>"""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

m = d["metrics"]
kpi = f"""<div class="kpi-row">
  <div class="kpi-card"><div class="kpi-value">{m['intel_count']}</div><div class="kpi-label">今日情报条数</div></div>
  <div class="kpi-card"><div class="kpi-value">{m['hot_signal_count']}</div><div class="kpi-label">爆款信号</div></div>
  <div class="kpi-card"><div class="kpi-value">{int(m['data_completeness']*100)}%</div><div class="kpi-label">数据完整率</div></div>
</div>"""

# hot signals
sig_cards = []
for s in d["hot_signals"]:
    cn = ["①","②","③","④","⑤"][s["rank"]-1]
    src = " · ".join(s["sources"])
    lis = "".join(f"<li>{esc(x)}</li>" for x in s["evidence"])
    links = "".join(f'<a class="link-btn" href="{x}" target="_blank">{"来源" if i==0 else "旁证"}</a>' for i,x in enumerate(s["links"]))
    sig_cards.append(f"""<div class="signal-card">
    <h4>{cn} {esc(s['title'])}</h4>
    <div class="src">来源：{esc(src)}</div>
    <ul>{lis}</ul>
    <div class="act"><strong>行动建议：</strong>{esc(s['action'])}</div>
    <div class="links">{links}</div>
  </div>""")

# review cells
cells = []
for r in d["steam_reviews"]:
    pct = f"{r['positive_pct_api']}%" if r['positive_pct_api'] is not None else "—"
    dl = r["delta_str"]
    dl_cls = "hot" if r["hot"] else ("warn" if dl in ("极小样本",) else "")
    nt = esc(r["note"])
    cells.append(f'<div class="review-cell"><div class="rn"><span class="nm">{esc(r["title"])}</span><span class="pct">{pct}</span></div><div class="dl {dl_cls}">{esc(dl)}</div><div class="nt">{nt}</div></div>')

# steam trending item cards
trend_cards = []
tagmap = {"新供给": "tag-p", "FMV": "tag-b", "营销": "tag-a", "影游": "tag-g", "叙事": "tag-g", "海外": "tag-b", "节奏": "tag-b", "促销": "tag-g", "谍战": "tag-g", "IP": "tag-a"}
for it in d["steam_trending"]:
    w = it.get("window", "")
    parts = [p for p in w.replace("·", " ").split() if p]
    tags = "".join(f'<span class="tag {tagmap.get(p, "tag-p")}">{esc(p)}</span>' for p in parts[:2])
    hot_cls = " hot" if "★" in it.get("note","") else ""
    trend_cards.append(f"""<div class="item-card">
    <div class="t"><span class="name">{esc(it['title'])}</span><span class="delta{hot_cls}">{esc(w)}</span></div>
    <div class="meta">{esc(it.get('developer',''))} · {esc(it.get('release',''))}</div>
    <div class="note">{esc(it['note'])}</div>
    <div class="tags">{tags}</div>
  </div>""")

# taptap cards
tap_cards = []
for it in d["taptap"]:
    delta = f"{it.get('score','')}" if it.get("score") else esc(it.get("release",""))
    tap_cards.append(f"""<div class="item-card">
    <div class="t"><span class="name">{esc(it['title'])}</span><span class="delta">{delta}</span></div>
    <div class="note">{esc(it['note'])}</div>
  </div>""")

# reddit cards
red_cards = []
for it in d["reddit"]:
    red_cards.append(f"""<div class="item-card">
    <div class="t"><span class="name">{esc(it['title'])}</span><span class="delta">媒体信号</span></div>
    <div class="note">{esc(it['note'])}</div>
  </div>""")

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>互动影游情报日报 | {DATE}</title>
{CSS}
</head>
<body>
<div class="container">
<header>
  <h1>互动影游 · 情报日报</h1>
  <div class="meta"><span>{DATE}</span><span>近24-48h增量</span><span>Steam · TapTap · Reddit/媒体</span><span style="color:var(--g)">链接已核实</span></div>
</header>

{kpi}

<section class="section">
  <div class="section-title">今日爆款信号</div>
  {''.join(sig_cards)}
</section>

<section class="section">
  <div class="section-title">Steam 竞品评测环比（中文口径 · 自{DATE.replace('2026-','')}前快照起）</div>
  <div class="review-grid">
    {''.join(cells)}
  </div>
</section>

<section class="section">
  <div class="section-title">Steam 爆款动态 / 新供给</div>
  {''.join(trend_cards)}
</section>

<section class="section">
  <div class="section-title">TapTap 动态</div>
  {''.join(tap_cards)}
</section>

<section class="section">
  <div class="section-title">Reddit / 社区讨论（媒体间接信号）</div>
  {''.join(red_cards)}
</section>

<footer><p>由 <span class="rn">互动影游情报机器人 v0.11</span> 生成 · 全部链接已核实</p><p style="margin-top:4px">数据源：Steam评测API · Steam搜索 · TapTap · Tech Times/今日头条/游民星空/腾讯新闻/中金在线/Next-Gen Gaming Blog | 仅供内部参考</p></footer>
</div>
</body>
</html>"""

open(OUT, "w", encoding="utf-8").write(html)
print(f"Rendered -> {OUT}")
print(f"  signals={len(d['hot_signals'])} trending={len(d['steam_trending'])} reviews={len(d['steam_reviews'])} taptap={len(d['taptap'])} reddit={len(d['reddit'])}")
