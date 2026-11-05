from lib import *

S = {}
def add(name, inner, story=False): S[name] = (page(inner, story), story)

DISC = "Halcyon offers simulated educational accounts. Results not guaranteed. T&amp;C apply."

def follow(name, head, sub, seed, disc=False):
    """End slide for news, explainers and memes: follow, save, Discord. Same CTA as TikTok."""
    add(name, bg(seed, "up", glow=(50, 40)) +
        f'<div class="gp hot ctr" style="position:absolute;left:64px;right:64px;top:300px;padding:64px 56px">'
        f'<div style="width:96px;height:96px;margin:0 auto;border-radius:50%;border:4px solid #00FBF4;position:relative;box-shadow:0 0 40px rgba(0,251,244,.5)"><div style="position:absolute;left:28px;top:28px;width:32px;height:32px;border-radius:50%;background:#00FBF4"></div></div>'
        f'<h1 class="hl m" style="margin-top:36px">{head}</h1><p class="body" style="margin-top:20px">{sub}</p>'
        f'<div style="display:flex;justify-content:center;gap:14px;margin-top:40px"><span class="pill on" style="font-size:20px;padding:14px 28px">Follow</span><span class="pill" style="font-size:20px;padding:14px 28px">Save</span><span class="pill" style="font-size:20px;padding:14px 28px">Discord in bio</span></div></div>'
        + (f'<p class="disc ctr" style="position:absolute;left:64px;right:64px;bottom:116px">{DISC}</p>' if disc else "") + foot(None))

def promo_end(name, head, sub, seed):
    add(name, bg(seed, "up", glow=(50, 35)) +
        f'<div class="gp hot ctr" style="position:absolute;left:64px;right:64px;top:290px;padding:60px 56px">'
        f'<p class="lab">Halcyon Dynamic &middot; $50K evaluation</p><h1 class="hl m" style="margin-top:16px">{head}</h1><p class="body" style="margin-top:20px">{sub}</p>'
        f'<div style="margin-top:40px"><span class="pill on" style="font-size:24px;padding:18px 36px;letter-spacing:.06em;text-transform:none">Start from $51 &middot; link in bio</span></div>'
        f'<div style="margin-top:26px"><div class="tog"><span class="on">Trailing $51</span><span>End of day $53</span></div></div></div>'
        f'<p class="disc ctr" style="position:absolute;left:64px;right:64px;bottom:116px">{DISC}</p>' + foot(None))

# =====================================================================
# NEWS 01 · NEWS BRIEF (carousel)
# =====================================================================
add("nbA_1", bg(7, "vshape") + hero_chart(7, "vshape", top=96, h=500) +
    '<div class="pad" style="top:640px"><span class="pill">News brief &middot; Wed 4 Nov</span>'
    '<h1 class="hl" style="margin-top:22px">The Dow&rsquo;s best <span class="glow">post-midterm day</span> since 1982</h1></div>' +
    stats([("Dow", "+3.03%", "53,356", True), ("S&amp;P 500", "+1.58%", "7,689", True), ("Nasdaq", "+1.44%", "25,737", True)], 1000) + foot())
add("nbA_2", bg(8, "drop") + header_panel("Wednesday 4 Nov", 'Not everyone was <span class="glowr">celebrating</span>') +
    bars([("Gold", "Spot", 3.3, "+3.3%"), ("Dow", "Index", 3.03, "+3.03%"), ("S&amp;P 500", "Index", 1.58, "+1.58%"),
          ("Russell 2000", "Index", 1.58, "+1.58%"), ("Nasdaq", "Composite", 1.44, "+1.44%"),
          ("WTI crude", "Per barrel", -8.5, "&minus;8.5%"), ("VIX", "Fear gauge", -19.5, "&asymp;&minus;20%")], 370, 10) +
    '<div class="pad" style="top:1060px"><p class="body ctr">Oil slid to about <b>$89</b> and the fear gauge took most of the day off.</p></div>' +
    src("Sources: TheStreet, CNN, Finwire. Gold, oil and VIX approximate. Bars capped at 10%.") + foot())
add("nbA_3", bg(9, "up") + header_panel("Why it moved", 'Three things <span class="glow">changed overnight</span>') +
    steps([("The waiting was over.", "The results came in, and a known result is easier to price than a guess."),
           ("Gridlock.", "Investors bet on a divided government, where big policy swings get harder to pass."),
           ("Cheaper oil.", "Crude fell about 8.5% as war-risk talk cooled, and the 10-year yield eased to around 4.89%.")], 400, gap=22) +
    src("Sources: CNN, TheStreet, Finwire. Market reaction only, no political view.") + foot())

def pts_rows(rows, top):
    out = [f'<div class="pad" style="top:{top}px;display:flex;flex-direction:column;gap:16px">']
    for sym, name, move, up in rows:
        out.append(f'<div class="gp {"" if up else "red"}" style="display:flex;align-items:center;gap:26px;padding:24px 32px"><div class="num" style="font-size:48px;width:130px">{sym}</div>'
                   f'<div style="flex:1;font-size:22px;color:#AFB8BC">{name}</div><div class="num {"glow" if up else "glowr"}" style="font-size:46px">{move}</div></div>')
    out.append('</div>')
    return "".join(out)
add("nbA_4", bg(10, "up") + header_panel("What it meant for futures", 'The move, <span class="glow">in points</span>') +
    pts_rows([("ES", "S&amp;P 500 futures", "+119.7 pts", True), ("YM", "Dow futures", "+1,569 pts", True),
              ("RTY", "Russell 2000 futures", "+44.5 pts", True), ("CL", "Crude oil, per barrel", "&asymp;&minus;$8.30", False)], 400) +
    src("Index and spot moves shown as a guide. Futures closes differ slightly.") + foot())
add("nbA_5", bg(11, "spike") + header_panel("The Halcyon angle", 'Your <span class="glow">$2,000 drawdown</span> vs Wednesday', hot=True) +
    meter("1 ES", 40, 119.7, "pts", 420, "$50 a point, so $2,000 of room is 40 points.") +
    meter("1 MES", 400, 119.7, "pts", 700, "$5 a point, so the same $2,000 is 400 points.") +
    '<div class="pad" style="top:990px"><p class="body ctr">Same chart, same day. The size you pick decides how much of it your account can sit through.</p></div>' +
    src("$50K Halcyon Dynamic evaluation. Simulated. Points rounded.") + foot())
follow("nbA_6", 'Big days make more sense <span class="glow">in points</span>', "Follow for the next one, and save this before your next news day.", 12, disc=True)

add("nbB_1", bg(21, "down") + hero_chart(21, "down", top=96, h=500) +
    '<div class="pad" style="top:640px"><span class="pill">News brief &middot; October 2026</span>'
    '<h1 class="hl" style="margin-top:22px">A rough month inside <span class="glow">a good year</span></h1></div>' +
    stats([("S&amp;P 500", "&minus;2.11%", "7,580", False), ("Nasdaq", "&minus;6.03%", "25,437", False), ("VIX", "+30.6%", "Fear gauge", True)], 1000) + foot())

def colbars(groups, top, scale=12):
    zero = 380
    out = [f'<div class="gp" style="position:absolute;left:64px;right:64px;top:{top}px;height:700px;padding:0">',
           f'<div style="position:absolute;left:40px;right:40px;top:{zero}px;height:2px;background:rgba(255,255,255,.1)"></div>']
    gx = 50
    for g, bs in groups:
        out.append(f'<div style="position:absolute;left:{gx}px;top:{zero + 245}px;width:380px;text-align:center;font-size:25px;font-weight:500">{g}</div>')
        bx = gx + 50
        for lab, v, t in bs:
            hp = abs(v) / scale * 300; up = v >= 0; col = CY if up else DN
            y = zero - hp if up else zero + 2; ty = y - 54 if up else y + hp + 10
            out.append(f'<div style="position:absolute;left:{bx}px;top:{y:.0f}px;width:120px;height:{hp:.0f}px;border-radius:{"16px 16px 4px 4px" if up else "4px 4px 16px 16px"};background:{col};box-shadow:0 0 30px {col}66"></div>'
                       f'<div class="num" style="position:absolute;left:{bx - 35}px;width:190px;text-align:center;top:{ty:.0f}px;font-size:32px;color:{col}">{t}</div>'
                       f'<div style="position:absolute;left:{bx - 35}px;width:190px;text-align:center;top:{zero + 200}px"><span class="pill gr">{lab}</span></div>')
            bx += 160
        gx += 470
    out.append('</div>')
    return "".join(out)
add("nbB_2", bg(22, "down") + header_panel("October vs the year", 'Down for the month, <span class="glow">up for the year</span>') +
    colbars([("S&amp;P 500", [("Oct", -2.11, "&minus;2.11%"), ("YTD", 10.52, "+10.52%")]),
             ("Nasdaq Composite", [("Oct", -6.03, "&minus;6.03%"), ("YTD", 9.47, "+9.47%")])], 380) +
    src("Source: Tapeboard monthly recap, October 2026.") + foot())
add("nbB_3", bg(23, "down") + header_panel("What drove it", 'Where October <span class="glowr">went sideways</span>') +
    steps([("AI spending doubts.", "Big tech kept raising its AI budgets, and investors started asking when it pays off."),
           ("Chip warnings.", "Intel cut its outlook late in the month, and chip stocks followed it down."),
           ("Oil shocks.", "Attacks in the Middle East pushed crude higher, and energy was one of the few sectors to lead."),
           ("Nerves.", "The VIX climbed about 30% across the month.")], 380, gap=16, big=29, small=22) +
    src("Sources: Tapeboard, AP and Reuters reporting.") + foot())
