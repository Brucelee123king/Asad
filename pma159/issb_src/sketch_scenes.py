import json,os,sys
sys.path.insert(0,'/home/user/Asad/pma159/issb_src')
src=open('/home/user/Asad/pma159/issb_src/pic_diagrams.py').read().split('P = []')[0]
exec(src)
L='stroke="#2b2b2b" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"'
L2='stroke="#3a3a3a" stroke-width="1.4" fill="none" stroke-linecap="round"'
def man(x,y,s=1.0,pose='stand',sh=True):
    # sketch figure with head, hair, shirt outline and hatching
    r=9*s;o='<circle cx="%.0f" cy="%.0f" r="%.0f" fill="#efece4" %s/>'%(x,y,r,L)
    o+='<path d="M%.0f %.0f q %.0f %.0f %.0f 0" fill="#3a3a3a"/>'%(x-r,y-2*s,r,-r*1.2,2*r)
    bw=13*s;bt=y+r;bb=y+r+30*s
    o+='<path d="M%.0f %.0f L%.0f %.0f L%.0f %.0f L%.0f %.0f Z" fill="%s" %s/>'%(x-bw,bt+3,x+bw,bt+3,x+bw*0.8,bb,x-bw*0.8,bb,'url(#hatch)' if sh else '#efece4',L)
    lp={'stand':(-6,6,-6,6),'walk':(-12,10,-2,4),'run':(-16,14,-6,10)}[pose if pose in('stand','walk','run') else 'stand']
    o+='<path d="M%.0f %.0f L%.0f %.0f M%.0f %.0f L%.0f %.0f" %s/>'%(x-5*s,bb,x+lp[0]*s,bb+30*s,x+5*s,bb,x+lp[1]*s,bb+30*s,L)
    ap={'stand':((-18,26),(18,26)),'walk':((-16,22),(18,24)),'run':((-22,12),(22,20)),'point':((-16,26),(34,4)),'head':((-14,26),(10,-6)),'hold':((-16,24),(16,18))}[pose]
    o+='<path d="M%.0f %.0f L%.0f %.0f M%.0f %.0f L%.0f %.0f" %s/>'%(x-bw*0.8,bt+8,x+ap[0][0]*s,bt+ap[0][1]*s,x+bw*0.8,bt+8,x+ap[1][0]*s,bt+ap[1][1]*s,L)
    return o
P=[]
# 1 young man at a broken bridge, river below
b=('<path d="M0 120 C 70 110,140 135,210 120 S 300 112,340 118" %s/><path d="M0 150 C 80 140,170 165,250 150 S 320 145,340 150" %s/>'%(L2,L2)
 +''.join('<path d="M%d %d q 8 -4 16 0" %s/>'%(x,y,L2) for x,y in ((40,133),(110,138),(190,132),(260,138),(300,130),(70,160),(160,165),(240,160)))
 +'<path d="M120 112 L178 112 L178 118 L120 118 Z" fill="url(#hatch2)" %s/><path d="M196 116 L250 132 L248 138 L194 122 Z" fill="url(#hatch2)" %s/>'%(L,L)
 +'<path d="M178 112 l6 10 M178 118 l3 9" %s/><path d="M124 118 L124 150 M174 118 L174 150 M246 136 L246 160" %s/>'%(L2,L)
 +man(90,62,1.0,'point')+'<path d="M20 112 L20 70 M14 80 q6 -16 12 0" %s/>'%L+'<circle cx="290" cy="38" r="16" %s/>'%L2)
P.append({'svg':svg(b),'hint':'A young man stands near a broken bridge, pointing across the river. Who is he, what happened, and what does he do?'})
# 2 group around a man lying on road, bike fallen
b=('<path d="M0 135 L340 135 M0 190 L340 190" %s/>'%L+''.join('<path d="M%d 162 l18 0" %s/>'%(x,L) for x in range(10,340,36))
 +'<path d="M110 150 L175 150" stroke="#2b2b2b" stroke-width="7" stroke-linecap="round"/><circle cx="102" cy="148" r="8" fill="#efece4" %s/>'%L
 +'<circle cx="235" cy="160" r="16" %s/><circle cx="290" cy="160" r="16" %s/><path d="M235 160 L262 136 L290 160 M262 136 L255 126 M262 136 L276 140" %s/>'%(L,L,L)
 +man(70,58,0.95,'head')+man(140,56,0.95,'point')+man(200,60,0.9,'hold'))
P.append({'svg':svg(b),'hint':'People gather around a young man lying on the road next to a fallen bicycle. What happened, who helps him, and how does it end?'})
# 3 student at a desk at night, lamp, window with moon
b=('<rect x="230" y="20" width="78" height="62" fill="url(#hatch2)" %s/><circle cx="282" cy="42" r="10" fill="#f3f0e8" %s/><path d="M269 20 L269 82 M230 51 L308 51" %s/>'%(L,L,L)
 +'<path d="M50 125 L260 125 L260 133 L50 133 Z" fill="url(#hatch)" %s/><path d="M60 133 L60 190 M250 133 L250 190" %s/>'%(L,L)
 +'<path d="M205 80 L230 80 L218 62 Z" %s/><path d="M218 80 L218 125" %s/><path d="M150 125 L245 125 L222 80 Z" fill="#fffbe6" opacity=".6"/>'%(L,L)
 +'<path d="M150 118 L200 118 L198 124 L152 124 Z" fill="#fff" %s/><path d="M158 120 l30 0" %s/>'%(L,L2)
 +man(122,84,1.0,'head',False)+'<path d="M50 125 L260 125 L260 133 L50 133 Z" fill="#e9e5da" %s/><path d="M50 125 L260 125 L260 133 L50 133 Z" fill="url(#hatch)" %s/><path d="M150 118 L200 118 L198 124 L152 124 Z" fill="#fff" %s/>'%(L,L,L)+'<path d="M92 133 L92 190 M152 133 L152 190 M88 160 L156 160" %s/>'%L)
P.append({'svg':svg(b),'hint':'A young man sits at a study table late at night under a lamp, holding his head. What is he worried or working about, and what does he decide?'})
# 4 group on a hilltop raising a flag
b=('<path d="M0 200 L120 72 L250 200" fill="url(#hatch)" %s/><path d="M150 200 L262 100 L340 165" %s/>'%(L,L)
 +'<path d="M120 72 L120 22" stroke="#2b2b2b" stroke-width="3"/><path d="M120 22 L160 30 L120 42" fill="url(#hatch2)" %s/>'%L
 +man(98,92,0.85,'point')+man(146,104,0.85,'hold')+man(70,124,0.85,'walk')+'<path d="M200 40 q 10 -8 20 0 q 10 -8 20 0" %s/>'%L2)
P.append({'svg':svg(b),'hint':'A small group climbs to the top of a hill and raises a flag. Who are they, what problem did they face, and what did they achieve?'})
json.dump(P,open('/home/user/Asad/pma159/issb_src/pics.json','w'),ensure_ascii=False)
h='<html><body style="background:#cbd5e1;font-family:sans-serif;display:grid;grid-template-columns:repeat(2,460px);gap:14px;padding:14px;width:960px">'+''.join('<div style="background:#fff;border-radius:14px;padding:12px">%s<p style="color:#555;font-size:13px">%s</p></div>'%(v['svg'],v['hint']) for v in P)+'</body></html>'
open('/tmp/claude-0/-home-user/549049af-53c4-5020-a180-21e595f45279/scratchpad/issb/pics.html','w').write(h);print(len(P))
