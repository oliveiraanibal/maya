// node tools/hero-loop/render.js [--test t1 t2 ...]   renders the loop to assets/hero-loop.mp4 + .webm (+ poster)
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const ROOT = path.resolve(__dirname, '../..'), OUT = process.env.HERO_TMP || path.join(require('os').tmpdir(), 'hero-loop-frames');
(async () => {
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: 1920, height: 1200 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.join(__dirname, 'index.html')); await p.evaluate(() => window.ready);
  const total = await p.evaluate(() => window.TOTAL); console.log('duration', total.toFixed(1), 's');
  const test = process.argv.indexOf('--test');
  if (test > -1) { for (const t of process.argv.slice(test + 1).map(Number)) { await p.evaluate(t => window.frame(t), t); await p.screenshot({ path: path.join(OUT + '_t' + t.toFixed(1) + '.png') }); } await b.close(); return; }
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true });
  const N = Math.round(total * 30);
  for (let i = 0; i < N; i++) { await p.evaluate(t => window.frame(t), i / 30); await p.screenshot({ path: path.join(OUT, String(i).padStart(5, '0') + '.jpg'), type: 'jpeg', quality: 93 }); }
  await b.close();
  const f = path.join(OUT, '%05d.jpg');
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', '30', '-i', f, '-c:v', 'libx264', '-preset', 'slow', '-crf', '24', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-an', path.join(ROOT, 'assets/hero-loop.mp4')]);
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', '30', '-i', f, '-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', '37', '-pix_fmt', 'yuv420p', '-an', path.join(ROOT, 'assets/hero-loop.webm')]);
  console.log('done', N, 'frames');
})();
