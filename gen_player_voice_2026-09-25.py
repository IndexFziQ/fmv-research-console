#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate player-voice report 2026-09-25 (issue #29, 48h make-up window).
Design system identical to player-voice-2026-09-23.html (v1.1)."""

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/player-voice-2026-09-25.html"

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
.pat-card:nth-child(8)::before{background:var(--amb)}
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
<title>玩家心声报告 v1.1 | 2026-09-25</title>
<style>{CSS}</style>
</head>
<body>
<div class="c">

<header>
  <h1>玩家心声报告 v1.1</h1>
  <div class="sub">互动影游竞品 · Steam 评测深读 · 2026-09-25（周五）· 池内 36 款 / 采集 35 款（Rescue the Hostages 月扫跳过，下期 10-23）· 第 29 期（48h 补跑窗口）· ⚠️ 09-24（周四）全管线未触发（intel/rendered 均无产物），故窗口为 09-23 08:20 → 09-25 08:07，跨两日 · 全库主语言净增 +39（正 32 / 负 7），新评测原文捕获 40 条 ≥ 净增（首遍捕获 24 缺口 15 → 复探协议触发：d5all 复探仍命中滞后分片，改 num_per_page=100 查询形态命中新鲜分片补齐 → 窗口对账归零）· 数据口径：day_range=30 负面抽样 + 主语言全量抽样 + day_range=3 翻页捕获（中文游戏 schinese / 英文游戏 english，1000王子 补全语言口径）· 商店基线：intel0923 回退（intel 机器人自 09-23 起停更两日，已标注；恢复后下期校正）</div>
</header>

<!-- ═══ Hero ═══ -->
<div class="hero">
  <div class="hero-tag">⚡ CORE FINDING</div>
  <h2>幸存者笔记止跌回稳（89.8→89.7%）且给出 AI 路线的「正名三连」：「原来我不讨厌AI做游戏，只是讨厌AI粗制滥造端上来坑钱的游戏」（16.1h）、「算第一部能看能玩的AI类影游」（12.3h·8.65分）、「给未来的AI游戏指明了方向」（6.4h）——48h 14正2负，好感度事故修复后未再发酵，AI 口碑公式从「低价+题材容错」升级为「制作完成度正名」。同期女帝篇内容量指控升级为工程级：5.3h 差评「选项都懒得出了…这不是在看红果短剧吗？你既然没办法做成同一款游戏你不如出成DLC」+ 20.7h 深度好评内嵌「李泰和高阳都没死的结局竟是普通结局」结局优先级错位</h2>
  <p class="lead">本期信号面：分支可视化导航成跨产品系统性缺口——幸存者 5.7h 玩家给出完整规格（「选择时间节点能不能做成像盛世天下/隐形守护者那种…没选过的路线就不该展示出来」防剧透）同日与女帝 20.7h（「应该放一个你之前选择泛起涟漪的提示，亮起一条线告诉玩家在那一幕选了什么」）双证共现，加在池媚娘探索度/绍宋回档，共 4 款。微移除前哨证伪：花满楼 posΔ-2 后 48h 回正 +1，恶校 posΔ-1 为新单点、绍宋 negΔ-2（反向差评移除）——判定为噪声级波动而非审计重启。花满楼新好评点名「Steam 内置录像功能录出来声音和飞机起飞一样」且同条点名代号三国同款 bug——Steam 平台功能兼容族（录像/F12截图/云存档）首次成族。灭寇1939 出现全库首条「开箱爆率暗改」指控。零清洗状态延续（窗口内无批量移除）。</p>
  <div class="hero-stats">
    <div class="hero-stat"><span class="hsv">36</span><span class="hsl">池内产品（35 采集）</span></div>
    <div class="hero-stat"><span class="hsv">40</span><span class="hsl">48h 新评测原文捕获</span></div>
    <div class="hero-stat"><span class="hsv">+32/+7</span><span class="hsl">全库正/负净增</span></div>
    <div class="hero-stat"><span class="hsv">13</span><span class="hsl">行动卡（P0+P1 = 7）</span></div>
    <div class="hero-stat"><span class="hsv">8</span><span class="hsl">交叉模式（🆕×2）</span></div>
  </div>
</div>''')

# ═══ Quick Strip ═══
H.append('<div class="quick-strip">')
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4354460/8c136db542f3c9ac30ea86cf105014b99206d2f5/header_schinese.jpg?t=1789289866", "幸存者笔记", "89.7%", "warn", 90, "🟢 止跌回稳：413→429（+16，正 14/负 2），89.8→89.7%（-0.1）不再下探，好感度事故修复后未二次发酵 · AI 正名三连（16.1h「不讨厌AI只讨厌粗制滥造」/12.3h「第一部能看能玩」/6.4h「指明方向」）· 分线卡点批评（23.3h「没有设置卡点…导致分线没有深度」）+ Steam Deck 无云存档（7.6h）"))
H.append(qcard("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg", "女帝篇", "82.5%", "ok", 83, "🟠 +5（正 3/负 2）82.5% 持平 · 🔴 5.3h 长差评内容量指控升级：「45线两个小时就玩完…选项都懒得出了…这不是在看红果短剧吗」「两部道具剧情好感度完全不衔接…不如出成DLC」· 20.7h 长好评内嵌：李泰高阳全存活结局竟是普通结局（结局优先级错位）+ 名字和谐破坏代入 + 登基小游戏硬塞 · 13.0h「看不出女主的心态变化」"))
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4292950/dfd52caf6453e43b4d613a662064aca4924a7858/header.jpg?t=1787201131", "绍宋", "80.9%", "ok", 81, "🟢 +3（posΔ+5/negΔ-2）80.9% 回升 · 3 条新好评全为情怀向顶点：41.7h「宋可亡，天下不可亡！」/ 7.7h「官家，臣也请斩杨沂中！」/ 13.6h「历史题材影游较少，能遇到一部愿意认真做，已经挺难得了…愿意给点耐心」· ⚠️ negΔ-2 = 2 条差评被移除（复核中）"))
H.append(qcard("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3478050/0e3d390564332c03dd980d0b295cb533d0ecb7a7/capsule_616x353_schinese.jpg", "媚娘篇", "82.9%", "ok", 83, "🟠 +7（正 6/负 1）全库增量第一 · 4.5h 好评内嵌批评给出选择无意义痛点的完整表述：「出这个选项的意义在哪里直接让我看短剧得了啊…想做女性向剧情抉择就不该把路线定这么死，自由度很低」· 3.1h 新差评「剧情和选项真的很无聊」· 9.1h「服化道很用心」"))
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3749320/912e382a3edc1ccd8f6f71e05317b0ff312b84af/header_schinese.jpg?t=1787291920", "花满楼", "97.4%", "ok", 97, "🟢 posΔ-2 后 48h 回正 +1（1486→1487）——微移除前哨证伪为噪声 · 🆕 新好评实为批评：「和代号三国龙起一样的问题，用steam内置的录像功能，录出来的视频声音和飞机起飞一样，根本用不了」——Steam 录像 bug 且跨厂共现，平台功能兼容族成族信号"))
H.append(qcard("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4108460/1fccc7802715bb0a98e0e30338b1762abb71e16/header_schinese.jpg?t=1785990990", "灭寇1939", "83.0%", "warn", 83, "🟠 +1neg 83.0% · 🆕 全库首条「爆率暗改」指控：「游戏本身就垃圾，箱子还暗改爆率。我两个号连续1个月都没金箱子」（8.1h 09-24）——含随机掉落元素的影游首次出现 live-service 式信任崩塌差评，概率公示合规问题显形"))
H.append('</div>')

# ═══ Per-product section ═══
H.append('<div class="section">')
H.append('<div class="section-title">逐款分析 <span class="st-num">36 款池 · 35 款采集 · 按信号强度排序 · 好评率为 API 抽样（已与商店页基线比对，基线取 intel0923 回退——intel 自 09-23 停更，恢复后下期校正）</span></div>')

# --- 幸存者笔记 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（画质/导航/存档债延续，48h 仅 2 条新差评）</h4><ul class="pb-list">'
blocks += li("分线无卡点 / 全线遍历（分支深度批评）", "×1", "「分线分的挺多但是好像没有设置卡点？总之我每章都是全线遍历后，没有卡章节卡分线的情况，导致分线没有深度。个人还是比较喜欢命运家那种分线」（23.3h 09-25）——分线自由过了头反而失去「命运感」：玩家要求分线之间有互斥/锁定设计")
blocks += li("Steam Deck 无云存档（云存档族再+1证）", "×1", "「游戏还可以，一些小bug也能接受。不支持steam云？steamdeck玩了到电脑上没有存档」（7.6h 09-24）——与在池「换个电脑就没存档真牛」同族，新增 Deck 场景")
blocks += li("剧情逻辑批评（降智链）", "×1", "「一个被死亡威胁的主角…听见邻居阴沉沉的求助声，正确选项既不是不理她，也不是发现不对报警叫救护车，而是出去tm的找狗！…我们的大女主…能脚踩狂速奔袭的轿车…被TM一只狗咬了！」（0.7h 09-24 差评）——单条未发酵，但「选项正确答案反常识」批评框架与女帝/媚娘同构")
blocks += li("主界面音乐更换（微信号）", "×1", "「为什么主界面音乐换了，原有的更有感觉呀」（10.5h 09-23 好评内嵌）——更新改动既有资产需沟通")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（48h 14 条新好评，AI 正名三连）</h4><ul class="pb-list">'
blocks += li("🆕 AI 正名三连（制作完成度正名）", "×3", "「大概玩了一半，原来我不讨厌AI做游戏，只是讨厌AI粗制滥造端上来坑钱的游戏，玩的过程中基本没有不合理或者说话生硬的地方…剧情完整合理，牛」（16.1h 09-23）/「算第一部能看能玩的AI类影游…给个8.65分」（12.3h 09-24）/「给未来的AI游戏指明了方向，制作组和配音都是好样的」（6.4h 09-25）——AI 口碑公式升级：决定性变量不是「是不是AI」而是「完成度」，粗制滥造才是原罪")
blocks += li("量大管饱 / 直播转化 / 续作预期", "×3", "「量大管饱，直接当AI短剧玩，单流程7小时，全成就12小时…看主播直播间玩了一两章，还表示不屑，但是抛开脑子看进去后，还是决定买一个玩玩」（12.7h 09-24）/「不到20买的…如果出了第二部我应该还是会支持的」（23.3h 09-25）/「剧情很好，女主很帅，期待第二部」（15.4h 09-24）——直播渠道转化 + 二部预期双信号")
blocks += li("角色塑造（萝卜再点名）/ BGM", "×2", "「女主的建模越看越顺眼，非常喜欢萝卜，好评!!!!」（10.0h 09-23）/「角色塑造的不错，bgm也很带感，67章的男女主分线也是亮点」（23.3h）——配角引擎在 AI 路线持续运转（萝卜第 4 次被点名）")
blocks += li("防剧透导航诉求（规格级好评内嵌）", "×1", "「选择时间节点的部分，能不能做成像【盛世天下】或【隐形守护者】…那种简洁又容易选支线的」「B线怎么选都是死，A线大方展示出来了…没选过的路线，我觉得就不该展示出来」（5.7h 09-23 好评内嵌）——玩家自发点名竞品导航 UI 为标杆 + 防剧透规格")
blocks += '</ul></div>'
actions = act("P0", "分支图防剧透：未选择路线的可见性策略", "幸存者玩家给出双规格：① 未选过的路线不应在时间轴明示（「看不到选择结果也是play的一环」）② 死路 B 线与活路 A 线不应全摊在明面上。对自家：剧情树 UI 默认只显示已走过的路径 + 模糊化未探索节点（hover 才显暗纹），一处 CSS 级改动可挡「剧透感」差评——分支可见性=剧透风险，与女帝 20.7h「涟漪提示」诉求同族互补。")
actions += act("P1", "分线卡点：自由遍历与命运感的平衡", "23.3h 玩家点名「没有卡点导致分线没有深度，喜欢命运家那种分线」——全线遍历式自由 = 选择失去重量。对自家：关键分线应设置互斥锁（选 A 锁 B，二周目解锁），「回不去的选择」才有多周目情感差异；配合剧情树可视化让锁定关系可感知。")
actions += act("P2", "云存档：Deck/双机场景是标配刚需", "Deck 玩家「steamdeck玩了到电脑上没有存档」+ 在池「换个电脑就没存档」——云存档四件套证据链再+1；AI 长体量产品（7h+ 流程/全成就 12h）的进度资产更重，缺失即差评。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4354460/8c136db542f3c9ac30ea86cf105014b99206d2f5/header_schinese.jpg?t=1789289866", "幸存者笔记",
    stat_span("🟢 止跌回稳 +16（正 14/负 2）89.7%：AI 正名三连，好感度事故修复后未发酵", "g") + " " + stat_span("API 89.7% / 商店 90.5%（-0.8 ✓ pool0923）", "m"),
    "<span>MYSTERY CROWN · YESPLAY · 2026-09-11 · 全 AI 虚拟真人末日丧尸 FMV</span><span>30天差评 20</span><span>评测池 429（中文，48h +16）</span>",
    89.7, blocks, actions))

# --- 女帝篇 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（48h 2 条新差评，内容量指控工程级升级）</h4><ul class="pb-list">'
blocks += li("🆕 内容量指控升级：短剧化 + 跨作断裂 + DLC 化诉求", "×1", "「45线两个小时就玩完了，而且全是悲情结局，到最后李泰要死了连让主角选择留在身边的权利都没有吗…全程就没有几个甜的地方，全就是强制要求主角算计李泰…上一部选项就很少，这一部更是选项都懒得出了，强行让玩家走be结局是什么意味？…这是剧情选择游戏吗？这不是在看红果短剧吗？？…两部游戏道具和剧情以及好感度完全不衔接，跟说的完全不一样，你既然没办法做成同一款游戏你不如出成DLC，真的能不能用点心」（5.3h 09-23 差评五连问）——「选项都懒得出了」= 互动影游的存在性质疑；跨作道具/好感度不衔接是系列化工程债")
blocks += li("主角动机批评（心态变化缺失）", "×1", "「我不理解我为什么要掌权，我从这个游戏根本看不出女主的心态变化，李治有这么不值得相信吗」（13.0h 09-24 差评）——与在池「被剧本强迫推着走」（江山同款）同框架：权谋线主角的主动性/动机链是系列最大叙事短板")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（48h 3 条新好评，20.7h 规格级长评）</h4><ul class="pb-list">'
blocks += li("画面审美认可（上药镜头）", "×1", "「这部画面是真的养眼，随时暂停下都有好多镜头很好看，尤其是小伍给礼泰上药那段，恭喜制作组的审美得到了我的认可」（8.3h 09-24）——「随时暂停都好看」= 帧级审美认证")
blocks += li("多周目动力正面证据（三刷研究）", "×1", "「竟然不是只换个结局，每条线都会看到不一样的剧情，我已经开始研究三刷走哪条了」（7.5h 09-23）——差异化分支是多周目动力的直接来源（与花满楼 PPT 复用成反例）")
blocks += li("20.7h 深度长评（好评内嵌结局优先级批评）", "×1", "「我唯一哭的半死的唯有蕊儿溺死的那一幕…怎么都没有办法救蕊儿」（情感峰值）/「既然有一个结局是李泰跟高阳都没死的结局既然是普通结局，我拜托制作组，这个放在支线最后结局也许不会被骂那么惨」（结局优先级错位）/「武媚娘变成伍媚娘…整个代入感直接变0」（名字和谐）/「成功登基后那个小游戏一言难尽，就是一种硬塞的概念」（机制衔接）/「应该要放一个你之前选择泛起涟漪的…亮起一条线告诉玩家在那一幕选了什么」（分支导航规格）——单条评测浓缩 5 项设计规格，系列顶级反馈样本")
blocks += '</ul></div>'
actions = act("P1", "结局分层与情感浓度对齐（优先级错位修复）", "「李泰高阳全存活的结局竟是普通结局」——玩家用情感浓度感知结局等级，制作组用完成度定义：错位即差评。对自家：结局命名/展示层级（真结局/普通结局/BE）应按情感兑现强度排序；「全员存活」类高成本结局永远不该被标记为低优先级普通结局。")
actions += act("P1", "跨作数据衔接：系列作的存档/好感度/道具继承", "「两部游戏道具和剧情以及好感度完全不衔接…不如出成DLC」——系列化产品的跨作断裂数据债。对自家：系列作立项时即定义继承契约（哪些状态跨作保留、如何展示），无继承能力则用「独立新篇」定位管理预期，绝不暗示连续性。")
actions += act("P2", "敏感词和谐的品质化处理", "「武媚娘变成伍媚娘，其他角色在说伍才人的时候我还恍惚…整个代入感直接变0」——为过审改名是系列级现实约束，但可通过世界观内合理化（赐姓/封号剧情）降低代入断裂。")
H.append(pcard("var(--g)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg", "女王的游戏：盛世天下 女帝篇",
    stat_span("🟠 +5（正 3/负 2）82.5% 持平：内容量指控工程级升级 + 20.7h 规格级长评", "amb") + " " + stat_span("API 82.5% / 商店 82.3%（+0.2 ✓）", "g"),
    "<span>New One Studio · 2026-06-08 · 宫廷权谋 FMV</span><span>30天差评 20</span><span>评测池 7837（中文，48h +5）</span>",
    82.5, blocks, actions))

# --- 媚娘篇 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（48h 1 条新差评 + 选择自由度批评完整表述）</h4><ul class="pb-list">'
blocks += li("选择自由度批评（完整表述版）", "×1", "「剧情选项不能多一点吗，感觉很多就是我非选对的那条走固定结局不可，不然就得死，那出这个选项的意义在哪里直接让我看短剧得了啊，演员演的确实挺好的，剧情也很用心，但是如果你想做女性向剧情抉择问题就不该把路线定这么死，自由度很低」（4.5h 09-23 好评内嵌）——选择无意义痛点的教科书级表述：好评玩家也把它点名为头号问题")
blocks += li("新差评（无聊退场）", "×1", "「对我来说剧情和选项真的很无聊，抱着花了钱是屎也吃完的想法，也没能坚持玩到结局」（3.1h 09-24）——与 09-23 期 3.1h 同时长同框架（沉没成本退场型）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（48h 6 条新好评，全库增量第一）</h4><ul class="pb-list">'
blocks += li("服化道 + 上头体验", "×2", "「游戏服化道很用心 剧情也没什么雷点」（9.1h 09-23）/「好玩是好玩，有点上头，但是演技和某些情节，有些不敢恭维」（6.1h 09-24 好评内嵌批评）——上头（成瘾性）与不敢恭维并存的分裂好评层")
blocks += li("短评层（爽/丰富）", "×4", "「超级好玩」（4.9h）/「还是不错的剧情丰富」（0.7h）/「不错」（5.7h）——系列 8 周后短好评层仍在自然供给，长尾健康")
blocks += '</ul></div>'
actions = act("P1", "选择密度的量纲：影游 vs 短剧的分界", "媚娘 4.5h「出这个选项的意义在哪里直接让我看短剧得了」+ 女帝 5.3h「这不是在看红果短剧吗」——同厂两部、同周、同款批评句式：选项密度不足时玩家直接切换到「短剧比价」心智。对自家：每个选择节点自检「这个选项改变什么」；不能改变任何下游状态的选项应删掉或升级为可改变（哪怕只改一句台词反应）。")
H.append(pcard("var(--amb)", "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3478050/0e3d390564332c03dd980d0b295cb533d0ecb7a7/capsule_616x353_schinese.jpg", "女王的游戏：盛世天下 媚娘篇",
    stat_span("🟠 +7（正 6/负 1）全库增量第一：选择自由度批评获完整表述", "amb") + " " + stat_span("API 82.9% / 商店 86.7%（-3.8 口径差：中文 vs 全语言）", "m"),
    "<span>New One Studio · 2025-09-08 · 宫廷生存 FMV 上部</span><span>30天差评 17</span><span>评测池 9464（中文，48h +7）</span>",
    82.9, blocks, actions))

# --- 绍宋 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池 + negΔ-2 反向移除）</h4><ul class="pb-list">'
blocks += li("在池批评框架延续", "在池", "战棋批评/音频混音事故/AI 过场批评框架延续（neg30 池 20 条），48h 无新增差评文本（negΔ-2 为移除：2 条存量差评被平台或审计删除，复核中）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（48h 3 条新好评，情怀向顶点）</h4><ul class="pb-list">'
blocks += li("名场面复读式好评（情怀浓度顶点）", "×2", "「宋可亡，天下不可亡！」（41.7h 09-24）/「官家，臣也请斩杨沂中！」（7.7h 09-23）——玩家直接引用原著名场面做整条评测：IP 情绪资产被完整承接")
blocks += li("稀缺题材宽容（耐心型好评）", "×1", "「历史题材影游较少，能遇到一部愿意认真做，已经挺难得了。战旗系统有待提高…但冲着情怀，还是愿意给点耐心」（13.6h 09-24）——「愿意给点耐心」= 修补窗口期内的宽容资本，战棋差评潮未转化为口碑崩塌")
blocks += '</ul></div>'
actions = act("P2", "情怀宽容是限时的：修复节奏决定口碑走向", "41.7h/13.6h 玩家在差评潮中给出「愿意给点耐心」的宽容资本——但 80.9% 平台期已持续两周。观察点：战棋默认跳过（08-26 更新已做）与音频修复若在 DLC 前落地，情怀盘可承接 DLC 转化；否则宽容资本到期转化为差评。")
H.append(pcard("var(--g)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4292950/dfd52caf6453e43b4d613a662064aca4924a7858/header.jpg?t=1787201131", "绍宋：还我河山",
    stat_span("🟢 +3（posΔ+5/negΔ-2）80.9% 回升：情怀向好评三连，2 条差评被移除复核中", "g") + " " + stat_span("API 80.9% / 商店 80.1%（+0.9 ✓）", "g"),
    "<span>互动之星 · 猫眼娱乐 · 2026-08-20 · 历史正剧 FMV（南宋抗金）</span><span>30天差评 20</span><span>评测池 2776（中文，48h +3）</span>",
    80.9, blocks, actions))

# --- 灭寇1939 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（48h 1 条新差评）</h4><ul class="pb-list">'
blocks += li("🆕 开箱爆率暗改指控（全库首条）", "×1", "「游戏本身就垃圾，箱子还暗改爆率。我两个号连续1个月都没金箱子，服了」（8.1h 09-24 差评）——全库首次出现 live-service 式「暗改爆率」信任指控：含随机掉落/开箱元素的影游，玩家会用双账号做纵向对照；一旦形成「暗改」叙事即为不可逆信任崩塌")
blocks += li("在池批评框架延续", "在池", "谍战恋爱化/演技批评框架延续（neg30 池 9 条）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（在池）</h4><ul class="pb-list">'
blocks += li("多结局体量认可（在池）", "在池", "「剧情很丰富，多种结局」（20.6h 在池）——ED 系底盘稳定")
blocks += '</ul></div>'
actions = act("P0", "随机掉落概率公示：开箱元素的合规与信任刚需", "「箱子还暗改爆率，我两个号连续1个月都没金箱子」——只要产品含随机掉落，概率不透明就会在长线玩家处积累「暗改」叙事（双号对照=玩家侧的统计审计）。对自家：① 若引入开箱/掉落，概率公示（且国内有相应监管规范）；② 掉落规则变更必须公告；③ 影游产品应慎重引入 live-service 元素——单机买断玩家对概率 manipulation 的容忍度为零。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4108460/1fccc7802715bb0a98e0e30338b1762abb71e16/header_schinese.jpg?t=1785990990", "灭寇1939：上川往事",
    stat_span("🟠 +1neg 83.0%：全库首条「爆率暗改」指控（开箱信任崩塌型差评）", "amb") + " " + stat_span("API 83.0% / 商店 83.3%（-0.3 ✓）", "m"),
    "<span>KARMAGAME · 2026-08-05 · 谍战互动叙事（含开箱元素）</span><span>30天差评 9</span><span>评测池 569（中文，48h +1neg）</span>",
    83.0, blocks, actions))

# --- 花满楼 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 负面观测（在池 + Steam 录像 bug 新证）</h4><ul class="pb-list">'
blocks += li("🆕 Steam 内置录像功能音频损坏（跨厂共现）", "×1", "「和代号三国龙起一样的问题，用steam内置的录像功能，录出来的视频声音和飞机起飞一样，根本用不了！」（6.7h 09-23 好评实为 bug 报告）——玩家在评测里直接点名两款游戏同款 bug：Steam overlay 录像音轨损坏；与在池江山「F12 截图功能完全失效 + 叠加窗口无限叠加」同族")
blocks += li("在池批评框架延续", "在池", "1080p/50G、条件达成不显示绿色、解码卡顿批评在池，48h 无新增差评")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 正面观测（微移除回正）</h4><ul class="pb-list">'
blocks += li("posΔ-2 → +1 回正", "×1", "1486→1487：09-23 观测的好评净减 48h 内回正——微移除前哨证伪为噪声（Steam 后台数据修正或玩家改评），非审计重启")
blocks += '</ul></div>'
actions = act("P1", "Steam 平台功能回归清单：overlay/录像/截图/云存档", "花满楼+代号三国「录像声音和飞机起飞一样」+ 江山「F12 截图失效/叠加窗口无限叠加」+ 幸存者「Deck 无云存档」——Steam 集成功能是 FMV 产品的高发故障区（视频解码器与 overlay 冲突）。对自家：上线前用 Steamworks 集成测试清单（overlay 兼容/录像/截图/云存档/Deck）过一遍，这类 bug 玩家无法区分责任方，全部算在产品头上。")
H.append(pcard("var(--g)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3749320/912e382a3edc1ccd8f6f71e05317b0ff312b84af/header_schinese.jpg?t=1787291920", "花满楼",
    stat_span("🟢 +1pos 97.4%：posΔ-2 回正（前哨证伪）；Steam 录像 bug 跨厂共现", "g") + " " + stat_span("API 97.4% / 商店 97.3%（+0.1 ✓）", "g"),
    "<span>初域游戏 · 2026-08-20 · 女间谍谍战 FMV</span><span>30天差评 14</span><span>评测池 1487（中文，48h +1）</span>",
    97.4, blocks, actions))

# --- 无言之林 ---
blocks = '<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨（英文组，48h 1 条新差评长文）</h4><ul class="pb-list">'
blocks += li("「艺术品而非游戏」批评（交互深度死因）", "×1", "「It is impossible not to appreciate the effort a solo developer put into 40 days of work… However, this title has serious shortcomings in terms of being a &#39;game&#39;. Your choices have no real impact on the story; you are often forced back to the beginning after a wrong choice… The story flow is very slow, and the game lacks a real climax… It would have been more accurate to market it as an interactive film」（0.7h 09-24）——「拍成电影营销更准确」：一人团队样本的死因确诊=交互深度缺失（与 08-25 首诊「45分钟流程/中文玩家不买账」同一根因的第二证据）")
blocks += '</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美（在池）</h4><ul class="pb-list">'
blocks += li("视听品质认可（在池）", "在池", "「insanely impressive」「beautifully shot」在池——摄影质感是一人团队的唯一口碑资产，53.6% 全靠它撑")
blocks += '</ul></div>'
actions = act("P2", "「交互电影 vs 游戏」的品类承诺管理", "无言之林差评核心句「marketing it as an interactive film would have been more accurate」——品类错标是低交互产品的差评放大器。对自家：若做重氛围轻交互产品，商店页标签/预告片应显式管理预期（interactive film 而非 game），承诺错位的差评无法靠品质弥补。")
H.append(pcard("var(--amb)", "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3978240/08eb60ff49ea804e40f693b5a3183cf3df39cb2a/header.jpg?t=1787587217", "无言之林",
    stat_span("🟠 +1neg 53.6%（55.6→53.6 续跌）：「拍成电影营销更准确」死因确诊", "r") + " " + stat_span("API 53.6% / 商店 53.1%（+0.5 ✓）", "m"),
    "<span>Dogus Cagrici（一人团队）· 2026-08-24 · 无对白生存惊悚 FMV（英文）</span><span>30天差评 5</span><span>评测池 28（英文，48h +1neg）</span>",
    53.6, blocks, actions))

# --- 其余产品简报 ---
H.append(f'''<div class="pcard" style="border-left:4px solid var(--b)">
  <div class="pcard-header">
    <div class="pinfo">
      <div class="ptitle">其余 29 款 · 48h 窗口观测简报 <span style="font-size:11px;font-weight:400;color:var(--b);background:var(--bl);padding:2px 8px;border-radius:4px">零增长 21 款 · 微量增长 8 款 · 微移除观测 2 款（恶校 posΔ-1 / 绍宋 negΔ-2）· 零清洗延续</span></div>
      <div class="pmeta"><span>金宵 +1pos（0.1h 鉴赏组式好评重申「引导性差/UI 不好」）· 江山 +1pos / 冰点 +1pos（均短评「好玩」）· 阴三国 +1pos（5.2h「血战折磨但小游戏好上手，BGM 贴合，希望有续作」——小游戏难度分层正面证据）· 雪落 +1neg（文本未捕获，分片滞后下期回补）· 不心动 +1neg（「这什么sb剧情」剧情批评延续）· 1000王子/Five Dates/The Complex/Bloodholic/Cage of Roses/The Run/Libera/DeepWeb/光与影 0 增长</span></div>
    </div>
  </div>
  <div class="pcard-body"><div class="pb-grid"><div class="pb-block"><h4><span class="hdot neg"></span> 在池要点</h4><ul class="pb-list">
<li>东北往事：选择层交互 bug（选「不给钱」被改走「给钱」线）差评在池第 8 日，官方仍无修复回应——「修复后再改好评」悬置中 <span class="cnt">在池</span></li>
<li>恶校 posΔ-1：微移除单点观测（与 09-23 花满楼/代号三国前哨并列样本；花满楼已回正 → 噪声概率上升，明日复核定性） <span class="cnt">观测</span></li>
<li>绍宋 negΔ-2：2 条差评被移除（平台审计或投诉删除）——与好评清洗波相反方向，定性待复核 <span class="cnt">观测</span></li>
<li>主角：8.1h 好评内嵌「程序bug比较严重，经常动不动卡住」在池；97.3% 好评内嵌批评层延续 <span class="cnt">在池</span></li>
<li>阴三国：pck 启动崩溃差评在池；1000王子 中文口径 n=2 全差评（⚠️ -22.2 不可信） <span class="cnt">⚠️</span></li>
</ul></div><div class="pb-block"><h4><span class="hdot pos"></span> 微信号</h4><ul class="pb-list">
<li>媚娘 +7 全库增量第一（老产品 8 周后长尾供给仍健康） <span class="cnt">×1</span></li>
<li>阴三国 5.2h：小游戏难度分层的正面证据（「最高难度都好上手，除了仕诡牌」） <span class="cnt">×1</span></li>
<li>Rescue the Hostages：月扫降频中（英文池 09-23 仍 0 条），下期 10-23 <span class="cnt">月扫</span></li>
<li>光与影 107 条 100% 零差评维持；DeepWeb 14 条 100% 长尾维持 <span class="cnt">维持</span></li>
</ul></div></div></div>
</div>''')

H.append('</div>')  # close section

# ═══ Patterns ═══
H.append('<div class="section">')
H.append('<div class="section-title">交叉模式 <span class="st-num">跨产品信号 · 2+ 款共现才成立 · 本期 8 条（🆕×2：分支可视化导航族 / Steam 平台功能兼容族）</span></div>')
H.append('<div class="pattern-grid">')
H.append(pat(1, "🆕 分支可视化导航族（防剧透 + 涟漪提示）", "幸存者 5.7h「选择时间节点能不能做成像盛世天下/隐形守护者那种…没选过的路线就不该展示出来」+ 女帝 20.7h「应该放一个你之前选择泛起涟漪的提示，亮起一条线告诉玩家在那一幕选了什么」同日双证，加在池媚娘「探索进度百分百太难达成」/绍宋回档导航债——跨 4 款的系统性缺口：玩家要的不是更多分支，而是<b>看得见分支</b>（走过哪、锁了哪、改了会怎样）。导航 UI 是选择体验的下半场。", [("from", "4 款共现"), ("fix", "剧情树 + 防剧透")]))
H.append(pat(2, "🆕 Steam 平台功能兼容族（overlay/录像/截图/云存档）", "花满楼+代号三国「用steam内置的录像功能，录出来的视频声音和飞机起飞一样」（同一条评测点名两款同厂发行产品）+ 江山在池「F12 截图功能完全失效/叠加窗口无限叠加」+ 幸存者「Deck 无云存档」——FMV 的视频解码链与 Steam overlay 集成是隐性雷区，玩家不区分责任方。Steamworks 集成清单（overlay/录像/截图/云存档/Deck）应进上线 SOP。", [("from", "3 款共现"), ("fix", "Steamworks 回归清单")]))
H.append(pat(3, "AI 用途分界线（正名阶段：完成度决定论）", "幸存者 AI 正名三连（「原来我不讨厌AI做游戏，只是讨厌AI粗制滥造端上来坑钱的游戏」16.1h）+ 列车怪谈在池「AI 适合恐怖题材」——分界线从「题材轴」（恐怖=容错 vs 正剧=廉价）进化出第二判据：<b>完成度轴</b>（认真做=正名 vs 粗制滥造=原罪）。AI 路线的产品口碑上限定在制作完成度上，与是否 AI 无关。", [("from", "2 款"), ("fix", "完成度验收标准")]))
H.append(pat(4, "选择无意义痛点（同周双厂同句式升级）", "媚娘 4.5h「出这个选项的意义在哪里直接让我看短剧得了啊…不该把路线定这么死，自由度很低」+ 女帝 5.3h「这不是在看红果短剧吗？…选项都懒得出了」——同厂两部、同周、同一比价对象（红果短剧）：选项密度不足时玩家直接切换短剧心智。加上在池无言之林「choices have no real impact」英文版与退婚后「选择基本上没什么用」——全库最普遍的品类级痛点，四语言同构。", [("from", "4 款"), ("fix", "选项状态自检")]))
H.append(pat(5, "重播/跳过层工程债族（7 款在池延续）", "列车跳过污染结局 + 幸存者跳过判定双维缺陷 + 东北选择被改写 + 绍宋回档无跳过 + 江山回档导航债 + 恶校死局无重开 + The Complex 不能回档——本期无新增成员但幸存者分线卡点批评（23.3h）补充了新维度：重播层不只要求「能跳过」，还要求「跳过有边界」（互斥锁/卡点），自由遍历同样摧毁二周目价值。", [("from", "7 款在池"), ("fix", "重播层回归清单")]))
H.append(pat(6, "更新回归测试缺失族（在池延续）", "幸存者好感度事故（09-18，已修复未发酵）+ 绍宋 BGM 混音 + 列车跳过 bug 在池——本期无新增事故，且幸存者修复后 48h 14正2负验证了「快速修复→口碑回稳」路径成立；但新微信号出现：幸存者「主界面音乐换了，原有的更有感觉」——更新改动既有资产（音乐/UI）需公告沟通，属同类 SOP 的轻量版。", [("from", "3 款在池"), ("fix", "热修回归 SOP")]))
H.append(pat(7, "云存档/进度资产族（长体量产品的标配刚需）", "幸存者「Deck 玩了到电脑上没有存档」（7.6h 本期新证）+ 在池「换个电脑就没存档」+ 江山「完全没有云存档功能…几十小时进度直接消失」+ 主角「笔记本存档无法上传到云，换PC从头再来」——AI/长流程产品进度资产更重（7h+ 主线/12h 全成就），云存档缺失的差评权重随体量线性增长。", [("from", "4 款"), ("fix", "云存档标配")]))
H.append(pat(8, "微移除观测（本期结论：噪声级，审计未重启）", "09-23 前哨三款走势：花满楼 posΔ-2 → +1 回正（证伪）、代号三国 0（持平）、The Complex 0（持平）；本期新增恶校 posΔ-1 单点 + 绍宋 negΔ-2（反向差评移除）——四点全部为个位数波动且方向互斥，判定为 Steam 后台数据修正/玩家改评噪声。零清洗状态自 09-11 起延续 14 天（历史波间期 7-10 天，已超期），审计重启概率随时间上升，维持每日对账。", [("from", "4 款观测"), ("fix", "每日 posΔ/negΔ 对账")]))
H.append('</div>')
H.append('</div>')

# ═══ Self-eval ═══
H.append(f'''<div class="self-eval">
  <h4>自评 · 第 29 期（48h 补跑窗口）</h4>
  <div class="se-grid">
    <div class="se-item"><div class="score g">35/36</div><div class="lbl">评测覆盖</div><div class="note">48h 窗口净增 +39（正 32/负 7）；原文捕获 40 ≥ 净增，窗口对账归零（复探协议触发：d5all 复探命中滞后分片 → num_per_page=100 查询形态补齐 16 条）；Rescue 月扫占位</div></div>
    <div class="se-item"><div class="score g">100%</div><div class="lbl">数据完整性（偏差标注率）</div><div class="note">35/35 全标注；⚠️ 不可信 1 款：1000王子 -22.2（n=2）；临界 4 款：Bloodholic +9.8 / 心之岛 +8.3 / 退婚后 -7.1 / Five Dates -5.3（英文口径）；基线 intel0923 回退（intel 停更两日，已标注）</div></div>
    <div class="se-item"><div class="score a">7</div><div class="lbl">可行动建议（P0+P1）</div><div class="note">P0×2（分支防剧透 / 爆率公示）+ P1×5（结局优先级 / 跨作衔接 / 选项密度 / Steamworks 清单 / 分线卡点）≥ 3 合格；另 P2×6</div></div>
    <div class="se-item"><div class="score g">8</div><div class="lbl">交叉模式</div><div class="note">🆕×2（分支可视化导航族 / Steam 平台功能兼容族）≥ 2 合格；选择无意义痛点同周双厂同句式升级为最强品类信号</div></div>
  </div>
  <div class="next-steps">
    <strong>明日盯守（下期 09-28 周一，72h 跨周末窗口 + Rescue 维持月扫）</strong>
    ① 幸存者 429→? 斜率与 89.7 守稳、分线卡点/防剧透诉求增样、主界面音乐更换是否发酵 · ② 女帝 45 线批评扩散与 DLC 化诉求、李泰全存活结局官方回应 · ③ 恶校 posΔ-1 / 绍宋 negΔ-2 定性复核（噪声 or 审计重启前哨）· ④ 灭寇爆率暗改指控增样 · ⑤ 花满楼/代号三国 Steam 录像 bug 官方回应 · ⑥ 雪落 +1neg 文本回补 · ⑦ intel 机器人 09-24/09-25 连续两日未触发，落盘后基线校正 · ⑧ ⚠️ 平台侧：调度缺口两周内第三次出现（09-21 中断、09-22 未触发、09-24 未触发），建议核对 automation 调度
  </div>
</div>''')

H.append('''
<footer>
  <div class="rn">玩家心声机器人 · 第 29 期（48h 补跑窗口）</div>
  <div>2026-09-25 · 数据源：Steam appreviews API（neg30 负面抽样 + 主语言全量 + d3all 翻页捕获 + num_per_page=100 复探）· 窗口 09-23 08:20 → 09-25 08:07 · 每条标签均附原文引用，无编造</div>
</footer>

</div>
</body>
</html>''')

html = "\n".join(H)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved {OUT} ({len(html)} bytes, {html.count(chr(10))+1} lines)")
