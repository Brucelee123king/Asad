import cv2,numpy as np,subprocess,csv,io,re
BAD=re.compile(r'(issbno|notes|gmai|\.com|^@|complete)',re.I)
def ocr(img):
    ok,buf=cv2.imencode('.png',img)
    out=subprocess.run(['tesseract','stdin','stdout','--psm','11','tsv'],input=buf.tobytes(),capture_output=True).stdout.decode('utf8','ignore')
    return [r for r in csv.DictReader(io.StringIO(out),delimiter='\t',quoting=csv.QUOTE_NONE) if r.get('text','').strip() and float(r.get('conf','-1'))>10]
pages=list(range(12,26))+list(range(84,94))
for n in pages:
    f='c/p-%03d.png'%n;im=cv2.imread(f);H,W=im.shape[:2];g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    # find picture region: rows/cols with non-white content below header
    nz=np.where(g[200:H-150]<200);
    if len(nz[0])==0: continue
    y0,y1=nz[0].min()+200,nz[0].max()+200;x0,x1=nz[1].min(),nz[1].max()
    mask=np.zeros((H,W),np.uint8);hits=[]
    crop=im[y0:y1,x0:x1]
    for variant in ('n','i'):
        v=crop if variant=='n' else 255-crop
        big=cv2.resize(v,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
        rows=ocr(big);lines={}
        for r in rows:lines.setdefault((r['block_num'],r['par_num'],r['line_num']),[]).append(r)
        for ws in lines.values():
          if not any(BAD.search(w['text']) for w in ws) or len(ws)>5: continue
          for r in ws:
            t=r['text'].strip()
            if True:
                x,y,w,h=[int(r[k])//2 for k in ('left','top','width','height')]
                if h>60 or w>600: continue
                hits.append(t);cv2.rectangle(mask,(x0+x-10,y0+y-10),(x0+x+w+10,y0+y+h+10),255,-1)
    if hits:
        k=cv2.getStructuringElement(cv2.MORPH_RECT,(40,30));mask=cv2.dilate(mask,k)
        im=cv2.inpaint(im,mask,7,cv2.INPAINT_TELEA);cv2.imwrite(f,im)
    print(n,hits,flush=True)
# page 2: remove the contact box completely
im=cv2.imread('c/p-002.png');im[1270:1510,:]=255;cv2.imwrite('c/p-002.png',im)
# last page: remove 'For any question Email us'
im=cv2.imread('c/p-094.png');g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
for r in ocr(im):
    if re.search(r'question|email|any|For|us',r['text'],re.I):
        x,y,w,h=[int(r[k]) for k in ('left','top','width','height')]
        if y<1000:im[y-10:y+h+10,x-10:x+w+10]=255
cv2.imwrite('c/p-094.png',im)
