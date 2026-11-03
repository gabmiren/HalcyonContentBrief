import json, html as H
P="carousel/project"
order=json.load(open(f"{P}/canvas.json"))["order"]
slides=[open(f"{P}/{f}").read().split("</helmet>",1)[1].split("</x-dc>",1)[0].strip() for f in order]
slide_html="\n".join(f'<div class="slide" aria-roledescription="slide" aria-label="Slide {i+1} of {len(slides)}"><div class="scaler">{b}</div></div>' for i,b in enumerate(slides))

CALL={"ready":("Close to ready","ok"),"refresh":("Needs changes","warn"),"hold":("On hold","hold"),"retire":("Retire","bad"),"new":("New","new")}
def vid(file,title,sub,status,call,notes,ai=False):
    lab,cls=CALL[call]
    ai_tag='<span class="chip ai">AI</span>' if ai else ""
    li="".join(f"<li>{n}</li>" for n in notes)
    return f'''<article class="card">
<div class="media"><video src="media/{file}" controls playsinline preload="metadata"></video></div>
<div class="info"><div class="chips"><span class="chip">{status}</span>{ai_tag}<span class="chip {cls}">{lab}</span></div>
<h4>{title}</h4><p class="sub">{sub}</p><ul>{li}</ul></div></article>'''
def refvid(file,title,handle,url,notes,pre='Example: ',tag='Example'):
    li="".join(f"<li>{n}</li>" for n in notes)
    return f'''<article class="card">
<div class="media"><video src="media/{file}#t=1" controls playsinline preload="metadata"></video></div>
<div class="info"><div class="chips"><span class="chip new">{tag}</span><span class="chip hold">Not ours</span></div>
<h4>{pre}{title}</h4><p class="sub">By <a href="{url}">{handle} on TikTok</a></p><ul>{li}</ul></div></article>'''
def refs(items):
    return '<div class="refs"><span>Works in the niche:</span>'+" ".join(f'<a href="{u}">{t}</a>' for t,u in items)+"</div>"

proof=[vid("proof1-no-closed-beta.mp4","Why no closed beta","Founder short · from Steve's Arena video · 24 s","Draft · needs your OK","refresh",
  ["Safe message, founder on camera, Discord end card","Fix: crop to 9:16 so Steve fills the frame, 3 to 5 word captions, readable disclaimer","Posts once counsel clears the Arena wording"]),
 vid("proof2-arena-rewards.mp4","How fast are Arena rewards","Founder short · from Steve's Arena video · 21 s","Draft · needs compliance OK","hold",
  ["\"You literally could be paid the same day\" is a payout-speed claim","Promotes Arena's seat-funded pool","Needs Halcyon's written OK and counsel first"])]
ent_chars='''<div class="chars"><figure><img src="media/char-cyan.jpg" alt="Character sheet of Cyan: a tall man with teal hair, handlebar mustache and a charcoal three-piece suit"><figcaption><b>Cyan</b> deadpan gentleman · memes</figcaption></figure>
<figure><img src="media/char-mark.jpg" alt="Character sheet of Mark: a young man in a grey hoodie with the hood up, joggers and white sneakers"><figcaption><b>Mark</b> young trader host · tutorials</figcaption></figure></div>'''
tut=[vid("tutorial-mark-says-hi.mp4","Mark says hi","Mark · intro to the tutorial series · 12 s","Draft · voice being fixed","refresh",
  ["\"Make the most out of Halcyon… so you can do the same\" reads as an AI customer implying results","Rewrite: \"I'm Mark, an AI character. One futures rule a week, under 30 seconds.\"","Hide the Apple logo; AI label on"],ai=True)]
memes=[vid("meme1-touch-grass.mp4","Touch grass","Cyan · first post · 12 s","Draft","ready",
  ["Already the approved Cyan v5 look","Pigeons forming a double top, then \"Short.\" is a trader-only joke","Add a Discord end card; needs Halcyon's OK on Cyan"],ai=True),
 vid("meme2-done-for-the-day.mp4","Done for the day","Cyan · when the trade hits target · 15 s","Draft","refresh",
  ["Discipline punchline works","Swap the cigarette for a coffee cup and the explosion for a calmer backdrop","Match Cyan v5 hair"],ai=True)]
