#!/usr/bin/env python3
"""Generates the static site. Fails if any note reference cannot be found on its cited PDF page."""
import re, subprocess, html, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import *
from pictures import PICTURES, AD_QUESTION
from icons import icon_svg
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
SHORT = {"uw-computational-neuroscience": "UW", "jhu-neuroimaging": "JHU", "uchicago-understanding-the-brain": "UChicago", "yale-introduction-to-psychology": "Yale", "harvardx-mcb80-1x": "HarvardX 1", "harvardx-mcb80-2x": "HarvardX 2", "harvardx-mcb80-3x": "HarvardX 3", "jhu-neurohacking-in-r": "JHU Neurohacking", "jhu-principles-of-fmri-1": "JHU fMRI 1", "jhu-principles-of-fmri-2": "JHU fMRI 2", "cambridge-neuropsychology-of-decision-making": "Cambridge", "cambridge-psychology-of-emotions": "Cambridge", "epflx-neuronal-dynamics-of-cognition": "EPFLx"}

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

def page(path, title, body, active="", desc="Skills, certificates and neuroscience coursework of Jagadrupa Sahoo, with the evidence attached."):
    depth = path.count("/")
    rel = "../" * depth
    links = [("index.html", "Home", "home"), ("research.html", "Research", "research"), ("skills.html", "Skills and certificates", "certs"), ("courses.html", "Neuroscience courses", "courses"), ("other-courses.html", "Other courses", "other")]
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
        o += f'<circle cx="30" cy="{y}" r="13" fill="var(--paper)" stroke="var(--accent)" stroke-width="2"/><text x="30" y="{y+4}" text-anchor="middle" font-family="var(--mono)" font-size="11" fill="var(--ink)">{i+1}</text><text x="56" y="{y+5}" font-size="14" fill="var(--ink)">{E(it[2])}</text>'
    return f'<figure class="demo" style="margin:16px 0"><h4>Course map</h4><p>Topics in the order the course teaches them.</p><div class="scroll"><svg class="diag" style="min-width:680px" viewBox="0 0 760 {h}" font-family="var(--sans)" role="img" aria-label="Course topics in order">{o}</svg></div></figure>'

# ---- home
tk_rows = ""
for label, items in TOOLKIT:
    bs = "".join(f'<span class="tb{" tc" if kind == "course" else ""}" style="--b:{col}">{icon_svg(n)}{E(n)}</span>' for n, col, kind in items)
    tk_rows += f'<div class="tkrow"><span class="tklabel">{E(label)}</span><div class="tbs">{bs}</div></div>'
tk_m = "".join(f'<p><b>{E(a)}:</b> {E(d)}</p>' for a, d in TOOLKIT_METHODS)
toolkit = f'<section><h2>Toolkit</h2><div class="tk">{tk_rows}</div><div class="tkm">{tk_m}</div><p class="note" style="margin-top:12px"><span class="tb" style="--b:var(--muted);font-size:10px;padding:2px 7px">Filled</span> used in my own projects &nbsp; <span class="tb tc" style="--b:var(--muted);font-size:10px;padding:2px 7px">Outlined</span> from audited coursework so far. The courses and certificates behind these are listed below.</p></section>'
def counts(k): return sum(1 for c, o in ALL if o[0] == k) + (len(AD_FINDINGS) if k == "disease" else 0)
n_out = len(ALL) + len(AD_FINDINGS)

# ---- courses
def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
NEURO_IDS = {c["id"] for c in COURSES}
_have = {c["cert"] for c in COURSES if c.get("cert")}
for k, v in sorted(CERTS.items(), key=lambda kv: kv[1][3], reverse=True):
    if k in _have or k == "spec": continue
    m = CERT_META[k]
    if k in OTHER_DETAIL:
        CERT_MODULES[k] = [t_ for t_, _, _ in OTHER_DETAIL[k]]
        COURSE_DETAIL[slug(v[0])] = {t_: (d_, tp_) for t_, d_, tp_ in OTHER_DETAIL[k]}
    mods = CERT_MODULES.get(k, [])
    COURSES.append(dict(id=slug(v[0]), title=v[0], provider=v[1] if "edX" in v[1] else v[1] + " · Coursera", status="cert", cert=k,
                        url=m["url"] or "https://www.coursera.org/search?query=" + v[0].replace(" ", "%20"), outcomes=[("brain", "Official course modules", x) for x in mods],
                        kind="syllabus", summary=m["summary"], graphic="rail" if mods else None, demos=[]))
for a_ in AUDITS:
    if a_["page"]: continue
    cid = slug(a_["title"]); det = {}; outs_ = []
    for l in a_["lessons"]:
        name, _, rest = l.partition(": ")
        outs_.append(("brain", "Modules", name)); det[name] = ("", [x.strip()[:1].upper() + x.strip()[1:] for x in rest.split(", ")] if rest else [])
    COURSE_DETAIL[cid] = det; a_["page"] = cid
    COURSES.append(dict(id=cid, title=a_["title"], provider=a_["provider"], status="audit", url=a_["url"], outcomes=outs_, kind="syllabus",
                        summary=AUDIT_SUMMARY.get(a_["title"], ""), graphic="rail", demos=[]))
S2M = {sk: m for m, sks in SKILL_MAJOR.items() for sk in sks}
MCOL = {k: col for k, _, col in MAJORS}
def skchip(sk):
    return f'<span class="chip sk">{E(sk)}</span>'
COURSE_SK = {}; COURSE_BR = {}
for c in COURSES:
    if c.get("cert"): COURSE_SK[c["id"]] = CERT_META[c["cert"]]["skills"]; COURSE_BR[c["id"]] = CERT_GROUP[c["cert"]]
for a_, g_ in zip(AUDITS, AUDIT_GROUP):
    if a_["page"]: COURSE_SK[a_["page"]] = a_["skills"]; COURSE_BR[a_["page"]] = g_
BRANCHES = [(f'neuro/{br["key"]}', br["name"]) for br in TREE[0]["branches"]]
def ccard(c):
    td = " todo" if c["status"] == "todo" else ""
    sk = COURSE_SK.get(c["id"], [])
    chips_ = f'<span class="chips">{"".join(skchip(x) for x in sk[:3])}{f"""<span class="chip src">+{len(sk)-3}</span>""" if len(sk) > 3 else ""}</span>' if sk else ""
    return f'<a class="card ccard{td}" href="courses/{c["id"]}.html"><div>{BADGE[c["status"]]}</div><h3>{E(c["title"])}</h3><small>{E(c["provider"])}</small><span style="font-size:14px">{E(c["summary"])}</span>{chips_}</a>'
