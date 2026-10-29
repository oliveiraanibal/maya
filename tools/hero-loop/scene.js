// Deterministic timeline: window.frame(t) draws the map story at time t (seconds). No panel, top bar or dock.
const K = 2.1, OX = -724, OY = -272;                       // map zoom used by every screen (px = K * map + offset)
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const seg = (t, a, b) => clamp((t - a) / (b - a));
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
const eo = x => 1 - Math.pow(1 - clamp(x), 3);
const sine = x => .5 - .5 * Math.cos(Math.PI * clamp(x));

class Path {
  constructor(d) {
    this.p = d.match(/[ML]\s*-?[\d.]+,-?[\d.]+/g).map(s => s.replace(/[ML]\s*/, '').split(',').map(Number));
    this.c = [0]; for (let i = 1; i < this.p.length; i++) this.c.push(this.c[i - 1] + Math.hypot(this.p[i][0] - this.p[i - 1][0], this.p[i][1] - this.p[i - 1][1]));
    this.L = this.c[this.c.length - 1];
  }
  idx(s) { let lo = 0, hi = this.c.length - 1; while (hi - lo > 1) { const m = (lo + hi) >> 1; if (this.c[m] <= s) lo = m; else hi = m; } return lo; }
  at(s) { s = clamp(s, 0, this.L); const i = this.idx(s), a = this.p[i], b = this.p[Math.min(i + 1, this.p.length - 1)], l = this.c[i + 1] - this.c[i] || 1, u = (s - this.c[i]) / l; return [a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u]; }
  head(s) { const a = this.at(s - 7), b = this.at(s + 7); return Math.atan2(b[1] - a[1], b[0] - a[0]) * 180 / Math.PI + 90; }
  sub(a, b) { a = clamp(a, 0, this.L); b = clamp(b, 0, this.L); if (b - a < .05) return ''; const pts = [this.at(a)]; for (let i = this.idx(a) + 1; i < this.p.length && this.c[i] < b; i++) if (this.c[i] > a) pts.push(this.p[i]); pts.push(this.at(b)); return 'M' + pts.map(q => q[0].toFixed(1) + ',' + q[1].toFixed(1)).join(' L'); }
  near(x, y, min = 0) { let best = 1e9, bs = 0; for (let i = 0; i < this.p.length; i++) { if (this.c[i] < min) continue; const d = Math.hypot(this.p[i][0] - x, this.p[i][1] - y); if (d < best) { best = d; bs = this.c[i]; } } return bs; }
}
const Pm = (x, y) => [K * x + OX, K * y + OY];             // map units -> px
const HOME = new Path(DATA.home), V1 = new Path(DATA.v1), FIN = new Path(DATA.final), COU = new Path(DATA.courier);

// ---------- route layers
const rt = document.getElementById('rt');
rt.insertAdjacentHTML('beforeend', '<defs><filter id="rg" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="4.3"/></filter></defs>');
const mk = (attrs) => { const e = document.createElementNS('http://www.w3.org/2000/svg', 'path'); e.setAttribute('fill', 'none'); e.setAttribute('stroke-linecap', 'round'); e.setAttribute('stroke-linejoin', 'round'); for (const k in attrs) e.setAttribute(k, attrs[k]); rt.appendChild(e); return e; };
const glow = (op = 1) => [mk({ stroke: '#3D63FF', 'stroke-opacity': .55 * op, 'stroke-width': 11.4, filter: 'url(#rg)' }), mk({ stroke: '#5CD6F2', 'stroke-opacity': op, 'stroke-width': 3.2 }), mk({ stroke: '#E9FBFF', 'stroke-opacity': .7 * op, 'stroke-width': .86 })];
const setG = (g, d, a) => g.forEach((e, i) => { e.setAttribute('d', d); e.style.opacity = a; });
const past = mk({ stroke: '#3E4F60', 'stroke-width': 3.6 });
const old = mk({ stroke: '#7B8D9E', 'stroke-opacity': .7, 'stroke-width': 1.6, 'stroke-dasharray': '.5 4' });
const gHome = glow(), gV1 = glow(), gFin = glow();
const cglow = mk({ stroke: '#3D63FF', 'stroke-opacity': .45, 'stroke-width': 5.7, filter: 'url(#rg)' });
const cdash = mk({ stroke: '#7E9BFF', 'stroke-width': 1.9, 'stroke-dasharray': '3.3 3.3', 'stroke-linecap': 'butt' });
const florl = mk({ stroke: '#5CD6F2', 'stroke-opacity': .75, 'stroke-width': 1.43, 'stroke-dasharray': '1.4 4.3' });