ads=[vid("ad-forgot-to-close.mp4","Forgot to close the trade","POV with sound design · Halloween · 23 s","Draft","retire",
  ["Says \"relax\" because positions auto-close, but the help center says an account not flat by 4:45 PM fails","Halloween is over; old character, code HWN, \"Halcyon Trading\", old disclaimer","Reuse the panic footage for an honest rules explainer"],ai=True)]
edu=[vid("edu1-checklist.mp4","What an evaluation checks · Checklist","Motion graphics · glow panels · 21 s","Draft","new",
  ["A checklist of the four rules the $50K Halcyon Dynamic evaluation checks, ticking off one per beat","Each rule gets its own animated panel: the target bar fills to $3,000, a chart shows a trailing vs end-of-day drawdown floor, then the contract limit and a clock running to 4:45 PM ET","Ends on \"Save this before your eval\" and the Discord end card"]),
 vid("edu1-numbers.mp4","What an evaluation checks · Four numbers","Motion graphics · dealt cards · 20 s","Draft","new",
  ["One big number per card: $3,000, $2,000, 5 / 25 and 4:45 PM","Each card deals in on the beat and files into a row at the top, then all four come together as a recap","Faster and punchier; the checklist version explains more"]),
 vid("edu2-arena-two-sessions.mp4","Why Arena has two sessions","Founder short · from Steve's Arena video · 35 s","Draft · needs compliance OK","hold",
  ["Session times match the help center","Trim to about 20 s; drop the cyan highlight on \"$10,000, $15,000, $20,000 in profit\"","Waits on counsel's Arena sign-off"])]
promo=[vid("promo-dynamic.mp4","Halcyon Dynamic (current)","Your best seller in 20 s · unchanged","Draft","ready",
  ["Best-looking draft; values match the site ($3,000 target, $2,000 drawdown, 1 day)","Audio is silent: add a track","Confirm \"Traders' top choice\" and \"no daily loss limit\" wording, then compliance review"]),
 vid("promo-dynamic-v2A_builder.mp4","Option A · The Builder","Aurora · Sub Clair \"Technology\" · 15.5 s","Reworked","new",
  ["One glass panel the whole way: headline words light up on the drop, the evaluation rows cascade, a progress bar fills to \"You passed\"","Reward-account builder with sliding highlights: size steps 50K to 150K one per half-beat while the drawdown counts up, then drawdown type and consistency slide on the beat","Light sweeps and flares on the drop, the pass and the stats; the Discord pill grows on the end card"]),
 vid("promo-dynamic-v2B_fork.mp4","Option B · The Fork","Aurora · Sub Clair \"Technology\" · 15.5 s","Reworked","new",
  ["The line draws up through the intro and the node flares on the drop; rule tags pop on the next three beats","\"Passed\" grows over the node, then the line forks into four sizes on half-beats and a spark runs up to 100K","The camera dives through the node into the stats, then the end card"]),
 vid("promo-dynamic-v2C_card.mp4","Option C · The Card","Candle field · \"The Mountain\" · 16 s","Reworked","new",
  ["The card rises, lights on the drop and fills in row by row; \"Passed\" grows, then the card turns over in 3D","Four reward-account cards deal on half-beats and a ring hops across them to land on 150K","150K grows back into the main card; rule toggles slide on downbeats, then the stats and end card"]),
 vid("promo-dynamic-v2D_voice.mp4","Option D · Their voice","Candle field · Sub Clair phonk instrumental · 16.7 s","Reworked","new",
  ["Your original script, now in the glow style: the question sits in a top panel, the answer drops into the panel below","A typing indicator holds the beat before the punchlines (\"Optional.\", \"Never heard of her!\")","A new question every two beats (1.45 s) instead of every 2 s, with sliding controls for size, drawdown and consistency"])]

slide_html=open('carousel_slides.html').read()
cap=open('carousel_caption.txt').read()
tierlist=[refvid("ex-tierlist-setups.mp4","Ranking trading setups","@sellingrips","https://www.tiktok.com/@sellingrips/video/7691740202875882783",
  ["Solo founder at a desk, tier list fills the bottom half","Each setup gets a small chart as it lands in its row","Closest match for Steve"]),
 refvid("ex-tierlist-stocks.mp4","Ranking stocks","@_russellckai","https://www.tiktok.com/@_russellckai/video/7642209212478573845",
  ["Phone-camera selfie, fast and casual","Title on screen the whole time: \"ranking stocks tier list\"","Shows how low the production bar can be"]),
 refvid("ex-tierlist-strategies.mp4","Ranking trading strategies","@kingzeltzin_6","https://www.tiktok.com/@kingzeltzin_6/video/7670271908440509717",
  ["Two hosts trade opinions on each pick","Disagreements keep people watching and commenting","Works if Steve brings on a guest or a team member"])]
