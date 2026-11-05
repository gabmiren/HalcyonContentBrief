import json, re, os, shutil
D = os.path.dirname(os.path.abspath(__file__))
OUT = f"{D}/site"
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(f"{OUT}/img")
for f in os.listdir(f"{D}/img"): shutil.copy(f"{D}/img/{f}", f"{OUT}/img/{f}")

DISC = "Halcyon offers simulated educational accounts. Results not guaranteed. T&C apply."
def C(head, body, cta, tags, disc=False):
    """Caption in the TikTok house style: header with emoji, short lines, question, 👉 CTA with link in bio, disclaimer when rules or promo are mentioned."""
    out = head + "\n" + body + "\n\n" + cta + "\n\n"
    out += (DISC + "\n" + tags) if disc else tags
    return out

def fr(prefix, caps): return [{"src": f"img/{prefix}_{i}.png", "cap": c} for i, c in enumerate(caps, 1)]
def one(name, cap): return [{"src": f"img/{name}.png", "cap": cap}]
def L(*pairs): return [{"label": a, "url": b} for a, b in pairs]

SRC_DAY = (("TheStreet, close 4 Nov", "https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-nov-04-2026"),
           ("CNN, best post-midterm day since 1982", "https://www.cnn.com/2026/11/04/investing/us-markets-midterm-elections"),
           ("Finwire, oil, gold and yields", "https://finwire.io/news/forex-news/financial-forex-market-recap-nov-4-2026"))
SITE = ("Halcyon site (rules, fees)", "https://www.halcyontraderfunding.com")

