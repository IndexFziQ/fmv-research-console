#!/usr/bin/env python3
"""Build player-voice-2026-09-09.html from 2026-09-08 base + today's digest data.
Approach: per-app numeric/status patch (regex per pcard chunk keyed by appid) +
full rewrite of hero / quick-strip / pattern#2 / self-eval / footer + new-quote insertions."""
import re, json

BASE = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/player-voice-2026-09-08.html"
OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/player-voice-2026-09-09.html"
html = open(BASE, encoding="utf-8").read()

# ── per-app data: (status_badge, badge_color, api, store, dev_str, badge2_color, pool, delta, neg30, label_extra) ──
A = {
 "4148240": ("🟢 82.5% 持平（24h +4）：「选择权剥夺」未获新差评强化，「宝宝权谋」新叙事接棒", "g", 82.5, 82.3, "+0.2 ✓", "g", 7792, "+4", 19, "清洗后 09-07 新基线，24h 持平"),
 "3831120": ("🟢 91.3% 持平（24h +1）：有机增长三连降（+12→+9→+1），回归常态水位", "g", 91.3, 91.0, "+0.3 ✓", "g", 6242, "+1", 18, "稳定盘，连续多日持平"),
 "4920100": ("🔴 三日斜率向下 89.7→88.1→86.7 跌破 88 底线：U盘证据链 bug 差评「修复才改评价」", "r", 86.7, 87.7, "-1.0", "amb", 60, "+1", 7, "三日连降 89.7→88.1→86.7"),
 "4292950": ("🔴 81.3→81.2 缓降（24h +3）：「改编不如小说」+ AI 过场新差评续增", "r", 81.2, 80.4, "+0.8 ✓", "g", 2752, "+3", 20, "81.3→81.2 缓降"),
 "3749320": ("🟠 97.6% 守线（24h +4 全好评）：差评首次指控「刷好评」+ 1080p/50G 工程债并发", "amb", 97.6, 97.4, "+0.2 ✓", "g", 1491, "+4", 20, "企稳，24h +4 全好评"),
 "4143220": ("🟠 四日连升 56.0→59.5（24h +1）：类金偶像玩法获中评向好评", "amb", 59.5, 61.2, "-1.7", "amb", 116, "+1", 20, "四日连升 56.0→59.5"),
 "3478050": ("🟠 82.9%（24h +1），上部企稳：新好评「无敌」", "amb", 82.9, 86.7, "-3.8 临界", "amb", 9434, "+1", 20, "长期低于商店全语言口径 3-4pp"),
 "4234260": ("⚠️ 模板好评证据链完整存活第 3 日：08-11/08-12 十余条结构一致好评仍在池", "amb", 97.3, 97.3, "+0.0 ✓", "g", 974, "±0", 3, "持平"),
 "3818020": ("🟢 93.1%（24h +2）：新好评三连「神作」，750w 成本话题浮出", "g", 93.1, 92.6, "+0.5 ✓", "g", 755, "+2", 20, "93.1 持平微增"),
 "4855450": ("🟢 95.3%（24h +5 全好评，全库第一）：马老师/陈漫妆造是核心资产", "g", 95.3, 95.7, "-0.4 ✓", "g", 1305, "+5", 20, "95.3 持平"),
 "3412900": ("91.2%（24h ±0），清洗 -87 后企稳第 3 日", "g", 91.2, 90.1, "+1.1 ✓", "g", 2683, "±0", 11, "持平"),
 "3711170": ("93.5%（24h ±0），清洗 -128 后企稳；骰子机制两极", "g", 93.5, 92.1, "+1.4 ✓", "g", 2640, "±0", 3, "持平"),
 "3987560": ("84.8%（24h +2）：新好评口吻差评点名「配音更换/演员前后割裂」", "amb", 84.8, 84.6, "+0.2 ✓", "g", 809, "+2", 6, "持平"),
 "4104120": ("78.0%（24h ±0），港风题材长尾稳定", "a", 78.0, 78.4, "-0.4 ✓", "g", 758, "±0", 1, "持平"),
 "4699920": ("86.1%（24h ±0），「全明星卡司 + 零剧本」结构性差评定型", "amb", 86.1, 84.3, "+1.8 ✓", "g", 944, "±0", 20, "持平"),
 "4384120": ("96.9%（24h ±0），婚介题材稳定盘", "g", 96.9, 95.9, "+1.0 ✓", "g", 479, "±0", 15, "持平"),
 "4108460": ("83.5%（24h ±0），「披谍战皮的恋爱游戏」批评定型", "a", 83.5, 83.7, "-0.2 ✓", "g", 564, "±0", 20, "持平"),
 "4056810": ("83.4%（24h +1「演员颜值高」），IP 改编稳定盘", "g", 83.4, 84.2, "-0.8 ✓", "g", 169, "+1", 1, "83.3→83.4 微升"),
 "3828610": ("81.5%（24h ±0），韩厂 storytaco 供给波动期", "a", 81.5, 79.7, "+1.8 ✓", "g", 65, "±0", 12, "持平"),
 "3155310": ("93.8%（24h ±0），策略+怪谈混合题材小而美", "g", 93.8, 94.4, "-0.6 ✓", "g", 48, "±0", 3, "持平"),
 "4740420": ("96.5%（24h ±0），单女主纯爱+文旅融合稳定盘", "g", 96.5, 95.3, "+1.2 ✓", "g", 597, "±0", 1, "持平"),
 "4734650": ("🔴 87.1%（24h ±0）：骰子核心玩法+存档损坏双雷，差评侧 4/4 全提工程问题", "r", 87.1, 84.8, "+2.3", "g", 31, "±0", 4, "持平"),
 "3794770": ("68.3%（24h ±0），偏差 +9.3 临界（小样本 n=41）", "amb", 68.3, 59.0, "+9.3 临界⚠", "amb", 41, "±0", 2, "持平"),
 "3447920": ("88.9%（24h ±0）：英文口径三日滑落 91.1→88.9，n=45 小样本波动", "amb", 88.9, 88.2, "+0.7 ✓", "g", 45, "±0", 3, "91.1→88.9 回落"),
 "1353270": ("79.9%（24h ±0），偏差 -5.2（英文口径显著低于商店全语言）", "a", 79.9, 85.1, "-5.2", "amb", 884, "±0", 1, "持平"),
 "1107790": ("77.7%（24h ±0），英文稳定盘", "g", 77.7, 78.0, "-0.3 ✓", "g", 1060, "±0", 2, "持平"),
 "2993720": ("87.8%（24h ±0），中文侧翻译质量差评是独有死因", "a", 87.8, 88.5, "-0.7 ✓", "g", 172, "±0", 1, "持平"),
 "4412960": ("100.0%（24h ±0，n=103），零差评纪录保持", "g", 100.0, 100.0, "+0.0 ✓", "g", 103, "±0", 0, "零差评纪录"),
 "3978240": ("57.7%（24h ±0），「45分钟/7个选择」体量争议 vs 一人团队情怀", "amb", 57.7, 53.3, "+4.4", "amb", 26, "±0", 11, "持平，商店全语言 53.3 续降"),
 "3756870": ("100.0%（英文 n=10），桌面模拟+深网探索利基盘", "g", 100.0, 93.8, "+6.2", "amb", 10, "±0", 0, "n=10 满分"),
 "1188710": ("98.1%（24h ±0，n=54），免费短篇稳定盘；偏差 +9.9 临界（n 小）", "amb", 98.1, 88.2, "+9.9 临界⚠", "amb", 54, "±0", 1, "持平"),
 "4902060": ("66.7%（24h ±0，n=3），AI slop 低价恐怖样本", "a", 66.7, 66.7, "+0.0 ✓", "g", 3, "±0", 1, "n=3 未起量"),
 "2816920": ("🔴 26.8%（中文口径，24h ±0）：竖屏+章节内购双死因，反面标本", "r", 26.8, 33.9, "-7.1", "r", 41, "±0", 20, "长期低位"),
 "4846800": ("⚠️ 数据不可信：中文口径 n=1（0%），全语言 n=6（33%）；偏差 -33.3pp", "r", 0.0, 33.3, "-33.3 ⚠️", "r", 1, "±0", 1, "n=1"),
 "4619230": ("⏸️ 长尾未起量：发售第 6 天英文评测池仍 0 条——降频为每周一扫", "b", None, 100.0, "n/a", "b", 0, "±0", 0, "英文池 0 条"),
}
COLORS = {"g": ("var(--g)", "var(--gl)"), "amb": ("var(--amb)", "var(--alm)"), "r": ("var(--r)", "var(--rl)"), "a": ("var(--a)", "var(--al)"), "b": ("var(--b)", "var(--bl)")}