pnp=[refvid("ex-pnp-expo.mp4","Expo guest, quick fire","@wayondtv","https://www.tiktok.com/@wayondtv/video/7623424230847237394",
  ["Host reads a habit off his phone, the guest calls it in one or two words","Big tick or cross pops on every answer","Quick cutaways to other guests keep the pace up"]),
 refvid("ex-pnp-sitdown.mp4","Sit-down version","@wayondtv","https://www.tiktok.com/@wayondtv/video/7613034553493523730",
  ["Two chairs by a window, calmer and more premium","Same list, more room for the guest to explain","Easiest to film with Steve in an office"]),
 refvid("ex-pnp-floor.mp4","Event floor","@wayondtalks","https://www.tiktok.com/@wayondtalks/video/7674638334735551762",
  ["Shot at a trading expo with a branded mic","Guest gives a short reason after each call","Fits any meetup or event Halcyon attends"])]
react=[refvid("ex-react-revenge.mp4","Reacting to a revenge-trading clip","@danielholmestrades","https://www.tiktok.com/@danielholmestrades/video/7469766820224978192",
  ["The clip plays small over his shot, then he talks to camera","Turns someone else's mistake into his own rules","Bold captions with one key word highlighted"]),
 refvid("ex-react-lambo.mp4","Reacting to a lifestyle flex","@danielholmestrades","https://www.tiktok.com/@danielholmestrades/video/7455656190224157970",
  ["Calls out a \"month 1 to month 12\" Lamborghini clip","Grounded take: it takes time, unfollow the flex pages","Fits Halcyon's no-earnings-claims line well"]),
 refvid("ex-react-split.mp4","Split-screen reaction","@thebigdaddymax","https://www.tiktok.com/@thebigdaddymax/video/7683139024256535839",
  ["Founder on top, the clip underneath the whole time","Reactions land live, no talking-head section","Lowest editing effort of the four"]),
 refvid("ex-react-loss.mp4","Reacting to a fast loss","@jayfroneman","https://www.tiktok.com/@jayfroneman/video/7699194939690749205",
  ["Title bar sets it up: \"Hedge Fund COO reacts\"","Plays the trade, then explains what went wrong","Answers a viewer comment on screen to keep the thread going"])]
news=[refvid("ex-news-ipo-money.mp4","Explaining a big company headline","@alexisanddean","https://www.tiktok.com/@alexisanddean/video/7702147565600443661",
  ["The viewer's question sits in a caption box for the whole video","Shot on a phone at his desk, news on the TV behind him","Plain, calm explanation in about a minute"]),
 refvid("ex-news-market-down.mp4","\"Why is the market down this week?\"","@alexisanddean","https://www.tiktok.com/@alexisanddean/video/7696962249792998686",
  ["Ties the week's drop to a few clear causes","Hand gestures and the TV keep a static shot moving","Closest fit for Halcyon: a futures trader's view of the week"]),
 refvid("ex-news-ipo-story.mp4","Longer take on the same story","@alexisanddean","https://www.tiktok.com/@alexisanddean/video/7701036629175143711",
  ["Four and a half minutes, same setup","Shows the format holds even when it runs long","For Halcyon, keep most to under 90 seconds"])]
totw=[vid("totw-founder.mp4","Founder reply","Chart on top, founder below · 39 s","Draft · founder to film","new",
  ["The bottom half is a placeholder that talks with the voice; swap in Steve filmed chest-up and keep the layout","Opens on a Discord comment and a \"Halcyon breaks down this week's top trade\" title box","A light trade log highlights \"50% of the fair value gap\" and \"20 EMA\" as they're spoken"]),
 vid("totw-replay.mp4","Replay panels","Chart replay in glass panels · 39 s","Draft","new",
  ["The trade plays back with a 0:00 to 2:45 scrubber while a checklist ticks off each step","Flips to a result card, then a reply card types the question","Closest to the approved 18th Street default"]),
 vid("totw-faceless.mp4","Faceless edit","Founder-edit pacing, no presenter · 39 s","Draft","new",
  ["Hard cuts between chart framings with a slow push in each shot","Giant \"64 points\" on the drop and \"No early exit\" one word at a time","Proof card with highlight sweeps, then the question card"])]