posts = [
 # ------------------------------------------------------------- NEWS
 {"id": "nb", "title": "News brief", "short": "News brief", "when": "News · Carousel",
  "brief": {"job": "The big market story in plain English within 24 hours, told in points and finished with the Halcyon angle: how much of a $2,000 drawdown the move would use on one ES and one MES.",
            "topics": "Big market days · Monthly recaps · Fed, CPI and jobs days · Big tech earnings",
            "fixed": "TikTok glow-panel look: blurred candle backdrop, glowing hero chart on the cover, glass stat panels, header panels, round bars. Moves shown in points or percent, never as dollar wins. The drawdown meter slide is the signature. Ends on a Follow, Save, Discord slide.",
            "cadence": "Within 24 hours of major news"},
  "versions": [
   {"name": "Best post-midterm day since 1982 (4 Nov)",
    "caption": C("The Dow just had its best post-midterm day since 1982 📈",
                 "Up 3.03% on Wednesday, while oil slid about 8.5%.\nThe S&P 500 moved 119.7 points. On one ES that's three times a whole $2,000 drawdown. On one MES it's under a third.\nSame chart, very different evenings, depending on your size.\nWere you in it or watching?",
                 "👉 Talk through your Wednesday in our Discord: link in bio", "#futurestrading #daytrading #stockmarket #ES", disc=True),
    "frames": fr("nbA", ["Cover", "Movers", "Why", "In points", "Drawdown meter", "Follow"]), "links": L(*SRC_DAY)},
   {"name": "October recap",
    "caption": C("October was a rough month inside a good year 📉",
                 "The S&P 500 fell 2.11% and the Nasdaq 6.03% as AI spending doubts hit tech. Both are still up more than 9% this year.\nThe S&P drifted about 163 points over the month. That's four times the room a $2,000 drawdown gives one ES.\nHow did October treat you?",
                 "👉 Share your October in our Discord: link in bio", "#futurestrading #marketrecap #daytrading", disc=True),
    "frames": fr("nbB", ["Cover", "Month vs year", "Why", "Drawdown meter", "Follow"]),
    "links": L(("Tapeboard, October 2026 recap", "https://tapeboard.com/blog/monthly-recap-2026-10"))},
  ]},
 {"id": "gc", "title": "Group chat", "short": "Group chat", "when": "News · Carousel · New",
  "brief": {"job": "The day's news told as a traders' group chat, then a fact-check slide with the real numbers. The fun way into a news day, for people who scroll past charts.",
            "topics": "Wild market days · Surprise data · Holiday sessions · Anything the timeline is yelling about",
            "fixed": "Glass phone-style chat panel with cyan bubbles for 'me'. Two chat slides, then a fact-checked checklist with sources. Invented first names only, never real people.",
            "cadence": "On big news days, 1 to 2 a week"},
  "versions": [
   {"name": "Oil day in the group chat (4 Nov)",
    "caption": C("The group chat on Wednesday 💀",
                 "Oil fell about 8.5%, gold went back above $4,000 and the Dow ripped 1,569 points.\nSomewhere, a CL long is being held for the weekend.\nWhat did your chat look like?",
                 "👉 Bring the screenshots to our Discord: link in bio", "#tradinghumor #futurestrading #crudeoil #daytrading"),
    "frames": fr("gcA", ["Chat 1", "Chat 2", "Fact-check"]), "links": L(*SRC_DAY)},
  ]},
 {"id": "na", "title": "News alert", "short": "News alert", "when": "News · Single",
  "brief": {"job": "One fast graphic for a big move, posted the same day. A little personality in the headline, the facts straight underneath.",
            "topics": "Oil, gold and index moves · Record days · Surprise data",
            "fixed": "Glowing glass panel with a before and after bar pair, or one giant glowing number. Red news pill, two-line headline with a glowing half, source line.",
            "cadence": "Same day as the move"},
  "versions": [
   {"name": "Oil had a rough Wednesday", "caption": C("Oil had a rough Wednesday 🛢️", "WTI slid about 8.5% in one session, to near $89, as war-risk talk cooled after the election.\nCrude traders, how are we holding up?", "👉 Swap oil stories in our Discord: link in bio", "#crudeoil #futurestrading #marketnews"),
    "frames": one("naA", "Oil"), "links": L(SRC_DAY[2])},
   {"name": "Gold back above $4,000", "caption": C("Gold is back above $4,000 🟡", "Up about 3.3% on Wednesday as the dollar and bond yields slipped.\nBull or bear from here?", "👉 Make your call in our Discord: link in bio", "#gold #futurestrading #marketnews"),
    "frames": one("naB", "Gold"), "links": L(SRC_DAY[2])},
   {"name": "Dow +1,569", "caption": C("+1,569 points in one day 📈", "The Dow's best day since April 2025, and its biggest post-midterm gain since 1982.\nWhere were you when it ripped?", "👉 Tell us in our Discord: link in bio", "#dowjones #stockmarket #futurestrading"),
    "frames": one("naC", "Dow"), "links": L(SRC_DAY[1])},
  ]},
 {"id": "md", "title": "Market mood", "short": "Market mood", "when": "News · Single · New",
  "brief": {"job": "A playful scoreboard: every big market gets a mood for the day, plus its real move. Replaces 18th Street's per-contract dollar scoreboard.",
            "topics": "Big days · Friday weekly wrap · Month end",
            "fixed": "Stacked glass rows, a mood pill for each market (cyan, red or grey), the move glowing on the right. The day's winner gets the glowing panel.",
            "cadence": "After big days, or Fridays"},
  "versions": [
   {"name": "How every market's Wednesday went", "caption": C("How every market's Wednesday went 😮‍💨", "The Dow had its best day since April 2025. Oil was down bad. The VIX took the day off.\nWhich one matched your mood?", "👉 Drop your mood in our Discord: link in bio", "#futurestrading #tradinghumor #stockmarket"),
    "frames": one("mdA", "Mood board"), "links": L(*SRC_DAY)},
  ]},
 {"id": "wk", "title": "This week", "short": "This week", "when": "News · Carousel",
  "brief": {"job": "Every Sunday, the week's market-moving events with Eastern times, and the Halcyon rule that applies to each one.",
            "topics": "CPI, PPI, jobs, Fed days · Holidays and early closes · Big earnings",
            "fixed": "Glowing day-card row on the cover. One slide per event: glowing date tile, What it is and Why traders care panels, a red Halcyon rule panel where one applies, and the time huge at the bottom. Ends on a save-this-week checklist.",
            "cadence": "Every Sunday"},
  "versions": [
   {"name": "Inflation week (9 to 13 Nov)",
    "caption": C("Inflation week is here 🗓️",
                 "CPI lands Tuesday at 8:30 AM ET and PPI follows on Friday, with a bond holiday in between.\nPlan your trade before 8:30, or give yourself permission to sit it out.\nSave this so Tuesday doesn't sneak up on you.",
                 "👉 Plan the week with us in our Discord: link in bio", "#futurestrading #CPI #economiccalendar #daytrading", disc=True),
    "frames": fr("wkA", ["Cover", "CPI", "Veterans Day", "PPI", "Save this week"]),
    "links": L(("Release calendar (CPI, PPI)", "https://fedratecalc.com/us-economic-calendar/november-2026/"), ("Schwab week ahead", "https://www.schwab.com/learn/story/stock-market-update-open"))},
   {"name": "Thanksgiving week (23 to 27 Nov)",
    "caption": C("Short week, busy Wednesday 🦃",
                 "GDP and PCE drop at the same second on Wednesday, then Thanksgiving cuts two sessions short.\nHoliday markets are thin, so small orders can move price more than you'd expect.\nSave this for the week.",
                 "👉 Check holiday hours with us in our Discord: link in bio", "#futurestrading #thanksgiving #tradinghours", disc=True),
    "frames": fr("wkB", ["Cover", "GDP + PCE", "Thanksgiving", "Day after", "Save this week"]),
    "links": L(("CME holiday calendar", "https://www.cmegroup.com/tools-information/holiday-calendar.html"), ("QuantVPS, CME holiday hours 2026", "https://www.quantvps.com/blog/cme-holiday-schedule"))},
  ]},
 # ------------------------------------------------------------- EXPLAINERS
 {"id": "et", "title": "Every trader should know", "short": "Explainers", "when": "Explainer · Carousel",
  "brief": {"job": "One idea a futures trader needs, one step per slide, with a real example from this week's market. Same question-hook, one-idea-per-slide rhythm as the TikTok trailing drawdown carousel.",
            "topics": "Drawdown in points · Order types · Contract sizing · Reading a release",
            "fixed": "Question hook on the cover, header panels marked Step 1, 2, 3, glass tables and price ladders, the drawdown meter for real examples. Ends on Follow, Save, Discord.",
            "cadence": "Weekly"},
  "versions": [
   {"name": "How many points is your drawdown?",
    "caption": C("How many points is your drawdown? 📏",
                 "On one ES, $2,000 is 40 points. On one MES it's 400.\nWednesday the S&P moved 119.7 points, so the contract you pick decides whether that's a normal day or the end of the account.\nSave this before you size your next trade.",
                 "👉 Questions on sizing? Ask in our Discord: link in bio", "#futurestrading #ES #riskmanagement #propfirm", disc=True),
    "frames": fr("etA", ["Cover", "Point values", "Room in points", "Real example", "Micros", "Follow"]),
    "links": L(("CME E-mini S&P 500 specs", "https://www.cmegroup.com/markets/equities/sp/e-mini-sandp500.contractSpecs.html"), SITE)},
   {"name": "Market, limit or stop?",
    "caption": C("Market, limit or stop? 🎯",
                 "A market order fills now. A limit waits for your price. A stop turns into a market order the moment it's touched, which is why it can fill past your level on CPI mornings.\nWhich one surprised you the first time?",
                 "👉 Ask us anything about orders in our Discord: link in bio", "#futurestrading #tradingeducation #daytrading", disc=True),
    "frames": fr("etB", ["Cover", "Market", "Limit", "Stop", "Follow"]), "links": L(SITE)},
  ]},
 {"id": "mm", "title": "Meme explainer", "short": "Meme explainer", "when": "Explainer · Carousel",
  "brief": {"job": "A joke traders recognise, with the rule underneath. The IG cousin of the TikTok 4:44 PM and CPI memes, so the same jokes reinforce each other across both accounts.",
            "topics": "Rules that end accounts · Myths about evaluations · Trader habits",
            "fixed": "Meme panel in glass on top, a red rule panel with a warning icon below. Built from type, chat bubbles and order tickets, so nothing needs a licensed meme. Myth or fact uses a quote panel and a tilted MYTH or FACT stamp.",
            "cadence": "Weekly"},
  "versions": [
   {"name": "4 ways to fail without a losing trade",
    "caption": C("Your strategy can be fine and the account can still end 😅",
                 "Holding at 4:45 PM ET, skipping the stop, straddling the CPI print or hedging across accounts. All four break the rules, win or lose.\nWhich one have you seen someone try?",
                 "👉 More rules, explained simply, in our Discord: link in bio", "#tradinghumor #propfirm #futurestrading #daytrading", disc=True),
    "frames": fr("mmA", ["Cover", "The clock", "The stop", "The cheat code", "The big brain", "Takeaway"]), "links": L(SITE)},
   {"name": "Myth or fact: evaluation edition",
    "caption": C("Myth or fact, evaluation edition 🤔",
                 "Five things traders get wrong about the $50K evaluation, from the 1-day minimum to how 25 micros really compare to 5 minis.\nPlay along and drop your score in the comments.",
                 "👉 Check every rule with us in our Discord: link in bio", "#propfirm #futurestrading #mythorfact", disc=True),
    "frames": fr("mmB", ["Cover", "01", "02", "03", "04", "05", "Score"]), "links": L(SITE)},
  ]},
 {"id": "kh", "title": "Know your hours", "short": "Know your hours", "when": "Explainer · Single",
  "brief": {"job": "A save-worthy timetable: when the market opens, breaks and closes, and when Halcyon needs you flat.",
            "topics": "A trading day · Holiday hours",
            "fixed": "Header panel and one glass checklist, the key row glowing. Cyan check, grey cross or red warning icons. All times Eastern.",
            "cadence": "Monthly, plus before holidays"},
  "versions": [
   {"name": "A Halcyon trading day", "caption": C("Save this one ⏰", "The week opens Sunday at 6:00 PM ET and futures trade almost 24 hours from there.\n4:45 PM ET is the one that catches people. Set an alarm and let that last minute be boring.", "👉 More rules, explained simply, in our Discord: link in bio", "#futurestrading #tradinghours #daytrading", disc=True),
    "frames": one("khA", "Trading day"), "links": L(("CME trading hours", "https://www.cmegroup.com/trading-hours.html"), SITE)},
   {"name": "Thanksgiving hours", "caption": C("Thanksgiving hours for ES and NQ 🦃", "Thursday halts at 1:00 PM ET and reopens at 6:00 PM ET. Friday closes early at 1:15 PM ET.\nThin markets, early exits. Plan around them.", "👉 Holiday questions? Ask in our Discord: link in bio", "#futurestrading #thanksgiving #tradinghours"),
    "frames": one("khC", "Thanksgiving"), "links": L(("CME holiday calendar", "https://www.cmegroup.com/tools-information/holiday-calendar.html"))},
  ]},
 # ------------------------------------------------------------- PROMO
 {"id": "dy", "title": "Halcyon Dynamic in four cards", "short": "Dynamic cards", "when": "Promo · Carousel · New",
  "brief": {"job": "The main promo carousel, built from the same four numbers as the TikTok 'Four numbers' explainer and the Option D promo, so the offer looks the same everywhere.",
            "topics": "Halcyon Dynamic · Later: reward account sizes, platform picks",
            "fixed": "Fanned glass cards on the cover, then one glowing number per slide with a 1/4 pill, the Trailing / End of day toggle and page dots. A good-to-know slide, then the Start from $51 end card.",
            "cadence": "Every 2 weeks, plus launches"},
  "versions": [
   {"name": "Your $50K evaluation in four cards",
    "caption": C("Your $50K evaluation in four cards 🃏",
                 "A $3,000 target, a $2,000 drawdown, up to 5 minis or 25 micros, and flat by 4:45 PM ET.\nPick Trailing for $51 or end of day for $53. Every rule is on our site before you start, so day one feels calm.",
                 "👉 Start your evaluation: link in bio", "#propfirm #futurestrading #daytrading #NQ", disc=True),
    "frames": fr("dyA", ["Cover", "Target", "Drawdown", "Contracts", "Session close", "Good to know", "Start"]), "links": L(SITE)},
  ]},
 {"id": "wh", "title": "Why Halcyon", "short": "Why Halcyon", "when": "Promo · Single",
  "brief": {"job": "Answer one buyer question in four points, using only facts from the Halcyon site.",
            "topics": "Why Halcyon · Who it's for · Platforms",
            "fixed": "Huge headline with a glowing half, four glass step cards with numbered circles. Disclaimer on every graphic.",
            "cadence": "Every 2 weeks, alternating with the four cards"},
  "versions": [
   {"name": "Why Halcyon?", "caption": C("Why Halcyon? 💡", "One fee from $51, a 1-day minimum, and your pick of Trailing or end-of-day drawdown.\nReward accounts have no daily loss limit, so the drawdown is the line that matters.", "👉 See every rule: link in bio", "#propfirm #futurestrading #daytrading", disc=True),
    "frames": one("whA", "Why Halcyon"), "links": L(SITE)},
   {"name": "Who is it for?", "caption": C("Who is Halcyon for? 🎯", "Futures traders with a plan, on whatever schedule and platform suits them.\nAnd people who like reading the rules before they pay. Sound like you?", "👉 Start from $51: link in bio", "#propfirm #futurestrading #daytrader", disc=True),
    "frames": one("whB", "Who it's for"), "links": L(SITE)},
   {"name": "Platforms", "caption": C("Trade on what you already know 🖥️", "Volumetrica, TradingView, Quantower or DeepCharts.\nLearning the rules is enough. No new screen to learn on top.\nWhich one do you use?", "👉 Tell us your setup in our Discord: link in bio", "#tradingview #volumetrica #futurestrading", disc=True),
    "frames": one("whC", "Platforms"), "links": L(SITE)},
  ]},
 # ------------------------------------------------------------- STORIES
 {"id": "bn", "title": "One big number", "short": "Big number", "when": "Stories",
  "brief": {"job": "Send story viewers to the feed post with one huge glowing number and a tappable post card.",
            "topics": "The day's big move · A rule · A product number",
            "fixed": "9:16 with the IG top and bottom bars kept clear. Glowing number with a unit, one line, the feed cover in a white post frame inside a glowing panel, and a Tap to read pill. Add the link sticker over the panel.",
            "cadence": "With each feed post"},
  "versions": [
   {"name": "+3.03%", "caption": "Story. Link sticker to the News brief.", "frames": one("bnA", "Story"), "links": []},
   {"name": "4:45 PM ET", "caption": "Story. Link sticker to Know your hours.", "frames": one("bnB", "Story"), "links": []},
   {"name": "40 pts", "caption": "Story. Link sticker to How many points is your drawdown?", "frames": one("bnC", "Story"), "links": []},
  ]},
]