done = ""
other = ""
for bk, bn in BRANCHES:
    cs = [c for c in COURSES if c["status"] != "todo" and COURSE_BR.get(c["id"]) == bk]
    if cs:
        nc = sum(c["status"] == "cert" for c in cs); na = len(cs) - nc
        sub = " · ".join(x for x in [f"{nc} certified" if nc else "", f"{na} audited" if na else ""] if x)
        done += f'<div class="cgroup" style="--c:var(--neurons);margin-top:22px"><h4 id="{bk.split("/")[1]}">{E(bn)} <small>{sub}</small></h4><div class="grid" style="margin-top:10px">{"".join(ccard(c) for c in cs)}</div></div>'
assert all(c["id"] in COURSE_BR for c in COURSES if c["status"] != "todo")
for t in TREE[1:]:
    sec_ = ""
    for br in t["branches"]:
        g_ = f'{t["key"]}/{br["key"]}'
        cs = [c for c in COURSES if COURSE_BR.get(c["id"]) == g_]
        if cs:
            nc = sum(c["status"] == "cert" for c in cs); na = len(cs) - nc
            sub = " · ".join(x for x in [f"{nc} certified" if nc else "", f"{na} audited" if na else ""] if x)
            sec_ += f'<div class="cgroup" style="margin-top:22px"><h4>{E(br["name"])} <small>{sub}</small></h4><div class="grid" style="margin-top:10px">{"".join(ccard(c) for c in cs)}</div></div>'
    if sec_: other += f'<div style="--c:var(--{t["col"]})"><h3 class="ah" style="margin-top:{44 if other else 10}px">{E(t["name"])}</h3>{sec_}</div>'
AREA_COL = {t["key"]: t["col"] for t in TREE}
todo = "".join(ccard(c) for c in COURSES if c["status"] == "todo")
read = "".join(f'<li><p><a href="{u}">{E(t)} ↗</a></p><small style="color:var(--muted)">{E(a)}</small></li>' for t, a, u in READING)
page("other-courses.html", "Other courses", f"""<section><p class="eyebrow">Other courses</p><h1>Other courses</h1><p class="lede">Courses outside neuroscience that I have completed or audited: deep learning and machine learning, bioinformatics and biotechnology.</p></section>
<section><p class="note">Grouped and coloured as on the <a href="skills.html">summary map</a>. Each course has its own page with its modules, skills and certificate.</p>{other}</section>""", "other")
page("courses.html", "Neuroscience courses", f"""<section><p class="eyebrow">Neuroscience courses</p><h1>Neuroscience courses</h1><p class="lede">Every neuroscience course I have completed or audited. Each has its own page with a graphical summary, learning outcomes and skills.</p></section>
<section><h2>Completed and audited</h2><p class="note">Grouped as on the <a href="skills.html">summary map</a>. Each card shows the first skills listed for the course.</p>{done}</section>
<section><h2>To be updated</h2><div class="grid" style="margin-top:14px">{todo}</div></section>
<section><h2>Reference texts</h2><ul class="out">{read}</ul></section>""", "courses")

for cid_, d_ in COURSE_DETAIL.items():
    assert set(d_) <= {o[2] for c in COURSES if c["id"] == cid_ for o in c["outcomes"]}, cid_
for c in COURSES:
    rel = "../"
    tut = (" · " + E(c["tutors"])) if c.get("tutors") else ""
    meta = f'<p style="margin:10px 0 0">{BADGE[c["status"]]} <span style="color:var(--muted);font-size:14px">{E(c["provider"])}{tut}</span></p>'
    proof = f'<a class="chip src" href="{c["url"]}">Official course page ↗</a>'
    if c.get("cert"):
        cc = CERTS[c["cert"]]
        proof = f'<a class="chip" href="{rel}{cc[4]}.pdf">Certificate · {cc[2]}</a><a class="chip" href="{cc[5]}">Verify with issuer ↗</a>' + proof
    skl = f'<p class="eyebrow" style="margin:18px 0 6px">Skills</p><div class="chips">{"".join(skchip(x) for x in COURSE_SK[c["id"]])}</div>' if c["id"] in COURSE_SK else ""
    if c.get("repo"): proof += f'<a class="chip" href="{c["repo"]}">Public notes repository ↗</a>'
    body = f'<section><a href="{rel}{"courses.html" if c["id"] in NEURO_IDS else "other-courses.html"}" class="eyebrow" style="text-decoration:none">← {"Neuroscience courses" if c["id"] in NEURO_IDS else "Other courses"}</a><h1 style="font-size:clamp(28px,5vw,42px);margin-top:8px">{E(c["title"])}</h1>{meta}<p class="lede" style="font-size:19px">{E(c["summary"])}</p><div class="chips" style="margin-top:12px">{proof}</div>{skl}</section>'
    if c["kind"] == "todo":
        body = body.replace(f'<p class="lede" style="font-size:19px">{E(c["summary"])}</p>', "")
        body += '<section><div class="card ccard todo"><h3>To be updated</h3><span style="font-size:14px">Learning outcomes and a graphical summary will be added here.</span></div></section>'
    else:
        g = ""
        if c["graphic"] == "uw": g = UW_ARC(rel)
        elif c["graphic"] == "jhu": g = JHU_GFX(rel)
        elif c["graphic"] == "rail": g = RAIL(c)
        pk = c["id"] if c["id"] in PICTURES else c["title"]
        if pk in PICTURES:
            pt, pc, ps = PICTURES[pk]
            g = f'<figure class="demo" style="margin:16px 0"><h4>{E(pt)}</h4><p>{E(pc)}</p>{ps}</figure>'
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
            det = COURSE_DETAIL.get(c["id"], {})
            def more(o):
                if o[2] not in det: return ""
                d, tp = det[o[2]]
                if not d and not tp: return ""
                if not tp: return f'<p class="od">{E(d)}</p>'
                if not d: return f'<div class="leaves" style="--c:var(--accent);margin:8px 0 4px;padding:0;border:0">{"".join(f"<span>{E(x)}</span>" for x in tp)}</div>'
                return f'<p class="od">{E(d)}</p><div class="leaves" style="--c:var(--accent);margin:8px 0 4px;padding:0;border:0">{"".join(f"<span>{E(x)}</span>" for x in tp)}</div>'
            refs = (lambda o: f'<div class="chips">{outcome_refs(c, o, rel)}</div>') if c["kind"] == "notes" else (lambda o: "")
            lis = "".join(f'<li><p>{E(o[2])}</p>{more(o)}{refs(o)}</li>' for o in os_)
            outs += f'<h3 style="margin-top:22px">{E(u)}</h3><ul class="out">{lis}</ul>'
        extra_note = "The course was audited, so there is no graded work or certificate behind them." if c["status"] == "audit" else "The certificate is the evidence of completion."
        caveat = "" if c["kind"] == "notes" else f'<p class="note">These are the outcomes listed by the course. {extra_note}</p>'
        if g:
            body += f'<section><h2>Graphical summary</h2>{g}</section>'
        mods = ""
        if c["id"] in COURSE_MODULES:
            ml = "".join(f'<li><p>{E(t)}</p><p class="od">{E(d)}</p><div class="leaves" style="--c:var(--accent);margin:8px 0 4px;padding:0;border:0">{"".join(f"<span>{E(x)}</span>" for x in tp)}</div></li>' for t, d, tp in COURSE_MODULES[c["id"]])
            mods = f'<h3 style="margin-top:22px">Official course modules</h3><ul class="out">{ml}</ul><h3 style="margin-top:34px">Outcomes from my own notes</h3><p class="note">Each outcome links to the page of my notes that covers it.</p>'
        if outs or mods: body += f'<section><h2>Learning outcomes</h2>{caveat}{mods}{outs}</section>'
        if demos:
            body += f'<section><h2>Interactive simulations</h2><p class="note">Small models of ideas from the course, with illustrative parameters.</p>{demos}</section>'
        body += gal
    col_ = AREA_COL.get(COURSE_BR.get(c["id"], "neuro/x").split("/")[0], "neurons")
    page(f'courses/{c["id"]}.html', c["title"], f'<div style="--c:var(--{col_})">{body}</div>', "courses" if c["id"] in NEURO_IDS else "other", c["summary"])

