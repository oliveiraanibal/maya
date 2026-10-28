// Lists visible text elements and their boxes for a mock, to help write hotspots in prototype/flow.json
// usage: node tools/dump_texts.js screens/live/S14-Trip.html
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1200 } });
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + require('path').resolve(f)); await p.waitForTimeout(300);
    const items = await p.evaluate(() => {
      const out = [];
      for (const el of document.querySelectorAll('body *')) {
        if (el.children.length) continue;
        const t = (el.textContent || '').trim().replace(/\s+/g, ' ');
        if (!t || t.length > 46) continue;
        const r = el.getBoundingClientRect();
        if (r.width < 4 || r.height < 4 || r.x > 1920 || r.y > 1200) continue;
        out.push(`${t} @${Math.round(r.x)},${Math.round(r.y)} ${Math.round(r.width)}x${Math.round(r.height)}`);
      }
      return out;
    });
    console.log('## ' + f + '\n' + items.join('\n'));
  }
  await b.close();
})();
