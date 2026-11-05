# The flag bound of Allikvere, Section 3, extended to n = 15 and n = 16

Fable, 2026-11-05. Source: J. Allikvere, "Fourteen and fifteen lonely runners",
arXiv 2609.02604v2 (LaTeX source read in full; Section 3 closely). Notation is his:
n = number of speeds (so LRC(n) is n+1 runners; the next rung, 16 runners, is n = 15).

Everything below was computed with exact rationals (`fractions`) and 60-digit
`decimal` arithmetic with every final figure rounded in the safe direction. Scripts:
`bound15.py` (all checks, n = 13..25) and `bound15_final.py` (certified table). Both
reproduce his published constants exactly (K_14 as a rational, A_13, A_14, 341.0320,
414.7794, 401.9846, the minimal ratios 1175/688 and 847/513, and the two prime-set
sums 353.772559 and 408.8233), which is the check that I am computing his objects.

## 1. Statement

**Theorem A (ratio hypothesis).** With B_r = (2r/((n+1)(n+1-r)))^2 and c_i = B_i - B_{i-1},
the hypothesis of his Theorem 3.8, c_{i+1}/c_i > 4/3 for 1 <= i < n-1, holds for every
13 <= n <= 25 and fails for every 26 <= n <= 30 (exact rationals). Minimal ratios:

| n | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| min c_{i+1}/c_i | 1175/688 | 847/513 | 3751/2349 | 4932/3175 | 948/625 | 29237/19723 | 2303/1584 | 497/348 | 25875/18421 | 15808/11417 | 736/539 | 17051/12645 | 47107/35325 | 3123/2368 |
| decimal | 1.7078 | 1.6511 | 1.5969 | 1.5534 | 1.5168 | 1.4824 | 1.4539 | 1.4282 | 1.4046 | 1.3846 | 1.3655 | 1.3484 | 1.33353 | 1.3188 (fails) |

For n = 15 the minimum 3751/2349 is at i = 6; for n = 16 the minimum 4932/3175 is at i = 6.
(The ratio tends to 1 as n grows, so his Lemma 3.6 cannot be used as stated beyond n = 25;
see Section 6.)

**Theorem B (shape bound).** On the positive simplex, for every 14 <= n <= 25, R_n < 1/2.
Sharper, certified upper bounds for sup R_n:

| n | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H_min > | 664.925 | 798.307 | 944.961 | 1105.000 | 1278.52 | 1465.62 | 1666.36 | 1880.82 | 2109.06 | 2351.14 | 2607.09 | 2876.98 | 3160.83 |
| sup R_n < | 0.504147 | 0.495500 | 0.487961 | 0.481326 | 0.475439 | 0.470178 | 0.465446 | 0.461165 | 0.457272 | 0.453716 | 0.450453 | 0.447449 | 0.444672 |

In particular **R_15 < 61/125 = 0.488** and **R_16 < 2407/5000 = 0.4814**; the bound
decreases in n. (His r_13 = 101/200 and r_14 = 1/2 are consistent with the first two columns:
his one-variable minima 663.48 and 796.4 are lower bounds of my 664.925 and 798.307.)

**Theorem C (the thresholds).** Assume LRC(m) for all m < n. For a primitive counterexample
v to LRC(n):

| | n = 15 (16 runners) | n = 16 (17 runners) |
|---|---|---|
| K_n = prod c_i | 233570089 / 12695029890685690413859209216000000000000 | 10135711517637019653643 / 849413517394726036287015664301622449271885791232000000000 |
| A_n = K_n^(-1/2) | 7372389141119765.13... | 289489264860166275.62... |
| log A_n | 36.536518 | 40.206895 |
| r_n (this note) | 61/125 | 2407/5000 |
| n log(A_n r_n / n), rounded up | **496.6655** | **587.2520** |
| same with r_n = 1/2 | 497.0299 | 587.8586 |
| MSS/ST bound n((n-1) log C(n+1,2) - log n) | 964.7526 | 1134.6758 |
| forced divisor lcm(2..n+1) | 720720 = 2^4 3^2 5 7 11 13 | 12252240 = 720720 * 17 |
| log lcm, rounded down | 13.488005 | 16.321219 |
| **target: sum log p must exceed** | **483.1775** (483.5419 with r = 1/2) | **570.9308** (571.5374 with r = 1/2) |
| MSS target for comparison | 951.2646 | 1118.3546 |

