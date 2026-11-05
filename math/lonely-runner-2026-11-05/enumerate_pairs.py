# Rigorous enumeration: all W={u<v}, u,v>=n, whose windows cover the hole I=[x0,a] left near t=1/2 once speed 2 is gone.
# t=1/2-x. B_w = {x: ||w(1/2-x)|| <= 1/n}. Exact rationals throughout.
from fractions import Fraction as F
from math import floor, ceil
import sys
def hole(n):
    o = n-1 if (n-1)%2 else n-2
    return F(1,4*n), F(n-2,2*n*o), o
def norm(x):
    x=x-floor(x); return min(x,1-x)
def windows(n,w,lo,hi):
    e=F(1,n); s=F(0) if w%2==0 else F(1,2); out=[]
    k0=floor(lo*w-s-1); k1=ceil(hi*w-s+1)
    for k in range(k0,k1+1):
        a=(k+s-e)/w; b=(k+s+e)/w
        if b<lo or a>hi: continue
        out.append((max(a,lo),min(b,hi)))
    return out
def pieces(lo,hi,win):
    win=sorted(win); cur=lo; out=[]
    for a,b in win:
        if a>cur: out.append((cur,a))
        cur=max(cur,b)
    if cur<hi: out.append((cur,hi))
    return out
def inside_one(n,w,p):
    return any(a<=p[0] and p[1]<=b for a,b in windows(n,w,p[0],p[1]))
def covers_all(V):
    n=len(V)+1; e=F(1,n); pts={F(0),F(1,2)}
    for v in V:
        for k in range(0,v+1):
            for s in (F(k)-e,F(k)+e):
                t=s/v
                if 0<t<F(1,2): pts.add(t)
    pts=sorted(pts)
    return all(any(norm(v*(a+b)/2)<=e for v in V) for a,b in zip(pts,pts[1:]))
# Lemma 1 brute check: no base speed except 2 meets the open hole
def lemma1(n):
    x0,a,o=hole(n)
    for v in range(1,n):
        if v==2: continue
        for lo,hi in windows(n,v,x0,a):
            if lo<hi: return False,v
    return True,None
tot=[]
for n in range(5,41):
    x0,a,o=hole(n); ell=a-x0
    ok,bad=lemma1(n)
    Umax=floor(F(6,n)/ell)
    single=[]; cands=[]; maxv=0
    for u in range(n,Umax+1):
        P=pieces(x0,a,windows(n,u,x0,a))
        if not P: single.append(u); continue
        vmax=floor(F(2,n)/max(b-c for c,b in P))
        for v in range(u+1,vmax+1):
            maxv=max(maxv,v)
            if all(inside_one(n,v,p) for p in P): cands.append((u,v))
    tight=[]
    for (u,v) in cands:
        for r in range(1,n):
            if r==2: continue
            V=sorted(set(range(1,n))-{2,r}|{u,v})
            if covers_all(V): tight.append((tuple(V),r,u,v))
    # also two-speed candidates with u alone covering the hole (v free) reported separately
    print(f"n={n:2d} lemma1={ok} ell={float(ell):.5f} Umax={Umax} single-speed covers={single} pairs covering hole={len(cands)} {cands[:12]} tight={tight}")
