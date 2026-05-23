# 96_post_transition_schur_gap_structure — Plan

## Purpose

Group 96 follows the main clue from Group 95.

Group 95 showed that the post-transition Schur ratio route is mostly a gap/sign reformulation:

```text
r_N = correction_N / alpha_N
gap_N = 1 - r_N = schur_N / alpha_N
```

and extended evidence through `N=25`:

```text
alpha_N > 0
correction_N > 0
schur_N > 0
0 < r_N < 1
gap_N > 0
```

for `N=11..25`.

But Group 95 also found that simple one-step monotonicity fails:

```text
gap decreasing failures:
  (11,12), (13,14), (15,16), ...

ratio increasing failures:
  (11,12), (13,14), (15,16), ...
```

This suggests the gap/ratio structure may be parity-split.

Group 96 tests that clue directly.

## Group Name

```text
96_post_transition_schur_gap_structure
```

## Central Question

```text
Does the post-transition Schur gap have a parity-split structure that can become a theorem target?
```

## Starting State

Imported from Group 95:

```text
ratio-bound equivalence derived;
post-transition ratio-bound supported N=11..25;
Schur gap positive N=11..25;
ratio route repackages Schur positivity as gap positivity under alpha>0;
simple gap monotonicity not established;
simple ratio monotonicity not established;
all-order ratio-bound theorem open;
all-order Schur positivity theorem open;
all-order determinant nonzero open;
parent divergence identity unproven;
recombination blocked.
```

## Core Objects

For row-signed Schur decomposition:

```text
schur_N = alpha_N - correction_N
r_N = correction_N / alpha_N
gap_N = 1 - r_N = schur_N / alpha_N.
```

Group 96 splits post-transition indices:

```text
odd branch:
  N = 11, 13, 15, ...

even branch:
  N = 12, 14, 16, ...
```

and tests whether each branch has simpler structure than the combined one-step sequence.

## What This Group May Do

Group 96 may:

```text
compute exact post-transition gap and ratio evidence through N=30;
split gap and ratio into odd/even branches;
test monotonicity within each branch;
test interlacing inequalities between odd and even branches;
test positivity of branch differences exactly;
classify whether parity-split monotonicity is a useful theorem target.
```

## What This Group Must Not Do

Group 96 must not:

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
candidate_gap_structure_problem.py
candidate_parity_gap_sequence_probe.py
candidate_parity_monotonicity_test.py
candidate_gap_interlacing_test.py
candidate_parity_theorem_target_classifier.py
candidate_group_96_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_gap_structure_problem.py

Open Group 96 as a parity-split Schur gap structure search.

### 2. candidate_parity_gap_sequence_probe.py

Compute exact post-transition values for:

```text
gap_N = schur_N / alpha_N
ratio_N = correction_N / alpha_N
```

for `N=11..30`.

Record odd/even sequences separately.

### 3. candidate_parity_monotonicity_test.py

Test monotonicity within parity branches:

```text
gap_11, gap_13, gap_15, ...
gap_12, gap_14, gap_16, ...

ratio_11, ratio_13, ratio_15, ...
ratio_12, ratio_14, ratio_16, ...
```

Likely target:

```text
gap decreases within each parity branch;
ratio increases within each parity branch.
```

### 4. candidate_gap_interlacing_test.py

Test interlacing relationships, for example:

```text
gap_odd(N) < gap_even(N+1)
gap_even(N) > gap_odd(N+1)
```

or whatever finite evidence shows.

This matters because one-step monotonicity failed; interlacing may explain the zig-zag.

### 5. candidate_parity_theorem_target_classifier.py

Classify:

```text
POST_TRANSITION_GAP_POSITIVE_N11_TO_N30
PARITY_GAP_MONOTONICITY_SUPPORTED_N11_TO_N30
PARITY_RATIO_MONOTONICITY_SUPPORTED_N11_TO_N30
SIMPLE_ONE_STEP_MONOTONICITY_BLOCKED
INTERLACING_PATTERN_SUPPORTED_OR_BLOCKED
ALL_ORDER_PARITY_GAP_THEOREM_OPEN
```

### 6. candidate_group_96_status_summary.py

Close the group.

Expected useful result:

```text
Group 96 shows that the Schur gap is not one-step monotone but may be parity-branch monotone. The next theorem target becomes parity-split gap positivity/monotonicity rather than simple monotonicity.
```

## Key Success Criteria

Group 96 must earn at least one of:

```text
parity-split monotonicity supported;
interlacing pattern identified;
simple parity route blocked cleanly;
post-transition evidence extended to N=30.
```

## Safe Handoff Options

Likely next groups:

```text
97_parity_gap_theorem_attempt
97_post_transition_alpha_correction_sign_theorem_attempt
97_even_odd_schur_asymptotic_probe
97_biorthogonal_pivot_construction
97_hankel_difference_pivot_analysis
```

If parity-split monotonicity is supported, the best next group is:

```text
97_parity_gap_theorem_attempt
```

If parity-split monotonicity fails, the better next group is:

```text
97_post_transition_alpha_correction_sign_theorem_attempt
```

## Final Interpretation

Group 96 asks:

```text
Was the failed monotonicity proof looking with the wrong eye?
```

Goblin discipline:

```text
If the footprints zig-zag,
sort left feet from right feet.
