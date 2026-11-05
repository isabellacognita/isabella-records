# Independent of the bounds in the proof: every pair u<v<=VMAX, n=7..15, does {u,v} cover the hole? Compare with enumerate_pairs' answer.
import sys
sys.argv=['x']
from fractions import Fraction as F
from math import floor,ceil
def hole(n):
    o=n-1 if (n-1)%2 else n-2
    return F(1,4*n),F(n-2,2*n*o)
def wins(n,w,lo,hi):
    e=F(1,n); s=F(0) if w%2==0 else F(1,2); out=[]
    for k in range(floor(lo*w-s-1),ceil(hi*w-s+1)+1):
        a=(k+s-e)/w;b=(k+s+e)/w
        if b<lo or a>hi: continue
        out.append((max(a,lo),min(b,hi)))
    return out
def covered(lo,hi,ws):
    cur=lo
    for a,b in sorted(ws):
        if a>cur: return False
        cur=max(cur,b)
        if cur>=hi: return True
    return cur>=hi
for n in range(7,16):
    lo,hi=hole(n); VMAX=600
    W={w:wins(n,w,lo,hi) for w in range(n,VMAX+1)}
    res=[(u,v) for u in W for v in W if u<v and covered(lo,hi,W[u]+W[v])]
    print(n,len(res),res)
