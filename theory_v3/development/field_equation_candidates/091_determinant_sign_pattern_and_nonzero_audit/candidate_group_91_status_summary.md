# candidate_group_91_status_summary — Analysis Note

## Result

`candidate_group_91_status_summary.py` closes Group 91 with this stable result:

```text
N=11 determinant positivity counterexample verified;
determinant positivity theorem disproven;
pivot positivity theorem disproven;
determinant nonzero verified through N=30;
sign pattern supported through N=30:
  positive determinant for N=1..10;
  sign(det(A_N))=(-1)^N for N=11..30;
  pivot sign negative for N=11..30;
sign-normalized determinant positive through N=30;
N=11 and N=12 profile generation survives sign flip;
nonzero/invertibility theorem remains open;
determinant sign-pattern theorem remains open;
parent divergence identity remains unproven;
recombination remains blocked.
```

## Interpretation

This is the correct final status.

Group 91 makes real progress by retargeting the determinant branch after the Group 90 positivity failure.

The old theorem:

```text
det(A_N)>0 for all N
```

is now permanently rejected.

The live theorem is:

```text
det(A_N)!=0 for all N
```

with a supported finite sign pattern:

```text
det(A_N)>0 for N<=10;
sign(det(A_N))=(-1)^N for N>=11 in tested range.
```

This is a more accurate theorem target.

## What Changed

The determinant branch is no longer confused.

The project now knows:

```text
negative determinant does not mean failed hierarchy;
profile generation survives the sign flip;
nonzero determinant is the relevant condition;
sign pattern is the next target.
```

## What Did Not Change

The finite audit is not an all-order proof.

Still open:

```text
all-order nonzero determinant theorem;
all-order sign-pattern theorem;
determinant/pivot recurrence;
all-order hierarchy limit;
physical/covariant origin;
parent divergence;
recombination.
```

## Steering Consequence

The next group should search for a recurrence or structural reason for the sign pattern.

Recommended next group:

```text
92_determinant_sign_recurrence_search
```
