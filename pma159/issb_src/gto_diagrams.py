"""Own GTO / planning diagrams (SVG) for the ISSB page. Writes issb_src/gto.json: {section: {svg, caption}}"""
import json, os
here = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(here, 'final.json'), encoding='utf8'))


def svg(body, w=340, h=200):
    return ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" style="width:100%%;max-width:440px;background:#f0fdf4;border-radius:10px">'
            '<defs><pattern id="hz" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#fee2e2"/><line x1="0" y1="0" x2="0" y2="8" stroke="#dc2626" stroke-width="3"/></pattern>'
            '<marker id="ga" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#1e3a8a"/></marker></defs>%s</svg>') % (w, h, body)


def t(x, y, s, sz=12, c='#1e293b', w=700, a='middle'):
    return '<text x="%d" y="%d" font-size="%d" font-weight="%d" fill="%s" text-anchor="%s" font-family="sans-serif">%s</text>' % (x, y, sz, w, c, a, s)


def plank(x, y, l, ang=0, lab='plank'):
    return '<g transform="rotate(%d %d %d)"><rect x="%d" y="%d" width="%d" height="9" fill="#a16207" stroke="#713f12"/></g>' % (ang, x, y, x, y, l) + (t(x + l // 2, y - 5, lab, 10, '#713f12') if lab else '')


def drum(x, y):
    return '<rect x="%d" y="%d" width="22" height="30" rx="4" fill="#475569"/><ellipse cx="%d" cy="%d" rx="11" ry="4" fill="#64748b"/>' % (x, y, x + 11, y) + t(x + 11, y + 44, 'drum', 10)


def rope(x1, y1, x2, y2):
    return '<path d="M%d %d Q %d %d %d %d" stroke="#92400e" stroke-width="2.5" fill="none" stroke-dasharray="6 3"/>' % (x1, y1, (x1 + x2) // 2, max(y1, y2) + 20, x2, y2)


def oob(x, y, w, h):
    return '<rect x="%d" y="%d" width="%d" height="%d" fill="url(#hz)" stroke="#dc2626" stroke-width="2"/>' % (x, y, w, h)


def load(x, y):
    return '<rect x="%d" y="%d" width="26" height="20" fill="#f59e0b" stroke="#78350f"/>' % (x, y) + t(x + 13, y + 34, 'load', 10, '#78350f')


LEG = (t(14, 190, 'Hatched red = out of bounds (do not touch)', 10, '#991b1b', 700, 'start'))
G = {}
# PGT: start -> 3 obstacles -> finish
b = ('<rect x="0" y="0" width="340" height="200" fill="#ecfccb"/>' + '<line x1="20" y1="30" x2="20" y2="160" stroke="#16a34a" stroke-width="5"/>' + t(20, 22, 'START', 11, '#166534')
     + '<line x1="320" y1="30" x2="320" y2="160" stroke="#1e3a8a" stroke-width="5"/>' + t(320, 22, 'FINISH', 11, '#1e3a8a')
     + oob(60, 70, 50, 70) + '<rect x="135" y="60" width="16" height="80" fill="#94a3b8"/>' + t(143, 54, 'wall', 10) + oob(175, 85, 60, 55)
     + '<rect x="255" y="70" width="14" height="70" fill="#94a3b8"/>' + t(262, 64, 'pole', 10)
     + plank(30, 105, 70, -20, '') + drum(110, 110) + load(25, 140) + rope(150, 70, 255, 75)
     + '<path d="M40 175 L300 175" stroke="#1e3a8a" stroke-width="2" marker-end="url(#ga)"/>' + t(170, 170, 'whole group carries everything across', 10, '#1e3a8a') + LEG)
G['pgt'] = {'svg': svg(b), 'caption': 'Progressive Group Task: the whole group crosses 3-4 obstacles in a row, carrying a load, using planks, drums and ropes. Rules get harder at each obstacle.'}
# HGT: same idea, half group, 1-2 obstacles
b = ('<rect x="0" y="0" width="340" height="200" fill="#ecfccb"/>' + '<line x1="30" y1="30" x2="30" y2="160" stroke="#16a34a" stroke-width="5"/>' + t(30, 22, 'START', 11, '#166534')
     + '<line x1="310" y1="30" x2="310" y2="160" stroke="#1e3a8a" stroke-width="5"/>' + t(310, 22, 'FINISH', 11, '#1e3a8a')
     + oob(110, 60, 120, 90) + plank(80, 100, 110, 0) + drum(200, 70) + rope(60, 60, 290, 60) + load(45, 135)
     + t(170, 175, 'half the group (4-5 candidates), more chance to show ideas', 10, '#1e3a8a') + LEG)
G['hgt'] = {'svg': svg(b), 'caption': 'Half Group Task: like PGT but with only half the group and fewer obstacles, so each candidate gets more chance to give and use ideas.'}
# Command task
b = ('<rect x="0" y="0" width="340" height="200" fill="#ecfccb"/>' + oob(110, 70, 110, 80) + plank(70, 95, 70, 0) + plank(225, 95, 60, 0, '') + drum(250, 115)
     + ''.join('<circle cx="%d" cy="%d" r="11" fill="%s" stroke="#1e293b" stroke-width="2"/>' % (x, y, c) + t(x, y + 4, l, 11, '#fff') for x, y, l, c in ((40, 60, 'C', '#dc2626'), (40, 100, 'H', '#2563eb'), (40, 140, 'H', '#2563eb')))
     + t(95, 35, 'C = commander (you), H = helpers you choose', 11, '#991b1b', 700, 'start') + '<path d="M60 160 L300 160" stroke="#1e3a8a" stroke-width="2" marker-end="url(#ga)"/>'
     + t(180, 178, 'plan, give clear orders, cross with your helpers', 10, '#1e3a8a') + LEG)
G['command'] = {'svg': svg(b), 'caption': 'Command Task: you are the commander. You pick 1-2 helpers, explain your plan clearly, and lead them across the obstacle.'}
# FGT
b = ('<rect x="0" y="0" width="340" height="200" fill="#ecfccb"/>' + '<line x1="25" y1="30" x2="25" y2="160" stroke="#16a34a" stroke-width="5"/>' + t(25, 22, 'START', 11, '#166534')
     + '<line x1="315" y1="30" x2="315" y2="160" stroke="#1e3a8a" stroke-width="5"/>' + t(315, 22, 'FINISH', 11, '#1e3a8a')
     + oob(90, 60, 170, 95) + plank(60, 80, 120, 0) + plank(180, 120, 110, 0) + drum(170, 60) + load(35, 130)
     + t(170, 178, 'last group task: one big obstacle, whole group', 10, '#1e3a8a') + LEG)
G['fgt'] = {'svg': svg(b), 'caption': 'Final Group Task: the last group task on the final day, one bigger obstacle for the whole group. Show your best teamwork.'}
# IOT course: numbered obstacles
names = [o for o in D.get('iot', {}).get('obstacles', [])][:10] or ['Obstacle %d' % i for i in range(1, 11)]
pts = [(40, 40), (110, 40), (180, 40), (250, 40), (310, 75), (250, 110), (180, 110), (110, 110), (40, 110), (40, 160)]
b = '<rect x="0" y="0" width="340" height="200" fill="#ecfccb"/>' + '<polyline points="%s" fill="none" stroke="#1e3a8a" stroke-width="2" stroke-dasharray="5 4"/>' % ' '.join('%d,%d' % p for p in pts)
for i, (x, y) in enumerate(pts):
    b += '<circle cx="%d" cy="%d" r="13" fill="#f59e0b" stroke="#78350f" stroke-width="2"/>' % (x, y) + t(x, y + 4, str(i + 1), 12, '#3b2a05', 800)
b += t(200, 165, '10 obstacles, 3 minutes, numbers = marks', 11, '#1e3a8a') + t(200, 182, 'do them in any order you like', 10, '#1e3a8a')
G['iot'] = {'svg': svg(b), 'caption': 'Individual Obstacles: about 10 obstacles numbered 1 to 10 (the number is the marks). You have about 3 minutes; plan your route and attempt as many as you can. ' + ('Obstacles: ' + ', '.join(names) if names else '')}
# Planning map
b = ('<rect x="0" y="0" width="340" height="200" fill="#f7fee7"/>'
     + '<path d="M0 120 C 80 100, 140 150, 220 120 S 340 110, 340 110 L340 140 C 300 140, 260 160, 220 150 S 80 130, 0 150 Z" fill="#7dd3fc"/>' + t(300, 150, 'river', 10, '#075985')
     + '<path d="M20 30 L320 30" stroke="#78716c" stroke-width="7"/>' + t(170, 24, 'main road', 10)
     + '<path d="M150 30 L150 190" stroke="#a8a29e" stroke-width="5"/>' + '<rect x="140" y="118" width="20" height="26" fill="#a16207"/>' + t(185, 112, 'bridge', 10)
     + ''.join('<rect x="%d" y="%d" width="12" height="10" fill="#b45309"/>' % (x, y) for x, y in ((40, 55), (56, 55), (40, 70), (56, 70))) + t(55, 98, 'village', 10)
     + '<circle cx="260" cy="70" r="9" fill="#dc2626"/>' + t(260, 95, 'accident', 10, '#991b1b')
     + '<circle cx="90" cy="175" r="9" fill="#dc2626"/>' + t(90, 196, 'fire', 10, '#991b1b')
     + '<rect x="270" y="165" width="34" height="20" fill="#1e40af"/>' + t(287, 179, 'H', 11, '#fff') + t(287, 160, 'hospital', 10, '#1e3a8a')
     + '<circle cx="200" cy="58" r="8" fill="#16a34a"/>' + t(200, 50, 'you', 10, '#166534'))
G['planning'] = {'svg': svg(b), 'caption': 'Group Planning map (example): you are given a map with several problems at once (fire, accident) and limited time and resources. Read the scale and distances, list problems by urgency, use roads and the bridge wisely, and share your team.'}
json.dump(G, open(os.path.join(here, 'gto.json'), 'w'), ensure_ascii=False)
print(list(G))