# ---- Alzheimer's project
_steps = "".join(f'<li><p>{E(t)}</p><p class="od">{E(d)}</p></li>' for t, d in AD_STEPS)
_key = "".join(f'<div class="finding"><div><p class="eyebrow">Finding {i + 1}</p><h3>{E(t)}</h3><p>{E(d)}</p><div class="chips"><a class="chip" href="{REPO_AD}{a}">Evidence in the repository ↗</a></div></div>'
               f'<figure><a href="figs/{f}.png"><img loading="lazy" src="figs/{f}.png" alt="{E(cap)}"></a><figcaption>{E(cap)}</figcaption></figure></div>' for i, (t, d, f, cap, a) in enumerate(AD_KEY))
page("alzheimers-project.html", "Alzheimer's project: spatial transcriptomics of human cortex", f"""<div style="--c:var(--neurons)"><section><a href="research.html" class="eyebrow" style="text-decoration:none">← Research</a><p class="eyebrow" style="margin-top:14px">Independent research project · 2026</p><h1 style="font-size:clamp(30px,5vw,46px)">Spatial transcriptomics of human Alzheimer's cortex</h1>
<div class="chips" style="margin-top:14px"><a class="chip" href="{REPO_AD}">Code, notebooks and report on GitHub ↗</a></div>
<nav class="jump" aria-label="Sections of this page"><a href="#introduction">Introduction</a><a href="#data">Data</a><a href="#methods">Methods</a><a href="#findings">Key findings</a><a href="#biology">Biological analysis</a><a href="#ml">Machine learning</a><a href="#conclusion">Conclusion</a><a href="#limitations">Limitations</a><a href="#tools">Tools</a></nav></section>
<section id="introduction"><h2>Introduction</h2>
<div class="intro3"><div class="card"><p class="eyebrow">The problem</p><p>Alzheimer's disease does not damage the brain evenly. Some cell populations and regions fail early while their neighbours hold on for years, and why is still not understood.</p></div>
<div class="card"><p class="eyebrow">The approach</p><p>Spatial transcriptomics measures gene activity in each cell while keeping the cell in its place in the tissue. I compared one Alzheimer's section of human cortex with a matched healthy one.</p></div>
<div class="card"><p class="eyebrow">The main result</p><p>The oligodendrocyte lineage, the cells that make myelin, is the dominant axis of disruption: more numerous, less mature and concentrated in the pathological zones.</p></div></div>
<figure class="demo qfig"><div class="scroll">{AD_QUESTION}</div></figure>
<h3 class="mlh">The questions, set before the analysis</h3>
<div class="qgrid">{"".join(f'<div class="card qc" style="--c:var(--{col})"><span class="qn">{i + 1}</span><h4>{E(t)}</h4><p>{E(q)}</p></div>' for i, (t, q, col) in enumerate(AD_QUESTIONS))}</div>
<div class="stats"><div class="stat"><b>44,955</b><span>cells in the Alzheimer's section</span></div><div class="stat"><b>24,406</b><span>cells in the matched healthy section</span></div><div class="stat"><b>19.7 → 36.0%</b><span>oligodendrocyte share, healthy to Alzheimer's</span></div><div class="stat"><b>58% vs 15%</b><span>oligodendrocytes in AD-hot against preserved zones</span></div></div></section>
<section id="data"><h2>Data</h2><p style="margin:10px 0 0">The public <a href="{REPO_AD}#dataset">10x Genomics Xenium In Situ human brain dataset</a>: one Alzheimer's and one matched healthy cortical section, prepared and processed the same way.</p></section>
<section id="methods"><h2>Methods</h2><ol class="out" style="list-style:none">{_steps}</ol></section>
<section id="findings"><h2>Key findings</h2>{_key}</section>
<section id="biology"><h2>Biological analysis</h2><div class="prose"><p>The first half of the project asked:</p>
<p class="mlq">How is the cellular architecture of human cortex reorganised in Alzheimer's disease, and is that reorganisation spatially structured?</p></div>
<div class="grid" style="margin-top:18px"><div class="card"><h3 style="font-size:17px">Analyses</h3><ul class="mll"><li>Cell-type composition and marker scores</li><li>Neighbourhood enrichment</li><li>Spatial autocorrelation (Moran's I)</li><li>Spatial zoning by a pathology index</li><li>Differential expression by zone and cell type</li><li>Pseudotime along the oligodendrocyte lineage</li></ul></div>
<div class="card"><h3 style="font-size:17px">How the comparison was kept honest</h3><ul class="mll"><li>The two sections were clustered and annotated separately</li><li>Zones are compared within the Alzheimer's section, not across sections</li><li>Effects are tested within each cell type, to separate them from composition</li><li>Core claims are checked against an independent atlas</li></ul></div></div>
<h3 class="mlh">Composition</h3><p class="note">Share of annotated cells in each section.</p><div class="scroll"><table class="plain"><tr><th>Cell type</th><th>Healthy</th><th>Alzheimer's</th></tr><tr><td><b>Oligodendrocytes</b></td><td>19.7%</td><td><b>36.0%</b></td></tr><tr><td>Excitatory neurons</td><td>28.8%</td><td>25.1%</td></tr><tr><td>Astrocytes</td><td>13.0%</td><td>10.4%</td></tr><tr><td>Inhibitory neurons (all subtypes)</td><td>13.5%</td><td>8.1%</td></tr><tr><td>Endothelial cells</td><td>10.8%</td><td>7.4%</td></tr><tr><td>Microglia</td><td>6.5%</td><td>7.2%</td></tr><tr><td>Oligodendrocyte precursors (OPC)</td><td>3.8%</td><td>5.7%</td></tr></table></div><div class="prose"><p>Oligodendrocytes nearly double their share while every neuronal and vascular class shrinks. Each oligodendrocyte is also less oligodendrocyte-like: the median marker score falls from about 3.2 to about 1.1, although the two sections use partly different marker sets, so that comparison is weighted with care.</p></div>
<h3 class="mlh">Spatial organisation</h3><p class="note">Neighbourhood enrichment (z-scores) and spatial autocorrelation of cell-type marker scores (Moran's I).</p><div class="scroll"><table class="plain"><tr><th>Relationship</th><th>Healthy</th><th>Alzheimer's</th></tr><tr><td>Oligodendrocytes with themselves</td><td>+19.97</td><td><b>+78.41</b></td></tr><tr><td>Oligodendrocytes with excitatory neurons</td><td>−11.91</td><td><b>−44.46</b></td></tr></table></div><div class="scroll" style="margin-top:12px"><table class="plain"><tr><th>Marker score, Moran's I</th><th>Healthy</th><th>Alzheimer's</th></tr><tr><td><b>Oligodendrocytes</b></td><td>0.272</td><td><b>0.463</b></td></tr><tr><td>Excitatory neurons</td><td>0.279</td><td>0.305</td></tr><tr><td>Astrocytes</td><td>0.157</td><td>0.294</td></tr><tr><td>Microglia</td><td>0.081</td><td>0.113</td></tr><tr><td>Endothelial cells</td><td>0.058</td><td>0.097</td></tr><tr><td>OPC</td><td>0.124</td><td>0.050</td></tr></table></div><figure class="mlfig"><a href="figs/ad-b1_niche_enrichment.png"><img loading="lazy" src="figs/ad-b1_niche_enrichment.png" alt="Neighbourhood enrichment between cell types, Alzheimer's section"></a><figcaption>Neighbourhood enrichment between cell types, Alzheimer's section</figcaption></figure><div class="prose"><p>In healthy tissue, oligodendrocytes and neurons avoid each other mildly, as white and grey matter should. In the Alzheimer's section oligodendrocytes become a strongly self-segregating domain that avoids nearly every other cell type, and their spatial co-occurrence with excitatory neurons falls from 0.974 to 0.669.</p></div>
<h3 class="mlh">Spatial zoning</h3><p class="note">A transcriptional pathology index splits the Alzheimer's section into three zones of roughly equal size.</p><div class="scroll"><table class="plain"><tr><th>Zone</th><th>Cells</th><th>Oligodendrocyte share</th><th>Genes raised in the zone</th></tr><tr><td><b>AD-hot</b></td><td>12,334</td><td><b>about 58%</b></td><td>SERPINA3, SPP1, CRYAB, MOBP, CLDND1, CA2, UGT8, ERMN</td></tr><tr><td>Mixed</td><td>12,708</td><td></td><td></td></tr><tr><td>Preserved</td><td>12,334</td><td>about 15%</td><td>RORB, WIF1, PVALB, LAMP5, CUX2, HTR2A, CEMIP, SLC17A6</td></tr></table></div><figure class="mlfig"><a href="figs/ad-b2_zone_composition.png"><img loading="lazy" src="figs/ad-b2_zone_composition.png" alt="Cell-type composition of each zone"></a><figcaption>Cell-type composition of each zone</figcaption></figure><div class="prose"><p>The oligodendrocyte excess is not spread through the tissue: it lives in the AD-hot zones. Preserved zones are more than half neuronal and keep the identity of upper-layer excitatory neurons. Of 117 genes that differ between zones, 42 are higher in AD-hot and 59 in preserved, a balanced split.</p></div>
<h3 class="mlh">The zone effect within each cell type</h3><p class="note">AD-hot against preserved, tested separately in five cell types, so that composition cannot explain the result.</p><div class="scroll"><table class="plain"><tr><th>Cell type</th><th>Significant genes</th><th>Higher in AD-hot</th><th>Higher in preserved</th><th>Top genes higher in AD-hot</th></tr><tr><td><b>Oligodendrocytes</b></td><td>21</td><td>9</td><td>1</td><td>SERPINA3, GFAP, SPP1, MOBP, S100B</td></tr><tr><td>Excitatory neurons</td><td>41</td><td>24</td><td>5</td><td>SPP1, CRYAB, GFAP, MOBP, HS3ST4</td></tr><tr><td>Astrocytes</td><td>37</td><td>19</td><td>12</td><td>SERPINA3, SPP1, CRYAB, MOBP, GFAP</td></tr><tr><td>Inhibitory neurons</td><td>32</td><td>16</td><td>12</td><td>SPP1, CRYAB, MOBP, UGT8, CLDND1</td></tr><tr><td>Microglia</td><td>27</td><td>13</td><td>9</td><td>SPP1, CRYAB, MOBP, GFAP, CD74</td></tr></table></div><div class="prose"><p>SPP1, CRYAB, GFAP and MOBP are raised in AD-hot zones in all five cell types, so they mark the local environment and not a lineage. SERPINA3 is the exception: it stays restricted to oligodendrocytes and astrocytes. CRYAB, usually described as a glial stress chaperone, is the strongest signal in both neuronal types, which points to a neuronal stress response inside the affected zones.</p></div>
<h3 class="mlh">Maturation of the oligodendrocyte lineage</h3><p class="note">Mean pseudotime from precursor to mature oligodendrocyte.</p><div class="scroll"><table class="plain"><tr><th>Section</th><th>Cell type</th><th>Cells</th><th>Mean pseudotime</th></tr><tr><td>Healthy</td><td>Oligodendrocytes</td><td>4,560</td><td><b>0.490</b></td></tr><tr><td>Healthy</td><td>OPC</td><td>890</td><td>0.167</td></tr><tr><td>Alzheimer's</td><td>Oligodendrocytes</td><td>13,461</td><td><b>0.075</b></td></tr><tr><td>Alzheimer's</td><td>OPC</td><td>2,124</td><td>0.091</td></tr></table></div><div class="prose"><p>Alzheimer's oligodendrocytes sit at about one sixth of the healthy maturation position and barely separate from their precursors: numerically expanded, developmentally stalled. Pseudotime is not comparable in absolute units between separately embedded datasets, so the size of the shift is indicative; the loss of separation is the result.</p></div>
<h3 class="mlh">External validation</h3><p class="note">The same genes in oligodendrocytes of SEA-AD, an independent whole-transcriptome atlas, along disease progression.</p><div class="scroll"><table class="plain"><tr><th>Finding</th><th>Gene</th><th>Log fold change</th><th>FDR</th></tr><tr><td>Chaperone stress response up</td><td>CRYAB</td><td>+0.32</td><td>0.032</td></tr><tr><td>Reactive glial programme up</td><td>GFAP</td><td>+0.91</td><td>0.0063</td></tr><tr><td>Stress marker up</td><td>SPP1</td><td>+0.43</td><td>0.014</td></tr><tr><td>α-synuclein up with progression</td><td>SNCA</td><td>+0.03</td><td>0.044</td></tr><tr><td><b>Myelin gene down</b></td><td><b>MAG</b></td><td><b>−0.20</b></td><td><b>0.019</b></td></tr><tr><td>Calcium buffer down</td><td>S100B</td><td>−0.35</td><td>0.0048</td></tr><tr><td>Myelin gene down</td><td>MOBP</td><td>−0.32</td><td>0.083 (not significant)</td></tr></table></div><div class="prose"><p>The core oligodendrocyte claims hold in a different cohort measured on a different platform. The direct section-against-section expression comparison does not, and the project reports it as confounded by the detection gap between the two sections.</p></div></section>
<section id="ml"><h2>Machine learning</h2><div class="prose"><p>After the cell types had been annotated, the project asked a second question:</p>
<p class="mlq">Can supervised machine learning classify cell types from expression-derived, marker-signature, quality-control and spatial-context features, and does that transfer across tissue regions and across disease state?</p>
<p>Cells in the ambiguous mixed clusters were excluded from training, because there is no reliable label to score them against.</p></div>
<div class="grid" style="margin-top:18px"><div class="card"><h3 style="font-size:17px">Features</h3><ul class="mll"><li>Expression-derived PCA components</li><li>Quality-control metrics</li><li>Spatial coordinates</li><li>Marker signature scores</li><li>Neighbour-averaged marker scores (Squidpy)</li></ul></div>
<div class="card"><h3 style="font-size:17px">Models</h3><ul class="mll"><li>Logistic regression</li><li>Calibrated linear SVM</li><li>Random forest</li><li>Extra trees</li><li>Histogram gradient boosting</li></ul></div></div>
<h3 class="mlh">Random split</h3><p class="note">A stratified random split of cells within each section.</p><div class="scroll"><table class="plain"><tr><th>Model</th><th>Alzheimer's macro F1</th><th>Healthy macro F1</th></tr><tr><td><b>Histogram gradient boosting</b></td><td><b>0.9121</b></td><td><b>0.9445</b></td></tr><tr><td>Random forest</td><td>0.8668</td><td>0.9343</td></tr><tr><td>Calibrated linear SVM</td><td>0.8529</td><td>0.9335</td></tr><tr><td>Logistic regression</td><td>0.8480</td><td>0.9443</td></tr><tr><td>Extra trees</td><td>0.8467</td><td>0.9353</td></tr></table></div><div class="prose"><p>On the healthy section all five models perform within a narrow band, so the cell types are close to linearly separable. On the Alzheimer's section boosting pulls clearly ahead and logistic regression falls from joint best to among the weakest. Expression components are the most important features in both sections; spatial coordinates and neighbour features rank last.</p></div>
<h3 class="mlh">Spatial hold-out</h3><p class="note">Each section is divided into nine spatially compact blocks, and each block is held out in turn: 5 models × 4 feature sets × 9 blocks = 180 folds per section.</p><div class="scroll"><table class="plain"><tr><th>Model</th><th>Alzheimer's macro F1</th><th>Alzheimer's accuracy</th><th>Healthy macro F1</th><th>Healthy accuracy</th></tr><tr><td><b>Histogram gradient boosting</b></td><td><b>0.9053</b></td><td>0.9235</td><td><b>0.9574</b></td><td>0.9637</td></tr><tr><td>Random forest</td><td>0.8702</td><td>0.8949</td><td>0.9464</td><td>0.9534</td></tr><tr><td>Extra trees</td><td>0.8492</td><td>0.8756</td><td>0.9462</td><td>0.9527</td></tr><tr><td>Calibrated linear SVM</td><td>0.8427</td><td>0.8745</td><td>0.9419</td><td>0.9508</td></tr><tr><td>Logistic regression</td><td>0.8419</td><td>0.8661</td><td>0.9494</td><td>0.9574</td></tr></table></div><div class="scroll" style="margin-top:12px"><table class="plain"><tr><th>Feature set (Alzheimer's section)</th><th>Included features</th><th>Macro F1</th></tr><tr><td>expression_qc_marker</td><td>PCA + QC + marker scores</td><td><b>0.8648</b></td></tr><tr><td>expression_qc_marker_spatial</td><td>+ spatial coordinates</td><td>0.8622</td></tr><tr><td>expression_qc_marker_neighbor</td><td>+ neighbour marker scores</td><td>0.8610</td></tr><tr><td>full_spatial_context</td><td>+ coordinates and neighbour scores</td><td>0.8596</td></tr></table></div><figure class="mlfig"><a href="figs/ad-ml1_spatial_holdout.png"><img loading="lazy" src="figs/ad-ml1_spatial_holdout.png" alt="Spatial hold-out summary, Alzheimer's section"></a><figcaption>Spatial hold-out summary, Alzheimer's section</figcaption></figure><div class="prose"><p>Holding out whole regions costs almost nothing compared with the random split (0.9121 to 0.9053 for the best model), so the classifier is learning expression identity and not memorising position. Adding spatial features does not help; it very slightly hurts.</p></div>
<h3 class="mlh">Transfer between the two sections</h3><p class="note">The hardest test: train on one section and test on the other, with labels harmonised to six shared classes.</p><div class="scroll"><table class="plain"><tr><th>Model</th><th>Mean macro F1</th></tr><tr><td><b>Extra trees</b></td><td><b>0.554</b></td></tr><tr><td>Voting ensemble</td><td>0.549</td></tr><tr><td>Histogram gradient boosting</td><td>0.539</td></tr><tr><td>Random forest</td><td>0.537</td></tr><tr><td>Calibrated linear SVM</td><td>0.445</td></tr><tr><td>Logistic regression</td><td>0.429</td></tr></table></div><figure class="mlfig"><a href="figs/ad-ml2_cross_section_models.png"><img loading="lazy" src="figs/ad-ml2_cross_section_models.png" alt="Cross-section macro F1 by model"></a><figcaption>Cross-section macro F1 by model</figcaption></figure><div class="prose"><p>Performance falls from about 0.92 within a section to about 0.55 across disease state. The direction matters: training on the Alzheimer's section and testing on the healthy one reaches a macro F1 of about 0.59, while the reverse reaches about 0.43, for every model family tested. Alzheimer's tissue contains a broader range of cell states, so a model trained on it has already seen the healthy states; trained the other way, the disease states are new to it.</p>
<p>The practical conclusion is that transferring cell-type labels from a healthy reference to diseased tissue should not be assumed to work. This is still a comparison of two sections, so true generalisation needs more donors.</p></div></section>
<section id="conclusion"><h2>Conclusion</h2><div class="prose"><p>Taken together, the findings point one way. In this tissue the oligodendrocyte lineage is more numerous, less mature, less coherent in its myelin programme, and concentrated in the zones where pathology-associated genes are highest. The change is spatially organised and not uniform, and the most disturbed zones impose a shared signature on every cell type living in them.</p>
<p>The project compares one section per condition, so it cannot say how general this is or what comes first. What it does show is that the core oligodendrocyte signal survives a test against an independent atlas, and that a careful spatial analysis can separate what is robust from what is an artefact of the measurement. The next step is to repeat the analysis across more donors and across disease stages.</p></div></section>
<section id="limitations"><h2>Limitations</h2><p class="note">Stated in the repository before any result. This is research and a portfolio project, not a clinical tool.</p><ul class="out">{"".join(f"<li><p style='font-weight:400'>{E(x)}</p></li>" for x in AD_LIMITS)}</ul></section>
<section id="tools"><h2>Tools</h2><div class="chips" style="margin-top:10px">{"".join(skchip(x) for x in AD_TOOLS)}</div></section></div>""", "research", "An independent analysis of 10x Xenium spatial transcriptomics of human Alzheimer's cortex.")

