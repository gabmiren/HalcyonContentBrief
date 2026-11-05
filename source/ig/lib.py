"""Halcyon IG slide kit v3.

Built from halcyontraderfunding.com (pure black, pink/cyan star dust, Inter, cyan + lavender + pink accents,
thin teal-bordered cards, glowing featured card, HUD certificate corners, cyan wave) with FTMO's cinematic
layouts (centred mixed-weight titles, spaced kickers, glass panels with a light streak, ghost numerals)
and Lucid's internet-native bits (terminal ticker, native UI mockups). Uses the real Halcyon logo.
"""
import random, math, html

CY = "#00FBF4"; GR = "#B0B0B0"; DN = "#F472B6"; LAV = "#C4B5FD"; AMB = "#FCD34D"
BRAND = "file:///home/claude/halcyon/ig/brand/"
E = html.escape

CSS = """
*{box-sizing:border-box}html,body{margin:0;background:#000}
body{font-family:Inter,sans-serif;color:#fff;-webkit-font-smoothing:antialiased;font-feature-settings:"ss01","cv11"}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;background:#000}
.s.st{height:1920px}
.pad{position:absolute;left:72px;right:72px}
.hl{font-family:"Inter Display",Inter,sans-serif;font-weight:700;font-size:72px;line-height:1.04;letter-spacing:-.035em;margin:0;text-wrap:balance}
.hl.m{font-size:62px}.hl.s2{font-size:52px}.hl.xl{font-size:100px;line-height:.98;letter-spacing:-.04em}
.hl .lt{font-weight:400;color:#E8ECEE}
.ctr{text-align:center}
.a,.glow{color:#00FBF4}
.glow{text-shadow:0 0 28px rgba(0,251,244,.22)}
.glowr,.dn{color:#F472B6}
.glowr{text-shadow:0 0 28px rgba(244,114,182,.22)}
.lav{color:#C4B5FD}.g{color:#B0B0B0}
.kick{font-weight:600;font-size:22px;letter-spacing:.22em;text-transform:uppercase;color:#00FBF4;margin:0}
.kick.lav{color:#C4B5FD}.kick.pk{color:#F472B6}.kick.g{color:#B0B0B0}
.lab{font-weight:600;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:#9AA3A8;margin:0}
.body{font-size:32px;line-height:1.4;color:#D3D9DC;margin:0;text-wrap:pretty}
.body b{color:#fff;font-weight:600}.body .a{font-weight:600}
.gp{position:relative;border-radius:28px;background:linear-gradient(180deg,rgba(16,20,24,.86),rgba(6,8,10,.90));border:1.5px solid rgba(0,251,244,.17);box-shadow:inset 0 1px 0 rgba(255,255,255,.05),0 30px 70px rgba(0,0,0,.55);padding:30px 34px}
.gp.hot{border:2px solid #00FBF4;box-shadow:0 0 0 1px rgba(0,251,244,.10),0 0 40px rgba(0,251,244,.16),0 30px 70px rgba(0,0,0,.6)}
.gp.hot::before,.flare::before{content:"";position:absolute;left:18%;right:18%;top:-2px;height:3px;border-radius:3px;background:linear-gradient(90deg,transparent,#B9FFFD 50%,transparent);box-shadow:0 0 22px 6px rgba(0,251,244,.55);pointer-events:none}
.gp.red{border-color:rgba(244,114,182,.55);box-shadow:0 0 50px rgba(244,114,182,.14),0 30px 70px rgba(0,0,0,.55)}
.gp.lavb{border-color:rgba(196,181,253,.5);box-shadow:0 0 50px rgba(167,139,250,.16),0 30px 70px rgba(0,0,0,.55)}
.pill{display:inline-flex;align-items:center;gap:10px;border-radius:999px;padding:12px 24px;font-weight:600;font-size:24px;letter-spacing:0;border:1.5px solid rgba(0,250,242,.32);color:#00FBF4;background:rgba(0,250,242,.09)}
.pill.on{background:#00FBF4;color:#001312;border-color:#00FBF4;box-shadow:0 0 34px rgba(0,251,244,.45)}
.pill.r{border-color:rgba(244,114,182,.45);color:#F472B6;background:rgba(244,114,182,.10)}
.pill.gr{border-color:#3A4247;color:#B0B0B0;background:rgba(255,255,255,.03)}
.pill.lav{border-color:rgba(196,181,253,.45);color:#C4B5FD;background:rgba(167,139,250,.12)}
.pill.amb{border-color:rgba(252,211,77,.45);color:#FCD34D;background:rgba(245,158,11,.10)}
.tog{display:inline-flex;border-radius:16px;background:rgba(2,6,23,.6);border:1.5px solid #1D2328;padding:6px}
.tog span{padding:16px 32px;border-radius:12px;font-weight:600;font-size:26px;color:#A3AEBD}
.tog span.on{background:#C4B5FD;color:#0B0620;box-shadow:0 0 24px rgba(196,181,253,.35)}
.tog.cy span.on{background:#00FBF4;color:#001312;box-shadow:0 0 26px rgba(0,251,244,.45)}
.foot{position:absolute;left:72px;right:72px;bottom:48px;display:flex;justify-content:space-between;align-items:center}
.swipe{font-size:24px;color:#B0B0B0;font-weight:500;display:flex;align-items:center;gap:10px}
.src{position:absolute;left:72px;right:72px;bottom:120px;font-size:20px;line-height:1.4;letter-spacing:.02em;color:#8E979C;margin:0}
.num{font-family:"Inter Display",Inter,sans-serif;font-weight:700;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.disc{font-size:20px;line-height:1.45;color:#9AA3A8;margin:0}
.ic{flex:none;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.ic.ok{background:rgba(0,251,244,.12);border:1.5px solid rgba(0,251,244,.5)}
.ic.no{border:1.5px solid #3A4247}
.ic.wn{background:rgba(244,114,182,.16);border:1.5px solid rgba(244,114,182,.7)}
.ghost{position:absolute;font-family:"Inter Display",Inter,sans-serif;font-weight:800;line-height:.8;color:transparent;-webkit-text-stroke:2px rgba(0,251,244,.13);letter-spacing:-.05em;pointer-events:none}
.tick{position:absolute;left:0;right:0;top:0;height:56px;background:rgba(0,0,0,.6);border-bottom:1px solid rgba(0,251,244,.2);display:flex;align-items:center;overflow:hidden;white-space:nowrap;font-family:"DejaVu Sans Mono",monospace;font-size:20px;letter-spacing:.08em;color:#00FBF4}
.tick span{padding:0 26px;opacity:.9}.tick em{font-style:normal;color:#F472B6}
.bubble{max-width:720px;padding:24px 32px;font-size:35px;line-height:1.32}
.bubble.l{align-self:flex-start;background:#1F2226;border-radius:34px 34px 34px 10px}
.bubble.r{align-self:flex-end;background:linear-gradient(180deg,#14E8E1,#00BDB7);color:#00201E;border-radius:34px 34px 10px 34px;font-weight:500}
.who{font-size:24px;color:#9AA3A8;letter-spacing:.04em;margin:0 0 -14px 14px}
"""

