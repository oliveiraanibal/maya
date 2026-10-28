#!/usr/bin/env python3
"""Builds the static site for GitHub Pages from src/docs/*.md and copies assets.
Usage: python3 tools/build_site.py <assets_dir>   (assets_dir holds screens, mood, journey, wireframes sources)"""
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
a{color:var(--teal)}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:8px;background:var(--card);margin:14px 0}
table{border-collapse:collapse;width:100%;min-width:640px;font-size:.92rem}
th,td{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}
th{font-size:.74rem;letter-spacing:.07em;text-transform:uppercase;color:var(--mute);background:var(--paper)}
tr:last-child td{border-bottom:0}
code,pre{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.88rem}
pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 14px;overflow-x:auto}
footer{margin-top:56px;padding-top:16px;border-top:1px solid var(--line);color:var(--mute);font-size:.88rem}
"""
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'
def page(title, body, depth=1, desc=""):
    up = "../" * depth
    nav = f'<nav class="top"><a href="{up}">Maya · process index</a><span>/</span><span>{html.escape(title)}</span></nav>' if depth else ""
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Maya</title><meta name="description" content="{html.escape(desc)}">{FONT}<style>{CSS}</style></head>
<body><div class="wrap">{nav}{body}<footer>Aníbal Oliveira · CTW UX challenge · Maya, an AI trip concierge for a Level 5 car</footer></div></body></html>'''

def md2html(src):
    h = markdown.markdown(src, extensions=["tables", "fenced_code", "sane_lists"])
    return re.sub(r"(<table>.*?</table>)", r'<div class="tw">\1</div>', h, flags=re.S)

DOCS = [("brief","Hypothesis and Assumptions"),("hero","Hero Scenario and Conversation Script"),("screens","Screen Plan and Strip Specification"),
        ("matrix","Multimodal Matrix"),("edge","Edge Cases and Validation Plan"),("decisions","Decision Log and Trade-offs")]
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
extra = '<p>Also live: <a href="live/Components.html">component inventory</a> · <a href="live/Strip.html">LED strip states</a></p>'
g_css = "<style>.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-top:20px}figure{margin:0}figure img{width:100%;height:auto;display:block;border:1px solid var(--line);background:#020812}figcaption{font-size:.88rem;margin-top:6px;color:var(--mute)}figcaption b{color:var(--ink)}</style>"
body = g_css + '<h1>Hi-fi screens</h1><p>Every screen in story order: S01 to S20 in the car, C1 to C5 for courier mode, V1 and V2 for variants. Tablet canvas 1920 × 1200, Deep ocean. Click an image for full size; “live page” opens the screen as HTML.</p>' + extra + f'<div class="grid">{cards}</div>'
(sc/"index.html").write_text(page("Hi-fi screens", body, 1))

# mood board
md = ROOT/"mood"; md.mkdir(exist_ok=True); shutil.copy(A/"mood3/final.png", md/"mood-board.png")
(md/"index.html").write_text(page("Mood board", '<h1>Mood board</h1><p>The final direction, Deep ocean: dark first, a blue-green ground with cobalt and lumen glows, inspired by The Abyss.</p><p><a href="mood-board.png">Open full size</a></p><img src="mood-board.png" alt="Mood board: Deep ocean" style="max-width:100%;height:auto;border:1px solid var(--line)">', 1))

# journey + wireframes (standalone pages, copied)
def standalone(slug, src, title):
    d = ROOT/slug; d.mkdir(exist_ok=True)
    h = pathlib.Path(src).read_text()
    h = re.sub(r"<!--claude-mermaid-runtime-begin.*?<!--claude-mermaid-runtime-end-->", "", h, flags=re.S)
    back = '<p style="margin:0;padding:10px 16px;font:14px Inter,system-ui,sans-serif;background:#F3F6F9;border-bottom:1px solid #D3DCE5"><a href="../" style="color:#0A7896">&larr; Maya · process index</a></p>'
    h = re.sub(r"(<body[^>]*>)", r"\1"+back.replace("\\","\\\\"), h, count=1) if "<body" in h else back+h
    (d/"index.html").write_text(h)
standalone("journey", sys.argv[2], "Journey map and task flow")
standalone("wireframes", sys.argv[3], "Tablet wireframes")