# ---- checks on every caption
bad = []
for p in posts:
    for v in p["versions"]:
        c = v["caption"]
        if "—" in c: bad.append((v["name"], "em dash"))
        emo = re.findall(r"[\U0001F300-\U0001FAFF☀-➿]", c)
        if len(emo) > 2: bad.append((v["name"], f"{len(emo)} emojis"))
        if re.search(r"\bnot [^.,]+ but\b", c, re.I): bad.append((v["name"], "not X but Y"))
        if re.search(r"\$\d[\d,]* (?:profit|made|gain)", c, re.I): bad.append((v["name"], "dollar result"))
        if "Arena" in c: bad.append((v["name"], "Arena"))
        for f in v["frames"]: assert os.path.exists(f"{D}/{f['src']}"), f["src"]
print("caption issues:", bad)
used = {f["src"].split("/")[1] for p in posts for v in p["versions"] for f in v["frames"]}
print("unused images:", sorted(set(os.listdir(f"{D}/img")) - used))
open(f"{OUT}/data.js", "w").write("window.D=" + json.dumps({"posts": posts}, ensure_ascii=False) + ";")

h = open("/home/claude/gabmiren/18thstreet/index.html").read()
h = h.replace("family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono", "family=Poppins:wght@400;500;600;700")
h = h.replace('--display:Archivo,"Helvetica Neue",Arial,sans-serif;--serif:Archivo,"Helvetica Neue",Arial,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace',
              '--display:Poppins,"Helvetica Neue",Arial,sans-serif;--serif:Poppins,"Helvetica Neue",Arial,sans-serif;--mono:Poppins,"Helvetica Neue",Arial,sans-serif')