def logo(h=56, kind="full", st=""):
    return f'<img src="{BRAND}logo_{kind}.png" style="height:{h}px;display:block;{st}">'

def lockup(h=52, st="", glow=False):
    """Horizontal lockup built from the real logo: candle mark + HALCYON / TRADER FUNDING wordmark."""
    gl = "filter:drop-shadow(0 0 18px rgba(0,251,244,.45));" if glow else ""
    return (f'<div style="display:flex;align-items:center;gap:{h * .3:.0f}px;{gl}{st}"><img src="{BRAND}logo_mark.png" style="height:{h}px;display:block">'
            f'<img src="{BRAND}logo_word.png" style="height:{h * .64:.0f}px;display:block"></div>')

def biglogo(h=300, st=""):
    return f'<img src="{BRAND}logo_full.png" style="height:{h}px;display:block;margin:0 auto;filter:drop-shadow(0 0 40px rgba(0,251,244,.40));{st}">'

def wordmark(st=""):
    return lockup(66, st)

def cover_top(top=74):
    return f'<div style="position:absolute;left:0;right:0;top:{top}px;display:flex;justify-content:center">{lockup(50, glow=True)}</div>'

def rings(cx, cy, rs=(230, 330, 450), col="0,251,244"):
    """Concentric orbit rings (the circle half of the circles + rectangles system)."""
    return "".join(f'<div style="position:absolute;left:{cx - r_}px;top:{cy - r_}px;width:{2 * r_}px;height:{2 * r_}px;border-radius:50%;border:1.5px solid rgba({col},{.22 - i * .06:.2f})"></div>' for i, r_ in enumerate(rs))

def foot(left=None, logo_on=True):
    l = f'<span class="swipe">{left}</span>' if left else '<span></span>'
    lg = lockup(42) if logo_on else '<span></span>'
    return f'<div class="foot">{lg}{l}</div>'

