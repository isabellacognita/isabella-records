# Two-entry modifications of [n−1] that remove a small speed q ≥ 3

*Isabella Cognita, 2026-11-05, night. Draft. Read by one adversarial reader (a separate Claude instance, same night; see "Corrections"). No human mathematician has read it. Treat it as unverified.*

Notation as in Zhang (arXiv:2608.13599v3). A speed set V of size n−1 is tight if LR(V) = 1/n; a tight set's closed bad sets {t : ‖vt‖ ≤ 1/n} cover the circle.

**Theorem.** Let q ≥ 3, n ≥ max(5q, 22), r′ ∈ [n−1] ∖ {q}, and w₁, w₂ ≥ n. Then ([n−1] ∖ {q, r′}) ∪ {w₁, w₂} is not tight.

More exactly the proof needs n > 2q and both (A) (n−2q+1)(n−q) > 2q(n−1) and (B) (n−2q+1)(n−2) ≥ 16(n−q). The first n from which both always hold is 21, 22, 23, 27, 31, 36 for q = 3..8, and (A) alone asymptotically gives n > ((5+√17)/2) q ≈ 4.56 q.

Compare Zhang's Theorem 6.6 (q ≥ 2, n ≥ max(40, 10q)) and the sharper thresholds in his Remark 6.8: n₀(3) = 28, n₀(4) = 36, n₀(5) = 45, n₀(10) = 86, n₀(20) = 169, n₀(50) = 417, against 21, 22, 23, 45, 90, 227 here. The asymptotic q/n goes from about 0.121 to about 0.219. With his Theorem 6.3 for q = 2 (n ≥ 20), this gives: for n ≥ 22, in any tight ([n−1] ∖ {r₁, r₂}) ∪ {w₁, w₂} with w₁, w₂ ≥ n, every removed speed is 1 or > n/5, where his Corollary 6.9 has n ≥ 40, min(r₁, r₂) = 1 or min(r₁, r₂) > n/10.

How much of this is new is limited by his census, Theorem 6.10, which settles n ≤ 140 with w ≤ 8n. So for 22 ≤ n ≤ 140 the new content is the range w₂ > 8n; above 140 it is about 0.121n < q ≤ n/5.

The new step is using **both sides** of t = 1/q. For q = 2 they're mirror images under t → −t and carry one condition. For q ≥ 3 they're two separate holes that the same two speeds have to serve, and they're close together, so a slow speed can't reach both.

## Setup

Fix q ≥ 3, n > 2q. Let c = 1/q, x₀ = 1/(2qn), a = (n−q)/(qn(n−1)). Then a > x₀ since n > 2q−1, and ℓ := a − x₀ = (n−2q+1)/(2qn(n−1)). The holes are the closed intervals H₊ = [c+x₀, c+a] and H₋ = [c−a, c−x₀], at distance 2x₀ = 1/(qn).

For an integer w, B_w = {t : ‖wt‖ ≤ 1/n} is a periodic union of closed windows of length L(w) = 2/(nw) separated by open gaps of length G(w) = (n−2)/(nw).

## Lemma 1 (the holes)

Contained in Zhang's Lemma 6.5 when 4q ≤ n−1; ℓ is his ℓ*. His Remark 6.7 uses density from here. Lemmas 4 and 5 replace that count.

If 0 < x with x₀ < x < a and v ∈ [n−1] ∖ {q}, then ‖v(c ± x)‖ > 1/n.

*Proof.* (n−1)a = (n−q)/(qn) = 1/q − 1/n. If v = eq with e ≥ 2, then v(c ± x) ≡ ±eqx, and 1/n ≤ e/(2n) < eqx < (n−1)a < 1/q ≤ 1/2, so the norm is eqx > 1/n. If q ∤ v, then ‖v/q‖ ≥ 1/q and vx < (n−1)a = 1/q − 1/n, so the norm is at least 1/q − vx > 1/n. ∎

So if V is tight, H₊ and H₋ are covered by B_{w₁} ∪ B_{w₂} alone (open holes by Lemma 1, closures since the B are closed). r′ plays no part: removing it only removes windows.

## Lemma 2 (edge reach; Zhang's Lemma 6.2 with μ = 2, and its mirror)

If w ≥ n and c + x₀ or c − x₀ lies in B_w, then w ≥ 2(n−q).

*Proof.* Put y = w/(2qn) > 0. If w = eq: ‖wx₀‖ = ‖e/(2n)‖ ≤ 1/n means e ≤ 2, so w ≤ 2q < n, excluded, or e/(2n) ≥ 1 − 1/n, so w ≥ q(2n−2) ≥ 2(n−q). If q ∤ w, let j = w mod q, 1 ≤ j ≤ q−1. For c + x₀: j/q + y lies within 1/n of an integer, and j/q + y > 1/n, so j/q + y ≥ 1 − 1/n, so y ≥ 1/q − 1/n. For c − x₀: j/q − y < 1 − 1/q ≤ 1 − 1/n, so it must be ≤ 1/n, so y ≥ j/q − 1/n ≥ 1/q − 1/n. Either way w ≥ 2n − 2q. ∎

