"""Halcyon IG slide kit v2: TikTok glow-panel system (glass panels, pills, glow numbers, blurred candles)."""
import random, math, html

CY = "#00FBF4"; GR = "#AFAFAF"; DN = "#FF6B78"

CSS = """
*{box-sizing:border-box}html,body{margin:0;background:#03070A}
body{font-family:Poppins,sans-serif;color:#fff;-webkit-font-smoothing:antialiased}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;background:#03070A}
.s.st{height:1920px}
.pad{position:absolute;left:64px;right:64px}
.hl{font-weight:700;font-size:68px;line-height:1.08;letter-spacing:-.025em;margin:0;text-wrap:balance}
.hl.m{font-size:58px}.hl.s2{font-size:50px}.hl.xl{font-size:94px;line-height:1.02}
.ctr{text-align:center}
.a{color:#00FBF4}.g{color:#AFAFAF}.dn{color:#FF6B78}
.glow{color:#00FBF4;text-shadow:0 0 30px rgba(0,251,244,.55)}
.glowr{color:#FF6B78;text-shadow:0 0 30px rgba(255,107,120,.45)}
.lab{font-weight:500;font-size:16px;letter-spacing:.2em;text-transform:uppercase;color:#9AA3A8;margin:0}
.body{font-size:27px;line-height:1.45;color:#C9D1D4;margin:0;text-wrap:pretty}
.body b{color:#fff;font-weight:500}
.gp{border-radius:30px;background:linear-gradient(180deg,rgba(22,48,52,.66),rgba(6,14,17,.70));border:1.5px solid rgba(0,251,244,.15);box-shadow:inset 0 1px 0 rgba(255,255,255,.07),0 24px 60px rgba(0,0,0,.5);padding:28px 32px}
.gp.hot{border-color:rgba(0,251,244,.55);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 0 0 1px rgba(0,251,244,.08),0 0 60px rgba(0,251,244,.18),0 24px 60px rgba(0,0,0,.5)}
.gp.red{border-color:rgba(255,107,120,.45);box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 0 50px rgba(255,107,120,.12),0 24px 60px rgba(0,0,0,.5)}
.pill{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:9px 20px;font-weight:500;font-size:16px;letter-spacing:.14em;text-transform:uppercase;border:1.5px solid rgba(0,251,244,.35);color:#00FBF4;background:rgba(0,251,244,.07)}
.pill.on{background:linear-gradient(180deg,#7CFFFA,#00D8D2);color:#022C2B;border-color:transparent;box-shadow:0 0 26px rgba(0,251,244,.5)}
.pill.r{border-color:rgba(255,107,120,.5);color:#FF6B78;background:rgba(255,107,120,.08)}
.pill.gr{border-color:#2B363B;color:#AFAFAF;background:rgba(255,255,255,.03)}
.tog{display:inline-flex;border-radius:999px;background:rgba(0,0,0,.35);border:1.5px solid rgba(255,255,255,.07);padding:6px}
.tog span{padding:14px 34px;border-radius:999px;font-weight:500;font-size:24px;color:#AFAFAF}
.tog span.on{background:linear-gradient(180deg,#7CFFFA,#00D8D2);color:#022C2B;box-shadow:0 0 26px rgba(0,251,244,.5)}
.foot{position:absolute;left:64px;right:64px;bottom:48px;display:flex;justify-content:space-between;align-items:center}
.swipe{font-size:20px;color:#AFAFAF;font-weight:500}
.wm{display:flex;align-items:center;gap:12px;margin-left:auto}
.wm .mk{width:30px;height:30px;border-radius:50%;border:3px solid #00FBF4;position:relative;box-shadow:0 0 18px rgba(0,251,244,.4)}
.wm .mk:after{content:"";position:absolute;left:7px;top:7px;width:10px;height:10px;border-radius:50%;background:#00FBF4}
.wm b{display:block;font-weight:700;letter-spacing:.34em;font-size:17px;line-height:1}
.wm small{display:block;font-size:9px;letter-spacing:.46em;color:#AFAFAF;margin-top:5px}
.src{position:absolute;left:64px;right:64px;bottom:108px;font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:#68737A;margin:0}
.num{font-weight:700;letter-spacing:-.02em}
.disc{font-size:15px;line-height:1.5;color:#7D878C;margin:0}
.ic{flex:none;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ic.ok{background:#00FBF4;box-shadow:0 0 18px rgba(0,251,244,.55)}
.ic.no{border:2px solid #3A464C}
.ic.wn{background:#FF6B78;box-shadow:0 0 18px rgba(255,107,120,.45)}
.bubble{max-width:720px;padding:24px 32px;font-size:35px;line-height:1.35}
.bubble.l{align-self:flex-start;background:rgba(40,54,60,.85);border-radius:34px 34px 34px 10px}
.bubble.r{align-self:flex-end;background:linear-gradient(180deg,#5FFFF9,#00CFC9);color:#032321;border-radius:34px 34px 10px 34px;font-weight:500}
.who{font-size:20px;color:#7D878C;letter-spacing:.06em;margin:0 0 -14px 12px}
"""