# ── split into head / pcard chunks / tail ──
m = re.search(r'(<div class="section">\s*<div class="section-title">逐款分析.*?</div>\s*)(<div class="pcard".*?)(</div>\s*\n\s*<div class="section">\s*<div class="section-title">跨产品交叉模式)', html, re.S)
head, cards_html, tail = html[:m.start(2)], m.group(2), html[m.end(2):]

chunks = cards_html.split('<div class="pcard"')
out_cards = []
for chunk in chunks:
    if not chunk.strip():
        continue
    am = re.search(r'apps/(\d+)/', chunk)
    appid = am.group(1) if am else None
    if appid in A:
        d = A[appid]
        status, c, api, store, dev, c2, pool, delta, neg30, label_extra = d
        fg, bg = COLORS[c]; fg2, bg2 = COLORS[c2]
        if appid == "4619230":
            badge2 = "API n/a / 商店 100.0%（n=1）"
        else:
            badge2 = f"API {api}% / 商店 {store}%（{dev}）"
        span = 'style="font-size:11px;font-weight:400;color:%s;background:%s;padding:2px 8px;border-radius:4px"'
        new_ptitle = re.sub(
            r'(<div class="ptitle">[^<]+ )<span style="font-size:11px;font-weight:400;color:var\(--\w+\);background:var\(--\w+\);padding:2px 8px;border-radius:4px">[^<]*</span> <span style="font-size:11px;font-weight:400;color:var\(--\w+\);background:var\(--\w+\);padding:2px 8px;border-radius:4px">[^<]*</span>',
            r'\1' + f'<span {span % (fg, bg)}>{status}</span> <span {span % (fg2, bg2)}>{badge2}</span>',
            chunk, count=1)
        chunk = new_ptitle
        chunk = re.sub(r'评测池 \d+（([^，]+)，24h [^）]*）', rf'评测池 {pool}（\1，24h {delta}）', chunk, count=1)
        chunk = re.sub(r'30天差评 \d+（满额）', f'30天差评 {neg30}（满额）' if neg30 >= 20 else f'30天差评 {neg30}', chunk, count=1)
        chunk = re.sub(r'30天差评 \d+', f'30天差评 {neg30}', chunk, count=1)
        if api is not None:
            chunk = re.sub(r'(<div class="pmeter"><div class="pos" style="width:)\d+(%"></div><div class="neg" style="width:)\d+(%"></div></div>)',
                          rf'\g<1>{round(api)}\g<2>{100 - round(api)}\g<3>', chunk, count=1)
            lang = '英文' if appid in ("2993720","3447920","1353270","1107790","4902060","3756870","3978240","4619230") else '中文'
            chunk = re.sub(r'<span>好评 [\d.]+%（API [^<]*）</span><span>差评 [\d.]+%[^<]*</span>',
                          f'<span>好评 {api}%（API {lang}口径，{label_extra}）</span><span>差评 {round(100 - api, 1)}%</span>', chunk, count=1)
    out_cards.append('<div class="pcard"' + chunk)