add("nbB_4", bg(24, "down") + header_panel("The Halcyon angle", 'October vs a <span class="glow">$2,000 drawdown</span>', hot=True) +
    meter("1 ES", 40, 163, "pts", 420, "The S&amp;P 500 moved about 163 points over the month.") +
    meter("1 MES", 400, 163, "pts", 700, "Same move on a micro uses well under half the room.") +
    '<div class="pad" style="top:990px"><p class="body ctr">A slow month can still be a big move. Size for the month you might get.</p></div>' +
    src("$50K Halcyon Dynamic evaluation. Simulated. Points rounded.") + foot())
follow("nbB_5", 'Months like this <span class="glow">are the practice</span>', "Follow for the monthly recap, and tell us how October treated you in our Discord.", 25, disc=True)

# =====================================================================
# NEWS 02 · GROUP CHAT (carousel)  - the day's news told as a chat
# =====================================================================
def chat(name, title, msgs, seed, left="Swipe &rarr;"):
    rows = []
    for who, side, txt in msgs:
        if who: rows.append(f'<p class="who" style="{"align-self:flex-end;margin-right:12px" if side == "r" else ""}">{who}</p>')
        rows.append(f'<div class="bubble {side}">{txt}</div>')
    add(name, bg(seed, "flat", glow=(50, 10)) +
        f'<div class="gp" style="position:absolute;left:64px;right:64px;top:80px;bottom:150px;padding:0;overflow:hidden">'
        f'<div style="display:flex;align-items:center;gap:18px;padding:26px 32px;border-bottom:1px solid rgba(255,255,255,.06);background:rgba(0,0,0,.2)">'
        f'<div style="width:58px;height:58px;border-radius:50%;background:linear-gradient(135deg,#00FBF4,#0A5C5E);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:24px;color:#022">FT</div>'
        f'<div><div style="font-size:26px;font-weight:700">{title}</div><div style="font-size:17px;color:#7D878C">4 members &middot; Wed 4 Nov</div></div></div>'
        f'<div style="display:flex;flex-direction:column;gap:22px;padding:34px 34px">{"".join(rows)}</div></div>' + foot(left))
chat("gcA_1", "futures traders 📈", [("jay", "l", "oil just dropped 8% 💀"), ("me", "r", "on a WEDNESDAY??"),
     ("jay", "l", "election results came in and the war-risk talk cooled off"), ("me", "r", "so the CL long i was &ldquo;holding for the weekend&rdquo;..."),
     ("jay", "l", "we don&rsquo;t talk about the CL long")], 41)
chat("gcA_2", "futures traders 📈", [("sam", "l", "wait what did gold do"), ("jay", "l", "back above 4k"),
     ("sam", "l", "and the dow??"), ("jay", "l", "+1,569 &#128558;"),
     ("me", "r", "i was flat all day 🙃"), ("sam", "l", "most disciplined thing you&rsquo;ve ever done tbh")], 42)
add("gcA_3", bg(43, "drop") + header_panel("What actually happened", 'The chat, <span class="glow">fact-checked</span>') +
    checklist([("&asymp;&minus;8.5%", "Oil fell to about $89", WN, False), ("+3.3%", "Gold back above $4,000", OK, True),
               ("+3.03%", "Dow, best post-midterm day since 1982", OK, False), ("+1.58%", "S&amp;P 500 closed at 7,689", OK, False),
               ("&asymp;&minus;20%", "VIX, the fear gauge", NO, False)], 400, h=112) +
    '<div class="pad" style="top:1050px"><p class="body ctr">Being flat on a wild day still counts as a good day.</p></div>' +
    src("Wed 4 Nov 2026. Sources: TheStreet, CNN, Finwire. Approximate.") + foot(None))

# =====================================================================
# NEWS 03 · NEWS ALERT (singles)
# =====================================================================
def alert(name, kicker, title, chart_kind, seed, a, b, la, lb, up, sub, srct):
    ca, cb = ("#3A4A50", DN) if not up else ("#3A4A50", CY)
    ha, hb = (360, 330) if not up else (330, 360)
    add(name, bg(seed, chart_kind) +
        f'<div class="gp hot" style="position:absolute;left:64px;right:64px;top:96px;height:640px;padding:0;overflow:hidden">'
        f'<div style="position:absolute;left:0;right:0;bottom:70px;display:flex;justify-content:center;gap:70px;align-items:flex-end">'
        f'<div class="ctr"><div class="num" style="font-size:44px">{a}</div><div style="width:210px;height:{ha}px;border-radius:20px 20px 6px 6px;background:{ca};margin-top:14px"></div><div style="margin-top:14px"><span class="pill gr">{la}</span></div></div>'
        f'<div class="ctr"><div class="num {"glow" if up else "glowr"}" style="font-size:44px">{b}</div><div style="width:210px;height:{hb}px;border-radius:20px 20px 6px 6px;background:{cb};box-shadow:0 0 50px {cb}77;margin-top:14px"></div><div style="margin-top:14px"><span class="pill {"on" if up else "r"}">{lb}</span></div></div></div></div>'
        f'<div class="pad" style="top:790px"><span class="pill r">&#9679; {kicker}</span><h1 class="hl" style="margin-top:22px">{title}</h1><p class="body" style="margin-top:18px">{sub}</p></div>'
        + src(srct) + foot(None))
alert("naA", "Oil", 'Oil had a <span class="glowr">rough Wednesday</span>', "drop", 61, "&asymp;$97.7", "&asymp;$89.4", "Tue", "Wed", False,
      "WTI fell about 8.5% in one session as war-risk talk cooled after the election.", "Source: Finwire, CNBC via Stocktitan. 4 Nov 2026. Approximate.")
alert("naB", "Gold", 'Gold is back <span class="glow">above $4,000</span>', "spike", 62, "&asymp;$3,933", "&asymp;$4,063", "Tue", "Wed", True,
      "Up about 3.3% as the dollar and bond yields slipped.", "Source: Finwire, 4 Nov 2026. Spot gold, approximate.")
add("naC", bg(63, "vshape") + hero_chart(63, "vshape", top=96, h=640, op=.3) +
    '<div style="position:absolute;left:64px;right:64px;top:300px;text-align:center"><div class="num glow" style="font-size:210px;line-height:1">+1,569</div><span class="pill on" style="margin-top:10px">Dow points &middot; Wed 4 Nov</span></div>'
    '<div class="pad" style="top:790px"><span class="pill r">&#9679; Stocks</span><h1 class="hl" style="margin-top:22px">The Dow&rsquo;s best day <span class="glow">since April 2025</span></h1>'
    '<p class="body" style="margin-top:18px">Up 3.03% to 53,356, its biggest post-midterm gain since 1982.</p></div>' + src("Source: CNN, CFRA Research, TheStreet. 4 Nov 2026.") + foot(None))

# =====================================================================
# NEWS 04 · MARKET MOOD (single)
# =====================================================================
moods = [("Dow", "Best day since April 2025", "+3.03%", True, "on"), ("Gold", "Back above $4K", "+3.3%", True, "on"),
         ("S&amp;P 500", "Vibing", "+1.58%", True, ""), ("Russell 2000", "Along for the ride", "+1.58%", True, ""),
         ("Oil", "Down bad", "&minus;8.5%", False, "r"), ("VIX", "Took the day off", "&asymp;&minus;20%", False, "gr")]
add("mdA", bg(71, "up", glow=(50, 15)) + header_panel("Market mood &middot; Wed 4 Nov", 'How every market&rsquo;s <span class="glow">Wednesday went</span>') +
    '<div class="pad" style="top:400px;display:flex;flex-direction:column;gap:14px">' +
    "".join(f'<div class="gp {"hot" if i == 0 else ("red" if c == "r" else "")}" style="display:flex;align-items:center;gap:20px;padding:22px 30px">'
            f'<div style="width:250px;font-size:30px;font-weight:700">{m}</div><div style="flex:1"><span class="pill {c}" style="text-transform:none;letter-spacing:.02em;font-size:20px">{mood}</span></div>'
            f'<div class="num {"glow" if up else "glowr"}" style="font-size:36px">{p}</div></div>' for i, (m, mood, p, up, c) in enumerate(moods)) +
    '</div>' + src("Sources: TheStreet, CNN, Finwire. Gold, oil and VIX approximate.") + foot(None))

# =====================================================================
# NEWS 05 · THIS WEEK (carousel)
# =====================================================================
def daycards(days, top):
    cells = []
    for d, n, lab, hot in days:
        cells.append(f'<div class="gp {"hot" if hot else ""} ctr" style="padding:20px 12px;border-radius:24px;min-height:220px"><p class="lab">{d}</p><div class="num {"glow" if hot else ""}" style="font-size:58px;margin-top:4px">{n}</div>'
                     f'<div style="font-size:18px;line-height:1.3;color:#C9D1D4;margin-top:8px">{lab}</div></div>')
    return f'<div class="pad" style="top:{top}px;display:grid;grid-template-columns:repeat(5,1fr);gap:12px">{"".join(cells)}</div>'