E = html.escape

def wordmark(st=""):
    return f'<div class="wm" style="{st}"><div class="mk"></div><div><b>HALCYON</b><small>TRADER FUNDING</small></div></div>'

def foot(left="Swipe &rarr;"):
    l = f'<span class="swipe">{left}</span>' if left else '<span></span>'
    return f'<div class="foot">{l}{wordmark()}</div>'

def src(t, bottom=108):
    return f'<p class="src" style="bottom:{bottom}px">{t}</p>'

def page(inner, story=False):
    return f'<!doctype html><html><head><meta charset=utf8><style>{CSS}</style></head><body><div class="s{" st" if story else ""}">{inner}</div></body></html>'

OK = '<div class="ic ok"><svg width="22" height="22" viewBox="0 0 22 22"><path d="M5 11.5l4 4 8-9" stroke="#022C2B" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
NO = '<div class="ic no"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M4 4l10 10M14 4L4 14" stroke="#6E7A80" stroke-width="2.4" stroke-linecap="round"/></svg></div>'
WN = '<div class="ic wn"><svg width="22" height="22" viewBox="0 0 22 22"><path d="M11 5v8" stroke="#2A0508" stroke-width="3.2" stroke-linecap="round"/><circle cx="11" cy="17" r="1.9" fill="#2A0508"/></svg></div>'

# ---------- backgrounds ----------
def candles_svg(r, w, h, kind, n=26, base=None, col_up="#00FBF4", col_dn="#24484C"):
    out = []; cw = w / n
    p = base if base is not None else h * (0.7 if kind in ("up", "spike") else 0.35)
    for i in range(n):
        t = i / (n - 1)
        drift = {"up": -h * .018, "down": h * .016, "flat": 0,
                 "spike": -h * (0.003 if t < .7 else .06), "drop": h * (0.003 if t < .7 else .06),
                 "vshape": h * (0.03 if t < .5 else -0.034)}.get(kind, 0)
        o = p; c = p + drift + r.uniform(-h * .035, h * .035)
        hi = min(o, c) - r.uniform(6, h * .05); lo = max(o, c) + r.uniform(6, h * .05)
        up = c < o; x = i * cw + cw / 2
        col = col_up if up else col_dn
        out.append(f'<line x1="{x:.0f}" y1="{hi:.0f}" x2="{x:.0f}" y2="{lo:.0f}" stroke="{col}" stroke-width="3"/>'
                   f'<rect x="{x - cw * .32:.0f}" y="{min(o, c):.0f}" width="{cw * .64:.0f}" height="{max(abs(c - o), 4):.0f}" rx="4" fill="{col}"/>')
        p = c
    return "".join(out)

def bg(seed=1, kind="flat", story=False, glow=(78, 22), blur=7, op=.30):
    """Full-bleed blurred candle field with teal glows, like the TikTok motion backgrounds."""
    r = random.Random(seed); w, h = 1080, (1920 if story else 1350)
    gx, gy = glow
    return (f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at {gx}% {gy}%,rgba(0,251,244,.20),transparent 55%),radial-gradient(ellipse at 10% 95%,rgba(0,140,150,.16),transparent 50%),#03070A"></div>'
            f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;filter:blur({blur}px);opacity:{op}">{candles_svg(r, w, h, kind)}</svg>'
            f'<div style="position:absolute;inset:0;background:linear-gradient(rgba(3,7,10,.15),rgba(3,7,10,.55) 70%,rgba(3,7,10,.85))"></div>')

def hero_chart(seed, kind, top=120, h=520, n=30, op=1):
    """A crisp glowing candle chart inside a glass panel, for covers."""
    r = random.Random(seed); w = 952
    return (f'<div class="gp hot" style="position:absolute;left:64px;right:64px;top:{top}px;height:{h}px;padding:0;overflow:hidden">'
            f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;opacity:{op}">' +
            "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="rgba(0,251,244,.07)" stroke-width="1.5"/>' for y in range(60, h, 80)) +
            f'<g style="filter:drop-shadow(0 0 8px rgba(0,251,244,.45))">{candles_svg(r, w, h, kind, n=n, col_dn="#2E5A5F")}</g></svg></div>')

# ---------- components ----------
def stats(items, top, cols=3):
    cells = []
    for lab, big, small, up in items:
        cls = "glow" if up is True else ("glowr" if up is False else "")
        cells.append(f'<div class="gp" style="padding:24px 26px"><p class="lab">{lab}</p><div class="num {cls}" style="font-size:52px;margin-top:8px;line-height:1.05">{big}</div><div style="font-size:20px;color:#8A959A;margin-top:6px">{small}</div></div>')
    return f'<div class="pad" style="top:{top}px;display:grid;grid-template-columns:repeat({cols},1fr);gap:16px">{"".join(cells)}</div>'

