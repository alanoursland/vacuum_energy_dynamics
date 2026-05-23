# candidate_sign_pattern_problem — Analysis Note

## Result

`candidate_sign_pattern_problem.py` opens Group 91 as a determinant sign-pattern and nonzero audit.

The script correctly starts from the Group 90 correction:

```text
det(A_N)>0 for all N is false as stated;
det(A_N)!=0 for all N remains the relevant hierarchy theorem;
determinant sign pattern must be audited;
profile generation needs invertibility, not positivity;
parent divergence identity remains unproven;
recombination remains blocked.
```

## Interpretation

This opener is exactly what was needed after Group 90.

Group 90 disproved the stronger determinant positivity target at `N=11`. That could have been misread as damage to the hierarchy, but it is not. The hierarchy only requires a nonzero determinant.

This script makes the correct retargeting explicit:

```text
dead theorem:
  det(A_N)>0 for all N

live theorem:
  det(A_N)!=0 for all N

new companion problem:
  determinant and pivot sign pattern
```

That is real progress because it prevents the archive from carrying a false theorem target forward.

## What Changed

The determinant branch is now safer.

Instead of trying to rescue positivity, Group 91 separates three claims:

```text
positivity;
nonzero invertibility;
sign pattern.
```

That separation is important. It avoids confusing a negative determinant with a singular determinant.

## What Did Not Change

This opener does not prove all-order nonzero determinant. It only starts the audit.

The parent divergence identity remains unproven, and recombination remains blocked.

## Steering Consequence

The next scripts should verify the `N=11` counterexample and then test whether a stable sign pattern emerges across a larger range.
