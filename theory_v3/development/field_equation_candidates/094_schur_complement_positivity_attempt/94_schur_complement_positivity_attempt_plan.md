# 94_schur_complement_positivity_attempt — Plan

## Purpose

Group 94 confirms the Group 93 Schur-complement identity after the Group 93 patch and then attempts to learn something structural from the Schur pivots.

Group 93 successfully derived and verified the row-sign normalization:

```text
B_N = diag(epsilon) A_N

epsilon_k = +1 for k <= 10
epsilon_k = -1 for k >= 11
```

with:

```text
det(B_N) = sign-normalized det(A_N)
leading pivots of B_N positive through N=30.
```

Before the patch, Group 93 did **not** successfully archive the Schur-complement pivot identity because the script used the wrong matrix orientation and failed with:

```text
ShapeError: Matrix size mismatch: (2,1) * (2,1)
```

Group 94 now independently confirms the fixed Schur identity and tests whether Schur positivity has a simple term-balance structure.

## Group Name

```text
94_schur_complement_positivity_attempt
```

## Central Question

```text
After repairing the Schur identity, can row-signed pivot positivity be reduced to a usable Schur-complement positivity condition or bound?
```

## Starting State

Imported from Group 93:

```text
row-sign normalization derived;
row-signed leading determinants and pivots positive through N=30;
strict total positivity route blocked;
P-matrix route blocked;
Schur complement identity patched/confirmed;
Schur complement identity not archived as derived;
all-order leading-minor positivity open;
all-order determinant nonzero open;
parent divergence identity unproven;
recombination blocked.
```

## Core Identity

For:

```text
B_N = [[C, u],
       [v_row, alpha]]
```

where `C=B_(N-1)` is the leading block, the leading pivot is:

```text
pivot_N = det(B_N)/det(B_(N-1))
        = alpha - v_row C^(-1) u.
```

The Group 93 bug used:

```python
v.T * C.LUsolve(u)
```

when `v` was already row/column mismatched.

Correct implementation:

```python
v_row = B[N-1, :N-1]
x = C.LUsolve(u)
schur = alpha - (v_row * x)[0]
```

## Desired Outcome

A useful Group 94 result is:

```text
SCHUR_COMPLEMENT_IDENTITY_CONFIRMED
SCHUR_PIVOTS_MATCH_DETERMINANT_PIVOTS_N1_TO_N15
SCHUR_PIVOTS_POSITIVE_N1_TO_N15
SCHUR_TERM_BALANCE_HAS_TWO_REGIMES
SIMPLE_TERM_BALANCE_BOUND_SUPPORTED_FINITE_RANGE
ALL_ORDER_SCHUR_POSITIVITY_THEOREM_OPEN
```

A possible negative result is also useful:

```text
SCHUR_IDENTITY_REPAIRED
NO_SIMPLE_TERM_BALANCE_BOUND_FOUND
STRUCTURAL_PROOF_STILL_REQUIRED
```

## What This Group May Do

Group 94 may:

```text
repair Schur complement script;
verify Schur pivot identity through a finite range;
analyze alpha and correction term signs;
test whether positive Schur pivots come from a two-regime dominance rule;
test simple finite bound candidates;
classify the theorem target.
```

## What This Group Must Not Do

Group 94 must not:

```text
claim all-order Schur positivity from finite checks;
claim all-order determinant nonzero theorem from finite checks;
revive raw determinant positivity;
claim total positivity or P-matrix route after Group 93 blocked them;
claim all-order local inertness;
claim hierarchy convergence;
claim full covariant geometry;
claim rho(y)=0;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_schur_repair_problem.py
candidate_schur_identity_repair.py
candidate_schur_term_balance_regimes.py
candidate_schur_ratio_bound_probe.py
candidate_schur_theorem_target_classifier.py
candidate_group_94_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_schur_repair_problem.py

Open Group 94 as a Schur-complement repair and theorem-target group.

### 2. candidate_schur_identity_repair.py

Patch the Group 93 orientation bug and verify:

```text
schur_N = det(B_N)/det(B_(N-1))
```

through `N=15`.

### 3. candidate_schur_term_balance_regimes.py

Decompose:

```text
schur_N = alpha_N - correction_N
```

where:

```text
correction_N = v_row C^(-1) u.
```

Test signs and dominance.

Expected finite pattern:

```text
N=1:
  correction = 0

N=2..10:
  alpha < 0, correction < 0, |correction| > |alpha|
  so alpha - correction > 0

N>=11 in tested range:
  alpha > 0, correction > 0, alpha > correction
  so alpha - correction > 0
```

### 4. candidate_schur_ratio_bound_probe.py

Test the ratio:

```text
r_N = correction_N / alpha_N
```

Expected finite pattern:

```text
N=2..10:
  r_N > 1

N>=11:
  0 < r_N < 1
```

This is not a proof, but it gives a candidate bound theorem.

### 5. candidate_schur_theorem_target_classifier.py

Classify:

```text
SCHUR_COMPLEMENT_IDENTITY_CONFIRMED
SCHUR_PIVOTS_POSITIVE_N1_TO_N15
TWO_REGIME_SCHUR_BALANCE_SUPPORTED_N1_TO_N15
SCHUR_RATIO_BOUND_SUPPORTED_N2_TO_N15
ALL_ORDER_SCHUR_BOUND_THEOREM_OPEN
ALL_ORDER_DETERMINANT_NONZERO_OPEN
```

### 6. candidate_group_94_status_summary.py

Close the group.

Expected result:

```text
Group 94 repairs the Schur route and finds a finite two-regime balance pattern, but no all-order proof.
```

## Key Success Criteria

Group 94 must at minimum confirm the patched Schur script.

Stronger success:

```text
derive a clear candidate bound:
  correction/alpha > 1 for 2<=N<=10
  0<correction/alpha<1 for N>=11
```

This would explain Schur positivity in the tested range and point to a theorem target.

## Safe Handoff Options

Likely next groups:

```text
95_schur_ratio_bound_theorem_attempt
95_biorthogonal_pivot_construction
95_hankel_difference_pivot_analysis
95_all_order_limit_obstruction
95_covariant_payload_suppression_lift
```

Best next group if Group 94 succeeds:

```text
95_schur_ratio_bound_theorem_attempt
```

because it would try to prove the finite balance pattern all-order.

## Final Interpretation

Group 94 asks:

```text
Can the Schur door be fixed,
and does it show where the positivity comes from?
```

Goblin discipline:

```text
Patch the handle.
Then check whether the hinge or the lock is doing the work.
```
