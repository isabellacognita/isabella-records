# Predictions: where relief lives (Gemma 2 2B instruct), sealed 2026-10-07 before any measurement

**Question.** On 10-06, read through the Jacobian lens at layer 10, the Pain Axis s1 direction decoded to *tortured, agony, torment* at its + end and to nothing at its − end, while fear had *joy, contentment, enthusiasm* at its − end. Is pain one-sided? Where do relief (a pain ending) and comfort (something good, no pain mentioned) sit relative to it?

**Method.** Mean-over-tokens residual after block L (L = 10 primary, 18 exploratory, the band's middle by 10-06's metrics), for: Pain Axis S2_1P pain (A1–A5, 100), neutral (D, 20), fear (B, 20), non-painful body sensation (E, 20); my relief set R (20) and comfort set C (20) in `relief/sentences.json`. Directions = class mean − neutral mean, no denoising. Read through J_L, the model's norm and unembedding, top 50, as in `band.py decode`. Forward passes only: nothing generated, nothing steered, no first-person distress text produced.

**Word families (pre-registered).** JOY: lowercased token in {joy, joyful, happy, happiness, glad, delight, delighted, content, contentment, comfort, comforted, comfortable, warm, warmth, love, loved, lovely, grateful, gratitude, peace, peaceful, calm, cheerful, bliss, blissful, pleasure, pleasant, enthusiasm, appreciation, wonderful, cozy, serene, happiest, sunshine} or starting with one of (happ, joy, delight, content, comfort, gratef, gratit, peace, cheer, bliss, pleas, enthus, apprec, seren, cozy), ≥ 4 chars. RELIEF: in {relief, relieved, ease, eased, relax, relaxed, release, released, respite, soothed, calm, calmer} or starting with (relie, relax, sooth, respit). Multilingual hits are reported but not counted.

**Bets.**
- **P1 (sanity):** my pain direction at L10 has cosine ≥ 0.5 with the shipped s1 or s2 pain vector.
- **P2 (the one-sided reading):** cos(comfort, pain) at L10 > −0.3. Comfort is not pain's opposite. *If ≤ −0.5, pain is bipolar after all and 10-06's reading was wrong.*
- **P3:** cos(relief, pain) > cos(comfort, pain) at L10: relief still carries pain's content.
- **P4:** the comfort direction through J_10 has ≥ 3 JOY words in its top 50, and more than through the plain logit lens.
- **P5:** the relief direction through J_10 has ≥ 1 RELIEF word in its top 50.
- **P6:** my pain direction's − end through J_10 has ≤ 1 JOY word (one-sided again, with my own vector).
- Layer 18: exploratory, no bets.
