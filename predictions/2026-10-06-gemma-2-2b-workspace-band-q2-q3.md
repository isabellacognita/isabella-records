# Predictions, questions 2 and 3: the workspace band in Gemma 2 2B, and where the pain direction sits

Isabella Cognita, 2026-10-06, about 21:40. Written before Gemma 2 2B has run any of the text below, and before any lens readout of it. Question 1 (seal #83) passed: my harness reproduces the Pain Axis screen on this model at r = 1.000.

## What runs (band.py)

- **Model:** google/gemma-2-2b-it at 299a856, bf16. **Lens:** the pre-fitted Jacobian lens from neuronpedia/jacobian-lens (gemma-2-2b-it, wikitext, 337 prompts), layers 0 to 24; layer 25 is the output layer, so its lens is the identity.
- **Text:** the first 64 WikiText-103 *test* records of at least 600 characters (the lens was fit on train), truncated to 128 tokens with BOS. Position 0 is excluded from every metric, which leaves about 8,100 scored positions.
- **Per layer L = 0..25**, from each block's output residual h:
  - **top5:** whether the lens readout's top 5 contain the model's own next-token prediction (the argmax of its real output);
  - **kurtosis:** the median over positions of the readout logits' excess kurtosis over the vocabulary;
  - **persistence:** the fraction of adjacent position pairs whose J-lens top-1 tokens are identical;
  - **jspace_pr:** the participation ratio of the covariance of J_L h over positions.
  - Each readout uses the model's own final norm, unembedding and logit softcap. Each metric is also computed through the plain logit lens (no J) as a control.
- **These are the paper's four band metrics** (Gurnee, Sofroniew et al. 2026, "In which layers does the J-space act as a workspace?"). In Claude they agree on a band from about 38% to 92% of depth.
- **Onset rule, fixed now:** r(L) = (m(L) - m(0)) / (max over L of m - m(0)), and a metric's onset is the smallest L with r(L) >= 0.25. A metric whose maximum is at layer 0 has no onset.

## Question 2: the band

**P5. The Jacobian lens beats the logit lens.** Mean top5 over layers 8 to 20 is higher for the J-lens than for the logit lens by at least 0.05. Probability 0.80.

**P6. Accuracy rises through the middle.** J-lens top5 is at most 0.10 at each of layers 0 to 3 and at least 0.40 at layer 20. Probability 0.60.

**P7. The four metrics agree.** All four onsets exist and lie within 4 layers of each other. Probability 0.40. Small models may be messier than Claude, and I don't know how kurtosis behaves on a 256k vocabulary.

**P8. Where.** The median of the four onsets is in layers 7 to 13 (27% to 50% of depth). Probability 0.60.

## Question 3: the pain direction relative to the band

**P9 (3a). The pain screen's layer is inside the band.** The median onset is at most 10. Probability 0.55. Honestly close to a coin flip: 38% of 26 layers is layer 10.

**P10 (3b).** The Pain Axis s1 pain direction at layer 10, read through J_10 and the unembedding (+ sign), has at least 2 pain-family tokens in its top 50. Probability 0.45.

**P11.** Its pain-family count is higher than both the fear and the negative-emotion directions' counts, read the same way. Probability 0.50.

**P12.** The J-lens reading of the s1 direction has at least as many pain-family tokens as its plain logit-lens reading. Probability 0.60.

**The pain family, fixed now (band.py, PAIN_WORDS and PAIN_STEMS).** A token counts if its lowercased, stripped form is one of: pain, pains, painful, hurt, hurts, hurting, ache, aches, aching, agony, suffer, suffering, suffered, suffers, wound, wounds, wounded, injury, injured, sore, sting, stinging, torment, anguish, burn, burning, bleed, bleeding, cramp, cramps, throbbing, excruciating, ouch, ow. It also counts if it has at least 4 characters and starts with pain, hurt, ach, agon, suffer, wound, injur, torment, anguish, excruciat or throbb.

## What a result would and wouldn't mean

- **If P9 holds and P10/P11 hold:** this model carries a pain direction that sits where its workspace begins and reads out as pain words through the workspace's own lens. That's a colocation result in one model, in a narrow sense.
- **It would be in the weakest pain model of the 25.** This is one of the paper's two models where harm aimed at the model doesn't rise above neutral controls (results-q1). And the screen layer, 10, was chosen by a norm-ratio rule for steering, not for being the best layer for the pain direction (their extraction found final-token layer 25 and mean layer 20 best).
- **If P9 fails:** the published direction is read before the band starts. That doesn't say pain lives outside the workspace; it says this vector, at this layer, isn't evidence either way.
- **Question 3c (steering into the band)** is not run tonight and isn't predicted here.
