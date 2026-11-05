#!/usr/bin/env python3
# Final certified numbers for n = 15, 16 (and the comparison rows 13, 14).  Uses bound15.py.
# Run from this directory:  PYTHONPATH=. python3 bound15_final.py
from bound15 import *
from decimal import ROUND_CEILING, ROUND_FLOOR

def report(n, rlist):
    o = shape_analysis(n)
    K = K_product(n); logK = dln(K); logA = -logK / 2
    L = lcm_upto(n + 1); logL = dln(L)
    print(f"===== n = {n} =====")
    print(f"min c_(i+1)/c_i = {ratio_min(n)[0]} = {float(ratio_min(n)[0]):.6f}  (> 4/3: {ratio_min(n)[0] > Fr(4,3)})")
    print(f"K_{n} = {K}")
    print(f"log K_{n} = {logK:.30f}")
    print(f"A_{n} = K^(-1/2) = {logA.exp():.6f}")
    print(f"alpha_{n} in [{o['alpha'][0].numerator}/{o['alpha'][0].denominator} ...] ~ {float(o['alpha'][0]):.10f} < 1/(n-4) = {1/(n-4):.10f}")
    print(f"P_{n}(u) >= {o['Pn_lower_bound_on_(0,1/(n-4)]']} = {float(o['Pn_lower_bound_on_(0,1/(n-4)]']):.6f} > 0 on (0,1/(n-4)]")
    print(f"a(alpha_{n}) >= {down(o['a_alpha_lower'],6)};  two-or-more-ones case: H >= 4 a_min^(n-2) >= {down(o['H_two_ones_lower'],3)}")
    lo, hi = o['t0_bracket']
    print(f"S_3 = (2n-3)(n-1)t^3+(2n-5)t^2+(n-5)t-1 = {pstr(o['S3'])};  unique root t0 in [{float(lo):.12f}, {float(hi):.12f}]")
    print(f"   S_3({float(lo):.12f}) = {float(peval(o['S3'],lo)):.3e} < 0,  S_3({float(hi):.12f}) = {float(peval(o['S3'],hi)):.3e} > 0")
    print(f"one-one case: H_1 >= N1(lo) q(lo)^(n-2) hi^(-2(n-1)/n) = {down(o['H1_min_lower'],6)}   (H_1 at midpoint {o['H1_at_mid']:.6f})")
    Hl = down(o['H_lower'], 6)
    Rup = up(D(n) / Hl.sqrt(), 8)
    print(f"=> H > {Hl}  =>  sup R_{n} <= n/sqrt(H) < {Rup}   (R_n < 1/2 iff H > {4*n*n})")
    print(f"MSS/ST: log(v1..vn) < {up(mss_log(n),6)}   [= n((n-1) log C(n+1,2) - log n)]")
    print(f"lcm(2..{n+1}) = {L},  log = {down(logL,6)} (rounded down)")
    rows = []
    for r in rlist:
        assert fd(r) > Rup, "r must exceed the certified sup"
        T = n * (dln(r) + logA - dln(n))
        Tup = up(T, 4); target = up(T - down(logL, 6), 4)
        print(f"r_{n} = {r} = {float(r):.6f}:  n log(A_n r_n / n) = {T:.10f}  -> {Tup};  target sum log p > {target}")
        rows.append((r, Tup, target))
    return rows

if __name__ == "__main__":
    report(13, [Fr(101, 200)])
    report(14, [Fr(1, 2)])
    rows15 = report(15, [Fr(1, 2), Fr(61, 125)])
    rows16 = report(16, [Fr(1, 2), Fr(2407, 5000)])
    print()
    print("===== prime sets for n = 15 (16 runners) and n = 16 (17 runners) =====")
    P = primes_upto(4000); logs = {p: dln(p) for p in P}
    def need(target, p0):
        s = D(0); used = []
        for p in P:
            if p < p0: continue
            s += logs[p]; used.append(p)
            if down(s, 6) > target: return used, s
    for n, rows in [(15, rows15), (16, rows16)]:
        L = lcm_upto(n + 1)
        targ_mss = up(mss_log(n) - down(dln(L), 6), 4)
        for r, Tup, target in rows:
            print(f"--- n={n}, r_{n}={r}: target {target}   (MSS target {targ_mss})")
            for p0 in [17, 89, 131, 199, 239, 251, 293, 347, 401, 503]:
                used, s = need(target, p0)
                usedm, sm = need(targ_mss, p0)
                print(f"   every prime from {p0:4d}: flag -> largest {used[-1]:4d}, {len(used):3d} primes, sum {down(s,4)} ;  MSS -> largest {usedm[-1]:4d}, {len(usedm):3d} primes")
    # the explicit set in the style of his k=14 main block (contiguous from 239), for n=15 with r=61/125
    r, Tup, target = rows15[1]
    used, s = need(target, 239)
    print()
    print(f"Explicit n=15 set, contiguous from 239 (r_15=61/125, target {target}): {len(used)} primes, sum log = {down(s,6)}")
    print("  ", used)
    used, s = need(target, 17)
    print(f"Explicit n=15 set, every prime from 17 (target {target}): {len(used)} primes, sum log = {down(s,6)}")
    print("  ", used)