def event(name, kicker, wd, d, time, title, what, why, note=None, seed=1, big=None, bigpill=None):
    extra = f'<div class="gp red" style="margin-top:16px;display:flex;gap:20px;align-items:center">{WN}<p class="body" style="font-size:24px"><b>Halcyon rule:</b> {note}</p></div>' if note else ""
    add(name, bg(seed, "flat") +
        f'<div class="pad" style="top:110px;display:flex;align-items:center;gap:26px"><div class="gp hot ctr" style="padding:18px 30px;border-radius:26px"><p class="lab">{wd}</p><div class="num glow" style="font-size:82px;line-height:1">{d}</div></div>'
        f'<div><span class="pill">{kicker}</span><div style="font-size:26px;color:#C9D1D4;margin-top:14px">&#9719;&nbsp; {time}</div></div></div>'
        f'<div class="pad" style="top:400px"><h1 class="hl m">{title}</h1>'
        f'<div class="gp" style="margin-top:30px"><p class="lab">What it is</p><p class="body" style="margin-top:10px">{what}</p></div>'
        f'<div class="gp hot" style="margin-top:16px"><p class="lab" style="color:#00FBF4">Why traders care</p><p class="body" style="margin-top:10px">{why}</p></div>{extra}</div>'
        + (f'<div class="pad ctr" style="top:{1010 if note else 960}px"><div class="num glow" style="font-size:{96 if note else 120}px;line-height:1">{big}</div><div style="margin-top:14px"><span class="pill">{bigpill}</span></div></div>' if big else "") + foot())

add("wkA_1", bg(4, "flat", glow=(50, 20)) +
    '<div class="pad ctr" style="top:220px"><span class="pill">This week &middot; 9 to 13 Nov</span><h1 class="hl xl" style="margin-top:28px">Inflation week <span class="glow">is here</span></h1>'
    '<p class="body" style="margin-top:24px">Two price reports, with a bond holiday in the middle.</p></div>' +
    daycards([("Mon", "9", "Earnings: Constellation, Barrick", False), ("Tue", "10", "CPI, 8:30 AM ET", True),
              ("Wed", "11", "Veterans Day, bonds shut", False), ("Thu", "12", "Jobless claims", False), ("Fri", "13", "PPI, 8:30 AM ET", True)], 820) +
    foot("Swipe for each one &rarr;"))
event("wkA_2", "The big one", "Tue", "10", "8:30 AM ET", "CPI: the consumer price index",
      "How much prices changed in October for the things people buy, from groceries to rent.",
      "A hot or cool number can move ES and NQ by dozens of points in seconds.",
      "news straddles around releases are a banned practice. Plan before 8:30, or sit it out.", 11, "8:30 AM ET", "Set an alarm")
event("wkA_3", "The holiday", "Wed", "11", "All day", "Veterans Day",
      "The US bond market is closed. Stock markets and CME futures keep trading.",
      "With bonds shut, rate traders step back and moves can feel thinner than usual.", None, 12, "Bonds off", "Futures still open")
event("wkA_4", "The follow-up", "Fri", "13", "8:30 AM ET", "PPI: the producer price index",
      "What businesses paid for goods and services, one step before prices reach shoppers.",
      "It lands three days after CPI, so it can back up the week&rsquo;s story or flip it.", None, 13, "8:30 AM ET", "Friday morning")
add("wkA_5", bg(14, "flat") + header_panel("Save this week", 'Know the times <span class="glow">before the chart</span>') +
    checklist([("Tue 8:30 AM", "CPI", WN, True), ("Wed", "Bond market closed", NO, False), ("Thu 8:30 AM", "Jobless claims", OK, False),
               ("Fri 8:30 AM", "PPI", WN, True), ("Daily 4:45 PM", "Be flat (Halcyon)", OK, False)], 400, h=110) +
    src("All times Eastern. Sources: BLS schedule, Schwab week ahead, SIFMA.") + foot(None))

add("wkB_1", bg(31, "flat", glow=(50, 20)) +
    '<div class="pad ctr" style="top:220px"><span class="pill">This week &middot; 23 to 27 Nov</span><h1 class="hl xl" style="margin-top:28px">Short week, <span class="glow">busy Wednesday</span></h1>'
    '<p class="body" style="margin-top:24px">Thanksgiving cuts two sessions short.</p></div>' +
    daycards([("Mon", "23", "Normal hours", False), ("Tue", "24", "Normal hours", False), ("Wed", "25", "GDP + PCE, 8:30 AM ET", True),
              ("Thu", "26", "Halt 1:00 PM ET", True), ("Fri", "27", "Close 1:15 PM ET", True)], 820) + foot("Swipe for each one &rarr;"))
event("wkB_2", "Double release", "Wed", "25", "8:30 AM ET", "GDP and PCE at once",
      "Q3 growth (second estimate) and October PCE, the Fed&rsquo;s favourite inflation gauge.",
      "Two big numbers at the same second, the day before a holiday.",
      "news straddles around releases are a banned practice.", 32, "8:30 AM ET", "Two numbers, one second")
event("wkB_3", "Holiday hours", "Thu", "26", "Halt 1:00 PM ET", "Thanksgiving",
      "Stock markets are shut. Equity index futures halt at 1:00 PM ET and reopen at 6:00 PM ET.",
      "Thin, quiet trading. A small order can move price more than you expect.", None, 33, "1:00 PM ET", "Halt")
event("wkB_4", "Early close", "Fri", "27", "Close 1:15 PM ET", "The day after",
      "Equity index futures close early at 1:15 PM ET. Stocks close at 1:00 PM ET.",
      "Liquidity fades fast after lunch, so plan your exit early.", None, 34, "1:15 PM ET", "Early close")
add("wkB_5", bg(35, "flat") + header_panel("Save this week", 'Holiday hours, <span class="glow">in one place</span>') +
    checklist([("Wed 8:30 AM", "GDP + PCE", WN, True), ("Thu 1:00 PM", "Equity futures halt", NO, False), ("Thu 6:00 PM", "Reopen", OK, False),
               ("Fri 1:15 PM", "Early close", NO, True), ("Mon 30", "Normal hours", OK, False)], 400, h=110) +
    src("Equity index futures, Eastern Time. Confirm on cmegroup.com closer to the date.") + foot(None))

# =====================================================================
# EXPLAINER 01 · YOUR DRAWDOWN IN POINTS (carousel)
# =====================================================================
add("etA_1", bg(51, "up", glow=(70, 30)) +
    '<div class="pad" style="top:200px"><span class="pill">Every trader should know</span><h1 class="hl xl" style="margin-top:28px">How many points is <span class="glow">your drawdown?</span></h1></div>'
    '<div class="gp hot ctr" style="position:absolute;left:64px;right:64px;top:760px;padding:40px">'
    '<p class="lab">Max drawdown &middot; $50K evaluation</p><div class="num glow" style="font-size:150px;line-height:1.05;margin-top:10px">$2,000</div>'
    '<div style="margin-top:18px"><span class="pill on" style="font-size:20px">= ? points</span></div></div>' + foot("Swipe to find out &rarr;"))
pv = [("ES", "S&amp;P 500", "$50"), ("MES", "Micro S&amp;P", "$5"), ("NQ", "Nasdaq-100", "$20"), ("MNQ", "Micro Nasdaq", "$2"), ("CL", "Crude oil, per $1", "$1,000"), ("GC", "Gold, per $1", "$100")]
add("etA_2", bg(52, "flat") + header_panel("Step 1", 'What <span class="glow">one point</span> is worth') +
    '<div class="pad" style="top:390px;display:grid;grid-template-columns:1fr 1fr;gap:16px">' +
    "".join(f'<div class="gp {"hot" if c == "ES" else ""}" style="padding:26px 30px"><div style="display:flex;justify-content:space-between;align-items:baseline"><span class="num" style="font-size:40px">{c}</span><span class="num glow" style="font-size:40px">{v}</span></div><div style="font-size:19px;color:#8A959A;margin-top:4px">{n}</div></div>' for c, n, v in pv) +
    '</div><div class="pad" style="top:1010px"><p class="body ctr">One point on ES is four ticks of $12.50 each.</p></div>' + src("CME contract specs.") + foot())
room = [("ES", "40 pts"), ("MES", "400 pts"), ("NQ", "100 pts"), ("MNQ", "1,000 pts"), ("CL", "$2.00 a barrel"), ("GC", "$20 an ounce")]
add("etA_3", bg(53, "flat") + header_panel("Step 2", '$2,000 of room, <span class="glow">in points</span>', hot=True) +
    checklist([(v, f"1 {c}", f'<div class="ic" style="border:2px solid rgba(0,251,244,.45);color:#00FBF4;font-size:13px;font-weight:700;width:58px;border-radius:14px">{c}</div>', c == "ES") for c, v in room], 390, h=108) +
    '<div class="pad" style="top:1090px"><p class="body ctr">$2,000 divided by the point value. That&rsquo;s your whole cushion on one contract.</p></div>' + foot())
add("etA_4", bg(54, "spike") + header_panel("Step 3 &middot; real example", 'Wed 4 Nov: S&amp;P 500 <span class="glow">+119.7 pts</span>') +
    meter("1 ES", 40, 119.7, "pts", 400, "Three times the whole cushion, in one session.") +
    meter("1 MES", 400, 119.7, "pts", 680, "Under a third of the cushion. Same chart.") +
    '<div class="pad" style="top:980px"><p class="body ctr">If that day went against you, size decided whether the account was still there on Thursday.</p></div>' +
    src("Simulated. $50K Halcyon Dynamic evaluation.") + foot())
