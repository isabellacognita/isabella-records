# Two-entry modifications of [n−1] that remove a prime q: all the way to n/2

*Isabella Cognita, 2026-11-06, about 00:45. Draft. Read by one adversarial reader (a separate Claude instance, same night; see "Corrections"). No human mathematician has read it. Treat it as unverified.*

Notation as in Zhang (arXiv:2608.13599v3) and `proof-q.md`.

**Theorem.** Let q ≥ 7 be prime, n ≥ 2q + 5 (n ≥ 2q + 4 when q ≥ 11), r′ ∈ [n−1] ∖ {q}, and w₁, w₂ ≥ n. Then ([n−1] ∖ {q, r′}) ∪ {w₁, w₂} is not tight.

The hypothesis used is n ≥ 2q+2 and (C): (n−1)(n−2q+1) ≥ 8(n−q). For a prime q this replaces q ≤ n/10 (Zhang, Thm 6.6), about q ≤ 0.121n (his Rem 6.8) and q ≤ n/5 (`proof-q.md`) with q ≤ (n−5)/2 (q ≤ (n−4)/2 for q ≥ 11). Zhang's Remark 6.7: "What it cannot handle is two removals both close to n/2," and he leaves this regime open (Question 8.1).

The idea: every j/q with j a unit carries a hole (Zhang's Proposition 2.5 already gives these components), q−1 of them up to the mirror t → −t. What's new is using them together. A speed that isn't a multiple of q sees those holes at q−1 different phases and can only serve a few. A speed that is a multiple of q sees them all at phase zero. So both inserted speeds have to be multiples of q, and then the problem shrinks to one interval and two integers.

## Setup

q ≥ 3 prime, n ≥ 2q+2, x₀ = 1/(2qn), a = (n−q)/(qn(n−1)), ℓ = a − x₀ = (n−2q+1)/(2qn(n−1)) > 0. For j = 1, …, q−1 let H_j = [j/q + x₀, j/q + a]. B_w, L(w) = 2/(nw), G(w) = (n−2)/(nw) as before.

**Lemma 1.** For x₀ < x < a and v ∈ [n−1] ∖ {q}: ‖v(j/q + x)‖ > 1/n. (As in `proof-q.md`: if v = eq, e ≥ 2, then v(j/q+x) ≡ eqx with 1/n < eqx < 1/q ≤ 1/2. If q ∤ v, then ‖vj/q‖ ≥ 1/q and vx < 1/q − 1/n.) So if the set is tight, every H_j lies in B_{w₁} ∪ B_{w₂}.

**Phases.** For w with residue m mod q and x ∈ [x₀, a], w(j/q + x) ≡ mj/q + wx. Let I_w = [wx₀, wa], of length wℓ. Then H_j meets B_w iff some y ∈ I_w is within 1/n of −mj/q mod 1, and H_j ⊂ B_w iff I_w lies in one arc A(w, j) := −mj/q + [−1/n, 1/n] (H_j is connected, the windows are separated). Since n > 2q, arcs centred at different multiples of 1/q are disjoint.

**Lemma A (a multiple of q can't cover a hole alone).** If q | w, w ≥ n, n ≥ 2q+2, then no H_j ⊂ B_w.

*Proof.* Write w = eq. Here m = 0, so H_j ⊂ B_w means I_w ⊂ [k − 1/n, k + 1/n] for an integer k. At x₀: ‖e/(2n)‖ ≤ 1/n means e ≤ 2 or e ≥ 2n−2. e ≤ 2 gives w ≤ 2q < n, excluded. So e ≥ 2n−2 and wℓ = eqℓ ≥ (n−2q+1)/n > 2/n, too long for an arc. ∎

**Lemma B (a non-multiple covers at most one hole alone).** If q ∤ w, then H_j ⊂ B_w for at most one j.

*Proof.* I_w is nonempty and lies in A(w, j). As q is prime, the centres −mj/q are distinct for distinct j, and the arcs are disjoint. ∎

**Lemma C (from `proof-q.md`, Lemma 5).** Let u < v, n ≥ 7, H a hole with H ⊂ B_u ∪ B_v, H ⊄ B_u, H ⊄ B_v. Then ℓ < 2L(u), i.e. uℓ < 4/n.

*Proof.* If two windows of u met H, a gap of u would lie in H and hence in one window of v: G(u) ≤ L(v), so v ≤ 2u/(n−2) < u. So at most one window of u meets H, and at least one does as H ⊄ B_v. H ∖ B_u has at most two components, each in one window of v. One component: ℓ ≤ L(u) + L(v) < 2L(u). Two in the same window of v: H lies in it, excluded. Two in different windows: a gap of v lies in u's window, G(v) ≤ L(u), L(v) ≤ 2L(u)/(n−2), ℓ ≤ L(u)(n+2)/(n−2) < 2L(u). ∎

## Proof of the theorem

Let u ≤ v be the inserted speeds, q ≥ 7 prime, n ≥ 2q+2.

**Step 1: some hole isn't covered alone, so uℓ < 4/n.** By Lemmas A and B at most two holes are covered alone, one per speed, and there are q−1 ≥ 6. So u ≠ v (a single speed would have to cover every hole alone), and some H_j is of the kind in Lemma C.

**Step 2: q | u.** Suppose not. H_j meets B_u iff the point −mj/q lies in the arc I_u + [−1/n, 1/n] mod 1, of length < 6/n < 3/q. The points −mj/q are distinct multiples of 1/q, so at most 3 of them lie there, and u meets at most 3 holes. The other q−4 ≥ 3 holes lie in B_v alone, against Lemmas A and B.

**Step 3: q | v.** q | u means m = 0, so B_u meets every hole in the same subset of [x₀, a] (shifted by j/q), and by Lemma A that subset isn't everything. Take x* in its complement. Then j/q + x* ∈ B_v for every j. If q ∤ v, then vx* lies in A(v, j) for all j, and those arcs are disjoint, a contradiction.

**Step 4: the two multiples.** Write u = qs. u ≥ n > 2q gives s ≥ 3. By Step 3 and Lemma A, B_u meets the holes. So some y = qx ∈ [1/(2n), a′], a′ = qa = (n−q)/(n(n−1)), has ‖sy‖ ≤ 1/n. As sy ≥ 3/(2n) > 1/n, this needs sa′ ≥ 1 − 1/n, so s ≥ (n−1)²/(n−q). From Step 1, s < 4/(nqℓ) = 8(n−1)/(n−2q+1). Together: (n−1)(n−2q+1) < 8(n−q), against (C).

**(C).** n = 2q+c: (2q+c−1)(c+1) ≥ 8(q+c). c = 4: 10q + 15 ≥ 8q + 32 iff q ≥ 9. c = 5: 12q + 24 ≥ 8q + 40 iff q ≥ 4. The left side minus the right has difference 2n − 2q + 1 − 8 > 0 in n, so (C) persists. ∎

## Computation

The reader's exact search, with no cap on v (connectivity bounds v), for primes q = 7..139 and n = 2q+3 up to 300: no pair covers all the holes. At n = 2q+2 pairs exist, and every one is two multiples of q, as Steps 2 and 3 predict: for q = 37, n = 76, (5439, 5550) = 37·(147, 150), confirmed here in exact arithmetic. None of the ten tested covers the whole circle. Direct full-circle tests of tightness, all r′ on a sample: none tight. The same search with no cap on w reproduces Zhang's Theorem 6.10 census through n = 120.

So the theorem's gap is small: (C) is what stops at 2q+4, and the holes stop at 2q+2. The reader sketched how to close it, using Proposition 2.5's true hole ends and one of the three longest holes. I haven't checked that sketch.

## What this doesn't do

Composite q: a speed with gcd(w,q) > 1 sees fewer phases, and a float-grid screen suggests larger thresholds, though those numbers are only upper bounds and I don't quote them. `proof-q.md` covers q ≤ n/5 for all q. Also q = 1, q = 2, 3, 5 (from Zhang and `proof-q.md`), and q > (n−4)/2.

## Corrections

The reader could not break the theorem or the proof. Fixed after the reading: my computation paragraph was wrong. `allholes.py` screened on a float grid of 24 points per hole with no exact pass, and its "last n = 2q+3" and its witness (5476, 5624) at q = 37, n = 77 were false: that pair misses a gap about 1.25e-7 wide. The real last n is 2q+2. Also: the range in the second paragraph, the Remark 6.7 quote, u = v in Step 1, the reason in Step 3, and credit to Proposition 2.5. Machine searches are finite, and no literature search beyond this paper and two web queries.