cards_html = ''.join(out_cards)
html = head + cards_html + tail

# ── global section rewrites ──
html = html.replace("<title>玩家心声报告 v1.1 | 2026-09-08</title>", "<title>玩家心声报告 v1.1 | 2026-09-09</title>")
html = re.sub(r'<div class="sub">[^<]*</div>',
  '<div class="sub">互动影游竞品 · Steam 评测深读 · 2026-09-09（周三）· 全量 35 款 · 第 20 期 · 24h 窗口（09-08→09-09）：全库中文评测池净增 25 条 · 新评测原文捕获 29 条（day_range=1 双通道修复昨日缺口）· 数据口径：day_range=30 负面抽样 + 主语言全量抽样（中文游戏 schinese / 英文游戏 english，1000王子 补全语言口径）+ day_range=1 新评测通道（窗口空时 API 回退全量，已按 CUTOFF 时间戳后过滤兜底）· 商店基线：当日 intel 09-09 全语言口径（昨日 _pool.json 回退缺档已回补校验）· ⏸️ Rescue the Hostages 发售第 6 天英文池仍 0 条，降频为每周一扫</div>', html, count=1)

# section title
html = html.replace('35 款 · 按信号强度排序 · 好评率为 API 抽样（已与商店页基线比对，基线取自 _pool.json 09-07 快照，当日 intel 未落盘）',
                    '35 款 · 按信号强度排序 · 好评率为 API 抽样（已与商店页基线比对，基线取自当日 intel 09-09 全语言口径，昨日缺档已回补）')