# ---- research page
def rcard(t, when, status, summary, methods, links=()):
    lk = "".join(f'<a class="btn" href="{u}">Open the project →</a>' if l == "Project page" else f'<a class="chip" href="{u}">{E(l)}</a>' for l, u in links)
    big = " rc1" if any(l == "Project page" for l, _ in links) else ""
    return f'<article class="card rc{big}"><p class="eyebrow">{E(when)} · {E(status)}</p><h3>{E(t)}</h3><p>{E(summary)}</p><div class="leaves" style="margin:10px 0 0;padding:0;border:0">{"".join(f"<span>{E(x)}</span>" for x in methods)}</div>{f"""<div class="chips" style="margin-top:12px;align-items:center">{lk}</div>""" if lk else ""}</article>'
_indep = "".join(rcard(*r) for r in RESEARCH_INDEP)
_tum = "".join(rcard(t, role, st, "", ms) for t, role, st, ms in OMICS_PROJECTS)
_tm = "".join(f'<div class="card"><h3 style="font-size:17px">{E(t)}</h3><p style="margin:8px 0 0;font-size:14.5px">{E(d)}</p></div>' for t, d in TUM_METHODS)
_early = "".join(rcard(t, when, "", s, ms, lk).replace(" · </p>", "</p>") for t, when, s, ms, lk in RESEARCH_EARLIER)
page("research.html", "Research", f"""<section><p class="eyebrow">Research</p><h1>Research</h1><p class="lede">My research so far: independent projects in spatial transcriptomics, multi-omics research at the Technical University of Munich, and the research I did during my studies.</p>
<nav class="jump" aria-label="Sections of this page"><a href="#independent">Independent projects</a><a href="#tum">Research at TUM</a><a href="#studies">Research during my studies</a></nav></section>
<section id="independent" style="--c:var(--neurons)"><h2>Independent projects</h2><p class="note">Designed, analysed and written up on my own. Code and reports are public where a repository is linked.</p><div class="rcs">{_indep}</div></section>
<section id="tum" style="--c:var(--networks)"><h2>Research at the Technical University of Munich</h2><p class="note">2023 to 2026, on microbial sulfur metabolism in chronic intestinal inflammation and colitis-associated cancer, within Collaborative Research Centre 1371. Manuscripts are in preparation, with submission planned for 2027.</p>
<div class="rcs">{_tum}</div>
<h3 class="mlh">Methods I developed and applied</h3><div class="grid" style="margin-top:12px">{_tm}</div>
<h3 class="mlh">Talks and posters</h3><ul class="out"><li><p style="font-weight:400">Talk at the Seeon conference, 2025: Westernized diets exacerbate tumorigenesis by expanding H₂S-producing Desulfovibrio in murine models of Atf6-driven colon cancer.</p></li><li><p style="font-weight:400">Talk at the Collaborative Research Centre 1371 retreat, 2025.</p></li><li><p style="font-weight:400">Three poster presentations.</p></li></ul></section>
<section id="studies" style="--c:var(--brain)"><h2>Research during my studies</h2><p class="note">Projects completed as part of my MSc at the University of Manchester and my BSc at Amity University.</p><div class="rcs">{_early}</div></section>""", "research", "Research projects of Jagadrupa Sahoo: spatial transcriptomics, multi-omics and genetics.")