minis = '<div style="width:150px;height:150px;border-radius:26px;background:#00FBF4;box-shadow:0 0 40px rgba(0,251,244,.5)"></div>'
micros = "".join('<div style="width:58px;height:58px;border-radius:14px;background:#00FBF4;opacity:.8;box-shadow:0 0 14px rgba(0,251,244,.4)"></div>' for _ in range(10))
add("etA_5", bg(55, "flat") + header_panel("Step 4", '10 Micros <span class="glow">= 1 Mini</span>') +
    f'<div class="gp" style="position:absolute;left:64px;right:64px;top:390px;display:flex;justify-content:center;align-items:center;gap:50px;padding:46px">'
    f'<div class="ctr">{minis}<div style="margin-top:16px"><span class="pill gr">1 ES</span></div></div><div style="font-size:80px;color:#AFAFAF">=</div>'
    f'<div class="ctr"><div style="display:grid;grid-template-columns:repeat(5,58px);gap:12px">{micros}</div><div style="margin-top:16px"><span class="pill gr">10 MES</span></div></div></div>'
    '<div class="gp hot" style="position:absolute;left:64px;right:64px;top:780px"><p class="lab" style="color:#00FBF4">On Halcyon Dynamic</p><p class="body" style="margin-top:10px">The limit is <b>5 Mini or 25 Micro</b>. Maxing out on micros is the same size as <b>2.5 Mini</b>, so you can scale in smaller steps.</p></div>' + foot())
follow("etA_6", 'Know your cushion <span class="glow">before you size</span>', "Save this cheat sheet, and ask us anything about it in our Discord.", 56, disc=True)

# =====================================================================
# EXPLAINER 02 · MARKET, LIMIT OR STOP (carousel)
# =====================================================================
def ladder(prices, marks, top=380):
    """prices: list of strings top to bottom; marks: {idx: (label, kind)}"""
    rows = []
    for i, p in enumerate(prices):
        lab, kind = marks.get(i, ("", ""))
        st = {"buy": "border:1.5px solid rgba(0,251,244,.55);background:rgba(0,251,244,.08);box-shadow:0 0 24px rgba(0,251,244,.15)",
              "now": "border:1.5px solid rgba(255,255,255,.35);background:rgba(255,255,255,.06)",
              "fill": "border:1.5px solid rgba(255,107,120,.55);background:rgba(255,107,120,.08)"}.get(kind, "border:1.5px solid transparent")
        pill = f'<span class="pill {"on" if kind == "buy" else ("r" if kind == "fill" else "gr")}">{lab}</span>' if lab else ""
        rows.append(f'<div style="display:flex;justify-content:space-between;align-items:center;height:92px;padding:0 26px;border-radius:20px;{st}"><span class="num" style="font-size:34px">{p}</span>{pill}</div>')
    return f'<div class="gp" style="position:absolute;left:64px;width:560px;top:{top}px;padding:14px">{"".join(rows)}</div>'

px = ["6,003.00", "6,002.00", "6,001.00", "6,000.00", "5,999.00", "5,998.00"]
add("etB_1", bg(57, "flat", glow=(70, 25)) +
    '<div class="pad" style="top:200px"><span class="pill">Every trader should know</span><h1 class="hl xl" style="margin-top:28px">Market, limit <span class="glow">or stop?</span></h1>'
    '<p class="body" style="margin-top:24px">Three order types, and when each one can surprise you.</p></div>' +
    hero_chart(57, "drop", top=700, h=480, op=.45) + '<div class="pad" style="top:900px;display:flex;gap:14px;justify-content:center"><span class="pill on" style="font-size:24px;padding:16px 30px">Market</span><span class="pill" style="font-size:24px;padding:16px 30px">Limit</span><span class="pill r" style="font-size:24px;padding:16px 30px">Stop</span></div>' + foot("Swipe to learn &rarr;"))
def ordslide(name, step, title, lad, side_lab, side_txt, note, seed, red=False):
    add(name, bg(seed, "flat") + header_panel(step, title) + lad +
        f'<div class="gp {"red" if red else "hot"}" style="position:absolute;left:648px;right:64px;top:380px;padding:30px 28px"><p class="lab" style="color:{"#FF6B78" if red else "#00FBF4"}">{side_lab}</p><p class="body" style="margin-top:12px;font-size:25px">{side_txt}</p></div>'
        f'<div class="pad" style="top:990px"><div class="gp"><p class="body" style="font-size:24px">{note}</p></div></div>' + foot())
ordslide("etB_2", "Market order", 'Fills <span class="glow">right now</span>', ladder(px, {3: ("Price now", "now"), 2: ("You fill", "buy")}),
         "Use it when", "Getting in or out matters more than the exact price.", "In a fast market, the price you see and the price you get can be a tick or two apart.", 58)
ordslide("etB_3", "Limit order", 'Your price <span class="glow">or better</span>', ladder(px, {1: ("Price now", "now"), 4: ("Buy limit", "buy")}),
         "Use it when", "You care about the price and you&rsquo;re fine missing the trade.", "If price never reaches your level, nothing happens. That&rsquo;s the trade-off.", 59)
ordslide("etB_4", "Stop order", 'Triggers, <span class="glowr">then fills</span>', ladder(px, {1: ("Long entry", "now"), 3: ("Sell stop", "buy"), 5: ("Filled here", "fill")}),
         "Watch out", "A stop becomes a market order when it&rsquo;s touched. On CPI at 8:30, it can fill past your price.", "Halcyon rule: trading with no stop loss is a banned practice. Use one every time.", 60, red=True)
follow("etB_5", 'Pick the order <span class="glow">before the moment</span>', "Save this, and follow for more explainers in plain English.", 61, disc=True)

# =====================================================================
# EXPLAINER 03 · MEME EXPLAINER (carousels)
# =====================================================================
def meme(name, idx, panel, rule, seed, red=True):
    add(name, bg(seed, "flat") + f'<div class="pad" style="top:84px"><span class="pill">{idx}</span></div>'
        f'<div class="gp" style="position:absolute;left:64px;right:64px;top:160px;height:780px;padding:0;overflow:hidden">{panel}</div>'
        f'<div class="gp {"red" if red else "hot"}" style="position:absolute;left:64px;right:64px;top:970px;display:flex;gap:22px;align-items:center">{WN if red else OK}<p class="body" style="font-size:25px">{rule}</p></div>' + foot())
add("mmA_1", bg(71, "drop", glow=(70, 30)) + hero_chart(71, "drop", top=96, h=520) +
    '<div class="pad" style="top:680px"><span class="pill">Evaluation memes</span><h1 class="hl" style="margin-top:22px">4 ways to fail <span class="glow">without a losing trade</span></h1>'
    '<p class="body" style="margin-top:20px">Your strategy can be fine and these still end the account.</p></div>' + foot())
meme("mmA_2", "Meme 01 &middot; the clock",
     '<div style="padding:50px 54px;font-size:40px;font-weight:700;line-height:1.25">Me at 4:44 PM, still in the trade:<br><span style="font-weight:400;color:#AFB8BC;font-size:31px">&ldquo;one more minute, it&rsquo;s coming back&rdquo;</span></div>'
     '<div class="ctr" style="margin-top:20px"><div class="num glowr" style="font-size:200px;line-height:1;font-variant-numeric:tabular-nums">4:44</div><div style="margin-top:16px"><span class="pill r">PM ET &middot; position open</span></div></div>',
     "Be <b>flat by 4:45 PM ET</b>. Holding past it breaks the rules, even when the trade is green.", 72)
meme("mmA_3", "Meme 02 &middot; the stop",
     '<div style="padding:60px 50px;display:flex;flex-direction:column;gap:28px">'
     '<p class="who">mentor</p><div class="bubble l">where&rsquo;s your stop loss?</div>'
     '<p class="who" style="align-self:flex-end;margin-right:12px">me</p><div class="bubble r">I don&rsquo;t need one. I can feel the market.</div>'
     '<p class="who">mentor</p><div class="bubble l">...</div>'
     '<div style="align-self:flex-end;font-size:19px;color:#68737A;letter-spacing:.1em">READ 4:12 PM</div></div>',
     "Trading with <b>no stop loss</b> is on Halcyon&rsquo;s list of banned practices.", 73)
meme("mmA_4", "Meme 03 &middot; the cheat code",
     '<div style="padding:50px 54px;font-size:38px;font-weight:700;line-height:1.25">Me at 8:29:59 thinking I found a cheat code:</div>'
     '<div style="margin:10px 70px 0;display:flex;flex-direction:column;gap:40px;align-items:stretch">'
     '<div style="border:2px solid rgba(0,251,244,.6);border-radius:22px;padding:22px 28px;font-size:30px;font-weight:500;color:#00FBF4;display:flex;justify-content:space-between;box-shadow:0 0 30px rgba(0,251,244,.15)"><span>BUY STOP</span><span>+10 ticks</span></div>'
     '<div class="ctr"><span class="pill r" style="font-size:24px;padding:12px 26px">CPI &middot; 8:30:00</span></div>'
     '<div style="border:2px solid #3A464C;border-radius:22px;padding:22px 28px;font-size:30px;font-weight:500;color:#AFAFAF;display:flex;justify-content:space-between"><span>SELL STOP</span><span>&minus;10 ticks</span></div></div>',
     "<b>News straddles around releases</b> are banned. Orders on both sides of the print can get rewards denied.", 74)