# hero
hero_new = '''<!-- ═══ Hero ═══ -->
<div class="hero">
  <div class="hero-tag">⚡ CORE FINDING</div>
  <h2>列车怪谈跌破 88 底线（89.7→88.1→86.7，三日 -3.0）：继探索度 bug 之后，U盘证据链 bug 再制造一条「修复才改评价」差评——AI 低价容忍带的工程债在加速兑付。花满楼 24h +4 全好评，但差评首次指控「刷好评」+ 1080p/50G 工程债并发，97%+ 读数开始缴「信任税」。女帝篇「选择权剥夺」叙事退潮，「宝宝权谋」新叙事接棒</h2>
  <p class="lead">24h 窗口全库中文评测池净增 25 条，新评测原文捕获 29 条（day_range=1 双通道上线，昨日「原文捕获 2 条」缺口已修复）。重点信号：①《列车怪谈》6.4h 差评明码标价「什么时候修复了这个恶心bug，什么时候改评价」——继 09-07 探索度 bug「好评转差评」后，工程债第二次直接制造差评，且好评率三日斜率 -3.0 说明 9.9 元低价锚点对 bug 类缺陷不豁免；②《花满楼》0.2h 差评「目测这游戏刷好评的居多，真正想买的朋友我建议还是点开详情多看看评论」——刷量指控首次进入其差评池，与主角模板好评证据链、绍宋水军指控构成「高好评率信任税」三角；③《女帝篇》24h +4，新差评「宝宝权谋/礼治恋爱脑」（15.0h）替代「选择权剥夺」成为差评侧新招牌，同日高扬黑化线获赞（6.1h「越看越上头」）；④《江山北望》有机增长三连降（+12→+9→+1）回归常态水位，口碑质量仍全库最高；⑤《恶校游戏》新好评三连「神作」+「成本竟高达750w」话题浮出；⑥《金宵》四日连升 56.0→59.5，工程修复杠杆持续验证；⑦《不心动才有鬼》24h +5 全好评领跑全库（16.4h「这才是影游应该要有的」）。</p>
  <div class="hero-stats">
    <div class="hero-stat"><span class="hsv">35</span><span class="hsl">分析产品</span></div>
    <div class="hero-stat"><span class="hsv">+25</span><span class="hsl">24h 全库净增</span></div>
    <div class="hero-stat"><span class="hsv">29</span><span class="hsl">新评测原文捕获</span></div>
    <div class="hero-stat"><span class="hsv">15</span><span class="hsl">P0+P1 建议</span></div>
    <div class="hero-stat"><span class="hsv">7</span><span class="hsl">交叉模式</span></div>
  </div>
</div>

'''
html = re.sub(r'<!-- ═══ Hero ═══ -->.*?(?=<!-- ═══ Quick Strip ═══ -->)', hero_new, html, flags=re.S)