# ---- certificates
assert set(CERT_META) == set(CERTS) == set(CERT_GROUP), "certificate tables out of step"
assert len(AUDIT_GROUP) == len(AUDITS)
S2M = {sk: m for m, sks in SKILL_MAJOR.items() for sk in sks}
MCOL = {k: col for k, _, col in MAJORS}
def skchip(sk):
    return f'<span class="chip sk">{E(sk)}</span>'
def ol(label, items):
    return f'<p class="dl">{E(label)}</p><ol>{"".join(f"<li>{E(x)}</li>" for x in items)}</ol>' if items else ""
groups = {}
for k, v in sorted(CERTS.items(), key=lambda kv: kv[1][3], reverse=True):
    m = CERT_META[k]
    for sk in m["skills"]: assert sk in S2M, sk
    cid = next((c["id"] for c in COURSES if c.get("cert") == k), None)
    thumb = f'<img class="thumb" loading="lazy" src="{v[4]}.png" alt="">' if v[4] else '<span class="thumb ph">Verified<br>on edX</span>'
    links = (f'<a class="chip" href="{v[4]}.pdf">Certificate PDF</a>' if v[4] else "") + f'<a class="chip" href="{v[5]}">Verify with issuer ↗</a>'
    if cid: links += f'<a class="chip course" href="courses/{cid}.html">Course page</a>'
    if m["url"]: links += f'<a class="chip src" href="{m["url"]}">Official course page ↗</a>'
    big = f'<a href="{v[4]}.pdf"><img class="big" loading="lazy" src="{v[4]}.png" alt="Certificate: {E(v[0])}"></a>' if v[4] else ""
    card = f'<details class="card ccd"><summary>{thumb}<span class="cs"><span class="ct">{E(v[0])}</span><small>{E(v[1])} · {v[2]}</small><span class="chips">{"".join(skchip(s) for s in m["skills"][:4])}</span></span></summary><div class="cd"><p>{E(m["summary"])}</p>{ol("Modules", CERT_MODULES.get(k))}<p class="dl">Skills listed by the course</p><div class="chips">{"".join(skchip(s) for s in m["skills"])}</div>{big}<div class="chips">{links}</div></div></details>'
    groups.setdefault(CERT_GROUP[k], []).append(card)