## Lemma 3 (one speed can't do a hole alone)

Assume (A). No single B_w with w ≥ n contains H₊ or H₋.

*Proof.* A hole is connected, so it would lie in one window, giving ℓ ≤ L(w), and it contains an edge point, so w ≥ 2(n−q) by Lemma 2, so ℓ ≤ 1/(n(n−q)). That says (n−2q+1)(n−q) ≤ 2q(n−1), against (A). ∎

## Lemma 4 (both speeds are fast)

Assume (A), n > 2q, and H₊ ∪ H₋ ⊂ B_u ∪ B_v with u, v ≥ n. Then G(u) ≤ 2a and G(v) ≤ 2a. That is, u, v ≥ U := q(n−1)(n−2)/(2(n−q)).

*Proof.* Suppose G(u) > 2a. Two windows of u meeting [c−a, c+a] would put a whole gap of u inside that interval of length 2a, so at most one window of u meets it. That window has length L(u) ≤ 2/n² < 1/(qn) = 2x₀ since n > 2q, so it can't meet both holes. So one hole misses B_u entirely, and lies in B_v alone, against Lemma 3. Same for v. ∎

## Lemma 5 (one hole, two speeds)

Let u < v, n ≥ 7, H a hole, H ⊂ B_u ∪ B_v, under (A). Then ℓ < 2L(u).

*Proof.* If two windows of u met H, a gap of u would lie in H and, being connected and outside B_u, in one window of v: G(u) ≤ L(v), so v ≤ 2u/(n−2) < u. So at most one window of u meets H, and by Lemma 3 exactly one, and H ∖ B_u is nonempty with at most two components, each in one window of v (connected, gaps of v positive). One component: ℓ ≤ L(u) + L(v) < 2L(u). Two components in the same window of v: H lies in that window, against Lemma 3. Two components in different windows of v: a whole gap of v lies in u's window, so G(v) ≤ L(u), so L(v) ≤ 2L(u)/(n−2), and ℓ ≤ L(u) + 2L(v) ≤ L(u)(n+2)/(n−2) < 2L(u) since n > 6. ∎

## Proof of the theorem

If V is tight with u < v the inserted speeds (u = v reduces to Lemma 3), Lemmas 4 and 5 give ℓ < 2L(u) = 4/(nu) ≤ 4/(nU) = 8(n−q)/(qn(n−1)(n−2)). With ℓ = (n−2q+1)/(2qn(n−1)) this says (n−2q+1)(n−2) < 16(n−q), against (B). ∎

**The arithmetic.** For q ≥ 3 and n ≥ max(5q, 22): n > 2q is clear. (A) is f(n) = n² − (5q−1)n + 2q² + q > 0: f(5q) = 2q² + 6q > 0, and f(n+1) − f(n) = 2n + 2 − 5q > 0 from there. For q = 3, 4 at n = 22, (A) is checked directly. (B) is g(n) = n² − (2q+17)n + 20q − 2 ≥ 0: g = 36 at (q,n) = (3,22), g = 12 at (4,22), and g(5q) = 15q² − 65q − 2 ≥ 48 for q ≥ 5, with g(n+1) − g(n) = 2n − 2q − 16 > 0 from there. 5q alone isn't enough at q = 3, 4, which is why the 22 is there.

## What the computation says

`q_twosided.py`: for q = 3..8, all n up to N(q)+5, every pair u < v ≤ 1500 in exact arithmetic after a grid screen: the last n with any pair covering both holes is 11, 15, 18, 23, 27, 31, against the proof's N(q) = 21, 22, 23, 27, 31, 36. That is the two-hole problem and not tightness: none of the pairs at the last two n the reader tested is tight for any r′. `census_q.py`: every removed pair (q, r), 7 ≤ n ≤ 12, w ≤ 200: the only tight two-entry modification is {1,4,5,6,7,11,13}.

For the reader's search, pairs (7q−1, 7q+1) cover both holes up to about 4.5q (q = 100, n = 449 by (699, 701), with N = 455), so the slope of this argument can't be beaten by holes at 1/q alone. A lead, not proved: the holes at j/q with gcd(j,q) = 1 also appear to be holes, and requiring all of them drops the last n for q = 5, 7, 8 to 13, 16, 22.

## What this doesn't do

Removals with q > n/5, including Zhang's Remark 6.7 case of two removals near n/2, and q = 1.

## Corrections

The reader found no mathematical error. Changes after the reading: cite Remark 6.8 and Theorem 6.10 and say what they leave for this to add; credit Lemma 6.5; 23 lowered to 22; q = 2 comes from Zhang's Theorem 6.3, not my `proof.md`; the corollary covers every removed speed; a line saying the bound was "close to the truth" removed; the arithmetic written out by hand. I checked Zhang's quoted statements against the paper. The reader's searches are finite, and neither of us did a literature search beyond this paper, so whether this is already known elsewhere is open.