capmemes=[vid("meme3-life-after-profit.mp4","Life after taking profit","Viral clip + one-line caption · 21 s","Draft","new",
  ["Caption box on top, the clip in the middle, Halcyon logo below","Easy to make weekly from trending clips","The clip belongs to someone else: credit or license it before posting"])]
recreated=[refvid("recreate-original.mp4","Original · 83.6K views","@danielholmestrades","https://www.tiktok.com/@danielholmestrades/video/7657167264470371604",
  ["83.6K views and 3.6K likes on 3 Nov","\"When she's crashing out but you're in drawdown\"","The trading screen behind him is what makes the joke land"],pre="",tag="Original"),
 vid("recreate-remake.mp4","Crashing out vs drawdown","AI character · recreated trending meme · 15 s","Draft","new",
  ["Same movement and timing as the original, played by our AI character","Trading screen rebuilt in post: price rallies back into the red zone","Copy added to match the original"],ai=True)]
carousel=f'''<article class="card wide">
<div class="phone"><div class="viewport" id="vp" aria-roledescription="carousel" aria-label="Carousel preview" tabindex="0">
<div class="track" id="track">
{slide_html}
</div>
<button class="nav prev" id="prev" aria-label="Previous slide">‹</button>
<button class="nav next" id="next" aria-label="Next slide">›</button>
</div><div class="dots" id="dots"></div><div class="count" id="count"></div></div>
<div class="info"><div class="chips"><span class="chip">Photo carousel · 7 slides · 1080×1440</span><span class="chip new">New</span></div>
<h4>Trailing vs end of day drawdown</h4><p class="sub">Modelled on the @flowfaceless order flow carousels: question hook, one idea per slide, recap with \"Follow &amp; save\"</p>
<ul><li>Example figures use the $50K Dynamic evaluation ($2,000 drawdown)</li><li>Halcyon to confirm the drawdown mechanics match their rules</li><li>Swap @halcyontraderfunding for the new account's handle once set</li></ul>
<p class="lab">Caption</p><pre id="cap">{H.escape(cap)}</pre><button class="copy" id="copyBtn">Copy caption</button></div></article>'''

def section(id,name,share,desc,inner):
    return f'<section id="{id}"><div class="sec-head"><h2>{name}</h2><span class="share">{share}</span></div><p class="desc">{desc}</p>{inner}</section>'
grid=lambda cards:'<div class="grid">'+"".join(cards)+"</div>"