n_cert = {g: len(c) for g, c in groups.items()}
for a, g in zip(AUDITS, AUDIT_GROUP):
    for sk in a["skills"]: assert sk in S2M, sk
    links = (f'<a class="chip course" href="courses/{a["page"]}.html">Course page</a>' if a["page"] else "") + f'<a class="chip src" href="{a["url"]}">Official course page ↗</a>'
    card = f'<details class="card ccd"><summary><span class="thumb ph au">Audited<br>no certificate</span><span class="cs"><span class="ct">{E(a["title"])}</span><small>{E(a["provider"])}</small><span class="chips">{"".join(skchip(s) for s in a["skills"][:4])}</span></span></summary><div class="cd">{PICTURES[a["title"]][2] if a["title"] in PICTURES else ""}{ol(a["lessons_label"], a["lessons"])}<p class="dl">Skills</p><div class="chips">{"".join(skchip(s) for s in a["skills"])}</div><div class="chips">{links}</div></div></details>'
    groups.setdefault(g, []).append(card)
tree = ""; lists = ""
for i, t in enumerate(TREE):
    col = t["col"]; kids = ""; sec = ""; total = 0
    for br in t["branches"]:
        g = f'{t["key"]}/{br["key"]}'; n = len(groups.get(g, [])); total += n
        cnt = f'<small>{n} course{"s" if n != 1 else ""}</small>' if n else ""
        href = f'#g-{t["key"]}-{br["key"]}' if n else br.get("link")
        pill = f'<a class="bpill" href="{href}">{E(br["name"])}{cnt}</a>' if href else f'<span class="bpill">{E(br["name"])}</span>'
        src = f'<span class="bsrc">{E(br["note"])}</span>' if br.get("note") else ""
        pj = ""
        if br.get("projects"):
            items = "".join(f'<div class="pj"><p>{E(t0)}</p><small>{E(role)} · {E(st)}</small><div class="leaves">{"".join(f"<span>{E(x)}</span>" for x in ms)}</div></div>' for t0, role, st, ms in br["projects"])
            pj = f'<details class="proj"><summary>{E(br.get("projects_label", "Research projects"))} ({len(br["projects"])})</summary>{items}</details>'
        kids += f'<div class="tbr"><div class="bhead">{pill}{src}</div><div class="leaves">{"".join(f"<span>{E(x)}</span>" for x in br["leaves"])}</div>{pj}</div>'
        if n:
            nc = n_cert.get(g, 0); sub = f"{nc} certified" + (f" · {n-nc} audited" if n - nc else "") if nc else f"{n} audited"
            sec += f'<h4 id="g-{t["key"]}-{br["key"]}">{E(br["name"])} <small>{sub}</small></h4><div class="ccds">{"".join(groups[g])}</div>'
    op = i == 0
    tree += f'<div class="tn" style="--c:var(--{col})"><button type="button" class="tpill" aria-expanded="{"true" if op else "false"}"><span class="tw">{E(t["name"])}</span><small>{len(t["branches"])} branches{f" · {total} courses" if total else ""}</small></button><div class="tkids"{"" if op else " hidden"}><p class="tnote">{E(t["note"])}</p>{kids}</div></div>'
    if sec: lists += f'<div class="mgroup" style="--c:var(--{col})"><h3>{E(t["name"])}</h3>{sec}</div>'