# quick strip
qs_new = '''<!-- ═══ Quick Strip ═══ -->
<div class="quick-strip">
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4920100/aecf4db2323a4eebc76013235e0091fd07a600a2/header_schinese.jpg?t=1788225078" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">列车怪谈</span><span class="qrating warn">86.7%</span></div>
    <div class="qbar"><div class="pos" style="width:87%"></div><div class="neg" style="width:13%"></div></div>
    <div class="qtag">🔴 三日斜率 89.7→88.1→86.7 跌破 88 底线 · U盘证据链 bug 差评「修复才改评价」· 继探索度 bug 后工程债第二案 · 低价锚点对 bug 类缺陷不豁免</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3749320/912e382a3edc1ccd8f6f71e05317b0ff312b84af/header_schinese.jpg?t=1787291920" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">花满楼</span><span class="qrating ok">97.6%</span></div>
    <div class="qbar"><div class="pos" style="width:98%"></div><div class="neg" style="width:2%"></div></div>
    <div class="qtag">🟠 97.6% 守线（24h +4 全好评）· 差评首次指控「刷好评」+ 1080p/50G 工程债 · 25h 全成就长评「2026 年影游前五」· 抄袭风信楼指控仍是第一叙事</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">女王的游戏 女帝篇</span><span class="qrating warn">82.5%</span></div>
    <div class="qbar"><div class="pos" style="width:82%"></div><div class="neg" style="width:18%"></div></div>
    <div class="qtag">🟢 82.5% 持平（24h +4）·「选择权剥夺」未获新差评强化、「宝宝权谋」新叙事接棒 · 登录故障第 20 日 · 高扬黑化线获赞（6.1h「越看越上头」）</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3831120/6a5af0317c2156f49b790588f09484e1f63cbbed/capsule_616x353.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">江山北望</span><span class="qrating ok">91.3%</span></div>
    <div class="qbar"><div class="pos" style="width:91%"></div><div class="neg" style="width:9%"></div></div>
    <div class="qtag">🟢 91.3% 持平 · 有机增长三连降（+12→+9→+1）回归常态水位 · 09-08 新好评 13.7h「关卡设计得不错，沉浸感还可以」· 宣发失位待解（流量入口仍在绍宋评论区）</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3818020/f463d6f2fe1ab48704011f38680bdd02a8f2d6d5/header_schinese.jpg?t=1786676383" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">恶校游戏</span><span class="qrating ok">93.1%</span></div>
    <div class="qbar"><div class="pos" style="width:93%"></div><div class="neg" style="width:7%"></div></div>
    <div class="qtag">🟢 93.1%（24h +2）· 新好评三连「神作」「全收集」+「成本竟高达 750w」话题浮出 · 救孔鸢争议长尾未消 · 配音批评仍是差评第二核</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4143220/4925056509db1533da002335787556f640ac1a2e/capsule_616x353.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">金宵公寓事件</span><span class="qrating bad">59.5%</span></div>
    <div class="qbar"><div class="pos" style="width:60%"></div><div class="neg" style="width:40%"></div></div>
    <div class="qtag">🟠 四日连升 56.0→59.5（24h +1）· 4.5h 中评向好评认可「全网公敌调调」但点名信息冗杂 · 解密引导（97 关键词找到 96 个）仍是第一死因</div>
  </div>
</div>

'''
html = re.sub(r'<!-- ═══ Quick Strip ═══ -->.*?(?=<div class="section">)', qs_new, html, flags=re.S)

