#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate player-voice report 2026-09-23 (issue #28 make-up, 5-day window).
Design system identical to player-voice-2026-09-18.html (v1.1)."""
import re

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/player-voice-2026-09-23.html"

CSS = """:root{--bg:#fafaf9;--card-bg:#fff;--text:#1a1a1a;--s:#5f5e5a;--muted:#888780;--border:#e5e5e0;--a:#534AB7;--al:#EEEDFE;--g:#1D9E75;--gl:#E1F5EE;--amb:#BA7517;--alm:#FAEEDA;--r:#E24B4A;--rl:#FCEBEB;--b:#378ADD;--bl:#E6F1FB}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--text);line-height:1.5;padding:32px 16px}
.c{max-width:920px;margin:0 auto}
header{text-align:center;margin-bottom:24px;padding-bottom:18px;border-bottom:1px solid var(--border)}
h1{font-size:24px;font-weight:600;margin-bottom:4px}
header .sub{font-size:12px;color:var(--s)}
.hero{background:linear-gradient(135deg,var(--a),#3C3489);color:#fff;border-radius:14px;padding:28px 28px 20px;margin-bottom:24px}
.hero-tag{display:inline-block;font-size:10px;padding:2px 8px;border-radius:4px;background:rgba(255,255,255,0.18);margin-bottom:10px;letter-spacing:0.5px}
.hero h2{font-size:22px;font-weight:700;line-height:1.3;margin-bottom:6px}
.hero .lead{font-size:13px;opacity:0.85;line-height:1.6;max-width:680px;margin-bottom:16px}
.hero-stats{display:flex;gap:20px;flex-wrap:wrap}
.hero-stat{display:flex;flex-direction:column;background:rgba(255,255,255,0.12);border-radius:8px;padding:10px 16px;min-width:90px}
.hero-stat .hsv{font-size:26px;font-weight:700;line-height:1}
.hero-stat .hsl{font-size:10px;opacity:0.7;margin-top:2px;white-space:nowrap}
.quick-strip{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:28px}
.qcard{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;padding:12px;transition:box-shadow 0.15s}
.qcard:hover{box-shadow:0 2px 12px rgba(0,0,0,0.05)}
.qcard-top{display:flex;align-items:center;gap:8px;margin-bottom:6px}
.qcard .qicon{width:28px;height:28px;border-radius:6px;object-fit:cover;flex-shrink:0;background:var(--border)}
.qcard .qname{font-size:12px;font-weight:600;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.qcard .qrating{font-size:18px;font-weight:700;line-height:1}
.qcard .qrating.ok{color:var(--g)}.qcard .qrating.warn{color:var(--amb)}.qcard .qrating.bad{color:var(--r)}
.qcard .qbar{display:flex;height:4px;border-radius:2px;overflow:hidden;margin-bottom:6px}
.qcard .qbar .pos{background:var(--g)}.qcard .qbar .neg{background:var(--r)}
.qcard .qtag{font-size:10px;color:var(--muted);line-height:1.4}
.section{margin-bottom:28px}
.section-title{font-size:16px;font-weight:600;color:var(--a);margin-bottom:14px;padding-bottom:6px;border-bottom:2px solid var(--al);display:flex;align-items:center;gap:8px}
.section-title .st-num{font-size:10px;color:var(--muted);font-weight:400}
.pcard{background:var(--card-bg);border:1px solid var(--border);border-radius:12px;margin-bottom:18px;overflow:hidden;display:flex;flex-direction:column}
.pcard-header{display:flex;gap:16px;padding:16px 20px;background:var(--bg);border-bottom:1px solid var(--border);align-items:center}
.pcard-header .pcover{width:120px;height:68px;border-radius:6px;object-fit:cover;flex-shrink:0;background:var(--border)}
.pcard-header .pinfo{flex:1;min-width:0}
.pcard-header .pinfo .ptitle{font-size:15px;font-weight:600;display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:2px}
.pcard-header .pinfo .pmeta{font-size:11px;color:var(--muted);margin-bottom:6px;display:flex;gap:12px;flex-wrap:wrap}
.pcard-header .pinfo .pmeter{display:flex;height:6px;border-radius:3px;overflow:hidden;margin-bottom:4px}
.pcard-header .pinfo .pmeter .pos{background:var(--g)}.pmeter .neg{background:var(--r)}
.pcard-header .pinfo .pmeter-labels{display:flex;justify-content:space-between;font-size:10px;color:var(--muted)}
.pcard-body{padding:18px 20px}
.pcard-body .pb-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:700px){.pcard-body .pb-grid{grid-template-columns:1fr}.quick-strip{grid-template-columns:repeat(2,1fr)}}
.pb-block{margin-bottom:2px}
.pb-block h4{font-size:11px;font-weight:600;margin-bottom:6px;display:flex;align-items:center;gap:4px}
.pb-block h4 .hdot{display:inline-block;width:8px;height:8px;border-radius:50%;flex-shrink:0}
.pb-block h4 .hdot.neg{background:var(--r)}.pb-block h4 .hdot.pos{background:var(--g)}
.pb-list{list-style:none;display:flex;flex-direction:column;gap:4px}
.pb-list li{font-size:12px;color:var(--s);line-height:1.5;padding:4px 10px;border-radius:6px;transition:background 0.1s}
.pb-list li:hover{background:var(--bg)}
.pb-list .cnt{font-size:10px;color:var(--muted);background:var(--bg);padding:1px 6px;border-radius:3px;white-space:nowrap;flex-shrink:0}
.pb-list .q{display:block;font-size:10px;color:var(--muted);font-style:italic;margin-top:2px;line-height:1.4}
.pb-en{grid-column:1 / -1;font-size:11px;color:var(--s);background:var(--bg);border-radius:6px;padding:8px 12px;line-height:1.6}
.pb-en b{color:var(--a)}
.pcard-actions{padding:0 20px 18px}
.act-item{background:var(--al);border:1px solid var(--a);border-radius:8px;padding:10px 14px;margin-bottom:8px;display:flex;gap:10px;align-items:flex-start}
.act-item:last-child{margin-bottom:0}
.act-item .prio{display:inline-block;font-size:9px;padding:1px 6px;border-radius:3px;font-weight:700;flex-shrink:0;margin-top:1px}
.prio.p0{background:var(--r);color:#fff}.prio.p1{background:var(--amb);color:#fff}.prio.p2{background:var(--b);color:#fff}
.act-item .act-text{flex:1;min-width:0}
.act-item h4{font-size:12px;font-weight:600;margin-bottom:2px;color:var(--a)}
.act-item p{font-size:11px;color:var(--s);line-height:1.5}
.pattern-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:700px){.pattern-grid{grid-template-columns:1fr}}
.pat-card{background:var(--card-bg);border:1px solid var(--border);border-radius:10px;padding:18px;position:relative;overflow:hidden}
.pat-card::before{content:"";position:absolute;top:0;left:0;width:4px;height:100%;border-radius:2px 0 0 2px}
.pat-card:nth-child(1)::before{background:var(--a)}
.pat-card:nth-child(2)::before{background:var(--g)}
.pat-card:nth-child(3)::before{background:var(--amb)}
.pat-card:nth-child(4)::before{background:var(--r)}
.pat-card:nth-child(5)::before{background:var(--b)}
.pat-card:nth-child(6)::before{background:var(--a)}
.pat-card:nth-child(7)::before{background:var(--g)}
.pat-num{font-size:36px;font-weight:700;color:var(--border);line-height:1;margin-bottom:-10px}
.pat-card h4{font-size:13px;font-weight:600;margin-bottom:6px}
.pat-card p{font-size:12px;color:var(--s);line-height:1.5;margin-bottom:8px}
.pat-card .pat-tags{display:flex;gap:6px;flex-wrap:wrap}
.pat-card .pat-tags .tag{font-size:9px;padding:1px 7px;border-radius:3px;font-weight:600}
.tag.from{background:var(--rl);color:var(--r)}.tag.fix{background:var(--gl);color:var(--g)}
.self-eval{background:var(--card-bg);border:1px solid var(--amb);border-radius:10px;padding:18px;margin-top:24px}
.self-eval h4{font-size:14px;font-weight:600;color:var(--amb);margin-bottom:10px}
.se-grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px}
@media(max-width:700px){.se-grid{grid-template-columns:1fr}}
.se-item{text-align:center;padding:10px 8px;border-radius:8px;background:var(--bg)}
.se-item .score{font-size:30px;font-weight:700;line-height:1}
.se-item .score.r{color:var(--r)}.se-item .score.g{color:var(--g)}.se-item .score.a{color:var(--a)}
.se-item .lbl{font-size:10px;color:var(--muted);margin-top:4px}
.se-item .note{font-size:10px;color:var(--s);margin-top:6px;line-height:1.4}
.next-steps{margin-top:12px;padding:12px 16px;background:var(--bl);border:1px solid var(--b);border-radius:8px;font-size:12px;color:var(--b);line-height:1.6}
.next-steps strong{display:block;margin-bottom:2px}
footer{margin-top:32px;padding-top:16px;border-top:1px solid var(--border);text-align:center;font-size:11px;color:var(--muted)}
footer .rn{font-weight:600;color:var(--a)}"""

def stat_span(text, kind):
    color = {"g": ("var(--g)", "var(--gl)"), "r": ("var(--r)", "var(--rl)"), "a": ("var(--a)", "var(--al)"), "m": ("var(--muted)", "var(--bg)"), "amb": ("var(--amb)", "var(--alm)")}.get(kind, ("var(--muted)", "var(--bg)"))
    return f'<span style="font-size:11px;font-weight:400;color:{color[0]};background:{color[1]};padding:2px 8px;border-radius:4px">{text}</span>'

def li(label, cnt, quote):
    return f'<li>{label} <span class="cnt">{cnt}</span><span class="q">{quote}</span></li>'

def act(prio, title, body):
    return f'<div class="act-item"><span class="prio p{prio.lower()}">{prio}</span><div class="act-text"><h4>{title}</h4><p>{body}</p></div></div>'

def pcard(border, cover, title, spans, meta, pos_pct, blocks_html, actions_html):
    pos_w = int(round(pos_pct))
    neg_w = 100 - pos_w
    return f'''<div class="pcard" style="border-left:4px solid {border}">
  <div class="pcard-header">
    <img class="pcover" src="{cover}" alt="{title}" loading="lazy" onerror="this.style.display='none'">
    <div class="pinfo">
      <div class="ptitle">{title} {spans}</div>
      <div class="pmeta">{meta}</div>
      <div class="pmeter"><div class="pos" style="width:{pos_w}%"></div><div class="neg" style="width:{neg_w}%"></div></div>
      <div class="pmeter-labels"><span>好评 {pos_pct}%（API 中文口径）</span><span>差评 {100-pos_pct}%</span></div>
    </div>
  </div>
  <div class="pcard-body"><div class="pb-grid">{blocks_html}</div></div>
  <div class="pcard-actions">{actions_html}</div>
</div>'''

def qcard(cover, name, rating, cls, pos_w, tag):
    return f'''<div class="qcard">
  <div class="qcard-top"><img class="qicon" src="{cover}" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">{name}</span><span class="qrating {cls}">{rating}</span></div>
  <div class="qbar"><div class="pos" style="width:{pos_w}%"></div><div class="neg" style="width:{100-pos_w}%"></div></div>
  <div class="qtag">{tag}</div>
</div>'''

def pat(num, title, body, tags):
    tag_html = "".join(f'<span class="tag {t[0]}">{t[1]}</span>' for t in tags)
    return f'''<div class="pat-card">
  <div class="pat-num">{num:02d}</div>
  <h4>{title}</h4>
  <p>{body}</p>
  <div class="pat-tags">{tag_html}</div>
</div>'''

H = []
H.append(f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>玩家心声报告 v1.1 | 2026-09-23</title>
<style>{CSS}</style>
</head>
<body>
<div class="c">

<header>
  <h1>玩家心声报告 v1.1</h1>
  <div class="sub">互动影游竞品 · Steam 评测深读 · 2026-09-23（周三）· 池内 36 款全量采集（Rescue the Hostages 周扫恢复，英文池仍 0 条，维持月扫降频）· 第 28 期（补跑）· ⚠️ 本期为 5 日补跑窗口：09-21 周一运行中断（采集脚本已建、原始数据未落盘）、09-22 未触发，故窗口为 09-18 09:06 → 09-23 08:20，跨周末+停跑两日 · 全库主语言净增 +135（正 105 / 负 30），新评测原文捕获 145 条（捕获 ≥ 净增，窗口对账零缺口）· 数据口径：day_range=30 负面抽样 + 主语言全量抽样 + day_range=5 翻页捕获（中文游戏 schinese / 英文游戏 english，1000王子 补全语言口径）· 商店基线：pool0921 快照回退（intel 机器人自 09-18 起停更，已标注；intel 恢复后下期校正）</div>
</header>

<!-- ═══ Hero ═══ -->
<div class="hero">
  <div class="hero-tag">⚡ CORE FINDING</div>
  <h2>幸存者笔记起量第 8 日 413 条（+53）但好评率 92.2→89.8% 首次跌破 90——转折点不是 AI 也不是剧情，而是 09-18 一次「好感度系统更新」引入的回归 bug：旧进度无法获取好感度→主线卡死→官方回应「删档重玩」，单日制造 9+ 条差评（「上线一周买的就活该吃大便」）；修复后 Mac 端第七章资源损坏接棒。这是 AI 影游首个「更新回归」完整事故样本，与绍宋 BGM 混音盖台词（「你们自己不测试吗」）、列车怪谈跳过破坏故事线同日入库——上线后热修本身正在成为差评制造机</h2>
  <p class="lead">本期信号面：正面侧幸存者笔记仍以「目前最好的 AI 影游」命名潮领跑（多条「我用我的游戏库保证，没有之一」级好评 + B 站云通关补票 + 豆瓣 140 部全探索长评全文转载），剧情反转/伏笔回收/真人配音/配角（萝卜、释无禅、孔雀小队）被反复点名；3.9h 好评给出全库首条「双向粉丝服务」诉求（「女主战斗服没开奶窗我得给好评…男角色也卖起来，一起卖」）。女帝篇 5 日 +25 全库第二，配角引擎第七日扩展（府哥/礼忠/王皇后），但 CP 派系斗争公开化（「54党真的吐了」）且 AI 对话结局彩蛋被「严肃抵制」——AI 用途分界线在权谋正剧中再添反向判据。绍宋 +17（正 11/负 6）80.8% 平台期：战棋批评集中爆发（3 条「拿来做噱头营销」「ui像网页游戏」）+ BGM 混音事故。江山北望 +10 维持 91.3%。花满楼 5 日 posΔ-2（全库首见单款好评净减）+ 代号三国 posΔ-1 + The Complex negΔ-1——零清洗期后的微移除前哨观测重启；对不起警察 posΔ 前哨连续两日后归零（证伪为噪声）。金宵 55.6% 五连跌。列车怪谈 86.1%：跳过污染结局判定 bug 入库（重播层工程债族第 7 款）。</p>
  <div class="hero-stats">
    <div class="hero-stat"><span class="hsv">36</span><span class="hsl">池内产品（36 采集）</span></div>
    <div class="hero-stat"><span class="hsv">145</span><span class="hsl">5 日新评测原文捕获</span></div>
    <div class="hero-stat"><span class="hsv">+105/+30</span><span class="hsl">全库正/负净增</span></div>
    <div class="hero-stat"><span class="hsv">14</span><span class="hsl">行动卡（P0+P1 = 10）</span></div>
    <div class="hero-stat"><span class="hsv">7</span><span class="hsl">交叉模式（🆕×1）</span></div>
  </div>
</div>''')

# ═══ Quick Strip ═══
H.append('<div class="quick-strip">')
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4354460/8c136db542f3c9ac30ea86cf105014b99206d2f5/header_schinese.jpg?t=1789289866", "幸存者笔记", "89.8%", "warn", 90, "🟠 起量第 8 日：360→413（+53，正 39/负 4→实际正 39/负 14），92.2→89.8%（-2.4）首破 90 · 🔴 09-18 好感度更新回归 bug：旧进度无法获取好感度→主线卡死→「删档重玩」，9+ 条差评，修复后 Mac 第七章资源损坏接棒 · praise：「目前最好的 AI 影游」命名潮/B站云通关补票/豆瓣长评全文转载 · 🆕全库首条「双向粉丝服务」诉求"))
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4292950/dfd52caf6453e43b4d613a662064aca4924a7858/header.jpg?t=1787201131", "绍宋", "80.8%", "ok", 81, "🟠 +17（正 11/负 6）80.8% 持平 · 🆕P0 音频混音事故：「背景音乐太tm大了，完全听不清过程在讲什么？你们自己不测试吗」+ 漫画环节音量骤降 · 战棋批评集中爆发 ×3（「拿来做噱头营销」「ui像网页游戏」）· AI 配音出错/妆容网红感 · praise：演技在线/家国情怀/DLC 呼声（43.1h「出必买」）"))
H.append(qcard("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg", "女帝篇", "82.5%", "ok", 83, "🟢 +25（正 22/负 3）82.5% 持平，全库第二 · 配角引擎第七日（府哥眼神/礼忠/王皇后气场/龙袍服化道）· 🔴 CP 派系斗争公开化：「54党真的吐了」 vs 95线 · 🆕AI 对话结局彩蛋被「严肃抵制」（11.8h 好评内嵌）· 历史观批评（「贬唐抬蛮夷」17.5h）"))
H.append(qcard("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3831120/6a5af0317c2156f49b790588f09484e1f63cbbed/capsule_616x353.jpg", "江山北望", "91.3%", "ok", 91, "🟢 +10（正 8/负 2）91.3% 持平 · praise 顶点：8.9h 长评「北地子民终其一生盼王师而不得，王师，王师，王师何日北上？」（历史意难平情感兑现最高级样本）· 🆕新差评：鼠标动作场景 UI 提示缺失（「用鼠标玩你所谓的『动作场景』跟赤石一样」7.0h）"))
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3749320/912e382a3edc1ccd8f6f71e05317b0ff312b84af/header_schinese.jpg?t=1787291920", "花满楼", "97.4%", "warn", 97, "🟠 5 日 posΔ-2（1487→1486，差评 +1）——零清洗期后全库首见单款好评净减，微移除前哨观测重启（与代号三国 posΔ-1、The Complex negΔ-1 并列三日观测点）· 若下期续负 → 按审计前哨提高警戒级 · 在池：1080p/50G、条件达成不显示绿色"))
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4920100/aecf4db2323a4eebc76013235e0091fd07a600a2/header_schinese.jpg?t=1788225078", "列车怪谈", "86.1%", "warn", 86, "🟠 +4（正 3/负 1）86.8→86.1 · 🆕跳过污染结局判定 bug：10.9h 玩家「跳过看过片段容易出bug…打不出自己想要的结局，只能从头一个片段一个片段正常过」——重播层工程债族第 7 款 · 全库首条无障碍信号：键盘 D 键损坏玩家「屏幕键盘无法在游戏内使用」（QTE 键位自定义诉求）"))
H.append('</div>')

# ═══ Per-product section ═══
H.append('<div class="section">')
H.append('<div class="section-title">逐款分析 <span class="st-num">36 款 · 按信号强度排序 · 好评率为 API 抽样（已与商店页基线比对，基线取 pool0921 快照回退——intel 自 09-18 停更，恢复后下期校正）</span></div>')

# --- 幸存者笔记 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（好感度事故 + 画质族延续，5 日 14 条新差评）</h4><ul class="pb-list">'
blocks += li("🆕 好感度系统更新回归 bug（P0 工程事故）", "×6", "「你妈你今天更新的好感度系统是什么玩意，直接卡进度，旧进度无法获得好感度」（13.7h 09-18 13:03）/「最新的更新会导致卡关，无法获取好感度，这个问题，制作组都测试不出来…让玩家花钱帮你测BUG来的？」（6.3h 09-18 16:00）/「你把我剧情卡了，然后告诉我要删档重玩？？？？什么时候改回来什么时候好评」（3.7h 09-22）/「和我说好感度问解决不了了，哦上线一周买的就活该吃大便，还要删文件重看」（12.2h 09-20）——09-18 更新引入回归，主线刚需女主好感度 → 全进度卡死；官方回应「删档重玩」直接把存量玩家推向差评。已有玩家二改确认修复（6.4h「二改：好感度问题修复了 顺利通过第五章 但是mac会在第七章审问出现资源已损坏」）——修复后 Mac 端第七章崩坏接棒")
blocks += li("画质糊 / 720P 族延续（高画质包诉求在池）", "×3", "「背景画质太糊了，在我2k屏上很多背景都是马赛克，AI涂抹的痕迹很重」（2.9h 09-22 好评内嵌）/「画质太差，像720P」（3.0h 09-19）/ neg30 在池「压缩率太高 画质都糊的，连高码率的720P都不如。其他影游也有高画质包下载的选项，强烈建议增加高画质」——画质债与 30G 体量叠加，被多名玩家点名")
blocks += li("剧情逻辑批评（降智/为悲而悲）", "×2", "「屎一般的剧情，为了悲剧而悲剧，编剧的水平功底非常差…全员脑瘫，降智」（1.5h 09-21）/「剧情纯傻逼 纯无脑 我尼玛真是后悔花钱买了…几个路人尼玛也来参加重要行动」（3.0h 09-19）——AI 量产路线的剧本逻辑质检债延续")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 39 条新好评，AI 影游口碑双样本主证据侧）</h4><ul class="pb-list">'
blocks += li("「目前最好的 AI 影游」命名潮", "×4", "「这是目前我见到各方面表现都比较均衡的AI互动影游…整体感觉更像没有战斗打斗过程的准3A游戏」（25.4h 09-19 长评）/「我愿称之为：目前最好的AI影游，我用我的游戏库保证，没有之一」（8.4h 09-20）/「就这么和你说在2026年九月这个为节点！是迄今为止最好的AI游戏！和今年最好的影游！」（30.8h 09-22）/「至今玩过最用心的AI游戏」（29.2h 09-20）——与列车怪谈「AI 适合恐怖题材」构成 AI 影游双样本，且幸存者被玩家置于「断代最佳」位置")
blocks += li("剧情反转 / 伏笔回收 / 配角魅力", "×5", "「结尾还把前面铺垫的都完美的圆回来…编剧真的无敌我只能说」（12.0h 09-20）/「剧本质量很高，反转多、伏笔回收完整，人物塑造比较立体。特别喜欢释无禅启动精元战甲BOSS战那段，太燃了」（22.8h 09-19）/「相当于看了个不断反转的电影」（2.6h 09-19）/「男女主线真的很好磕，但是我个人还是更喜欢萝卜…变态三人组和孔雀小队的人设也确实让人记忆犹新」（16.5h 09-19）/「我最喜欢的角色是稀无禅，又酷又很神秘。那场打斗简直把我弄得浑身沸腾」（13.4h 09-19）——配角引擎在 AI 路线同样成立")
blocks += li("B 站云通关补票 + 豆瓣长评全文转载", "×2", "「没玩，但在b站云通关了纯净流的剧情，过来补票的。不希望优秀的制作组就此埋没」（0.2h 09-20）——云通关→付费补票的转化路径首证；35.2h 玩家将豆瓣 140 部全探索长评全文转载进 Steam 评测区（「第140部互动影游…评分架构：4-0.5=3.5」）——深度认可样本 + 「直播/云观看」渠道价值再确认")
blocks += li("🆕 女性向设计敏感度 / 双向粉丝服务诉求（全库首条）", "×1", "「女主简直帅爆，而且战斗服装没有开奶窗我得给好评。两个女医师也没有穿得很暴露，挺好的…希望以后不仅仅是女角色爆衣，男角色也卖起来，一起卖」（3.9h 09-23 07:13 今日晨间新好评）——「不开奶窗」被作为好评理由点名 + 男女角色同等待遇的粉丝服务诉求首次显形")
blocks += '</ul></div>'
actions = act("P0", "更新回归测试 SOP：热修本身需要全平台回归清单", "好感度事故完整链路：09-18 更新引入回归 → 主线刚需依赖好感度 → 全进度卡死 → 官方回应「删档重玩」激化差评 → 修复后 Mac 端第七章资源损坏接棒。对自家：① 任何更新上线前对「主线刚需依赖项」（好感度/存档/关键道具）跑回归用例；② 热修回应话术禁用「删档重玩」，先做存档兼容迁移；③ Mac/多平台同步回归；④ 监控「更新后 48h 差评突增」作为事故信号——本期 9+ 条差评本可全部避免。")
actions += act("P1", "存档卫生四件套第五证 + 快退/倍速诉求", "22.8h 好评点名「没有快退键，想回看剧情，只能返回重新看」；0.9h 好评「希望有2倍速模式」；云存档缺失差评在池（「换个电脑就没存档真牛」）；高画质包诉求在池。跳过/倍速 + 分段进度条 + 读档防剧透 + 云存档/自动存档四件套在 AI 长体量产品中已是逐条被点名的基本盘。")
actions += act("P2", "双向粉丝服务：女性向与男性向审美的平衡点", "3.9h 好评证明「不开奶窗」本身可以成为好评理由（女性向玩家用购买投票），同篇提出「男角色也卖起来」。对自家：粉丝服务设计应做性别双向预算，女性向玩家是 AI 路线（无真人卡司红利）的重要增量客群。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4354460/8c136db542f3c9ac30ea86cf105014b99206d2f5/header_schinese.jpg?t=1789289866", "幸存者笔记",
    stat_span("🟠 起量第 8 日 +53 但 92.2→89.8% 首破 90：好感度更新事故单日制造 9+ 差评", "amb") + " " + stat_span("API 89.8% / 商店 90.5%（-0.7 ✓）", "m"),
    "<span>MYSTERY CROWN · YESPLAY · 2026-09-11 · 全 AI 虚拟真人末日丧尸 FMV</span><span>30天差评 20</span><span>评测池 413（中文，5d +53：正 39/负 14）</span>",
    89.8, blocks, actions))

# --- 绍宋 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（5 日 6 条新差评，音频与战棋集中）</h4><ul class="pb-list">'
blocks += li("🆕 音频混音事故：BGM 盖过台词（P0）", "×2", "「背景音乐太tm大了，完全听不清过程在讲什么？你们自己不测试吗？？？？」（17.1h 09-19 差评）/「一到漫画环节视频的声音就变得小小的，希望官方予以改进！」（15.5h 09-19 好评内嵌）——同一产品两类音量问题并存（BGM 过大 + 过场音量骤降），响度未做归一化；「你们自己不测试吗」直指验收缺位")
blocks += li("战棋批评集中爆发", "×3", "「1/3内容是AI和不明所以的战棋（完全没有任何策略、只能按顺序点击、点完加一些莫名其妙的资源的战棋）…这战棋还拿来做噱头营销 我真笑不活了」（10.0h 09-20）——「提名2026最难绷影游」长评；「那个战棋，更加潦草…ui像网页游戏，没有逻辑」（5.3h 09-20 原著粉差评）/「战棋是不是做的有些太low了」（3.9h 09-23 差评）——战棋从「可跳过的瑕疵」升级为差评主因")
blocks += li("AI 配音出错 + 妆容网红感", "×1", "「ai属实难绷，ai配音还有不少出错的地方，女角色的妆容网红感太强很出戏，游戏的跳转衔接不够流畅，画幅也有问题」（12.1h 09-18 好评内嵌）——AI 分界线反向判据：配音层出错比画面层更伤")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 11 条新好评）</h4><ul class="pb-list">'
blocks += li("演技认可 + 战棋双面证据", "×2", "「老实说，这剧可以直接上映了，不少演员演技都在线。比小鲜肉啥的好多了」（17.0h 09-20）/「作为战棋爱好者，游戏里穿插的战棋也很喜欢玩！总之推荐」（3.7h 09-19）——同一战棋系统在细分受众处获得正反馈：批评的真正焦点是「无策略深度却当卖点」，而非战棋本身")
blocks += li("家国情怀 + DLC 呼声", "×2", "「配乐恰到好处，家国情怀拉满」（7.7h 09-21）/「无意义甚至无好感度的二选一太多了，剧情等DLC可以继续延伸，出必买」（43.1h 09-18）——43.1h 深时长玩家的 DLC 预购承诺（IP 生命周期信号）")
blocks += li("改编中评样本（好评内嵌批评层）", "×1", "「作为改编自小说《绍宋》的真人互动影视游戏…在剧情表现和逻辑上，许多剧情就像主角是参与表演的嘉宾、而其他角色则是一群演员在cos情景剧一样单纯且略显违和」（9.4h 09-20 长评「虽然不比原作，但至少也是穿越爽文」）——「短剧式影游化」改编路径的理性中评")
blocks += '</ul></div>'
actions = act("P0", "音频响度归一化验收：混音检查清单进上线 SOP", "BGM 盖台词 + 漫画段音量骤降同日入库，且被玩家归因于「不测试」——混音问题是最廉价的差评来源（5 分钟能修）却最伤沉浸。对自家：① 全片响度归一化（对白轨 vs BGM 轨 LUFS 标准）；② 过场/插叙/漫画段三类非主线素材单独音量验收；③ 「静音 BGM 只听台词」的辅助开关。")
actions += act("P1", "战棋与叙事的情绪衔接：机制段应是放大器而非重置器", "在池批评「一场战斗演到一半突然来个战棋再从头打一遍，割裂玩家情绪」+ 本期 3 条集中爆发，但战棋爱好者同时给出正评。结论：战棋问题不是「做不做」而是「怎么嵌」——① 战棋胜负应衔接剧情分支而非重播同一段战斗；② 若无策略深度则不得作为营销卖点（「拿来做噱头营销」是差评导火索）；③ 默认可跳过 + 跳过不惩罚（已有，需在商店页明示）。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4292950/dfd52caf6453e43b4d613a662064aca4924a7858/header.jpg?t=1787201131", "绍宋：还我河山",
    stat_span("🟠 +17（正 11/负 6）80.8% 持平：BGM 混音事故 + 战棋批评集中爆发", "amb") + " " + stat_span("API 80.8% / 商店 80.1%（+0.7 ✓）", "g"),
    "<span>互动之星 · 猫眼娱乐 · 2026-08-20 · 历史正剧 FMV（南宋抗金）</span><span>30天差评 20</span><span>评测池 2773（中文，5d +17）</span>",
    80.8, blocks, actions))

# --- 女帝篇 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（5 日 3 条新差评 + 派系斗争显形）</h4><ul class="pb-list">'
blocks += li("🆕 CP 派系斗争公开化（54党 vs 95线）", "×1", "「54党真的吐了」（9.5h 09-22 02:57）+ neg30 在池「对得起我们54玩家吗？在架空历史线说历史…甚至到最后分别的时候连一个给玩家选择的权利都没有」——系列 CP 战争从隐性偏好分歧升级为公开派系攻击（54线玩家认定 95线挤压了自己的叙事空间）")
blocks += li("剧情批评层（宝宝权谋 / 为死而死 / 编剧强加）", "×3", "「45线的剧情拿脚写也就算了，95线又好到哪里？…某些角色的下线完全是为了死而死…除了服化道和导演厉害剧情就是一坨，玩完难受一整天」（14.4h 09-22 差评）/「宝宝权谋…最后登基的部分太草率了。容错率比史实还低」（19.8h 09-22 好评内嵌）/「给三星不能再多了…选项丝毫经不起推敲，全凭运气闭眼瞎选才能过。编剧的个人喜好强加于玩家，这一点非常恶心」（5.7h 09-20 差评）")
blocks += li("🆕 历史观批评（贬唐抬蛮夷）", "×1", "「到了支线徐敏慧时，他竟然为了贬低唐朝中原而去抬蛮夷游牧…武则天能当上皇帝…还得益于当时的社会足够开放，这都要贬低一下来去抬蛮夷游牧，编剧你是马粪吃多了？」（17.5h 09-19 差评）——历史改编的价值观审查压力（历史正剧受众对「立场先行」高度敏感）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 22 条新好评，配角引擎第七日）</h4><ul class="pb-list">'
blocks += li("配角引擎第七日（反派层 + 忠仆层双供给）", "×3", "「武媚娘对李益府掏心窝子，府哥的眼神给我看哭了，太燃了卧槽。全剧最好看的我认为是王皇后和高阳，越看越带劲」（27.4h 09-23 今日新评）/「礼忠真的太让人心疼了，一个小孩子被卷进这些事情里，看他每次小心翼翼的样子都很心疼」（5.1h 09-20）/「刘熙恨了小伍半生，最后才发现恨错了人，空恨一场，我看的时候非常解气！」（5.1h 09-18）——反派、忠仆、悔恨者三层配角各自产出独立口碑")
blocks += li("服化道 + 沉浸时长证据", "×3", "「服化道非常在线，小伍好多套衣服都好好看…尤其龙袍那套，太霸气了吧，一出来气场直接变了」（5.8h 09-22）/「女帝篇内容是真的好多，本来想着刷两集就睡，结果一玩就好几个小时，完全停不下来」（5.3h 09-21）/「拍的比第一部还好 越杀越兴起 一不小心天都亮了」（6.5h 09-21 好评内嵌军营剧情批评）——「熬夜通关」是沉浸强度的行为证据")
blocks += li("🆕 AI 对话结局彩蛋被抵制（好评内嵌批评）", "×1", "「这最后怎么还搞上ai对话啦，严肃抵制严肃抵制。这个游戏给7分及格分，全程忍俊不禁，后思之又令人发笑」（11.8h 09-20 好评）——与 neg30 在池「差评给垃圾ai…你ai生成的段落能不能删一下八股」同向：AI 内容出现在叙事关键节点（结局彩蛋）触发「严肃抵制」级反感")
blocks += '</ul></div>'
actions = act("P1", "AI 生成内容的 opt-out 与披露粒度", "女帝 AI 对话彩蛋被「严肃抵制」、AI 段落被要求「删八股」，而幸存者全 AI 画面获「断代最佳」——分界线精化为：<b>AI 可承担画面层（氛围/大场面），不可承担叙事关键节点（结局语义/角色对话）</b>。对自家：① AI 生成内容显式标注 + 可关闭；② AI 不进入结局/彩蛋等情感结算区；③ 配音层禁用 AI（绍宋 AI 配音出错同向）。")
actions += act("P2", "CP 派系的运营化管理：把派系战争变成 DLC 路线图", "54党/95线公开冲突 + 李泰线 BE→HE 呼声（5.8h「为什么他们二人就不能有happy end呢」）+ 媚娘篇高阳争议——多 CP 产品的派系情绪需要出口。对自家：DLC/番外路线图显式回应各派系诉求（一条 BE 逆转线即可安抚一整个派系），把派系能量转化为复购而非差评。")
H.append(pcard("var(--g)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg", "女王的游戏：盛世天下 女帝篇",
    stat_span("🟢 +25（正 22/负 3）82.5% 持平：配角引擎第七日，AI 彩蛋抵制 + 54/95 派系公开化", "g") + " " + stat_span("API 82.5% / 商店 82.3%（+0.2 ✓）", "g"),
    "<span>New One Studio · 2026-06-08 · 宫廷权谋 FMV</span><span>30天差评 20</span><span>评测池 7832（中文，5d +25）</span>",
    82.5, blocks, actions))

# --- 江山北望 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（5 日 2 条新差评）</h4><ul class="pb-list">'
blocks += li("🆕 鼠标动作场景 UI 提示缺失", "×1", "「用鼠标玩你所谓的『动作场景』跟赤石一样，有些 UI 该怎么操作连个像样的提示都没有，能别牛魔过度设计吗？」（7.0h 09-21 差评）——交互段（动作场景/QTE）的操作引导缺位；与 neg30 在池「弄这么多弱智QTE是干什么」同族但新增了「无提示」维度")
blocks += li("剧本强迫推进批评", "×1", "「感觉像是被剧本强迫强迫推着走，以及我想问一下，现实中真有这么倒霉熊的皇帝么？」（5.8h 09-19 差评）——「主角主动性不足」批评的新短样本（与 08-28 3.9h 长评「棋盘搭得很好，但游戏不太想让我下棋」同框架）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 8 条新好评）</h4><ul class="pb-list">'
blocks += li("历史情感唤起顶点样本（王师何日北上）", "×1", "「从前学历史，很感慨的一段史事就是西晋灭亡…北地子民终其一生盼王师而不得，王师，王师，王师何日北上？」（8.9h 09-20 长评）——历史意难平的情感兑现路径最高级措辞；同篇给出「整体立意十分优秀」定性")
blocks += li("立意 + 遗憾美学 + 情绪浓度", "×3", "「好玩，剧情不错，最终的结局每一种都或多或少会留下遗憾」（15.8h 09-20）/「很有精神 去tma女人 北伐北伐」（15.1h 09-20——情绪浓度样本）/「穷了点，但是剧情什么没毛病」（7.4h 09-19）——「穷但值」叙事在好感侧稳定运转")
blocks += li("群演经费内嵌批评（好评侧自曝）", "×1", "「感觉一些表演还是不是很好，而且一些剧情经不起推敲。尤其是群演经费都不足啊」（8.1h 09-19 好评内嵌）——与 09-07「哪怕用AI生成一下呢？几万人打斗的场面」构成同一玩家群体的两副面孔：理解穷，但期待大场面（AI 需求信号）")
blocks += '</ul></div>'
actions = act("P1", "交互段的操作教学：动作场景前置 3 秒操作预览", "「UI 该怎么操作连个像样的提示都没有」+ 在池 QTE 批评——动作/QTE 段需要在触发前给出操作说明（键位高亮 + 3 秒练习预览），而非靠玩家死亡后试错。低成本高收益：一条提示文案可挡一条差评。")
H.append(pcard("var(--g)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3831120/6a5af0317c2156f49b790588f09484e1f63cbbed/capsule_616x353.jpg", "江山北望",
    stat_span("🟢 +10（正 8/负 2）91.3% 持平：「王师何日北上」历史情感顶点样本", "g") + " " + stat_span("API 91.3% / 商店 91.0%（+0.3 ✓）", "g"),
    "<span>木焱工作室 · 2025-11-19 · 大宋历史权谋 FMV</span><span>30天差评 18</span><span>评测池 6276（中文，5d +10）</span>",
    91.3, blocks, actions))

# --- 媚娘篇 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（5 日 1 条新差评 + 全收集引导缺口显形）</h4><ul class="pb-list">'
blocks += li("新差评（开局即 GameOver 型）", "×1", "「垃圾游戏，游戏里面的人物心理变态的：游戏开头如实告之那东西是刘熙的，就被韦贵妃打入监牢受刑了，GameOver」（0.1h 09-21）——「如实选择即死」的引导缺位极端样本（0.1h 内退出打差评）")
blocks += li("在池批评框架延续", "在池", "选择无意义/强制联网+充值/登录故障（系列级工程债）批评框架延续，5 日无新增实质差评")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 新增观测（5 日 9 条新好评，探索度诉求 + 情感浓度）</h4><ul class="pb-list">'
blocks += li("🆕 探索度 100% 达成困难（全收集引导缺口）", "×2", "「每个选项都死一次才能推进剧情吗……」（3.4h 09-19 好评内嵌）/「探索进度百分百太难达成了，有些分支太细还重复频繁。作为一个橙光老玩家…有的选项还是有点离谱」（8.8h 09-22）——与恶校「探索度每章都没有满，求指点」同族同厂：全收集系统的达成路径不透明是系列级缺口")
blocks += li("情感浓度 + 篇章认可", "×3", "「媚娘好可爱！！李治和李泰也很帅…总体已经很不错用心了」（8.8h 09-22）/「挺好玩的，就是喝桂花羹死了好几次，高阳线好无力啊，泪点好足，故事线再长点就好了」（8.6h 09-22）/「非常好。很棒的游戏体验。角色演技都在线。辩机篇拍的无敌了」（5.8h 09-19）——「辩机篇拍的无敌了」为篇章级口碑新锚点")
blocks += li("20.6h 长评理性好评（改编狂悖的宽容）", "×1", "「剧情挺牛的 制作真是精良 权谋环环入扣（指死的很合理而且出乎意料）…魏王帮我掩盖尸体 做兄弟真是一流 就是改编的比历史上还狂悖…李二像个死人一样」（20.6h 09-18）——深度玩家对「戏剧化加工」的宽容框架：接受狂悖、批评逻辑")
blocks += '</ul></div>'
actions = act("P1", "全收集引导：探索度面板 + 遗漏提示", "媚娘「探索进度百分百太难达成」+ 恶校「探索度每章都没有满，求指点」——同厂两款产品的同一缺口已交叉验证：玩家不知道遗漏在哪。对自家：① 章节完成度面板（已探索节点计数）；② 通关后解锁「遗漏分支提示」（模糊提示避免剧透）；③ 死路/BE 的路线图回看。")
H.append(pcard("var(--amb)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3478050/0e3d390564332c03dd980d0b295cb533d0ecb7a7/capsule_616x353_schinese.jpg", "女王的游戏：盛世天下 媚娘篇",
    stat_span("🟠 +9（全正）82.9% 持平：探索度诉求显形，辩机篇口碑锚点确立", "amb") + " " + stat_span("API 82.9% / 商店 86.7%（-3.8 口径差：中文 vs 全语言）", "m"),
    "<span>New One Studio · 2025-09-08 · 宫廷生存 FMV 上部</span><span>30天差评 18</span><span>评测池 9457（中文，5d +9）</span>",
    82.9, blocks, actions))

# --- 列车怪谈 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（跳过 bug 新证）</h4><ul class="pb-list">'
blocks += li("🆕 跳过污染结局判定 bug（重播层工程债族第 7 款）", "×1", "「给差评的主要原因是跳过看过片段容易出bug，如果想玩别的结局必须从头来过不能跳视频，如果跳视频可能就会导致故事线混乱，打不出自己想要的结局…我又从第一章一个片段一个片段正常过，才将故事线拉回来，打出隐藏结局」（10.9h 09-19 差评）——跳过操作改变结局结算（好感度证据线判定被跳过污染）：与探索度统计 bug（09-09 好评改差评样本）同属「重播层状态管理」缺陷")
blocks += li("在池批评框架延续", "在池", "U盘证据链 bug 卡死（「什么时候修复了这个恶心bug，什么时候改评价」）/ AI 味/选项无逻辑批评延续，5 日无新增")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 新增观测（5 日 3 条新好评）</h4><ul class="pb-list">'
blocks += li("AI 塑料感的中性接受（低价缓冲）", "×1", "「全AI生成的…人物那张脸有种说不出的塑料感，表情僵得跟蜡像似的，配音也怪，像在听导航念台词…不过话说回来，这游戏才几块钱啊，当个便宜的小品恐怖游戏玩玩也还行」（6.5h 09-18）——AI 缺陷的「低价豁免」机制再确认（AI 影游=低价+题材容错公式的负面侧承接）")
blocks += li("🆕 无障碍信号（全库首条）", "×1", "「我键盘d键坏了。按不到qte，屏幕键盘无法在游戏内使用，哈哈哈哈哈」（2.0h 09-22 好评）——QTE 键位不可自定义 + 软键盘不兼容：硬件受限玩家的无障碍诉求首次显形（自嘲语气=非差评，但诉求真实）")
blocks += '</ul></div>'
actions = act("P0", "跳过功能的「状态污染」测试用例", "跳过改变结局判定 = 与东北往事「选择被静默改写」同级的交互正确性问题（09-18 P0 族）。对自家：快进/跳过路径必须进回归清单——跳过后「好感度/证据/分支标记」状态应与正常播放完全一致；跳过只能省时间，不能改语义。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4920100/aecf4db2323a4eebc76013235e0091fd07a600a2/header_schinese.jpg?t=1788225078", "列车怪谈：虚像之境",
    stat_span("🟠 +4（正 3/负 1）86.1%（-0.7）：跳过污染结局判定 bug 入库", "amb") + " " + stat_span("API 86.1% / 商店 87.2%（-1.1 ✓）", "m"),
    "<span>司命工作室 · 2026-08-30 · AI 悬疑恐怖互动影游</span><span>30天差评 10</span><span>评测池 72（中文，5d +4）</span>",
    86.1, blocks, actions))

# --- 金宵 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（引导刚性死因延续，五连跌）</h4><ul class="pb-list">'
blocks += li("完形填空 + 找词条卡关（引导刚性）", "×2", "「潦草开场，潦草收场，说是互动式推理解密，互动较弱，推理解密也弱，完形填空还整的呆头呆脑的，希望制作者可以玩玩其他的推理游戏之后再勉励自己吧」（2.7h 09-22 差评）/「案件推理很简单，难在找线索，难收集齐，特别是最后一章，想到了是[镜子]，但就是找了好久好久才找到那个词条。找不到词条就等着卡关吧。要是能自己输入就好了，这才是真正的盲探好吗」（4.4h 09-19 差评）——「知道答案但找不到词条」的交互刚性：难度不在推理而在检索")
blocks += li("在池批评框架延续", "在池", "线索重复收集/章节不互通/角色行为逻辑批评框架延续（neg30 池 20 条）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（在池）</h4><ul class="pb-list">'
blocks += li("玩法融合价值认可（在池）", "在池", "「监寓+类鲁特里+金偶像」玩法缝合被部分玩家认可（11.8h 好评「除了引导太差其他的我都还能接受」）——死因是引导而非玩法本身")
blocks += '</ul></div>'
actions = act("P1", "关键词收集的自由输入回退", "「要是能自己输入就好了，这才是真正的盲探」——当玩家已推理出答案时，检索词条不应是唯一输入路径。对自家（若做解谜向）：点选 + 打字双输入通道；点选失败 3 次后开放模糊匹配提示；「知道答案却卡关」是解谜产品最冤的差评来源。")
H.append(pcard("var(--r)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4143220/4925056509db1533da002335787556f640ac1a2e/capsule_616x353.jpg", "金宵公寓事件",
    stat_span("🔴 +2neg 55.6%（57.0→56.6→55.6 五连跌）：引导刚性死因不变", "r") + " " + stat_span("API 55.6% / 商店 57.8%（-2.2 ✓）", "m"),
    "<span>Buddy Studio · 2026-08-25 · 监控视角推理 FMV</span><span>30天差评 20</span><span>评测池 124（中文，5d +2neg）</span>",
    55.6, blocks, actions))

# --- 盛夏离与合 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（系列连续性问题显形）</h4><ul class="pb-list">'
blocks += li("🆕 系列作换配音/替身的角色连续性问题", "×1", "「为什么顾易的声音换了，换成一个大叔音…盛夏的顾易的一开口给我的感觉就是声音大，粗糙，大叔音，难听…还有盛夏顾易的替身男演员为什么换啊，换一个四十多岁的胖大叔…所以我想问导演还有编剧这是为什么啊」（8.0h 09-21 好评内嵌长段）——完蛋系列男主的配音/替身更换引发角色认同断裂：玩家逐部列举历任配音/替身演员，情绪强度等同于「角色被替换」")
blocks += li("在池批评框架延续", "在池", "进度 99% 卡死 + 存档回滚丢失（15.8h 全成就玩家 P0 在池）批评延续，5 日无新增")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 3 条新好评）</h4><ul class="pb-list">'
blocks += li("系列分岔设计的最高级认可", "×1", "「盛夏篇就是整个完蛋全系列命运的分水岭，所有平行宇宙，全部在这场毕业旅行完成分岔…它不只是一个番外续篇，是整个故事的分岔原点」（10.7h 09-20 元柒线长评）——「一个夏天的抉择决定往后十几年人生底色」：系列世界观的结构性设计被玩家完整解读并推崇")
blocks += li("番外价值 + 角色忠诚", "×2", "「元柒固然美好但是最后玩番外篇的意义就是为了季颜语啊！太短了还得是前传第5章神」（5.8h 09-21）/「30块钱买情绪价值，很值得」（在池）——番外太短（内容量诉求）+ 角色忠诚双信号")
blocks += '</ul></div>'
actions = act("P1", "系列作换角/换配音的显式公告与理由", "盛夏顾易换配音/替身被 8.0h 玩家逐部对比质问（「为什么啊」×4 连发）——系列 IP 的角色连续性是资产而非成本项。对自家：换配音/换演员必须官方公告理由（档期/合约/健康），并提供「新旧双轨」选项或至少怀旧彩蛋；沉默换角会被解读为「不尊重玩家记忆」。")
H.append(pcard("var(--g)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3987560/faeffae4a00fde7027c6a1124e88565156e7fdf0/header_schinese.jpg?t=1782476929", "盛夏离与合",
    stat_span("🟢 +3（全正）84.6% 持平：分岔原点设计获最高级认可；换配音角色连续性问题显形", "g") + " " + stat_span("API 84.6% / 商店 84.5%（+0.1 ✓）", "g"),
    "<span>intiny · 2026-06-24 · 完蛋 IP 新作 · 毕业季恋爱 FMV</span><span>30天差评 4</span><span>评测池 814（中文，5d +3）</span>",
    84.6, blocks, actions))

# --- 天平 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池）</h4><ul class="pb-list">'
blocks += li("在池批评框架延续", "在池", "「剧情性约等于零直接看A」/ 八位女主同质化流程 / 跳过键形同虚设批评框架延续，5 日无新增差评")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 新增观测（5 日 2 条新好评）</h4><ul class="pb-list">'
blocks += li("🆕 「为清晰度买单」理论（福利向付费逻辑的玩家自发命名）", "×1", "「以前想过这种影游为什么不直接看视频，现在想通了，视频的清晰度不够，不购买游戏的话永远达不到那个清晰度，为了更清晰看你喜欢的角色买游戏也是一种追求」（6.4h 09-22 全成就长评）——回答了福利向影游「为什么不直接看盗摄」的根本问题：画质与合法清晰度即付费理由（与花满楼 1080p 批评互为反面印证：画质债直接侵蚀付费理由）")
blocks += li("全成就玩家忠诚 + 演员导流", "×1", "「总结一句话就是阵容豪华，剧情一坨…但如果其中八个角色有你喜欢的角色的话是可以一玩的」（同上 6.4h）——「阵容豪华剧情一坨」的自洽消费逻辑（卡司=产品）")
blocks += '</ul></div>'
actions = act("P2", "画质是福利向产品的付费理由本身（「为清晰度买单」）", "天平玩家自发总结「不购买游戏就永远达不到那个清晰度」，而花满楼因 1080p/50G 被骂——画质在福利向品类中不是体验项而是付费正当性本身。对自家：此类产品的高码率/高分辨率是收入侧投资，不是成本项。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4699920/f66f671768b02c66edbdae30743c5af6cad208c/header_schinese.jpg?t=1785634781", "天平游戏1:抉择",
    stat_span("🟠 +1pos 85.5%：全成就玩家给出「为清晰度买单」理论", "amb") + " " + stat_span("API 85.5% / 商店 83.4%（+2.1 ✓）", "g"),
    "<span>MYSTERY CROWN · 2026-07-25 · 密闭囚笼福利向 FMV</span><span>30天差评 18</span><span>评测池 938（中文，5d +1）</span>",
    85.5, blocks, actions))

# --- 冰点之下 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（骰子机制批评新证）</h4><ul class="pb-list">'
blocks += li("骰子运气墙（连续判定关卡）", "×1", "「全是骰子运气游戏，最离谱的有将近连续10个骰子的关卡，真是离谱到家，叫什么冰点之下，直接叫『美女们喜欢臭屌丝的我——以骰子运气战斗游戏为例』」（4.2h 09-19 差评）+ 男频味/软色情擦边批评——骰子机制的难度曲线与题材承诺错位（「叫什么冰点之下」= 品类承诺审判）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 1 条新好评）</h4><ul class="pb-list">'
blocks += li("续作诉求", "×1", "「希望出第二部，没有过瘾」（7.8h 09-21）——机制被骂但内容被认可的分裂样本")
blocks += '</ul></div>'
actions = act("P2", "随机机制的「运气墙」检测", "连续 10 次骰子判定 = 玩家体验的方差失控。对自家（若引入随机机制）：① 连续随机判定的次数上限；② 失败 N 次后保底；③ 随机段必须可跳过——运气不应成为内容墙。")
H.append(pcard("var(--amb)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3711170/9f5c70a0241948bc9c96a4af88a441afdeeabeb9/capsule_616x353.jpg", "冰点之下",
    stat_span("🟠 +2（正 1/负 1）93.4%：骰子运气墙 + 男频味批评", "amb") + " " + stat_span("API 93.4% / 商店 92.0%（+1.4 ✓）", "g"),
    "<span>Joy Media · 2026-05-29 · 骰子机制末日 FMV</span><span>30天差评 3</span><span>评测池 2631（中文，5d +2）</span>",
    93.4, blocks, actions))

# --- DeepWeb ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池）</h4><ul class="pb-list">'
blocks += li("在池批评框架延续", "在池", "「community 没兴趣帮忙」的硬核门槛批评在池，5 日无新增差评")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（英文组，5 日 1 条新好评）</h4><ul class="pb-list">'
blocks += li("深度沉迷样本（长尾第三周）", "×1", "「Another amazing, mind-boggling dive into the Deep Web! Even while solving everything I could on the first playthrough, there still seems to be so many mysteries left to uncover…It was so immersive I almost didn&#39;t want to leave - I guess it&#39;s no surprise I got the void ending lol - and I think my brain has been a little rewired to boot!」（6.8h 09-20）——「大脑被重新接线」级沉浸证据；13→14 稳定长尾")
blocks += '</ul></div>'
actions = act("P2", "硬核解谜的长尾运营：谜题社区化", "「只有13条评测是绝对罪行」（在池）+ 本期 mind-boggling 级好评——硬核解谜的口碑浓度极高但扩散靠社区。对自家观察：此类产品的攻略/社区生态（Wiki/ Discord）是销量的第二引擎，值得在求扩散型好评中显式引导。")
H.append(pcard("var(--g)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3756870/572dcbf1c182bfa5d65bfe51bb2b359841f0d70e/header.jpg?t=1787077015", "Project DeepWeb",
    stat_span("🟢 +1pos 100%（13→14）长尾第三周：mind-boggling 级沉浸证据", "g") + " " + stat_span("API 100% / 商店 95.0%（+5.0 临界）", "amb"),
    "<span>NightCat Studios · 2026-08-17 · 桌面模拟+FMV 深网探索（英文）</span><span>30天差评 0</span><span>评测池 14（英文，5d +1）</span>",
    100.0, blocks, actions))

# --- The Complex ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池）</h4><ul class="pb-list">'
blocks += li("在池批评框架延续", "在池", "Linux 加载卡死 + 选项语义模糊（09-11 差评）延续；negΔ-1 微移除观测（见交叉模式）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（英文组，5 日 2 条新好评）</h4><ul class="pb-list">'
blocks += li("选择权重认可（choices matter 正面命名）", "×1", "「Many different endings depending on your choices. A game in which your choices truly change the outcome.」（4.5h 09-21）——英文市场「choices matter」是 FMV 评价的第一锚点（对照中文市场「选择无意义」批评）")
blocks += li("沙盒式恶玩法被当卖点", "×1", "「As someone who enjoys leading characters to their deaths in these kinds of games I managed to execute the entire cast on my first playthrough which was I quite pleased with. Limits the replayability though」（3.7h 09-20）——「处决全体角色」的恶玩法自由度被玩成乐趣：分支自由度本身即内容（BE 不是失败态而是内容态）")
blocks += '</ul></div>'
actions = act("P2", "BE 即内容：恶玩法自由度的设计许可", "「第一次通关就处决了全体演员并且相当满意」——英文玩家把 BE 当作主动探索的内容而非失败。对自家：BE 的仪式感（专属结局画面/成就/文案）决定多周目动力；「失败」叙事应奖励而非惩罚重玩。")
H.append(pcard("var(--g)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1107790/header_schinese.jpg?t=1780398865", "The Complex",
    stat_span("🟢 +1（正 2/负 -1）77.8%：choices matter 正面锚点 + 恶玩法自由度样本", "g") + " " + stat_span("API 77.8% / 商店 78.0%（-0.2 ✓）", "m"),
    "<span>Wales Interactive · 2020-03-31 · 科幻惊悚 FMV（英文）</span><span>30天差评 3</span><span>评测池 1065（英文，5d +1）</span>",
    77.8, blocks, actions))

# --- 恶校游戏 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池）</h4><ul class="pb-list">'
blocks += li("在池批评框架延续", "在池", "孔鸢救赎争议/剧情逻辑/彩蛋位置批评框架延续，5 日无新增差评")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 新增观测（5 日 2 条新好评）</h4><ul class="pb-list">'
blocks += li("演员颜值向短好评层", "×2", "「纪晴天是真他妈美啊，想深深」（14.1h 09-18）/「孔鸢可爱捏」（4.2h 09-20）——情绪浓度短好评层健康运转（无新增实质批评=口碑平台期稳定）")
blocks += '</ul></div>'
actions = act("P2", "口碑平台期的维持成本观察", "93.1% 连续多日稳定，无新增差评无重大新好评——发行 6 周后的自然衰减期。观察点：孔鸢争议与彩蛋批评是否随折扣季重启扩散。")
H.append(pcard("var(--g)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3818020/f463d6f2fe1ab48704011f38680bdd02a8f2d6d5/header_schinese.jpg?t=1786676383", "恶校游戏",
    stat_span("🟢 +2（全正）93.1% 持平：口碑平台期稳定", "g") + " " + stat_span("API 93.1% / 商店 92.6%（+0.5 ✓）", "g"),
    "<span>CineGame Interactive · 2026-08-13 · 校园霸凌复仇 FMV</span><span>30天差评 18</span><span>评测池 768（中文，5d +2）</span>",
    93.1, blocks, actions))

# --- 不心动 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池）</h4><ul class="pb-list">'
blocks += li("在池批评框架延续", "在池", "剧情稀碎/班底审美疲劳批评框架延续，5 日无新增差评")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 新增观测（5 日 3 条新好评）</h4><ul class="pb-list">'
blocks += li("擦边定位的坦然接受 + 角色竞争叙事", "×3", "「继咸鱼殿下之后又一款擦得明明白白的作品，更何况还是元老级演员阵容，演技到位的同时加之剧情还有那么些新意」（15.6h 09-19）/「不是你们不够好，是黑皮太无敌」（8.2h 09-22——角色人气竞争的饭圈化表达）/「为演员打好评。剧情有点跳」（21.0h 09-22 好评内嵌批评）——「演员扛剧」逻辑稳定运转")
blocks += '</ul></div>'
actions = act("P2", "「演员扛剧」模式的口碑天花板", "差评骂剧情、好评夸演员——产品口碑与演员口碑已分层。对自家观察：此模式好评率上限约 95%（演员粉丝盘锁定），破圈需剧情侧投入；「黑皮太无敌」的饭圈化表达=演员个人 IP 的社区货币。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4855450/32b18b2fd0dc505d38dd91500dfc359b771c37d0/header_schinese.jpg?t=1786671930", "不心动才有鬼",
    stat_span("🟠 +3（全正）95.0% 持平：演员扛剧逻辑稳定运转", "amb") + " " + stat_span("API 95.0% / 商店 95.4%（-0.4 ✓）", "m"),
    "<span>SP Studio · 2026-08-13 · 恋爱喜剧 FMV</span><span>30天差评 19</span><span>评测池 1324（中文，5d +3）</span>",
    95.0, blocks, actions))

# --- 灭寇1939 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（5 日 1 条新差评）</h4><ul class="pb-list">'
blocks += li("支线角色戏份分配批评", "×1", "「这游戏最难崩地方是，我觉得跟丽贝卡在一起去美国结局是最爽的，可以轰炸小日子，但是丽贝卡一点感情戏都没有，拉完了」（7.8h 09-19 差评）——最强结局线（轰炸结局）挂接最弱感情铺垫：结局价值与情感投资的错配")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（5 日 1 条新好评）</h4><ul class="pb-list">'
blocks += li("多结局体量认可", "×1", "「确实很不错，剧情很丰富，多种结局」（20.6h 09-19）——多分支设计是 ED 系产品的稳定口碑底盘（与江山/代号三国同向）")
blocks += '</ul></div>'
actions = act("P2", "结局价值与情感投资的挂接检查", "「最爽的结局挂最弱的感情线」——玩家为结局投入的情感需要角色载体。对自家：高光结局（大场面/情绪释放点）应挂接情感浓度最高的角色线，否则「爽」无处安放。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4108460/1fccc7802715bb0a98e0e30328b1762abb71e16/header_schinese.jpg?t=1785990990", "灭寇1939：上川往事",
    stat_span("🟠 +3（正 2/负 1）83.1%：最强结局线挂最弱感情铺垫批评", "amb") + " " + stat_span("API 83.1% / 商店 83.3%（-0.2 ✓）", "m"),
    "<span>KARMAGAME · 2026-08-05 · 谍战互动叙事</span><span>30天差评 9</span><span>评测池 568（中文，5d +3）</span>",
    83.1, blocks, actions))

# --- 其余产品简报（无新增或低信号，合并卡片式列表说明） ---
H.append(f'''<div class="pcard" style="border-left:4px solid var(--b)">
  <div class="pcard-header">
    <div class="pinfo">
      <div class="ptitle">其余 24 款 · 5 日窗口观测简报 <span style="font-size:11px;font-weight:400;color:var(--b);background:var(--bl);padding:2px 8px;border-radius:4px">无新增或低信号 · 微移除观测 3 款</span></div>
      <div class="pmeta"><span>零增长 16 款 · 微量增长 5 款 · 微移除观测 3 款（花满楼 posΔ-2 / 代号三国 posΔ-1 / The Complex negΔ-1）· 对不起警察 posΔ 前哨归零（证伪为噪声）</span></div>
    </div>
  </div>
  <div class="pcard-body"><div class="pb-grid"><div class="pb-block"><h4><span class="hdot neg"></span> 在池要点</h4><ul class="pb-list">
<li>东北往事：选择层交互 bug（选「不给钱」被改走「给钱」线）差评在池第 6 日，官方无修复回应——「修复后再改好评」承诺悬置中 <span class="cnt">在池</span></li>
<li>阴三国：pck 文件启动崩溃差评在池（「卸载重装也不行」）<span class="cnt">在池</span></li>
<li>主角：8.1h 好评内嵌「程序bug比较严重，经常动不动卡住」——高好评率产品的好评内嵌批评层 <span class="cnt">在池</span></li>
<li>Five Dates（英文组）：中文差评「玩了3段约会卡死2次…只有画面不动」+ 需连续通关不可中途退出（09-13）<span class="cnt">×1</span></li>
<li>1000王子：中文口径 n=2 全差评（API 0% vs 商店 22.2%，偏差 -22.2 ⚠️ 数据不可信）；英文新差评点名无成就设计 <span class="cnt">⚠️</span></li>
</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 微信号</h4><ul class="pb-list">
<li>雪落情书时 +1pos：「民宿的文旅宣传片」（3.4h 09-20）——文旅结合定位被玩家半调侃半认可地命名 <span class="cnt">×1</span></li>
<li>代号三国 posΔ-1（好评微移除观测点，与花满楼并列）<span class="cnt">×1</span></li>
<li>Rescue the Hostages：英文池仍 0 条（周扫恢复采集，维持月扫降频）；中文 1 条好评在池 <span class="cnt">周扫</span></li>
<li>光与影之恋 107 条 100% 零差评维持；DeepWeb 13→14 起量长尾 <span class="cnt">维持</span></li>
</ul></div></div></div>
</div>''')

H.append('</div>')  # close section

# ═══ Patterns ═══
H.append('<div class="section">')
H.append('<div class="section-title">交叉模式 <span class="st-num">跨产品信号 · 2+ 款共现才成立 · 本期 7 条（🆕×1：更新回归测试缺失族）</span></div>')
H.append('<div class="pattern-grid">')
H.append(pat(1, "重播/跳过层工程债族（扩容至 7 款）", "列车怪谈「跳过看过片段导致故事线混乱、打不出想要的结局」（10.9h 本期新证）+ 幸存者跳过判定双维度缺陷 + 东北选择被改写 + 绍宋回档无跳过 + 江山回档导航债 + 恶校死局无重开 + The Complex 中文差评不能回档——跳过/快进/回档路径是 FMV 工程债的最高发区，且全部发生在「二周目价值」环节：多周目是复购核心，重播层 bug 直接摧毁它。", [("from", "7 款共现"), ("fix", "快进路径进回归清单")]))
H.append(pat(2, "🆕 更新回归测试缺失族（本期最强 P0 证据）", "幸存者 09-18 好感度更新事故（旧进度无法获取好感度→主线卡死→「删档重玩」→修复后 Mac 第七章接棒，9+ 条差评）+ 绍宋 BGM 混音（「背景音乐太tm大了…你们自己不测试吗」）+ 列车跳过 bug——上线后热修本身正在成为差评制造机。对自家的 SOP 启示：热修需全平台回归清单 + 主线刚需依赖项用例 + 「更新后 48h 差评突增」监控。", [("from", "3 款共现"), ("fix", "热修回归 SOP")]))
H.append(pat(3, "AI 用途分界线（双向证据再扩：画面层可，叙事节点不可）", "正向：幸存者「目前最好的AI影游」命名潮（4 条）+ 列车「这题材就得AI才能做气氛」在池；反向：女帝 AI 对话结局彩蛋被「严肃抵制」+ 绍宋 AI 配音出错被点名——分界线精化为双轴：<b>题材轴</b>（恐怖/末日=氛围刚需 vs 历史正剧=廉价替代）×<b>层次轴</b>（画面层可 AI vs 对话/配音/结局语义层不可 AI）。", [("from", "4 款"), ("fix", "AI opt-out + 披露")]))
H.append(pat(4, "配角引擎（第 7 日，跨 3 款）", "女帝府哥/礼忠/王皇后（27.4h「府哥的眼神给我看哭了」）+ 幸存者萝卜/释无禅/孔雀小队（「我最喜欢的角色是稀无禅」）+ 恶校纪晴天——非主角情感投注对象持续产出独立口碑，且在 AI 路线（幸存者）同样成立：配角魅力与制作路线解耦，是内容设计层的通用杠杆。", [("fix", "配角预算优先级清单")]))
H.append(pat(5, "画质/体量工程债族（= 福利向付费正当性）", "幸存者 720P/2K马赛克（「背景画质太糊…AI涂抹的痕迹很重」）+ 花满楼 1080p/50G 在池 + 盛夏 2K 插帧在池；反向印证：天平玩家自发总结「视频的清晰度不够，不购买游戏的话永远达不到那个清晰度，为了更清晰看你喜欢的角色买游戏也是一种追求」——画质在福利向产品中直接等于付费理由，画质债=收入流失。", [("from", "4 款"), ("fix", "高画质包先例")]))
H.append(pat(6, "CP 派系斗争族（公开化升级）", "女帝「54党真的吐了」vs 95线（派系攻击首次公开化）+ 媚娘高阳争议（「为什么剧情要把高阳写成这样」在池）+ 盛夏元柒 vs 季颜语（「最后玩番外篇的意义就是为了季颜语啊」）+ 天平八选一——多 CP 产品的派系情绪是复购动力与差评风险的同一来源，需要 DLC 路线图显式管理。", [("from", "4 款"), ("fix", "派系路线图")]))
H.append(pat(7, "跨作品角色一致性族（系列 IP 资产保护）", "盛夏顾易换配音/替身被逐部对比质问（「为什么顾易的声音换了…换一个四十多岁的胖大叔」8.0h）+ 媚娘高阳两篇形象割裂在池——系列作的角色（含配音/替身）是连续性资产，沉默换角=资产贬值。对自家：换角需公告理由 + 提供连续性过渡。", [("from", "2 款"), ("fix", "换角公告 SOP")]))
H.append('</div>')
H.append('</div>')

# ═══ Self-eval ═══
H.append(f'''<div class="self-eval">
  <h4>自评 · 第 28 期（补跑）</h4>
  <div class="se-grid">
    <div class="se-item"><div class="score g">36/36</div><div class="lbl">评测覆盖</div><div class="note">5 日窗口净增 135（正 105/负 30）；原文捕获 145 ≥ 净增，窗口对账零缺口；Rescue 周扫恢复（英文池仍 0，维持月扫）</div></div>
    <div class="se-item"><div class="score g">100%</div><div class="lbl">数据完整性（偏差标注率）</div><div class="note">36/36 全标注；⚠️ 不可信 1 款：1000王子 -22.2（n=2）；临界 5 款：Bloodholic +9.8 / 心之岛 +8.3 / 退婚后 -7.1 / Five Dates -5.3（中文口径）/ DeepWeb +5.0；基线 pool0921 快照回退（intel 自 09-18 停更，已标注）</div></div>
    <div class="se-item"><div class="score a">10</div><div class="lbl">可行动建议（P0+P1）</div><div class="note">P0×3（幸存者好感度回归 SOP / 绍宋音频混音 / 列车跳过状态污染）+ P1×7 ≥ 3 合格；另 P2×4</div></div>
    <div class="se-item"><div class="score g">7</div><div class="lbl">交叉模式</div><div class="note">🆕×1（更新回归测试缺失族）≥ 2 合格；重播层族扩容至 7 款为最大模式</div></div>
  </div>
  <div class="next-steps">
    <strong>明日盯守（下期 09-24，恢复正常 24h 窗口）</strong>
    ① 幸存者笔记好感度 bug 修复转化验证（二改好评已现 1 条）+ 好感率 89.8 能否回 90 + Mac 第七章资源损坏增样 · ② 花满楼 posΔ-2 / 代号三国 posΔ-1 / The Complex negΔ-1 三款微移除前哨复核（续负 → 审计预警窗口，波间期已 9 天）· ③ 绍宋 BGM/音量修复回应 · ④ 女帝 AI 对话批评增样 + 54/95 派系事态 · ⑤ 东北选择层 bug 第 7 日修复回应 · ⑥ 列车跳过 bug 修复 · ⑦ Rescue 英文池（月扫）· ⑧ ⚠️ 平台侧：本 automation 09-21 中断于采集环节（脚本已建、数据未落盘）、09-22 未触发——停跑两日原因需核对调度，若 09-24 再现中断需上报
  </div>
</div>''')

H.append('''
<footer>
  <div class="rn">玩家心声机器人 · 第 28 期（补跑）</div>
  <div>2026-09-23 · 数据源：Steam appreviews API（neg30 负面抽样 + 主语言全量 + d5all 翻页捕获）· 窗口 09-18 09:06 → 09-23 08:20 · 每条标签均附原文引用，无编造</div>
</footer>

</div>
</body>
</html>''')

html = "\n".join(H)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved {OUT} ({len(html)} bytes, {html.count(chr(10))+1} lines)")