So for sixteen runners: log(v_1...v_15) < 496.6655 in place of 964.7526, and the corollary in
his form reads: *if P is a set of primes p >= 17 such that every primitive counterexample to
LRC(15) with pairwise distinct coordinates has p | v_1...v_15, and sum_{p in P} log p > 483.1775,
then LRC(15) holds.* (Proof identical to his Corollary 3.11: LRC(14) forces distinct coordinates;
720720 and the primes in P are pairwise coprime; Theorem 3.8 with n = 15.) The n = 15 instance
needs LRC(m) for m <= 14, all now proven; the n = 16 instance is conditional on LRC(15).

**Prime sets (Section 5).** If the primes are taken in increasing order from a starting point
p_0, as in his tables, the largest prime needed for n = 15 is

| every prime from | 17 | 89 | 131 | 199 | 239 | 251 | 293 | 347 | 401 |
|---|---|---|---|---|---|---|---|---|---|
| flag bound, largest prime | 523 | 599 | 631 | 691 | 733 | 743 | 797 | 829 | 887 |
| number of primes | 93 | 86 | 84 | 80 | 79 | 79 | 78 | 77 | 76 |
| MSS bound, largest prime | 1009 | 1063 | 1097 | 1181 | 1217 | 1223 | 1277 | 1301 | 1373 |

The analogue of his k = 14 main block (contiguous from 239) is every prime 239..733, 79 primes,
sum log = 483.716564, which exceeds both targets (483.1775 and 483.5419). If every prime from
17 upward verified, 17..523 (93 primes, sum 489.2128) would do. For n = 16 the corresponding
largest primes are 617 (from 19; corrected by the reader, see the end), 797 (from 199), 827 (from 239), against 1171..1399 with MSS.

## 2. Setup (his Section 3, restated)

v in Z_{>0}^n primitive, S = sum v_i, x_i = v_i/S, u_i = v_i/max_j v_j, q_i = 1 + 2u_i - u_i^2,
F_n(x)^2 = prod q_i * sum x_i^2/q_i, R_n(x) = n (prod x_i)^{1/n} / F_n(x). Lemma 3.2:
covol_E(Lambda) = 1/(S F_n(x)). Prop 3.4: a counterexample has t_1 + ... + t_r > B_r for every
r <= d = n-1, where t_i are the squared Gram-Schmidt lengths of any basis in the E-norm. Lemma 3.5:
a KZ basis has t_{i+1} >= (3/4) t_i. Lemma 3.6: if c_{i+1}/c_i > 4/3 then prod t_i >= prod c_i =
K_n. Theorem 3.8: S F_n(x) <= A_n = K_n^{-1/2}, and if R_n < r_n on the simplex then
v_1...v_n < (A_n r_n / n)^n. I take 3.2, 3.4, 3.5, 3.6, 3.8 as proved by him (they are stated for
general n) and verify only their hypotheses for n = 15, 16 (Theorem A) and supply the shape bound
(Theorem B), which he proved only for n = 13, 14.

## 3. Proof of Theorem A

c_i = B_i - B_{i-1} with B_r = 4r^2 / ((n+1)^2 (n+1-r)^2) are rationals; `ratio_min(n)` in
`bound15.py` computes min_i c_{i+1}/c_i exactly for n = 13..30. Output (`run3.txt`): OK for
n <= 25, FAILS for n = 26..30. As a second check of Lemma 3.6 itself, `K_vertices(n)` enumerates
all 2^{d-1} block partitions of the polyhedron {t_{i+1} >= 3/4 t_i, prefix sums >= B_r}, builds
the vertex of each (geometric blocks with ratio 3/4 whose sums are B_b - B_a), discards infeasible
ones, and takes the minimal product: it equals prod c_i for every n = 13..17, with the all-singleton
partition minimizing, and for n = 14 it equals his printed K_14 exactly.