// ---------- pins
const TAGOFF = { '': 26, done: 24, nx: 36, new: 31, x: 24, sug: 26 };
const defs = {
  work:   { x: 684,  y: 565, n: '✓', time: '17:15', name: 'Work', a: 'l' },
  school: { x: 1054, y: 297, n: '2', time: '17:35', name: 'School', a: 't' },
  kinder: { x: 1507, y: 253, n: '3', time: '17:55', name: 'Kindergarten', a: 't' },
  ph1:    { x: 1278, y: 244, n: '✕', time: '', name: 'Pharmacy 1', a: 't' },
  ph2:    { x: 1697, y: 589, n: '4', time: '18:10', name: 'Pharmacy 2', a: 'l' },
  home:   { x: 1733, y: 892, n: '5', time: '18:33', name: 'Home', a: 'b' },
  salon:  { x: 1479, y: 706, n: '5', time: '18:30', name: 'Hair salon', a: 'l' },
  dinner: { x: 1319, y: 862, n: '6', time: '18:55', name: 'Italian, Main St', a: 'l' },
  dry:    { x: 1352, y: 519, n: '7', time: '19:20', name: 'Dry cleaner', a: 't' },
  fl:     { x: 1250, y: 784, n: '', time: '18:45', name: 'Flowers', a: 't', fp: true },
};
const pinsEl = document.getElementById('pins'), P = {};
for (const k in defs) {
  const d = defs[k], o = { d };
  o.rings = [0, 1, 2].map(() => { const s = document.createElement('span'); s.className = 'ring'; pinsEl.appendChild(s); return s; });
  o.pn = document.createElement('div'); pinsEl.appendChild(o.pn);
  o.tg = document.createElement('span'); pinsEl.appendChild(o.tg);
  P[k] = o;
}
// state: {s: '', 'nx','done','new','x','sug', a: opacity, tag: time text, nw: badge, ring: bool, check: bool}
function pin(k, st, t) {
  const o = P[k], d = o.d, a = st.a ?? 0;
  if (a <= 0.001) { o.pn.style.display = o.tg.style.display = 'none'; o.rings.forEach(r => r.style.display = 'none'); return; }
  const s = st.s || '', sc = .6 + .4 * eo(a);
  o.pn.style.display = o.tg.style.display = 'block';
  o.pn.className = d.fp ? 'fp ' + s : 'pn ' + s;
  if (d.fp) o.pn.className = 'fp' + (s === 'done' ? ' done' : s === 'sug' ? ' sug' : '');
  o.pn.style.cssText = `left:${d.x}px;top:${d.y}px;opacity:${a};` + (d.fp ? `transform:translate(-50%,-50%) rotate(45deg) scale(${sc})` : `transform:translate(-50%,-50%) scale(${sc})`);
  o.pn.innerHTML = d.fp ? '' : (st.check ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square"><path d="M4 12.5l5 5L20 6.5"/></svg>' : (s === 'done' ? '✓' : d.n));
  const off = d.fp ? 22 : (TAGOFF[s] ?? 26);
  let pos = '';
  if (d.a === 'l') pos = `left:${d.x - off}px;top:${d.y}px;transform:translate(-100%,-50%)`;
  else if (d.a === 't') pos = `left:${d.x}px;top:${d.y - off}px;transform:translate(-50%,-100%)`;
  else pos = `left:${d.x}px;top:${d.y + off}px;transform:translate(-50%,0)`;
  o.tg.className = 'tg ' + (d.fp ? (s === 'done' ? 'done' : s === 'sug' ? 'sug' : '') : s);
  o.tg.style.cssText = pos + `;opacity:${a * (st.tagA ?? 1)}`;
  const tm = st.tag ?? d.time;
  o.tg.innerHTML = `<i>${tm}</i>${d.name}` + (st.nw ? `<span class="nw">${st.nw}</span>` : '');
  const base = s === 'nx' ? 70 : s === 'new' ? 58 : 0;
  o.rings.forEach((r, i) => {
    if (!st.ring || !base) { r.style.display = 'none'; return; }
    const p = ((t * .85 + i * .3) % 1); r.style.display = 'block';
    r.style.cssText = `left:${d.x}px;top:${d.y}px;width:${base * (1 + p * .9)}px;height:${base * (1 + p * .9)}px;opacity:${(1 - p) * .8 * a}`;
  });
}

// ---------- schedule (built from the real route lengths)
const sSchool = FIN.near(846.7, 271), sKinder = FIN.near(1062.4, 249.8, sSchool + 30), sPh2 = FIN.near(1152.7, 409.8, sKinder + 30),
      sSalon = FIN.near(1049.2, 465.6, sPh2 + 30), sDin = FIN.near(973, 540, sSalon + 30);
const splitV1 = V1.near(1152.7, 409.8, V1.near(1062.4, 249.8) + 30);
const SPEED = 110, DW = .95;
const stops = [['school', sSchool], ['kinder', sKinder], ['ph2', sPh2], ['salon', sSalon], ['dinner', sDin]];
const T_GO = 8.0; let tc = T_GO, sc0 = 0; const run = [];            // run: {k, s0, s1, ta (travel start), tb (arrive), td (depart)}
for (const [k, s1] of stops) { const dur = Math.max(1.15, (s1 - sc0) / SPEED), dw = k === 'dinner' ? 2.0 : DW; run.push({ k, s0: sc0, s1, ta: tc, tb: tc + dur, td: tc + dur + dw }); tc += dur + dw; sc0 = s1; }
const R = Object.fromEntries(run.map(r => [r.k, r]));
const T_REROUTE = R.ph2.ta + (R.ph2.tb - R.ph2.ta) * .42;               // after the kindergarten, before the pharmacy
const T_FLOWERS = R.dinner.ta + (R.dinner.tb - R.dinner.ta) * .75;
const T_COU0 = R.dinner.td - .2, T_COU1 = T_COU0 + Math.max(1.8, COU.L / 55), T_END = T_COU1 + 1.9, TOTAL = T_END + 1.1;
window.TOTAL = TOTAL;
function carS(t) { for (const r of run) { if (t < r.ta) return r.s0; if (t < r.tb) return r.s0 + (r.s1 - r.s0) * sine((t - r.ta) / (r.tb - r.ta)); } return sDin; }

// ---------- frame
const carEl = document.getElementById('car'), carp = document.getElementById('carp');
window.frame = function (t) {
  const G = 1 - seg(t, TOTAL - 1.0, TOTAL);                               // global fade at the end of the loop
  const Gi = eo(seg(t, 0, .8));
  const g = Math.min(G, Gi);
  // timings of the plan build
  const tDef0 = .9, tDef1 = 2.2, tPlan0 = 3.0, tPlan1 = 5.0;
  const sCar = carS(t), moving = t >= T_GO, inCou = t >= T_COU0;
  const rerouted = t >= T_REROUTE;
  // default "going home" route
  const defA = g * (1 - seg(t, tPlan0 - .2, tPlan0 + .5));
  const defD = HOME.sub(0, HOME.L * eo(seg(t, tDef0, tDef1)));
  setG(gHome, defA > 0 ? defD : '', defA);
  // plan route v1 (via home) draws in, then follows the car; after the reroute only its prefix to the pharmacy remains
  const v1Draw = V1.L * ease(seg(t, tPlan0, tPlan1));
  const dV = splitV1 - sPh2;                                                   // the prefix of both plans is the same road
  const v1a = sCar + dV, v1b = rerouted ? splitV1 : v1Draw;
  setG(gV1, (t >= tPlan0) ? V1.sub(moving ? v1a : 0, v1b) : '', g);
  // old route (the part via home) stays as a dotted trace, then fades
  old.setAttribute('d', rerouted ? V1.sub(splitV1, V1.L) : '');
  old.style.opacity = g * (1 - seg(t, T_REROUTE + .8, T_REROUTE + 2.4));
  // final route draws in beyond the pharmacy
  const fin = eo(seg(t, T_REROUTE, T_REROUTE + 1.0));
  const dimFin = 1 - .62 * seg(t, T_COU0 - .3, T_COU0 + .5);
  const fa = Math.max(sCar, sPh2);
  setG(gFin, rerouted ? FIN.sub(fa, fa + (FIN.L - fa) * fin) : '', g * dimFin);
  // past (grey) trail follows the car along the final route
  past.setAttribute('d', moving ? FIN.sub(0, sCar) : '');
  past.style.opacity = g;
  // courier leg
  const cEnd = COU.L * ease(seg(t, T_COU0, T_COU1));
  const cA = g * seg(t, T_COU0 - .5, T_COU0 + .2);
  cglow.setAttribute('d', inCou ? COU.sub(0, COU.L) : ''); cglow.style.opacity = cA * .9;
  cdash.setAttribute('d', inCou ? COU.sub(0, COU.L) : ''); cdash.style.opacity = cA;
  // florist link (dotted)
  florl.setAttribute('d', '');

  // ----- pins
  const A = (t0, t1 = t0 + .45) => g * eo(seg(t, t0, t1));
  const doneAt = (r) => t >= r.tb + .25;
  pin('work', { s: 'done', a: g * eo(seg(t, .3, .8)), tag: '17:15' }, t);
  // school, kindergarten
  for (const k of ['school', 'kinder']) {
    const r = R[k], ap = A(k === 'school' ? 3.4 : 3.8);
    const s = doneAt(r) ? 'done' : (t >= T_GO - .3 && (k === 'school' || doneAt(R.school)) ? 'nx' : '');
    pin(k, { s, a: ap, ring: s === 'nx', tag: s === 'nx' ? 'NEXT · ' + defs[k].time : defs[k].time }, t);
  }
  // pharmacy 1 (no stock) -> crossed, pharmacy 2 (changed)
  const ph1a = A(5.1) * (1 - seg(t, T_GO + 1, T_GO + 2));
  pin('ph1', { s: t >= 5.9 ? 'x' : 'sug', a: ph1a, tag: '' }, t);
  { const r = R.ph2, ap = A(6.2); const s = doneAt(r) ? 'done' : (doneAt(R.kinder) ? 'nx' : (t >= 6.2 && t < 8.1 ? 'new' : ''));
    pin('ph2', { s, a: ap, ring: s === 'nx' || s === 'new', nw: (t >= 6.2 && t < 8.1 && !doneAt(R.kinder)) ? 'CHANGED' : '', tag: s === 'nx' ? 'NEXT · 18:10' : '18:10' }, t); }
  // home -> crossed after the reroute; hair salon new -> next -> done
  pin('home', { s: rerouted ? 'x' : '', a: A(4.3) * (1 - seg(t, T_REROUTE + 3.2, T_REROUTE + 4.2)) }, t);
  { const r = R.salon, ap = rerouted ? g * eo(seg(t, T_REROUTE + .25, T_REROUTE + .7)) : 0;
    const s = doneAt(r) ? 'done' : (doneAt(R.ph2) ? 'nx' : 'new');
    pin('salon', { s, a: ap, ring: s !== 'done', nw: s === 'new' ? 'NEW' : '', tag: s === 'nx' ? 'NEXT · 18:30' : '18:30' }, t); }
  // flowers
  pin('fl', { s: t >= T_FLOWERS ? 'done' : (t < 7.3 ? 'sug' : ''), a: A(6.8), tag: '18:45' }, t);
  // restaurant
  { const r = R.dinner; const arrived = t >= r.tb; const nx = doneAt(R.salon) && !arrived;
    const s = arrived ? 'nx' : (nx ? 'nx' : '');
    const cleared = t >= T_COU0 + .2;
    pin('dinner', { s: cleared ? 'done' : s, a: A(4.8), ring: !cleared && s === 'nx', check: arrived && !cleared, tag: arrived && !cleared ? 'ARRIVED · 18:55' : (nx ? 'NEXT · 18:55' : '18:55') }, t); }
  // dry cleaner (courier)
  { const arrived = t >= T_COU1; const ap = g * eo(seg(t, T_COU0 - .2, T_COU0 + .35));
    pin('dry', { s: arrived ? 'done' : 'new', a: ap, ring: !arrived, tag: arrived ? '19:20' : 'NEXT · 19:20' }, t); }

  // ----- car
  let cp, ch, hollow = false;
  if (inCou) { const s = COU.L * ease(seg(t, T_COU0, T_COU1)); cp = COU.at(s); ch = COU.head(s); hollow = true; }
  else { cp = FIN.at(sCar); ch = FIN.head(Math.max(sCar, 8)); }
  const px = Pm(cp[0], cp[1]);
  carEl.style.cssText = `left:${px[0]}px;top:${px[1]}px;transform:translate(-50%,-50%) rotate(${ch}deg);opacity:${g * eo(seg(t, .35, .9))}`;
  carp.setAttribute('fill', hollow ? 'rgba(2,18,28,.85)' : '#FFFFFF');
  carp.setAttribute('stroke', hollow ? '#E6F1F8' : '#02121C');
};
window.ready = Promise.all([document.fonts.load('500 16px Inter'), document.fonts.load('600 16px Inter'), document.fonts.load('400 16px Inter')]);
