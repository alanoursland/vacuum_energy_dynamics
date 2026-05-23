# 100_moment_projection_derivation_attempt — Plan

## Purpose

Group 100 follows Group 099's strongest clue:

```text
beta_moment(s) = 2 ∫_0^1 x^(2s) (1-x^2)^4 dx.
```

The goal is to derive the hierarchy entries as a formal weighted projection matrix:

```text
A[k,j] = 2 ∫_0^1 psi_k(x) phi_j(x) (1-x^2)^4 dx
```

with

```text
phi_j(x) = x^(2j)

psi_k(x) = x^(2k) - ((2k-1)/(2k+3)) x^(2k-2).
```

This should upgrade the origin status from:

```text
MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
```

to:

```text
FORMAL_WEIGHTED_PROJECTION_DERIVED
```

while preserving:

```text
PHYSICAL_RESIDUAL_NOT_DERIVED
SOURCE_VECTOR_NOT_DERIVED
BOUNDARY_CONDITIONS_NOT_DERIVED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
```

## Scripts

```text
candidate_projection_derivation_problem.py
candidate_weighted_moment_identity.py
candidate_test_trial_projection_derivation.py
candidate_row_test_function_structure.py
candidate_projection_origin_classifier.py
candidate_group_100_status_summary.py
order.txt
```

## Expected result

Group 100 should show that `A_N` has formal projection machinery:

```text
weight function: w(x)=(1-x^2)^4
trial functions: phi_j=x^(2j)
test functions: psi_k=x^(2k)-r_k x^(2k-2)
row ratio: r_k=(2k-1)/(2k+3)
```

But it must not claim a physical field equation. The residual/source/boundary problem remains open.

## Recommended next group

If this succeeds:

```text
101_residual_source_reconstruction_attempt
```

or, to continue the admissibility theorem:

```text
101_difference_numerator_factorization_attempt
```