## 4. Proof of Theorem B

Follow his Lemma 3.7. With q(u) = 1 + 2u - u^2, a(u) = q(u) u^{-2/n}, w(u) = u^2/q(u) and
H(u) = (sum_i w(u_i)) prod_i a(u_i) on the domain u in (0,1]^n with max u_i = 1, one has
R_n(x)^2 = n^2 / H(u) (scale cancels), so sup R_n < r_n iff H > n^2/r_n^2 on the domain. H tends
to infinity when any coordinate tends to 0 (a(u) -> infinity, sum w >= w(1) = 1/2), so H has a
minimizer. The four steps, each for general n.

**(i) Interior coordinates share one value.** Fix all coordinates but one, u in (0,1), and put
C = sum of the other w's, 0 < C <= (n-1)/2 (w is increasing on (0,1], w(1) = 1/2: w'(u) has the sign
of 2q - u q' = 2 + 2u > 0). With phi(u) = a(u)(C + w(u)) one checks by direct expansion

  (n/2) u^{1+2/n} phi'(u) = -beta(u),  beta(u) = C{(n-1)u^2 - (n-2)u + 1} - (n-1)u^2,

exactly as in his (3.5) (I re-expanded this by hand; the same identity for every n). beta(0) = C > 0,
beta(alpha) = -(n-1)alpha^2 < 0 at the smaller root alpha = alpha_n of (n-1)u^2 - (n-2)u + 1
(discriminant n^2 - 8n + 8 > 0 for n >= 8). If C <= 1, beta is concave with beta(0) > 0: one positive
root. If C > 1, beta is convex and beta(1) = 2C - (n-1) <= 0: its second root is >= 1. So beta has
exactly one root u_0 in (0,1), and u_0 < alpha; phi decreases on (0,u_0) and increases on (u_0,1).
Hence every interior coordinate of a minimizer equals the critical point, which satisfies, with
A = sum_i w(u_i) (the same number for every coordinate),

  g(u) := q(u){1 - (n-2)u + (n-1)u^2} / (n u^2 (1+u)) = 1/A.          (crit)

(Derivation: beta = 0 with C = A - u^2/q gives A{(n-1)u^2-(n-2)u+1} = (u^2/q)[(n-1)q + (n-1)u^2
- (n-2)u + 1] = n u^2 (1+u)/q.) With N = q * (1-(n-2)u+(n-1)u^2), D = n u^2 (1+u), expanding
N'D - ND' by hand gives

  N'D - N D' = -n u P_n(u),   P_n(u) = (n-1)u^5 + 2(n-1)u^4 - (4n-6)u^3 - (2n-8)u^2 - (n-7)u + 2,

so sign g'(u) = -sign P_n(u) for u > 0. (For n = 13 and 14 this is his -2P(u) and
-(13u^5 + 26u^4 - 50u^3 - 20u^2 - 7u + 2); `bound15.py` asserts the identity between the
machine-expanded N'D - ND' and this formula for every n = 13..25.) Now alpha_n < 1/(n-4) for
n >= 8, because the quadratic equals (7-n)/(n-4)^2 < 0 at u = 1/(n-4) while it is positive on
[0, alpha_n). For n >= 8 the coefficients of u, u^2, u^3 in P_n are negative and those of u^4, u^5
positive, so on (0, 1/(n-4)]

  P_n(u) >= 2 - (n-7)/(n-4) - (2n-8)/(n-4)^2 - (4n-6)/(n-4)^3 = [(n-3)(n-4)^2 - (4n-6)] / (n-4)^3 > 0

(n = 15: 1398/1331; n = 16: 907/864; in general (n-3)(n-4)^2 >= 80 > 26). Sturm sequences confirm
P_n has no root in (0, 1/(n-4)]. So g is strictly decreasing on (0, alpha_n), (crit) has at most one
solution there, and all interior coordinates of a minimizer share one value t in (0, alpha_n). Thus a
minimizer is (1,...,1, t,...,t) with k >= 1 ones. This step holds for **every n >= 8**.