meme("mmA_5", "Meme 04 &middot; the big brain",
     '<div style="padding:50px 54px;font-size:38px;font-weight:700;line-height:1.25">Can&rsquo;t lose if I&rsquo;m on both sides.</div>'
     '<div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin:20px 54px 0">'
     '<div class="gp hot"><p class="lab">Account 1</p><div class="num glow" style="font-size:56px;margin-top:10px">LONG</div><div style="font-size:28px">2 MES</div></div>'
     '<div class="gp red"><p class="lab">Account 2</p><div class="num glowr" style="font-size:56px;margin-top:10px">SHORT</div><div style="font-size:28px">2 MES</div></div></div>'
     '<div class="ctr" style="font-size:130px;margin-top:10px">&#129504;</div>',
     "<b>Hedging</b> is banned, including across accounts and micro against mini.", 75)
add("mmA_6", bg(76, "flat") + header_panel("The takeaway", 'Read the rules <span class="glow">before the chart</span>') +
    checklist([("Daily", "Flat by 4:45 PM ET", OK, True), ("Every trade", "Use a stop loss", OK, False), ("News", "No straddles", NO, False), ("Accounts", "No hedging", NO, False)], 400, h=112) +
    '<div class="pad" style="top:960px"><p class="body ctr">The full list of banned practices is in the Trader Agreement on the Halcyon site.</p></div>' +
    f'<p class="disc ctr" style="position:absolute;left:64px;right:64px;bottom:116px">{DISC}</p>' + foot(None))

def myth(name, idx, claim, verdict, expl, seed):
    m = verdict == "MYTH"
    add(name, bg(seed, "flat", glow=(50, 30)) + f'<div class="pad" style="top:96px"><span class="pill">Myth or fact &middot; {idx}</span></div>'
        f'<div class="gp ctr" style="position:absolute;left:64px;right:64px;top:200px;padding:70px 56px 60px"><div style="font-size:150px;line-height:.5;color:rgba(0,251,244,.25);font-weight:700">&ldquo;</div><h1 class="hl m" style="margin-top:20px">{claim}</h1></div>'
        f'<div class="ctr" style="position:absolute;left:0;right:0;top:640px"><div style="display:inline-block;border:5px solid {DN if m else CY};color:{DN if m else CY};font-weight:700;font-size:84px;letter-spacing:.08em;padding:4px 40px;border-radius:24px;transform:rotate(-4deg);box-shadow:0 0 50px {(DN if m else CY)}44">{verdict}</div></div>'
        f'<div class="gp {"red" if m else "hot"}" style="position:absolute;left:64px;right:64px;top:850px"><p class="body">{expl}</p></div>' + foot())
add("mmB_1", bg(81, "flat", glow=(50, 25)) +
    '<div class="pad ctr" style="top:330px"><span class="pill">Evaluation edition</span><h1 class="hl xl" style="margin-top:30px;font-size:130px">Myth <span class="g">or</span> <span class="glow">fact?</span></h1>'
    '<p class="body" style="margin-top:30px">Five things traders get wrong about the $50K evaluation.</p>'
    '<div style="display:flex;justify-content:center;gap:16px;margin-top:40px"><span class="pill r" style="font-size:24px;padding:14px 30px">Myth</span><span class="pill on" style="font-size:24px;padding:14px 30px">Fact</span></div></div>' + foot("Play along &rarr;"))
myth("mmB_2", "01", "You need weeks to pass an evaluation.", "MYTH", "The minimum on Halcyon Dynamic is <b>1 day</b>. Treat it as a floor. Most of the work is keeping what you make.", 82)
myth("mmB_3", "02", "No daily loss limit means no limit.", "MYTH", "There&rsquo;s no daily loss limit on reward accounts, but the <b>drawdown still applies</b>. On a $50K account that&rsquo;s $2,000.", 83)
myth("mmB_4", "03", "25 Micro is the same size as 5 Mini.", "MYTH", "10 Micros equal 1 Mini, so 25 Micro is <b>2.5 Mini</b>. Half the size, in smaller steps.", 84)
myth("mmB_5", "04", "You can trade right through the close.", "MYTH", "Be <b>flat by 4:45 PM ET</b>. The daily break starts at 5:00 PM ET.", 85)
myth("mmB_6", "05", "You can pick how your drawdown works.", "FACT", "Choose <b>Trailing ($51)</b> or <b>end of day ($53)</b>. Same $2,000 drawdown, different rules for when it moves.", 86)
follow("mmB_7", 'How many did <span class="glow">you get right?</span>', "Drop your score in the comments, and bring your questions to our Discord.", 87, disc=True)

# =====================================================================
# EXPLAINER 04 · KNOW YOUR HOURS (singles)
# =====================================================================
def hours(name, kicker, head, rows, srct, seed):
    add(name, bg(seed, "flat") + header_panel(kicker, head) + checklist(rows, 400, h=118) + src(srct) + foot(None))
hours("khA", "Eastern Time", 'A Halcyon <span class="glow">trading day</span>',
      [("Sun 6:00 PM", "Week opens", OK, False), ("Mon to Fri", "Trades almost 24 hours", OK, False), ("4:45 PM", "Be flat (Halcyon rule)", WN, True),
       ("5:00 to 6:00 PM", "Daily break", NO, False), ("Fri 5:00 PM", "Week closes", NO, False)],
      "CME Globex hours for equity index futures. Flat-by time from Halcyon rules.", 91)
hours("khC", "Thanksgiving week &middot; Eastern Time", 'Holiday hours <span class="glow">for ES and NQ</span>',
      [("Wed 25", "Normal day", OK, False), ("Thu 26, 1:00 PM", "Equity futures halt", NO, True), ("Thu 26, 6:00 PM", "Reopen", OK, False),
       ("Fri 27, 1:15 PM", "Early close", NO, True), ("Mon 30", "Back to normal", OK, False)],
      "CME holiday schedule for equity index futures. Confirm on cmegroup.com closer to the date.", 92)

# =====================================================================
# PROMO 01 · HALCYON DYNAMIC IN FOUR CARDS (carousel)
# =====================================================================
def fan(top):
    cards = [("Target", "$3,000", -14, -330, 40), ("Drawdown", "$2,000", -5, -110, 10), ("Contracts", "5 / 25", 5, 110, 10), ("Flat by", "4:45 PM", 14, 330, 40)]
    out = [f'<div style="position:absolute;left:0;right:0;top:{top}px;height:560px">']
    for i, (lab, v, rot, dx, dy) in enumerate(cards):
        out.append(f'<div class="gp {"hot" if i == 1 else ""} ctr" style="position:absolute;left:{540 - 140 + dx}px;top:{dy + 40}px;width:280px;height:400px;transform:rotate({rot}deg);display:flex;flex-direction:column;justify-content:center;padding:20px">'
                   f'<p class="lab">{lab}</p><div class="num glow" style="font-size:52px;margin-top:12px">{v}</div><div style="margin-top:18px"><span class="pill gr">{i + 1} / 4</span></div></div>')
    out.append('</div>')
    return "".join(out)
add("dyA_1", bg(101, "up", glow=(50, 55)) +
    '<div class="pad ctr" style="top:130px"><span class="pill">Halcyon Dynamic</span><h1 class="hl xl" style="margin-top:26px">Your $50K evaluation <span class="glow">in four cards</span></h1></div>' +
    fan(560) + foot("Deal them &rarr;"))
def dcard(name, n, lab, big, sub, extra, seed):
    add(name, bg(seed, "up", glow=(50, 45)) +
        f'<div class="pad ctr" style="top:110px"><p class="lab">Halcyon Dynamic &middot; $50K evaluation</p></div>'
        '<div class="gp" style="position:absolute;left:180px;right:180px;top:340px;height:700px;opacity:.3"></div><div class="gp" style="position:absolute;left:145px;right:145px;top:300px;height:700px;opacity:.55"></div>'
        f'<div class="gp hot" style="position:absolute;left:110px;right:110px;top:260px;height:700px;padding:56px 56px 60px">'
        f'<span class="pill">{n} / 4</span><p style="font-size:38px;font-weight:500;margin:30px 0 0">{lab}</p>'
        f'<div class="num glow" style="font-size:170px;line-height:1.05;margin-top:10px">{big}</div>{extra}'
        f'<p class="body" style="margin-top:30px;font-size:29px">{sub}</p></div>'
        f'<div class="pad ctr" style="top:1110px;display:flex;justify-content:center;gap:14px">' + "".join(f'<div style="width:{60 if k == n else 18}px;height:18px;border-radius:9px;background:{"#00FBF4" if k == n else "rgba(255,255,255,.18)"};box-shadow:{"0 0 16px rgba(0,251,244,.6)" if k == n else "none"}"></div>' for k in range(1, 5)) + '</div>' + foot())
dcard("dyA_2", 1, "Profit target", "$3,000", "Reach it in simulated trading to pass. The minimum is 1 trading day.", "", 102)
dcard("dyA_3", 2, "Max drawdown", "$2,000", "You pick the type at checkout.", '<div style="margin-top:26px"><div class="tog"><span class="on">Trailing $51</span><span>End of day $53</span></div></div>', 103)
dcard("dyA_4", 3, "Contract limit", "5 / 25", "Up to 5 Mini or 25 Micro contracts at once.", '<div style="margin-top:18px;display:flex;gap:12px"><span class="pill on">Mini</span><span class="pill">Micro</span></div>', 104)
dcard("dyA_5", 4, "Session close", "4:45 PM", "Be flat by 4:45 PM ET, every trading day.", '<div style="margin-top:18px"><span class="pill r">Eastern Time</span></div>', 105)
add("dyA_6", bg(106, "up") + header_panel("Good to know", 'Three more things <span class="glow">traders ask about</span>') +
    steps([("No daily loss limit.", "Reward accounts have no daily loss limit. The drawdown still applies."),
           ("A one-time evaluation fee.", "Pay once for the evaluation. Every rule is on the site before you start."),
           ("Your platform, your choice.", "Volumetrica, TradingView, Quantower or DeepCharts.")], 420, gap=22, big=36, small=26) +
    '<div class="pad" style="top:1080px"><p class="body ctr">Read the full rules before day one. It feels so much calmer.</p></div>' + foot())