dark = "--bg:#03070A;--surface:#0B1417;--line:#17262A;--ink:#FFFFFF;--ink2:#C9D1D4;--ink3:#9AA3A8;--accent:#00FBF4;--chip:#081013;color-scheme:dark"
h = re.sub(r":root\{--bg:#F5F6F6;[^}]*?--chip:#FFFFFF;", ":root{" + dark.replace(";color-scheme:dark", "") + ";", h, count=1)
h = h.replace(":root{color-scheme:light;", ":root{color-scheme:dark;")
h = h.replace("--bg:#16191C;--surface:#1C2023;--line:#2C3136;--ink:#E4E6E6;--ink2:#9BA1A6;--ink3:#6E767C;--accent:#7FA0A3;--chip:#1F2428;color-scheme:dark", dark)
# softer, rounder chrome to match the glow-panel slides
h = h.replace("</style>\n\n<div class=\"wrap\">", "#tabs button,nav button,.pick,.meta div,.tray,.ref,.vid,#vbar button{border-radius:14px}figure button{border-radius:12px;overflow:hidden}.meta div{border:1px solid var(--line)}\n</style>\n\n<div class=\"wrap\">", 1)
h = h.replace("18th Street Trading · internal", "Halcyon Trader Funding · new Instagram account · Miren Partners").replace(".wrap{max-width:1500px;", ".wrap{max-width:1180px;").replace("padding-left:max(16px,", "padding-left:max(20px,").replace("padding-right:max(16px,", "padding-right:max(20px,").replace("<title>Design Drafts</title>", "<title>Halcyon Instagram design drafts</title>")
h = h.replace("<h1>Design drafts</h1>", "<h1>Instagram drafts</h1>\n  <p class=\"lede\">Same look and voice as the TikTok: glow panels, Poppins, cyan, short warm captions and a Discord CTA. News is told five ways, explainers teach one idea per slide, and promos reuse the TikTok's four numbers. Moves are shown in points, never as dollar wins.</p>")
h = h.replace("'picks7'", "'hal_ig_picks2'").replace("'post4'", "'hal_ig_post2'")
h = h.replace('<p class="insp">Inspiration: ', '<p class="insp">Sources: ').replace("for 18th Street", "for Halcyon")
open(f"{OUT}/index.html", "w").write(h)
print(len(posts), "posts;", sum(len(v["frames"]) for p in posts for v in p["versions"]), "frames")
