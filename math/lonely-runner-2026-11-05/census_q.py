# Two-entry modifications of [n-1]: remove {q,r}, add {w1<w2}, w>=n. Which are tight (every t within 1/n of a multiple for some speed)?
# Grid screens, exact Fractions confirm. Base set must leave a hole, else any pair works and it isn't interesting.
import sys, numpy as np
from fractions import Fraction as F
from math import floor,ceil,gcd
from functools import reduce
def holes(V,n):
    e=F(1,n); arcs=[]
    for v in V:
        for k in range(0,v//2+2):
            a=(k-e)/v;b=(k+e)/v
            if b<0 or a>F(1,2): continue
            arcs.append((max(a,F(0)),min(b,F(1,2))))
    arcs.sort(); cur=F(0); out=[]
    for a,b in arcs:
        if a>cur: out.append((cur,a))
        cur=max(cur,b)
    if cur<F(1,2): out.append((cur,F(1,2)))
    return out
def covered_exact(hs,ws,n):
    e=F(1,n)
    for lo,hi in hs:
        arcs=[]
        for w in ws:
            for k in range(floor(lo*w)-1,ceil(hi*w)+2):
                a=(k-e)/w;b=(k+e)/w
                if b<lo or a>hi: continue
                arcs.append((a,b))
        arcs.sort(); cur=lo; ok=True
        for a,b in arcs:
            if a>cur: ok=False;break
            cur=max(cur,b)
        if cur<hi: ok=False
        if not ok: return False
    return True
def run(n,WMAX,qs):
    res=[]
    for q in qs:
        for r in range(1,n):
            if r==q or (r<q and r in qs): continue
            V=[v for v in range(1,n) if v not in(q,r)]
            hs=holes(V,n)
            if not hs: continue
            pts=np.concatenate([np.linspace(float(a),float(b),max(8,int(float(b-a)*40000)))[1:-1] for a,b in hs if b>a])
            if len(pts)==0: continue
            ws=np.arange(n,WMAX+1)
            M=np.abs(((ws[:,None]*pts[None,:]+0.5)%1)-0.5)<=1/n+1e-11
            N=~M
            cnt=N.astype(np.int32)@N.T.astype(np.int32)
            for i,j in zip(*np.where(np.triu(cnt==0,1))):
                w1,w2=int(ws[i]),int(ws[j])
                if covered_exact(hs,[w1,w2],n):
                    S=sorted(V+[w1,w2]); g=reduce(gcd,S)
                    res.append((n,q,r,w1,w2,g))
    return res
if __name__=='__main__':
    for n in range(7,int(sys.argv[1])+1):
        R=run(n,int(sys.argv[2]),list(range(2,n)))
        print(n,len(R),R[:14],flush=True)