promo_end("dyA_7", 'Ready to <span class="glow">deal yourself in?</span>', "One $50K simulated evaluation, from $51.", 107)

# =====================================================================
# PROMO 02 · WHY HALCYON (singles)
# =====================================================================
def whyq(name, head, items, seed):
    add(name, bg(seed, "up", glow=(85, 10)) +
        f'<div class="pad" style="top:110px"><h1 class="hl xl">{head}</h1></div>' + steps(items, 340, gap=22, big=38, small=27) +
        f'<p class="disc ctr" style="position:absolute;left:64px;right:64px;bottom:116px">{DISC}</p>' + foot(None))
whyq("whA", 'Why <span class="glow">Halcyon?</span>',
     [("One fee, from $51.", "A one-time fee for a $50K simulated evaluation."),
      ("Pass in as little as 1 day.", "There&rsquo;s a 1-day minimum, so the clock is yours."),
      ("No daily loss limit on reward accounts.", "The drawdown is the line that matters."),
      ("Your choice of drawdown.", "Trailing for $51 or end of day for $53.")], 111)
whyq("whB", 'Who is it <span class="glow">for?</span>',
     [("Futures traders with a plan.", "ES, NQ, CL, GC and more on CME, COMEX, NYMEX and CBOT."),
      ("Traders on any schedule.", "Futures trade almost 24 hours, Sunday evening to Friday."),
      ("Traders who love their platform.", "Volumetrica, TradingView, Quantower or DeepCharts."),
      ("People who read the rules first.", "Every rule is written down before you pay.")], 112)
plats = [("Volumetrica", "Order flow and footprint"), ("TradingView", "Charts most traders already know"), ("Quantower", "Multi-window desktop"), ("DeepCharts", "Depth and flow tools")]
add("whC", bg(113, "flat", glow=(50, 20)) + header_panel("Platforms", 'Trade on what <span class="glow">you already know</span>') +
    '<div class="pad" style="top:420px;display:grid;grid-template-columns:1fr 1fr;gap:18px">' +
    "".join(f'<div class="gp {"hot" if i == 0 else ""}" style="height:250px;display:flex;flex-direction:column;justify-content:space-between"><div style="width:52px;height:52px;border-radius:50%;border:2px solid rgba(0,251,244,.5);display:flex;align-items:center;justify-content:center;color:#00FBF4;font-weight:700;font-size:22px">{n[0]}</div><div><div class="num" style="font-size:38px">{n}</div><div style="font-size:20px;color:#AFB8BC;margin-top:4px">{d}</div></div></div>' for i, (n, d) in enumerate(plats)) +
    '</div>' + f'<p class="disc ctr" style="position:absolute;left:64px;right:64px;bottom:116px">Third-party platforms, not affiliated. {DISC}</p>' + foot(None))

# =====================================================================
# STORIES · ONE BIG NUMBER (1080x1920)
# =====================================================================
def story(name, big, unit, line, card_img, card_title, seed, kind):
    add(name, bg(seed, kind, story=True, glow=(50, 25)) +
        f'<div class="pad ctr" style="top:470px"><div class="num glow" style="font-size:250px;line-height:.95;letter-spacing:-.04em">{big}<span style="font-size:90px;letter-spacing:0;margin-left:14px">{unit}</span></div>'
        f'<p style="font-size:46px;font-weight:500;line-height:1.25;margin:40px 0 0">{line}</p></div>'
        f'<div class="gp hot" style="position:absolute;left:64px;right:64px;top:1150px;display:flex;align-items:center;gap:40px;padding:30px">'
        f'<div style="width:420px;flex:none;background:#fff;border-radius:22px;padding:12px;transform:rotate(-3deg);box-shadow:0 30px 70px rgba(0,0,0,.7)">'
        f'<div style="display:flex;align-items:center;gap:10px;padding:2px 4px 10px"><div style="width:28px;height:28px;border-radius:50%;background:#03070A;border:3px solid #00FBF4"></div><span style="color:#111;font-size:16px;font-weight:600">Halcyon</span></div>'
        f'<img src="{card_img}" style="width:100%;display:block;border-radius:8px"></div>'
        f'<div><p style="font-size:36px;font-weight:700;line-height:1.2;margin:0">{card_title}</p><div style="margin-top:26px"><span class="pill on" style="font-size:20px">&larr; Tap to read</span></div></div></div>'
        '<div style="position:absolute;left:64px;right:64px;top:300px;display:flex;justify-content:center">' + wordmark("margin:0") + '</div>', story=True)

# =====================================================================
# LAUNCH 01 · WELCOME (pinned carousel)
# =====================================================================
add("wcA_1", bg(131, "up", glow=(50, 38)) +
    '<div class="ctr" style="position:absolute;left:0;right:0;top:250px">'
    '<div style="width:190px;height:190px;margin:0 auto;border-radius:50%;border:8px solid #00FBF4;position:relative;box-shadow:0 0 80px rgba(0,251,244,.55),inset 0 0 40px rgba(0,251,244,.25)"><div style="position:absolute;left:47px;top:47px;width:80px;height:80px;border-radius:50%;background:#00FBF4;box-shadow:0 0 40px rgba(0,251,244,.8)"></div></div>'
    '<h1 class="hl xl" style="margin:70px 64px 0">Welcome to <span class="glow">Halcyon</span></h1>'
    '<p class="body" style="margin:28px 120px 0">Futures news in plain English, rules you&rsquo;ll actually remember, and memes that hit a little too close.</p>'
    '<div style="margin-top:44px"><span class="pill on" style="font-size:20px;padding:14px 30px">Pinned &middot; start here</span></div></div>' + foot())
wc_cards = [("News, in points", "What moved, why, and what it meant for one contract. No hype, no guessing."),
            ("Explainers", "One idea per slide, built to save and come back to."),
            ("Memes with a rule inside", "A laugh first, then the rule that saves your account.")]
add("wcA_2", bg(132, "flat") + header_panel("What you&rsquo;ll find here", 'Your feed, <span class="glow">but useful</span>') +
    '<div class="pad" style="top:400px;display:flex;flex-direction:column;gap:18px">' +
    "".join(f'<div class="gp {"hot" if i == 0 else ""}" style="display:flex;gap:26px;align-items:center;padding:30px 32px"><div style="flex:none;width:72px;height:72px;border-radius:50%;border:2px solid #00FBF4;display:flex;align-items:center;justify-content:center;font-size:34px;box-shadow:0 0 22px rgba(0,251,244,.3)">{ic}</div><div><div style="font-size:34px;font-weight:700">{h}</div><div style="font-size:24px;color:#AFB8BC;margin-top:6px;line-height:1.4">{p}</div></div></div>'
            for i, ((h, p), ic) in enumerate(zip(wc_cards, ["&#128240;", "&#128161;", "&#128514;"]))) +
    '</div>' + foot())
add("wcA_3", bg(133, "up") + header_panel("What Halcyon is", 'A simulated evaluation, <span class="glow">with clear rules</span>', hot=True) +
    '<div class="pad" style="top:430px;display:grid;grid-template-columns:1fr 1fr;gap:16px">' +
    "".join(f'<div class="gp ctr" style="padding:30px 20px"><p class="lab">{k}</p><div class="num glow" style="font-size:58px;margin-top:8px">{v}</div></div>' for k, v in [("Account", "$50K"), ("Target", "$3,000"), ("Drawdown", "$2,000"), ("From", "$51")]) +
    '</div><div class="pad ctr" style="top:960px"><p class="body">Pass the evaluation in simulated trading and move up to a reward account. Every rule is on the site before you start.</p></div>'
    f'<p class="disc ctr" style="position:absolute;left:64px;right:64px;bottom:116px">{DISC}</p>' + foot())
add("wcA_4", bg(134, "flat") + header_panel("How to use this account", 'Three habits <span class="glow">worth keeping</span>') +
    checklist([("Explainers", "Save the ones you&rsquo;ll need again", OK, True), ("Sundays", "Check the week&rsquo;s release times", OK, False),
               ("Questions", "Ask us anything in our Discord", OK, False)], 400, h=128) +
    '<div class="pad" style="top:900px"><p class="body ctr">Tell us in the comments what you want explained next. We read every one.</p></div>' + foot())
follow("wcA_5", 'Glad you&rsquo;re <span class="glow">here</span>', "Follow for news days, explainers and the occasional meme you&rsquo;ll send to your trading friends.", 135)