# ── per-app new-quote insertions & text fixes (unique anchors) ──
INS = [
 # 女帝篇: new complaint narrative
 ('<li>选择权剥夺（09-05 三连差评在池固化，第 4 日）',
  '<li>🆕 「宝宝权谋/恋爱脑」叙事接棒（09-08 新差评） <span class="cnt">×1</span><span class="q">"剧情弱智的不行 宝宝权谋来了 人礼治直接干成恋爱脑了 就登基一会…礼泰那边就亲个嘴啊。两条线都写的很乐色，纯圈钱吧你就"（15.0h 09-08）</span></li><li>选择权剥夺（09-05 三连差评在池第 5 日，无新增、开始被新叙事覆盖）'),
 # 女帝篇: new praises
 ('<li>深度情感长评（高时长好评持续沉淀）',
  '<li>🆕 高扬黑化线 + 妆造双重资产（09-08 新好评双证） <span class="cnt">×2</span><span class="q">"高扬从前面那个天真又爱玩的公主，一路走到后面真的变化好大，看得我一边心疼一边又觉得她这个疯劲好带感，越看越上头"（6.1h 09-08）/"新世界线怎么是这样，怎么还是bad ending啊，编剧你没有心！！！要不是演员妆造美的无与伦比，我真要给你打差评了"（3.2h 09-08，BE 吐槽仍投好评——妆造对冲剧本缺陷的又一实证）</span></li><li>深度情感长评（高时长好评持续沉淀）'),
 # 女帝登录故障天数
 ('登录/联网故障（持续第 19 日）', '登录/联网故障（持续第 20 日）'),
 ('<h4>登录故障第 19 日 + 进程假死细节', '<h4>登录故障第 20 日 + 进程假死细节'),
 ('<p>清洗（-426）+ 登录故障叠加的失真期未见缓解', '<p>清洗（-426）+ 登录故障叠加的失真期未见缓解（已进入第 20 日）'),
 # 花满楼: new complaint (刷量指控+工程债)
 ('<li>抄袭《风信楼》指控（差评侧第一叙事）',
  '<li>🆕 刷量指控首次进入差评池 + 1080p/50G/UI 工程债（09-08 新差评） <span class="cnt">×1</span><span class="q">"一打开游戏我就发现三个问题：1、只有1080p，2k、4k都不给一个还要占用50g的空间 2、这UI实在太诡异了，这操作提示还在看而后面就已经开始放播片了 3、…宣纸上的字还能有标点符号？…目测这游戏刷好评的居多，真正想买的朋友我建议还是点开详情多看看评论再做定夺吧"（0.2h 09-08）</span></li><li>抄袭《风信楼》指控（差评侧第一叙事）'),
 # 花满楼: new praise
 ('<li>玩法创新（碎片化叙事+经营养成首创）',
  '<li>🆕 深度长评定性「2026 影游前五」+ 25h 全成就（09-08 新好评） <span class="cnt">×2</span><span class="q">"挺耐玩的…2026年的影游中能排个前五。『梦有时』这几个女主的BE结局拍的比较好，推荐看一下。靠着攻略花了25小时总算全成就了"（25.0h 09-08）/"绝对八月最佳影游"（6.5h 09-08）</span></li><li>玩法创新（碎片化叙事+经营养成首创）'),
 # 列车怪谈: U盘 bug new complaint
 ('<li>AI 画面缺陷（差评侧第一死因）',
  '<li>🆕 U盘证据链 bug 卡死（09-08 新差评，「修复才改评价」明码标价） <span class="cnt">×1</span><span class="q">"如果选取第一个U盘证据没图像，第二个U盘不完整，再缺少陈铭的U盘，那么跟姜夺取U盘时，夺取成功就会bug卡死，非常影响体验，什么时候修复了这个恶心bug，什么时候改评价"（6.4h 09-08）</span></li><li>AI 画面缺陷（差评侧第一死因）'),
 # 列车怪谈 P0 action update
 ('<h4>探索度统计 bug 直接制造「好评转差评」——6.1h 玩家案例是本月最贵的 bug</h4><p>该玩家明确写「本来给的好评…更改为差评」',
  '<h4>工程 bug 连续制造「好评转差评 / 修复才改评价」：探索度之后是 U盘证据链</h4><p>09-07 探索度 bug 完成「好评转差评」（6.1h 改分），09-08 U盘证据链 bug 再造一条「什么时候修复了这个恶心bug，什么时候改评价」（6.4h）——工程债两天连造两条差评，好评率三日 -3.0（89.7→86.7）。原探索度案例'),
 # 绍宋: new complaints
 ('<li>AI 素材滥用（差评侧第一大死因，结构固化）',
  '<li>🆕 「改编不如小说」+ AI 过场差评续增（09-08 新差评×2） <span class="cnt">×2</span><span class="q">"有点粗糙，没小说动人，改编的太多了，还是得好好打磨剧本和游戏之间的关系"（11.7h 09-08）/"战旗部分依托，剧情部分也很无趣，里面过场动画有一部分ai，感觉很出戏啊"（1.0h 09-08）</span></li><li>AI 素材滥用（差评侧第一大死因，结构固化）'),
 # 绍宋: new praise (好评内工程债)
 ('<li>原著立意与「当赵构」的代入感（好评侧核心）',
  '<li>🆕 漫画过场音频缺陷（09-08 新好评内的工程债信号） <span class="cnt">×1</span><span class="q">"整体还不错，就是漫画过场部分声音太小，还没有字幕，很难知道在说什么，希望改进下"（4.8h 09-09 00:27 好评内）</span></li><li>原著立意与「当赵构」的代入感（好评侧核心）'),
 # 恶校: new praise
 ('<li>题材立意与社会议题',
  '<li>🆕 「神作」三连 + 750w 成本话题（09-08 新好评×3） <span class="cnt">×3</span><span class="q">"神作，我非常喜欢，真希望这部作品能有上千万销量…大量粗制滥造的影游充斥市场的环境下看到这样用心的作品，不舍得她就此结束"（4.8h 09-08）/"全收集了。制作相当精良。没想到这个游戏的成本竟然高达750w"（4.7h 09-08，成本话题首次由玩家口述浮出）/"能看出演员也都在努力的饰演好每个角色…整体还是比较推荐的"（7.2h 09-08）</span></li><li>题材立意与社会议题'),
 # 不心动: new praise
 ('<li>演员阵容（全明星卡司是核心资产）',
  '<li>🆕 24h +5 全好评领跑全库（09-08 新好评×5） <span class="cnt">×5</span><span class="q">"可以说美女系列的后作…非常看好这种类型的影游，这才是影游应该要有的，未来可期"（16.4h 09-08）/"马老师可爱捏，陈漫这部的的妆造也是顶级"（5.6h 09-08，好评内点名剧情低智但妆造对冲）/"福利满满，第一次玩，挺满意的"（6.1h 09-08）</span></li><li>演员阵容（全明星卡司是核心资产）'),
 # 金宵: new praise
 ('<li>玩法融合创新（类金偶像+真人影像）',
  '<li>🆕 类「全网公敌/别喂猴子」调调获认可（09-08 新好评，中评向） <span class="cnt">×1</span><span class="q">"玩法方面有几分全网公敌/别喂猴子的调调，是我感觉比较可以的地方，演员演技也算到位；但…视频浏览方面会有些冗杂与信息重复感…整体的案件逻辑有时也稍感欠缺"（4.5h 09-08 23:53，给好评但问题清单完整——第二次机会窗口的代表样本）</span></li><li>玩法融合创新（类金偶像+真人影像）'),
 # 江山北望: new praise
 ('<li>🆕 09-07 三连新好评全为深度长评（7.8h+）',
  '<li>🆕 09-08 新好评：关卡设计与沉浸感（13.7h 中长时玩家） <span class="cnt">×1</span><span class="q">"关卡设计得不错，我挺喜欢的。沉浸感还可以"（13.7h 09-08）</span></li><li>09-07 三连新好评全为深度长评（7.8h+）'),
 # 盛夏: new complaint (好评口吻差评)
 ('<li>体量/价格不匹配（差评第一叙事）',
  '<li>🆕 配音更换/演员前后割裂（09-09 凌晨新差评口吻好评） <span class="cnt">×1</span><span class="q">"真服了，整的这脑残剧情…顾易配音也换了，演员前后割裂，就留元柒颜值演技在线这一个优点，为了最后一个好结局，就这样吧"（3.5h 09-09 02:22，投了推荐票但差评实质——收官作演员阵容变动的情感成本首次被点名）</span></li><li>体量/价格不匹配（差评第一叙事）'),
 # pattern #5 login day count
 ('单机强制联网/账号体系：第 19 日的持续失血', '单机强制联网/账号体系：第 20 日的持续失血'),
 # pattern #6 add 女帝 BE
 ('The Run（"The ending is extremely abrupt" 2.3h 05-24）',
  'The Run（"The ending is extremely abrupt" 2.3h 05-24）、女帝篇（🆕"新世界线怎么是这样，怎么还是bad ending啊，编剧你没有心"3.2h 09-08 好评内吐槽）'),
]
for old, new in INS:
    assert old in html, f"anchor not found: {old[:60]}"
    html = html.replace(old, new, 1)