def src(t, bottom=120):
    return f'<p class="src" style="bottom:{bottom}px">{t}</p>'

def page(inner, story=False):
    return f'<!doctype html><html><head><meta charset=utf8><style>{CSS}</style></head><body><div class="s{" st" if story else ""}">{inner}</div></body></html>'

_ck = '<svg width="20" height="20" viewBox="0 0 20 20"><path d="M5 10.5l3.4 3.4L15.5 6.5" stroke="#00FBF4" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
OK = f'<div class="ic ok">{_ck}</div>'
NO = '<div class="ic no"><svg width="16" height="16" viewBox="0 0 16 16"><path d="M4 4l8 8M12 4l-8 8" stroke="#6E777C" stroke-width="2.2" stroke-linecap="round"/></svg></div>'
WN = '<div class="ic wn"><svg width="20" height="20" viewBox="0 0 20 20"><path d="M10 4.5v7" stroke="#F472B6" stroke-width="2.8" stroke-linecap="round"/><circle cx="10" cy="15" r="1.7" fill="#F472B6"/></svg></div>'

# ---------- backgrounds ----------
def stars(r, w, h, n=90):
    out = []
    for _ in range(n):
        x, y = r.uniform(0, w), r.uniform(0, h); s = r.choice([1, 1, 1.2, 1.5, 2, 2.6])
        c = r.random(); col = "#F472B6" if c < .22 else ("#00FBF4" if c < .34 else "#FFFFFF")
        op = r.uniform(.25, .85) if col != "#FFFFFF" else r.uniform(.12, .45)
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s}" fill="{col}" opacity="{op:.2f}"/>')
    return "".join(out)

def price_path(r, n, kind):
    """Closes with a trend shape plus real swings: pullbacks in uptrends, bounces in downtrends."""
    shape = {"up": lambda t: t, "down": lambda t: 1 - t, "flat": lambda t: .5,
             "spike": lambda t: .35 + (0 if t < .7 else (t - .7) * 2.2), "drop": lambda t: .65 - (0 if t < .7 else (t - .7) * 2.2),
             "vshape": lambda t: abs(t - .45) * 1.6}.get(kind, lambda t: .5)
    ph1, ph2 = r.uniform(0, 6.3), r.uniform(0, 6.3)
    out, ar_ = [], 0
    for i in range(n + 1):
        t = i / n
        ar_ = ar_ * .55 + r.gauss(0, .05)
        out.append(shape(t) + math.sin(t * 6.3 * 2.6 + ph1) * .09 + math.sin(t * 6.3 * 5.3 + ph2) * .04 + ar_)
    return out

def candles_svg(r, w, h, kind, n=26, base=None, col_up="#00FBF4", col_dn="#21474B", pad=.12):
    cl = price_path(r, n, kind); lo_, hi_ = min(cl), max(cl); rng = (hi_ - lo_) or 1
    y = lambda v: h * pad + (1 - (v - lo_) / rng) * h * (1 - 2 * pad)
    out = []; cw = w / n
    for i in range(n):
        o, c = y(cl[i]), y(cl[i + 1]) + r.uniform(-h * .006, h * .006)
        hi = min(o, c) - r.uniform(4, h * .035); lo = max(o, c) + r.uniform(4, h * .035)
        up = c < o; x = i * cw + cw / 2; col = col_up if up else col_dn
        out.append(f'<line x1="{x:.0f}" y1="{hi:.0f}" x2="{x:.0f}" y2="{lo:.0f}" stroke="{col}" stroke-width="3"/>'
                   f'<rect x="{x - cw * .3:.0f}" y="{min(o, c):.0f}" width="{cw * .6:.0f}" height="{max(abs(c - o), 4):.0f}" rx="3" fill="{col}"/>')
    return "".join(out)

def bg(seed=1, kind="flat", story=False, glow=(50, 18), blur=8, op=.16, lav=False):
    """Pure black, star dust, one soft light source (cyan, or lavender for promo), faint chart ghost."""
    r = random.Random(seed); w, h = 1080, (1920 if story else 1350)
    gx, gy = glow
    g2 = "rgba(167,139,250,.20)" if lav else "rgba(0,251,244,.17)"
    ghost = "" if kind == "flat" else f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;filter:blur({blur}px);opacity:{op}">{candles_svg(r, w, h, kind)}</svg>'
    return (f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse 70% 45% at {gx}% {gy}%,{g2},transparent 70%),#000"></div>'
            f'{ghost}<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0">{stars(r, w, h, 120 if story else 90)}</svg>'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 50%,transparent 55%,rgba(0,0,0,.55))"></div>')

