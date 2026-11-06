# q>=3: t=1/q+x and t=1/q-x each leave a hole (x0,a), x0=1/(2qn), a=(n-q)/(qn(n-1)). Do two speeds >=n cover BOTH closed holes? Exact confirm.
import numpy as np,sys
from fractions import Fraction as F
from math import floor,ceil
def windows_cover(lo,hi,ws,n):
    e=F(1,n);arcs=[]
    for w in ws:
        for k in range(floor(lo*w)-1,ceil(hi*w)+2):
            a=(k-e)/w;b=(k+e)/w
            if b<lo or a>hi: continue
            arcs.append((a,b))
    arcs.sort();cur=lo
    for a,b in arcs:
        if a>cur: return False
        cur=max(cur,b)
    return cur>=hi
def bound_N(q):
    # proof's threshold: smallest N>2q such that both inequalities hold for all n>=N
    ok=lambda n:(n-2*q+1)*(n-q)>2*q*(n-1) and (n-2*q+1)*(n-2)>=16*(n-q)
    last=2*q
    for n in range(2*q+1,60*q+200):
        if not ok(n): last=n
    return last+1
WMAX=int(sys.argv[1])
for q in range(3,int(sys.argv[2])+1):
    N=bound_N(q); out=[]
    for n in range(max(2*q+1,7),N+6):
        x0=F(1,2*q*n);a=F(n-q,q*n*(n-1));c=F(1,q)
        if a<=x0: continue
        H=[(c+x0,c+a),(c-a,c-x0)]
        pts=np.concatenate([np.linspace(float(l),float(h),max(30,int(float(h-l)*60000))) for l,h in H])
        ws=np.arange(n,WMAX+1)
        M=np.abs(((ws[:,None]*pts[None,:]+0.5)%1)-0.5)<=1/n+1e-11
        Nn=(~M).astype(np.int32)
        cnt=Nn@Nn.T
        pairs=[]
        for i,j in zip(*np.where(np.triu(cnt==0,1))):
            w=(int(ws[i]),int(ws[j]))
            if all(windows_cover(l,h,w,n) for l,h in H): pairs.append(w)
        out.append((n,len(pairs),pairs[:3]))
    print('q',q,'proof N',N,'10q/40',max(40,10*q),'last n with a covering pair:',max([o[0] for o in out if o[1]],default=None),[o for o in out if o[1]][-2:],flush=True)
