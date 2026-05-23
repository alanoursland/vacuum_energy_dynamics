# 95_schur_ratio_bound_theorem_attempt — Plan

## Purpose

Group 95 attempts to turn the Group 94 finite Schur ratio pattern into a sharper inequality theorem target.

Group 94 confirmed the patched Schur complement route and found:

```text
schur_N = alpha_N - correction_N
r_N = correction_N / alpha_N
```

with the finite pattern:

```text
2 <= N <= 10:
  r_N > 1

11 <= N <= 15:
  0 < r_N < 1
```

The first range is finite and can be audited directly. The real all-order burden is the post-transition bound:

```text
0 < r_N < 1 for all N >= 11.
```

Group 95 now tests whether this post-transition inequality can be reduced to exact positivity of symbolic numerator/denominator expressions, extended finite evidence, or a structural obstruction.

This group should try to make real progress by doing exact inequality analysis, not only printing more signs.

## Group Name

```text
95_schur_ratio_bound_theorem_attempt
```

## Central Question

```text
Can the post-transition Schur ratio bound 0 < correction_N/alpha_N < 1 be reduced to exact positivity conditions that are easier to prove?
```

## Starting State

Imported from Group 94:

```text
Schur complement identity confirmed through N=15;
Schur pivots positive through N=15;
two-regime alpha/correction balance supported through N=15;
Schur ratio bound supported through N=15;
all-order Schur positivity theorem open;
all-order ratio-bound theorem open;
all-order determinant nonzero open;
parent divergence identity unproven;
recombination blocked.
```

## Core Objects

For row-signed matrix:

```text
B_N = diag(epsilon) A_N
```

define the leading Schur decomposition:

```text
B_N = [[C, u],
       [v_row, alpha]]

correction_N = v_row C^(-1) u

schur_N = alpha_N - correction_N
```

and ratio:

```text
r_N = correction_N / alpha_N.
```

The target for `N >= 11` is:

```text
0 < r_N < 1.
```

Equivalent exact conditions when `alpha_N > 0`:

```text
correction_N > 0
alpha_N - correction_N > 0.
```

The second condition is exactly:

```text
schur_N > 0.
```

So Group 95 should test whether the ratio bound is actually just Schur positivity plus alpha/correction positivity, or whether it gives a new proof handle.

## What This Group May Do

Group 95 may:

```text
derive equivalences among ratio bounds, alpha signs, correction signs, and Schur positivity;
compute exact alpha/correction/schur signs through a wider finite range;
test numerator positivity for alpha, correction, and alpha-correction;
look for sign transitions beyond N=15;
test monotonicity or closeness-to-one patterns;
classify whether the ratio route is a genuine simplification or just a restatement of Schur positivity.
```

## What This Group Must Not Do

Group 95 must not:

```text
claim all-order ratio theorem from finite checks;
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
candidate_ratio_bound_problem.py
candidate_ratio_bound_equivalence.py
candidate_post_transition_ratio_evidence_N11_to_N25.py
candidate_ratio_gap_structure_probe.py
candidate_ratio_route_simplification_audit.py
candidate_group_95_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_ratio_bound_problem.py

Open Group 95 as a ratio-bound theorem attempt.

### 2. candidate_ratio_bound_equivalence.py

Show exact logical equivalence:

For `N >= 11`, if:

```text
alpha_N > 0
```

then:

```text
0 < correction_N/alpha_N < 1
```

is equivalent to:

```text
correction_N > 0
schur_N = alpha_N - correction_N > 0.
```

This is important because it tells us whether the ratio route is a simplification or merely a repackaging.

### 3. candidate_post_transition_ratio_evidence_N11_to_N25.py

Compute exact signs for:

```text
alpha_N
correction_N
schur_N
ratio_N
1-ratio_N
```

for `N=11..25`.

Expected:

```text
all positive:
  alpha_N
  correction_N
  schur_N
  ratio_N
  1-ratio_N.
```

This extends Group 94 beyond `N=15`.

### 4. candidate_ratio_gap_structure_probe.py

Analyze the gap:

```text
g_N = 1 - r_N = schur_N / alpha_N.
```

Test:

```text
g_N > 0
```

and whether it appears monotone, shrinking, or irregular.

Expected possible result:

```text
g_N positive through N=25 but not obviously monotone in a simple way.
```

or:

```text
g_N positive and decreasing through N=25.
```

This helps decide whether a monotonic bound proof is plausible.

### 5. candidate_ratio_route_simplification_audit.py

Classify whether the ratio route gives a new theorem handle.

Possible outcomes:

```text
RATIO_ROUTE_REDUCES_TO_SCHUR_POSITIVITY_PLUS_SIGNS:
  ratio bound is equivalent to alpha/correction/schur signs.

RATIO_ROUTE_ADDS_GAP_TARGET:
  gap positivity g_N=schur/alpha may be a useful bound target.

SIMPLE_MONOTONICITY_ROUTE_SUPPORTED:
  if gap/r_N monotonic behavior is clean.

SIMPLE_MONOTONICITY_ROUTE_NOT_ESTABLISHED:
  if not clean.
```

### 6. candidate_group_95_status_summary.py

Close the group.

Expected result:

```text
Group 95 extends post-transition ratio evidence and clarifies that the ratio theorem is equivalent to alpha/correction/schur positivity under alpha>0. The next theorem target should probably prove post-transition alpha>0, correction>0, and schur>0 structurally, or prove gap positivity directly.
```

## Key Success Criteria

Group 95 must earn at least one of:

```text
a logical equivalence reducing the ratio bound to simpler sign conditions;
extended exact post-transition evidence beyond N=15;
a gap/monotonicity pattern worth targeting;
or a controlled negative result showing the ratio route is not an independent proof route.
```

## Safe Handoff Options

Likely next groups:

```text
96_post_transition_schur_sign_theorem_attempt
96_alpha_correction_sign_theorem_attempt
96_schur_gap_positivity_theorem_attempt
96_biorthogonal_pivot_construction
96_hankel_difference_pivot_analysis
96_all_order_limit_obstruction
```

If Group 95 finds the ratio bound is equivalent to sign conditions, the best next group is probably:

```text
96_alpha_correction_sign_theorem_attempt
```

or:

```text
96_schur_gap_positivity_theorem_attempt.
```

## Final Interpretation

Group 95 asks:

```text
Is the ratio bound a new key,
or just the same lock seen through a smaller hole?
```

Goblin discipline:

```text
A sharper inequality is useful only if it cuts.
If it only renames the old wound, say so.
```