assert sum(len(v) for v in groups.values()) == len(CERTS) + len(AUDITS)
n_inst = len({x.strip() for v in CERTS.values() for x in v[1].replace(" · edX", "").split(" and ")})
js = "<script>(function(){var p=document.querySelectorAll('.tpill');function set(b,o){b.setAttribute('aria-expanded',o);b.nextElementSibling.hidden=!o}p.forEach(function(b){b.addEventListener('click',function(){set(b,b.getAttribute('aria-expanded')!=='true')})});var a=document.getElementById('tall');a.addEventListener('click',function(){var o=a.dataset.o!=='1';p.forEach(function(b){set(b,o)});a.dataset.o=o?'1':'';a.textContent=o?'Collapse all':'Expand all'})})();</script><noscript><style>.tkids[hidden]{display:block!important}</style></noscript>"
def _educard(t, inst, yrs, res, col, docs):
    d = "".join(f'<a class="edoc" href="education/{f}.jpg"><img loading="lazy" src="education/{f}-thumb.jpg" alt="{E(l)}"><span>{E(l)}</span></a>' for l, f in docs)
    return f'<article class="card edu" style="--c:var(--{col})"><p class="eyebrow">{E(yrs)}</p><h3>{E(t)}</h3><p class="einst">{E(inst)}</p><p class="eres">{E(res)}</p><div class="edocs">{d}</div></article>'
