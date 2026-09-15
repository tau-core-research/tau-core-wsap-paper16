# Tau Core WSAP Paper 16

**Title:** Stability-Suppressed Leakage and Cross-Readout Residual Coherence:
A Synthetic Weak-Signal Amplification Protocol for Tau Core

This repository contains Paper 16 in the Tau Core research sequence.  It turns
the WSAP v1.0 package into a reproducible, paper-grade synthetic-methodology
manuscript.

## Main claim

In a fully synthetic hard-mode setting, several heterogeneous low-SNR readout
channels can jointly recover a shared latent parent component better than any
single readout channel, while predefined negative controls fail.

## Does not claim

This repository does **not** claim that:

- Tau Core is physically proven;
- a real parent morphology has been detected;
- dark matter or dark energy is explained;
- lensing, rotation, Hubble, BAO, or CMB data are fit;
- the synthetic parent is the structure of reality;
- WSAP is already a validation-grade real-data protocol.

## Included data

Only compact synthetic derived artifacts are included under `data/derived/`.
No private workbench logs or raw external data are required.

## Full-4D Score Boundary

The WSAP specificity score is synthetic. The later physical compiler requires
one source-frozen `E_K = (K_HH - K_std) - C K_VV^-1 C^dagger`, its common
coframe push, exact duplicate quotienting, and full terminal covariance. The
reported synthetic values are unchanged.

## Reproduce

```bash
python scripts/reproduce.py
```

The command:

1. regenerates the synthetic summary table from the frozen artifact;
2. builds paper figures;
3. compiles `paper16_submission_source/main.tex`;
4. builds `arxiv_submission_source.zip`;
5. runs `pytest -q`;
6. prints `PAPER16_WSAP_REPRODUCTION_COMPLETE`.

## arXiv source package

The generated `arxiv_submission_source.zip` contains the TeX source, BibTeX
file, and figure PDFs needed for upload.  It excludes the compiled PDF and
temporary TeX files.

## Scope

Paper 16 is a synthetic methodological prevalidation paper.  It supports the
plausibility of a Tau Core weak-signal strategy, not the truth of Tau Core as
a physical theory.

## Reproducibility grade

The current package is result-artifact reproducible: it recomputes the frozen
headline metrics from `data/derived/results_v10_numeric.json`, rebuilds figures,
compiles the manuscript, builds the arXiv zip, and runs smoke tests.

It is not yet a raw-generator replay package from the original random seed,
feature matrices, covariance model, and train/held-out split.  The manuscript
therefore treats WSAP v1.0 as a synthetic methodology demonstration and names
raw-generator replay as a required v1.1 upgrade before stronger claims.

The required v1.1 upgrade is:

- raw-generator replay from seed, parent generator, feature matrix, noise
  model, covariance rule, ridge parameter, solver tolerance, and train/held-out
  split;
- sensitivity sweeps over thresholds, ridge `lambda`, SNR, feature dimensions,
  and held-out split stability;
- mock-catalog injection with realistic covariance, masks, selection effects,
  and known parent/control components;
- independent implementation of the same frozen protocol to check whether the
  same pattern appears without sharing the original analysis code.

Paper 17 supplies a stricter downstream classifier for WSAP-like work:
shared-parent covariance support (`Z_shared`) must be reported separately from
morphology/orientation support (`Z_orient`).  Orientation-only structure is not
Tau Core evidence by itself, even when it looks visually or morphologically
suggestive.

<!-- BEGIN OBSERVER UPDATE 20260914 -->
## Observer realization update (2026-09-14)

Different terminal labels are not independent information sources without a factorization or novelty proof. A nonzero correlation is not automatically a standard-orthogonal Tau signal.

The manuscript distinguishes inherited BRAC contact, conditional coherent-state
selection and interacting local covariance from physical observer identification,
preparation and stable resolution. Those physical claims remain open. No
empirical score was changed. The [dependency and source-result ledger](data/derived/observer_update_2026_09_14.json) records the assumptions and controls.
<!-- END OBSERVER UPDATE 20260914 -->
