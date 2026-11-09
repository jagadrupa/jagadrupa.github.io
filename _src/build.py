#!/usr/bin/env python3
"""Generates the static site. Fails if any note reference cannot be found on its cited PDF page."""
import re, subprocess, html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import *
ROOT = pathlib.Path(__file__).resolve().parent.parent
E = html.escape
TEX = str.maketrans({"–": "-", "—": "-", "’": "'", "‘": "'", "“": '"', "”": '"'})
def norm(s): return re.sub(r"[^a-z0-9]+", "", s.translate(TEX).lower().replace("ﬁ", "fi").replace("ﬀ", "ff").replace("ﬂ", "fl").replace("ﬃ", "ffi"))

TOC = {}
PAGES = {}
def pagetext(stem):
    if stem not in PAGES:
        t = subprocess.run(["pdftotext", str(ROOT/f"notes/{stem}.pdf"), "-"], capture_output=True, text=True).stdout
        PAGES[stem] = t.split("\f")
    return PAGES[stem]
for d, (stem, _) in DOCS.items():
    rows = []
    for l in open(ROOT/f"_src/{stem}.aux", errors="ignore"):
        m = re.search(r"\\contentsline \{section\}\{(.*)\}\{(\d+)\}\{", l)
        if m:
            t = re.sub(r"\\numberline \{[^}]*\}", "", m[1]); t = re.sub(r"\\[a-zA-Z@]+\s*", "", t).replace("{", "").replace("}", "")
            rows.append((t.replace("---", "—").replace("--", "–").strip(), int(m[2])))
    TOC[d] = rows
checked = 0
def ref(doc, frag):
    global checked
    hits = [(t, p) for t, p in TOC[doc] if norm(frag.replace("--", "-")) in norm(t)]
    exact = [h for h in hits if norm(h[0]) == norm(frag.replace("--", "-"))]
    if exact: hits = exact
    if not hits: sys.exit(f"NO SECTION {doc}: {frag}")
    t, p = hits[0]
    stem = DOCS[doc][0]
    if norm(t)[:14] not in norm(pagetext(stem)[p-1]):
        sys.exit(f"PAGE MISMATCH {doc} p{p}: {t}")
    checked += 1
    return t, p, stem

def chip(doc, frag, rel=""):
    t, p, stem = ref(doc, frag)
    return f'<a class="chip" href="{rel}notes/{stem}.pdf#page={p}" title="{E(t)}">{DOCS[doc][1]} · p.{p}</a>'
def chips(refs, rel=""):
    seen, out = set(), ""
    for d, f in refs:
        t, p, stem = ref(d, f)
        if (d, p) in seen: continue
        seen.add((d, p)); out += chip(d, f, rel)
    return out
BADGE = {"cert": '<span class="badge b-cert">Certificate</span>', "audit": '<span class="badge b-audit">Audited</span>', "todo": '<span class="badge b-todo">To be updated</span>', "research": '<span class="badge b-research">Original research</span>'}
SHORT = {"uw-computational-neuroscience": "UW", "jhu-neuroimaging": "JHU", "uchicago-understanding-the-brain": "UChicago", "yale-introduction-to-psychology": "Yale", "harvardx-mcb80-1x": "HarvardX 1", "harvardx-mcb80-2x": "HarvardX 2", "harvardx-mcb80-3x": "HarvardX 3"}

def outcome_refs(c, o, rel):
    if c["kind"] == "notes":
        return chips(o[3], rel)
    out = ""
    if c.get("cert"):
        cc = CERTS[c["cert"]]
        out += f'<a class="chip" href="{rel}{cc[4]}.pdf">Certificate · {cc[2]}</a>'
    else:
        out += '<span class="chip src">Audited, no certificate</span>'
    out += f'<a class="chip src" href="{c["url"]}">Official course page ↗</a>'
    return out