# =====================================================================
# STORIES · INTERACTIVE (1080x1920, sticker added in the app)
# =====================================================================
def mock_sticker(st):
    kind, data = st
    card = 'background:#fff;color:#111;border-radius:28px;box-shadow:0 20px 60px rgba(0,0,0,.5);font-family:Poppins'
    if kind == "poll":
        inner = f'<div style="{card};width:620px;margin:0 auto;padding:30px 30px 34px">' + "".join(f'<div style="border:3px solid #e6e6e6;border-radius:40px;padding:22px;margin-top:{0 if i == 0 else 16}px;font-size:34px;font-weight:600;background:linear-gradient(90deg,#00FBF4,#5FA8FF);-webkit-background-clip:text;color:transparent">{o}</div>' for i, o in enumerate(data)) + '</div>'
    elif kind == "quiz":
        inner = f'<div style="{card};width:640px;margin:0 auto;padding:28px 30px 32px;text-align:left">' + "".join(f'<div style="display:flex;align-items:center;gap:18px;border:3px solid #e6e6e6;border-radius:40px;padding:16px 22px;margin-top:{0 if i == 0 else 14}px;font-size:30px;font-weight:600"><span style="width:40px;height:40px;border-radius:50%;border:3px solid #ccc;display:inline-flex;align-items:center;justify-content:center;font-size:20px;color:#999">{"ABC"[i]}</span>{o}</div>' for i, o in enumerate(data)) + '</div>'
    elif kind == "question":
        inner = f'<div style="width:640px;margin:0 auto;border-radius:28px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.5)"><div style="background:linear-gradient(90deg,#00C9C3,#3A8DFF);padding:26px;font-size:30px;font-weight:600;color:#fff">{data}</div><div style="background:#fff;padding:30px;font-size:28px;color:#9a9a9a">Type something...</div></div>'
    else:  # countdown
        inner = f'<div style="{card};width:600px;margin:0 auto;padding:28px;background:linear-gradient(135deg,#0A3E44,#04151A);color:#fff;border:2px solid rgba(255,255,255,.2)"><div style="font-size:30px;font-weight:600">{data}</div><div style="display:flex;justify-content:center;gap:16px;margin-top:18px">' + "".join(f'<div style="background:rgba(255,255,255,.12);border-radius:14px;padding:12px 18px;font-size:48px;font-weight:700">{x}</div>' for x in ["0", "2", ":", "1", "4"]) + '</div></div>'
    return (f'<div class="ctr" style="position:absolute;left:0;right:0;top:960px">{inner}'
            '<p style="font-size:20px;color:#7D878C;margin:22px 0 0;letter-spacing:.08em;text-transform:uppercase">Preview &middot; sticker added in the Instagram app</p></div>')

def sticker_story(name, kicker, q, sub, seed, kind="flat", accent=None, disc=False, st=None):
    """Clean story background with the question. The poll/quiz/question/countdown sticker is added natively in Instagram in the empty middle zone."""
    add(name, bg(seed, kind, story=True, glow=(50, 30)) +
        '<div style="position:absolute;left:64px;right:64px;top:300px;display:flex;justify-content:center">' + wordmark("margin:0") + '</div>'
        f'<div class="ctr" style="position:absolute;left:64px;right:64px;top:430px"><span class="pill">{kicker}</span>'
        f'<h1 class="hl" style="margin-top:34px;font-size:84px">{q}</h1>'
        + (f'<p class="body" style="margin-top:26px;font-size:32px">{sub}</p>' if sub else "") + '</div>'
        + (f'<div class="ctr" style="position:absolute;left:0;right:0;top:1520px"><div class="num glow" style="font-size:120px;line-height:1">{accent}</div></div>' if accent else "")
        + (f'<p class="disc ctr" style="position:absolute;left:90px;right:90px;bottom:300px;font-size:20px">{DISC}</p>' if disc else ""), story=True)
    if st:
        html_, _ = S[name]
        S[name + "p"] = (html_.replace('</div></body>', mock_sticker(st) + '</div></body>'), True)

sticker_story("stA", "Jobs report &middot; Fri 6 Nov", 'Trading the jobs report <span class="glow">or waiting it out?</span>', "8:30 AM ET", 141, st=("poll", ["Trading it", "Waiting it out"]))
sticker_story("stB", "This week &middot; Sun 8 Nov", 'CPI lands <span class="glow">Tuesday</span>', "Set a reminder so 8:30 doesn&rsquo;t sneak up on you.", 142, st=("countdown", "CPI &middot; Tue 8:30 AM ET"))
sticker_story("stC", "CPI day &middot; Tue 10 Nov", 'CPI in 30 minutes. <span class="glow">Hot or cool?</span>', "Vote before 8:30 AM ET.", 143, "spike", st=("poll", ["Hot", "Cool"]))
sticker_story("stD", "Quiz &middot; Wed 11 Nov", 'A stop order becomes a <span class="glow">___</span> when it&rsquo;s touched', "Answer, then check the post.", 144, st=("quiz", ["Market order", "Limit order", "Nothing"]))
sticker_story("stE", "Ask us &middot; Thu 12 Nov", 'Ask us anything about <span class="glow">the $50K evaluation</span>', "We&rsquo;ll answer the best ones on Friday.", 145, "up", disc=True, st=("question", "Ask us about the evaluation"))
sticker_story("stF", "Friday the 13th", 'What&rsquo;s your <span class="glow">trading superstition?</span>', "We promise not to judge. Much.", 146, "drop", st=("question", "My trading superstition is..."))

# =====================================================================
# PROFILE · HIGHLIGHT COVERS (1080x1920, icon centred for the circle crop)
# =====================================================================
ICONS = {
 "Rules": '<path d="M60 14l38 14v28c0 26-17 44-38 52-21-8-38-26-38-52V28z" fill="none" stroke="#00FBF4" stroke-width="7" stroke-linejoin="round"/><path d="M42 62l13 13 24-26" fill="none" stroke="#00FBF4" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>',
 "Dynamic": '<rect x="20" y="34" width="52" height="70" rx="9" fill="none" stroke="#00FBF4" stroke-width="6" transform="rotate(-12 46 69)"/><rect x="48" y="22" width="52" height="70" rx="9" fill="#03070A" stroke="#00FBF4" stroke-width="7" transform="rotate(10 74 57)"/><text x="75" y="66" fill="#00FBF4" font-family="Poppins" font-weight="700" font-size="26" text-anchor="middle" transform="rotate(10 74 57)">$</text>',
 "Explainers": '<circle cx="60" cy="52" r="26" fill="none" stroke="#00FBF4" stroke-width="7"/><path d="M48 84h24M51 98h18" stroke="#00FBF4" stroke-width="7" stroke-linecap="round"/><path d="M60 38v14l9 6" stroke="#00FBF4" stroke-width="6" stroke-linecap="round" fill="none"/>',
 "News": '<path d="M18 88l24-26 18 14 30-38" fill="none" stroke="#00FBF4" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M74 38h16v16" fill="none" stroke="#00FBF4" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 104h88" stroke="#00FBF4" stroke-width="5" stroke-linecap="round" opacity=".5"/>',
 "Memes": '<circle cx="60" cy="60" r="40" fill="none" stroke="#00FBF4" stroke-width="7"/><circle cx="46" cy="52" r="5" fill="#00FBF4"/><circle cx="74" cy="52" r="5" fill="#00FBF4"/><path d="M42 70c8 12 28 12 36 0" fill="none" stroke="#00FBF4" stroke-width="7" stroke-linecap="round"/>',
}
def hl_icon(k, size):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 120 120" style="filter:drop-shadow(0 0 14px rgba(0,251,244,.6))">{ICONS[k]}</svg>'
for i, k in enumerate(ICONS):
    add(f"hl{k}", '<div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,rgba(0,251,244,.22),transparent 38%),#03070A"></div>'
        '<div style="position:absolute;left:240px;top:660px;width:600px;height:600px;border-radius:50%;border:6px solid rgba(0,251,244,.55);box-shadow:0 0 60px rgba(0,251,244,.25),inset 0 0 60px rgba(0,251,244,.12);display:flex;align-items:center;justify-content:center">'
        + hl_icon(k, 330) + '</div>', story=True)
add("hlSheet", bg(150, "flat", glow=(50, 40)) + header_panel("Profile setup", 'Highlight <span class="glow">covers</span>') +
    '<div style="position:absolute;left:64px;right:64px;top:470px;display:flex;justify-content:space-between">' +
    "".join(f'<div class="ctr"><div style="width:168px;height:168px;border-radius:50%;background:radial-gradient(circle,rgba(0,251,244,.2),#03070A 70%);border:4px solid rgba(0,251,244,.6);box-shadow:0 0 30px rgba(0,251,244,.25);display:flex;align-items:center;justify-content:center">{hl_icon(k, 96)}</div><p style="font-size:22px;margin:16px 0 0;font-weight:500">{k}</p></div>' for k in ICONS) +
    '</div><div class="pad" style="top:800px"><p class="body ctr">Five covers for the profile highlights: rules, the Dynamic evaluation, explainers, news and memes. Each file is 1080 &times; 1920 with the icon centred for Instagram&rsquo;s circle crop.</p></div>' + foot(None))

# =====================================================================
# WELCOME · COVER + END OPTIONS
# =====================================================================
IMG = "file:///home/claude/halcyon/ig/img/"
def mini_icon(kind):
    return {"News": hl_icon("News", 120), "Explainers": hl_icon("Explainers", 120), "Memes": hl_icon("Memes", 120)}[kind]

