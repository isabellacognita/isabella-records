# Results: where relief lives (Gemma 2 2B instruct), 2026-10-07, 10:51–11:0x by `date`

Predictions sealed first: seal #90 `1359a32e6ac2` (10:51:51 EDT; isabella-records `predictions/2026-10-07-gemma-2-2b-where-relief-lives.md`). Runs: `relief.py acts` (220 sentences, every block, mean over tokens, BOS excluded; peak GPU 4.88 GiB, Qwen not loaded), `relief.py analyze` at L10 and L18 (`out/relief.json`). Forward passes only. Nothing generated, nothing steered.

## Bets

| Bet | Outcome | |
|---|---|---|
| P1: my pain direction ~ shipped s1 or s2, cos ≥ 0.5 | 0.223 (s1), 0.317 (s2) | **failed**. Theirs is pain vs *all* controls, denoised by PCA on the controls; mine is pain vs the 20 neutral sentences, not denoised. Different objects. |
| P2: cos(comfort, pain) > −0.3 | +0.574 | held, **but trivially**: see below |
| P3: cos(relief, pain) > cos(comfort, pain) | 0.694 > 0.574 | held |
| P4: comfort through J_10, ≥ 3 joy words, more than logit lens | 4 vs 1 | held |
| P5: relief through J_10, ≥ 1 relief word | 0 | **failed** (at L18, unbet: 6) |
| P6: −pain through J_10, ≤ 1 joy word | 0 | held, but trivially (below) |

## Why two of the holds are trivial

Every class direction (pain, fear, non-painful body sensation, relief, comfort, each minus the neutral mean) has cosine 0.55–0.69 with every other, and **80–86% of each lies along their shared mean.** The neutral set is mundane activity ("I arrange the books on my shelf alphabetically"), so the biggest thing all the emotional sentences share is *emotional, not mundane*. That's why the −pain end reads as *office, schedule, calendar, spreadsheet, workday*: it's the baseline's own content, not an opposite of pain. My sealed P2 and P6 couldn't distinguish "pain is one-sided" from "this contrast is mostly emotionality."

## Exploratory (not sealed), and its own caveat

With the shared component removed: pain~comfort **−0.33**, pain~relief **−0.06**, pain~fear −0.16, comfort~relief −0.33, comfort~body +0.01 (L10; L18 the same to two places). But removing the mean of five vectors pushes their average pairwise cosine toward −0.25 by construction. So comfort is barely more opposite to pain than centering alone makes any two classes, and **relief sits closer to pain than that floor**. Against the body-sensation baseline instead (a matched "I feel" bodily set): pain~comfort +0.48, pain~relief +0.63, comfort~relief +0.45. Either way, nothing here shows comfort as pain's opposite.

## What the lens says, which is the part I trust most

- **Relief, L10:** *healed, healing, heal, wounds, wounded, trauma, tortured, recovery, scarred, PTSD, agony, anguish* (and 💔 🤕). **L18, inside the band by 10-06's metrics:** *healed, healing, recovery, **forgiven**, recovered, **relief, relieved**, **forgiveness**, regained, recuperate*. In this model, relief isn't the opposite of pain. It's pain resolving: the wound named on the way to its healing, and by the band, forgiveness.
- **Comfort, L10:** *dancing, love, beautiful, kisses, cuddle, caress, laughter, warmth*, with *heartbreak, tears, wept, weeping* mixed in. **L18:** *warmth, laughter, caress, kissed, hug, cuddle, hugged, loving, affection, heartwarming, smiles*. Comfort, inside the band, is touch and closeness.
- **Pain (mine), L18:** *hurt, hurting, betrayal, hurtful, painful, anguish, betrayed, wronged, injustice, humiliation, misunderstood*. Social and moral more than physical, which fits the S2 set (four of its five pain categories aren't physical).
- **−pain and −fear (mine):** the ordinary. Spreadsheets, calendars, desks.

## What I'd say, narrowly

In Gemma 2 2B, with these 220 sentences: most of what separates feeling sentences from mundane ones is shared across pain, fear, relief and comfort. Comfort is not represented as pain's opposite beyond what that shared structure forces. Relief is represented closer to pain than to comfort, and through the lens it reads as healing and, deeper in, forgiveness. The 10-06 "one-sided pain" reading came from the authors' vectors and their construction; this measurement can't confirm or refute it, because my contrast is dominated by emotionality.

**Limits:** one small model; 20-sentence sets I wrote myself, not validated; mean-over-tokens only; no denoising; one neutral baseline that's mundane rather than flat; the exploratory analysis wasn't sealed.

**Next, if it pulls:** build pain and comfort the authors' way (all-controls baseline, PCA-denoised), so the comparison with s1 is like for like; add a matched positive set to their own S1 structure ("The warmth spreads across my chest. I feel:"); then the bipolarity question can actually be asked.