_edu = "".join(_educard(*e) for e in EDUCATION)
page("skills.html", "Skills and certificates", f"""<section><p class="eyebrow">Skills and certificates</p><h1>Skills and certificates</h1><p class="lede">This is a summary of my skills, and the certifications that have helped me build them over the years. Expand any area to see how each skill was gained.</p></section>
<section id="education"><h2>Education</h2><div class="edus">{_edu}</div><p class="note" style="margin-top:12px">Select a document to open it. Identification numbers, date of birth and family names are covered.</p></section>
<section><h2>Summary map</h2><p class="note">This map traces how my research interests have developed over the years, from biotechnology and bioinformatics towards neuroscience. <button type="button" id="tall" class="linkb">Expand all</button></p><div class="tree">{tree}</div></section>
{toolkit}
<section id="list"><h2>Certificates and courses</h2><p class="note">Select a card for the course details, the full certificate and the issuer's verification link. Audited courses are marked and carry no certificate.</p>{lists}</section>{js}""", "certs")
# ---- home page (built last, so it can reuse the summary map)
_n_neuro = sum(1 for c in COURSES if c["id"] in NEURO_IDS and c["status"] != "todo")
_path = "".join(f'<div class="pstep" style="--c:var(--{col})"><span class="pdot"></span><b>{E(t)}</b><span>{E(d)}</span><small>{E(w)}</small>{f"""<em>{E(x)}</em>""" if x else ""}</div>' for t, d, w, col, x in PATH_STEPS)
_npath = "".join(f'<div class="pstep" style="--c:var(--neurons)"><span class="pdot"></span><small>{E(w)}</small><b>{E(t)}</b><span>{E(d)}</span></div>' for w, t, d in NEURO_STEPS)
_why = "".join(f'<div class="card"><p class="eyebrow" style="color:var(--accent)">{E(t)}</p><p style="margin:8px 0 0;font-size:15.5px;line-height:1.55">{E(d)}</p></div>' for t, d in WHY)
def _ri(t, sub, href): return f'<a class="ri" href="{href}"><b>{E(t)}</b><small>{E(sub)}</small></a>'
_ad0 = RESEARCH_INDEP[0]
_ri1 = f'<a class="ri ri1" href="alzheimers-project.html"><small>{E(_ad0[1])} · {E(_ad0[2])}</small><b>{E(_ad0[0])}</b><span>{E(_ad0[3])}</span><span class="btn">Open the project →</span></a>'
_tabs = [("spatial_AD", _ri1), ("Independent projects", "".join(_ri(t, f"{w} · {st}", "research.html#independent") for t, w, st, *_ in RESEARCH_INDEP[1:])),
         ("Research at TUM", "".join(_ri(t, f"{role} · {st}", "research.html#tum") for t, role, st, _ in OMICS_PROJECTS)),
         ("Research during my studies", "".join(_ri(t, w, "research.html#studies") for t, w, *_ in RESEARCH_EARLIER))]
_RI = 'class="ri'
_tabbtn = "".join(f'<button type="button" role="tab" class="tabb" aria-selected="{"true" if i == 0 else "false"}" data-t="{i}">{E(n)} <small>{h.count(_RI)}</small></button>' for i, (n, h) in enumerate(_tabs))
_tabpan = "".join(f'<div class="tabp" role="tabpanel" data-t="{i}"{"" if i == 0 else " hidden"}>{h}</div>' for i, (n, h) in enumerate(_tabs))
_can = ""
for i_, (area, col, src, groups_) in enumerate(CAN_DO):
    kids = "".join(f'<div class="tbr"><div class="bhead"><span class="bpill">{E(g)}</span></div><div class="leaves">{"".join(f"<span>{E(x)}</span>" for x in ab)}</div></div>' for g, ab in groups_)
    _can += f'<div class="tn" style="--c:var(--{col})"><button type="button" class="tpill" aria-expanded="false"><span class="tw">{E(area)}</span><small>{E(" · ".join(g for g, _ in groups_[:3]))}{" · …" if len(groups_) > 3 else ""}</small></button><div class="tkids" hidden><p class="tnote">{E(src)}</p>{kids}</div></div>'
_tabjs = "<script>(function(){var b=document.querySelectorAll('.tabb'),p=document.querySelectorAll('.tabp');b.forEach(function(x){x.addEventListener('click',function(){b.forEach(function(y){y.setAttribute('aria-selected',y===x)});p.forEach(function(q){q.hidden=q.dataset.t!==x.dataset.t})})})})();</script><noscript><style>.tabp[hidden]{display:grid!important}</style></noscript>"
page("index.html", "Jagadrupa Sahoo", f"""<section class="hero"><img class="me" src="assets/jagadrupa-sahoo.jpg" alt="Jagadrupa Sahoo" width="150" height="150"><div><h1>Jagadrupa Sahoo</h1>
<p class="lede">I am a bioinformatician working towards neuroscience and computational neuroscience. I study how the cells of the human cortex are reorganised in Alzheimer's disease, and I am interested in how molecular change becomes a change in what neural circuits do.</p>
<div class="chips" style="margin-top:16px"><a class="chip big" href="mailto:{EMAIL}">{EMAIL}</a><a class="chip big" href="https://github.com/jagadrupa">GitHub ↗</a><a class="chip big course" href="research.html">Research</a><a class="chip big course" href="skills.html">Skills and certificates</a></div></div></section>
<section><h2>Why neuroscience and computational neuroscience</h2><div class="intro3">{_why}</div>
<h3 class="mlh">Education and research</h3><div class="ppath">{_path}</div>
<h3 class="mlh">My path in neuroscience</h3><div class="ppath">{_npath}</div></section>
<section><h2>Featured project</h2><a class="card feat" href="alzheimers-project.html"><img loading="lazy" src="figs/ad-f3_zone_map.png" alt="Spatial zone map of the Alzheimer's section"><div><p class="eyebrow">Independent research project · 2026</p><h3>Spatial transcriptomics of human Alzheimer's cortex</h3>
<p class="eyebrow" style="margin-top:6px;color:var(--accent)">Conclusion</p>
<p>In this tissue the oligodendrocyte lineage, the cells that make myelin, is more numerous, less mature, less coherent in its myelin programme, and concentrated in the zones where pathology is highest. The change is spatially organised and not uniform, and the most disturbed zones impose a shared signature on every cell type living in them. The core signal survives a test against an independent atlas.</p>
<span class="chip course" style="margin-top:14px;align-self:flex-start">Read the project →</span></div></a></section>
<section><h2>Research</h2><p class="note">All projects, by where they were done. Select a project for the detail.</p><div class="tabs" role="tablist">{_tabbtn}</div>{_tabpan}</section>
<section><h2>What I can do</h2><p class="note">Practical skills, grouped by where I use them. Select an area to open it. <button type="button" id="tall" class="linkb">Expand all</button> The courses and certificates behind them are on the <a href="skills.html">Skills and certificates</a> page.</p><div class="tree">{_can}</div></section>
<section><h2>Contact</h2><p style="font-size:17px;margin:10px 0 0">I am glad to hear from researchers and programmes working in neuroscience and computational neuroscience: <a href="mailto:{EMAIL}">{EMAIL}</a></p></section>{js}{_tabjs}""", "home", "Jagadrupa Sahoo: bioinformatics, neuroscience and computational neuroscience.")

(ROOT/"certificates.html").write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Skills and certificates</title><meta http-equiv="refresh" content="0; url=skills.html"><link rel="canonical" href="skills.html"></head><body><p><a href="skills.html">Skills and certificates</a></p></body></html>')
(ROOT/".nojekyll").write_text("")
print(f"built: {n_out} course outcomes, {checked} note references verified on their cited PDF page, {notes_pages} note pages")