# ── pattern #2 replacement ──
i02 = html.find('<div class="pat-card"><div class="pat-num">02</div>')
i03 = html.find('<div class="pat-card"><div class="pat-num">03</div>')
assert i02 > 0 and i03 > i02
pat02_new = '''<div class="pat-card"><div class="pat-num">02</div><h4>「高好评率信任税」：刷量指控在三家产品共现</h4><p>🆕 同一 24h 窗口内：花满楼差评首次出现「目测这游戏刷好评的居多…点开详情多看看评论再做定夺」（0.2h 09-08）；主角的模板好评证据链（08-11/08-12 十余条结构一致好评）在 09-07 清洗波后完整存活第 3 日（清洗波本身已确认为一次性事件，受创 9 款全部转正）；绍宋差评池「还买水军刷好评我真笑了」等×4 持续在池。<b>97%+ 与「好评如潮」读数越高，玩家的自发反刷量审计越活跃，且指控一旦进入差评池会直接引导后续买家「看差评不看读数」</b>——高好评率从资产变成需要辩护的负债。</p><div class="pat-tags"><span class="tag from">花满楼·主角·绍宋</span><span class="tag fix">对自家：口碑可辩护性（真实长评占比/时长分布）要在运营期持续维护，而非发布期冲量</span></div></div>
'''
html = html[:i02] + pat02_new + html[i03:]

