# candidate_ratio_bound_problem — Analysis Note

## Result

`candidate_ratio_bound_problem.py` opens Group 95 as a Schur ratio-bound theorem attempt.

It correctly imports the Group 94 state:

```text
Schur complement identity confirmed through N=15;
Schur pivots positive through N=15;
two-regime alpha/correction balance supported through N=15;
correction/alpha ratio bound supported through N=15;
all-order Schur positivity theorem open;
all-order ratio-bound theorem open;
all-order determinant nonzero open;
parent divergence unproven;
recombination blocked.
```

The group target is:

```text
test whether the ratio bound reduces to exact sign/gap conditions.
```

## Interpretation

This is the right opening.

Group 94 gave a sharper-looking inequality:

```text
0 < correction_N / alpha_N < 1
```

for the post-transition regime. Group 95 correctly asks whether that inequality is actually a new proof handle or just Schur positivity written in ratio form.

This distinction matters. A narrower-looking inequality is only useful if it makes the proof easier. If it merely renames the old positivity condition, the next group should not over-invest in the ratio route as an independent theorem path.

## What Changed

The branch moves from observing the ratio pattern to auditing what the ratio pattern really means.

## What Did Not Change

The opener does not prove the all-order ratio bound. It only frames the exact inequality audit.

Raw determinant positivity remains false. Parent divergence remains unproven. Recombination remains blocked.

## Carry-forward status

```text
RATIO_BOUND_THEOREM_ATTEMPT_OPENED
FINITE_RATIO_EVIDENCE_NOT_THEOREM
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```
