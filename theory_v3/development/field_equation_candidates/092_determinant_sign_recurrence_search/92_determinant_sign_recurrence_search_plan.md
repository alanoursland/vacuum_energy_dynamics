# 92_determinant_sign_recurrence_search — Plan

## Purpose

Group 92 searches for the recurrence structure behind the Group 91 determinant sign pattern.

Group 91 corrected the determinant branch:

```text
determinant positivity is false;
det(A_11)<0;
det(A_N) nonzero verified through N=30;
sign(det(A_N)) = + for N=1..10;
sign(det(A_N)) = (-1)^N for N=11..30;
pivot sign = + for N=1..10;
pivot sign = - for N=11..30;
profile generation survives the sign flip.
```

Group 92 now asks whether this finite sign pattern can be reduced to a pivot recurrence or sign-normalized pivot positivity problem.

This is real progress if it converts the sign-pattern theorem into a smaller theorem target:

```text
prove sign-normalized pivots are positive;
or derive a recurrence explaining the N=11 transition;
or show that low-degree recurrence routes fail.
```

A failed simple recurrence search is useful if it prevents the project from assuming an easy formula exists.

## Group Name

```text
92_determinant_sign_recurrence_search
```

## Central Question

```text
Can the determinant sign pattern be explained by a recurrence or pivot-sign theorem,
or is the current evidence still only finite sign data?
```

## Starting State

Imported from Group 91:

```text
positivity theorem disproven by N=11;
pivot positivity theorem disproven by N=11;
determinant nonzero verified through N=30;
sign pattern supported through N=30;
sign-normalized determinant positive through N=30;
profile generation survives sign flip;
all-order nonzero theorem open;
sign-pattern theorem open;
parent divergence identity unproven;
recombination blocked.
```

## Main Reduction

Let:

```text
D_N = det(A_N)
p_N = D_N / D_(N-1)
D_0 = 1
```

Group 91 found:

```text
p_N > 0 for N <= 10
p_N < 0 for N >= 11   through N=30
```

If this pivot-sign law is true for all `N`, then determinant signs follow immediately:

```text
D_N > 0 for N <= 10
sign(D_N)=(-1)^N for N >= 11.
```

So the all-order sign theorem can be reduced to:

```text
prove p_N is never zero;
prove p_N changes sign once at N=11 and remains negative.
```

Equivalently, define the sign-normalized pivot:

```text
pi_N = p_N              for N <= 10
pi_N = -p_N             for N >= 11
```

Then the target becomes:

```text
pi_N > 0 for all N.
```

## What This Group May Do

Group 92 may:

```text
derive the determinant-sign-from-pivot-sign reduction;
compute sign-normalized pivots through N=30;
search for simple rational recurrences in the normalized pivot ratios;
test low-degree recurrence candidates;
classify whether the recurrence route is promising, blocked, or still open;
recommend the next theorem target.
```

## What This Group Must Not Do

Group 92 must not:

```text
claim an all-order recurrence from finite fit;
claim sign pattern theorem from finite checks;
revive determinant positivity;
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
candidate_sign_recurrence_problem.py
candidate_pivot_sign_reduction.py
candidate_sign_normalized_pivot_sequence.py
candidate_low_degree_rational_recurrence_search.py
candidate_recurrence_candidate_holdout_test.py
candidate_sign_recurrence_theorem_target.py
candidate_group_92_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_sign_recurrence_problem.py

Open Group 92 as a sign-recurrence search.

It should restate:

```text
positivity is dead;
nonzero/sign-pattern remains live;
recurrence search is the next target.
```

### 2. candidate_pivot_sign_reduction.py

Derive the conditional theorem:

```text
If p_N > 0 for N<=10 and p_N<0 for N>=11,
then D_N has the Group 91 sign pattern.
```

This reduces determinant signs to pivot signs.

### 3. candidate_sign_normalized_pivot_sequence.py

Compute:

```text
pi_N = p_N for N<=10
pi_N = -p_N for N>=11
```

through `N=30`.

Expected:

```text
pi_N > 0 through N=30.
```

### 4. candidate_low_degree_rational_recurrence_search.py

Search for a simple rational recurrence:

```text
pi_N / pi_(N-1) = R(N)
```

where `R` is a rational function of bounded degree.

Use a training range and reserve a holdout range.

Possible outcomes:

```text
simple recurrence found and held out;
or low-degree rational recurrence rejected.
```

Expected likely result:

```text
no simple low-degree rational recurrence found.
```

That is useful negative progress.

### 5. candidate_recurrence_candidate_holdout_test.py

If a recurrence candidate is found, test it against holdout data.

If no candidate is found, record a controlled obstruction:

```text
LOW_DEGREE_RATIONAL_RECURRENCE_NOT_FOUND
```

### 6. candidate_sign_recurrence_theorem_target.py

Classify the corrected theorem target:

```text
PIVOT_SIGN_REDUCTION_DERIVED
SIGN_NORMALIZED_PIVOT_POSITIVE_N1_TO_N30
LOW_DEGREE_RATIONAL_RECURRENCE_NOT_FOUND
ALL_ORDER_PIVOT_SIGN_THEOREM_OPEN
NONZERO_INVERTIBILITY_THEOREM_OPEN
```

### 7. candidate_group_92_status_summary.py

Close the group.

Expected result:

```text
sign theorem reduced to sign-normalized pivot positivity;
simple recurrence search does not close the theorem;
next route should use structural determinant/pivot proof rather than low-degree curve fitting.
```

## Key Success Criteria

Group 92 must earn at least one of:

```text
pivot-sign reduction derived;
a valid recurrence found;
a plausible recurrence route rejected cleanly;
sign-normalized pivot positivity supported through N=30.
```

## Safe Handoff Options

Likely next groups:

```text
93_pivot_sign_theorem_attempt
93_biorthogonal_pivot_construction
93_hankel_difference_pivot_analysis
93_all_order_limit_obstruction
93_covariant_payload_suppression_lift
```

If no simple recurrence is found, the best next group is:

```text
93_pivot_sign_theorem_attempt
```

or:

```text
93_biorthogonal_pivot_construction
```

because the sign theorem probably needs structural proof, not interpolation.

## Final Interpretation

Group 92 asks:

```text
Can the sign flip be made into a pivot theorem,
or is the recurrence goblin hiding behind a deeper structure?
```

Goblin discipline:

```text
A pattern is a trail.
A recurrence is a map.
Do not call footprints a map.
```
