#!/usr/bin/env python3
"""Render player-voice report 2026-09-14 (issue #23). Same design system as
player-voice-2026-08-11.html / 09-10. 35-app pool, 35 fetched (Rescue weekly Monday
scan restored). 72h window 09-11 -> 09-14 (weekend 09-12/09-13 not run).
Baseline: pool0911-fallback (today's intel 2026-09-14 not yet on disk at digest time).
NEW this issue: d3all channel (day_range=3, cursor-paginated) captured 76 full texts."""
from html.parser import HTMLParser

OUT = "/Users/alex/WorkBuddy/2026-08-11-09-56-47/library/rendered/player-voice-2026-09-14.html"

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
footer .rn{font-weight:600;color:var(--a)}
"""

def badge(text, kind):
    color = {"g": ("var(--g)", "var(--gl)"), "r": ("var(--r)", "var(--rl)"),
             "a": ("var(--a)", "var(--al)"), "amb": ("var(--amb)", "var(--alm)"),
             "b": ("var(--b)", "var(--bl)")}[kind]
    return (f'<span style="font-size:11px;font-weight:400;color:{color[0]};'
            f'background:{color[1]};padding:2px 8px;border-radius:4px">{text}</span>')

def card(d):
    pos = d["pos"]; neg = 100 - pos if pos is not None else 0
    meter = f'<div class="pmeter"><div class="pos" style="width:{int(pos)}%"></div><div class="neg" style="width:{int(neg)}%"></div></div>' if pos is not None else ""
    label = d.get("label", "")
    labels_html = f'<div class="pmeter-labels"><span>{label}</span><span>差评 {neg}%</span></div>' if label else ""
    comp = ""
    if d.get("comp"):
        comp_html = ""
        for li in d["comp"]:
            comp_html += f'<li>{li[0]} <span class="cnt">{li[1]}</span><span class="q">{li[2]}</span></li>'
        comp = f'<div class="pb-block"><h4><span class="hdot neg"></span> 高频抱怨</h4><ul class="pb-list">{comp_html}</ul></div>'
    pra = ""
    if d.get("pra"):
        pra_html = ""
        for li in d["pra"]:
            pra_html += f'<li>{li[0]} <span class="cnt">{li[1]}</span><span class="q">{li[2]}</span></li>'
        pra = f'<div class="pb-block"><h4><span class="hdot pos"></span> 高频赞美</h4><ul class="pb-list">{pra_html}</ul></div>'
    en = f'<div class="pb-en">{d["en"]}</div>' if d.get("en") else ""
    acts = ""
    for prio, title, text in d.get("acts", []):
        acts += (f'<div class="act-item"><span class="prio p{prio.lower()}">{prio}</span>'
                 f'<div class="act-text"><h4>{title}</h4><p>{text}</p></div></div>')
    badges = " ".join(d["badges"])
    border = d.get("border", "var(--a)")
    return f'''<div class="pcard" style="border-left:4px solid {border}">
  <div class="pcard-header">
    <img class="pcover" src="{d['cover']}" alt="{d['title']}" loading="lazy" onerror="this.style.display='none'">
    <div class="pinfo">
      <div class="ptitle">{d['title']} {badges}</div>
      <div class="pmeta">{d['meta']}</div>
      {meter}
      {labels_html}
    </div>
  </div>
  <div class="pcard-body"><div class="pb-grid">{comp}{pra}{en}</div></div>
  <div class="pcard-actions">{acts}</div>
</div>'''

APPS = [
# ───────────────────────────── 女帝篇 ─────────────────────────────
{
"title": "女王的游戏：盛世天下 女帝篇",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg",
"border": "var(--g)",
"badges": [badge("🟢 72h +16 全库领跑（14 好评 vs 2 新差评），82.5% 持平；配角塑造成为好评新引擎", "g"), badge("API 82.5% / 商店 82.3%（+0.2 ✓）", "g")],
"meta": "<span>New One Studio · 2026-06-08 · 宫廷权谋 FMV</span><span>30天差评 20（满额）</span><span>评测池 7800（中文，72h +16）</span>",
"pos": 82.5, "label": "好评 82.5%（API 中文口径，周末零清洗）",
"comp": [
("🆕 音频 bug：bgm 间歇消失", "×1", "「戴耳机的时候bgm时不时消失只剩下台词，只能切换成扬声器才能正常」（12.5h 09-11 新差评）——与在池音量失控/进程假死同属工程细节债"),
("🆕 剧情逻辑批评升级", "×1", "「很多正确选项跟错误选项本质上是一个意思，但就是会剧情杀…评价为8岁适龄儿童红果短剧水平」（4.3h 09-14 04:37 新差评）——「选择权剥夺」叙事的加强版表述"),
("选择权剥夺（在池第 10 日）", "×3", "「在新世界线该表露真心的时候游戏选项还在引导玩家选择玩弄李泰的选项…吃了苍蝇一样难受」（3.0h 09-05）/「很多选择不由因果逻辑驱动导致非常出戏」（16.8h 09-05）"),
("登录/联网故障（持续第 23 日）", "×2", "「B游戏老要联网就算了，还一直出错」（14.0h 08-31）/「一直显示登录超时，验证完整性和重新下载仍然无法登录」（6.5h 08-24）"),
],
"pra": [
("🆕 配角塑造成为口碑新叙事引擎", "×4", "「季怀衷这条线真的挺唏嘘的…真的有被背刺到，但再往后玩，才能理解他为什么会做出这种选择，非常可悲可敬的一个形象」（5.1h 09-12）/「长孙太尉虽然气人，但这个角色确实写得挺好…根据局势做取舍」（5.1h 09-11）/「看似衷心的臣子选择了背叛，看似会识时务的人却衷心到愿意赴死」（5.1h 09-13）——系列 5.1h 疑似同一玩家连发，但独立池内 27.8h/43.4h 高时长好评同步佐证"),
("高时长好评持续沉淀", "×3", "「我在连电视剧都看不进去的时期 这个游戏的剧情我一点都不舍得跳过」（27.8h 09-13）/「影游都能做成这种量就好了」（43.4h 09-12）/「影游天花板」（19.9h 09-14）"),
],
"acts": [
("P1", "配角动机自洽是权谋题材的口碑护城河——「反派为什么这样做」被写清楚比反转本身更值钱", "周末 14 条新好评中至少 4 条明确点名配角（季怀衷/长孙太尉/李益府）的动机自洽，而非主角颜值或 CP。对自家：权谋/群像题材的剧本预算应向配角动机链倾斜，这是可复用的口碑杠杆；「被背刺但可悲可敬」的复杂情感只有铺垫充分的配角才能触发。"),
("P1", "音频 bug + 剧情杀双新差评：长尾期工程债仍在以每周 1-2 条的速度兑换差评", "bgm 间歇消失（12.5h）与「红果短剧水平」逻辑批评（4.3h）叠加登录故障第 23 日，本期新增 2 差评全部指向可修/可改项。对自家：音频链路的隐性 bug（声道切换/间歇丢失）玩家感知极强且 100% 转化为差评，验收清单需含耳机/扬声器双声道长时间播放项。"),
],
},
# ───────────────────────────── 江山北望 ─────────────────────────────
{
"title": "江山北望",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3831120/6a5af0317c2156f49b790588f09484e1f63cbbed/capsule_616x353.jpg",
"border": "var(--g)",
"badges": [badge("🟢 72h +8 持续领跑质量盘（6251→6259），91.3% 持平；深度长评继续沉淀", "g"), badge("API 91.3% / 商店 91.0%（+0.3 ✓）", "g")],
"meta": "<span>木焱工作室 / 凤麟互娱 · 2025-11-19 · 架空历史权谋 FMV</span><span>30天差评 19</span><span>评测池 6259（中文，72h +8）</span>",
"pos": 91.3, "label": "好评 91.3%（API 中文口径，稳定盘）",
"comp": [
("权谋深度批评（两极差评核心，在池）", "×5", "「棋盘搭得很好，但游戏不太想让我下棋」（3.9h 08-28）/「大量影响进程的选择都是剧情杀根本没得选」（9.9h 08-31）/「剧情看似有很多选择，实则都是死路」（4.1h 09-10）"),
("回档导航债（在池）", "×1", "「前面选错了，到后面过不去了还得跑到老前面改选项，改完还不能跳」（2.3h 09-07）"),
("口碑反噬（在池）", "×1", "「谁说他剧情好场面大把我骗进来玩的」（6.7h 09-08）——高有机增长的期望清算叙事"),
],
"pra": [
("🆕 深度长评持续：微选择重拍被点名", "×1", "「为数不多剧情几乎不水不拖沓的影游佳作…即便是一个微小的选择改动，制作组也都重拍了一遍不同的剧情；制作、服化道也很精良」（12.2h 09-13）——「分支重拍度」首次被玩家明确命名为加分项"),
("🆕 高时长玩家梗二创（口碑资产）", "×1", "「男人一生只哭13次：晋王见死不救梦碎虞宫刑场😭…宣帝传位太子梦醒光武遗志😊」（9.4h 09-13 玩梗长评）——玩家自发整理「十三连坏结局」梗图式复盘，是沉浸深度与结局多样性的直接证据"),
("光武结局认可（多结局有效性）", "×2", "「好不容易才让哥哥和弟弟和平共处，哥哥当皇帝，光武这条线个人感觉最好」（11.3h 09-12）/「大场景穷了点，光武结局不错」（17.1h 09-12）"),
],
"acts": [
("P1", "「微选择重拍」被 12.2h 玩家点名为差异化资产——这是可直接引用的口碑话术", "玩家原话把「即便是微小的选择改动也都重拍了一遍」与「不水不拖沓」直接挂钩。对自家：分支重拍度是玩家可感知的诚意信号，宣发素材（对比向剪辑）与制作规格（哪些选择值得重拍）都应围绕它设计；同期绍宋的「AI 过场滥用」差评正是该资产的反面。"),
("P2", "信件道具穿帮被点名：低预算下的道具细节仍被玩家记账", "「就是信件上的字全是打印的还是太出戏了XD」（11.1h 09-12 好评内）——道具细节是玩家好评内也愿意点名的小扣分项，宣发/道具组核对清单的低成本项。"),
],
},
# ───────────────────────────── 金宵公寓事件 ─────────────────────────────
{
"title": "金宵公寓事件",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4143220/4925056509db1533da002335787556f640ac1a2e/capsule_616x353.jpg",
"border": "var(--r)",
"badges": [badge("🔴 续跌：58.5→57.0（72h -1.5），60 关口渐远；3 条新差评全部负面且两两同日", "r"), badge("API 57.0% / 商店 60.5%（-3.5）", "amb")],
"meta": "<span>Buddy Studio · 2026-08-25 · 监控视角推理 FMV</span><span>30天差评 20（满额）</span><span>评测池 121（中文，72h +3）</span>",
"pos": 57.0, "label": "好评 57.0%（API 中文口径，56.0→58.5→59.5→59.0→58.5→57.0）",
"comp": [
("🆕 男凝/DEI 批评从内容层升级到运营层", "×3", "「无时不刻的男凝视角才是最窒息的…女角色苦难叙事、男角色低素质反派，你算是两头都给得罪完了」（0.9h 09-13）/「网友询问是否出现辱男词作者积极回应，询问是否出现辱女词作者当作没看见…身为一个女性玩家感到生理不适」（4.0h 09-13）——制作人社媒回应的「不对称性」本身被写进差评"),
("🆕 解谜交互反人性（复制粘贴都不行）", "×2", "「在完形填空界面的关键词也是没法复制的…找到这个需要搜索的关键词出现的位置，复制后再黏贴到网页中搜索」（0.9h 09-13）/「解谜线索要走回头路…监控必须要复制人名，四个镜头重复素材完全是摆设」（3.2h 09-13）"),
("词条重复收集（在池）", "×2", "「97个关键词，第一遍打完我找到了96个」（5.3h）/「上一节用过的线索跟下一节不互通」（2.8h 08-26）"),
],
"pra": [
("玩法融合创新（在池）", "×1", "「有真人影片演出的类金偶像推理填词解谜游戏…侧重点完全是不一样的」（4.7h 09-01）"),
],
"acts": [
("P1", "读数续跌至 57.0：内容价值观批评不可逆，唯一可控杠杆只剩解谜交互层", "72h 内 3 条新差评同时命中男凝叙事与交互反人性两条线。价值观层（角色塑造/议题回应）短期不可逆；但「关键词不可复制、词条跨案不互通、监控素材重复」是明确的低成本修复项。对自家：文本类解谜的交互底线=可复制、可检索、词条一次收集全程可用。"),
("P1", "制作人「选择性回应」被玩家记账——危机公关的对称性本身成为差评素材", "4.0h 差评完整复述了「辱男词积极回应/辱女词装看不见」的社媒时间线。对自家：争议回应必须对称且公开留档，社群运营记录是口碑资产也可能是差评弹药；这是全库首个「运营回应方式」直接转化为差评的样本。"),
],
},
# ───────────────────────────── 绍宋 ─────────────────────────────
{
"title": "绍宋：还我河山",
"cover": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4292950/dfd52caf6453e43b4d613a662064aca4924a7858/header.jpg?t=1787201131",
"border": "var(--r)",
"badges": [badge("72h +5（2742→2747），81.0% 持平；好评长评与工程批评长评同日对冲", "a"), badge("API 81.0% / 商店 80.6%（+0.4 ✓）", "g")],
"meta": "<span>互动之星 / 猫眼娱乐 · 2026-08-20 · 历史 IP 改编 FMV</span><span>30天差评 20（满额）</span><span>评测池 2747（中文，72h +5）</span>",
"pos": 81.0, "label": "好评 81.0%（API 中文口径，平台期）",
"comp": [
("🆕 工程批评三连（长评点名）", "×1", "「游戏居然不支持2k分辨率，只能1080p小窗口玩。战旗无法窗口化全屏…会出现屏幕内容漂移。最厉害的就是网络，玩一半网络异常，重新登陆，登录账号都登不上」（9.4h 09-13 长评）——分辨率/战旗窗口化/单机联网三项工程债被一一点名"),
("AI 素材滥用（差评侧第一大死因，结构固化）", "×6", "「大多数场景以及内容使用ai画面，给我喂屎」（7.0h 09-13 新差评）/「前三章几十处AI视频直处，真当玩家是傻B看不出来？」（8.9h 在池）"),
("细节穿帮新增：镶钻美甲", "×1", "「你选的角儿，谁家好人宋朝有美甲，还是镶钻的？你家贤妃也穿越了？」（7.0h 09-13）——服化道考据差评的增量样本"),
("虚构角色杨沂真（在池第 25 日）", "×2", "「这个杨沂真存在的意义是？」（0.4h 09-13 新差评）——叙事零稀释"),
],
"pra": [
("🆕 深度长评：原著立意+演员选角双认可", "×1", "「总体来说并没有差到非常离谱…中规中矩有下一部我大概还会买的程度。家国情怀确实有表达出来…主要人物的选角太贴了，岳飞、李清照等等人物感觉完全没有违和感」（10.2h 09-13 长评，逐条列出优缺点的理性粉）"),
("原著立意与「当赵构」的代入感（在池）", "×1", "「你不是在选择剧情A还是B，你是在决定：这个天下到底要不要继续打」（25.1h 在池深度长评）"),
],
"acts": [
("P1", "9.4h 长评的工程批评三连是明确的可修清单：2K 支持、战旗窗口化漂移、单机联网弹窗", "差评叙事结构（AI/杨沂真/水军）未变，但本期新长评把工程债单独拎出且给出了具体复现路径。对自家：分辨率支持与窗口化是 Steam 玩家的「基础卫生」，单机联网弹窗在长尾期的差评成本已在此样本中复利兑现。"),
("P2", "「镶钻美甲」式穿帮说明历史 IP 的服化道审查颗粒度要到配饰层", "对自家：历史/年代题材的服化道验收清单需下探到美甲、纹身、现代发型等「近距离镜头可见」项；玩家会用放大镜逐帧核对，IP 粉丝尤其如此。"),
],
},
# ───────────────────────────── 列车怪谈 ─────────────────────────────
{
"title": "列车怪谈：虚像之境",
"cover": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4920100/aecf4db2323a4eebc76013235e0091fd07a600a2/header_schinese.jpg?t=1788225078",
"border": "var(--amb)",
"badges": [badge("🟠 微降：86.9→86.4（72h -0.5），5 条新评测 4 正 1 负；「AI 适合恐怖题材」成好评侧新共识", "amb"), badge("API 86.4% / 商店 90.3%（-3.9）", "amb")],
"meta": "<span>司命工作室 · 2026-08-30 · 全 AI 悬疑恐怖互动影游</span><span>30天差评 8</span><span>评测池 66（中文，72h +5）</span>",
"pos": 86.4, "label": "好评 86.4%（API 中文口径，86.7→86.9→86.4）",
"comp": [
("好评内批评：剧情连贯性", "×1", "「可以接受AI，但是能不能有点逻辑性，连贯性，东拉西扯的硬凑剧情…这在红果上免费的都不带看的，还过来花钱买，水军也是有够误导人的」（1.9h 09-12，推荐位但全文批评）——「红果短剧」对标已是 AI 影游差评的固定参照系"),
("探索度/QTE 工程债（在池第 14 日）", "×2", "「最后一章想100%流程很麻烦，感觉路线判定有时候会抽风，对全成就党不太友好」（6.8h 09-13 新评测）/「明明章节都探索完了，可显示的是已探索百分之九十几」（6.1h 09-01 在池）"),
("🆕 章节丢失 bug 疑似", "×1", "「怪谈玩着玩着没了 哪去了？」（0.8h 09-11 新差评）——低时长玩家的章节断流报告，需与探索度统计 bug 同查"),
],
"pra": [
("🆕 「AI 适合恐怖题材」成为好评共识", "×2", "「感觉AI就适合用来做恐怖游戏…对得起8.9的价格」（6.8h 09-13）/「很多恐怖的妆造和场景…这些都是真人妆造很难模拟的」（3.5h 09-01 在池）——AI 奇观优势与恐怖题材容错被明确挂钩"),
("低价锚点持续对冲", "×1", "「9块钱的游戏价格加上精致的建模给这个游戏加分很多，流程适中，剧情树也很明了」（14.5h 09-13）"),
],
"acts": [
("P0", "探索度统计 + QTE 判定 + 章节断流三 bug 未修复——86 底线保卫战进入第二周", "「路线判定抽风」「全成就党不友好」「玩着玩着没了」三条新证据均指向进度/判定层。修复成本极低（统计口径与判定窗口），但差评池已连续 14 日被同一叙事占据。对自家：探索度类成就的统计口径必须在上线前用 100% 全收集流程实测。"),
("P1", "「AI 适合恐怖题材」给出 AI 影游的选题答案：奇观型内容是 AI 的主场", "好评侧两次明确表示「真人妆造很难模拟」的恐怖场面是 AI 的优势区。对自家：AI 资产应集中在实拍做不到的奇观层（怪物/异变/超现实场景），而非替代表演；恐怖/惊悚题材同时提供题材容错（玩家对逻辑的要求低于本格推理）。"),
],
},
# ───────────────────────────── 盛夏离与合 ─────────────────────────────
{
"title": "盛夏离与合",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3987560/capsule_616x353_schinese.jpg",
"border": "var(--r)",
"badges": [badge("🔴 P0 进度卡死 + 存档丢失：15.8h 高时长粉丝向玩家新差评（09-13）", "r"), badge("API 84.7% / 商店 84.6%（+0.1 ✓）", "g")],
"meta": "<span>小有互动 · 2026-07-30 · 恋爱 FMV（完蛋系列收官作）</span><span>30天差评 5</span><span>评测池 808（中文，72h +2）</span>",
"pos": 84.7, "label": "好评 84.7%（API 中文口径，读数暂稳）",
"comp": [
("🆕 进度卡死 + 存档丢失（P0）", "×1", "「我游戏全结局都解锁了进度卡在了99%…结果是游戏出bug卡死了，点什么都没反应，我无奈的按了ALT+F4结果再进游戏存档都给我干没了变成之前的存档，之后我再进游戏点完季颜宇结局依然是会出BUG卡死界面」（15.8h 09-13 新差评）——全成就玩家+存档回滚双杀"),
("剧情注水/雷霆编剧批评（在池）", "×2", "「这一款就是全完蛋最烂的…你TM定37块」（6.5h 08-22 在池）"),
],
"pra": [
("系列情怀收官（在池）", "×2", "「我愿称为圆梦之作，感谢完蛋感谢小有弥补了我心中的遗憾。再见了顾易，再见了我的青春」（8.7h 09-07 在池）——收官作的情感资产仍在"),
],
"acts": [
("P0", "进度 99% 卡死 + 存档回滚：收官作的收尾 bug 会把整个系列终章印象定死", "受害者是 15.8h 全结局玩家（系列最核心粉丝层），且 bug 在重复触发（「点完季颜宇结局依然会出BUG卡死」）。对自家：结局解锁与进度统计的一致性、崩溃后的存档回滚保护，是「全成就玩家」这一最高价值人群的生死线；收官作上线前必须跑全结局自动化回归。"),
],
},
# ───────────────────────────── 花满楼 ─────────────────────────────
{
"title": "花满楼",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3749320/912e382a3edc1ccd8f6f71e05317b0ff312b84af/header_schinese.jpg?t=1787291920",
"border": "var(--amb)",
"badges": [badge("🟠 97.5% 守线，但 12.7h 玩家新差评报告进度判定 bug（P0）——差评池工程型占比继续 100%", "amb"), badge("API 97.5% / 商店 97.5%（+0.0 ✓）", "g")],
"meta": "<span>初域游戏 · 2026-08-20 · 女间谍谍战 FMV</span><span>30天差评 20（满额）</span><span>评测池 1487（中文，72h +1）</span>",
"pos": 97.5, "label": "好评 97.5%（API 中文口径，守线）",
"comp": [
("🆕 进度条件判定 bug（P0）", "×1", "「第三年卡润王过不去 条件也达成了 不显示绿色」（12.7h 09-13 新差评）——条件已满足但 UI 不变绿，玩家被卡死在进度门槛"),
("播片解码/存档/分辨率三重工程债（在池）", "×4", "「播片会动不动就给我卡住解码不成功」（2.9h 在池）/「存档、读档、时间线功能都用不了，50G还连2K分辨率都没有」（0.3h 在池）"),
("抄袭《风信楼》指控（差评侧第一叙事，在池）", "×4", "「剧本大体照搬游戏《风信楼》…希望花满楼能去找风信楼补授权吧」（1.2h 在池）"),
],
"pra": [
("玩法创新：碎片化叙事+经营养成（在池）", "×2", "「第一个通过时间章节+主线性叙事+碎片化叙事的玩法…在影游里算是第一个吃螃蟹的人」（9.4h 在池）"),
],
"acts": [
("P0", "「条件达成不显示绿色」是养成线产品的致命判定 bug——玩家无法区分「没达成」与「坏了」", "12.7h 高投入玩家在第三年（游戏后半程）被进度判定卡死，与在池「强行卡数值一直中途出坏结局」（7.8h）构成同一故障簇。对自家：任何条件判定（好感度门槛/任务完成/结局解锁）必须有可验证的中间态展示与日志，养成+多结局产品的进度判定是 P0 验收项。"),
],
},
# ───────────────────────────── 不心动才有鬼 ─────────────────────────────
{
"title": "不心动才有鬼",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4855450/header_schinese.jpg",
"border": "var(--amb)",
"badges": [badge("🟠 95.3→95.1（72h -0.2），+4 中 2 条为深度差评；「剧情稀碎」与「同质化疲劳」双叙事并进", "amb"), badge("API 95.1% / 商店 95.7%（-0.6）", "amb")],
"meta": "<span>山与海文化 · 2026-08-14 · 都市奇幻恋爱 FMV</span><span>30天差评 20（满额）</span><span>评测池 1318（中文，72h +4）</span>",
"pos": 95.1, "label": "好评 95.1%（API 中文口径，微降）",
"comp": [
("🆕 深度差评：剧本断裂被用 LLM 语境描述", "×1", "「除了第一章看起来在试图讲故事，后面几章充满着Token不足时AI梦到哪写到哪的前言不搭后语，人物的语言和行为在两个镜头之间毫无衔接逻辑可言」（9.1h 09-13 深度长评）——玩家已用大模型语言为「剧本不连贯」命名"),
("🆕 同质化疲劳（品类级预警信号）", "×1", "「可能对我个人而言现在影游同质化太严重了。请人气演员擦边惹火宅男们躁动的心，仅此而已…感觉以后可能会逐渐远离影游了，我腻了，我希望在影游乐趣中看到波涛，而不是在一堆波涛中硬找乐趣」（5.2h 09-13）——疲劳叙事从天平扩散到全明星阵容产品"),
("演员角色同质化批评", "×1", "「几个老师的角色也没有任何新鲜感可言，王新晨妆造很奇怪…陈老师老演这种角色，非常腻，马倩倩的角色跟表演也很拉」（2.5h 09-11 新差评）——同一班底的「角色复用疲劳」开始被点名"),
],
"pra": [
("演员信念感（在池）", "×1", "「虽然演员们大多颜值演技在线，且明显有着强大的信念感」（9.1h 09-13 差评内仍认可）"),
("玩法密度（在池）", "×1", "「游戏里还有很多互动和小游戏，参与感也会更强一点，而不是单纯的看电视」（2.1h 09-11 新评测）"),
],
"acts": [
("P1", "「Token 不足时 AI 梦到哪写到哪」——玩家的剧本连贯性检验已用 AI 时代语言标准化", "这是全库首个用 LLM 术语描述剧本断裂的差评，意味着玩家对「连贯性」的判据在升级：镜头间因果、人物动机连续性都成了显性验收项。对自家：剧本打磨应引入「镜头间逻辑审计」——每个转场问一句「角色为什么现在说这句话」。"),
("P1", "同质化疲劳从天平扩散至全明星产品——品类留存风险信号升级", "天平「越来越无聊 以后不玩了」（09-09）与不心动「我腻了…以后可能会逐渐远离影游了」（09-13）在 72h 内相继出现，且后者是 5.2h 中等时长玩家。对自家：题材/玩法差异化不再是加分项而是留存项；「演员班底复用」的边际递减已被玩家明确点名。"),
],
},
# ───────────────────────────── 恶校游戏 ─────────────────────────────
{
"title": "恶校游戏",
"cover": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3818020/f463d6f2fe1ab48704011f38680bdd02a8f2d6d5/header_schinese.jpg?t=1786676383",
"border": "var(--a)",
"badges": [badge("72h +5，93.0%；新评测含「影游最高分 8/10」长评，但也首现第一章死局退款差评（P0）", "a"), badge("API 93.0% / 商店 92.7%（+0.3 ✓）", "g")],
"meta": "<span>十三楼游戏 · 2026-08-14 · 校园反霸凌复仇 FMV</span><span>30天差评 20（满额）</span><span>评测池 759（中文，72h +5）</span>",
"pos": 93.0, "label": "好评 93.0%（API 中文口径，稳定）",
"comp": [
("🆕 第一章死局无法重开（P0）", "×1", "「第一章就玩出了个死局，然后就没办法继续下去，也没办法从头开始，这什么意思？才开始了20分钟，这就结束了？果断退款」（0.5h 09-12 新差评）——新手期死局+无重开入口=退款"),
("救孔鸢剧情批评（在池第一叙事）", "×4", "「非得救孔鸢…堪比美末二强行让玩家共情艾比环节」（5.4h 在池）"),
("剧本逻辑/配音批评（在池）", "×5", "「选项和剧情大部分都没啥逻辑，带脑玩感觉在侮辱我智商」（8.1h 09-01 在池）"),
],
"pra": [
("🆕 立意与制作获「影游最高分」长评", "×1", "「8/10分。挺惊喜，让我打出了目前玩过的影游最高分…开局十分钟尺度很大，讨论的校园暴力题材也比较大胆有意义。大部分影游都是福利向恋爱向，偶尔有这样一款换换脑子真挺好。游戏流程有点短，不到四个小时，也没什么重玩价值。制作组已官宣解散，有点可惜了」（3.7h 09-11）——题材差异化获满分级认可+团队解散惋惜并存"),
("演出细节", "×1", "「捅刀子的音效太特么牛逼了」（7.3h 09-13）——音效设计单点被玩家点名"),
],
"acts": [
("P0", "新手期死局是退款率杀手：死局本身可以设计，但「无法重开」不可以", "0.5h 玩家在第一章 20 分钟处遭遇死局且无任何恢复路径，直接退款。对自家：任何失败结局出现时，必须保证「章节重开」入口常驻（≤2 次点击可达）；死局惩罚应指向剧情分支而非流程阻断。"),
("P2", "制作组解散但口碑仍在沉淀（8/10 长评）——题材创新的商业回收滞后于口碑", "反霸凌题材在恋爱福利向红海中获差异化认可，但团队已官宣解散。对自家记档：创新题材的回报周期长于团队存续周期的风险，需要发行/资金节奏对冲。"),
],
},
# ───────────────────────────── 天平游戏1 ─────────────────────────────
{
"title": "天平游戏1:抉择",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4699920/header_schinese.jpg",
"border": "var(--amb)",
"badges": [badge("85.8→85.6（72h -0.2），+3 中 2 负 1 正；「花钱把妞看一遍」疲劳叙事继续", "amb"), badge("API 85.6% / 商店 84.3%（+1.3 ✓）", "g")],
"meta": "<span>背后系列团队 · 2026-08-16 · 全明星阵容恋爱 FMV</span><span>30天差评 19</span><span>评测池 937（中文，72h +3）</span>",
"pos": 85.6, "label": "好评 85.6%（API 中文口径，阴跌中）",
"comp": [
("同质化/罐头批评（在池第一叙事 + 新证据）", "×5", "「就花钱把妞看一遍，每个人几乎一样的流程，福利其实也没啥福利」（6.6h 09-11 新差评）/「影游界也有自己的罐头、不愧行业先驱」（7.3h 在池）"),
("单场景/无剧情（在池）", "×3", "「一般般，就在一个房间里拍的，也没啥选项」（6.8h 09-13 新评测，推荐位但全文贬义）——「推荐位差评文」现象持续"),
("跳过/读档体验（在池）", "×2", "「每个结局都需要我读档打…这个跳过键跟没有一样」（92.4h 在池）"),
],
"pra": [
("演员阵容买单（在池，仍在但边际递减）", "×2", "「参与演员：★★★★★ 很大很白：★★★★★ 剧情：史」（7.9h 在池）——阵容-剧本倒挂的自嘲式评分仍在传播"),
],
"acts": [
("P1", "「推荐位差评文」持续：推荐但通篇批评——读数与真实口碑的背离在拉大", "6.8h 新评测（点赞位）正文为「一般般…没啥选项」，与 09-12 1.9h 五日期「Wanted to like this」属同类。对自家：竞品读数分析必须读原文而非只看正负；自家产品要防「演员人情推荐位」稀释评测信息量。"),
("P2", "全明星阵容的买断红利进入消退期（85.6 阴跌第 4 周）", "疲劳叙事（「就花钱把妞看一遍」）已从差评池溢出到推荐位正文。对自家：阵容是首发杠杆不是长尾资产，长尾期只能靠剧情/分支重拍度支撑（对照江山北望 12.2h 长评）。"),
],
},
# ───────────────────────────── 阴三国谋论 ─────────────────────────────
{
"title": "阴三国谋论: 徐州篇",
"cover": "https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3155310/header_schinese.jpg",
"border": "var(--r)",
"badges": [badge("🔴 P0 启动崩溃：93.8→91.8（-2.0），0.4h 新差评报告重装无效的启动失败", "r"), badge("API 91.8% / 商店 94.4%（-2.6）", "amb")],
"meta": "<span>个人开发者 · 2025-08-12 · 三国怪谈策略互动</span><span>30天差评 3</span><span>评测池 49（中文，72h +1）</span>",
"pos": 91.8, "label": "好评 91.8%（API 中文口径，读数因启动 bug 下滑）",
"comp": [
("🆕 启动崩溃（P0，重装无效）", "×1", "「只进过一次游戏就进不去了，卸载了再装也不行，就一直显示这个：Error: Couldn't load project data at path '.'. Is the pck file missing?」（0.4h 09-11 新差评）——Godot 打包文件加载失败，用户侧无法恢复"),
("文本质量/题材错位批评（在池）", "×2", "「既不三国也不怪谈…很难让模拟经营产生任何的价值和意义」（0.7h 在池）"),
("无云存档（在池）", "×1", "「甚是无趣且没有云存档」（0.6h 在池）"),
],
"pra": [
("AI 参与度获认可（在池）", "×1", "「结合了AI配音、动画、立绘的AI占比很重的游戏，其玩法上真真不错，算是最为优质的AI参与的游戏之一了」（11.3h 在池）——AI 用途分界线正向样本（非表演层）"),
("权谋派系玩法（在池）", "×1", "「要在士族、豪族和丹阳兵之间走钢丝，推个政令还得防着背后捅刀子，代入感挺强」（6.3h 在池）"),
],
"acts": [
("P0", "Godot 打包启动失败（pck 缺失）：个人开发者的发布验证缺位样本", "用户重装无效说明是包体/路径层缺陷而非安装损坏。对自家：每次发版前需在「干净机器」上做冷启动冒烟测试；引擎打包产物（pck/资源路径）的完整性校验是个人开发者最容易漏的发布项。"),
],
},
# ───────────────────────────── Project DeepWeb ─────────────────────────────
{
"title": "Project DeepWeb: Eternal Nightmare",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3756870/header.jpg",
"border": "var(--g)",
"badges": [badge("🟢 100%（13/13），评测池 11→13 起量初现；6.8h+21.4h 新好评两连", "g"), badge("API 100.0% / 商店 93.8%（+6.2 临界，n 小读数不稳）", "amb")],
"meta": "<span>Sole developer · 2026-08-18 · 桌面模拟 ARG 恐怖解谜（EN）</span><span>30天差评 0</span><span>评测池 13（英文，72h +2）</span>",
"pos": 100.0, "label": "好评 100.0%（API 英文口径，n=13 读数方向健康）",
"comp": [
("上手门槛（在池）", "×2", "「steep learning curve if you aren't already a dev」（8.2h 在池）——高难解谜的固有代价，玩家已自行消化"),
],
"pra": [
("🆕 深度与细节再获长评", "×2", "「Amazing game, extremely detailed with so great storyline. The puzzles are more of an upper medium-high difficulty level…It's been ages since finishing a game made me want to replay it just to uncover all the puzzles I missed」（6.8h 09-13）/「If u liked the first one u will love this oneee」（21.4h 09-14）"),
("20h 级长评求扩散（在池）", "×1", "「it is an absolute crime that this game has only 13 reviews as of writing…i'm 17 hours in and i feel like i'm at the tip of the iceberg」（26.7h 09-10 在池）"),
],
"en": "<b>EN 口径</b>：评测池 11→13，新增 2 条好评均来自 6.8h+/21.4h 高时长玩家；上期 26.7h「求扩散」长评的传播效果开始显效（+2/72h）。利基高难解谜供给的口碑自传播样本，n 仍小但方向健康。",
"acts": [
("P2", "口碑自传播起量验证（+2/72h）：利基供给的「求扩散」路径有效", "对自家：高完成度利基产品的最小增长动作=识别并放大「求扩散」型核心玩家（长评作者）；评测池从 11→13 的增速对 n=13 基数是显著增量。"),
],
},
# ───────────────────────────── 代号三国:龙起 ─────────────────────────────
{
"title": "代号三国:龙起",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3412900/capsule_616x353_schinese.jpg",
"border": "var(--g)",
"badges": [badge("72h +1，91.2% 持平；新评测「福利+演技+深度」三合一点名", "g"), badge("API 91.2% / 商店 90.1%（+1.1 ✓）", "g")],
"meta": "<span>快斗娱乐 · 2025-08-08 · 三国架空恋爱 FMV</span><span>30天差评 11</span><span>评测池 2676（中文，72h +1）</span>",
"pos": 91.2, "label": "好评 91.2%（API 中文口径，粉丝盘稳定）",
"comp": [
("剧情杀/结局触发难（在池）", "×2", "「你一个影游搞这么难，我直接一个差评」（14.8h 在池）——难度曲线批评仍在池"),
("AI 过场滥用（在池）", "×2", "「你要么就别弄，弄你妈一堆ai过场有意思？!」（4.3h 在池）"),
],
"pra": [
("🆕 三合一好评", "×2", "「好玩 要福利有福利 要演技有演技 还有点深度 影游里的精品佳作」（12.5h 09-14）/「尤其是和瑶瑶互动绝美」（10.1h 09-13）"),
("演员群体买单（在池）", "×2", "「三幻神颜值在线，大乔是惊喜…2026最佳影游应该有代号的一席」（15.2h 在池）"),
],
"acts": [
("P2", "粉丝盘稳定运行：演员阵容+福利+架空剧情的组合在差评满额下仍守住 91%", "对自家：本作是「阵容-剧情倒挂」的反例——虽有剧情杀批评，但架空改编规避了历史考据差评（对照绍宋）；历史题材改编的考据风险可用架空设定对冲。"),
],
},
# ───────────────────────────── 灭寇1939 ─────────────────────────────
{
"title": "灭寇1939：上川往事",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4108460/header_schinese.jpg",
"border": "var(--amb)",
"badges": [badge("83.5→83.2（72h -0.3），+2 全为差评；「颠剧 vs 正剧」落差叙事继续固化", "amb"), badge("API 83.2% / 商店 83.8%（-0.6）", "amb")],
"meta": "<span>EpicDream Games · 2025-08-12 · 谍战抗日 FMV</span><span>30天差评 20（满额）</span><span>评测池 565（中文，72h +2）</span>",
"pos": 83.2, "label": "好评 83.2%（API 中文口径，缓慢阴跌）",
"comp": [
("🆕 题材错配新表述：颠剧 vs 正剧", "×1", "「本来预期是《隐形守护者》式的正剧风格，结果你来个《完蛋，我被美女包围了》式的颠剧。什么第一次就亲上了，和想杀你的人玩剪刀石头布…已经感觉常识在被暴击」（1.1h 09-12 新差评）——「正剧预期-恋爱内容」落差的最精准表述"),
("🆕 剪辑混乱批评", "×1", "「这游戏做的一坨，剪辑混乱，观感差，氛围诡异」（8.8h 09-14 新差评）"),
("谍战元素空转（在池第一叙事）", "×5", "「宣传的写实潜伏、情报博弈沦为空谈，前五章几乎无有效的谍战剧情」（32.1h 在池）"),
],
"pra": [
("演员/服化道（在池）", "×2", "「全体演员颜值与演技都在线，反派塑造尤为出彩」（32.1h 在池）"),
],
"acts": [
("P1", "「正剧预期-颠剧内容」的错配是谍战题材第一死因——宣发承诺管理再次被验证", "新差评把落差具象到桥段级（「和想杀你的人玩剪刀石头布」）。对自家：严肃题材的宣发素材必须与内容基调严格对齐；喜剧化桥段可以保留但要宣发明示，否则每次笑声都在消耗题材信任。"),
],
},
# ───────────────────────────── 女王的游戏 媚娘篇 ─────────────────────────────
{
"title": "女王的游戏：盛世天下 媚娘篇",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3478050/0e3d390564332c03dd980d0b295cb533d0ecb7a7/capsule_616x353_schinese.jpg",
"border": "var(--amb)",
"badges": [badge("82.9% 持平（72h +2），偏差 -3.8 临界延续；新差评把「选择无意义」推到逻辑终点", "amb"), badge("API 82.9% / 商店 86.7%（-3.8 临界）", "amb")],
"meta": "<span>New One Studio · 2025-09-08 · 宫廷权谋 FMV（上部）</span><span>30天差评 20（满额）</span><span>评测池 9440（中文，72h +2）</span>",
"pos": 82.9, "label": "好评 82.9%（API 中文口径，长期低于商店全语言口径 3-4pp）",
"comp": [
("🆕 「单线为什么做成选择性影游」——选择无意义的逻辑终点", "×1", "「全程剧情不合逻辑的地方数不胜数，大部分都是选错就死…而且分支剧情很少，所以你这剧情是单线的为什么要做成选择性影游呢？选择两个字体现在哪呢？挺怀疑编剧是否真的 有脑子 有文化 有逻辑？」（7.4h 09-12 新差评长文）"),
("选择无意义/高扬结局不可救（在池）", "×4", "「点了所有选项都帮不了高扬」（5.9h 在池）"),
("上下部分割销售定价反噬（在池）", "×3", "「49块钱买一个4小时的上部，还有一个原价70几的下部等着你」（10.5h 在池）"),
],
"pra": [
("辩机线情感爆点（在池长尾资产）", "×2", "「辩机行刑时的长视频真是爆哭，导演真是会拿捏人心」（23.1h 在池）"),
],
"acts": [
("P1", "「单线为什么要做成选择性影游？」——互动性是品类承诺，不是可选装饰", "新差评把全库第一痛点（选择无意义）推到终极质疑：如果选择不承载后果，品类本身就是错误包装。对自家：产品定义阶段就要回答「去掉选择后还成立吗」——若成立，说明互动设计是伪需求，会被最挑剔的玩家戳破。"),
],
},
# ───────────────────────────── 末日避难所 ─────────────────────────────
{
"title": "末日降临！被美女们关进避难所!?",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3828610/header_schinese.jpg",
"border": "var(--a)",
"badges": [badge("72h +1，81.8%（+0.3）；6.5h 长评「温吞水」剧本批评 vs 情绪价值认可并存", "a"), badge("API 81.8% / 商店 79.7%（+2.1）", "g")],
"meta": "<span>Storytaco · 2026-06-15 · 末日兽人恋爱 FMV（韩）</span><span>30天差评 12</span><span>评测池 66（中文，72h +1）</span>",
"pos": 81.8, "label": "好评 81.8%（API 中文口径）",
"comp": [
("🆕 长评系统性批评：温吞水剧情", "×1", "「温开水般的剧情…女主那句『回忆都在我的脑海里』，男主意外过来才几天就有回忆了，我整个人都尬住了。演技尬的淌口水，故事背景设定站不住脚」（6.5h 09-12 长评）——但对 UI/情绪价值/福利给出正向评价"),
("选角/审美批评（在池）", "×3", "「怎么选的角色越来越丑 有关系户？」（20.2h 在池）"),
("投票需梯子（在池）", "×1", "「投票也仍然需要梯子才可以」（4.9h 在池）——韩厂联网架构债"),
],
"pra": [
("🆕 情绪价值与 UI 认可", "×1", "「各场景布置还算合理，体现了与世隔绝的荒凉感…女主提供的情绪价值拉满，该有的身材镜头一点不少」（6.5h 09-12 同篇）——差评与认可在同一长评内分层共存"),
],
"acts": [
("P2", "「立意有深度但执行温吞」是韩厂模板的复现批评——福利可托底不可救口碑", "对自家：跨物种/末世等高概念设定若不在剧情中兑现（危险感/主线感），玩家会用「温吞水」一词统一退货；高概念必须配至少一场兑现设定的关键戏。"),
],
},
# ───────────────────────────── 主角 ─────────────────────────────
{
"title": "主角",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4234260/8304dfd2458ffffd8ce94ce8e76a12c95f4f6cf5/capsule_616x353.jpg",
"border": "var(--a)",
"badges": [badge("97.3% 持平（965→965，72h 零变动）；-3 后连续 4 日零移除——模板批次清算假设未获后续验证", "a"), badge("API 97.3% / 商店 97.3%（+0.0 ✓）", "g")],
"meta": "<span>顶顶阳光 / 一相逢互动 · 2026-07-15 · 校园反规训 FMV</span><span>30天差评 3</span><span>评测池 965（中文，72h ±0）</span>",
"pos": 97.3, "label": "好评 97.3%（API 中文口径，持平）",
"comp": [
("剧本逻辑硬伤（差评侧核心，在池）", "×2", "「开始讲的高大上，最后是幼儿园打架的水平做结局」（8.8h 08-24 在池）"),
],
"pra": [
("立意共鸣（在池）", "×1", "「反规训互动影游…关于校园霸凌和PUA，玩多了恋爱擦边爽游的可以来换换口味」（2.6h 08-31 在池长评）"),
("⚠️ 模板好评批次仍在池（08-11/12 十余条同句式）", "×10", "「回声计划的立意（有深度/很戳人/很有想法）+ 男主卧底校园大师班 + 节奏紧凑、主线清晰 + 选角和剧本都很（到位/出彩/靠谱）」句式批次本周零移除；09-10 的 -3 未见延续"),
],
"acts": [
("P1", "-3 后连续 4 日零移除：主角模板批次「清算确认」假设降级为「单次噪声」", "清洗观察修正：间歇性审计对主角批次的触达仅一次（-3）即止步，97.3% 读数继续按「部分含水」折扣处理。对自家：对竞品读数的清洗基线分段要记录「假设被证伪」的案例，避免把单次波动外推为趋势。"),
],
},
# ───────────────────────────── 冰点之下 ─────────────────────────────
{
"title": "冰点之下",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3711170/header_schinese.jpg",
"border": "var(--a)",
"badges": [badge("93.5% 持平（72h ±0）；7.6h 长评系统性批评骰子系统「打断气氛」", "a"), badge("API 93.5% / 商店 92.1%（+1.4 ✓）", "g")],
"meta": "<span>山与海文化 · 2026-08-14 · 寒潮末日悬疑 FMV</span><span>30天差评 3</span><span>评测池 2629（中文，72h ±0）</span>",
"pos": 93.5, "label": "好评 93.5%（API 中文口径，稳定）",
"comp": [
("🆕 骰子系统=换皮 QTE，打断叙事气氛", "×1", "「剧情走到关键地方，来一发骰子判定…刚酝酿起来的气氛，全被打断了，说白了就是换皮的qte…遇到脸黑的时候一个动作重复投好几遍，比qte还烦。qte至少我还能靠手速和反应打过去，你这骰子纯看运气」（7.6h 09-13 长评）"),
("骰子判定批评（在池）", "×1", "「游戏制作者是个赌徒吗，摇骰子摇的心烦」（5.0h 在池）"),
],
"pra": [
("女主塑造/题材（长评内认可）", "×1", "「几个女主颜值挺高，人设立的也还可以…这种题材确实少见」（7.6h 09-13 同篇）"),
],
"acts": [
("P2", "「随机性交互嵌入剧情」的节奏成本被量化：骰子判定在动作戏中连投=气氛杀手", "对自家：把随机判定放在「结果层」（结算/分支）而非「过程层」（打断演出）；动作戏中的失败重试上限（≤2 次）是节奏保护线；同一 QTE 段落内不重复判定。"),
],
},
# ───────────────────────────── 光与影之恋 ─────────────────────────────
{
"title": "光与影之恋",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4412960/header.jpg",
"border": "var(--g)",
"badges": [badge("🟢 100%（106/106）零差评延续，72h +1；鉴赏组长评为百合短篇背书", "g"), badge("API 100.0% / 商店 100.0%（+0.0 ✓）", "g")],
"meta": "<span>琉璃花糖 · 2026-08-18 · 百合短篇视觉小说</span><span>30天差评 0</span><span>评测池 106（中文，72h +1）</span>",
"pos": 100.0, "label": "好评 100.0%（API 中文口径）",
"comp": [],
"pra": [
("🆕 鉴赏组长评：小体量诚实定位", "×1", "「游戏选择在看似宏大的背景下讲述一个很小的故事，所谓以小见大，这样一个带着淡淡忧伤的百合情感故事更显珍贵。画风干净清新，角色表情差分做得相当细腻…有着全程配音」（1.9h 09-11 浮生评测组长评）"),
("每结局专属曲（在池差异化资产）", "×2", "「每个结局都有专属的片尾曲，加上角色歌…这么多首原创歌在视觉小说里也是少见的」（3.6h 在池）"),
],
"acts": [
("P2", "「预算内诚实」策略继续有效：明确品类承诺（百合短篇）+ 全程配音 + 专属曲", "对自家：小体量产品的口碑公式=承诺窄而兑现满；避免「宏大背景+小故事」错位（该作靠以小见大成立的前提是美术/音乐密度跟上）。"),
],
},
# ───────────────────────────── 请去Bar ─────────────────────────────
{
"title": "请去Bar，恋爱吧！",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4734650/header.jpg",
"border": "var(--amb)",
"badges": [badge("87.1% 持平（72h ±0）；骰子判定 bug + 存档损坏差评在池，未观测到修复证据", "amb"), badge("API 87.1% / 商店 84.8%（+2.3）", "g")],
"meta": "<span>画往时文化 · 2026-08-23 · 酒吧恋爱 FMV</span><span>30天差评 4</span><span>评测池 31（中文，72h ±0）</span>",
"pos": 87.1, "label": "好评 87.1%（API 中文口径）",
"comp": [
("骰子判定 bug + 存档损坏（在池，100% 工程型差评）", "×2", "「我的骰子是15242，对手骰子是64561，对方喊点3个6，我挑战后，系统判定失败，说实际上有4个6面」（0.4h 在池）/「存档也无法正常读取，要么点击读取没反应，要么读取的内容跟保存的不一致」（0.4h 在池）"),
("骰子玩法拖节奏（在池）", "×3", "「第一关赢5次，第二关直接变10次，规则还不提前说，输了重来、赢了还得继续摇」（3.5h 在池）"),
],
"pra": [
("酒吧氛围实拍（在池）", "×2", "「不知道制作组是不是真的找了一家酒吧实拍，反正灯光、布景、那种纸醉金迷的感觉很到位」（1.9h 在池）"),
],
"acts": [
("P1", "上期 P0（骰子判定 + 存档损坏）连续第二周未观测到修复证据——小池产品差评修复的时间成本被低估", "31 条评测池中差评 4 条全为工程型且修复证据缺失。对自家：小池产品的每条差评权重极高（1 条差评≈3pp），工程 bug 修复 SLA 应按「每差评≈3pp」定价。"),
],
},
# ───────────────────────────── 1000王子 ─────────────────────────────
{
"title": "1000王子: ChouChou Condo",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4846800/header_schinese.jpg",
"border": "var(--r)",
"badges": [badge("⚠️ n=2 中文 0%（0/2），偏差 -33.3pp 不可信；中文+英文新差评各 1（72h）", "r"), badge("API 0.0% / 商店 33.3%（-33.3 ⚠️≥15pp，n=2 数据不可信）", "r")],
"meta": "<span>个人开发者 · 2026-08-25 · 乙女向 AI 互动（中文主口径 + EN 补充）</span><span>30天差评 全部</span><span>评测池 2（中文）/ 9（全语言）</span>",
"pos": 0.0, "label": "好评 0.0%（API 中文口径，n=2，仅趋势参考）",
"comp": [
("🆕 中文新差评：AI slop + 反馈门槛", "×1", "「哈哈哈好大一坨3A大作，ai文案ai美术ai音乐，要反映bug居然要先交30块。进去后不到一分钟立马破绷，每次点开一个男角色的主页都会跳出一张ai味满满的大头照」（0.2h 09-12 新差评）——「反映 bug 需先购买」直接阻断反馈渠道"),
("🆕 EN 新差评：无 Steam 成就", "×1", "「No Steam achievements at all, which is disappointing for an otome game with multiple characters and story progression…It feels like a missed opportunity for achievement hunters」（1.1h 09-12 EN 新差评）——乙女向多线产品的成就系统缺位"),
("AI slop 判定跨语言一致（在池）", "×3", "「AI slop (tries to make you into a pay piggy) for poor gaymers」（17.6h 在池 EN）/俄区「тыща нейросеточных мужиков」——中英俄三语玩家对 AI 量产内容的判定完全一致"),
],
"pra": [],
"acts": [
("P2", "n=2 读数不可信（⚠️ -33.3pp 已标注），但两条新差评指向同一根因：发行工程完成度", "「反映 bug 要先交 30 块」+「无成就系统」均属发行层而非内容层问题。对自家：乙女/多线产品的成就系统是长尾留存的低成本杠杆；反馈渠道（社群/QA 入口）绝不能与付费墙绑定。"),
],
},
# ───────────────────────────── 无言之林 ─────────────────────────────
{
"title": "无言之林 (Wordless Forest)",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3978240/header.jpg",
"border": "var(--amb)",
"badges": [badge("55.6% 持平（72h ±0）；交互密度死因在池固化，读数稳定于 55 区间", "amb"), badge("API 55.6% / 商店 54.2%（+1.4 ✓）", "g")],
"meta": "<span>Solo dev · 2026-08-25 · 无对白生存氛围 FMV（EN）</span><span>30天差评 12</span><span>评测池 27（英文，72h ±0）</span>",
"pos": 55.6, "label": "好评 55.6%（API 英文口径，全库最低带）",
"comp": [
("交互密度不足（第一死因，在池）", "×4", "「My experience was 45 minutes long and I made around 7 decisions」（1.3h 在池）/「Not many decisions to be made and just got bored very quick」（0.2h 09-09 在池）——45min÷7 抉择 ≈ 6.4min/次"),
("游戏性存疑（在池）", "×2", "「Its a video with 5-7 choices. More of an art project than a game」（0.1h 在池）"),
],
"pra": [
("一人团队情怀（在池）", "×3", "「2 and a half years of solo development with 40 days spent outdoors, alone…That kind of dedication alone is worth the support」（1.5h 在池）"),
],
"en": "<b>EN 口径</b>：72h 无新增。一人实拍项目（2.5 年开发/40 天野外）的情怀与艺术性认可无法对冲「决策密度过低」的游戏性判定；读数连续多期稳定在 55 区间，情怀红利已到顶。",
"acts": [
("P2", "「情怀能救差评率救不了差评叙事」的长期验证样本：55.6% 稳定平台", "对自家：无对白/氛围型 FMV 的选择密度下限约 2-3 分钟/次；低于该密度就会被判「不是游戏」，制作投入（一人实拍）不被计入评分。"),
],
},
# ───────────────────────────── 雪落情书时 ─────────────────────────────
{
"title": "雪落情书时",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4740420/header.jpg",
"border": "var(--g)",
"badges": [badge("96.4% 持平（72h +1）；新评测认可非遗镜头真实感但点名男主配音出戏", "g"), badge("API 96.4% / 商店 95.3%（+1.1 ✓）", "g")],
"meta": "<span>山与海工作室 · 2026-08-14 · 单女主纯爱文旅 FMV</span><span>30天差评 1</span><span>评测池 591（中文，72h +1）</span>",
"pos": 96.4, "label": "好评 96.4%（API 中文口径）",
"comp": [
("男主配音出戏（在池+新证据）", "×2", "「男主刚开始的声音听着好习惯，有点结巴」（2.6h 09-13 新评测）/「男主配音也缺乏感情，像个机器人一样」（7.7h 在池）"),
("结局模糊（在池）", "×1", "「结局基本是相当于be，起码交代一下女主和男主确定关系的结局好吧，恋人未满？」（3.8h 在池）"),
],
"pra": [
("🆕 非遗镜头与真实感", "×1", "「穿插了不少体验非遗项目的镜头。但是恰恰这些视频显得女主更加真实，更加会有代入感沉浸感。主题曲很好听，价格也很实惠」（2.6h 09-13 新评测）"),
],
"acts": [
("P2", "「单女主纯爱+文旅结合」差异化持续获验证；男主配音是唯一系统性扣分项", "对自家：文旅/在地化实景是低成本差异化素材（政府合作+实景免搭棚）；配音选角与主角同等重要——男主声音的「结巴/机器人感」被连续两期点名。"),
],
},
# ───────────────────────────── 对不起，我是警察 ─────────────────────────────
{
"title": "对不起，我是警察",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4104120/header.jpg",
"border": "var(--a)",
"badges": [badge("78.0% 持平（72h ±0）；新评测认可港风题材但「流程短+坑没填」", "a"), badge("API 78.0% / 商店 78.6%（-0.6）", "g")],
"meta": "<span>戏格文化 · 2025-06-20 · 港风警匪 FMV</span><span>30天差评 1</span><span>评测池 758（中文，72h ±0）</span>",
"pos": 78.0, "label": "好评 78.0%（API 中文口径，长期平台）",
"comp": [
("🆕 篇幅与填坑（好评内批评）", "×1", "「剧情流程偏短，有一些地方明显安排的有点紧促，一些坑也没有填。剧情内容与《无间道》有一定的相似度…古惑仔的『痞气』并没有很多体现」（4.5h 09-12 新评测）"),
("重复剧情/QTE 少（在池）", "×1", "「太多重复剧情，QTE环节太少，过于简单」（9.0h 在池）"),
],
"pra": [
("🆕 港风宿命感认可", "×1", "「永远会为这类斗争中又带有宿命感的港风买单」（7.9h 09-07 在池）"),
],
"acts": [
("P2", "港风题材差异化成立但体量是硬伤——「无间道相似度」既是引流点也是天花板", "对自家：垂类风格题材（港风/谍战）的核心用户买账「氛围还原」，但 4-5h 体量下「坑没填」是高频批评；风格化产品更需要严密的伏笔回收。"),
],
},
# ───────────────────────────── 心之岛 ─────────────────────────────
{
"title": "心之岛",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3794770/header.jpg",
"border": "var(--amb)",
"badges": [badge("66.7%（68.3→66.7 微降，72h +1 差评）；偏差 +7.7 临界；「ABC 不调研」批评", "amb"), badge("API 66.7% / 商店 59.0%（+7.7 临界）", "amb")],
"meta": "<span>海外团队 · 2026-06 · 恋爱 FMV</span><span>30天差评 2</span><span>评测池 42（中文，72h +1）</span>",
"pos": 66.7, "label": "好评 66.7%（API 中文口径，n 小读数波动大）",
"comp": [
("🆕 文化错位批评", "×1", "「不推荐，剧情很差，真国外ABC做的游戏，完全不调研的」（3.3h 09-13 新差评）——海外团队写国内题材的本地化深度问题"),
("程序崩溃（在池）", "×1", "「第三章，索菲娅穿衣任务完成后，卡住，程序崩溃」（3.7h 在池）"),
],
"pra": [
("演员认可/剧情批评（在池）", "×1", "「演员不错，剧情不行」（3.4h 在池）"),
],
"acts": [
("P2", "「ABC 视角写国内题材」= 本地化缺位的产品级判定——跨文化制作必须配本地化主创", "对自家：若做跨市场题材（出海/回国双向），剧本层需要目标市场主创终审；「完全不调研」是比「写得差」更不可逆的差评标签。"),
],
},
# ───────────────────────────── Five Dates ─────────────────────────────
{
"title": "Five Dates",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1353270/header.jpg",
"border": "var(--amb)",
"badges": [badge("79.8% 持平（72h ±0），但 5.7h 玩家由好评改差评（翻评）+ 中文区技术差评", "amb"), badge("API 79.8% / 商店 85.1%（-5.3 临界）", "amb")],
"meta": "<span>Wales Interactive · 2020-11 · 视频约会 FMV（EN）</span><span>30天差评 1</span><span>评测池 884（英文，72h ±0）</span>",
"pos": 79.8, "label": "好评 79.8%（API 英文口径，长期阴跌通道）",
"comp": [
("🆕 长尾翻评：Wanted to like this", "×1", "「Wanted to like this more than I ended up doing, just not very good」（5.7h 09-14 04:30，由推荐改为不推荐）——6 年老作品的口碑缓慢折旧"),
("🆕 中文区技术差评", "×1", "「关键一段约会需要从头玩到尾…玩了3段约会卡死2次，游戏菜单都能调取的，只有画面不动，说明游戏没卡死，是剧情录像不动了」（0.8h 09-13 中文新差评）"),
("交互密度批评（在池）", "×2", "「选项没有什么多的剧情，只会影响好感度和1，2句不同的对话」（4.6h 在池）"),
],
"pra": [],
"en": "<b>EN 口径</b>：池量 884 持平，但出现 5.7h 玩家好评→差评翻转（推荐位不变、推荐态改变）；中文补充口径 2 条均为差评。品类早期（2020）作品在当下竞品池中的参照价值：交互密度与重玩价值的标准已被六年后的新品整体抬高。",
"acts": [
("P2", "老 FMV 的「翻评」现象：长尾期好评转差是缓慢阴跌的先行指标", "对自家：长尾监测需包含翻评（recommendation state change），单条翻评对老作品的信号强度高于新增差评；视频卡死类技术差评在 6 年老作上无修复预期，折旧不可逆。"),
],
},
# ───────────────────────────── The Complex ─────────────────────────────
{
"title": "The Complex",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1107790/header.jpg",
"border": "var(--a)",
"badges": [badge("77.7% 持平（72h +2 好评）；「类型佳作」与「太短」批评并存", "a"), badge("API 77.7% / 商店 78.0%（-0.3 ✓）", "g")],
"meta": "<span>Wales Interactive · 2020-07 · 科幻惊悚 FMV（EN）</span><span>30天差评 3</span><span>评测池 1064（英文，72h +2）</span>",
"pos": 77.7, "label": "好评 77.7%（API 英文口径，稳定）",
"comp": [
("选择意义不足（在池）", "×1", "「The acting and production is great, but none of the choices felt especially meaningful」（1.4h 在池）——欧美侧第一痛点样本"),
("Linux 兼容 bug（在池）", "×1", "「it is unplayable beyond that due to bugs…Very likely the game will get stuck and never load the next episode」（2.4h 09-10 在池）"),
],
"pra": [
("🆕 类型佳作定位好评", "×2", "「One of the better modern FMV games, worth playing for fans of the genre」（5.1h 09-13）/「Too short but fine I guess」（2.4h 09-11）"),
],
"acts": [
("P2", "欧美 FMV 老盘稳定：类型化好评（fans of the genre）+ 篇幅批评的固定组合", "对自家：「类型佳作」评价意味着存量用户圈层稳定但无破圈增量；多结局 FMV 的重玩价值（skip/undo/章节树）是拉高老盘口碑的少数杠杆。"),
],
},
# ───────────────────────────── 你好，你配吗？ ─────────────────────────────
{
"title": "你好，你配吗？",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4384120/header.jpg",
"border": "var(--g)",
"badges": [badge("96.8% 持平（72h ±0）；无新评测，快进缺失差评在池（上期 P0 未观测到修复证据）", "g"), badge("API 96.8% / 商店 95.9%（+0.9 ✓）", "g")],
"meta": "<span>小有互动 · 2026-04-18 · 相亲吐槽题材 FMV</span><span>30天差评 15</span><span>评测池 476（中文，72h ±0）</span>",
"pos": 96.8, "label": "好评 96.8%（API 中文口径，稳定）",
"comp": [
("无法快进（在池第一死因）", "×6", "「全是一大段一大段长的对话，无法倍速无法快进，纯纯坐牢」（0.3h 在池）/「对话不能快进，两小时光看两人打辩论赛」（2.0h 在池）——单一低频交互+长对话的复合死因"),
("交互缺失（在池）", "×3", "「游戏介绍里的可操作全部是骗人的…游戏里只能看对话」（5.3h 在池）——商店页交互承诺与实际不符"),
("价值观说教（在池）", "×2", "「玩家是来娱乐的，不是来上课的，用你教？」（0.5h 在池）"),
],
"pra": [
("题材敏感度与勇气（在池）", "×1", "「这个题材肯定是十分敏感的，懂的都懂，为制作组的勇气鼓掌」（0.9h 09-10 在池）——相亲吐槽题材的核心受众认可"),
],
"acts": [
("P2", "「无法快进」是差评池第一叙事且持续多期——对话密度型产品的最低工程底线", "对自家：长对话 FMV 的快进/倍速/已看跳过是 P0 功能而非优化项；上期标记后未观测到修复证据，每期 15 条满额差评中 6 条与此直接相关。"),
],
},
# ───────────────────────────── 东北往事 ─────────────────────────────
{
"title": "东北往事",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4056810/header.jpg",
"border": "var(--a)",
"badges": [badge("83.5% 持平（72h ±0）；窗口期静默，IP 改编盘稳定", "a"), badge("API 83.5% / 商店 84.1%（-0.6）", "g")],
"meta": "<span>十字星工作室 · 2026-08-15 · 黑道 IP 改编 FMV</span><span>30天差评 1</span><span>评测池 170（中文，72h ±0）</span>",
"pos": 83.5, "label": "好评 83.5%（API 中文口径）",
"comp": [
("剧情短（在池唯一差评主线）", "×1", "「剧情很短，看起来是靠事件相互交叉来映射几个不同的结局，可玩性一般般」（12.8h 在池）"),
],
"pra": [
("IP 还原与演员（在池）", "×2", "「由原著作者孔二狗执导，同名IP影视作品多位原班明星强势回归」（21.2h 在池）"),
],
"acts": [
("P2", "窗口期静默：IP 改编盘无新增信号——原著作者执导的原生 IP 是信任资产", "对自家：原作者执导/原班人马是 IP 改编的信任传递链；对照绍宋（无原作者参与的 IP 改编差评满额），IP 授权深度与口碑正相关。"),
],
},
# ───────────────────────────── 静默英文小盘 ─────────────────────────────
{
"title": "Cage of Roses",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2993720/header.jpg",
"border": "var(--a)",
"badges": [badge("87.8% 持平（72h ±0）", "a"), badge("API 87.8% / 商店 88.5%（-0.7 ✓）", "g")],
"meta": "<span>ebi-hime · 2025 · 吸血鬼百合视觉小说（EN）</span><span>30天差评 1</span><span>评测池 172（英文，72h ±0）</span>",
"pos": 87.8, "label": "好评 87.8%（API 英文口径）",
"comp": [
("expositionslop 批评（在池）", "×1", "「truly expositionslop. I don't know how you fumble the concept of vampire yuri this badly」（14.8h 09-05 在池）——「设定好、执行烂」的 VN 标准批评"),
("中文翻译质量（在池）", "×1", "「官中翻译严重不合格，古风得像ai生成的一般」（17.9h 在池）"),
],
"pra": [
("作者文笔认可（在池）", "×1", "「Melancholic and ever so beautiful…two very lonely women, both before and after they become each other's salvation」（7.9h 在池）"),
],
"acts": [
("P2", "百合 VN 的「设定卖点-执行」落差批评模板与中文区翻译质量批评并存", "对自家：出海 VN 的官中翻译是中文区口碑的独立变量（17.9h 差评全因翻译报废）；翻译质量验收需以「不出戏」为底线而非「能读懂」。"),
],
},
{
"title": "The Run",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3447920/header.jpg",
"border": "var(--a)",
"badges": [badge("88.9% 持平（72h ±0）", "a"), badge("API 88.9% / 商店 89.1%（-0.2 ✓）", "g")],
"meta": "<span>Sweet Bandits Studios · 2025 · 追杀惊悚 FMV（EN）</span><span>30天差评 3</span><span>评测池 45（英文，72h ±0）</span>",
"pos": 88.9, "label": "好评 88.9%（API 英文口径）",
"comp": [
("宣发承诺违背（在池）", "×1", "「This is the oldest professional writing rule broken. (You never break your promise to the audience.)」（2.3h 在池）——结局与商店页描述不符的「承诺违背」批评"),
("篇幅短+无法跳转（在池）", "×1", "「the unexpectedly short duration and the inability to skip around in the storyline absolutely kill the amount of value」（2.3h 在池）"),
],
"pra": [
("制作质量（在池）", "×1", "「The actors are much better than most other FMVs I've played…It is movie theater visual quality」（3.4h 在池）"),
],
"acts": [
("P2", "「商店页承诺-内容违背」是该作差评主叙事——宣发描述的审计是上线前必做项", "对自家：结局走向与商店页描述的符合度需产品+市场双签；「promise to the audience」被玩家当作专业写作规则引用，违背即差评。"),
],
},
{
"title": "Bloodholic",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1188710/header.jpg",
"border": "var(--a)",
"badges": [badge("98.1% 持平（72h ±0）；偏差 +9.9 临界（免费 VN 口径差异）", "a"), badge("API 98.1% / 商店 88.2%（+9.9 临界）", "amb")],
"meta": "<span>个人开发者 · 免费 · 吸血鬼视觉小说（中）</span><span>30天差评 1</span><span>评测池 54（中文，72h ±0）</span>",
"pos": 98.1, "label": "好评 98.1%（API 中文口径，免费小池）",
"comp": [
("无语音/代入感（在池唯一差评）", "×1", "「没有语音，剧情没有将我带入，不推荐，虽然免费」（0.5h 在池）"),
],
"pra": [
("剧情深度（在池）", "×1", "「这是我有史以来玩到过最喜欢的视觉小说…剧情非常有深意 世界观塑造的也很完美」（2.9h 在池）"),
],
"acts": [
("P2", "免费 VN 的口碑模型：深度认可与「无语音」批评并存——免费不豁免交付标准", "对自家：免费/低价只是获客杠杆，世界观深度才是口碑本体；音频缺位在小池产品中即构成唯一差评。"),
],
},
{
"title": "Libera Nos a Malo",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4902060/header.jpg",
"border": "var(--r)",
"badges": [badge("66.7%（2/3，72h ±0），$1.99 全 AI 低价带；n=3 读数不稳", "r"), badge("API 66.7% / 商店 66.7%（+0.0 ✓）", "g")],
"meta": "<span>个人开发者 · 2026-08 · 全 AI 宗教恐怖 FMV（EN）</span><span>30天差评 1</span><span>评测池 3（英文，72h ±0）</span>",
"pos": 66.7, "label": "好评 66.7%（API 英文口径，n=3 仅趋势参考）",
"comp": [
("AI slop 判定（在池）", "×1", "「AI slop (tries to make you into a pay piggy) for poor gaymers」（17.6h 在池 EN）——全 AI + 低价不豁免内容量判定"),
],
"pra": [],
"en": "<b>EN 口径</b>：72h 无新增。与列车怪谈（全 AI + 9.9 元，86.4%）对照：低价锚点只在内容量足够时才豁免 AI slop 判定——$1.99 + 内容量不足 = 66.7%。",
"acts": [
("P2", "全 AI 低价带的及格线由内容量决定：列车（86.4%）vs 本作（66.7%）的价差不在价格", "对自家：AI 产品的定价-内容量匹配矩阵：低价可对冲 AI 瑕疵但不能对冲「内容薄」；全 AI 产品需以同价位真人产品的内容量标准自检。"),
],
},
{
"title": "退婚后，宗主马甲藏不住",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2816920/header.jpg",
"border": "var(--r)",
"badges": [badge("26.8% 持平（72h ±0），全库最低分；竖屏+章节内购+短剧感三重死因在池固化", "r"), badge("API 26.8% / 商店 33.9%（-7.1）", "amb")],
"meta": "<span>个人开发者 · 2025 · 短剧改编竖屏互动（中）</span><span>30天差评 20（满额）</span><span>评测池 41（中文，72h ±0）</span>",
"pos": 26.8, "label": "好评 26.8%（API 中文口径，全库最低）",
"comp": [
("竖屏 PC 端形态错位（在池第一死因）", "×6", "「进游戏竖屏把我惊呆了，我还以为设置错误！内置付费也是一绝」（0.1h 在池）/「既然做了电脑端的游戏为什么不能全屏，而且还是竖屏的」（0.2h 在池）"),
("章节内购吃相（在池）", "×8", "「为什么要搞内购，是不是害怕玩家发现不值得然后退费」（0.1h 在池）/「明明是免费，第二章开始收费6元」（0.2h 在池）——免费+内购的 Steam 形态双重违背预期"),
("短剧搬运感（在池）", "×3", "「剧情直接照搬歪嘴龙王的剧情！这种套路的剧情真是满天飞，不用付费就能看到饱」（7.4h 在池）"),
],
"pra": [
("爽点受众存在（在池）", "×2", "「30块钱在现实生活中我能吃顿饭，在这里我却能当宗主，能体验被日本妹子和俄国妹子围堵的喜悦」（4.7h 在池）——核心受众的付费逻辑成立但无法对冲形态差评"),
],
"acts": [
("P2", "全库负面基线样本：竖屏+内购+短剧感的三重形态错位在 Steam 是不可逆死因", "对自家：手机端产品上 Steam 必须重构交互形态（横屏/买断/成就）；「能当宗主」的爽点受众存在说明题材可行，死于形态而非内容。"),
],
},
# ───────────────────────────── Rescue the Hostages ─────────────────────────────
{
"title": "Rescue the Hostages: Misaligned Fate",
"cover": "https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4619230/header.jpg",
"border": "var(--b)",
"badges": [badge("周扫恢复（周一）：英文主口径 0 条评测，商店全语言 n=1（中文好评）", "b"), badge("API 无数据 / 商店 100.0%（n=1）", "g")],
"meta": "<span>海外小团队 · 2026-09 · 拆弹解谜 FMV（EN）</span><span>30天差评 0</span><span>评测池 0（英文主口径）/ 1（全语言）</span>",
"pos": None, "label": "英文主口径无评测（score_desc: No user reviews）",
"comp": [],
"pra": [
("全语言唯一评测（在池，中文）", "×1", "「带有剧情的数字华容道模拟器，制作有些粗糙，期待未来的更新…游戏没有中文，推荐在设置里把视频英文字幕和数字华容道的图片序号打开」（0.6h 09-04 在池）——「有剧情的数字华容道」定位+制作粗糙判定"),
],
"en": "<b>EN 口径</b>：周扫恢复后英文池仍为 0 条评测。产品处于发售初期无口碑状态；中文区 1 条好评给出「数字华容道拆弹模拟器」的玩法画像与「无中文字幕」的本地化缺口。",
"acts": [
("P2", "零口碑冷启动样本：发售初期无英文评测——观察其从 0 到 1 的口碑启动路径", "对自家：记录该作后续首条英文评测的出现时间与内容（预期为解谜难度/无引导类反馈）；零评测期的商店页信息（视频/描述/标签）是唯一转化变量。"),
],
},
]

# ─────────────────────────────── HTML 拼装 ───────────────────────────────
cards = "\n".join(card(d) for d in APPS)

patterns = '''
<div class="pattern-grid">
<div class="pat-card"><div class="pat-num">01</div><h4>周末 72h 零清洗波：间歇性审计在 09-10 后停歇——「滚动审计」模型补上第三块拼图</h4><p>09-07（-929）→ 09-10（-63）→ 本期（0）：三个观测点构成「爆发-余波-停歇」节奏，全库 35 款主语言池零净移除（唯一例外是 Five Dates 一条好评改差评，属翻评非清洗）。间歇性审计模型至此完整：<b>清洗以波次出现，波次间隔 2-4 天，波间为净增长窗口</b>。对读数分析的含义：竞品趋势应按「波次基线日」（09-07、09-10）分段，波间期的新增数据可信度高，可直接用于口碑增量分析。</p><div class="pat-tags"><span class="tag from">全库 35 款（零移除）</span><span class="tag fix">对自家：波间期=口碑增量分析窗口；下一波时间未知，盯守女帝/绍宋/主角</span></div></div>
<div class="pat-card"><div class="pat-num">02</div><h4>「影游同质化疲劳」从单点扩散为品类预警：不心动「我腻了」与天平「花钱把妞看一遍」72h 内相继出现</h4><p>天平 09-09「真的没意思 越来越无聊」→ 09-11「就花钱把妞看一遍，每个人几乎一样的流程」；不心动 09-13「现在影游同质化太严重了…感觉以后可能会逐渐远离影游了，我腻了，我希望在影游乐趣中看到波涛，而不是在一堆波涛中硬找乐趣」。关键升级：<b>前者是单产品差评，后者是品类级退出宣言</b>——且来自全明星阵容产品（非粗制滥造盘）的中等时长玩家（5.2h）。同日不心动另一差评点名「陈老师老演这种角色，非常腻」：演员班底跨作复用的边际递减开始被显性记账。</p><div class="pat-tags"><span class="tag from">天平·不心动</span><span class="tag fix">对自家：题材/玩法差异化是留存项不是加分项；班底复用需控制节奏</span></div></div>
<div class="pat-card"><div class="pat-num">03</div><h4>女性向/男性凝视批评进入「运营对称性」阶段：制作人社媒回应本身成为差评素材</h4><p>金宵 72h 内 3 条新差评全部命中：「无时不刻的男凝视角才是最窒息的…女角色苦难叙事、男角色低素质反派，你算是两头都给得罪完了」（0.9h）；更具信号意义的是 4.0h 差评完整复述了制作人社媒时间线——「网友询问是否出现『辱男』词作者积极回应，询问是否出现『辱女』词作者当作没看见」。对照女帝篇在池差评「一边扯女性主义旗帜意图拔高立意，另一边抖机灵玩各种网络烂梗」（6.4h 08-29）与不心动「非要加一个黑妹」批评：<b>价值观内容批评不可逆，但「回应不对称」是可以避免的运营自伤</b>——全库首个「运营回应方式直接转化差评」的样本。</p><div class="pat-tags"><span class="tag from">金宵·不心动·女帝篇</span><span class="tag fix">对自家：争议回应必须对称+公开留档；社群运营记录是双刃资产</span></div></div>
<div class="pat-card"><div class="pat-num">04</div><h4>进度/存档/启动类 P0 四连发：高投入玩家遭遇进度丢失是最高危差评</h4><p>72h 内四款产品各中一枪：盛夏「全结局都解锁了进度卡在99%…存档都给我干没了」（15.8h 全成就玩家）；花满楼「第三年卡润王过不去 条件也达成了 不显示绿色」（12.7h 养成线玩家）；阴三国「卸载了再装也不行，Error: Couldn't load project data」（0.4h，启动即崩）；恶校「第一章死局…没办法从头开始，果断退款」（0.5h）。共同点：<b>受害玩家全部是流程后段/高投入玩家（或直接退款）</b>，且 bug 均为可预防的工程项（进度统计一致性、存档回滚保护、打包校验、死局重开入口）。</p><div class="pat-tags"><span class="tag from">盛夏·花满楼·阴三国·恶校</span><span class="tag fix">对自家：全结局自动化回归+存档回滚保护+死局重开入口=上线前 P0 三件套</span></div></div>
<div class="pat-card"><div class="pat-num">05</div><h4>AI 用途分界线新增「题材容错」维度：恐怖题材成为 AI 影游的最佳容器</h4><p>列车怪谈 5 条新评测给出双向证据：好评侧「感觉AI就适合用来做恐怖游戏」（6.8h）、「很多恐怖的妆造和场景…真人妆造很难模拟的」（3.5h 在池）；差评侧「跟红果短剧质量差不多」的 AI slop 判定仍在。合并既有证据（AI 用于实拍做不到的=被要求；AI 替代表演=差评放大器），本期补上第三条：<b>恐怖题材玩家对逻辑连贯性的容忍度高于推理/正剧题材，AI 瑕疵的差评转化率更低</b>。反面同日验证：绍宋新差评继续「AI 画面给我喂屎」（正剧题材），1000王子三语 AI slop 判定一致（乙女题材+内容量不足）。</p><div class="pat-tags"><span class="tag from">列车怪谈·绍宋·1000王子·阴三国</span><span class="tag fix">对自家：AI 预算投向奇观层+优先恐怖/惊悚题材容器</span></div></div>
<div class="pat-card"><div class="pat-num">06</div><h4>「单线为什么要做成选择性影游？」——玩家开始审判品类承诺本身</h4><p>媚娘篇新差评把全库第一痛点推到逻辑终点：「你这剧情是单线的为什么要做成选择性影游呢？选择两个字体现在哪呢？」（7.4h 09-12）。同期佐证：女帝篇「很多正确选项跟错误选项本质上是一个意思，但就是会剧情杀」（4.3h 09-14）、江山北望「剧情看似有很多选择，实则都是死路」（4.1h 09-10 在池）、The Complex「none of the choices felt especially meaningful」（在池）。<b>玩家对「互动性」的评价已从『选择不够多』升级为『选择是否该存在』</b>——互动影游的品类合法性本身进入被审计阶段。</p><div class="pat-tags"><span class="tag from">媚娘篇·女帝篇·江山北望·The Complex</span><span class="tag fix">对自家：产品定义期自问「去掉选择后还成立吗」；不成立才立项</span></div></div>
<div class="pat-card"><div class="pat-num">07</div><h4>方法论：d3all 翻页通道将周末 72h 原文捕获率从个位数拉到 76 条</h4><p>本期（首个 72h 跨周末窗口）新增 day_range=3 游标翻页通道（≤6 页/款），捕获新评测原文 76 条（对照上期 24h 窗口仅 4 条）：女帝篇 18、绍宋 6、江山 7、列车 5、恶校 5、不心动 4、媚娘 4……覆盖率 76/68 新增（含翻评与改评）。代价可控（每款 +6 次请求）。结论：<b>「d3 翻页采集」应固化为跨周末窗口的标准配置</b>，工作日 24h 窗口维持原 d1 通道不变。</p><div class="pat-tags"><span class="tag from">采集管线</span><span class="tag fix">对自家：周末窗口 SOP 固化 d3all；下期观察翻页深度是否需按池量自适应</span></div></div>
</div>'''

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>玩家心声报告 v1.1 | 2026-09-14</title>
<style>{CSS}</style>
</head>
<body>
<div class="c">

<header>
  <h1>玩家心声报告 v1.1</h1>
  <div class="sub">互动影游竞品 · Steam 评测深读 · 2026-09-14（周一）· 池内 35 款 · 35 款全部采集（Rescue the Hostages 周扫恢复）· 第 23 期 · 72h 窗口（09-11→09-14，跨周末 09-12/09-13 不跑）：全库主语言 +68 新增（正 53 / 负 23，捕获原文口径）· 新评测原文捕获 76 条（d3all 翻页通道首次启用）· 零清洗波（09-07/-929、09-10/-63 后首个净增长窗口）· 数据口径：day_range=30 负面抽样 + 主语言全量抽样 + day_range=3 翻页捕获（中文游戏 schinese / 英文游戏 english，1000王子 补全语言口径）· 商店基线：pool0911 快照回退（当日 intel 2026-09-14 未落盘，已标注；intel 落盘后下期校正）</div>
</header>

<!-- ═══ Hero ═══ -->
<div class="hero">
  <div class="hero-tag">⚡ CORE FINDING</div>
  <h2>周末 72h 零清洗波（全库零移除），+68 新增中女帝篇 +16 领跑且好评侧由「配角塑造」驱动；金宵 58.5→57.0 续跌且 3 条新差评把批评从内容层打到制作人社媒回应层；盛夏/花满楼/阴三国/恶校四款各爆一个进度/存档/启动/死局 P0；「同质化疲劳」从天平扩散到不心动（「我腻了…以后可能会逐渐远离影游了」）</h2>
  <p class="lead">间歇性审计在 09-10 后停歇：三个观测点（-929 → -63 → 0）补全「爆发-余波-停歇」节奏，波间期 = 净增长可信窗口。本期最大信号在好评侧：女帝篇 72h +16 中至少 4 条明确点名配角动机自洽（季怀衷「被背刺到但可悲可敬」、长孙太尉「根据局势做取舍」）——权谋题材的口碑护城河从主角/CP 扩散到配角层。负向侧：金宵 3 条新差评两两同日，男凝/DEI 批评升级为对制作人「辱男词积极回应/辱女词装看不见」的社媒时间线复述（全库首个运营回应直接转化差评的样本）；盛夏 15.8h 全成就玩家遭遇「进度 99% 卡死 + 存档回滚丢失」双 P0；花满楼「条件达成不显示绿色」、阴三国 pck 启动崩溃（重装无效）、恶校第一章死局无重开（直接退款）——四款 P0 全部命中流程后段/高投入玩家。疲劳叙事升级：不心动 5.2h「影游同质化太严重…我腻了，以后可能会逐渐远离影游了」与天平「就花钱把妞看一遍」72h 内相继出现，且不心动另一差评点名演员班底「陈老师老演这种角色，非常腻」——品类留存预警首次来自全明星产品。列车怪谈 86.4（-0.5），5 条新评测确认「AI 适合恐怖题材」成为好评侧共识；DeepWeb 评测池 11→13 起量初现（20h 求扩散长评的传播效果）；Five Dates 出现 5.7h 玩家好评改差（翻评）。方法论：d3all 翻页通道首次启用，原文捕获 76 条（上期 4 条），周末窗口 SOP 固化。</p>
  <div class="hero-stats">
    <div class="hero-stat"><span class="hsv">35</span><span class="hsl">池内产品（35 采集）</span></div>
    <div class="hero-stat"><span class="hsv">+68</span><span class="hsl">72h 全库净增（零清洗）</span></div>
    <div class="hero-stat"><span class="hsv">76</span><span class="hsl">新评测原文捕获</span></div>
    <div class="hero-stat"><span class="hsv">16</span><span class="hsl">P0+P1 建议</span></div>
    <div class="hero-stat"><span class="hsv">7</span><span class="hsl">交叉模式</span></div>
  </div>
</div>

<!-- ═══ Quick Strip ═══ -->
<div class="quick-strip">
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4148240/ad47878cf250027da631c4678102b8167fd166c1/capsule_616x353_schinese.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">女王的游戏 女帝篇</span><span class="qrating warn">82.5%</span></div>
    <div class="qbar"><div class="pos" style="width:82%"></div><div class="neg" style="width:18%"></div></div>
    <div class="qtag">🟢 72h +16 全库领跑 · 配角塑造成好评新引擎（季怀衷/长孙太尉）· 2 条新差评：bgm 消失音频 bug + 「红果短剧水平」逻辑批评 · 登录故障第 23 日</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3831120/6a5af0317c2156f49b790588f09484e1f63cbbed/capsule_616x353.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">江山北望</span><span class="qrating ok">91.3%</span></div>
    <div class="qbar"><div class="pos" style="width:91%"></div><div class="neg" style="width:9%"></div></div>
    <div class="qtag">🟢 72h +8 持续领跑质量盘 · 「微选择重拍」被 12.2h 长评命名为差异化资产 · 「男人一生只哭13次」玩家梗二创 = 沉浸深度证据</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4143220/4925056509db1533da002335787556f640ac1a2e/capsule_616x353.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">金宵公寓事件</span><span class="qrating bad">57.0%</span></div>
    <div class="qbar"><div class="pos" style="width:57%"></div><div class="neg" style="width:43%"></div></div>
    <div class="qtag">🔴 续跌 58.5→57.0，60 关口渐远 · 3 条新差评：男凝/DEI 升级到「制作人社媒回应不对称」+ 完形填空关键词不可复制 · 唯一可控杠杆是解谜交互层</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/4292950/dfd52caf6453e43b4d613a662064aca4924a7858/header.jpg?t=1787201131" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">绍宋：还我河山</span><span class="qrating warn">81.0%</span></div>
    <div class="qbar"><div class="pos" style="width:81%"></div><div class="neg" style="width:19%"></div></div>
    <div class="qtag">72h +5 持平 · 9.4h 长评工程批评三连（1080p only/战旗窗口化漂移/单机网络异常登不上）· AI/杨沂真/水军叙事第 25 日零稀释 · 新增「镶钻美甲」穿帮</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/4920100/aecf4db2323a4eebc76013235e0091fd07a600a2/header_schinese.jpg?t=1788225078" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">列车怪谈：虚像之境</span><span class="qrating ok">86.4%</span></div>
    <div class="qbar"><div class="pos" style="width:86%"></div><div class="neg" style="width:14%"></div></div>
    <div class="qtag">🟠 微降 86.9→86.4 · 5 条新评测确认「AI 适合恐怖游戏」共识 · 探索度/QTE/章节断流三 bug 第二周未修复 · 低价锚点持续对冲</div>
  </div>
  <div class="qcard">
    <div class="qcard-top"><img class="qicon" src="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/3987560/capsule_616x353_schinese.jpg" alt="" loading="lazy" onerror="this.style.display='none'"><span class="qname">盛夏离与合</span><span class="qrating warn">84.7%</span></div>
    <div class="qbar"><div class="pos" style="width:85%"></div><div class="neg" style="width:15%"></div></div>
    <div class="qtag">🔴 P0：15.8h 全成就玩家「进度卡 99% + ALT+F4 后存档回滚丢失」，重复触发 · 收官作的收尾 bug 会定死系列终章印象</div>
  </div>
</div>

<div class="section">
<div class="section-title">逐款分析 <span class="st-num">35 款 · 按信号强度排序 · 好评率为 API 抽样（已与商店页基线比对，基线取 pool0911 快照回退——当日 intel 未落盘，下期校正）</span></div>
{cards}
</div>

<div class="section">
<div class="section-title">跨产品交叉模式 <span class="st-num">7 条 · 2+ 款游戏共现的问题/赞美</span></div>
{patterns}
</div>

<!-- ═══ Self Eval ═══ -->
<div class="self-eval">
<h4>📊 自评 · 第 23 期</h4>
<div class="se-grid">
<div class="se-item"><div class="score g">68</div><div class="lbl">评测覆盖数（72h 新增）</div><div class="note">正 53 + 负 23（捕获原文口径）· 原文捕获 76/68（含翻评与改评）· 35/35 款完成采集（Rescue 周扫恢复）· d3all 翻页通道首次启用即达 76 条（上期 4 条）</div></div>
<div class="se-item"><div class="score g">100%</div><div class="lbl">数据完整性 · 偏差标注率</div><div class="note">35/35 款全部标注偏差 · ⚠️≥15pp：1000王子（-33.3，n=2，数据不可信）· 临界：Bloodholic +9.9 / 心之岛 +7.7 / DeepWeb +6.2 / Five Dates -5.3 · 基线 pool0911 快照回退（当日 intel 未落盘，标注于头部）</div></div>
<div class="se-item"><div class="score a">19</div><div class="lbl">可行动建议（P0×5 + P1×14）</div><div class="note">≥3 合格 ✓ · P0：盛夏进度+存档 / 花满楼条件判定 / 阴三国启动崩溃 / 恶校死局重开 / 列车怪谈探索度三bug</div></div>
<div class="se-item"><div class="score g">7</div><div class="lbl">交叉模式数</div><div class="note">≥2 合格 ✓ · 🆕 周末零清洗波（#1，间歇审计模型补全）/ 同质化疲劳扩散（#2）/ 运营对称性差评（#3）/ 进度类 P0 四连（#4）/ AI 题材容错（#5）/ 品类承诺审判（#6）/ d3all 方法论（#7）</div></div>
</div>
<div class="next-steps"><strong>⚠️ 已知数据缺口与明日盯守</strong>① 基线回退：当日 intel 2026-09-14 未落盘（08:00 机器人延迟，已知问题），商店口径以 pool0911 快照代替，部分 dev 值含一周漂移——intel 落盘后下期校正；② 女帝篇 3 条 5.1h 配角好评疑似同一玩家连发（09-11/12/13），虽独立池内佐证存在，单作者贡献需在趋势判断中折扣；③ Five Dates 5.7h 好评改差未计入新增（翻评），其池量不变但读数承压；④ Rescue the Hostages 英文池 0 评测，无趋势可判。明日盯守：第三波清洗是否出现（女帝/绍宋/主角——主角 -3 已 4 日无后续）、金宵 57 关口能否止跌、盛夏/花满楼 P0 是否被玩家追评确认修复、列车怪谈 86 底线、女帝篇配角叙事是否持续沉淀、DeepWeb 池量（13→?）、天平×不心动疲劳叙事是否再增样本、当日 intel 落盘后基线校正。</div>
</div>

<footer>
  <div>玩家心声报告 · 第 23 期 · 由玩家心声机器人每工作日 08:00 生成（周末停跑，周一为 72h 窗口）· 数据源：Steam appreviews API（day_range=30 负面 + 主语言全量 + day_range=3 翻页捕获）</div>
  <div class="rn">下一期：2026-09-15（周二，24h 窗口）</div>
</footer>

</div>
</body>
</html>'''

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Saved {OUT} ({len(html)} bytes)")

# HTML 标签平衡校验
class Checker(HTMLParser):
    VOID = {"meta", "img", "br", "hr", "link", "input"}
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"mismatch </{tag}> at {self.getpos()}, top={self.stack[-1] if self.stack else None}")
c = Checker()
c.feed(html)
if c.errors or c.stack:
    print("HTML ERRORS:", c.errors[:5], "unclosed:", [t for t, _ in c.stack][:5])
    raise SystemExit(1)
print("HTML tag balance: OK")
