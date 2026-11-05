import os
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from playwright.sync_api import sync_playwright
import slides
from slides import S, story

D = os.path.dirname(os.path.abspath(__file__))
os.makedirs(f"{D}/html", exist_ok=True); os.makedirs(f"{D}/img", exist_ok=True)
only = set(sys.argv[1:])

def render(items):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for name, (h, st) in items:
            if only and name not in only: continue
            f = f"{D}/html/{name}.html"; open(f, "w").write(h)
            pg.set_viewport_size({"width": 1080, "height": 1920 if st else 1350})
            pg.goto("file://" + f); pg.wait_for_timeout(120)
            pg.locator(".s").screenshot(path=f"{D}/img/{name}.png")
        b.close()

# slides that embed other renders go last, after their sources exist
DEP = ["wcB_1", "wcA_2", "wcD_1"]
render([kv for kv in S.items() if kv[0] not in DEP])
from PIL import Image
CROPS = {"etA_1_t": (40, 360, 1040, 1360), "nbA_1_t": (80, 290, 1000, 1210), "mmB_1_t": (90, 120, 990, 1020)}
for n, box in CROPS.items():
    p = f"{D}/img/{n}.png"
    if os.path.exists(p): Image.open(p).crop(box).save(f"{D}/img/{n}c.png")
dep = [(k, S[k]) for k in DEP if k in S]
S.clear(); render(dep)
I = f"file://{D}/img/"
story("bnA", "+3.03", "%", "The Dow&rsquo;s best post-midterm day since&nbsp;1982.", I + "nbA_1.png", "The full story, in points.", 121, "vshape")
story("bnB", "4:45", "PM ET", "Be flat by then, every trading day.", I + "mmB_1.png", "Myth or fact? Test yourself.", 122, "flat")
story("bnC", "40", "pts", "Your whole $2,000 drawdown on one ES contract.", I + "etA_1.png", "How many points is yours?", 123, "up")
render(list(S.items()))
print("done")