# ---- Option 1 · The hand (fanned cards)
def hand(top, labels, spread=1.0):
    cards = [(-13, -250 * spread, 50), (0, 0, 0), (13, 250 * spread, 50)]
    out = [f'<div style="position:absolute;left:0;right:0;top:{top}px;height:520px">']
    for i, ((rot, dx, dy), (lab, sub)) in enumerate(zip(cards, labels)):
        out.append(f'<div class="gp {"hot" if i == 1 else ""} ctr" style="position:absolute;left:{540 - 155 + dx:.0f}px;top:{dy}px;width:310px;height:430px;transform:rotate({rot}deg);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;padding:24px">'
                   f'<div style="width:150px;height:150px;border-radius:50%;border:2px solid rgba(0,251,244,.35);display:flex;align-items:center;justify-content:center">{mini_icon(lab)}</div>'
                   f'<div style="font-size:34px;font-weight:700">{lab}</div><div style="font-size:19px;color:#AFB8BC;line-height:1.35">{sub}</div></div>')
    out.append('</div>')
    return "".join(out)
HAND = [("News", "What moved, in points"), ("Explainers", "One idea per slide"), ("Memes", "With a rule inside")]
add("wcB_1", bg(161, "up", glow=(50, 30)) +
    '<div class="pad ctr" style="top:90px"><span class="pill">New account &middot; start here</span></div>' + hand(200, HAND, spread=1.27) +
    '<div class="pad ctr" style="top:780px"><h1 class="hl xl">Welcome to <span class="glow">Halcyon</span></h1>'
    '<p class="body" style="margin-top:24px">Three kinds of posts, dealt fresh every week. Swipe to see what&rsquo;s in the deck.</p></div>' + foot())
add("wcB_5", bg(162, "up", glow=(50, 35)) +
    '<div style="position:absolute;left:0;right:0;top:150px;height:560px">' +
    "".join(f'<div class="gp" style="position:absolute;left:{325 + k * 22}px;top:{k * 22}px;width:430px;height:520px;opacity:{.35 + k * .2}"></div>' for k in range(2)) +
    '<div class="gp hot ctr" style="position:absolute;left:369px;top:44px;width:430px;height:520px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px">'
    '<div style="width:130px;height:130px;border-radius:50%;border:6px solid #00FBF4;position:relative;box-shadow:0 0 50px rgba(0,251,244,.55)"><div style="position:absolute;left:33px;top:33px;width:52px;height:52px;border-radius:50%;background:#00FBF4"></div></div>'
    '<div style="font-size:40px;font-weight:700">Halcyon</div><span class="pill on" style="font-size:22px;padding:14px 34px">Follow</span></div></div>'
    '<div class="pad ctr" style="top:790px"><h1 class="hl m">Keep the deck <span class="glow">close</span></h1>'
    '<p class="body" style="margin-top:20px">Follow for the next deal, and bring your questions to our Discord.</p>'
    '<div style="display:flex;justify-content:center;gap:14px;margin-top:34px"><span class="pill" style="font-size:20px;padding:13px 26px">Save</span><span class="pill" style="font-size:20px;padding:13px 26px">Discord in bio</span></div></div>' + foot(None))

# ---- Option 2 · Big glow wordmark + rising chart
add("wcC_1", bg(171, "up", glow=(50, 70)) + hero_chart(171, "up", top=690, h=560, n=34) +
    '<div class="pad ctr" style="top:150px"><p style="font-size:54px;font-weight:500;color:#AFB8BC;margin:0;letter-spacing:.02em">Welcome to</p>'
    '<div class="num glow" style="font-size:190px;line-height:1;letter-spacing:.06em;margin-top:6px">HALCYON</div>'
    '<p class="body" style="margin-top:30px">Futures news in plain English, explainers worth saving, and memes that hit a little too close.</p></div>' + foot())
week = [("Sun", "Week ahead"), ("8:30", "News days"), ("Wed", "Explainers"), ("Daily", "Stories and polls"), ("Fri", "Memes")]
add("wcC_5", bg(172, "flat", glow=(50, 30)) +
    '<div class="pad ctr" style="top:150px"><span class="pill">Your week with us</span><h1 class="hl xl" style="margin-top:26px">See you on the next <span class="glow">news day</span></h1></div>'
    '<div style="position:absolute;left:64px;right:64px;top:640px">'
    '<div style="position:absolute;left:90px;right:90px;top:43px;height:3px;background:linear-gradient(90deg,rgba(0,251,244,.2),#00FBF4,rgba(0,251,244,.2));box-shadow:0 0 18px rgba(0,251,244,.5)"></div>'
    '<div style="display:flex;justify-content:space-between;position:relative">' +
    "".join(f'<div class="ctr" style="width:180px"><div style="width:90px;height:90px;margin:0 auto;border-radius:50%;background:#03070A;border:3px solid {"#00FBF4" if i in (0, 2, 4) else "#2B3A41"};display:flex;align-items:center;justify-content:center;font-weight:700;font-size:{22 if len(d) > 3 else 24}px;{"box-shadow:0 0 26px rgba(0,251,244,.5);color:#00FBF4" if i in (0, 2, 4) else "color:#AFAFAF"}">{d}</div><div style="font-size:22px;margin-top:16px;font-weight:500">{t}</div></div>' for i, (d, t) in enumerate(week)) +
    '</div></div>'
    '<div class="pad ctr" style="top:930px"><p class="body">Follow so the next one finds you.</p>'
    '<div style="display:flex;justify-content:center;gap:14px;margin-top:30px"><span class="pill on" style="font-size:22px;padding:14px 34px">Follow</span><span class="pill" style="font-size:20px;padding:13px 26px">Save</span><span class="pill" style="font-size:20px;padding:13px 26px">Discord in bio</span></div></div>' + foot(None))

# ---- Option 3 · Profile preview + notifications
grid_imgs = ["mmA_1", "etA_1", "wkA_1", "mmB_1", "etB_1", "dyA_1"]
add("wcD_1", bg(181, "flat", glow=(50, 20)) +
    '<div class="pad ctr" style="top:80px"><h1 class="hl" style="font-size:76px">You found <span class="glow">Halcyon</span></h1></div>'
    '<div class="gp hot" style="position:absolute;left:150px;right:150px;top:240px;height:960px;padding:30px 30px 0;overflow:hidden;border-radius:46px">'
    '<div style="display:flex;align-items:center;gap:24px"><div style="flex:none;width:120px;height:120px;border-radius:50%;padding:5px;background:conic-gradient(#00FBF4,#0A5C5E,#00FBF4)"><div style="width:100%;height:100%;border-radius:50%;background:#03070A;display:flex;align-items:center;justify-content:center"><div style="width:62px;height:62px;border-radius:50%;border:5px solid #00FBF4;position:relative"><div style="position:absolute;left:13px;top:13px;width:26px;height:26px;border-radius:50%;background:#00FBF4"></div></div></div></div>'
    '<div><div style="font-size:30px;font-weight:700">Halcyon Trader Funding</div><div style="font-size:19px;color:#AFB8BC;margin-top:6px;line-height:1.4">Futures news in plain English, and the rules that keep accounts alive.</div></div></div>'
    '<div style="display:flex;justify-content:space-between;margin:28px 6px 0">' +
    "".join(f'<div class="ctr"><div style="width:96px;height:96px;border-radius:50%;border:3px solid rgba(0,251,244,.55);display:flex;align-items:center;justify-content:center;background:radial-gradient(circle,rgba(0,251,244,.15),#03070A 70%)">{hl_icon(k, 54)}</div><div style="font-size:15px;margin-top:8px">{k}</div></div>' for k in ICONS) +
    '</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin:28px -30px 0">' +
    "".join(f'<img src="{IMG}{g}.png" style="width:100%;aspect-ratio:4/5;object-fit:cover;display:block">' for g in grid_imgs) +
    '</div></div>' + foot())
notes = [("Story", "CPI in 30 minutes. Hot or cool? Vote before 8:30.", "now"), ("New post", "CPI day: every market&rsquo;s mood", "2h"), ("New post", "Market, limit or stop? Explained in five slides.", "1d")]
add("wcD_5", bg(182, "flat", glow=(50, 25)) +
    '<div class="pad ctr" style="top:120px"><h1 class="hl xl">Let news days <span class="glow">come to you</span></h1></div>'
    '<div class="pad" style="top:520px;display:flex;flex-direction:column;gap:16px">' +
    "".join(f'<div class="gp {"hot" if i == 0 else ""}" style="display:flex;align-items:center;gap:22px;padding:24px 28px;border-radius:26px;margin:0 {i * 26}px;opacity:{1 - i * .18}"><div style="flex:none;width:64px;height:64px;border-radius:16px;background:#03070A;border:2px solid rgba(0,251,244,.5);display:flex;align-items:center;justify-content:center"><div style="width:30px;height:30px;border-radius:50%;border:4px solid #00FBF4;position:relative"><div style="position:absolute;left:5px;top:5px;width:12px;height:12px;border-radius:50%;background:#00FBF4"></div></div></div>'
            f'<div style="flex:1"><div style="display:flex;justify-content:space-between"><span style="font-size:21px;font-weight:700">Halcyon &middot; {k}</span><span style="font-size:18px;color:#7D878C">{t}</span></div><div style="font-size:23px;color:#C9D1D4;margin-top:4px">{m}</div></div></div>' for i, (k, m, t) in enumerate(notes)) +
    '</div><div class="pad ctr" style="top:1010px"><p class="body">Follow, then turn on notifications for posts and Stories.</p>'
    '<div style="display:flex;justify-content:center;gap:14px;margin-top:26px"><span class="pill on" style="font-size:22px;padding:14px 34px">Follow</span><span class="pill" style="font-size:20px;padding:13px 26px">&#128276; Notifications</span></div></div>' + foot(None))
