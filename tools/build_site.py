#!/usr/bin/env python3
"""Builds the static site for GitHub Pages from src/docs/*.md and copies assets.
Usage: python3 tools/build_site.py <assets_dir>
assets_dir holds the rendered images (pdf/img), the mock HTML (v2/prev) and the mood board (mood3/final.png).
The journey map, task flow and wireframes come from src/journey.html and src/wireframes.html."""
import markdown, pathlib, shutil, sys, html, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
A = pathlib.Path(sys.argv[1])

CSS = """
:root{--paper:#F3F6F9;--ink:#0B1726;--mute:#4D6074;--line:#D3DCE5;--teal:#0A7896;--cobalt:#2E4FD8;--card:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;font-size:16px;line-height:1.6;
 padding:0 max(16px,env(safe-area-inset-right)) 64px max(16px,env(safe-area-inset-left))}
.wrap{max-width:1040px;margin:0 auto}
nav.top{display:flex;gap:16px;flex-wrap:wrap;align-items:center;padding:20px 0;font-size:14px;border-bottom:1px solid var(--line)}
nav.top a{color:var(--teal);text-decoration:none;font-weight:500}nav.top a:hover{text-decoration:underline}
nav.top span{color:var(--mute)}
h1{font-size:clamp(1.9rem,4.5vw,2.6rem);line-height:1.12;margin:36px 0 12px;letter-spacing:-.02em;font-weight:700}
h2{font-size:1.35rem;margin:44px 0 8px;font-weight:650;letter-spacing:-.01em}
p,li{max-width:74ch}
img{max-width:100%;height:auto}
a{color:var(--teal)}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--card);margin:14px 0}
table{border-collapse:collapse;width:100%;min-width:640px;font-size:.92rem}
th,td{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}
th{font-size:.74rem;letter-spacing:.07em;text-transform:uppercase;color:var(--mute);background:var(--paper)}
tr:last-child td{border-bottom:0}
code,pre{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.88rem}
pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 14px;overflow-x:auto}
footer{margin-top:56px;padding-top:16px;border-top:1px solid var(--line);color:var(--mute);font-size:.88rem;font-family:Inter,system-ui,sans-serif}
"""
FOOTER = '<footer>Maya, L5 trip concierge by Aníbal Oliveira, 2026</footer>'
GC = '<script data-goatcounter="https://anibal.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>'
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
def page(title, body, depth=1, desc=""):
    up = "../" * depth
    nav = f'<nav class="top"><a href="{up}">Maya – L5 trip concierge</a><span>/</span><span>{html.escape(title)}</span></nav>' if depth else ""
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="icon" type="image/svg+xml" href="{up}assets/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="{up}assets/favicon-32.png"><link rel="apple-touch-icon" href="{up}assets/apple-touch-icon.png">
<title>{html.escape(title)} · Maya</title><meta name="description" content="{html.escape(desc)}">{FONT}<style>{CSS}</style></head>
<body><div class="wrap">{nav}{body}{FOOTER}</div>{GC}</body></html>'''

def md2html(src):
    h = markdown.markdown(src, extensions=["tables", "fenced_code", "sane_lists"])
    return re.sub(r"(<table>.*?</table>)", r'<div class="tw">\1</div>', h, flags=re.S)

DOCS = [("brief","Concept Foundations"),("hero","The Scenario"),("screens","Screen Specs and Mood Board"),
        ("matrix","Multimodal Matrix"),("edge","Edge Cases and Validation Plan")]
for slug, title in DOCS:
    out = ROOT / "docs" / slug; out.mkdir(parents=True, exist_ok=True)
    body = md2html((ROOT / "src/docs" / f"{slug}.md").read_text())
    (out / "index.html").write_text(page(title, body, 2))

# screens gallery
sc = ROOT / "screens"; (sc / "img").mkdir(parents=True, exist_ok=True); (sc / "live").mkdir(exist_ok=True); (sc / "project").mkdir(exist_ok=True)
IDS = [f"S{i:02d}" for i in range(1,21)] + [f"C{i}" for i in range(1,6)] + ["V1","V2"]
NAMES = {"S01":"Sign in","S02":"Welcome","S03":"Maya's access","S04":"Briefing: listening","S05":"Briefing: keyboard","S06":"Briefing: Maya asks","S07":"Briefing: building the plan",
 "S08":"Retailer calls","S09":"Plan change: automatic","S10":"Gift suggestion","S11":"Florist order","S12":"Plan overview","S13":"Vehicle intent","S14":"Active trip","S15":"Edit plan",
 "S16":"Incoming call","S17":"Plan change: ambient","S18":"Errand suggestion","S19":"Errand booked","S20":"Arrival report","C1":"Leaving in courier mode","C2":"Phone: courier run",
 "C3":"Phone: errand report","C4":"Errands","C5":"New errand","V1":"Takeover request (variant)","V2":"Running late (variant)"}
live = {p.name.split("-")[0]: p.name for p in (A/"v2/prev").glob("*.html")}
if (A/"v2/prev/Main.html").exists(): live["S01"] = "Main.html"  # S01 Sign in is rendered from Main.html
cards = ""
for i in IDS:
    for suf in ("", "_m"):
        shutil.copy(A/f"pdf/img/{i}{suf}.jpg", sc/"img"/f"{i}{suf}.jpg")
    lv = f' · <a href="live/{live[i]}">live page</a>' if i in live else ""
    ph = ""
    if i in ("C2","C3"):
        shutil.copy(A/f"pdf/img/{i}_phone.jpg", sc/"img"/f"{i}_phone.jpg"); ph = f' · <a href="img/{i}_phone.jpg">phone view</a>'
    cards += f'<figure><a href="img/{i}.jpg"><img loading="lazy" src="img/{i}_m.jpg" alt="{i} {html.escape(NAMES[i])}"></a><figcaption><b>{i}</b> {html.escape(NAMES[i])}{lv}{ph}</figcaption></figure>'
for f in (A/"v2/prev").glob("*.html"): shutil.copy(f, sc/"live"/f.name)
shutil.copy(A/"v2/deep-map.svg", sc/"project"/"deep-map.svg")
TABS = [("", "Screens"), ("components/", "Central Display Components"), ("panoramic/", "Panoramic Vision")]
TAB_CSS = "<style>.tabs{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 6px}.tabs a{padding:9px 16px;border:1px solid var(--line);background:var(--card);color:var(--ink);text-decoration:none;font-weight:500;font-size:.95rem}.tabs a.on{background:var(--ink);border-color:var(--ink);color:#fff}.tabs a:hover{border-color:var(--teal)}.board{display:block;width:100%;height:auto;margin-top:18px;border:1px solid var(--line);background:#020812}</style>"
def tabs(cur, up):
    return '<nav class="tabs" aria-label="UI Design Artboard">' + "".join(f'<a href="{up}{u}" class="{"on" if u == cur else ""}">{t}</a>' for u, t in TABS) + "</nav>"
g_css = "<style>.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-top:20px}figure{margin:0}figure img{width:100%;height:auto;display:block;border:1px solid var(--line);background:#020812}figcaption{font-size:.88rem;margin-top:6px;color:var(--mute)}figcaption b{color:var(--ink)}</style>"
body = g_css + TAB_CSS + '<h1>UI Design Artboard</h1>' + tabs("", "") + f'<div class="grid">{cards}</div>'
(sc/"index.html").write_text(page("UI Design Artboard", body, 1))
for slug, title, img, live_f in (("components", "Central Display Components", "components.jpg", "Components.html"), ("panoramic", "Panoramic Vision", "panoramic.jpg", "Strip.html")):
    d = sc / slug; d.mkdir(exist_ok=True)
    body = TAB_CSS + '<h1>UI Design Artboard</h1>' + tabs(slug + "/", "../") + f'<p><a href="../live/{live_f}">Open the live page</a> · <a href="../img/{img}">Full-size image</a></p><img class="board" src="../img/{img}" alt="{title}">'
    (d/"index.html").write_text(page(title, body, 2))

# mood board image (shown on the Screen Specs and Mood Board page)
md = ROOT/"mood"; md.mkdir(exist_ok=True); shutil.copy(A/"mood3/final.png", md/"mood-board.png")
if (md/"index.html").exists(): (md/"index.html").unlink()

# journey map, task flow, wireframes: standalone pages with the same back link and footer
FAV = '<link rel="icon" type="image/svg+xml" href="../assets/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="../assets/favicon-32.png"><link rel="apple-touch-icon" href="../assets/apple-touch-icon.png">'
BACK = '<p style="margin:0;padding:10px 16px;font:14px Inter,system-ui,sans-serif;background:#F3F6F9;border-bottom:1px solid #D3DCE5"><a href="../" style="color:#0A7896">&larr; Maya – L5 trip concierge</a></p>'
FOOT_SA = '<footer style="max-width:1180px;margin:40px auto 0;padding:16px 20px 40px;border-top:1px solid #D3DCE5;color:#4D6074;font:14px Inter,system-ui,sans-serif">Maya, L5 trip concierge by Aníbal Oliveira, 2026</footer>'
def finish(slug, h):
    d = ROOT/slug; d.mkdir(exist_ok=True)
    h = re.sub(r"<!--claude-mermaid-runtime-begin.*?<!--claude-mermaid-runtime-end-->", "", h, flags=re.S)
    if "favicon.svg" not in h: h = re.sub(r"(<meta charset=[\"']?utf-?8[\"']?>)", lambda m: m.group(1) + FAV, h, count=1, flags=re.I)
    h = re.sub(r"(<body[^>]*>)", lambda m: m.group(1) + BACK, h, count=1)
    h = h.replace("</body>", FOOT_SA + "\n" + GC + "\n</body>", 1)
    (d/"index.html").write_text(h)
J = (ROOT/"src/journey.html").read_text()
a = J.index('<h2>Task flow</h2>'); b = J.index('<p class="note">')
c = J.index('</p>', b) + 4
journey = J[:a] + J[c:]
journey = re.sub(r'<script type="module">.*?</script>', '', journey, flags=re.S)
journey = journey.replace('<title>Maya: Journey map and task flow</title>', '<title>Journey Map · Maya</title>').replace('<h1>Maya: journey map and task flow</h1>', '<h1>Maya: journey map</h1>')
finish("journey", journey)
m0 = J.index('<main>'); m1 = J.index('</main>')
head = J[:m0]; tail = J[m1:]
flow_main = '<main>\n<h1>Maya: task flow</h1>\n' + J[a:c].replace('<h2>Task flow</h2>', '') + '\n'
flow_main = re.sub(r'<pre class="mermaid">.*?</pre>', '<img src="flow.svg" alt="Task flow: every decision behind the evening" style="display:block;max-width:100%;height:auto;margin:0 auto">', flow_main, flags=re.S)
tail = re.sub(r'<script type="module">.*?</script>', '', tail, flags=re.S)
flow = head.replace('<title>Maya: Journey map and task flow</title>', '<title>Task Flow · Maya</title>') + flow_main + re.sub(r'<script>\s*var B=.*?</script>', '', tail, count=1, flags=re.S)
finish("flow", flow)
finish("wireframes", (ROOT/"src/wireframes.html").read_text())

# entry page
FACES = ''.join("@font-face{font-family:'InterDoc';src:url('assets/fonts/Inter-%s.woff') format('woff');font-weight:%d;font-display:swap}" % (n, w) for n, w in (('ExtraLight', 200), ('Light', 300), ('Regular', 400), ('Medium', 500), ('SemiBold', 600)))
ITEMS = [("docs/brief/", "Concept Foundations", "Problem, vision, hypothesis, scope, success metrics, assumptions, design principles, conversation rules and trade-offs."),
 ("docs/hero/", "The Scenario", "One evening in ten scenes: the day in numbers and the full script."),
 ("journey/", "Journey Map", "Ten beats from sign-in to the empty car charging, with what Maya does backstage."),
 ("flow/", "Task Flow", "Every decision behind the evening: replans, ambient intent and the courier hand-off."),
 ("docs/screens/", "Screen Specs and Mood Board", "S01 to S20, C1 to C5 and variants, Panoramic Vision through the story, and the Deep ocean mood board."),
 ("docs/matrix/", "Multimodal Matrix", "Voice, touch, Panoramic Vision, chime and phone: parity, outputs and stress tests."),
 ("docs/edge/", "Edge Cases and Validation Plan", "Seventeen edge cases and six tests tied to the assumptions."),
 ("wireframes/", "Central Display Wireframes", "Greyscale layout, interaction patterns and components, drawn before the hi-fi screens."),
 ("screens/", "UI Design Artboard", "Every screen at 1920 × 1200, the Central Display components and Panoramic Vision."),
 ("prototype/", "Clickable Prototype", "The whole evening by touch or voice, with edge cases 1 to 4 as what-if branches.")]
cards = "".join(f'<a class="item" href="{u}"><b>{html.escape(t)}</b><span>{html.escape(d)}</span></a>' for u, t, d in ITEMS)
(ROOT/"index.html").write_text(f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maya – L5 trip concierge</title><meta name="description" content="Maya, an L5 trip concierge. A UX challenge by Aníbal Oliveira.">
{FONT}<style>
:root{{--paper:#F3F6F9;--ink:#0B1726;--mute:#4D6074;--line:#D3DCE5;--teal:#0A7896;--card:#fff}}
{FACES}*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font-family:InterDoc,Inter,system-ui,sans-serif;line-height:1.6;padding:0 max(16px,env(safe-area-inset-right)) 64px max(16px,env(safe-area-inset-left))}}
.hero{{position:relative;overflow:hidden;background:url(assets/hero-bg.jpg) center/cover no-repeat,#020812;margin:0 calc(-1*max(16px,env(safe-area-inset-left)));padding:clamp(28px,6vw,72px) max(16px,env(safe-area-inset-left));min-height:min(62.5vw,820px);display:flex;align-items:center}}
.w{{max-width:1040px;margin:0 auto;width:100%}}
.hero video{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0}}.hero .w{{position:relative;z-index:1}}
@media (prefers-reduced-motion:reduce){{.hero video{{display:none}}}}
.glass{{max-width:680px;background:rgba(2,8,18,.74);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);padding:clamp(22px,3.4vw,40px);color:#E6F1F8}}
.kicker{{color:#5CD6F2;font-size:13px;letter-spacing:.16em;text-transform:uppercase;font-weight:600}}
h1{{font-size:clamp(3.8rem,10vw,6.6rem);line-height:.92;margin:18px 0 14px;letter-spacing:-.05em;font-weight:200}}
.sub{{font-size:clamp(1.35rem,3vw,1.9rem);font-weight:300;line-height:1.2;margin:0 0 20px;color:#E6F1F8}}
.glass p.intro{{color:#C3D1DD;margin:0 0 12px;font-size:16.5px;line-height:1.55;font-weight:400;text-wrap:pretty}}
.btns{{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}}
.btn{{display:inline-flex;align-items:center;background:#5CD6F2;color:#020812;padding:12px 20px;font-weight:600;text-decoration:none;min-height:48px}}
.btn.o{{background:rgba(2,8,18,.4);color:#5CD6F2;border:1px solid #5CD6F2}}
h2{{font-size:1.3rem;margin:44px 0 14px}}
.list{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,460px),1fr));gap:12px}}
.item{{display:block;background:var(--card);border:1px solid var(--line);padding:16px 20px;text-decoration:none;color:inherit}}
.item:hover{{border-color:var(--teal)}}.item b{{display:block}}.item span{{display:block;margin-top:2px;color:var(--mute);font-size:.92rem}}
footer{{margin-top:56px;padding-top:16px;border-top:1px solid var(--line);color:var(--mute);font-size:.88rem}}
</style></head><body>
<div class="hero"><video autoplay muted loop playsinline preload="auto" poster="assets/hero-bg.jpg" aria-hidden="true" tabindex="-1"><source src="assets/hero-loop.webm" type="video/webm"><source src="assets/hero-loop.mp4" type="video/mp4"></video><div class="w"><div class="glass"><div class="kicker">UX challenge · New AI assistant for infotainment</div>
<h1>Maya</h1><p class="sub">L5 trip concierge</p>
<p class="intro">A self-driving car frees your hands, not your agenda. Navigation handles routes, not commitments, so passengers still sequence the stops, phone businesses and replan whenever something changes.</p>
<p class="intro">With Maya, you share your needs and goals and she plans the stops, confirms with the shops, pays from her wallet and adapts when conditions change. Everything is shown on your Central Display and Panoramic Vision.</p>
<p class="intro">When the car is free, she becomes the courier that runs your errands.</p>
<div class="btns"><a class="btn" href="Anibal-Oliveira_CTW-UX-Challenge_Maya.pdf" download target="_blank" rel="noopener" data-goatcounter-click="pdf-download" data-goatcounter-title="PDF download">Get the PDF</a><a class="btn o" href="prototype/">Open the prototype</a><a class="btn o" href="screens/">UI Design Artboard</a></div></div></div></div>
<div class="w" style="padding-top:44px">
<div class="list">{cards}</div>
{FOOTER}</div>
{GC}
</body></html>''')
