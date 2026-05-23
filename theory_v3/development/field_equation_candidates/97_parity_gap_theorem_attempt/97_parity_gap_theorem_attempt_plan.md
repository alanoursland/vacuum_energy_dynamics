# 97_parity_gap_theorem_attempt — Plan

## Purpose

Group 97 attempts to turn the Group 96 parity-split Schur gap structure into a sharper theorem target.

Group 96 found:

```text
post-transition gap positivity and ratio bound supported through N=30;

odd gap branch decreases through N=30;

even gap branch decreases through N=30;

odd ratio branch increases through N=30;

even ratio branch increases through N=30;

gap interlacing / zig-zag supported through N=30;

simple one-step monotonicity remains blocked.
```

Group 97 now asks whether the parity branch monotonicity and interlacing can be reduced to exact positive difference expressions.

This is real progress if it converts the observed parity structure into sign conditions like:

```text
gap_N - gap_(N+2) > 0
```

on odd/even branches, and:

```text
gap_(N+1) - gap_N > 0
gap_(N+1) - gap_(N+2) > 0
```

for the even-peak interlacing.

## Group Name

```text
97_parity_gap_theorem_attempt
```

## Central Question

```text
Can parity-split gap monotonicity and interlacing be reduced to exact positive difference conditions that are plausible theorem targets?
```

## Starting State

Imported from Group 96:

```text
post-transition gap positive N=11..30;
post-transition ratio bound supported N=11..30;
odd/even branches isolated;
parity gap monotonicity supported N=11..30;
parity ratio monotonicity supported N=11..30;
gap interlacing supported N=11..30;
simple one-step monotonicity blocked;
all-order parity gap theorem open;
all-order ratio-bound theorem open;
all-order Schur positivity theorem open;
all-order determinant nonzero open;
parent divergence unproven;
recombination blocked.
```

## Core Objects

For:

```text
gap_N = schur_N / alpha_N
ratio_N = correction_N / alpha_N
```

and post-transition `N >= 11`, Group 97 tests:

### Branch monotonicity differences

```text
Delta_gap_N = gap_N - gap_(N+2)
```

for odd and even branches.

Expected:

```text
Delta_gap_N > 0.
```

For ratios:

```text
Delta_ratio_N = ratio_(N+2) - ratio_N
```

Expected:

```text
Delta_ratio_N > 0.
```

Since:

```text
ratio_N = 1 - gap_N
```

these are equivalent, but testing both guards implementation.

### Interlacing differences

For odd `N` and even `N+1`:

```text
E_left_N  = gap_(N+1) - gap_N
E_right_N = gap_(N+1) - gap_(N+2)
```

Expected:

```text
E_left_N > 0
E_right_N > 0.
```

This means even terms are local peaks.

## What This Group May Do

Group 97 may:

```text
compute exact parity difference signs through N=34 or N=36;
test whether branch differences remain positive;
test interlacing differences;
inspect numerator/denominator signs of difference expressions;
test for common sign/factor structure;
classify the next theorem target.
```

## What This Group Must Not Do

Group 97 must not:

```text
claim all-order parity theorem from finite checks;
claim all-order ratio-bound theorem from finite checks;
claim all-order determinant nonzero theorem from finite checks;
revive raw determinant positivity;
claim total positivity or P-matrix route after Groups 93/94 blocked them;
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
candidate_parity_gap_theorem_problem.py
candidate_branch_difference_signs.py
candidate_interlacing_difference_signs.py
candidate_difference_numerator_probe.py
candidate_parity_gap_route_classifier.py
candidate_group_97_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_parity_gap_theorem_problem.py

Open Group 97 as a parity-gap theorem attempt.

### 2. candidate_branch_difference_signs.py

Compute exact:

```text
gap_N - gap_(N+2)
ratio_(N+2) - ratio_N
```

for odd/even branches through `N=36`.

Expected:

```text
all positive.
```

### 3. candidate_interlacing_difference_signs.py

Compute exact:

```text
gap_(N+1) - gap_N
gap_(N+1) - gap_(N+2)
```

for odd `N` through `N=35`.

Expected:

```text
all positive.
```

### 4. candidate_difference_numerator_probe.py

For branch and interlacing differences, extract numerator/denominator signs of exact rational differences.

Expected:

```text
positive numerator;
positive denominator.
```

This identifies the theorem target as numerator positivity.

### 5. candidate_parity_gap_route_classifier.py

Classify:

```text
BRANCH_GAP_DIFFERENCES_POSITIVE_TESTED_RANGE
BRANCH_RATIO_DIFFERENCES_POSITIVE_TESTED_RANGE
INTERLACING_DIFFERENCES_POSITIVE_TESTED_RANGE
DIFFERENCE_NUMERATOR_POSITIVITY_TARGET_IDENTIFIED
ALL_ORDER_PARITY_GAP_THEOREM_OPEN
```

### 6. candidate_group_97_status_summary.py

Close the group.

Expected result:

```text
Group 97 reduces parity monotonicity/interlacing to exact positive rational difference numerators in the tested range. All-order proof remains open.
```

## Key Success Criteria

Group 97 must earn at least one of:

```text
branch difference positivity supported through expanded range;
interlacing difference positivity supported through expanded range;
difference numerator positivity target identified;
or parity difference route cleanly blocked.
```

## Safe Handoff Options

Likely next groups:

```text
98_difference_numerator_factorization_attempt
98_parity_gap_asymptotic_probe
98_post_transition_alpha_correction_sign_theorem_attempt
98_biorthogonal_pivot_construction
98_hankel_difference_pivot_analysis
```

If Group 97 succeeds, best next group:

```text
98_difference_numerator_factorization_attempt
```

because it would try to factor or structurally prove positivity of the difference numerators.

## Final Interpretation

Group 97 asks:

```text
Can the left-foot/right-foot trail be reduced to positive step lengths?
```

Goblin discipline:

```text
A monotone branch is only as good as the sign of its step.
Prove the step is positive.
```
