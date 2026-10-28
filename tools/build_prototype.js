#!/usr/bin/env node
// Builds the prototype's generated files from prototype/flow.json and the mock HTML in screens/live.
//   prototype/shots/<ID>.jpg    screenshot of each mock at 1920 x 1200
//   prototype/zones.json        tap zones (x, y, w, h) found in each mock
//   prototype/mocks/*.html      derived variants (edge cases), built from a base mock plus text replacements
// Run: npm run proto            (everything)
//      npm run proto -- S14 S17 (only these screens)
// It fails loudly if a hotspot can't be found, a text replacement doesn't match, or a link goes nowhere.
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');

const ROOT = path.resolve(__dirname, '..');
const P = path.join(ROOT, 'prototype');
const flow = JSON.parse(fs.readFileSync(path.join(P, 'flow.json'), 'utf8'));
const [W, H] = flow.size;
const MIN = 76; // minimum tap size in px (Android for Cars), see the Decision Log
const only = process.argv.slice(2);
const errors = [];

// 1. validate links ------------------------------------------------------------------------------
const ids = Object.keys(flow.screens);
const targets = (s) => [s.cta && s.cta.go, s.auto && s.auto.go, ...(s.hotspots || []).map(h => h.go), ...(s.branches || []).map(b => b.go)].filter(Boolean);
for (const id of ids) for (const t of targets(flow.screens[id]))
  if (t !== 'back' && !flow.screens[t]) errors.push(`${id}: link to unknown screen "${t}"`);
const seen = new Set(), queue = [flow.start];
while (queue.length) { const id = queue.shift(); if (seen.has(id) || !flow.screens[id]) continue; seen.add(id);
  const s = flow.screens[id]; targets(s).forEach(t => queue.push(t));
  if (!(flow.global.except || []).includes(id)) (flow.global.hotspots || []).forEach(h => queue.push(h.go)); }
for (const id of ids) if (!seen.has(id)) errors.push(`${id}: no way to reach this screen from "${flow.start}"`);

// 2. derived variants ----------------------------------------------------------------------------
fs.mkdirSync(path.join(P, 'mocks'), { recursive: true });
fs.mkdirSync(path.join(P, 'shots'), { recursive: true });
fs.mkdirSync(path.join(P, 'project'), { recursive: true });
fs.copyFileSync(path.join(ROOT, 'screens/project/deep-map.svg'), path.join(P, 'project/deep-map.svg'));
for (const [vid, v] of Object.entries(flow.variants || {})) {
  let html = fs.readFileSync(path.join(ROOT, flow.mockDir, v.base), 'utf8');
  for (const [from, to] of v.replace) {
    if (!html.includes(from)) { errors.push(`variant ${vid}: text not found in ${v.base}: ${from.slice(0, 70)}...  (the base mock changed: update "replace" in flow.json)`); continue; }
    html = html.replace(from, () => to);
  }
  fs.writeFileSync(path.join(P, 'mocks', `${vid}.html`), html);
}
const mockFile = (id) => { const s = flow.screens[id];
  return s.variant ? path.join(P, 'mocks', `${s.variant}.html`) : path.join(ROOT, flow.mockDir, s.mock); };

// 3. screenshots and zones -----------------------------------------------------------------------
(async () => {
  const zonesPath = path.join(P, 'zones.json');
  const zones = fs.existsSync(zonesPath) ? JSON.parse(fs.readFileSync(zonesPath, 'utf8')) : {};
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: W, height: H } });
  const clamp = (r) => { let [x, y, w, h] = r;
    if (w < MIN) { x -= (MIN - w) / 2; w = MIN; } if (h < MIN) { y -= (MIN - h) / 2; h = MIN; }
    x = Math.max(0, Math.min(W - w, x)); y = Math.max(0, Math.min(H - h, y)); return [x, y, w, h].map(Math.round); };

  const find = async (id, hs) => {
    const f = hs.find;
    if (hs.rect) return clamp(hs.rect);
    if (!f) { errors.push(`${id}/${hs.id}: needs "find" or "rect"`); return null; }
    if (f.rect) return clamp(f.rect);
    let loc = f.sel ? page.locator(f.sel) : page.getByText(f.text, { exact: f.exact !== false });
    const n = await loc.count();
    if (n === 0) { errors.push(`${id}/${hs.id}: nothing found for ${JSON.stringify(f)}`); return null; }
    const box = await loc.nth(f.nth || 0).boundingBox();
    if (!box) { errors.push(`${id}/${hs.id}: found but not visible: ${JSON.stringify(f)}`); return null; }
    const pad = f.pad || 0;
    return clamp([box.x - pad, box.y - pad, box.width + 2 * pad, box.height + 2 * pad]);
  };

  for (const id of ids) {
    if (only.length && !only.includes(id)) continue;
    const s = flow.screens[id];
    if (s.image) { // a plain image instead of a mock: only explicit rects can be used
      fs.copyFileSync(path.join(P, s.image), path.join(P, 'shots', `${id}.jpg`));
    } else {
      const file = mockFile(id);
      if (!fs.existsSync(file)) { errors.push(`${id}: mock not found: ${file}`); continue; }
      await page.goto('file://' + file); await page.waitForTimeout(500);
      await page.evaluate(() => document.fonts && document.fonts.ready);
      await page.screenshot({ path: path.join(P, 'shots', `${id}.jpg`), type: 'jpeg', quality: 88 });
    }
    const z = {};
    const all = [...(s.hotspots || []), ...(flow.global.except.includes(id) ? [] : flow.global.hotspots || [])];
    for (const hs of all) { if (s.image && !hs.rect && !(hs.find && hs.find.rect)) continue; const r = await find(id, hs); if (r) z[hs.id] = r; }
    zones[id] = z;
    console.log(`${id.padEnd(4)} ${Object.keys(z).length} zones`);
  }
  await browser.close();
  // drop zones of screens that no longer exist
  for (const k of Object.keys(zones)) if (!flow.screens[k]) delete zones[k];
  fs.writeFileSync(zonesPath, JSON.stringify(zones, null, 1));
  if (errors.length) { console.error('\nProblems:\n - ' + errors.join('\n - ')); process.exit(1); }
  console.log('\nOK: ' + ids.length + ' screens, all links resolve, every screen is reachable.');
})();
