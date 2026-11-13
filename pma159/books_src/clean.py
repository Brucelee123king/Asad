import cv2,numpy as np,subprocess,glob,os,re,csv,io,sys
os.makedirs('c',exist_ok=True)
BAD=re.compile(r'(issb.?notes|gmail|blogspot|preparationnotes|http|0322|5411956|contact\s*#)',re.I)
STAMP=re.compile(r'^[^a-z]*complete[^a-z]*$|^notes',re.I)
def ocr(img):
    ok,buf=cv2.imencode('.png',img)
    out=subprocess.run(['tesseract','stdin','stdout','--psm','11','tsv'],input=buf.tobytes(),capture_output=True).stdout.decode('utf8','ignore')
    rows=list(csv.DictReader(io.StringIO(out),delimiter='\t',quoting=csv.QUOTE_NONE))
    return [r for r in rows if r.get('text','').strip() and float(r.get('conf','-1'))>20]
log=[]
for f in sorted(glob.glob('r/p-*.png')):
    n=int(re.search(r'(\d+)',os.path.basename(f)).group(1))
    im=cv2.imread(f);H,W=im.shape[:2];g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # 1) header: white-out everything above the header rule
    rule=None
    for y in range(int(H*.03),int(H*.12)):
        row=g[y];dark=(row<215).sum()
        if dark>W*.55: rule=y;break
    if rule is None or rule<140: rule=150
    im[0:max(0,rule-2),:]=255
    # 2) OCR the rest; wipe any stamp/contact words
    words=ocr(im);mask=np.zeros((H,W),np.uint8);hits=[]
    for r in words:
        t=r['text'].strip()
        if BAD.search(t):
            x,y,w,h=int(r['left']),int(r['top']),int(r['width']),int(r['height'])
            if y<rule: continue
            hits.append(t);cv2.rectangle(mask,(x-8,y-8),(x+w+8,y+h+8),255,-1)
    # line-level: if a line contains a bad word, wipe the whole line (catches "Complete Notes at")
    if hits:
        byline={}
        for r in words:
            k=(r['block_num'],r['par_num'],r['line_num']);byline.setdefault(k,[]).append(r)
        for k,ws in byline.items():
            near=any(BAD.search(r2['text']) and 0<=int(r2['top'])-int(ws[0]['top'])<90 and abs(int(r2['left'])-int(ws[0]['left']))<200 for r2 in words)
            if any(BAD.search(w['text']) for w in ws) or (near and any(STAMP.search(w['text']) for w in ws) and len(ws)<=4):
                for r in ws:
                    x,y,w,h=int(r['left']),int(r['top']),int(r['width']),int(r['height'])
                    cv2.rectangle(mask,(x-8,y-8),(x+w+8,y+h+8),255,-1)
        # fill: white if the area is plain white, else inpaint
        cnts,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            x,y,w,h=cv2.boundingRect(c);pad=im[max(0,y-6):y+h+6,max(0,x-6):x+w+6]
            if np.median(pad)>235: im[y:y+h,x:x+w]=255
            else:
                im=cv2.inpaint(im,(mask[:, :]*0+0).astype(np.uint8) if False else np.where((np.indices(mask.shape)[0]>=y)&(np.indices(mask.shape)[0]<y+h)&(np.indices(mask.shape)[1]>=x)&(np.indices(mask.shape)[1]<x+w),255,0).astype(np.uint8),9,cv2.INPAINT_TELEA)
    cv2.imwrite('c/p-%03d.png'%n,im);log.append((n,rule,hits))
    print(n,rule,hits,flush=True)