**(ii) Two or more ones.** a'/a = q'/q - 2/(nu) vanishes exactly at the roots alpha < alpha' of
(n-1)u^2 - (n-2)u + 1, so a decreases on (0,alpha), increases on (alpha,alpha'), decreases to
a(1) = 2; hence a >= a_min := min(a(alpha), 2) on (0,1]. With k >= 2 ones, sum w >= k/2 and
prod a >= 2^k a_min^{n-k}, so H >= (k/2) 2^k a_min^{n-k}, increasing in k since 2/a_min >= 1, so
H >= 4 a_min^{n-2}. A rigorous lower bound a(alpha) >= q(alpha_lo)/alpha_hi^{2/n} with an exact
rational bracket [alpha_lo, alpha_hi] of width 2^{-60} gives a(alpha_15) >= 1.615248 and
a(alpha_16) >= 1.581809, hence H >= 2037.85 (n = 15) and H >= 2455.95 (n = 16), far above 4n^2.

**(iii) Exactly one one.** The other n-1 coordinates equal t, and

  H_1(t) = (1 + 2t + (2n-3)t^2) q(t)^{n-2} t^{-2(n-1)/n}

(n = 14: his (1+2t+25t^2) q^{12} t^{-13/7}). Expanding n t N_1' q + n(n-2) t q' N_1 - 2(n-1) N_1 q
by hand (N_1 = 1 + 2t + (2n-3)t^2) gives 2(n-1)(1-t) S_3(t) with

  S_3(t) = (2n-3)(n-1) t^3 + (2n-5) t^2 + (n-5) t - 1,

so on (0,1) sign H_1' = sign S_3 (n = 13: 276t^3+21t^2+8t-1, n = 14: 325t^3+23t^2+9t-1, his cubics;
the machine expansion is asserted equal to this formula for n = 13..25). For n >= 5 all
coefficients but the constant are positive: S_3 is increasing with exactly one positive root t_0
(Descartes; Sturm confirms one root in (0,1)). H_1 decreases on (0,t_0), increases on (t_0,1), and
its minimum over (0,1) is a lower bound for the k = 1 configurations. Bisection with exact signs
gives t_0 in [lo, hi] of width 2^{-40}; since N_1 and q increase and t^{-2(n-1)/n} decreases,
H_1 >= N_1(lo) q(lo)^{n-2} hi^{-2(n-1)/n} on [lo,hi]:

  n = 15: t_0 in [0.072476827919, 0.072476827920], S_3(lo) < 0 < S_3(hi),  H_1 >= 944.961244;
  n = 16: t_0 in [0.067533909484, 0.067533909485], S_3(lo) < 0 < S_3(hi),  H_1 >= 1105.000141.

**(iv) Conclusion.** H > min(944.961244, 2037.85) = 944.961244 > 900 = 4 * 15^2 for n = 15, so
sup R_15 <= 15/sqrt(944.961244) < 0.48796005 < 61/125; and H > 1105.000141 > 1024 for n = 16, so
sup R_16 <= 16/sqrt(1105.000141) < 0.48132544 < 2407/5000. The same four steps run for every
n = 13..25 (`run3.txt`): H_min > 4n^2 for all 14 <= n <= 25, which is Theorem B. (At n = 13 the
bound is 664.925 < 676, so R_13 < 1/2 is false there, consistent with his r_13 = 101/200.)

The decimal `ln`, `exp`, `sqrt` are correctly rounded at 60 digits (Python `decimal`), so the
rounding error in every figure above is below 1e-55; the displayed figures are additionally
rounded in the safe direction at 6 (H, a) or 4 (thresholds) decimals.

## 5. Proof of Theorem C and the prime sets

