/* Small interactive simulations. No libraries. All data here is synthetic. */
(function () {
  const NS = 'http://www.w3.org/2000/svg';
  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const rng = seed => () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  const gauss = r => Math.sqrt(-2 * Math.log(r() + 1e-12)) * Math.cos(2 * Math.PI * r());
  const el = (t, a = {}, p) => { const e = document.createElementNS(NS, t); for (const k in a) e.setAttribute(k, a[k]); if (p) p.appendChild(e); return e; };

  function plot(host, o) {
    host.innerHTML = '';
    const W = o.w || 640, H = (o.h || 220) + (o.legend ? 16 : 0), m = { l: 48, r: 14, t: o.legend ? 26 : 10, b: 36 };
    const s = el('svg', { viewBox: `0 0 ${W} ${H}`, role: 'img', 'aria-label': o.label || 'Plot' }, host);
    const xs = o.series.flatMap(q => q.x), ys = o.series.flatMap(q => q.y);
    const xl = o.xlim || [Math.min(...xs), Math.max(...xs)];
    let yl = o.ylim || [Math.min(...ys), Math.max(...ys)];
    if (yl[0] === yl[1]) yl = [yl[0] - 1, yl[1] + 1];
    const X = v => m.l + (v - xl[0]) / (xl[1] - xl[0]) * (W - m.l - m.r);
    const Y = v => H - m.b - (v - yl[0]) / (yl[1] - yl[0]) * (H - m.t - m.b);
    const ink = css('--muted'), grid = css('--line');
    const nice = (a, b, n) => { const out = []; const st = Math.pow(10, Math.floor(Math.log10((b - a) / n))); const k = (b - a) / n / st; const step = st * (k < 1.5 ? 1 : k < 3 ? 2 : k < 7 ? 5 : 10); for (let v = Math.ceil(a / step) * step; v <= b + 1e-9; v += step) out.push(+v.toFixed(6)); return out; };
    nice(yl[0], yl[1], 4).forEach(v => { el('line', { x1: m.l, x2: W - m.r, y1: Y(v), y2: Y(v), stroke: grid }, s); const t = el('text', { x: m.l - 6, y: Y(v) + 4, 'text-anchor': 'end', 'font-size': 11, fill: ink, 'font-family': 'IBM Plex Mono,monospace' }, s); t.textContent = v; });
    nice(xl[0], xl[1], 6).forEach(v => { const t = el('text', { x: X(v), y: H - m.b + 15, 'text-anchor': 'middle', 'font-size': 11, fill: ink, 'font-family': 'IBM Plex Mono,monospace' }, s); t.textContent = v; });
    if (o.xlabel) { const t = el('text', { x: (m.l + W - m.r) / 2, y: H - 4, 'text-anchor': 'middle', 'font-size': 12, fill: ink }, s); t.textContent = o.xlabel; }
    if (o.ylabel) { const t = el('text', { x: 12, y: (H - m.b + m.t) / 2, 'text-anchor': 'middle', 'font-size': 12, fill: ink, transform: `rotate(-90 12 ${(H - m.b + m.t) / 2})` }, s); t.textContent = o.ylabel; }
    o.series.forEach(q => {
      const c = q.color || css('--accent');
      if (q.dots) { q.x.forEach((v, i) => el('circle', { cx: X(v), cy: Y(q.y[i]), r: q.r || 2, fill: c, 'fill-opacity': q.opacity || .7 }, s)); return; }
      const d = q.x.map((v, i) => (i ? 'L' : 'M') + X(v).toFixed(1) + ' ' + Y(Math.max(yl[0], Math.min(yl[1], q.y[i]))).toFixed(1)).join('');
      el('path', { d, fill: q.fill ? c : 'none', 'fill-opacity': q.fill ? .15 : 1, stroke: c, 'stroke-width': q.width || 1.8, 'stroke-dasharray': q.dash || '' }, s);
    });
    (o.vlines || []).forEach(v => el('line', { x1: X(v.x), x2: X(v.x), y1: m.t, y2: H - m.b, stroke: v.color || ink, 'stroke-width': 1.5, 'stroke-dasharray': v.dash || '4 3' }, s));
    if (o.legend) { let lx = m.l + 8; o.legend.forEach(([n, c]) => { el('rect', { x: lx, y: 9, width: 12, height: 3, fill: c }, s); const t = el('text', { x: lx + 16, y: 15, 'font-size': 11.5, fill: css('--ink') }, s); t.textContent = n; lx += 28 + n.length * 6.3; }); }
    return { s, X, Y };
  }
  function controls(host) { const d = document.createElement('div'); d.className = 'ctl'; host.appendChild(d); return d; }
  function slider(ctl, label, min, max, step, val, fmt, on) {
    const l = document.createElement('label'); l.textContent = label + ' ';
    const i = document.createElement('input'); Object.assign(i, { type: 'range', min, max, step, value: val });
    const o = document.createElement('output'); const up = () => { o.textContent = fmt ? fmt(+i.value) : i.value; };
    i.addEventListener('input', () => { up(); on(); }); up(); l.append(i, o); ctl.appendChild(l); return i;
  }
  function buttons(ctl, names, cur, on) {
    const bs = names.map(n => { const b = document.createElement('button'); b.type = 'button'; b.textContent = n; if (n === cur) b.className = 'on'; b.addEventListener('click', () => { bs.forEach(x => x.className = ''); b.className = 'on'; on(n); }); ctl.appendChild(b); return b; });
  }
  const box = (host) => { const d = document.createElement('div'); host.appendChild(d); return d; };
  const readout = host => { const d = document.createElement('div'); d.style.cssText = 'font:12.5px IBM Plex Mono,monospace;color:var(--muted);margin-top:4px'; host.appendChild(d); return d; };
  const range = (a, b, n) => Array.from({ length: n }, (_, i) => a + (b - a) * i / (n - 1));

  const D = {
    nernst(h) {
      const c = controls(h), a = box(h), r = readout(h);
      const ou = slider(c, '[out] mM', 1, 150, 1, 5, null, go), inn = slider(c, '[in] mM', 1, 150, 1, 140, null, go);
      function go() {
        const e = 61.5 * Math.log10(+ou.value / +inn.value);
        const x = range(1, 150, 100);
        plot(a, { h: 180, label: 'Nernst potential', xlabel: '[out] (mM)', ylabel: 'E (mV)', ylim: [-120, 120], series: [{ x, y: x.map(v => 61.5 * Math.log10(v / +inn.value)) }, { x: [+ou.value], y: [e], dots: true, r: 6, color: css('--accent2'), opacity: 1 }] });
        r.textContent = `E = 61.5 log10([out]/[in]) = ${e.toFixed(1)} mV for a monovalent cation`;
      }
      go();
    },
    lif(h) {
      const c = controls(h), g = document.createElement('div'); g.className = 'two'; h.appendChild(g); const a = box(g), b = box(g), r = readout(h);
      const I = slider(c, 'Input current', 0, 3, .05, 1.6, v => v.toFixed(2), go);
      const sim = (cur) => { const tau = 10, th = 1, dt = .1, n = 2000; let v = 0, sp = 0; const V = []; for (let i = 0; i < n; i++) { v += dt / tau * (-v + cur); if (v >= th) { V.push(1.6); v = 0; sp++; } else V.push(v); } return { V, sp, t: n * dt }; };
      function go() {
        const R = sim(+I.value), t = R.V.map((_, i) => i * .1);
        plot(a, { w: 320, h: 200, label: 'Membrane voltage', xlabel: 'time (ms)', ylabel: 'V (relative)', ylim: [0, 1.7], series: [{ x: t, y: R.V, width: 1.3 }] });
        const cs = range(0, 3, 61), fr = cs.map(q => sim(q).sp / .2);
        plot(b, { w: 320, h: 200, label: 'f-I curve', xlabel: 'current', ylabel: 'rate (Hz)', series: [{ x: cs, y: fr }, { x: [+I.value], y: [R.sp / .2], dots: true, r: 5, color: css('--accent2'), opacity: 1 }] });
        r.textContent = R.sp ? `${R.sp} spikes in 200 ms` : 'Below threshold: no spikes';
      }
      go();
    },
    hh(h) {
      const c = controls(h), a = box(h), b = box(h), r = readout(h);
      const I = slider(c, 'Injected current (µA/cm²)', 0, 40, 1, 10, null, go);
      function go() {
        const dt = .02, n = 3000, cur = +I.value; let V = -65, m = .053, hh = .596, nn = .318;
        const T = [], Vs = [], M = [], H_ = [], N = []; let sp = 0, up = false;
        for (let i = 0; i < n; i++) {
          const t = i * dt, Ie = (t > 5 && t < 50) ? cur : 0, u = V + 65;
          const am = .1 * (25 - u) / (Math.exp((25 - u) / 10) - 1 || 1e-9), bm = 4 * Math.exp(-u / 18), ah = .07 * Math.exp(-u / 20), bh = 1 / (Math.exp((30 - u) / 10) + 1), an = .01 * (10 - u) / (Math.exp((10 - u) / 10) - 1 || 1e-9), bn = .125 * Math.exp(-u / 80);
          m += dt * (am * (1 - m) - bm * m); hh += dt * (ah * (1 - hh) - bh * hh); nn += dt * (an * (1 - nn) - bn * nn);
          V += dt * (Ie - 120 * m * m * m * hh * (V - 50) - 36 * nn * nn * nn * nn * (V + 77) - .3 * (V + 54.4));
          if (V > 0 && !up) { sp++; up = true; } if (V < -30) up = false;
          if (i % 10 === 0) { T.push(t); Vs.push(V); M.push(m); H_.push(hh); N.push(nn); }
        }
        const ac = css('--accent'), o = css('--accent2'), p = css('--networks');
        plot(a, { h: 190, label: 'Voltage', ylabel: 'V (mV)', ylim: [-90, 50], series: [{ x: T, y: Vs, width: 1.5 }] });
        plot(b, { h: 170, label: 'Gating variables', xlabel: 'time (ms)', ylabel: 'gate', ylim: [0, 1], series: [{ x: T, y: M, color: ac }, { x: T, y: H_, color: o }, { x: T, y: N, color: p }], legend: [['m (Na open)', ac], ['h (Na inactivation)', o], ['n (K open)', p]] });
        r.textContent = `${sp} spike${sp === 1 ? '' : 's'} during the 45 ms pulse`;
      }
      go();
    },
    sta(h) {
      const c = controls(h), a = box(h), r = readout(h);
      const n = slider(c, 'Recording length', 2, 60, 1, 8, v => v + ' s', go);
      const L = 40, f = range(0, L - 1, L).map(t => Math.exp(-t / 9) * Math.sin(2 * Math.PI * t / 22));
      const nf = Math.hypot(...f); const trueF = f.map(v => v / nf);
      function go() {
        const R = rng(11), N = +n.value * 1000, st = new Float64Array(N); for (let i = 0; i < N; i++) st[i] = gauss(R);
        const sum = new Float64Array(L); let k = 0;
        for (let i = L; i < N; i++) { let g = 0; for (let j = 0; j < L; j++) g += trueF[j] * st[i - j]; if (R() < .002 * Math.exp(2.2 * g)) { k++; for (let j = 0; j < L; j++) sum[j] += st[i - j]; } }
        const nm = Math.hypot(...sum) || 1, est = Array.from(sum, v => v / nm), x = range(0, L - 1, L);
        const dot = est.reduce((s, v, i) => s + v * trueF[i], 0);
        plot(a, { h: 210, label: 'Spike-triggered average', xlabel: 'time before spike (steps)', ylabel: 'normalised', series: [{ x, y: trueF, color: css('--muted'), dash: '5 4' }, { x, y: est, color: css('--accent') }], legend: [['true filter', css('--muted')], ['estimated STA', css('--accent')]] });
        r.textContent = `${k} spikes · correlation with the true filter: ${dot.toFixed(3)}`;
      }
      go();
    },
    sdt(h) {
      const c = controls(h), g = document.createElement('div'); g.className = 'two'; h.appendChild(g); const a = box(g), b = box(g), r = readout(h);
      const sep = slider(c, "Separation d'", 0, 4, .1, 1.5, v => v.toFixed(1), go), z = slider(c, 'Threshold', -3, 7, .1, 1, v => v.toFixed(1), go);
      const pdf = (x, m) => Math.exp(-.5 * (x - m) ** 2) / Math.sqrt(2 * Math.PI);
      const Phi = x => { const t = 1 / (1 + .2316419 * Math.abs(x)), d = .3989423 * Math.exp(-x * x / 2), p = d * t * (.3193815 + t * (-.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274)))); return x > 0 ? 1 - p : p; };
      function go() {
        const d = +sep.value, th = +z.value, x = range(-3, 7, 150);
        plot(a, { w: 320, h: 210, label: 'Response distributions', xlabel: 'response', ylabel: 'density', xlim: [-3, 7], series: [{ x, y: x.map(v => pdf(v, 0)), color: css('--muted'), fill: true }, { x, y: x.map(v => pdf(v, d)), color: css('--accent'), fill: true }], vlines: [{ x: th, color: css('--accent2') }] });
        const fa = 1 - Phi(th), hit = 1 - Phi(th - d), ts = range(-6, 9, 90);
        plot(b, { w: 320, h: 210, label: 'ROC curve', xlabel: 'false alarm rate', ylabel: 'hit rate', xlim: [0, 1], ylim: [0, 1], series: [{ x: [0, 1], y: [0, 1], color: css('--line') }, { x: ts.map(t => 1 - Phi(t)), y: ts.map(t => 1 - Phi(t - d)) }, { x: [fa], y: [hit], dots: true, r: 6, color: css('--accent2'), opacity: 1 }] });
        r.textContent = `hit rate ${hit.toFixed(2)} · false alarm rate ${fa.toFixed(2)}`;
      }
      go();
    },
    entropy(h) {
      const c = controls(h), a = box(h), bits = readout(h), r = readout(h);
      const p = slider(c, 'Spike probability', .01, .99, .01, .1, v => v.toFixed(2), go);
      const H = q => -(q * Math.log2(q) + (1 - q) * Math.log2(1 - q));
      function go() {
        const q = +p.value, x = range(.001, .999, 150);
        plot(a, { h: 190, label: 'Binary entropy', xlabel: 'spike probability', ylabel: 'bits', ylim: [0, 1.05], xlim: [0, 1], series: [{ x, y: x.map(H) }, { x: [q], y: [H(q)], dots: true, r: 6, color: css('--accent2'), opacity: 1 }] });
        const R = rng(5); let s = ''; for (let i = 0; i < 64; i++) s += R() < q ? '|' : '·';
        bits.textContent = s; bits.style.letterSpacing = '.15em'; bits.style.overflow = 'hidden'; bits.style.whiteSpace = 'nowrap';
        r.textContent = `H = ${H(q).toFixed(3)} bits per bin, the most at p = 0.5`;
      }
      go();
    },
    eigen(h) {
      const c = controls(h), a = box(h), r = readout(h);
      const l = slider(c, 'Eigenvalue λ', 0, 1.2, .01, .8, v => v.toFixed(2), go);
      function go() {
        const L = +l.value, dt = .1, t = range(0, 40, 400); let v = 0; const y = t.map(tt => { v += dt / 1 * (-v + (tt < 5 ? 1 : 0) + L * v); return v; });
        plot(a, { h: 200, label: 'Mode amplitude', xlabel: 'time (τ)', ylabel: 'amplitude', ylim: [0, Math.min(25, Math.max(1, ...y) * 1.1)], series: [{ x: t, y }], vlines: [{ x: 5 }] });
        r.textContent = L > 1.001 ? 'λ > 1: the linear network explodes' : Math.abs(L - 1) < .011 ? 'λ = 1: the mode integrates, then holds its value after input ends' : `λ < 1: decays after input ends (input lasts until the dashed line); steady-state gain 1/(1-λ) = ${(1 / (1 - L)).toFixed(1)}`;
      }
      go();
    },
    oja(h) {
      const c = controls(h), g = document.createElement('div'); g.className = 'two'; h.appendChild(g); const a = box(g), b = box(g), r = readout(h);
      const cr = slider(c, 'Input correlation', 0, .95, .05, .8, v => v.toFixed(2), go);
      function go() {
        const R = rng(3), rho = +cr.value, U = []; for (let i = 0; i < 300; i++) { const x = gauss(R), y = rho * x + Math.sqrt(1 - rho * rho) * gauss(R); U.push([x, y]); }
        let o = [.6, -.3], he = [.6, -.3]; const eta = .01, ss = [], no = [], nh = [];
        for (let k = 0; k < 900; k++) { const u = U[k % 300]; const vo = o[0] * u[0] + o[1] * u[1]; o = [o[0] + eta * vo * (u[0] - vo * o[0]), o[1] + eta * vo * (u[1] - vo * o[1])]; const vh = he[0] * u[0] + he[1] * u[1]; he = [he[0] + eta * vh * u[0], he[1] + eta * vh * u[1]]; if (k % 10 === 0) { ss.push(k); no.push(Math.hypot(...o)); nh.push(Math.hypot(...he)); } }
        const nHe = Math.hypot(...he), dir = [he[0] / nHe, he[1] / nHe], s = 2.8;
        const pl = plot(a, { w: 320, h: 240, label: 'Input cloud and learned weights', xlabel: 'u₁', ylabel: 'u₂', xlim: [-3.5, 3.5], ylim: [-3.5, 3.5], series: [{ x: U.map(q => q[0]), y: U.map(q => q[1]), dots: true, r: 1.8, color: css('--muted'), opacity: .4 }, { x: [0, o[0] * s], y: [0, o[1] * s], color: css('--accent'), width: 3 }, { x: [0, dir[0] * s * .8], y: [0, dir[1] * s * .8], color: css('--accent2'), width: 1.5, dash: '4 3' }] });
        plot(b, { w: 320, h: 240, label: 'Weight norm', xlabel: 'updates', ylabel: '|w|', ylim: [0, 6], series: [{ x: ss, y: no, color: css('--accent') }, { x: ss, y: nh, color: css('--accent2') }], legend: [['Oja', css('--accent')], ['Hebb', css('--accent2')]] });
        r.textContent = `after 900 updates: Oja |w| = ${Math.hypot(...o).toFixed(2)} · Hebb |w| = ${nHe.toExponential(1)}`;
      }
      go();
    },
    perceptron(h) {
      const c = controls(h), g = document.createElement('div'); g.className = 'two'; h.appendChild(g); const a = box(g), b = box(g), r = readout(h);
      const T = { AND: [0, 0, 0, 1], OR: [0, 1, 1, 1], XOR: [0, 1, 1, 0] }, P = [[0, 0], [0, 1], [1, 0], [1, 1]];
      function go(name) {
        const t = T[name]; let w = [.2, -.1], th = .1; const err = [];
        for (let e = 0; e < 60; e++) { let m = 0; P.forEach((p, i) => { const y = w[0] * p[0] + w[1] * p[1] > th ? 1 : 0, d = t[i] - y; if (d) m++; w = [w[0] + .1 * d * p[0], w[1] + .1 * d * p[1]]; th -= .1 * d; }); err.push(m); }
        const xs = [-.3, 1.3], ln = Math.abs(w[1]) > 1e-6 ? xs.map(x => (th - w[0] * x) / w[1]) : [-9, 9];
        plot(a, { w: 320, h: 240, label: 'Decision boundary', xlabel: 'x₁', ylabel: 'x₂', xlim: [-.3, 1.3], ylim: [-.3, 1.3], series: [{ x: P.filter((_, i) => t[i]).map(p => p[0]), y: P.filter((_, i) => t[i]).map(p => p[1]), dots: true, r: 8, color: css('--accent'), opacity: 1 }, { x: P.filter((_, i) => !t[i]).map(p => p[0]), y: P.filter((_, i) => !t[i]).map(p => p[1]), dots: true, r: 8, color: css('--accent2'), opacity: 1 }, { x: xs, y: ln, color: css('--ink'), width: 1.5 }] });
        plot(b, { w: 320, h: 240, label: 'Errors per epoch', xlabel: 'epoch', ylabel: 'errors', ylim: [0, 4], series: [{ x: err.map((_, i) => i), y: err }] });
        r.textContent = err[err.length - 1] ? `${name}: still making errors after 60 epochs. No straight line can separate these points.` : `${name}: converged, ${err.findIndex(v => !v)} epochs to zero errors.`;
      }
      buttons(c, ['AND', 'OR', 'XOR'], 'XOR', go); go('XOR');
    },
    td(h) {
      const c = controls(h), cv = document.createElement('canvas'); cv.width = 720; cv.height = 300; h.appendChild(cv); const a = box(h), r = readout(h);
      let omit = false;
      buttons(c, ['Reward delivered', 'Reward omitted on last trial'], 'Reward delivered', n => { omit = n !== 'Reward delivered'; go(); });
      function go() {
        const T = 25, N = 120, cue = 5, rew = 18, w = new Float64Array(T), eps = .25, Dm = [];
        for (let k = 0; k < N; k++) {
          const v = new Float64Array(T + 1); for (let t = 0; t < T; t++) { let s = 0; for (let j = 0; j <= t; j++) if (t - j === cue) s += w[j]; v[t] = s; }
          const d = new Float64Array(T);
          for (let t = 0; t < T; t++) { const R = (t === rew && !(omit && k === N - 1)) ? 1 : 0; d[t] = R + v[t + 1] - v[t]; for (let j = 0; j <= t; j++) if (t - j === cue) w[j] += eps * d[t]; }
          Dm.push(d);
        }
        const x = cv.getContext('2d'), cw = cv.width / T, ch = cv.height / N;
        x.fillStyle = css('--paper'); x.fillRect(0, 0, cv.width, cv.height);
        Dm.forEach((d, k) => d.forEach((v, t) => { if (Math.abs(v) < .01) return; x.fillStyle = v > 0 ? `rgba(180,80,31,${Math.min(1, v * 1.1)})` : `rgba(36,103,168,${Math.min(1, -v * 1.1)})`; x.fillRect(t * cw, k * ch, cw + .5, ch + .5); }));
        const t = range(0, T - 1, T);
        plot(a, { h: 170, label: 'Prediction error', xlabel: 'time step in trial (cue at 5, reward at 18)', ylabel: 'δ', ylim: [-1.1, 1.1], series: [{ x: t, y: Array.from(Dm[0]), color: css('--muted'), dash: '4 3' }, { x: t, y: Array.from(Dm[N - 1]), color: css('--accent') }], legend: [['first trial', css('--muted')], ['last trial', css('--accent')]] });
        r.textContent = 'Heatmap: trials run top to bottom, time left to right. Orange is positive error, blue negative. ' + (omit ? 'The dip at the expected reward time is the omission response.' : 'The error moves from the reward to the cue.');
      }
      go();
    },
    hrf(h) {
      const c = controls(h), a = box(h), r = readout(h);
      const gm = (t, k) => { if (t <= 0) return 0; let lg = 0; for (let i = 2; i < k; i++) lg += Math.log(i); return Math.exp((k - 1) * Math.log(t) - t - lg); };
      const hrf = t => gm(t, 6) - gm(t, 16) / 6;
      const go = name => {
        const dt = .5, t = range(0, 120, 241), s = t.map(tt => name === 'Block design' ? (tt % 40 < 20 && tt < 100 ? 1 : 0) : ([8, 28, 36, 60, 72, 96].some(e => Math.abs(tt - e) < .25) ? 1 : 0));
        const b = t.map((_, i) => { let v = 0; for (let j = 0; j <= i && j < 80 * 2; j++) v += (s[i - j] || 0) * hrf(j * dt) * dt; return v; });
        const m = Math.max(...b, .001);
        plot(a, { h: 210, label: 'Predicted BOLD', xlabel: 'time (s)', ylabel: 'relative signal', ylim: [-.4, 1.1], series: [{ x: t, y: s.map(v => v * .95), color: css('--line'), fill: true, width: 1 }, { x: t, y: b.map(v => v / m), color: css('--brain'), width: 2 }] });
        r.textContent = name === 'Block design' ? 'Blocks sum into a large, robust plateau, but hide the shape of the response.' : 'Single events give smaller responses, but their shape can be recovered.';
      };
      buttons(c, ['Block design', 'Event-related design'], 'Block design', go); go('Block design');
    },
    relax(h) {
      const c = controls(h), a = box(h);
      const t1 = slider(c, 'T1 (ms)', 200, 3000, 50, 1000, null, go), t2 = slider(c, 'T2 (ms)', 20, 400, 10, 100, null, go);
      function go() { const t = range(0, 3000, 200), ac = css('--accent'), o = css('--accent2'); plot(a, { h: 200, label: 'Relaxation', xlabel: 'time after excitation (ms)', ylabel: 'magnetisation', ylim: [0, 1], series: [{ x: t, y: t.map(v => 1 - Math.exp(-v / +t1.value)), color: ac }, { x: t, y: t.map(v => Math.exp(-v / +t2.value)), color: o }], legend: [['Longitudinal recovery (T1)', ac], ['Transverse decay (T2)', o]] }); }
      go();
    },
  };
  document.querySelectorAll('[data-demo]').forEach(f => { const s = f.querySelector('.stage'); const fn = D[f.dataset.demo]; if (s && fn) { s.innerHTML = ''; try { fn(s); } catch (e) { s.textContent = 'This simulation could not run.'; console.error(e); } } });
})();
