import cv2,numpy as np,glob,os,re
os.makedirs('f',exist_ok=True)
def lines(g,ys):
    out=[]
    for y in ys:
        row=g[y]<225;n=row.sum()
        if n>500:
            xs=np.where(row)[0];out.append((y,xs.min(),xs.max(),n))
    return out
for f in sorted(glob.glob('c/p-*.png')):
    n=int(re.search(r'(\d+)',os.path.basename(f)).group(1))
    im=cv2.imread(f);H,W=im.shape[:2]
    o=cv2.imread('r/p-%02d.png'%n);go=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
    for band in (range(120,215),range(int(H*.88),int(H*.97))):
        L=lines(go,band)
        if not L: continue
        # group consecutive rows; draw each found rule thicker in its own colour
        y,x0,x1,_=max(L,key=lambda t:t[3])
        col=[int(v) for v in o[y,(x0+x1)//2]]
        if band.start<300:
            cv2.rectangle(im,(x0,y-2),(x1,y+2),col,-1)
        else:
            cv2.rectangle(im,(x0,y-1),(x1,y+2),(120,120,120),-1)
    if n==2: im[1260:1520,:]=255
    im=cv2.copyMakeBorder(im,46,46,46,46,cv2.BORDER_CONSTANT,value=(255,255,255));H2,W2=im.shape[:2]
    cv2.rectangle(im,(22,22),(W2-23,H2-23),(30,74,46),7)
    cv2.rectangle(im,(36,36),(W2-37,H2-37),(80,160,200),2)
    cv2.imwrite('f/p-%03d.png'%n,im)
print('done')
