"""One drawn picture per course, shown as its graphical summary. Colours come from the site's CSS variables."""

_DEFS = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker></defs>')

def _panel(i, title, body, caption):
    x = 8 + i * 248
    cap = "".join(f'<text x="116" y="{236 + 15 * n}" text-anchor="middle" font-size="11.5" fill="var(--muted)">{line}</text>' for n, line in enumerate(caption))
    return (f'<g transform="translate({x} 0)"><rect x="0" y="4" width="232" height="268" rx="6" fill="var(--paper)" stroke="var(--line)"/>'
            f'<text x="14" y="27" font-family="var(--mono)" font-size="10.5" letter-spacing=".06em" fill="var(--accent)">{i + 1}</text>'
            f'<text x="30" y="27" font-family="var(--serif)" font-size="15.5" fill="var(--ink)">{title}</text>{body}{cap}</g>')

def _ions(points, colour, label):
    return "".join(f'<circle cx="{x}" cy="{y}" r="7.5" fill="color-mix(in srgb,var(--{colour}) 22%,var(--paper))" stroke="var(--{colour})" stroke-width="1.3"/>'
                   f'<text x="{x}" y="{y + 3}" text-anchor="middle" font-size="7.5" font-family="var(--mono)" fill="var(--ink)">{label}</text>' for x, y in points)

_H1 = [
 # 1 resting potential: membrane, a potassium channel, unequal ions
 ('Resting potential',
  '<text x="14" y="58" font-size="11" fill="var(--muted)">outside</text><text x="14" y="204" font-size="11" fill="var(--muted)">inside</text>'
  '<rect x="12" y="112" width="208" height="34" rx="4" fill="var(--tint)" stroke="var(--line)"/>'
  '<rect x="100" y="106" width="11" height="46" rx="4" fill="var(--molecules)"/><rect x="123" y="106" width="11" height="46" rx="4" fill="var(--molecules)"/>'
  '<rect x="111" y="112" width="12" height="34" fill="var(--paper)"/>'
  + _ions([(40, 80), (78, 66), (150, 74), (196, 84), (176, 60)], "brain", "Na⁺") + _ions([(60, 98)], "molecules", "K⁺")
  + _ions([(36, 172), (70, 190), (150, 178), (188, 196), (104, 204), (62, 164)], "molecules", "K⁺") + _ions([(196, 168)], "brain", "Na⁺")
  + '<path d="M117 170V92" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ah)"/>'
  '<text x="140" y="134" font-size="10.5" fill="var(--muted)">K⁺ channel</text>',
  ["Unequal ions and a leaky K⁺ channel", "hold the cell near −70 mV"]),
 # 2 passive properties: RC circuit and its slow charging curve
 ('Passive membrane',
  '<path d="M40 60H78l5-9 9 18 9-18 9 18 9-18 5 9h68V84M192 96v24H40V60" fill="none" stroke="var(--ink)" stroke-width="1.6"/>'
  '<path d="M176 84h32M176 96h32" stroke="var(--ink)" stroke-width="2.4"/>'
  '<text x="100" y="44" text-anchor="middle" font-size="11" fill="var(--muted)">R: leak channels</text><text x="168" y="94" text-anchor="end" font-size="11" fill="var(--muted)">C: membrane</text>'
  '<path d="M30 206H214M30 206V140" stroke="var(--line)" stroke-width="1.4"/>'
  '<path d="M30 200H62V152H214" fill="none" stroke="var(--muted)" stroke-width="1.2" stroke-dasharray="4 3"/>'
  '<path d="M30 200H62C84 160 120 153 214 152" fill="none" stroke="var(--accent)" stroke-width="2.2"/>'
  '<text x="150" y="146" font-size="10.5" fill="var(--muted)">current</text><text x="118" y="190" font-size="10.5" fill="var(--accent)">voltage lags</text>',
  ["The membrane is a resistor and a", "capacitor, so voltage changes slowly"]),
 # 3 action potential: the classic trace with its phases
 ('Action potential',
  '<path d="M22 206H214M22 206V48" stroke="var(--line)" stroke-width="1.4"/>'
  '<path d="M22 164H214" stroke="var(--muted)" stroke-width="1" stroke-dasharray="4 3"/>'
  '<path d="M22 182H74C88 182 94 168 100 150C107 100 112 62 120 60C130 60 134 150 144 192C152 206 172 186 214 182" fill="none" stroke="var(--accent)" stroke-width="2.4"/>'
  '<text x="212" y="160" text-anchor="end" font-size="10.5" fill="var(--muted)">threshold</text>'
  '<text x="92" y="104" text-anchor="end" font-size="11" fill="var(--brain)">Na⁺ in</text><text x="140" y="104" font-size="11" fill="var(--molecules)">K⁺ out</text>'
  '<text x="26" y="58" font-size="10" font-family="var(--mono)" fill="var(--muted)">+40 mV</text><text x="26" y="196" font-size="10" font-family="var(--mono)" fill="var(--muted)">−70</text>',
  ["Past threshold, Na⁺ rushes in,", "then K⁺ leaves and resets the cell"]),
 # 4 propagation: a myelinated axon, the signal jumping between nodes
 ('Propagation',
  '<circle cx="24" cy="130" r="13" fill="var(--tint)" stroke="var(--ink)" stroke-width="1.4"/>'
  '<path d="M37 130H222" stroke="var(--ink)" stroke-width="3"/>'
  + "".join(f'<rect x="{x}" y="116" width="46" height="28" rx="13" fill="color-mix(in srgb,var(--gold) 28%,var(--paper))" stroke="var(--gold)" stroke-width="1.3"/>' for x in (46, 102, 158))
  + "".join(f'<path d="M{x} 108Q{x + 28} 66 {x + 56} 108" fill="none" stroke="var(--accent)" stroke-width="1.8" marker-end="url(#ah)"/>' for x in (41, 97, 153))
  + '<text x="69" y="164" text-anchor="middle" font-size="10.5" fill="var(--muted)">myelin</text>'
  '<path d="M97 150V178" stroke="var(--muted)" stroke-width="1"/><text x="97" y="192" text-anchor="middle" font-size="10.5" fill="var(--muted)">node of Ranvier</text>',
  ["Myelin lets the signal jump from", "node to node, so it travels faster"]),
]

def _figure(panels, label):
    body = "".join(_panel(i, t, b, c) for i, (t, b, c) in enumerate(panels))
    return (f'<svg class="diag" style="min-width:880px" viewBox="0 0 1000 278" font-family="var(--sans)" role="img" aria-label="{label}">{_DEFS}{body}</svg>')

# course id -> (heading, one-line caption, svg)
PICTURES = {
 "harvardx-mcb80-1x": ("The course in one picture", "From a resting cell to a travelling signal, in the order the four lessons build it.",
                       _figure(_H1, "Four panels: resting potential, passive membrane properties, the action potential and its propagation along a myelinated axon")),
}
