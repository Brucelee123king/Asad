"""Own mechanical-aptitude diagrams (SVG) for the ISSB page. Writes issb_src/mech.json: [{q, a, svg}]"""
import json, math, os
here = os.path.dirname(os.path.abspath(__file__))
S = 'stroke="#1e293b" stroke-width="3" fill="none"'
F = 'fill="#1e293b"'


def svg(body, w=320, h=180):
    return '<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" style="width:100%%;max-width:420px;background:#fff;border-radius:10px">%s</svg>' % (w, h, body)


def gear(cx, cy, r, teeth, label, col='#fde68a'):
    pts = []
    for i in range(teeth * 2):
        a = math.pi * i / teeth
        rr = r + 7 if i % 2 == 0 else r
        pts.append('%.1f,%.1f' % (cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return ('<polygon points="%s" fill="%s" stroke="#1e293b" stroke-width="2.5"/><circle cx="%d" cy="%d" r="5" %s/>'
            '<text x="%d" y="%d" font-size="16" font-weight="700" text-anchor="middle" fill="#1e293b">%s</text>') % (' '.join(pts), col, cx, cy, F, cx, cy - r - 14, label)


def arrow_cw(cx, cy, r, cw=True, col='#dc2626'):
    a0, a1 = (-2.4, -0.8) if cw else (-0.8, -2.4)
    x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
    return ('<path d="M%.1f %.1f A%d %d 0 0 %d %.1f %.1f" stroke="%s" stroke-width="3" fill="none" marker-end="url(#ah)"/>'
            % (x0, y0, r, r, 1 if cw else 0, x1, y1, col))


DEFS = '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#dc2626"/></marker></defs>'
Q = []
# 1 three gears in a row
b = DEFS + gear(70, 110, 32, 10, '') + gear(150, 110, 32, 10, '') + gear(230, 110, 32, 10, '') + arrow_cw(70, 110, 52, True) + '<text x="70" y="170" font-size="18" font-weight="800" text-anchor="middle">A</text><text x="150" y="170" font-size="18" font-weight="800" text-anchor="middle">B</text><text x="230" y="170" font-size="18" font-weight="800" text-anchor="middle">C</text>'
Q.append({'q': 'Gear A turns clockwise. Which way does gear C turn?', 'opts': ['Clockwise', 'Anticlockwise', 'It does not turn'], 'a': 'Clockwise. Each gear turns the next one the opposite way: A clockwise, B anticlockwise, C clockwise.', 'svg': svg(b)})
# 2 big and small gear
b = DEFS + gear(100, 95, 55, 20, 'A (20 teeth)') + gear(197, 95, 28, 10, 'B (10 teeth)', '#bae6fd')
Q.append({'q': 'Gear A has 20 teeth and gear B has 10 teeth. When A makes 1 full turn, how many turns does B make?', 'opts': ['1/2', '1', '2', '4'], 'a': '2 turns. B has half as many teeth, so it turns twice as fast.', 'svg': svg(b)})
# 3 crossed belt
b = DEFS + '<circle cx="80" cy="90" r="40" fill="#fde68a" stroke="#1e293b" stroke-width="3"/><circle cx="240" cy="90" r="40" fill="#bae6fd" stroke="#1e293b" stroke-width="3"/>' \
    '<line x1="80" y1="50" x2="240" y2="130" %s/><line x1="80" y1="130" x2="240" y2="50" %s/><text x="80" y="96" font-size="18" font-weight="700" text-anchor="middle">A</text><text x="240" y="96" font-size="18" font-weight="700" text-anchor="middle">B</text>' % (S, S) + arrow_cw(80, 90, 56, True)
Q.append({'q': 'Wheel A turns clockwise. The belt is crossed. Which way does wheel B turn?', 'opts': ['Clockwise', 'Anticlockwise'], 'a': 'Anticlockwise. A crossed belt makes the second wheel turn the opposite way.', 'svg': svg(b)})
# 4 lever: where to push
b = DEFS + '<polygon points="150,150 135,175 165,175" fill="#94a3b8" stroke="#1e293b" stroke-width="2"/><rect x="20" y="140" width="280" height="10" fill="#a16207"/>' \
    '<rect x="105" y="105" width="38" height="35" fill="#475569"/><text x="124" y="128" font-size="13" fill="#fff" text-anchor="middle">LOAD</text>' \
    + ''.join('<text x="%d" y="88" font-size="20" font-weight="800" text-anchor="middle" fill="#dc2626">%s</text><line x1="%d" y1="96" x2="%d" y2="134" stroke="#dc2626" stroke-width="3" marker-end="url(#ah)"/>' % (x, t, x, x) for x, t in ((190, 'X'), (240, 'Y'), (290, 'Z')))
Q.append({'q': 'The load is on the left of the pivot. At which point (X, Y or Z) will you need the LEAST force to lift it?', 'opts': ['X', 'Y', 'Z'], 'a': 'Z. The farther you push from the pivot, the less force you need.', 'svg': svg(b, 320, 185)})
# 5 seesaw balance
b = '<polygon points="160,130 145,160 175,160" fill="#94a3b8" stroke="#1e293b" stroke-width="2"/><rect x="20" y="120" width="280" height="10" fill="#a16207"/>' \
    '<rect x="100" y="80" width="40" height="40" fill="#475569"/><text x="120" y="105" font-size="13" fill="#fff" text-anchor="middle">20 kg</text>' \
    '<rect x="260" y="80" width="40" height="40" fill="#f59e0b"/><text x="280" y="105" font-size="16" font-weight="800" fill="#fff" text-anchor="middle">?</text>' \
    '<text x="140" y="60" font-size="14" font-weight="700" text-anchor="middle">2 m</text><text x="220" y="60" font-size="14" font-weight="700" text-anchor="middle">4 m</text>' \
    '<line x1="120" y1="68" x2="160" y2="68" stroke="#64748b" stroke-width="2" stroke-dasharray="4 3"/><line x1="160" y1="68" x2="280" y2="68" stroke="#64748b" stroke-width="2" stroke-dasharray="4 3"/><line x1="160" y1="60" x2="160" y2="120" stroke="#64748b" stroke-dasharray="3 3"/>'
Q.append({'q': 'A 20 kg box is 2 m from the pivot. What weight is needed 4 m on the other side to balance it?', 'opts': ['5 kg', '10 kg', '20 kg', '40 kg'], 'a': '10 kg. 20 × 2 = 40, and 10 × 4 = 40, so it balances.', 'svg': svg(b)})
# 6 movable pulley
b = DEFS + '<rect x="20" y="10" width="280" height="12" fill="#64748b"/><line x1="110" y1="22" x2="110" y2="110" %s/><circle cx="140" cy="110" r="30" fill="#fde68a" stroke="#1e293b" stroke-width="3"/>' % S + \
    '<line x1="170" y1="110" x2="170" y2="40" %s/><line x1="140" y1="140" x2="140" y2="155" %s/><rect x="115" y="155" width="50" height="22" fill="#475569"/><text x="140" y="171" font-size="12" fill="#fff" text-anchor="middle">100 N</text>' % (S, S) + \
    '<line x1="170" y1="40" x2="170" y2="25" stroke="#dc2626" stroke-width="3" marker-end="url(#ah)"/><text x="200" y="45" font-size="14" font-weight="700" fill="#dc2626">pull = ?</text>'
Q.append({'q': 'A 100 N load hangs from one movable pulley. Ignoring friction, how much force is needed to lift it?', 'opts': ['25 N', '50 N', '100 N', '200 N'], 'a': '50 N. A single movable pulley halves the force (two rope parts share the load).', 'svg': svg(b)})
# 7 water tank taps
b = '<rect x="90" y="15" width="140" height="150" fill="#e0f2fe" stroke="#1e293b" stroke-width="3"/><rect x="92" y="35" width="136" height="128" fill="#7dd3fc"/>' + \
    ''.join('<rect x="230" y="%d" width="30" height="10" fill="#475569"/><text x="275" y="%d" font-size="16" font-weight="800">%s</text>' % (y, y + 10, t) for y, t in ((55, 'A'), (95, 'B'), (140, 'C')))
Q.append({'q': 'The tank is full of water. From which tap will water come out with the MOST force?', 'opts': ['A', 'B', 'C'], 'a': 'C. Water pressure is highest at the bottom of the tank.', 'svg': svg(b)})
# 8 wheel and axle / bicycle gears
b = DEFS + gear(90, 95, 50, 18, '') + gear(240, 95, 22, 8, '', '#bae6fd') + '<text x="90" y="175" font-size="14" font-weight="800" text-anchor="middle">Front (big)</text><text x="240" y="175" font-size="14" font-weight="800" text-anchor="middle">Back (small)</text>' + \
    '<line x1="90" y1="38" x2="240" y2="66" %s/><line x1="90" y1="152" x2="240" y2="124" %s/>' % (S, S)
Q.append({'q': 'On a bicycle, the front gear is big and the back gear is small. For one turn of the pedals, the back wheel turns:', 'opts': ['Less than once', 'Exactly once', 'More than once'], 'a': 'More than once. The small back gear turns faster than the big front gear.', 'svg': svg(b)})
json.dump(Q, open(os.path.join(here, 'mech.json'), 'w'), ensure_ascii=False)
print(len(Q))