def wave(top, story=False, h=120):
    """The cyan wave from the site footer."""
    w = 1080
    pts = " ".join(f"{x},{30 + math.sin(x / 150) * 9 + math.sin(x / 47) * 2:.1f}" for x in range(0, w + 10, 10))
    return (f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:{top}px">'
            f'<defs><linearGradient id="wf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0E4A49" stop-opacity=".9"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient></defs>'
            f'<polygon points="0,{h} {pts} {w},{h}" fill="url(#wf)"/><polyline points="{pts}" fill="none" stroke="#00FBF4" stroke-width="3" style="filter:drop-shadow(0 0 8px rgba(0,251,244,.8))"/></svg>')

def hud(l, t, w, h, c1="#00FBF4", c2="#00FBF4", s=48):
    """Certificate-style corner brackets: cyan top-left/bottom-right, pink top-right/bottom-left."""
    def corner(x, y, rot, col):
        return (f'<svg width="{s}" height="{s}" style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);filter:drop-shadow(0 0 8px {col})">'
                f'<path d="M3 {s - 3} V3 H{s - 3}" fill="none" stroke="{col}" stroke-width="4" stroke-linecap="round"/></svg>')
    return (f'<div style="position:absolute;left:{l}px;top:{t}px;width:{w}px;height:{h}px;pointer-events:none">'
            + corner(0, 0, 0, c1) + corner(w - s, 0, 90, c2) + corner(w - s, h - s, 180, c1) + corner(0, h - s, 270, c2) + '</div>')

def ticker(items, top=0):
    """Lucid-style terminal strip. items: plain strings; wrap a word in <em> for pink."""
    row = "".join(f"<span>{x}</span><span style='opacity:.35'>|</span>" for x in items * 3)
    return f'<div class="tick" style="top:{top}px">{row}</div>'

def ghostnum(n, right=40, top=60, size=560):
    return f'<div class="ghost" style="right:{right}px;top:{top}px;font-size:{size}px">{n}</div>'

