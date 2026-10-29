#!/usr/bin/env python3
"""Builds tools/hero-loop/index.html: the Porto map animated through the whole scenario (map only: no panel, top bar or dock).
It reuses the CSS, map and the exact route polylines of the hi-fi screens in screens/live, so it stays in step with the mocks.
Then run: node tools/hero-loop/render.js  (writes assets/hero-loop.mp4, .webm and the poster)."""
import re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
LIVE = ROOT / "screens/live"

def rt_paths(name):
    t = (LIVE / name).read_text()
    i = t.index('<svg class="rt"'); j = t.index('</svg>', i)
    return [(d, c) for d, c in re.findall(r'<path d="([^"]+)"[^>]*?(?:stroke="([^"]+)")', t[i:j])]

def pick(name, color, nth=0):
    return [d for d, c in rt_paths(name) if c == color][nth]

join = lambda a, b: a + " " + re.sub(r"^M[\d.\-]+,[\d.\-]+ ", "", b)
D = {
  "home":    join(pick("S02-Welcome.html", "#3E4F60"), pick("S02-Welcome.html", "#5CD6F2")),   # default route "Going home"
  "v1":      join(pick("S12-Plan.html", "#3E4F60"), pick("S12-Plan.html", "#5CD6F2")),          # the first plan (via home)
  "final":   pick("S20-Arrival.html", "#5CD6F2"),                                               # plan after the pharmacy and hair-salon changes
  "courier": pick("S20-Arrival.html", "#7E9BFF"),                                               # the empty car to the dry cleaner
}
css = re.search(r"<style>(.*?)</style>", (LIVE / "S12-Plan.html").read_text(), re.S).group(1)
css = re.sub(r"@import[^;]*;", "", css)
faces = "".join("@font-face{font-family:Inter;src:url('../../assets/fonts/Inter-%s.woff') format('woff');font-weight:%d}" % (n, w)
                for n, w in (("ExtraLight", 200), ("Light", 300), ("Regular", 400), ("Medium", 500), ("SemiBold", 600)))
css = css.replace("url(../project/deep-map.svg)", "url(../../screens/project/deep-map.svg)")
js = (pathlib.Path(__file__).parent / "scene.js").read_text()
html = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Maya hero loop</title>
<style>{faces}{css}
html,body{{margin:0;background:#020812}}.d5 .vig{{z-index:5}}
.d5 .lay{{position:absolute;inset:0}}
</style></head><body>
<div class="d5" id="stage"><div class="map"></div><div class="glow"></div>
<svg class="rt" id="rt" viewBox="0 0 1280 800"></svg>
<span class="lb" style="left:876px;top:646px">BOAVISTA</span><span class="lb" style="left:1370px;top:419px">PARANHOS</span>
<span class="lb" style="left:1607px;top:820px">BONFIM</span><span class="lb" style="left:935px;top:1009px">VILA NOVA DE GAIA</span>
<span class="lb rv" style="left:727px;top:908px">Rio Douro</span>
<span class="sh" style="left:641px;top:341px">A28</span><span class="sh" style="left:1393px;top:104px">A3</span><span class="sh" style="left:1878px;top:379px">A4</span>
<div class="lay" id="pins"></div>
<svg class="car" id="car" viewBox="0 0 40 40"><path id="carp" d="M20 4 L33 34 L20 27 L7 34 Z" fill="#FFFFFF" stroke="#02121C" stroke-width="2" stroke-linejoin="miter"/></svg>
<span class="lb oc" style="left:190px;top:1000px">Oceano Atlântico</span>
<div class="vig"></div></div>
<script>const DATA={json.dumps(D)};</script><script>{js}</script></body></html>"""
(pathlib.Path(__file__).parent / "index.html").write_text(html)
print("ok", {k: len(v) for k, v in D.items()}, len(html))
