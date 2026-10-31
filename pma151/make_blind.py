import json,re,sys
f=json.load(open('hk_final3.json')); START=3201
L="ABCDE"; new=f[START:]
N=int(sys.argv[1]) if len(sys.argv)>1 else 160
for k in range(0,len(new),N):
    with open('verify/blind_%02d.txt'%(k//N+1),'w') as o:
        for j,x in enumerate(new[k:k+N]):
            n=START+k+j+1
            o.write('%d. %s  %s\n'%(n,x[1],'  '.join('%s) %s'%(L[i],t) for i,t in enumerate(x[2]))))
print(len(new),'new MCQs ->',(len(new)+N-1)//N,'files')