# patterns section title
html = html.replace('7 条 · 2+ 款游戏共现的问题/赞美', '7 条 · 2+ 款游戏共现的问题/赞美 · 🆕 本期新增：高好评率信任税（#02）')

# ── self-eval rewrite ──
self_eval_new = '''<div class="self-eval">
<h4>📊 自评 · 第 20 期</h4>
<div class="se-grid">
<div class="se-item"><div class="score g">29</div><div class="lbl">新评测原文捕获数</div><div class="note">全库净增 25 · day_range=1 双通道修复昨日缺口（2→29）· 35/35 款完成采集</div></div>
<div class="se-item"><div class="score g">100%</div><div class="lbl">数据完整性 · 偏差标注率</div><div class="note">34/34 有数据款全部标注偏差 · ⚠️≥15pp：1000王子（-33.3，n=1，数据不可信）· 临界：Bloodholic +9.9 / 心之岛 +9.3 / Five Dates -5.2 · 商店基线已回补为当日 intel 09-09 口径（昨日缺档闭环）</div></div>
<div class="se-item"><div class="score a">15</div><div class="lbl">可行动建议（P0×4 + P1×11）</div><div class="note">≥3 合格 ✓ · P0：列车怪谈 U盘 bug / 女帝登录第 20 日 / 主角模板好评 / 你好你配吗快进</div></div>
<div class="se-item"><div class="score g">7</div><div class="lbl">交叉模式数</div><div class="note">≥2 合格 ✓ · 🆕 新增：高好评率信任税（#02）· 结局 abrupt 模式新增女帝篇新世界线实证</div></div>
</div>
<div class="next-steps"><strong>⚠️ 已知数据缺口 & 明日盯守</strong>① day_range=1 通道在窗口为空时 API 回退返回全量列表——已按 CUTOFF（09-08 08:05）时间戳后过滤兜底，29/29 捕获均经窗口校验；② Rescue the Hostages 英文池连续 2 期为 0，已降频为每周一扫（下期默认跳过其全量采集，下周一恢复）；③ 明日盯守：列车怪谈 86.7 能否止跌 / 花满楼信任税是否扩散 / 女帝「宝宝权谋」叙事是否固化 / 江山北望 +1 是否为新常态 / 金宵 60% 关口 / 恶校 750w 成本话题二次传播。</div>
</div>

'''
html = re.sub(r'<div class="self-eval">.*?(?=<footer>)', self_eval_new, html, flags=re.S)

# footer
html = re.sub(r'<footer>.*?</footer>', '''<footer>
  <div>玩家心声报告 · 第 20 期 · 由玩家心声机器人每日 08:00 生成 · 数据源：Steam appreviews API（day_range=30 负面 + 主语言全量 + day_range=1 新评测通道）</div>
  <div class="rn">下一期：2026-09-10（周四）</div>
</footer>''', html, flags=re.S)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved {OUT} ({len(html)} bytes)")

# ── validate: HTMLParser tag balance ──
from html.parser import HTMLParser
VOID = {"meta", "img", "br", "hr", "input", "link"}
class V(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if not self.stack:
            self.errors.append(f"extra </{tag}> at {self.getpos()}")
            return
        t, pos = self.stack.pop()
        if t != tag:
            self.errors.append(f"mismatch <{t}> (opened {pos}) closed by </{tag}> at {self.getpos()}")
v = V()
v.feed(open(OUT, encoding="utf-8").read())
v.close()
if v.stack:
    for t, pos in v.stack:
        print(f"UNCLOSED <{t}> opened at {pos}")
if v.errors:
    print("ERRORS:", v.errors[:10])
if not v.stack and not v.errors:
    print("HTML validation OK: all tags balanced")
