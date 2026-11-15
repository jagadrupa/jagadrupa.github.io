"""One drawn picture per course, shown as its graphical summary: four small panels in a responsive grid.
Colours come from the site's CSS variables, so the pictures follow the light and dark themes."""

_DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">'
         '<path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker></defs>')
V = lambda c: f"var(--{c})"
TINT = lambda c, p=20: f"color-mix(in srgb,var(--{c}) {p}%,var(--paper))"

def T(x, y, s, size=10.5, fill="muted", anchor="middle", font="sans", weight=400):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-family="var(--{font})" font-weight="{weight}" fill="{V(fill)}">{s}</text>'
def B(x, y, w, h, label, col="accent", size=10.5):
    lines = label.split("|"); y0 = y + h / 2 + 3.5 - (len(lines) - 1) * 6
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{TINT(col)}" stroke="{V(col)}" stroke-width="1.3"/>'
            + "".join(T(x + w / 2, y0 + 12 * i, l, size, "ink") for i, l in enumerate(lines)))
def AR(x1, y1, x2, y2, w=1.7):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="var(--accent)" stroke-width="{w}" fill="none" marker-end="url(#ah)"/>'
def AX(x0, y0, w, h):
    return f'<path d="M{x0} {y0 - h}V{y0}H{x0 + w}" stroke="var(--line)" stroke-width="1.4" fill="none"/>'
def P(d, col="accent", w=2.2, dash=None, fill="none"):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" stroke="{V(col)}" stroke-width="{w}" fill="{fill}"{da} stroke-linecap="round" stroke-linejoin="round"/>'
def C(x, y, r, col="accent", p=22, w=1.4):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{TINT(col, p)}" stroke="{V(col)}" stroke-width="{w}"/>'
def DOTS(pts, col="accent", r=3):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{V(col)}"/>' for x, y in pts)
def NEURON(x, y, col="neurons", axon=40):
    return (P(f"M{x-10} {y-6}L{x-26} {y-18}M{x-12} {y}L{x-30} {y}M{x-10} {y+6}L{x-26} {y+18}M{x+12} {y}H{x+12+axon}", "ink", 1.5) + C(x, y, 12, col))
def BRAIN(cx, cy, s=1.0, hi=()):
    g = (f'<path d="M-60 10C-70-30-30-52 10-50C50-50 72-25 68 5C66 25 40 30 20 28L10 28C-10 34-45 30-60 10Z" fill="{TINT("neurons", 14)}" stroke="var(--ink)" stroke-width="1.5"/>'
         f'<ellipse cx="48" cy="32" rx="21" ry="13" fill="{TINT("gold", 22)}" stroke="var(--ink)" stroke-width="1.3"/>'
         '<path d="M20 28L25 58H37L35 32" fill="var(--paper)" stroke="var(--ink)" stroke-width="1.3"/>'
         '<path d="M-20-44C-14-24-22-10-8 4M22-48C16-30 30-20 22-4M-44 6C-24 0-6 12 24 6" fill="none" stroke="var(--muted)" stroke-width="1"/>')
    spots = {"frontal": (-40, -12, 17, 15), "parietal": (10, -30, 17, 13), "occipital": (52, -8, 12, 14), "temporal": (-6, 16, 20, 9), "deep": (8, -6, 12, 9)}
    for name, col in hi:
        x, y, rx, ry = spots[name]
        g += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{TINT(col, 45)}" stroke="{V(col)}" stroke-width="1.3"/>'
    return f'<g transform="translate({cx} {cy}) scale({s})">{g}</g>'
