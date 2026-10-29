// Renders images the site needs that are not screens:
//   assets/hero-bg.jpg            entry page hero: S09's map and route only (hidden from the artboard and the prototype)
//   screens/img/components.jpg    full Central Display Components board (from screens/live/Components.html)
//   screens/img/panoramic.jpg     full Panoramic Vision board (from screens/live/Strip.html)
// Run: node tools/render_assets.js
const { chromium } = require('playwright');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const live = (f) => 'file://' + path.join(ROOT, 'screens/live', f);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1200 } });
  await p.goto(live('S09-ChangeAuto.html')); await p.waitForTimeout(600);
  await p.addStyleTag({ content: '.pl,.dk,.brand,.clock,.zm{display:none!important}' }); await p.waitForTimeout(200);
  await p.screenshot({ path: path.join(ROOT, 'assets/hero-bg.jpg'), type: 'jpeg', quality: 86 });
  await p.goto(live('Components.html')); await p.waitForTimeout(600);
  await p.screenshot({ path: path.join(ROOT, 'screens/img/components.jpg'), type: 'jpeg', quality: 88, fullPage: true });
  const q = await b.newPage({ viewport: { width: 2560, height: 1200 } });
  await q.goto(live('Strip.html')); await q.waitForTimeout(500);
  const h = await q.evaluate(() => { const s = document.querySelector('.sx'); s.style.height = 'auto'; return s.scrollHeight; });
  await q.setViewportSize({ width: 2560, height: h });
  await q.screenshot({ path: path.join(ROOT, 'screens/img/panoramic.jpg'), type: 'jpeg', quality: 88 });
  await b.close();
})();
