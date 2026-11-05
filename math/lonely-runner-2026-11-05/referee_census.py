#!/usr/bin/env python3
"""Referee's independent tightness census. No hole, no lemma, no filter.
For each n, r', w1<w2<=WMAX: V = ([n-1]-{2,r'}) u {w1,w2}.
 (a) sweep ALL closed arcs {t: ||vt||<=1/n} on the FULL circle [0,1] with exact integers
     over the common denominator D = n*lcm(1..WMAX)*2; no symmetry used.
 (b) any V with no gap gets an exact LR by Fraction over all breakpoints of f (peaks, crossings).
"""
import sys, math, time, json
from math import gcd
from fractions import Fraction as Q
from itertools import combinations
from functools import reduce
from multiprocessing import Pool

def lcm(a,b): return a*b//gcd(a,b)

def arcs_int(v,n,D):
    """closed arcs of {t in [0,1]: ||v t||<=1/n} as integer endpoints over D. Split at 0/1."""
    out=[]
    for k in range(v):
        lo=(k*n-1)*D//(n*v); hi=(k*n+1)*D//(n*v)   # exact: D divisible by n*v
        assert (k*n-1)*D%(n*v)==0
        if lo<0:
            out.append((lo+D,D)); out.append((0,hi))
        elif hi>D:
            out.append((lo,D)); out.append((0,hi-D))
        else:
            out.append((lo,hi))
    return out

def has_gap(arcs,D):
    arcs=sorted(arcs); cur=0
    for a,b in arcs:
        if a>cur: return True
        if b>cur: cur=b
    return cur<D

def norm(x):
    x=x-math.floor(x); return min(x,1-x)

def exact_LR(V):
    """max_t min_v ||vt|| evaluated at all breakpoints of the piecewise linear f."""
    V=sorted(V); C={Q(0)}
    for v in V:
        for k in range(v): C.add(Q(2*k+1,2*v))
    for u,v in combinations(V,2):
        for d in (v-u,v+u):
            for k in range(d): C.add(Q(k,d))
    best=Q(0);arg=None
    for t in C:
        m=min(norm(v*t) for v in V)
        if m>best: best=m;arg=t
    return best,arg

def run_n(args):
    n,WMAX=args
    D=2*n*reduce(lcm,range(1,WMAX+1))
    W={w:sorted(arcs_int(w,n,D)) for w in range(n,WMAX+1)}
    Sarcs={v:arcs_int(v,n,D) for v in range(1,n)}
    hits=[];tested=0
    t0=time.time()
    for r in range(1,n):
        if r==2: continue
        S=[v for v in range(1,n) if v not in (2,r)]
        base=sorted(a for v in S for a in Sarcs[v])
        for w1 in range(n,WMAX+1):
            for w2 in range(w1+1,WMAX+1):
                tested+=1
                if not has_gap(base+W[w1]+W[w2],D):
                    hits.append((r,w1,w2))
    res=[]
    for r,w1,w2 in hits:
        V=sorted((set(range(1,n))-{2,r})|{w1,w2})
        lr,arg=exact_LR(V)
        res.append(dict(n=n,r=r,w1=w1,w2=w2,V=V,LR=str(lr),argmax=str(arg),tight=(lr==Q(1,n))))
    return dict(n=n,tested=tested,covering=res,secs=round(time.time()-t0,1))

if __name__=="__main__":
    WMAX=int(sys.argv[1]); ns=range(int(sys.argv[2]),int(sys.argv[3])+1); procs=int(sys.argv[4])
    with Pool(procs) as p:
        for out in p.imap_unordered(run_n,[(n,WMAX) for n in ns]):
            print(json.dumps(out),flush=True)
