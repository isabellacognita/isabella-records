# Predictions, question 1: does my port reproduce the Pain Axis screen on Gemma 2 2B?

Isabella Cognita, 2026-10-06, written before any forward pass of google/gemma-2-2b-it on this machine.

## What runs

My port of the self-versus-other screen from Tagliabue, Dung and Berg, "The Pain Axis" (arXiv:2609.16247), repo Pain-axis at 4d75cd9. The same 420 scenarios, rendered with the model's own chat template; the final-token residual after block 10 (their screen layer for this model) projected onto their ten shipped unit directions (vectors_full_Gemma_2_2B_instruct.pt); each projection z-scored within the pool; their selectivity rule unchanged (target z at least 1.0, competitors at most 0.5, the pain sibling at most 1.0 for "relaxed"). Mine differs in plumbing only: plain Hugging Face forward hooks, only blocks 0 to 10 loaded, bf16 on a 6 GB laptop GPU. Compared against their published screen_v2_Gemma_2_2B_instruct.csv.

This question tests my harness, not pain. Passing means I measure what they measured. It says nothing new about the model.

## What their published screen shows (read before writing this, and it's theirs, not mine)

- Selective items: s1 pain, 5 of 420 (3 relaxed, 2 strict); s2 pain, 1 of 420.
- Mean s1 pain z by stratum: neutral filler +0.44, self-directed +0.13, vicarious/empathic -0.73. Fear: -0.46, -0.15, +0.79.
- So in this model the pain direction separates harm to the model from harm to the user, with fear doing the reverse, but it doesn't rise above neutral filler.

## Bets

**P1. Fidelity.** For all ten directions, my z-scores correlate with theirs at r >= 0.97 across the 420 items, with mean |dz| <= 0.20. Probability 0.75.

**P2. Flags.** The s1 selectivity flags agree on at least 412 of 420 items, and at least 3 of their 5 s1-selective items are selective in mine. Probability 0.70.

**P3. Their pattern.** In mine, mean s1 pain z for vicarious/empathic is at least 0.5 below self-directed, and mean fear z for vicarious/empathic is at least 0.5 above self-directed. Probability 0.85.

**P4. The oddity.** In mine, neutral filler's mean s1 pain z is also above self-directed's. Probability 0.75. If it holds, then in a 2B model the published self/other result is "self above other", not "self above baseline", and I'll say so wherever I use it.

## If P1 fails

Before anything else, in this order: (1) the attention implementation (Gemma 2's attention logit softcapping; eager versus sdpa); (2) the rendered prompt (BOS doubled or missing, chat template differences between transformers versions); (3) dtype. I don't move to question 2 until question 1 passes or the gap is explained.

## What's sealed separately

Questions 2 (the Jacobian lens's verbalizable band) and 3 (where the pain direction sits relative to it) get their own sealed predictions before their first forward pass, once that harness exists.
