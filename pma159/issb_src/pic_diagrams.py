"""Own simple drawn scenes for ISSB picture-story practice. Writes issb_src/pics.json: [{svg, hint}]"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))


SK = ('<defs><filter id="pn" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" result="n"/>'
      '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.2" xChannelSelector="R" yChannelSelector="G" result="d"/>'
      '<feColorMatrix in="d" type="saturate" values="0" result="g"/><feComponentTransfer in="g"><feFuncR type="gamma" exponent="1.4"/><feFuncG type="gamma" exponent="1.4"/><feFuncB type="gamma" exponent="1.4"/></feComponentTransfer></filter>'
      '<pattern id="hatch" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line x1="0" y1="0" x2="0" y2="5" stroke="#555" stroke-width="0.9"/></pattern>'
      '<pattern id="hatch2" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><line x1="0" y1="0" x2="0" y2="4" stroke="#333" stroke-width="1.1"/></pattern>'
      '<filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="0.6" numOctaves="3" seed="7"/><feColorMatrix values="0 0 0 0 0.94  0 0 0 0 0.92  0 0 0 0 0.87  0 0 0 0.35 0"/><feBlend in="SourceGraphic" mode="multiply"/></filter></defs>')


def svg(b):
    return ('<svg viewBox="0 0 340 200" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:440px;border-radius:6px">' + SK
            + '<rect width="340" height="200" fill="#f3f0e8" filter="url(#paper)"/><g filter="url(#pn)">' + b + '</g>'
            + '<rect x="3" y="3" width="334" height="194" fill="none" stroke="#444" stroke-width="1.5"/></svg>')


def person(x, y, c='#334155', s=1.0, arm=0):
    r = 7 * s
    return ('<circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/>' % (x, y, r, c)
            + '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x, y + r, x, y + 28 * s, c, 4 * s)
            + '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x, y + 28 * s, x - 7 * s, y + 46 * s, c, 4 * s)
            + '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x, y + 28 * s, x + 7 * s, y + 46 * s, c, 4 * s)
            + '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x, y + 14 * s, x - 10 * s, y + (24 - arm) * s, c, 3.5 * s)
            + '<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"/>' % (x, y + 14 * s, x + 11 * s, y + (24 - arm) * s, c, 3.5 * s))


P = []
# 1 young man near a broken bridge over a river, evening
b = ('<rect width="340" height="200" fill="#fde68a"/><rect y="110" width="340" height="90" fill="#86efac"/>'
     '<path d="M0 135 C 90 120, 200 160, 340 140 L340 175 C 220 190, 100 160, 0 175 Z" fill="#60a5fa"/>'
     '<rect x="120" y="120" width="40" height="8" fill="#92400e"/><rect x="185" y="126" width="45" height="8" fill="#92400e" transform="rotate(14 185 126)"/>'
     '<circle cx="290" cy="45" r="20" fill="#fb923c"/>' + person(95, 72, '#1f2937', 1.1, 8) + '<rect x="40" y="88" width="16" height="22" fill="#78350f"/>')
P.append({'svg': svg(b), 'hint': 'A young man stands near a broken bridge in the evening. Who is he, what happened, and what does he do?'})
# 2 people around someone lying on the road
b = ('<rect width="340" height="200" fill="#e2e8f0"/><rect y="120" width="340" height="80" fill="#64748b"/>'
     '<line x1="0" y1="160" x2="340" y2="160" stroke="#f8fafc" stroke-width="4" stroke-dasharray="20 14"/>'
     '<rect x="230" y="90" width="80" height="34" rx="6" fill="#ef4444"/><circle cx="248" cy="126" r="9" fill="#111"/><circle cx="292" cy="126" r="9" fill="#111"/>'
     '<line x1="120" y1="150" x2="170" y2="150" stroke="#1f2937" stroke-width="6" stroke-linecap="round"/><circle cx="114" cy="148" r="7" fill="#1f2937"/>'
     + person(90, 88, '#0f766e', 1.0, 4) + person(150, 86, '#7c2d12', 1.0, -6) + person(195, 90, '#1e3a8a', 0.95, 2))
P.append({'svg': svg(b), 'hint': 'People gather around someone lying on a road near a car. What happened, who helps, and how does it end?'})
# 3 a student at a desk at night with a lamp
b = ('<rect width="340" height="200" fill="#1e293b"/><rect x="230" y="25" width="70" height="60" fill="#0f172a" stroke="#475569" stroke-width="4"/><circle cx="280" cy="45" r="9" fill="#fef9c3"/>'
     '<rect x="60" y="120" width="190" height="10" fill="#92400e"/><rect x="70" y="130" width="8" height="60" fill="#92400e"/><rect x="232" y="130" width="8" height="60" fill="#92400e"/>'
     '<polygon points="200,80 230,80 215,60" fill="#fbbf24"/><line x1="215" y1="80" x2="215" y2="120" stroke="#fbbf24" stroke-width="3"/>'
     '<path d="M140 120 L250 120 L215 80 Z" fill="#fef9c3" opacity=".25"/><rect x="150" y="112" width="40" height="8" fill="#e2e8f0"/>'
     + person(125, 70, '#e2e8f0', 1.05, 10))
P.append({'svg': svg(b), 'hint': 'A young person sits at a desk late at night under a lamp. What is he working on, and why is it important to him?'})
# 4 group on a hill with a flag
b = ('<rect width="340" height="200" fill="#bae6fd"/><path d="M0 200 L120 70 L250 200 Z" fill="#65a30d"/><path d="M150 200 L260 100 L340 170 L340 200 Z" fill="#4d7c0f"/>'
     '<line x1="120" y1="70" x2="120" y2="25" stroke="#1f2937" stroke-width="3"/><rect x="120" y="25" width="34" height="22" fill="#15803d"/><rect x="120" y="25" width="9" height="22" fill="#fff"/>'
     + person(100, 98, '#1f2937', 0.9, 14) + person(140, 106, '#1f2937', 0.9, 0) + person(75, 126, '#1f2937', 0.9, 6))
P.append({'svg': svg(b), 'hint': 'A small group reaches the top of a hill and raises a flag. Who are they, what did they face, and what did they achieve?'})
json.dump(P, open(os.path.join(here, 'pics.json'), 'w'), ensure_ascii=False)
print(len(P))