def hero_chart(seed, kind, top=120, h=520, n=30, op=1, tilt=False, left=72, right=72):
    """Glass panel holding a crisp glowing candle chart. tilt=True floats it in 3D like FTMO's UI panels."""
    r = random.Random(seed); w = 1080 - left - right
    tf = ""  # always face forward
    return (f'<div class="gp hot" style="position:absolute;left:{left}px;right:{right}px;top:{top}px;height:{h}px;padding:0;overflow:hidden;{tf}">'
            f'<svg width="{w}" height="{h}" style="position:absolute;left:0;top:0;opacity:{op}">' +
            "".join(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="rgba(0,251,244,.07)" stroke-width="1.5"/>' for y in range(60, h, 80)) +
            f'<g style="filter:drop-shadow(0 0 8px rgba(0,251,244,.45))">{candles_svg(r, w, h, kind, n=n, col_dn="#F472B6")}</g></svg></div>')

# ---------- components ----------
def header_panel(kicker, title, top=112, hot=False, ctr=False):
    """FTMO-style title block: spaced kicker over a big title. No box."""
    al = "text-align:center;" if ctr else ""
    k = f'<p class="kick{" lav" if hot else ""}" style="margin-bottom:16px">{kicker}</p>' if kicker else ""
    return f'<div class="pad" style="top:{top}px;{al}">{k}<h1 class="hl">{title}</h1></div>'

def stats(items, top, cols=3):
    cells = []
    for i, (lab, big, small, up) in enumerate(items):
        cls = "a" if up is True else ("dn" if up is False else "")
        cells.append(f'<div class="gp" style="padding:24px 24px 24px"><p class="lab">{lab}</p><div class="num {cls}" style="font-size:54px;margin-top:10px;line-height:1">{big}</div>' + (f'<div style="font-size:24px;color:#9AA3A8;margin-top:8px">{small}</div>' if small else "") + '</div>')
    return f'<div class="pad" style="top:{top}px;display:grid;grid-template-columns:repeat({cols},1fr);gap:16px">{"".join(cells)}</div>'

def bars(rows, top, scale, label_w=260, val_w=170, row_h=90):
    track = 1080 - 144 - 68 - label_w - val_w
    mid = track / 2
    out = [f'<div class="gp" style="position:absolute;left:72px;right:72px;top:{top}px;padding:14px 34px">']
    for i, (lab, sub, v, t) in enumerate(rows):
        w = min(abs(v) / scale, 1) * mid; up = v >= 0; col = CY if up else DN
        x = mid if up else mid - w
        bd = "" if i == len(rows) - 1 else "border-bottom:1px solid rgba(255,255,255,.05);"
        out.append(f'<div style="display:flex;align-items:center;height:{row_h}px;{bd}"><div style="width:{label_w}px"><div style="font-size:30px;font-weight:600">{lab}</div>' + (f'<div style="font-size:22px;color:#9AA3A8">{sub}</div>' if sub else "") + f'</div>'
                   f'<div style="position:relative;width:{track}px;height:100%"><div style="position:absolute;left:{mid}px;top:16px;bottom:16px;width:2px;background:rgba(255,255,255,.12)"></div>'
                   f'<div style="position:absolute;left:{x:.0f}px;top:{row_h / 2 - 9}px;width:{max(w, 6):.0f}px;height:18px;border-radius:9px;background:{col};box-shadow:0 0 16px {col}88"></div></div>'
                   f'<div class="num" style="width:{val_w}px;text-align:right;font-size:34px;color:{col}">{t}</div></div>')
    out.append('</div>')
    return "".join(out)

def steps(items, top, gap=18, big=32, small=24):
    out = [f'<div class="pad" style="top:{top}px;display:flex;flex-direction:column;gap:{gap}px">']
    for i, (h, p) in enumerate(items, 1):
        out.append(f'<div class="gp" style="display:flex;gap:24px;align-items:flex-start;padding:32px">'
                   f'<div class="num" style="flex:none;width:64px;font-size:44px;line-height:1.05;color:#00FBF4">{i:02d}</div>'
                   f'<div><div style="font-size:{big}px;font-weight:700;line-height:1.2;letter-spacing:-.01em">{h}</div>' + (f'<div style="font-size:{small}px;line-height:1.45;color:#AEB6BA;margin-top:8px">{p}</div>' if p else "") + '</div></div>')
    out.append('</div>')
    return "".join(out)

def checklist(rows, top, h=100):
    out = [f'<div class="gp" style="position:absolute;left:72px;right:72px;top:{top}px;padding:12px 18px">']
    for i, (t, lab, ic, key) in enumerate(rows):
        bg_ = "background:rgba(0,251,244,.07);border:1.5px solid rgba(0,251,244,.5);box-shadow:0 0 30px rgba(0,251,244,.12);" if key else "border:1.5px solid transparent;"
        sep = "" if key or i == len(rows) - 1 else "box-shadow:inset 0 -1px 0 rgba(255,255,255,.05);"
        out.append(f'<div style="display:flex;align-items:center;gap:22px;height:{h}px;padding:0 22px;border-radius:20px;{bg_}{sep}">{ic}'
                   f'<div style="flex:1;font-size:30px;font-weight:{700 if key else 500};color:{"#fff" if key else "#D3D9DC"}">{lab}</div><div class="num" style="font-size:30px;color:{"#00FBF4" if key else "#B0B0B0"}">{t}</div></div>')
    out.append('</div>')
    return "".join(out)

def meter(label, room, move, unit, top, note=None):
    frac = move / room; over = frac > 1; w = 830
    fill = min(frac, 1) * w; col = DN if over else CY
    tag = f'{frac:.0f}x your room' if over else f'{frac * 100:.0f}% of your room'
    ticks = "".join(f'<div style="position:absolute;left:{w * k / 4:.0f}px;top:-7px;bottom:-7px;width:2px;background:rgba(255,255,255,.14)"></div>' for k in range(1, 4))
    return (f'<div class="gp {"red" if over else "hot"}" style="position:absolute;left:72px;right:72px;top:{top}px;padding:30px 34px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><span class="num" style="font-size:44px">{label}</span><span class="pill {"r" if over else "on"}">{tag}</span></div>'
            f'<div style="font-size:28px;color:#AEB6BA;margin-top:8px">Room <b style="color:#fff">{room:,} {unit}</b> &nbsp;&middot;&nbsp; Move <b style="color:#fff">{move:,} {unit}</b></div>'
            f'<div style="position:relative;margin-top:24px;width:{w}px;height:24px;border-radius:12px;background:rgba(255,255,255,.06)">{ticks}'
            f'<div style="position:absolute;left:0;top:0;height:24px;width:{fill:.0f}px;border-radius:12px;background:{col};box-shadow:0 0 22px {col}99"></div></div>'
            + (f'<div style="font-size:26px;color:#9AA3A8;margin-top:16px">{note}</div>' if note else "") + '</div>')
