# Executive Summary — Tau Core WSAP v1.0

## Core idea

Tau Core does not predict a huge clean signal in one channel. It predicts weak residual leakage across several readout sectors.

Key slogan:

> Stability suppresses amplitude; shared parent preserves coherence.

## Final synthetic result

WSAP v1.0 numeric achieved a synthetic hard-mode PASS.

- SNR per channel: 0.44
- Best single-sector parent recovery: 0.361
- Joint parent recovery: 0.673
- Joint gain: 0.312
- Mean held-out noisy prediction: 0.411
- Specificity score: 0.646
- Kernel-shuffle control: -0.051
- Common-noise vs parent: -0.389

## Meaning

Several weak heterogeneous synthetic readouts jointly recovered a shared parent better than any single readout, while negative controls failed.

## Claim boundary

This is not real physics evidence. It is a methodological proof-of-concept.

## Next step

Move from synthetic WSAP to semi-real mock catalogs, then blind real-data pilots.