upgrade=section("sheet-upgrade","Character sheet upgrade","Preview","Testing the Higgsfield three-panel method on Mark. Nothing above is replaced; this is for comparison only.",
 '''<div class="compare">
<figure><img src="media/char-mark.jpg" alt="Current Mark sheet: face in the portrait, front panel cut at the chin, face visible in the back panel"><figcaption><b>Current</b> approved 2 Nov · in use</figcaption></figure>
<figure><img src="media/mark-sheet-v2.jpg" alt="Upgraded Mark sheet: close-up portrait, then front and back full-body views cropped from the neck down on plain grey"><figcaption><b>Upgraded</b> draft 3 Nov · not in use</figcaption></figure>
</div>
<div class="card notes"><div class="info"><div class="chips"><span class="chip">GPT Image 2.5 · from Mark's approved source image</span><span class="chip new">New</span></div>
<h4>What changed</h4><ul>
<li>The portrait is the only face on the sheet, so video models have one face to copy instead of averaging several</li>
<li>Front and back views are cropped from the neck down and only carry the outfit and proportions</li>
<li>Plain mid-grey background, soft even light, neutral colour, empty hands</li>
<li>To check: a sliver of chin shows at the top of the front panel and a little hair on the back; a tighter crop would remove both</li>
<li>Next if approved: save it as a new Higgsfield Element (e.g. HTF-Mark-v2), then add a separate expression sheet</li>
</ul></div></div>''')
body=(
 section("community","Community &amp; Proof","40%","The founder, real traders and the community on camera. Every post invites people into the Discord.",
   '<h3>Founder talking head</h3>'+grid(proof)+refs([("Prop firm CEO on trader habits","https://www.tiktok.com/@elevatebasics/video/7229676115785207045"),("Trader story","https://www.tiktok.com/@ak.nq/video/7699491375506525470"),("\"Did you take W or L?\"","https://www.tiktok.com/@tizztrades/video/7702143469627723028"),("Street interview","https://www.tiktok.com/@chibotai/video/7701012021239680286")]))+
 section("entertainment","Entertainment","40%","Two recurring AI characters, Cyan and Mark, in tutorials, memes and ads, plus light, repeatable founder formats for Steve. The AI characters are always labelled as AI and never pose as customers.",
   ent_chars+'<h3>Tutorials</h3>'+grid(tut)+'<h3>Meme with AI character</h3>'+grid(memes+recreated[1:])+refs([("Expectation vs reality","https://www.tiktok.com/@maxsancho1/video/7699137365456981278"),("Trader-vs-family joke","https://www.tiktok.com/@vinc_nq/video/7698108253888089376"),("Market-day reaction","https://www.tiktok.com/@kojiro_0o/video/7696582759455657248")])+'<h3>Meme + caption</h3>'+grid(capmemes)+'<h3>Ads</h3>'+grid(ads)+'<h3>Founder tier list</h3><p class="desc" style="margin:-4px 0 14px">Steve ranks one trading topic from S to F (setups, habits, sessions) while the tier list fills in below him. Easy to run as a series, and every ranking gets people talking in the comments. No ranking other prop firms.</p><p class="lab" style="margin:0 0 10px">Examples from other creators, not Halcyon drafts</p>'+grid(tierlist)+'<h3>Founder reacts</h3><p class="desc" style="margin:-4px 0 14px">Steve reacts to something traders are already talking about: a viral trading clip (a blown account, a revenge trade, a flex) or a market headline (CPI, a Fed decision, a big move in the indices). It borrows the attention that\'s already there and shows how he thinks. Use TikTok stitch or duet so the original creator is credited, skip clips from other prop firms or ones that show earnings, and keep news takes to explaining what happened, with no predictions or trade calls.</p><p class="lab" style="margin:0 0 10px">Examples from other creators, not Halcyon drafts</p>'+grid([react[0],react[2],news[1]]))+
 section("education","Education","10%","Short explainers people save for later.",
   '<h3>Explainers</h3>'+grid(edu)+'<h3>Trade of the Week</h3><p class="desc" style="margin:-4px 0 14px">A weekly reel that tells one trader\'s trade as a calm process story: the setup, the wait, the entry, how it was managed, the exit. Same script and voice as the approved 18th Street series, in Halcyon\'s glow style. The result is shown in points, since a dollar figure reads as an earnings claim. This is an example trade for illustration; the real series needs the trader\'s written OK and their actual chart.</p>'+grid(totw)+refs([("Myth-buster","https://www.tiktok.com/@thequantbuilder/video/7699030814419422497"),("The math of an evaluation","https://www.tiktok.com/@diegotradez/video/7699193253261790478"),("Real-life metaphor","https://www.tiktok.com/@thedigital..lpn1/video/7697662424081681667")]))+
 section("promo","Promo","10%","One product or offer per post. Every price, rule and code is checked with Halcyon first.",
   '<h3>Ours: current draft plus 4 new motion options</h3><p class="desc" style="margin:-4px 0 14px">All four now use the glow-panel system from 18th Street (living background, glass panels, one hero at a time), recoloured to Halcyon cyan and Poppins. D keeps your original script in Halcyon\'s voice. Every change lands on the beat of its track. Backgrounds: aurora for A and B, candle field for C and D. Music is the three Sub Clair / Pixabay-style tracks you sent; confirm with Halcyon before posting, since their compliance doc asks for TikTok Commercial Music Library audio. Facts read from the site on 3 Nov; no prices shown.</p>'+grid(promo)+''+refs([("Rules explainer (prop firm)","https://www.tiktok.com/@fundednext/video/7694625035557932309")]))

)
page=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Halcyon content drafts</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box}}
html,body{{margin:0;background:#050505;color:#fff;font-family:Inter,Helvetica,Arial,sans-serif}}
a{{color:#00FBF4}}
header{{max-width:1180px;margin:0 auto;padding:36px 20px 8px}}
header .eyebrow{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#AFAFAF;margin:0 0 8px}}
header h1{{font-size:34px;margin:0 0 8px;letter-spacing:-.01em}}
header p{{color:#AFAFAF;margin:0;font-size:15px;max-width:760px;line-height:1.5}}
nav.tabs{{position:sticky;top:0;z-index:5;background:rgba(5,5,5,.92);backdrop-filter:blur(6px);border-bottom:1px solid #1d1d1d}}
nav.tabs div{{max-width:1180px;margin:0 auto;padding:12px 20px;display:flex;gap:8px;flex-wrap:wrap}}
nav.tabs a{{text-decoration:none;color:#fff;border:1px solid #2a2a2a;border-radius:999px;padding:8px 14px;font-size:14px;font-weight:600}}
nav.tabs a b{{color:#00FBF4;margin-left:6px}}
main{{max-width:1180px;margin:0 auto;padding:10px 20px 80px}}
section{{padding-top:34px}}
.sec-head{{display:flex;align-items:baseline;gap:12px}}
h2{{font-size:28px;margin:0}}
.share{{color:#00FBF4;font-weight:800;font-size:22px}}
.desc{{color:#AFAFAF;margin:6px 0 4px;font-size:15px}}
h3{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#AFAFAF;margin:26px 0 12px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:18px}}
.card{{background:#0c0c0c;border:1px solid #1f1f1f;border-radius:16px;overflow:hidden;display:flex;flex-direction:column}}
.media{{background:#000;aspect-ratio:9/16}}
.media video{{width:100%;height:100%;display:block;background:#000}}
.info{{padding:14px 16px 16px}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}}
.chip{{font-size:11px;font-weight:600;padding:4px 9px;border-radius:999px;border:1px solid #2c2c2c;color:#cfcfcf}}
.chip.ai{{border-color:#555;color:#fff}}
.chip.ok{{background:#00FBF4;color:#000;border-color:#00FBF4}}
.chip.warn{{border-color:#00FBF4;color:#00FBF4}}
.chip.hold{{border-color:#AFAFAF;color:#AFAFAF}}
.chip.bad{{background:#fff;color:#000;border-color:#fff}}
.chip.new{{background:#00FBF4;color:#000;border-color:#00FBF4}}
h4{{margin:0 0 4px;font-size:18px}}
.sub{{margin:0 0 10px;color:#AFAFAF;font-size:13px}}
.info ul{{margin:0;padding-left:18px;color:#ddd;font-size:13.5px;line-height:1.55}}
.refs{{margin-top:14px;font-size:13px;color:#AFAFAF;display:flex;flex-wrap:wrap;gap:6px 14px}}
.chars{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px;margin-top:18px}}
.chars figure{{margin:0;background:#0c0c0c;border:1px solid #1f1f1f;border-radius:16px;overflow:hidden}}
.chars img{{width:100%;display:block}}
.chars figcaption{{padding:12px 16px;font-size:14px;color:#AFAFAF}}.chars b{{color:#fff;margin-right:6px}}
.card.wide{{flex-direction:row;flex-wrap:wrap}}
.card.wide .phone{{flex:0 0 auto;width:min(400px,100%);padding:16px}}
.card.wide .info{{flex:1 1 320px}}
.viewport{{position:relative;width:100%;aspect-ratio:3/4;overflow:hidden;border-radius:12px;border:1px solid #222;background:#000;touch-action:pan-y}}
.track{{display:flex;height:100%;transition:transform .35s ease}}
.slide{{flex:0 0 100%;height:100%;position:relative;overflow:hidden}}
.scaler{{position:absolute;left:0;top:0;width:1080px;height:1440px;transform-origin:0 0}}
.nav{{position:absolute;top:50%;transform:translateY(-50%);width:44px;height:44px;border-radius:50%;border:1px solid #333;background:rgba(0,0,0,.6);color:#fff;font-size:22px;cursor:pointer}}
.nav:hover{{border-color:#00FBF4;color:#00FBF4}}.prev{{left:8px}}.next{{right:8px}}.nav[disabled]{{opacity:.25;cursor:default}}
.dots{{display:flex;gap:8px;justify-content:center;margin:12px 0 4px}}
.dot{{width:9px;height:9px;border-radius:50%;background:#333;border:0;padding:0;cursor:pointer}}.dot[aria-current="true"]{{background:#00FBF4}}
.count{{text-align:center;color:#AFAFAF;font-size:13px}}
.lab{{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#AFAFAF;margin:16px 0 8px}}
pre{{white-space:pre-wrap;background:#050505;border:1px solid #222;border-radius:12px;padding:14px;font:13.5px/1.55 Inter,Helvetica,Arial,sans-serif;margin:0}}
.copy{{margin-top:10px;background:#00FBF4;color:#000;border:0;border-radius:10px;padding:10px 16px;font-weight:700;font-size:14px;cursor:pointer}}
".compare{{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:18px;margin-top:18px}}
.compare figure{{margin:0;background:#0c0c0c;border:1px solid #1f1f1f;border-radius:16px;overflow:hidden}}
.compare img{{width:100%;display:block}}
.compare figcaption{{padding:12px 16px;font-size:14px;color:#AFAFAF}}.compare b{{color:#fff;margin-right:6px}}
.card.notes{{margin-top:18px}}
footer{{max-width:1180px;margin:0 auto;padding:0 20px 40px;color:#6f6f6f;font-size:13px}}
</style>
</head>
<body>
<header><p class="eyebrow">Halcyon Trader Funding · new TikTok account · Miren Partners</p>
<h1>Content drafts</h1>
<p>Every draft built so far from the content pillars brief, with its status and review notes from 3 Nov 2026. Reference posts belong to other creators and are linked to show the format works; we never copy them.</p></header>
<nav class="tabs" aria-label="Pillars"><div><a href="#community">Community &amp; Proof<b>40%</b></a><a href="#entertainment">Entertainment<b>40%</b></a><a href="#education">Education<b>10%</b></a><a href="#promo">Promo<b>10%</b></a></div></nav>
<main>{body}</main>
<footer>Halcyon offers simulated educational accounts. Results not guaranteed. T&amp;C apply.</footer>
<script>
(function(){{
  var track=document.getElementById('track'), vp=document.getElementById('vp');if(!track)return;
  var n=track.children.length, i=0, dots=document.getElementById('dots'), count=document.getElementById('count');
  for(var k=0;k<n;k++){{var b=document.createElement('button');b.className='dot';b.setAttribute('aria-label','Go to slide '+(k+1));(function(k){{b.onclick=function(){{go(k)}}}})(k);dots.appendChild(b);}}
  function fit(){{var s=vp.clientWidth/1080;Array.prototype.forEach.call(document.querySelectorAll('.scaler'),function(el){{el.style.transform='scale('+s+')'}});}}
  function go(k){{i=Math.max(0,Math.min(n-1,k));track.style.transform='translateX('+(-100*i)+'%)';
    Array.prototype.forEach.call(dots.children,function(d,j){{d.setAttribute('aria-current',j===i?'true':'false')}});
    count.textContent=(i+1)+' / '+n;document.getElementById('prev').disabled=i===0;document.getElementById('next').disabled=i===n-1;}}
  document.getElementById('prev').onclick=function(){{go(i-1)}};document.getElementById('next').onclick=function(){{go(i+1)}};
  vp.addEventListener('keydown',function(e){{if(e.key==='ArrowRight')go(i+1);if(e.key==='ArrowLeft')go(i-1);}});
  var x0=null;vp.addEventListener('touchstart',function(e){{x0=e.touches[0].clientX}},{{passive:true}});
  vp.addEventListener('touchend',function(e){{if(x0===null)return;var dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>40)go(i+(dx<0?1:-1));x0=null;}});
  window.addEventListener('resize',fit);fit();go(0);
  document.getElementById('copyBtn').onclick=function(){{var b=this;try{{navigator.clipboard.writeText(document.getElementById('cap').textContent).then(function(){{b.textContent='Copied'}},function(){{b.textContent='Select and copy the text above'}})}}catch(e){{b.textContent='Select and copy the text above'}}}};
}})();
</script>
</body>
</html>"""
open("site/index.html","w").write(page)
print(len(page))
