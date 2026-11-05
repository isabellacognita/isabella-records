# My own check of the n=15,16 flag-bound numbers, written from Allikvere's definitions, not from Fable's scripts.
from fractions import Fraction as F
from math import log, comb
import numpy as np
def B(n,r): return F(2*r,(n+1)*(n+1-r))**2
def c(n,i): return B(n,i)-B(n,i-1)
def K(n):
    k=F(1)
    for i in range(1,n): k*=c(n,i)
    return k
def thr(n,r):
    A=float(K(n))**-0.5
    return A, n*log(A*r/n)
for n,r in [(13,101/200),(14,0.5),(15,61/125),(15,0.5),(16,2407/5000)]:
    A,t=thr(n,r); mr=min(c(n,i+1)/c(n,i) for i in range(1,n-1))
    print(f"n={n} r={r:.4f} A={A:.6e} threshold={t:.4f} min ratio={float(mr):.4f}>4/3:{mr>F(4,3)}  MSS={n*((n-1)*log(comb(n+1,2))-log(n)):.3f}")
print("published n=13: 341.0320, n=14: 414.7794; K_14 check below")
# numeric attack on the shape constant: maximise R_n directly by multi-start
def R(x):
    x=np.abs(x); x=x/x.sum(); u=x/x.max(); q=1+2*u-u*u
    F2=np.prod(q)*np.sum(x*x/q)
    return len(x)*np.exp(np.mean(np.log(x)))/np.sqrt(F2)
rng=np.random.default_rng(5)
for n,bound in [(13,101/200),(14,.5),(15,61/125),(16,2407/5000)]:
    best=0;bx=None
    for st in range(400):
        x=rng.exponential(size=n)**rng.uniform(.2,3)
        cur=R(x);step=.3
        for it in range(4000):
            y=x*np.exp(step*rng.normal(size=n))
            r=R(y)
            if r>cur: x,cur=y,r
            else: step=max(step*.999,1e-3)
        if cur>best: best,bx=cur,x/x.max()
    print(f"n={n}: numeric sup R_n ~ {best:.6f} (claimed bound {bound:.6f}) ok={best<bound}; shape sorted u: {np.round(np.sort(bx),3)[:4]}...{np.round(np.sort(bx),3)[-2:]}")
# prime sum
def primes(a,b): return [p for p in range(a,b+1) if all(p%q for q in range(2,int(p**.5)+1))]
P=primes(239,733); print("primes 239..733:",len(P),"sum log=",round(sum(map(log,P)),4),"need 483.1775")
from math import lcm
L=1
for i in range(2,17): L=lcm(L,i)
print("lcm(2..16)=",L,"log=",round(log(L),6))
