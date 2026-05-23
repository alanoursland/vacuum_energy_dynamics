# candidate_pivot_evidence_extension_N1_to_N12 — Analysis Note

## Result

`candidate_pivot_evidence_extension_N1_to_N12.py` produced the most important unexpected result in Group 90.

The script intended to extend positivity evidence through `N=12`, but the raw values show:

```text
N=1..10:
  det(A_N)>0
  pivot>0

N=11:
  det(A_N)>0? False
  pivot>0? False

N=12:
  det(A_N)>0? True
  pivot>0? False
```

The exact `N=11` values are negative:

```text
det(A_11) < 0
pivot_11 < 0
```

The `N=12` determinant is positive, but the pivot is negative because it is the ratio of a positive `det(A_12)` to a negative `det(A_11)`.

The output’s governance section incorrectly says:

```text
det(A_N)>0 through N=12
pivots positive through N=12
```

Those status lines are contradicted by the raw derived results.

## Interpretation

This is the central result of Group 90.

The all-order determinant positivity conjecture is not merely unproven. It is false as stated.

The correct status is:

```text
DETERMINANT_POSITIVITY_DISPROVEN_BY_N11
PIVOT_POSITIVITY_DISPROVEN_BY_N11
DETERMINANT_NONZERO_VERIFIED_THROUGH_N12
INVERTIBILITY_ROUTE_REMAINS_OPEN
```

This is a major correction. The hierarchy only requires:

```text
det(A_N) != 0
```

for Cramer coefficient generation. It does not require positivity. So the hierarchy is not killed by the `N=11` sign flip.

But the proof target changes:

```text
old target:
  prove det(A_N)>0 for all N

new target:
  prove det(A_N)!=0 for all N
  and understand the determinant sign pattern.
```

## What Changed

Group 90 unexpectedly breaks the positivity route.

This is real progress because it prevents future groups from chasing a false theorem.

## What Did Not Change

The determinant is still nonzero through `N=12`. The finite hierarchy generation may still continue. All-order invertibility remains open.

## Steering Consequence

Before any future determinant theorem group, statuses in the scripts/classifier/summary must be corrected. The next group should probably be:

```text
91_determinant_sign_pattern_and_nonzero_audit
```

or:

```text
91_invertibility_theorem_retarget
```

The project should not proceed with `DETERMINANT_POSITIVITY_THEOREM` as the main target.
