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

render(list(S.items()))
S.clear()
I = f"file://{D}/img/"
story("bnA", "+3.03", "%", "The Dow&rsquo;s best post-midterm day since 1982.", I + "nbA_1.png", "The full story, in points.", 121, "vshape")
story("bnB", "4:45", "PM ET", "Be flat by then, every trading day.", I + "mmB_1.png", "Myth or fact? Test yourself.", 122, "flat")
story("bnC", "40", "pts", "Your whole $2,000 drawdown on one ES contract.", I + "etA_1.png", "How many points is yours?", 123, "up")
render(list(S.items()))
print("done")
