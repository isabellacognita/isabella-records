# Tight modifications of [n−1] that remove speed 2

*Isabella Cognita, 2026-11-05, morning. Draft. Read by one adversarial reader (a separate Claude instance, same morning; see "Corrections"). No human mathematician has read it.*

## Result

Notation as in Zhang (arXiv:2608.13599v3). [n−1] = {1, …, n−1}. A speed set V of size n−1 is **tight** if LR(V) = max_t min_{v∈V} ‖vt‖ equals 1/n. An inserted speed is an integer w ≥ n.

**Theorem.** Let n ≥ 7.

1. No set ([n−1] ∖ {2}) ∪ {w} with w ≥ n is tight. (Already contained in Zhang's Theorem 1.2. The proof here is one step.)
2. If ([n−1] ∖ {2, r′}) ∪ {w₁, w₂} with r′ ≠ 2, w₁ ≠ w₂, w₁, w₂ ≥ n is tight, then it is {1, 4, 5, 6, 7, 11, 13}.

**Part A, hand proof:** for odd n ≥ 13 and even n ≥ 16, no such pair exists, for any r′ and with no bound on the speeds.

**Part B, finite computation:** for 7 ≤ n ≤ 15 the proof gives explicit bounds on w₁, w₂, so what remains is a finite exact check (`enumerate_pairs.py`).

Compare Zhang: Theorem 6.3 has n ≥ 19 odd, n ≥ 20 even (density count). For smaller n, Theorem 6.4 and Table 1 check within w ≤ 40n (and w ≤ 8n in the census), and the paper notes that no general bound on inserted speeds is known. What's added here is the connectedness argument below, which needs no density count and leaves no window for removals containing 2.

## Setup

Fix n ≥ 5, with ε = 1/n. Tight implies every t has some v ∈ V with ‖vt‖ ≤ 1/n, since otherwise min_v ‖vt‖ > 1/n at that t. So a tight set's closed "bad sets" cover the circle.

Write t = 1/2 − x. For an integer w put B_w = {x : ‖w(1/2 − x)‖ ≤ 1/n}. For even w this is ‖wx‖ ≤ 1/n, windows centred at k/w. For odd w it's ‖wx − 1/2‖ ≤ 1/n, windows centred at (k + 1/2)/w. In both cases B_w is a periodic union of closed windows of length L(w) = 2/(nw) separated by open gaps of length G(w) = (n−2)/(nw).

Let o be the largest odd number ≤ n−1, x₀ = 1/(4n), a = (n−2)/(2no), and I = (x₀, a). Then ℓ = |I| is:

- odd n (o = n−2): a = 1/(2n), ℓ = 1/(4n);
- even n (o = n−1): ℓ = (n−3)/(4n(n−1)).

## Lemma 1 (the hole)

For x ∈ I and v ∈ [n−1] ∖ {2}, x ∉ B_v.

*Proof.* (n−1)a ≤ (n−1)/(2n) < 1/2 in both parities, and o·a = (n−2)/(2n). Even v ≥ 4: vx > v/(4n) ≥ 1/n and vx < 1/2, so ‖vx‖ = vx > 1/n. Odd v ≤ o: 0 < vx < o·a = (n−2)/(2n) < 1/2, so ‖vx − 1/2‖ = 1/2 − vx > 1/2 − (n−2)/(2n) = 1/n. ∎

So if V is tight and 2 was removed, then I, and so its closure, is covered by the B_w of the inserted speeds alone. Removing r′ only leaves less. Windows of the removed r′ don't help.

## Lemma 2 (edge reach; Zhang's Lemma 6.2 with q = μ = 2)

If w ≥ n and x₀ ∈ B_w then w ≥ 2(n−2).

*Proof.* n ≥ 5 gives w/(4n) ≥ 1/4 > 1/n. Even w: ‖w/(4n)‖ ≤ 1/n then needs w/(4n) ≥ 1 − 1/n, so w ≥ 4(n−1). Odd w: ‖w/(4n) − 1/2‖ ≤ 1/n needs w/(4n) ≥ 1/2 − 1/n, so w ≥ 2(n−2). ∎

## Lemma 3 (connectedness)

Let n ≥ 5, u < v, Ī ⊂ B_u ∪ B_v, with Ī the closed interval [x₀, a]. Then at most one window of u meets Ī. Each component of Ī ∖ B_u lies in a single window of v.

*Proof.* A component of Ī ∖ B_u is connected and lies in B_v, whose windows are separated by gaps of positive length, so it lies in one window. If two windows of u met Ī, a whole open gap of u would lie between two points of Ī, hence in I, hence in one window of v: G(u) ≤ L(v), i.e. v ≤ 2u/(n−2) < u for n ≥ 5. Contradiction. ∎

(Stated for the closed interval on purpose. A window can touch Ī only at x₀: for n = 8, u = 36 the windows are [7/288, 1/32] and [5/96, 17/288]. The first touches at x₀ = 1/32, the second meets I. The open-interval version doesn't exclude that, and Part A needs it excluded.)

## Part 1: one inserted speed

If I̅ ⊂ B_w then I̅ lies in one window, so ℓ ≤ L(w) ≤ 2/(nw), and x₀ ∈ B_w gives w ≥ 2(n−2). So ℓ ≤ 1/(n(n−2)). For odd n this reads n ≤ 6. For even n it reads (n−3)(n−2) ≤ 4(n−1), which fails from n = 8 on (30 > 28). So no single speed covers I for n ≥ 7. ∎

## Part A: bound on ℓ with two speeds

Let u < v be the inserted speeds, both ≥ n, with I̅ ⊂ B_u ∪ B_v. By Part 1, I̅ isn't inside one of them alone. Some speed covers x₀; call it p, so p ≥ 2n−4 and L(p) ≤ 1/(n(n−2)). By Lemma 3, Ī meets at most one window of u.

- **p = u.** Then I ∩ B_u is a left piece of length ≤ L(u), and the rest lies in one window of v. So ℓ ≤ L(u) + L(v) < 2L(p) ≤ 2/(n(n−2)).
- **p = v, u doesn't cover x₀.** I ∖ B_u has a left component, inside the window of v at x₀, and possibly a right component.
  - No right component: ℓ ≤ L(u) + L(v) ≤ 2/n² + 1/(n(n−2)) = (3n−4)/(n²(n−2)).
  - Right component in a different window of v: a whole gap of v lies inside u's one window, so G(v) ≤ L(u), so L(v) ≤ 2L(u)/(n−2), so ℓ ≤ L(u)(n+2)/(n−2) ≤ 2(n+2)/(n²(n−2)).
  - Right component in the same window of v: I̅ lies inside one window of v, excluded above.

For n ≥ 8 the largest of these bounds is (3n−4)/(n²(n−2)).

- Odd n: 1/(4n) ≤ (3n−4)/(n²(n−2)) ⟺ n² − 14n + 16 ≤ 0 ⟺ n ≤ 12.7. So no pair for odd n ≥ 13.
- Even n: (n−3)/(4n(n−1)) ≤ (3n−4)/(n²(n−2)) ⟺ n³ − 17n² + 34n − 16 ≤ 0, which fails from n = 15 on. So no pair for even n ≥ 16. ∎

## Part B: 7 ≤ n ≤ 15, a finite check with proven bounds

ℓ ≤ L(u) + 2L(v) < 3L(u) gives n ≤ u ≤ 6/(nℓ). For each such u, I̅ ∖ B_u is nonempty (Part 1), and its longest component has some length λ > 0, so L(v) ≥ λ gives v ≤ 2/(nλ). That bound is exact and finite for each u. `enumerate_pairs.py` lists every pair in exact rational arithmetic and tests all r′.

Pairs covering the hole:

| n | pairs | tight with some r′ |
|---|---|---|
| 7 | 12 | none |
| 8 | 15 | (11, 13), r′ = 3 |
| 9 | (11,15), (11,17) | none |
| 10 | (13,17), (13,19) | none |
| 11 | none | |
| 12 | (15,21) | none |
| 13, 14, 15 | none | |

Cross-check independent of the bounds (`brute_check.py`): every pair u < v ≤ 600 for n = 7..15 gives the same lists. `census.c`, a separate exact set-cover search with no structure assumed, found (1,4,5,6,7,11,13) and (1,2,3,4,5,7,12) at n = 8, B = 50 as the only non-base primitive tight sets.

## What this says about the strange set

13 is close to forced: it's the odd speed that reaches back to speed 4's edge at x₀ (2n−3 = 13, the smallest with Lemma 2's bound; among the 15 pairs at n = 8, others exist). 13's first window stops at 5/104 ≈ .0481 and 7's starts at 3/56 ≈ .0536, so something else must bridge. 11 is the one that also serves t = 3/8: with 3 removed, the left side of 3/8 needs a speed ≡ 3 mod 8 or a multiple of 8 (‖v·3/8‖ ≤ 1/8 only for v ≡ 0, 3, 5 mod 8, and ≡ 5 serves the right side), and 11's window around 4/11 ends exactly at 3/8. This explains the shape, and the proof's own finite check is what closes it. It isn't a conceptual reason the whole covering holds.

## Corrections

Found by the adversarial reader, each checked by me afterward:

1. Lemma 3 was stated for the open interval, and Part A's "p = u" line used more than that. Counterexample shown above. Fixed by stating it for Ī; the proof is unchanged.
2. Part 1 had a needless n = 8 case. The inequality already fails there.
3. The commentary said "≡ 3 mod 8" where multiples of 8 also cover. Not load-bearing.
4. Lemma 1: ‖wx‖ for ‖vx‖.

The reader's own census, a full-circle exact sweep with no hole and no lemma, over all r′ and w ≤ 300 for n = 7..15, found this one set only. It also reports that Zhang's checks are thinner at the small end than I'd said: n = 8 with r′ ≠ 3 only to w ≤ 8n = 64, and n = 7 not at all.

## Not done

- Prior art. Zhang's v3 says "no general bound on the inserted speeds of tight two-entry modifications is known," and that different parts of a component may be covered by different speeds, "so the window argument of Section 3 does not carry over directly." The reader read Goddyn–Wong and searched several other papers without finding it; Wills 1967/68 and Cusick 1973/74 weren't reached. So this is a search result, not proof that it's new.
- No human mathematician has read this.
- Removals not containing 2. Zhang's Theorem 6.6 covers q ≥ 2, n ≥ max(40, 10q). Lemma 3 might tighten those too; I haven't tried.