def page(path, title, body, active="", desc="A learning record in neuroscience, from molecules to disease, where every claim links to its evidence."):
    depth = path.count("/")
    rel = "../" * depth
    links = [("index.html", "Home", "home"), ("by-scale.html", "By scale", "scale"), ("courses.html", "By course", "courses"), ("certificates.html", "Certificates", "certs")]
    nav = "".join(f'<a href="{rel}{h}"{" class=on" if a == active else ""}>{t}</a>' for h, t, a in links)
    doc = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="author" content="Jagadrupa Sahoo">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M2 18h8l3-10 5 18 3-8h9' fill='none' stroke='%230f6e6e' stroke-width='3'/%3E%3C/svg%3E"><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/style.css"></head><body>
<header class="top"><div class="wrap"><a class="brand" href="{rel}index.html">Jagadrupa Sahoo</a><nav>{nav}<a href="https://github.com/jagadrupa">GitHub ↗</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">Notes and research are my own. Course names and certificates belong to their institutions; lecture slides and assessment answers are not reproduced here. Site and interactive simulations were built with AI assistance. Simulations use illustrative parameters and synthetic data.</div></footer>
<script src="{rel}assets/demos.js"></script></body></html>'''
    (ROOT/path).parent.mkdir(exist_ok=True, parents=True)
    (ROOT/path).write_text(doc)

ICON = {
 "molecules": '<circle cx="20" cy="22" r="8"/><circle cx="44" cy="20" r="6"/><circle cx="32" cy="44" r="10"/><path d="M27 26l2 8M38 24l-3 11M26 21l12-1"/>',
 "neurons": '<circle cx="18" cy="32" r="8"/><path d="M26 32h28M46 32l8-8M46 32l8 8M12 26L5 18M12 38L5 46M18 24V12"/>',
 "networks": '<circle cx="12" cy="14" r="5"/><circle cx="12" cy="50" r="5"/><circle cx="32" cy="32" r="5"/><circle cx="52" cy="14" r="5"/><circle cx="52" cy="50" r="5"/><path d="M16 17l12 12M16 47l12-12M36 29l12-12M36 35l12 12M12 19v26M52 19v26"/>',
 "brain": '<path d="M16 42c-8-2-10-14-4-19 0-8 10-13 17-9 7-4 19-1 21 8 7 5 6 16-2 19-3 7-14 8-18 2-5 3-12 3-14-1z"/><path d="M30 14v30M18 24c5 0 8 3 8 8M44 24c-5 0-8 3-8 8"/>',
 "cognition": '<path d="M20 56V44C10 38 8 22 18 13c10-9 28-6 32 7l5 12-6 2v8c0 4-4 6-8 5l-5-1v10"/><circle cx="31" cy="26" r="7"/><path d="M31 15v4M31 33v4M20 26h4M38 26h4"/>',
 "disease": '<path d="M8 32h12l5-14 9 28 7-20 3 6h12"/><circle cx="32" cy="32" r="26" stroke-dasharray="3 5"/>',
}
def icon(k, size=64): return f'<svg viewBox="0 0 64 64" width="{size}" height="{size}" fill="none" stroke="var(--{k})" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'

ALL = []
for c in COURSES:
    for o in c["outcomes"]:
        ALL.append((c, o))
n_note = sum(1 for c, o in ALL if c["kind"] == "notes")
notes_pages = sum(len([p for p in pagetext(DOCS[d][0]) if p.strip()]) for d in DOCS)

def demo(k, rel):
    t, d, refs = DEMOS[k]
    cs = chips(refs, rel)
    return f'<figure class="demo" data-demo="{k}" style="margin-left:0;margin-right:0"><h4>{E(t)}</h4><p>{E(d)}</p><div class="stage"><noscript>This simulation needs JavaScript.</noscript></div><div class="chips" style="margin-top:8px"><span class="chip src">Simulation, synthetic data</span>{cs}</div></figure>'

def ladder(rel=""):
    x = [70, 246, 422, 598, 774, 950]
    parts = ['<line x1="70" y1="70" x2="950" y2="70" stroke="var(--line)" stroke-width="2"/>']
    for (k, name, sub, _), cx in zip(SCALES, x):
        parts.append(f'<a href="{rel}by-scale.html#{k}"><circle class="node" cx="{cx}" cy="70" r="42" fill="var(--paper)" stroke="var(--{k})" stroke-width="2"/><g transform="translate({cx-24} 46) scale(.75)" fill="none" stroke="var(--{k})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{ICON[k]}</g><text x="{cx}" y="136" text-anchor="middle" font-family="var(--serif)" font-size="21" fill="var(--ink)">{name}</text></a>')
    parts.append('<circle class="spike" r="6" fill="var(--accent2)"/>')
    return f'<svg class="ladder" viewBox="0 0 1020 150" role="img" aria-label="Six scales from molecules to disease">{"".join(parts)}</svg>'

# ---- diagrams
def TRANSMITTERS(rel):
    rows = [("Acetylcholine", "Alzheimer's disease", None), ("Dopamine", "Parkinson's disease", "Schizophrenia"), ("Glutamate", None, "ALS (excitotoxic)")]
    y = 62; out = ""
    for name, lt, ht in rows:
        out += f'<text x="20" y="{y+5}" font-size="15" font-family="var(--serif)" fill="var(--ink)">{name}</text><line x1="170" x2="710" y1="{y}" y2="{y}" stroke="var(--line)"/>'
        if lt: out += f'<rect x="210" y="{y-14}" width="210" height="28" rx="4" fill="var(--disease)" fill-opacity=".14" stroke="var(--disease)"/><text x="315" y="{y+5}" text-anchor="middle" font-size="13" fill="var(--ink)">{lt}</text>'
        if ht: out += f'<rect x="460" y="{y-14}" width="210" height="28" rx="4" fill="var(--disease)" fill-opacity=".14" stroke="var(--disease)"/><text x="565" y="{y+5}" text-anchor="middle" font-size="13" fill="var(--ink)">{ht}</text>'
        y += 48
    svg = f'<svg class="diag" viewBox="0 0 730 {y-10}" role="img" aria-label="Clinical signatures of too little and too much transmitter" font-family="var(--sans)"><text x="315" y="24" text-anchor="middle" font-size="12" font-family="var(--mono)" fill="var(--muted)">TOO LITTLE</text><text x="565" y="24" text-anchor="middle" font-size="12" font-family="var(--mono)" fill="var(--muted)">TOO MUCH</text><line x1="440" x2="440" y1="34" y2="{y-20}" stroke="var(--muted)" stroke-dasharray="3 4"/>{out}</svg>'
    c = chip("ni", "Four Transmitters and Their Clinical Signatures", rel)
    return f'<figure class="demo" style="margin-left:0;margin-right:0"><h4>Either direction is pathological</h4><p>A schematic of the clinical signatures in my notes. It is qualitative, and bar width carries no meaning.</p>{svg}<div class="chips">{c}</div></figure>'

def UW_ARC(rel):
    w = [("w1", "Neurobiology"), ("w2", "Encoding"), ("w3", "Decoding"), ("w4", "Information"), ("w5", "Carbon"), ("w6", "Networks"), ("w7", "Plasticity"), ("w8", "Reward")]
    q = [("What is", "a neuron?"), ("Stimulus", "to spikes"), ("Spikes to", "stimulus"), ("How good", "is the code?"), ("Physics of", "a neuron"), ("Reduced", "to circuits"), ("How circuits", "learn alone"), ("Learning", "from reward")]
    cells = ""
    for i, (d, t) in enumerate(w):
        x = 12 + i * 92
        stem = DOCS[d][0]
        cells += f'<text x="{x+42}" y="26" font-size="12" text-anchor="middle" fill="var(--muted)">{q[i][0]}</text><text x="{x+42}" y="42" font-size="12" text-anchor="middle" fill="var(--muted)">{q[i][1]}</text>'
        cells += f'<a href="{rel}notes/{stem}.pdf"><rect x="{x}" y="54" width="84" height="66" rx="5" fill="var(--paper)" stroke="var(--accent)"/><text x="{x+42}" y="80" text-anchor="middle" font-family="var(--mono)" font-size="11" fill="var(--muted)">WEEK {i+1}</text><text x="{x+42}" y="101" text-anchor="middle" font-family="var(--serif)" font-size="13.5" fill="var(--ink)">{t}</text></a>'
        if i < 7: cells += f'<line x1="{x+84}" y1="87" x2="{x+92}" y2="87" stroke="var(--accent)"/>'
    return f'<figure class="demo" style="margin:16px 0"><h4>The course as a chain of questions</h4><p>Open any week to read its notes.</p><div class="scroll"><svg class="diag" style="min-width:640px" viewBox="0 0 760 130" font-family="var(--sans)" role="img" aria-label="Eight weeks as a chain of questions">{cells}</svg></div></figure>'

def JHU_GFX(rel):
    steps = [("Neural activity", "Synapses and spikes"), ("Metabolic demand", "Oxygen is used"), ("Blood response", "Oxygenated blood arrives"), ("BOLD signal", "What the scanner sees")]
    b = ""
    for i, (a, c) in enumerate(steps):
        x = 12 + i * 186
        acc = i == 3
        fill = "var(--brain)" if acc else "var(--paper)"
        op = .14 if acc else 1
        b += f'<rect x="{x}" y="14" width="164" height="64" rx="6" fill="{fill}" fill-opacity="{op}" stroke="var(--brain)"/><text x="{x+82}" y="42" text-anchor="middle" font-family="var(--serif)" font-size="16" fill="var(--ink)">{a}</text><text x="{x+82}" y="62" text-anchor="middle" font-size="11.5" fill="var(--muted)">{c}</text>'
        if i < 3: b += f'<path d="M{x+166} 46h17m-6-5l6 5l-6 5" fill="none" stroke="var(--muted)"/>'
    grid = """<table class="plain" style="margin-top:6px"><tr><th>Case</th><th>Impaired</th><th>Spared</th><th>What it shows</th></tr>
<tr><td>Broca's patients</td><td>Producing language</td><td>Comprehending it</td><td rowspan="2">A double dissociation: two capacities can fail independently</td></tr>
<tr><td>Wernicke's patients</td><td>Comprehending language</td><td>Producing it</td></tr>
<tr><td>H.M.</td><td>Forming new memories</td><td>Improving at mirror drawing</td><td>Memory is several systems</td></tr></table>"""
    tree = """<table class="plain" style="margin-top:6px"><tr><th>Family</th><th>Methods in my notes</th><th>Key point</th></tr>
<tr><td>Electrical</td><td>EEG</td><td>Records electrical activity directly, but localises poorly</td></tr>
<tr><td>Ionising or tracer-based</td><td>CT, SPECT, PET</td><td>Radiation dose; for PET, the tracer defines the experiment</td></tr>
<tr><td>One magnet, several refinements</td><td>MRI, fMRI, DTI, spectroscopy</td><td>The same hardware gives different contrasts</td></tr></table>"""
    c1 = chips([("ni", "Why Blood Follows Activity"), ("ni", "What Is BOLD Correlated With?")], rel)
    c2 = chips([("ni", "Language: Broca and Wernicke"), ("ni", "Memory: H.M. and E.P."), ("ni", "The Mirror-Drawing Result")], rel)
    c3 = chips([("ni", "EEG"), ("ni", "SPECT and PET"), ("ni", "Three Refinements of the Same Hardware")], rel)
    return (f'<figure class="demo" style="margin:16px 0"><h4>What fMRI actually measures</h4><p>A downstream vascular proxy, not neural activity itself.</p><div class="scroll"><svg class="diag" style="min-width:640px" viewBox="0 0 760 92" font-family="var(--sans)" role="img" aria-label="From neural activity to the BOLD signal">{b}</svg></div><div class="chips">{c1}</div></figure>'
            f'<figure class="demo" style="margin:16px 0"><h4>What lesions taught us</h4>{grid}<div class="chips" style="margin-top:8px">{c2}</div></figure>'
            f'<figure class="demo" style="margin:16px 0"><h4>The imaging toolkit</h4>{tree}<div class="chips" style="margin-top:8px">{c3}</div></figure>')

def RAIL(c):
    items = c["outcomes"]
    n = len(items); h = 44 * n + 16
    o = f'<line x1="30" x2="30" y1="24" y2="{h-30}" stroke="var(--line)" stroke-width="2"/>'
    for i, it in enumerate(items):
        y = 28 + i * 44; k = it[0]
        name = next(s[1] for s in SCALES if s[0] == k).upper()
        o += f'<circle cx="30" cy="{y}" r="13" fill="var(--paper)" stroke="var(--{k})" stroke-width="2"/><text x="30" y="{y+4}" text-anchor="middle" font-family="var(--mono)" font-size="11" fill="var(--ink)">{i+1}</text><text x="56" y="{y+5}" font-size="14" fill="var(--ink)">{E(it[2])}</text><text x="745" y="{y+4}" text-anchor="end" font-family="var(--mono)" font-size="10.5" fill="var(--{k})">{name}</text>'
    return f'<figure class="demo" style="margin:16px 0"><h4>Course map</h4><p>Topics in order from the official course page, coloured by scale.</p><div class="scroll"><svg class="diag" style="min-width:680px" viewBox="0 0 760 {h}" font-family="var(--sans)" role="img" aria-label="Course topics in order">{o}</svg></div></figure>'

# ---- home
def counts(k): return sum(1 for c, o in ALL if o[0] == k) + (len(AD_FINDINGS) if k == "disease" else 0)
n_out = len(ALL) + len(AD_FINDINGS)
home = f'''<section><p class="eyebrow">Neuroscience learning record</p><h1>From molecules to disease,<br>with the evidence attached.</h1>
<p class="lede">I work in bioinformatics and study human Alzheimer's tissue with spatial transcriptomics. This record shows what I have learned about the brain, how I learned it, and where to check each claim.</p>
{ladder()}
<div class="stats"><a class="stat" href="by-scale.html"><b>{n_out}</b><span>learning outcomes and findings, each referenced</span></a><a class="stat" href="courses.html"><b>{sum(c["status"]=="cert" for c in COURSES)} + {sum(c["status"]=="audit" for c in COURSES)}</b><span>courses certified + audited</span></a><a class="stat" href="courses/uw-computational-neuroscience.html"><b>{notes_pages}</b><span>pages of my own public notes</span></a><a class="stat" href="certificates.html"><b>2020–26</b><span>span of certificates</span></a></div></section>
<section><h2>Three ways in</h2><div class="grid" style="margin-top:16px">
<a class="card ccard" href="by-scale.html"><span class="eyebrow">By scale</span><h3>Everything learned, from molecules up</h3><small>Six levels, with simulations, textbook chapters and sources.</small></a>
<a class="card ccard" href="courses.html"><span class="eyebrow">By course</span><h3>Each course and its graphical summary</h3><small>Outcomes by unit, with a page reference for each.</small></a>
<a class="card ccard" href="certificates.html"><span class="eyebrow">Certificates</span><h3>Verifiable certificates, on a timeline</h3><small>Open the PDF, or verify it with the issuer.</small></a></div></section>
<section><h2>How to read the evidence</h2><p class="note">A claim is only as strong as its source, so each one shows which kind it is.</p>
<table class="plain" style="margin-top:12px"><tr><th>Label</th><th>What it means</th><th>Where the link goes</th></tr>
<tr><td><a class="chip" href="notes/uw-w5.pdf#page=10">UW week 5 · p.10</a></td><td>I wrote this up in my own notes</td><td>The exact PDF page. The build fails if the section is not on that page.</td></tr>
<tr><td>{BADGE["cert"]}</td><td>Course completed and certified by the institution</td><td>The certificate, and the issuer's verification page</td></tr>
<tr><td>{BADGE["audit"]}</td><td>Course audited, so no graded work or certificate</td><td>The official outcomes on the course page</td></tr>
<tr><td>{BADGE["todo"]}</td><td>Details will be added later</td><td>The official course page</td></tr>
<tr><td>{BADGE["research"]}</td><td>My own analysis, with code and stated limitations</td><td>The relevant section of the public repository</td></tr></table></section>'''
page("index.html", "Jagadrupa Sahoo: neuroscience learning record", home, "home")

# ---- by scale
sec = ""
jump = '<div class="jump">' + "".join(f'<a href="#{k}" style="color:var(--{k})">{n} · {counts(k)}</a>' for k, n, _, _ in SCALES) + "</div>"
for k, name, sub, why in SCALES:
    items = ""
    groups = {}
    for c, o in ALL:
        if o[0] == k: groups.setdefault(c["id"], (c, []))[1].append(o)
    for cid, (c, os_) in groups.items():
        for o in os_:
            items += f'<li><p>{E(o[2])}</p><div class="chips"><a class="chip course" href="courses/{cid}.html">{SHORT[cid]}</a>{outcome_refs(c, o, "")}</div></li>'
    if k == "disease":
        for s, u, t, a in AD_FINDINGS:
            items += f'<li><p>{E(t)}</p><div class="chips">{BADGE["research"]}<a class="chip" href="{REPO_AD}{a}">Repository section ↗</a></div></li>'
    extra = ""
    if k == "disease":
        figs = "".join(f'<figure><a href="figs/{f}.png"><img loading="lazy" src="figs/{f}.png" alt="{E(cap)}"></a><figcaption>{E(cap)} · <a href="{REPO_AD}{a}">source ↗</a></figcaption></figure>' for f, cap, a in AD_FIGS)
        extra = f'<h3 style="margin-top:22px">Original work: human Alzheimer\'s cortex, 10x Xenium</h3><p class="note">About 45,000 AD cells and 24,000 matched healthy cells. <a href="{REPO_AD}">Code, figures and limitations are public</a>.</p><div class="gallery">{figs}</div>' + TRANSMITTERS("")
    book = "".join(f'<a class="chip src" href="{BOOK_BASE}{h}" title="{E(t)}">{l} · {E(t)} ↗</a>' for h, l, t in BOOK[k])
    demos = "".join(demo(d, "") for d in SCALE_DEMOS[k])
    sec += f'''<section id="{k}"><div class="lvl">{icon(k)}<div><span class="eyebrow">{sub}</span><h2>{name}</h2><p class="note" style="margin:6px 0 0">{why}</p></div></div>
{demos}{extra}<ul class="out">{items}</ul>
<h3 style="margin-top:20px;font-size:16px">Textbook chapters for this level</h3><div class="chips" style="margin-top:7px">{book}</div></section>'''

page("by-scale.html", "By scale: molecules to disease", f"""<section><p class="eyebrow">By scale</p><h1>Molecules → disease</h1><p class="lede">Everything I have learned, arranged by the level of the nervous system it belongs to, not by the course it came from. Each line names its source.</p>{jump}</section>{sec}""", "scale")

# ---- courses
hdr = "".join(f'<th><a href="by-scale.html#{k}" style="color:var(--{k});font:inherit">{n}</a></th>' for k, n, _, _ in SCALES)
rows = ""
for c in COURSES:
    if c["status"] == "todo":
        continue
    cells = ""
    for k, *_ in SCALES:
        v = sum(1 for o in c["outcomes"] if o[0] == k)
        inner = '<a href="courses/%s.html">%d</a>' % (c["id"], v) if v else ""
        cells += f'<td style="background:color-mix(in srgb,var(--{k}) {min(65,v*9)}%,transparent)">{inner}</td>'
    rows += f'<tr><td><a href="courses/{c["id"]}.html" style="color:var(--ink)">{E(c["title"])}</a></td>{cells}</tr>'
adc = len(AD_FINDINGS)
rows += f'<tr><td><a href="{REPO_AD}" style="color:var(--ink)">Original research: Alzheimer\'s spatial transcriptomics ↗</a></td>' + "<td></td>" * 5 + f'<td style="background:color-mix(in srgb,var(--disease) 45%,transparent)"><a href="by-scale.html#disease">{adc}</a></td></tr>'
matrix = f'<div class="scroll"><table class="matrix"><tr><th>Number of outcomes</th>{hdr}</tr>{rows}</table></div>'
def ccard(c):
    td = " todo" if c["status"] == "todo" else ""
    return f'<a class="card ccard{td}" href="courses/{c["id"]}.html"><div>{BADGE[c["status"]]}</div><h3>{E(c["title"])}</h3><small>{E(c["provider"])}</small><span style="font-size:14px">{E(c["summary"])}</span></a>'
done = "".join(ccard(c) for c in COURSES if c["status"] != "todo")
todo = "".join(ccard(c) for c in COURSES if c["status"] == "todo")
read = "".join(f'<li><p><a href="{u}">{E(t)} ↗</a></p><small style="color:var(--muted)">{E(a)}</small></li>' for t, a, u in READING)
page("courses.html", "By course", f"""<section><p class="eyebrow">By course</p><h1>Courses</h1><p class="lede">Each course has its own page with a graphical summary and learning outcomes. This grid shows where each one contributes.</p><div style="margin-top:20px">{matrix}</div></section>
<section><h2>Completed and audited</h2><div class="grid" style="margin-top:14px">{done}</div></section>
<section><h2>To be updated</h2><div class="grid" style="margin-top:14px">{todo}</div></section>
<section><h2>Reference texts</h2><p class="note">Textbook chapters are mapped to each level on the <a href="by-scale.html">By scale</a> page.</p><ul class="out">{read}</ul></section>""", "courses")

for c in COURSES:
    rel = "../"
    tut = (" · " + E(c["tutors"])) if c.get("tutors") else ""
    meta = f'<p style="margin:10px 0 0">{BADGE[c["status"]]} <span style="color:var(--muted);font-size:14px">{E(c["provider"])}{tut}</span></p>'
    proof = f'<a class="chip src" href="{c["url"]}">Official course page ↗</a>'
    if c.get("cert"):
        cc = CERTS[c["cert"]]
        proof = f'<a class="chip" href="{rel}{cc[4]}.pdf">Certificate · {cc[2]}</a><a class="chip" href="{cc[5]}">Verify with issuer ↗</a>' + proof
    if c.get("repo"): proof += f'<a class="chip" href="{c["repo"]}">Public notes repository ↗</a>'
    body = f'<section><a href="{rel}courses.html" class="eyebrow" style="text-decoration:none">← All courses</a><h1 style="font-size:clamp(28px,5vw,42px);margin-top:8px">{E(c["title"])}</h1>{meta}<p class="lede" style="font-size:19px">{E(c["summary"])}</p><div class="chips" style="margin-top:12px">{proof}</div></section>'
    if c["kind"] == "todo":
        body = body.replace(f'<p class="lede" style="font-size:19px">{E(c["summary"])}</p>', "")
        body += '<section><div class="card ccard todo"><h3>To be updated</h3><span style="font-size:14px">Learning outcomes and a graphical summary will be added here.</span></div></section>'
    else:
        g = ""
        if c["graphic"] == "uw": g = UW_ARC(rel)
        elif c["graphic"] == "jhu": g = JHU_GFX(rel)
        elif c["graphic"] == "rail": g = RAIL(c)
        demos = "".join(demo(d, rel) for d in c["demos"])
        gal = ""
        if c["id"].startswith("uw-"):
            fs = ""
            for f, cap, d, sc in FIGS:
                t, p, stem = ref(d, sc)
                fs += f'<figure><a href="{rel}figs/{f}.png"><img loading="lazy" src="{rel}figs/{f}.png" alt="{E(cap)}"></a><figcaption>{E(cap)} · <a href="{rel}notes/{stem}.pdf#page={p}">{DOCS[d][1]}, p.{p}</a></figcaption></figure>'
            gal = f'<section><h2>Figures from my notes</h2><p class="note">Plots and simulations made for the notes, separate from the lecture slides.</p><div class="gallery">{fs}</div></section>'
        groups = {}
        for o in c["outcomes"]: groups.setdefault(o[1], []).append(o)
        outs = ""
        for u, os_ in groups.items():
            lis = "".join(f'<li><p>{E(o[2])}</p><div class="chips"><a class="chip course" href="{rel}by-scale.html#{o[0]}" style="color:var(--{o[0]})">{o[0]}</a>{outcome_refs(c, o, rel)}</div></li>' for o in os_)
            outs += f'<h3 style="margin-top:22px">{E(u)}</h3><ul class="out">{lis}</ul>'
        extra_note = "The course was audited, so there is no graded work or certificate behind them." if c["status"] == "audit" else "The certificate is the evidence of completion."
        caveat = "" if c["kind"] == "notes" else f'<p class="note">These are the outcomes listed by the course. {extra_note}</p>'
        if g or demos:
            body += f'<section><h2>Graphical summary</h2>{g}{demos}</section>'
        body += gal + f'<section><h2>Learning outcomes</h2>{caveat}{outs}</section>'
    page(f'courses/{c["id"]}.html', c["title"], body, "courses", c["summary"])

# ---- certificates
order = sorted(CERTS.items(), key=lambda kv: kv[1][3])
yr = lambda d: int(d[:4]) + (int(d[5:7]) - 1) / 12 + (int(d[8:]) - 1) / 365
X = lambda v: 40 + (v - 2020) / 7 * 680
ticks = "".join(f'<line x1="{X(y):.0f}" x2="{X(y):.0f}" y1="60" y2="68" stroke="var(--muted)"/><text x="{X(y):.0f}" y="84" text-anchor="middle" font-family="var(--mono)" font-size="11" fill="var(--muted)">{y}</text>' for y in range(2020, 2028))
marks = ""
for i, (k, v) in enumerate(order):
    marks += f'<circle cx="{X(yr(v[3])) + i*5:.1f}" cy="60" r="6" fill="var(--accent)" fill-opacity=".8"/>'
marks += f'<text x="{X(2020.5):.0f}" y="38" font-size="13" font-family="var(--serif)" fill="var(--ink)">July 2020: three certificates</text><text x="{X(2026.67)+6:.0f}" y="38" text-anchor="end" font-size="13" font-family="var(--serif)" fill="var(--ink)">September 2026: Computational Neuroscience</text>'
tl = f'<svg class="diag" viewBox="0 0 760 94" role="img" aria-label="Timeline of certificates"><line x1="40" x2="720" y1="60" y2="60" stroke="var(--line)" stroke-width="2"/>{ticks}{marks}</svg>'
cards = ""
for k, v in reversed(order):
    cid = next(c["id"] for c in COURSES if c.get("cert") == k)
    cards += f'<div class="card cert"><a href="{v[4]}.pdf"><img loading="lazy" src="{v[4]}.png" alt="Certificate: {E(v[0])}"></a><h3 style="font-size:17px">{E(v[0])}</h3><small style="color:var(--muted)">{E(v[1])} · {v[2]}</small><div class="chips"><a class="chip" href="{v[4]}.pdf">PDF</a><a class="chip" href="{v[5]}">Verify with issuer ↗</a><a class="chip course" href="courses/{cid}.html">Course page</a></div></div>'
aud = "".join(f'<li><p><a href="courses/{c["id"]}.html">{E(c["title"])}</a></p><small style="color:var(--muted)">{E(c["provider"])}</small></li>' for c in COURSES if c["status"] == "audit")
page("certificates.html", "Certificates", f"""<section><p class="eyebrow">Certificates</p><h1>Certificates</h1><p class="lede">Each one can be opened as a PDF or checked directly with the issuer.</p>{tl}<div class="grid" style="margin-top:16px">{cards}</div></section>
<section><h2>Audited, without a certificate</h2><p class="note">Listed separately so that nothing here reads as a credential it is not.</p><ul class="out">{aud}</ul></section>""", "certs")
(ROOT/".nojekyll").write_text("")
print(f"built: {n_out} course outcomes, {checked} note references verified on their cited PDF page, {notes_pages} note pages")