K_n = prod c_i exactly (Section 3 verifies Lemma 3.6's hypothesis), log A_n = -(1/2) log K_n,
and n log(A_n r_n/n) = n log r_n - n log n - (n/2) log K_n; all logs of rationals at 60 digits,
rounded up. The MSS/ST column is n((n-1) log C(n+1,2) - log n) (his Remark 3.9 form; n = 14 gives
810.0740, his number). lcm(2..n+1) by direct computation; log rounded down; target = bound - log lcm,
rounded up. Prime sets: natural logs of primes summed at 60 digits, rounded down at 1e-6, taken in
increasing order from p_0 until the sum exceeds the target. His selection, read off his Sections 5
and 6, is exactly this: verified primes in increasing order (a contiguous main block, plus whichever
smaller primes verified), stopped when the logarithmic sum passes the target; so the largest prime
for n = 15 lies between 523 (if every prime from 17 verifies) and 733 (his k = 14 style, from 239).

## 6. What was verified by computation, and how to reproduce

    cd the_lab/lonely-runner-2026-11-05/fable-composite
    python3 -I bound15.py              > run3.txt     # ~6 s: ratios n=13..30, K_n two ways n=13..17,
                                                      # shape analysis n=13..25, thresholds, prime sets
    PYTHONPATH=. python3 bound15_final.py > final.txt # certified table for n=13,14,15,16, explicit sets

Checks inside the scripts (each an `assert` or printed verdict): the two polynomial identities
(P_n and S_3) against machine expansion for n = 13..25; alpha_n < 1/(n-4); P_n's lower bound and
Sturm root count on (0,1/(n-4)]; Descartes/Sturm for S_3; exact signs at the bracket ends; K_14
equal to his rational; vertex enumeration equal to prod c_i for n = 13..17; his constants and
prime sums reproduced.

## 7. What remains open, and the weakest step

- I did not re-prove Prop 3.4, Lemma 3.5, Lemma 3.6 or Theorem 3.8; I checked their hypotheses
  for n = 15, 16 and reproduced their constants for n = 13, 14. If any of those has a gap, it is a
  gap for 15 runners too. His Prop 3.4 uses Lemma 3.3 (Giri-Kravitz) and the nearest-plane rounding;
  I read them and found nothing wrong, but that reading is not a verification.
- Theorem B is proved for 13 <= n <= 25 by running the general-n argument at each n, not for all n.
  Step (i) is general (n >= 8); steps (ii) and (iii) are numeric at each n. A uniform proof for all
  n >= 14 would need lower bounds for a(alpha_n)^{n-2}/n^2 and min H_1 / n^2; the data (ratio
  4.07, 4.20, 4.32, ..., 5.06 at n = 14..25, tending to e^2) suggest both are routine but I did
  not write them.
- For n >= 26 the ratio hypothesis fails; prod c_i is then only an upper bound for min prod t_i
  (t = c is still feasible since c_{i+1}/c_i > 3/4), so a flag bound there needs the true minimum
  over the polyhedron, which my block enumeration does not certify (degenerate vertices with two
  active prefixes in one block would be missed). Not needed for 16 or 17 runners.
- The weakest step of this note is (iii)'s reduction: that the global minimizer of H has the form
  (1^k, t^{n-k}) rests on his interior-coordinate argument, which I re-derived (the identity for
  phi', the two-case analysis of beta, the monotonicity of g via P_n). The numerical content
  (brackets, 60-digit logs) is not where the risk is.


## Corrections from the reader (a separate Claude, 2026-11-05, 08:3x), checked by Isabella

- n = 16 only: "613 from 17" was wrong. lcm(2..17) already contains 17, so log 17 counts twice. 19..613 sums to 569.0634 < 570.9308; the largest prime is 617. The MSS comparison figure 1171 has the same double count.
- "all now proven": LRC(13) and LRC(14) rest on Allikvere's preprint, whose computation hasn't been independently reimplemented.
- 733 isn't an upper bound on anything. No prime has been verified at k = 15.
- Lemma 3.7 is the only n-specific step in his Section 3 (his a > 8/5 fails at n = 16), and Section 4 here replaces it. Theorem 3.8 is general, so the reduction is his. This note adds the shape bound and the arithmetic for n = 15 and up, not a new method.
- The reader's independent lower bound, using none of Section 4: H >= 944.949, so R_15 <= 0.487963 (double precision). Margin to 61/125 is about 4e-5.