def NET(layers, x0=30, x1=202, y0=60, y1=200, col="networks", r=7, off=()):
    xs = [x0 + (x1 - x0) * i / (len(layers) - 1) for i in range(len(layers))]
    pos = [[(xs[i], (y0 + y1) / 2 + (j - (n - 1) / 2) * min(30, (y1 - y0) / max(n, 1))) for j in range(n)] for i, n in enumerate(layers)]
    e = "".join(f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" stroke="var(--muted)" stroke-width=".7" opacity=".7"/>' for i in range(len(pos) - 1) for a in pos[i] for b in pos[i + 1])
    n = "".join(C(x, y, r, "line" if (i, j) in off else col, 30) for i, l in enumerate(pos) for j, (x, y) in enumerate(l))
    return e + n
def GRID(x, y, cols, rows, cell, vals=None, col="accent"):
    out = ""
    for r in range(rows):
        for c in range(cols):
            v = vals[r * cols + c] if vals else 20
            out += f'<rect x="{x + c * cell}" y="{y + r * cell}" width="{cell - 1.5}" height="{cell - 1.5}" rx="1.5" fill="{TINT(col, v)}" stroke="var(--line)" stroke-width=".6"/>'
    return out
def FACE(cx, cy, kind, r=22):
    mouth = {"happy": f"M{cx-10} {cy+6}Q{cx} {cy+17} {cx+10} {cy+6}", "sad": f"M{cx-10} {cy+13}Q{cx} {cy+3} {cx+10} {cy+13}", "flat": f"M{cx-9} {cy+10}H{cx+9}"}.get(kind)
    m = P(mouth, "ink", 1.6) if mouth else f'<ellipse cx="{cx}" cy="{cy+10}" rx="5" ry="6" fill="none" stroke="var(--ink)" stroke-width="1.6"/>'
    return C(cx, cy, r, "gold", 18) + DOTS([(cx - 8, cy - 5), (cx + 8, cy - 5)], "ink", 2.2) + m
def ION(pts, col, label):
    return "".join(C(x, y, 7.5, col, 22, 1.3) + T(x, y + 3, label, 7.5, "ink", font="mono") for x, y in pts)
THR = lambda y, x0=22, x1=214: P(f"M{x0} {y}H{x1}", "muted", 1, "4 3")

# ---------------- neuroscience ----------------
H1 = [
 ("Resting potential", T(14, 58, "outside", 11, anchor="start") + T(14, 204, "inside", 11, anchor="start")
  + f'<rect x="12" y="112" width="208" height="34" rx="4" fill="var(--tint)" stroke="var(--line)"/><rect x="100" y="106" width="11" height="46" rx="4" fill="var(--molecules)"/><rect x="123" y="106" width="11" height="46" rx="4" fill="var(--molecules)"/><rect x="111" y="112" width="12" height="34" fill="var(--paper)"/>'
  + ION([(40, 80), (78, 66), (150, 74), (196, 84), (176, 60)], "brain", "Na⁺") + ION([(60, 98)], "molecules", "K⁺")
  + ION([(36, 172), (70, 190), (150, 178), (188, 196), (104, 204), (62, 164)], "molecules", "K⁺") + ION([(196, 168)], "brain", "Na⁺")
  + AR(117, 170, 117, 92) + T(140, 134, "K⁺ channel", anchor="start"),
  ["Unequal ions and a leaky K⁺ channel", "hold the cell near −70 mV"]),
 ("Passive membrane", P("M40 60H78l5-9 9 18 9-18 9 18 9-18 5 9h68V84M192 96v24H40V60", "ink", 1.6) + P("M176 84h32M176 96h32", "ink", 2.4)
  + T(100, 44, "R: leak channels", 11) + T(168, 94, "C: membrane", 11, anchor="end") + AX(30, 206, 184, 66)
  + P("M30 200H62V152H214", "muted", 1.2, "4 3") + P("M30 200H62C84 160 120 153 214 152") + T(150, 146, "current", anchor="start") + T(118, 190, "voltage lags", fill="accent", anchor="start"),
  ["The membrane is a resistor and a", "capacitor, so voltage changes slowly"]),
 ("Action potential", AX(22, 206, 192, 158) + THR(164) + P("M22 182H74C88 182 94 168 100 150C107 100 112 62 120 60C130 60 134 150 144 192C152 206 172 186 214 182", w=2.4)
  + T(212, 160, "threshold", anchor="end") + T(92, 104, "Na⁺ in", 11, "brain", "end") + T(140, 104, "K⁺ out", 11, "molecules", "start")
  + T(26, 58, "+40 mV", 10, anchor="start", font="mono") + T(26, 196, "−70", 10, anchor="start", font="mono"),
  ["Past threshold, Na⁺ rushes in,", "then K⁺ leaves and resets the cell"]),
 ("Propagation", C(24, 130, 13, "neurons") + P("M37 130H222", "ink", 3)
  + "".join(f'<rect x="{x}" y="116" width="46" height="28" rx="13" fill="{TINT("gold", 28)}" stroke="var(--gold)" stroke-width="1.3"/>' for x in (46, 102, 158))
  + "".join(f'<path d="M{x} 108Q{x + 28} 66 {x + 56} 108" fill="none" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ah)"/>' for x in (41, 97, 153))
  + T(69, 164, "myelin") + P("M97 150V178", "muted", 1) + T(97, 192, "node of Ranvier"),
  ["Myelin lets the signal jump from", "node to node, so it travels faster"]),
]
H2 = [
 ("The synapse", P("M70 44V84C70 104 84 112 116 112C148 112 162 104 162 84V44", "ink", 1.6, fill=TINT("neurons", 14)) + "".join(C(x, y, 7, "molecules", 30) for x, y in ((98, 70), (120, 62), (138, 78), (112, 90)))
  + DOTS([(100, 124), (116, 130), (130, 122), (108, 138), (126, 140)], "molecules", 2.6) + P("M56 196V170C56 158 70 152 116 152C162 152 176 158 176 170V196", "ink", 1.6, fill=TINT("brain", 14))
  + "".join(f'<rect x="{x}" y="146" width="9" height="13" rx="2" fill="var(--brain)"/>' for x in (92, 112, 132)) + T(170, 60, "vesicles", anchor="start") + T(40, 132, "cleft") + T(116, 212, "receptors on the next cell", 10),
  ["Transmitter released from one cell", "binds receptors on the next"]),
 ("Excitation and inhibition", AX(22, 120, 192, 70) + THR(66) + P("M22 104H60C72 104 76 78 88 78C104 78 118 104 214 104") + T(212, 60, "EPSP: towards threshold", fill="accent", anchor="end", size=10)
  + AX(22, 206, 192, 70) + P("M22 172H60C72 172 76 196 88 196C104 196 118 172 214 172", "cognition") + T(212, 150, "IPSP: away from threshold", fill="cognition", anchor="end", size=10),
  ["Each input nudges the membrane", "up or down"]),
 ("Small circuits", NEURON(150, 110, "neurons", 44) + C(40, 62, 9, "accent") + C(40, 110, 9, "accent") + C(40, 158, 9, "cognition") + AR(50, 66, 122, 98) + AR(50, 110, 118, 110) + P("M50 154L122 122", "cognition", 1.7)
  + T(40, 66, "+", 12, "ink") + T(40, 114, "+", 12, "ink") + T(40, 162, "−", 12, "ink") + AX(120, 206, 94, 40) + THR(176, 120, 214) + P("M120 200H140C148 200 150 188 156 188C162 188 164 170 172 170C180 170 186 200 214 200"),
  ["A neuron adds its inputs across", "space and time before it fires"]),
 ("Modulation and plasticity", C(50, 78, 14, "neurons") + C(182, 78, 14, "neurons") + P("M64 78H168", "ink", 1.3) + T(116, 68, "before") + C(50, 150, 14, "neurons") + C(182, 150, 14, "neurons") + P("M64 150H168", "accent", 5.5) + T(116, 136, "after repeated use")
  + AR(116, 92, 116, 120) + T(116, 190, "dopamine and serotonin tune the gain", 10),
  ["Synapses strengthen with use, and", "neuromodulators set the circuit's state"]),
]
H3 = [
 ("Vision", C(46, 120, 26, "networks", 14) + f'<ellipse cx="30" cy="120" rx="6" ry="13" fill="{TINT("networks", 40)}" stroke="var(--networks)"/>' + P("M66 106C72 114 72 126 66 134", "brain", 3.5) + T(46, 164, "eye and retina")
  + AR(76, 120, 122, 120) + BRAIN(168, 112, 0.62, [("occipital", "networks")]) + T(170, 164, "visual cortex"),
  ["Light becomes neural signals in the", "retina and is assembled in cortex"]),
 ("Audition", P("M16 120q8-22 16 0t16 0t16 0", "accent", 1.8) + T(40, 150, "sound") + P("M112 122c0-8 10-8 10 0c0 12-18 12-18-2c0-18 28-18 28 2c0 22-36 22-36-4", "gold", 2.2) + T(112, 162, "cochlea") + AR(70, 120, 86, 120) + AR(140, 120, 156, 120)
  + BRAIN(190, 114, 0.44, [("temporal", "gold")]) + T(190, 162, "auditory cortex", 10),
  ["Sound waves are sorted by frequency", "in the cochlea, then interpreted"]),
 ("Movement and action", B(72, 44, 88, 26, "motor cortex", "neurons") + B(72, 100, 88, 26, "spinal cord", "networks") + B(72, 156, 88, 26, "muscle", "brain") + AR(116, 70, 116, 98) + AR(116, 126, 116, 154)
  + '<path d="M72 169H40V113H68" stroke="var(--accent)" stroke-width="1.6" fill="none" stroke-dasharray="4 3" marker-end="url(#ah)"/>' + T(36, 104, "reflex", 10),
  ["Upper and lower motor neurons drive", "muscle; reflexes loop through the cord"]),
 ("Subcortical areas", BRAIN(112, 108, 1.15, [("deep", "cognition")]) + T(112, 92, "limbic", 9.5, "ink") + T(52, 196, "forebrain", 10) + T(128, 196, "brainstem", 10) + T(192, 172, "cerebellum", 10),
  ["Structures beneath the cortex handle", "survival, emotion and coordination"]),
]
_p = [(116, 56), (166, 82), (176, 136), (140, 178), (92, 178), (56, 136), (66, 82)]
EPFL = [
 ("Associative memory", "".join(f'<path d="M{a[0]} {a[1]}L{b[0]} {b[1]}" stroke="var(--muted)" stroke-width=".7"/>' for i, a in enumerate(_p) for b in _p[i + 1:])
  + "".join(C(x, y, 10, "accent" if i in (0, 2, 3, 6) else "line", 60 if i in (0, 2, 3, 6) else 20) for i, (x, y) in enumerate(_p)) + T(116, 206, "a stored pattern", 10),
  ["A Hopfield network stores patterns", "in its connections and recalls them"]),
 ("Attractor dynamics", P("M20 84C44 84 50 172 78 172C104 172 104 112 122 112C142 112 140 190 168 190C196 190 196 84 214 84", "networks") + C(96, 138, 8, "brain", 70) + AR(100, 146, 84, 164) + T(78, 190, "memory A", 10) + T(168, 208, "memory B", 10) + T(116, 58, "energy landscape"),
  ["Activity rolls downhill into the", "nearest stored memory"]),
 ("Populations", DOTS([(26 + 13 * (i % 6) + (4 if (i // 6) % 2 else 0), 56 + 13 * (i // 6)) for i in range(36)], "muted", 2.6) + DOTS([(26 + 13 * 2, 56 + 13), (30 + 13 * 4, 56 + 39), (26 + 13, 56 + 52), (26 + 13 * 5, 56)], "accent", 3.4) + AR(112, 90, 134, 90) + T(60, 144, "thousands of neurons", 10)
  + AX(140, 126, 76, 66) + P("M140 116C156 116 158 76 172 76C188 76 190 102 216 100") + T(178, 144, "one activity A(t)", 10) + T(116, 190, "mean-field theory", 11, "ink"),
  ["A population is described by its", "average activity"]),
 ("Decisions and learning", AX(22, 150, 192, 100) + P("M22 132H70C100 132 120 70 214 62") + P("M22 134H70C100 134 120 142 214 146", "cognition") + T(210, 56, "choice A wins", 10, "accent", "end") + T(210, 164, "choice B loses", 10, "cognition", "end")
  + C(60, 186, 9, "neurons") + C(170, 186, 9, "neurons") + P("M70 186H160", "accent", 4) + T(116, 178, "plasticity", 10),
  ["Competing populations settle a choice;", "synapses change to store what worked"]),
]
UCHI = [
 ("Neurons and signalling", NEURON(64, 96, "neurons", 60) + C(166, 96, 12, "neurons") + DOTS([(142, 90), (146, 98), (140, 102)], "molecules", 2.4) + T(116, 138, "electrical within, chemical between", 10)
  + B(34, 156, 76, 24, "sympathetic", "brain", 10) + B(122, 156, 86, 24, "parasympathetic", "networks", 10) + T(116, 200, "the body shapes emotion", 10),
  ["How neurons talk, and how the", "autonomic system ties body to feeling"]),
 ("Neuroanatomy", BRAIN(112, 112, 1.15, [("frontal", "neurons"), ("parietal", "networks"), ("occipital", "cognition"), ("temporal", "gold")]) + T(112, 196, "regions, blood supply, pathways", 10),
  ["Where a lesion is tells you which", "function is lost"]),
 ("Perception", C(40, 70, 15, "networks", 14) + C(40, 70, 6, "ink", 70) + T(40, 100, "vision", 10) + P("M28 132q6-14 12 0t12 0", "accent", 1.8) + T(40, 150, "hearing", 10) + P("M40 166a10 10 0 1 1 0.1 0M40 172a4 4 0 1 1 0.1 0", "gold", 1.6) + T(40, 204, "balance", 10)
  + AR(64, 72, 110, 100) + AR(64, 132, 110, 118) + AR(64, 184, 110, 134) + BRAIN(166, 112, 0.7),
  ["The senses are interpreted, not", "simply recorded"]),
 ("Movement and homeostasis", B(20, 48, 90, 24, "cerebellum", "gold", 10) + B(122, 48, 90, 24, "basal ganglia", "cognition", 10) + T(116, 92, "refine and select movement", 10)
  + '<path d="M116 126a34 34 0 1 1-24 10" fill="none" stroke="var(--accent)" stroke-width="2" marker-end="url(#ah)"/>' + T(116, 158, "set point", 10, "ink") + T(116, 172, "37 °C", 10, font="mono") + T(116, 208, "temperature, breathing, sleep", 10),
  ["Movement is tuned by deep circuits;", "the brain also keeps the body steady"]),
]
YALE = [
 ("Foundations", BRAIN(72, 96, 0.62) + T(116, 170, "the mind has a physical basis", 10) + C(160, 70, 9, "gold", 50) + T(160, 96, "signal", 9.5) + AR(160, 104, 160, 126) + B(128, 130, 64, 22, "response", "brain", 10) + T(116, 196, "Freud · Skinner · conditioning", 10),
  ["The brain, the unconscious and", "learned behaviour"]),
 ("Development and language", C(40, 150, 9, "accent") + C(84, 140, 13, "accent") + C(138, 126, 18, "accent") + AR(54, 172, 170, 172) + T(110, 190, "infant to adult", 10)
  + f'<path d="M150 50h56a6 6 0 0 1 6 6v24a6 6 0 0 1-6 6h-30l-10 12v-12h-16a6 6 0 0 1-6-6V56a6 6 0 0 1 6-6z" fill="{TINT("networks")}" stroke="var(--networks)" stroke-width="1.3"/>' + T(178, 66, "sounds", 9.5, "ink") + T(178, 79, "words, syntax", 9.5, "ink"),
  ["How thinking grows, and how", "language is built and learned"]),
 ("Cognition", B(14, 96, 60, 30, "perception", "networks", 10) + B(86, 96, 60, 30, "attention", "accent", 10) + B(158, 96, 60, 30, "memory", "cognition", 10) + AR(74, 111, 84, 111) + AR(146, 111, 156, 111) + T(116, 78, "from the world to the mind", 10) + T(116, 156, "memories can fail or be false", 10),
  ["What we notice, keep and", "later recall"]),
 ("People and differences", AX(22, 150, 192, 96) + P("M24 148C70 148 86 62 118 62C150 62 166 148 212 148", "cognition") + T(118, 168, "personality and intelligence vary", 10) + "".join(C(x, 194, 8, "gold", 40) for x in (72, 104, 136, 168)) + P("M80 194H96M112 194H128M144 194H160", "muted", 1.2),
  ["Emotion, social life, individual", "variation, mental illness, happiness"]),
]
CAMCOG = [
 ("Measuring the mind", BRAIN(116, 92, 0.8) + B(14, 150, 46, 22, "lesions", "disease", 9.5) + B(66, 150, 46, 22, "fMRI", "networks", 9.5) + B(118, 150, 46, 22, "EEG", "accent", 9.5) + B(170, 150, 48, 22, "TMS", "gold", 9.5) + T(116, 196, "each method answers a different question", 9.5),
  ["Lesion studies, imaging, recording", "and stimulation"]),
 ("Language", B(22, 54, 84, 24, "phonology", "networks") + B(48, 92, 84, 24, "morphology", "accent") + B(74, 130, 84, 24, "syntax", "cognition") + B(100, 168, 84, 24, "semantics", "gold") + P("M30 96V188H92", "muted", 1, "3 3") + T(176, 80, "sound", 9.5) + T(204, 160, "meaning", 9.5, anchor="end") ,
  ["How language is structured and", "how children acquire it"]),
 ("Working memory", B(66, 50, 100, 30, "central executive", "accent") + B(14, 128, 96, 34, "phonological|loop", "networks") + B(122, 128, 96, 34, "visuo-spatial|sketchpad", "cognition") + AR(96, 80, 66, 126) + AR(136, 80, 166, 126) + T(116, 190, "the senses also influence one another", 9.5),
  ["A small workspace that holds", "sounds and images in mind"]),
 ("Attention", f'<path d="M116 46L60 176H172Z" fill="{TINT("gold", 30)}" stroke="var(--gold)" stroke-width="1.2"/>' + C(116, 46, 6, "gold", 80) + "".join(C(x, 164, 11, "line", 30) for x in (30, 202)) + C(92, 160, 11, "accent", 60) + C(140, 160, 11, "accent", 60) + T(116, 200, "what falls outside is missed", 10),
  ["Attention selects what reaches", "awareness"]),
]
CAMDM = [
 ("Brain and development", BRAIN(116, 92, 0.95) + AX(40, 206, 150, 30) + P("M40 202C90 200 120 182 190 180") + T(116, 164, "the cortex matures into adulthood", 9.5),
  ["The anatomy and development", "that decisions rest on"]),
 ("Prefrontal cortex", BRAIN(116, 110, 1.15, [("frontal", "accent")]) + T(116, 196, "prefrontal cortex", 10.5, "accent") + T(116, 211, "plans, weighs, inhibits", 10),
  ["The region that weighs options", "and controls impulses"]),
 ("Chemistry and networks", B(84, 48, 64, 24, "prefrontal", "accent", 10) + B(18, 124, 64, 24, "striatum", "cognition", 10) + B(150, 124, 64, 24, "amygdala", "disease", 10) + P("M100 72L58 122M132 72L174 122M82 136H148", "muted", 1.4) + DOTS([(74, 94), (80, 102), (156, 96), (116, 130)], "molecules", 3) + T(116, 176, "dopamine and serotonin", 10, "molecules") + T(116, 192, "carry value and risk signals", 10),
  ["Neurotransmitters and connected", "regions produce a decision"]),
 ("Styles and deficits", AX(22, 150, 192, 96) + P("M22 144C80 140 110 80 214 66") + P("M22 146C80 144 120 124 214 116", "disease", 2, "5 3") + C(56, 142, 5, "gold", 80) + T(56, 166, "early experience", 9.5, anchor="start") + T(210, 60, "typical", 9.5, "accent", "end") + T(210, 132, "impaired", 9.5, "disease", "end") + T(116, 190, "for example in schizophrenia", 10),
  ["Childhood shapes decision style;", "illness can disrupt it"]),
]
CAMEM = [
 ("Reading faces", FACE(52, 110, "happy") + FACE(116, 110, "sad") + FACE(180, 110, "o") + T(52, 152, "joy", 10) + T(116, 152, "sadness", 10) + T(180, 152, "surprise", 10) + T(116, 190, "expressions carry emotion", 10),
  ["Faces are the main channel for", "reading what others feel"]),
 ("Simulation", FACE(48, 96, "happy", 20) + FACE(184, 96, "happy", 20) + AR(74, 96, 156, 96) + T(116, 86, "see") + T(184, 136, "mirror it", 10) + T(48, 136, "other person", 10) + B(64, 160, 104, 26, "mirror neurons", "accent"),
  ["We understand a feeling partly by", "re-creating it in our own body"]),
 ("How it is measured", T(20, 60, "EEG", 10.5, "ink", "start") + P("M20 86q7-22 14 0t14 0t14 0t14 0q7-10 14 0t14 0t14 0t14 0t14 0t14 0t14 0", "accent", 1.7) + T(20, 132, "EMG of face muscles", 10.5, "ink", "start") + P("M20 164h24l4-18 5 34 5-30 4 22 4-8h20l4-22 5 38 5-28 4 12h28l4-14 5 22 4-8h20", "cognition", 1.6) + T(116, 204, "plus studies of brain lesions", 10),
  ["Brain waves and tiny facial muscle", "movements reveal the simulation"]),
 ("When it is hard", FACE(70, 104, "flat") + T(108, 86, "?", 22, "accent") + B(130, 84, 86, 40, "context and|prior knowledge", "networks", 10) + AR(128, 104, 98, 104) + T(116, 168, "motivation to understand matters too", 9.5),
  ["Ambiguous expressions are resolved", "with context and what we know"]),
]
FMRI1 = [
 ("From scanner to image", B(14, 60, 56, 30, "scanner", "networks", 10) + AR(70, 75, 84, 75) + GRID(88, 54, 6, 6, 7.5, [10, 14, 20, 20, 14, 10, 14, 26, 44, 44, 26, 14, 20, 44, 90, 90, 44, 20, 20, 44, 90, 90, 44, 20, 14, 26, 44, 44, 26, 14, 10, 14, 20, 20, 14, 10], "accent")
  + AR(136, 75, 150, 75) + f'<ellipse cx="184" cy="76" rx="26" ry="22" fill="{TINT("neurons", 30)}" stroke="var(--ink)" stroke-width="1.3"/>' + T(110, 116, "k-space", 10) + T(184, 116, "image", 10) + B(40, 148, 152, 26, "a 4D series: space × time", "gold", 10),
  ["Radio signals are collected in", "k-space and turned into images"]),
 ("The BOLD signal", AX(22, 180, 192, 110) + P("M40 180V168M44 180V168", "ink", 2) + T(42, 196, "stimulus", 10) + P("M22 164H44C60 164 66 86 88 86C110 86 112 176 134 176C150 176 160 164 214 164") + T(96, 78, "peak after about 5 s", 10, anchor="start"),
  ["Blood flow follows neural activity", "slowly, which limits time resolution"]),
 ("General Linear Model", GRID(20, 60, 1, 9, 13, [30, 60, 80, 40, 20, 50, 90, 70, 30], "ink") + T(26, 196, "Y", 11, "ink") + T(50, 124, "=", 16, "ink") + GRID(66, 60, 3, 9, 13, [80, 10, 40, 80, 10, 40, 10, 80, 40, 10, 80, 40, 80, 10, 40, 80, 10, 40, 10, 80, 40, 10, 80, 40, 80, 10, 40], "accent")
  + T(86, 196, "X", 11, "ink") + T(126, 124, "×  β", 14, "ink") + T(164, 124, "+  ε", 14, "ink") + T(186, 150, "noise", 9.5),
  ["Each voxel's time series is modelled", "as task regressors plus noise"]),
 ("Group maps", f'<ellipse cx="116" cy="104" rx="64" ry="50" fill="{TINT("neurons", 16)}" stroke="var(--ink)" stroke-width="1.4"/><path d="M116 56V152" stroke="var(--muted)" stroke-width="1"/>' + f'<ellipse cx="88" cy="96" rx="14" ry="11" fill="{TINT("brain", 80)}"/><ellipse cx="146" cy="118" rx="10" ry="8" fill="{TINT("brain", 60)}"/>' + B(40, 168, 68, 22, "FWER", "disease", 10) + B(124, 168, 68, 22, "FDR", "gold", 10),
  ["Subjects are combined, then corrected", "for thousands of comparisons"]),
]
FMRI2 = [
 ("Efficient design", P("M22 96H214", "line", 1.4) + "".join(P(f"M{x} 96V70", "accent", 3) for x in (36, 52, 92, 104, 150, 198)) + "".join(P(f"M{x} 96V78", "cognition", 3) for x in (70, 122, 168, 182)) + T(116, 120, "jittered events of two conditions", 10) + B(40, 148, 152, 26, "optimise timing for power", "gold", 10),
  ["How events are spaced decides how", "much the experiment can detect"]),
 ("Connectivity", BRAIN(116, 108, 1.2) + "".join(P(d, "accent", 1.6) for d in ("M72 96L112 72", "M112 72L172 100", "M72 96L108 124", "M108 124L172 100")) + "".join(C(x, y, 6, "accent", 80) for x, y in ((72, 96), (112, 72), (172, 100), (108, 124))) + T(116, 200, "regions that rise and fall together", 10),
  ["Functional connectivity and the", "networks it reveals"]),
 ("Causal models", B(24, 60, 54, 28, "A", "networks", 12) + B(154, 60, 54, 28, "B", "accent", 12) + B(89, 140, 54, 28, "M", "cognition", 12) + AR(78, 74, 152, 74) + AR(60, 88, 96, 138) + AR(136, 138, 172, 90) + T(116, 62, "direct", 9.5) + T(116, 190, "mediation · DCM · Granger causality", 10),
  ["Asking which region drives which,", "and through what"]),
 ("Pattern analysis", GRID(18, 62, 5, 5, 14, [10, 70, 20, 90, 30, 60, 10, 80, 20, 50, 30, 90, 10, 60, 20, 80, 20, 50, 10, 70, 20, 60, 90, 30, 10], "accent") + T(52, 148, "voxel pattern", 10) + AR(92, 96, 112, 96) + B(116, 80, 54, 32, "classifier", "gold", 9.5) + AR(170, 96, 186, 96) + T(202, 92, "A", 14, "accent") + T(202, 108, "or B", 9.5) + T(116, 190, "decoding mental states", 10),
  ["Many voxels together predict what a", "person sees, feels or intends"]),
]
NH = [
 ("Images as arrays", "".join(f'<rect x="{40 + 10 * i}" y="{56 + 10 * i}" width="96" height="96" rx="3" fill="{TINT("networks", 10 + 8 * i)}" stroke="var(--networks)" stroke-width="1.1"/>' for i in range(4)) + f'<ellipse cx="118" cy="134" rx="34" ry="38" fill="{TINT("neurons", 36)}" stroke="var(--ink)" stroke-width="1.1"/>' + T(190, 58, "NIfTI", 11, "ink", font="mono") + T(190, 72, "3D voxels", 10),
  ["A brain scan is a 3D array of", "numbers, read into R"]),
 ("Visualisation", f'<ellipse cx="116" cy="116" rx="62" ry="68" fill="{TINT("neurons", 24)}" stroke="var(--ink)" stroke-width="1.4"/><ellipse cx="116" cy="116" rx="44" ry="50" fill="{TINT("neurons", 50)}" stroke="none"/><path d="M104 96c-10 14-10 28 0 40M128 96c10 14 10 28 0 40" fill="none" stroke="var(--paper)" stroke-width="5"/>' + P("M116 40V200M40 116H192", "gold", 1, "4 3") + T(116, 212, "orthographic slices", 10),
  ["Slices, overlays and intensity", "transforms"]),
 ("Processing pipeline", B(46, 46, 140, 26, "inhomogeneity correction", "networks", 10) + B(46, 96, 140, 26, "brain extraction", "accent", 10) + B(46, 146, 140, 26, "registration to template", "cognition", 10) + AR(116, 72, 116, 94) + AR(116, 122, 116, 144) + T(116, 196, "fslr · ANTsR", 10.5, "ink", font="mono"),
  ["The standard clean-up steps before", "any analysis"]),
 ("Tissue segmentation", f'<ellipse cx="116" cy="112" rx="64" ry="66" fill="{TINT("networks", 34)}" stroke="var(--ink)" stroke-width="1.3"/><ellipse cx="116" cy="112" rx="52" ry="54" fill="{TINT("muted", 55)}"/><ellipse cx="116" cy="112" rx="36" ry="38" fill="{TINT("gold", 26)}"/><path d="M106 96c-8 12-8 22 0 32M126 96c8 12 8 22 0 32" fill="none" stroke="{TINT("networks", 60)}" stroke-width="5"/>'
  + T(116, 200, "CSF · grey matter · white matter", 10),
  ["Each voxel is labelled by", "tissue type"]),
]
# ---------------- deep learning ----------------
def _loss(ball=(86, 118)):
    return AX(22, 200, 192, 140) + P("M30 66C60 190 110 196 126 196C150 196 180 150 208 70", "networks") + C(ball[0], ball[1], 7, "brain", 80) + AR(ball[0] + 6, ball[1] + 10, ball[0] + 26, ball[1] + 46) + T(204, 214, "weights", 10, anchor="end") + T(30, 56, "loss", 10, anchor="start")
KERAS = [
 ("The artificial neuron", "".join(C(30, y, 8, "networks", 30) + f'<path d="M38 {y}L98 112" stroke="var(--muted)" stroke-width="1.1"/>' for y in (70, 112, 154)) + T(68, 82, "w₁", 9.5) + T(68, 106, "w₂", 9.5) + T(68, 146, "w₃", 9.5) + C(112, 112, 16, "accent") + T(112, 116, "Σ", 14, "ink")
  + AR(128, 112, 150, 112) + B(152, 96, 36, 32, "f", "gold", 14) + AR(188, 112, 214, 112) + T(170, 146, "activation", 9.5),
  ["Weighted inputs are summed and", "passed through an activation"]),
 ("Learning by descent", _loss(),
  ["Gradient descent and backpropagation", "adjust weights to reduce the loss"]),
 ("Deep networks", NET([3, 5, 5, 2]) + T(30, 214, "input", 9.5) + T(202, 214, "output", 9.5) + T(116, 50, "hidden layers", 10),
  ["Stacked layers, built for regression", "and classification in Keras"]),
 ("Architectures", B(18, 48, 94, 34, "CNN|images", "networks", 10) + B(120, 48, 94, 34, "RNN|sequences", "cognition", 10) + B(18, 100, 94, 34, "transformer|attention", "accent", 10) + B(120, 100, 94, 34, "autoencoder|compression", "gold", 10) + T(116, 170, "one idea, shaped to the data", 10),
  ["The main model families and what", "each is for"]),
]
PTB = [
 ("Tensors", GRID(22, 64, 6, 1, 15, [20, 50, 80, 40, 60, 30], "networks") + T(66, 96, "1D", 10) + GRID(134, 56, 5, 5, 15, [20, 60, 30, 80, 40, 70, 20, 50, 30, 60, 40, 80, 20, 60, 30, 30, 50, 70, 20, 80, 60, 30, 40, 70, 20], "accent") + T(170, 146, "2D", 10) + B(30, 164, 172, 26, "autograd tracks gradients", "gold", 10),
  ["PyTorch's arrays, with automatic", "differentiation"]),
 ("Linear regression", AX(22, 200, 192, 140) + DOTS([(40, 176), (58, 160), (74, 164), (92, 140), (110, 138), (128, 116), (146, 120), (164, 96), (184, 88), (200, 70)], "muted", 3.2) + P("M30 182L208 70"),
  ["Fit a line by minimising the", "squared error"]),
 ("Gradient descent", _loss((70, 150)) + T(126, 92, "batch · mini-batch", 9.5) + T(126, 106, "stochastic", 9.5),
  ["Step down the loss, a batch", "at a time"]),
 ("Logistic regression", AX(22, 200, 192, 140) + P("M24 190C90 190 96 130 116 130C136 130 142 70 210 70") + THR(130) + DOTS([(40, 190), (58, 190), (78, 190), (96, 190)], "cognition", 3.6) + DOTS([(140, 70), (160, 70), (182, 70), (200, 70)], "brain", 3.6) + T(210, 124, "p = 0.5", 9.5, anchor="end"),
  ["A sigmoid turns a line into a", "class probability"]),
]
DLPT = [
 ("Softmax", "".join(f'<rect x="{38 + 44 * i}" y="{190 - h}" width="28" height="{h}" rx="3" fill="{TINT("accent" if i == 2 else "networks", 60 if i == 2 else 26)}" stroke="var(--{"accent" if i == 2 else "networks"})"/>' + T(52 + 44 * i, 206, l, 9.5) for i, (h, l) in enumerate(((22, "cat"), (40, "dog"), (112, "bird"), (16, "fish")))) + P("M30 190H204", "line", 1.4) + T(140, 70, "0.71", 10, "accent", font="mono"),
  ["Scores become probabilities across", "several classes"]),
 ("Going deeper", NET([2, 3, 2], 22, 96, 70, 180, r=6) + AR(102, 124, 122, 124) + NET([2, 4, 4, 4, 2], 128, 214, 60, 190, r=5) + T(58, 206, "shallow", 10) + T(172, 206, "deep", 10),
  ["More hidden layers learn more", "complex functions"]),
 ("Training tricks", NET([3, 5, 5, 2], off=((1, 1), (1, 3), (2, 0), (2, 4))) + T(116, 50, "dropout switches units off", 10) + T(116, 214, "batch norm · momentum · initialisation", 9.5),
  ["Regularisation and normalisation", "keep deep networks trainable"]),
 ("Convolution", GRID(14, 70, 6, 6, 12, [10, 10, 60, 60, 10, 10, 10, 60, 10, 10, 60, 10, 60, 10, 10, 10, 10, 60, 60, 60, 60, 60, 60, 60, 60, 10, 10, 10, 10, 60, 60, 10, 10, 10, 10, 60], "ink") + '<rect x="13" y="69" width="37" height="37" fill="none" stroke="var(--accent)" stroke-width="2"/>'
  + AR(90, 106, 104, 106) + GRID(108, 82, 4, 4, 12, [70, 30, 30, 70, 30, 80, 80, 30, 80, 80, 80, 80, 70, 20, 20, 70], "accent") + AR(160, 106, 174, 106) + GRID(178, 94, 2, 2, 12, [80, 80, 90, 90], "brain") + T(50, 160, "image", 10) + T(132, 148, "features", 10) + T(190, 136, "pooled", 10),
  ["Filters slide over an image to", "find local patterns"]),
]
TFK = [
 ("Advanced CNNs", GRID(16, 76, 4, 4, 14, [20, 60, 60, 20, 60, 90, 90, 60, 60, 90, 90, 60, 20, 60, 60, 20], "ink") + AR(76, 104, 90, 104) + B(92, 80, 64, 48, "pre-trained|layers", "networks", 9.5) + AR(154, 104, 168, 104) + B(172, 88, 46, 32, "new|head", "accent", 10) + T(124, 152, "frozen", 9.5) + T(195, 140, "trained", 9.5) + T(116, 190, "transfer learning and augmentation", 10),
  ["Reuse a trained network and adapt", "it to a new task"]),
 ("Transformers", "".join(B(18 + 50 * i, 150, 44, 24, w, "networks", 10) for i, w in enumerate(("the", "signal", "moved", "fast"))) + "".join(P(d, "accent", w) for d, w in (("M40 148Q90 70 140 148", 2.4), ("M90 148Q115 104 140 148", 1.6), ("M140 148Q165 110 190 148", 1.2), ("M40 148Q65 116 90 148", 0.9))) + T(116, 70, "attention", 11, "ink") + T(116, 200, "sequences and time series", 10),
  ["Each token attends to the others", "that matter to it"]),
 ("Generative models", f'<path d="M22 60H52L96 104V132L52 176H22Z" fill="{TINT("networks")}" stroke="var(--networks)" stroke-width="1.3"/><path d="M210 60H180L136 104V132L180 176H210Z" fill="{TINT("cognition")}" stroke="var(--cognition)" stroke-width="1.3"/>' + B(100, 104, 32, 28, "z", "gold", 13) + T(52, 122, "encode", 10, "ink") + T(182, 122, "decode", 10, "ink") + T(116, 202, "autoencoders · GANs · diffusion", 10),
  ["Compress data to a code, then", "generate new examples from it"]),
 ("Reinforcement learning", B(22, 66, 76, 34, "agent", "accent", 11) + B(134, 66, 76, 34, "environment", "networks", 10) + '<path d="M98 74H132" stroke="var(--accent)" stroke-width="1.7" marker-end="url(#ah)"/><path d="M134 94H100" stroke="var(--accent)" stroke-width="1.7" marker-end="url(#ah)"/>' + T(116, 66, "action", 9.5) + T(116, 112, "state, reward", 9.5) + B(30, 146, 172, 28, "Q-learning · deep Q-networks", "gold", 10),
  ["Learn what to do from reward", "alone"]),
]
CAP = [
 ("Data loading", "".join(f'<rect x="{20 + 6 * i}" y="{60 + 6 * i}" width="56" height="44" rx="3" fill="{TINT("networks", 12 + 8 * i)}" stroke="var(--networks)"/>' for i in range(3)) + AR(96, 96, 114, 96) + B(118, 60, 96, 26, "flip · rotate", "accent", 10) + B(118, 96, 96, 26, "crop · shift", "accent", 10) + T(60, 136, "images", 10) + T(166, 140, "augmentation", 10) + B(36, 160, 160, 26, "generators save memory", "gold", 10),
  ["Feed large image sets efficiently", "in Keras and PyTorch"]),
 ("CNN classifier", GRID(16, 82, 4, 4, 13, [20, 70, 70, 20, 70, 20, 20, 70, 70, 20, 20, 70, 20, 70, 70, 20], "ink") + AR(72, 108, 84, 108) + "".join(f'<rect x="{88 + 16 * i}" y="{76 + 8 * i}" width="12" height="{64 - 16 * i}" rx="2" fill="{TINT("networks", 30 + 14 * i)}" stroke="var(--networks)"/>' for i in range(4)) + AR(154, 108, 166, 108) + B(170, 92, 46, 32, "class", "brain", 10.5) + T(116, 190, "convolution, pooling, dense layers", 10),
  ["Build and train a convolutional", "classifier"]),
 ("Vision transformer", GRID(18, 70, 4, 4, 15, [30, 50, 50, 30, 50, 80, 80, 50, 50, 80, 80, 50, 30, 50, 50, 30], "cognition") + T(48, 146, "image patches", 10) + AR(84, 100, 100, 100) + B(104, 78, 64, 44, "CNN +|attention", "accent", 10) + AR(168, 100, 182, 100) + B(186, 86, 32, 28, "ŷ", "brain", 13) + T(116, 190, "combining two architectures", 10),
  ["Integrate a CNN with a vision", "transformer"]),
 ("Evaluation", GRID(70, 60, 3, 3, 30, [90, 12, 10, 14, 86, 12, 10, 16, 88], "accent") + T(116, 166, "predicted class", 10) + '<text x="56" y="108" font-size="10" fill="var(--muted)" text-anchor="middle" transform="rotate(-90 56 108)">true class</text>' + T(116, 196, "confusion matrix", 10.5, "ink"),
  ["Check where the model is right", "and where it confuses classes"]),
]

def _panel(i, title, body, caption):
    cap = "".join(T(116, 240 + 15 * n, line, 11.5) for n, line in enumerate(caption))
    return (f'<svg viewBox="0 0 232 278" font-family="var(--sans)" role="img" aria-label="{title}. {" ".join(caption)}">{_DEFS}'
            f'<rect x="1" y="1" width="230" height="276" rx="6" fill="var(--paper)" stroke="var(--line)"/>'
            f'<text x="14" y="26" font-family="var(--mono)" font-size="10.5" fill="var(--accent)">{i + 1}</text>'
            f'<text x="30" y="26" font-family="var(--serif)" font-size="15" fill="var(--ink)">{title}</text>{body}{cap}</svg>')
def _figure(panels):
    return '<div class="pics">' + "".join(_panel(i, t, b, c) for i, (t, b, c) in enumerate(panels)) + "</div>"

H = "The course in one picture"
# course id (or audited-course title) -> (heading, one-line caption, html)
PICTURES = {
 "harvardx-mcb80-1x": (H, "From a resting cell to a travelling signal, in the order the four lessons build it.", _figure(H1)),
 "harvardx-mcb80-2x": (H, "From a single synapse to circuits that adapt.", _figure(H2)),
 "harvardx-mcb80-3x": (H, "Sensing, moving, and the structures beneath the cortex.", _figure(H3)),
 "epflx-neuronal-dynamics-of-cognition": (H, "How networks of neurons remember, perceive and decide.", _figure(EPFL)),
 "uchicago-understanding-the-brain": (H, "From single neurons to the systems that run everyday life.", _figure(UCHI)),
 "yale-introduction-to-psychology": (H, "The main territories of psychology, in the order the course visits them.", _figure(YALE)),
 "cambridge-cognitive-psychology": (H, "How cognition is studied, and three of its core functions.", _figure(CAMCOG)),
 "cambridge-neuropsychology-of-decision-making": (H, "From brain anatomy to how decisions go right or wrong.", _figure(CAMDM)),
 "cambridge-psychology-of-emotions": (H, "How we recognise what other people feel.", _figure(CAMEM)),
 "jhu-principles-of-fmri-1": (H, "The path from scanner signal to a statistical map.", _figure(FMRI1)),
 "jhu-principles-of-fmri-2": (H, "Sharper designs, connectivity and decoding.", _figure(FMRI2)),
 "jhu-neurohacking-in-r": (H, "A structural MRI scan from file to labelled tissue, in R.", _figure(NH)),
 "Deep Learning Fundamentals with Keras": (H, "", _figure(KERAS)),
 "PyTorch Basics for Machine Learning": (H, "", _figure(PTB)),
 "Deep Learning with Python and PyTorch": (H, "", _figure(DLPT)),
 "Deep Learning with TensorFlow and Keras": (H, "", _figure(TFK)),
 "Applied Deep Learning Capstone Project": (H, "", _figure(CAP)),
}
