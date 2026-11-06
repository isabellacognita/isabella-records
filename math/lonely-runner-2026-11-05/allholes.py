# NOTE 2026-11-06: float grid screen with no exact pass; it reported false survivors near n = 2q+3 (see proof-prime.md, Corrections). A screen only.
# All holes at j/q, gcd(j,q)=1, both sides (Lemma 1 is the same proof for every j). For each q, the largest n with two speeds covering them all, WMAX cap.
import numpy as np,sys
from math import gcd
def holes(q,n):
    x0=1/(2*q*n);a=(n-q)/(q*n*(n-1));H=[]
    for j in range(1,q//2+1):
        if gcd(j,q)!=1: continue
        c=j/q;H+=[(c+x0,c+a),(c-a,c-x0)]
    return H,a>x0
def cover_pair(q,n,WMAX):
    H,ok=holes(q,n)
    if not ok: return None
    pts=np.concatenate([np.linspace(l,h,max(24,int((h-l)*40000))) for l,h in H])
    ws=np.arange(n,WMAX+1)
    inb=lambda w,P:np.abs(((w*P+0.5)%1)-0.5)<=1/n+1e-11
    e=pts[0]
    C=ws[inb(ws,np.array([e]))]
    for a in C:
        unc=pts[~inb(a,pts)]
        if len(unc)==0: return (int(a),None)
        D=ws[inb(ws,unc[:1])]
        for t in unc[len(unc)//2:len(unc)//2+1]: D=D[inb(D,np.array([t]))]
        for b in D:
            if inb(b,unc).all(): return (int(min(a,b)),int(max(a,b)))
    return None
WMAX=int(sys.argv[1]); out=[]
for q in range(3,int(sys.argv[2])+1):
    last=None;wit=None
    for n in range(2*q+1,int(5.2*q)+24):
        r=cover_pair(q,n,WMAX)
        if r: last,wit=n,r
    print(q,'phi-holes',sum(1 for j in range(1,q//2+1) if gcd(j,q)==1)*2,'last n',last,wit,'last/q',round(last/q,2) if last else None,flush=True)