def bars(rows, top, scale, label_w=260, val_w=160, row_h=88):
    track = 1080 - 128 - 64 - label_w - val_w
    mid = track / 2
    out = [f'<div class="gp" style="position:absolute;left:64px;right:64px;top:{top}px;padding:14px 32px">']
    for i, (lab, sub, v, t) in enumerate(rows):
        w = min(abs(v) / scale, 1) * mid; up = v >= 0; col = CY if up else DN
        x = mid if up else mid - w
        bd = "" if i == len(rows) - 1 else "border-bottom:1px solid rgba(255,255,255,.05);"
        out.append(f'<div style="display:flex;align-items:center;height:{row_h}px;{bd}"><div style="width:{label_w}px"><div style="font-size:25px;font-weight:500">{lab}</div><div style="font-size:15px;color:#7D878C">{sub}</div></div>'
                   f'<div style="position:relative;width:{track}px;height:100%"><div style="position:absolute;left:{mid}px;top:16px;bottom:16px;width:2px;background:rgba(255,255,255,.1)"></div>'
                   f'<div style="position:absolute;left:{x:.0f}px;top:{row_h / 2 - 11}px;width:{max(w, 6):.0f}px;height:22px;border-radius:11px;background:{col};box-shadow:0 0 18px {col}88"></div></div>'
                   f'<div class="num" style="width:{val_w}px;text-align:right;font-size:30px;color:{col}">{t}</div></div>')
    out.append('</div>')
    return "".join(out)

def steps(items, top, gap=18, big=31, small=23):
    out = [f'<div class="pad" style="top:{top}px;display:flex;flex-direction:column;gap:{gap}px">']
    for i, (h, p) in enumerate(items, 1):
        out.append(f'<div class="gp" style="display:flex;gap:26px;align-items:flex-start;padding:26px 30px"><div style="flex:none;width:56px;height:56px;border-radius:50%;border:2px solid #00FBF4;color:#00FBF4;display:flex;align-items:center;justify-content:center;font-weight:500;font-size:20px;box-shadow:0 0 20px rgba(0,251,244,.25)">{i:02d}</div>'
                   f'<div><div style="font-size:{big}px;font-weight:700;line-height:1.2">{h}</div><div style="font-size:{small}px;line-height:1.45;color:#AFB8BC;margin-top:6px">{p}</div></div></div>')
    out.append('</div>')
    return "".join(out)

def checklist(rows, top, h=100):
    """rows: (left, label, icon, key)"""
    out = [f'<div class="gp" style="position:absolute;left:64px;right:64px;top:{top}px;padding:12px 18px">']
    for i, (t, lab, ic, key) in enumerate(rows):
        bg_ = "background:rgba(0,251,244,.08);border:1.5px solid rgba(0,251,244,.45);box-shadow:0 0 30px rgba(0,251,244,.12);" if key else "border:1.5px solid transparent;"
        out.append(f'<div style="display:flex;align-items:center;gap:22px;height:{h}px;padding:0 20px;border-radius:22px;{bg_}">{ic}'
                   f'<div style="flex:1;font-size:27px;font-weight:{700 if key else 500};color:{"#fff" if key else "#D5DBDE"}">{lab}</div><div class="num" style="font-size:27px;color:{"#00FBF4" if key else "#AFAFAF"}">{t}</div></div>')
    out.append('</div>')
    return "".join(out)

def meter(label, room, move, unit, top, note=None):
    """How much of a $2,000 drawdown a move eats, in points."""
    frac = move / room
    over = frac > 1
    w = 820
    fill = min(frac, 1) * w
    col = DN if over else CY
    tag = f'{frac:.0f}x your room' if over else f'{frac * 100:.0f}% of your room'
    ticks = "".join(f'<div style="position:absolute;left:{w * k / 4:.0f}px;top:-8px;bottom:-8px;width:2px;background:rgba(255,255,255,.12)"></div>' for k in range(1, 4))
    return (f'<div class="gp {"red" if over else "hot"}" style="position:absolute;left:64px;right:64px;top:{top}px;padding:28px 32px">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span class="num" style="font-size:38px">{label}</span><span class="pill {"r" if over else "on"}" style="font-size:20px;padding:10px 22px">{tag}</span></div>'
            f'<div style="font-size:24px;color:#AFB8BC;margin-top:10px">Room: <b style="color:#fff">{room:,} {unit}</b> &middot; Move: <b style="color:#fff">{move:,} {unit}</b></div>'
            f'<div style="position:relative;margin-top:24px;width:{w}px;height:28px;border-radius:14px;background:rgba(255,255,255,.06)">{ticks}'
            f'<div style="position:absolute;left:0;top:0;height:28px;width:{fill:.0f}px;border-radius:14px;background:{col};box-shadow:0 0 22px {col}99"></div></div>'
            + (f'<div style="font-size:22px;color:#8A959A;margin-top:14px">{note}</div>' if note else "") + '</div>')

def header_panel(kicker, title, top=96, hot=False):
    return (f'<div class="gp {"hot" if hot else ""} ctr" style="position:absolute;left:64px;right:64px;top:{top}px;padding:30px 40px">'
            f'<p class="lab">{kicker}</p><h1 class="hl m" style="margin-top:12px">{title}</h1></div>')
