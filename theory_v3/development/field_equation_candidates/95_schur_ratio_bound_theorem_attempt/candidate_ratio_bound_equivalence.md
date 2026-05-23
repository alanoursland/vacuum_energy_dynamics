# candidate_ratio_bound_equivalence — Analysis Note

## Result

`candidate_ratio_bound_equivalence.py` derives the key logical reduction.

Assuming:

```text
alpha_N > 0
```

the bound:

```text
0 < correction_N / alpha_N < 1
```

is equivalent to:

```text
correction_N > 0
alpha_N - correction_N > 0.
```

The second condition is exactly:

```text
schur_N > 0.
```

The script verifies symbolically:

```text
1 - correction/alpha = (alpha - correction)/alpha
schur/alpha = (alpha - correction)/alpha
difference = 0.
```

It also checks the finite data:

```text
finite equivalence failures N=11..25: []
```

## Interpretation

This is the central conceptual result of Group 95.

The ratio route does not bypass Schur positivity. Under `alpha_N > 0`, it repackages the same burden as:

```text
correction_N > 0
schur_N > 0.
```

Equivalently:

```text
gap_N = 1 - ratio_N = schur_N / alpha_N.
```

So proving the ratio bound is not easier by default. It is useful only if `gap_N > 0` or the alpha/correction signs are easier to prove than `schur_N > 0` directly.

## What Changed

The theorem target is clarified.

Old possible reading:

```text
prove the ratio bound; maybe it is independent.
```

Correct reading:

```text
prove alpha_N > 0, correction_N > 0, and gap_N = schur_N/alpha_N > 0.
```

The ratio route is a gap/sign reformulation, not a separate escape hatch.

## What Did Not Change

This equivalence does not prove the signs all-order.

## Carry-forward status

```text
RATIO_BOUND_EQUIVALENCE_DERIVED
RATIO_ROUTE_REPACKAGES_SCHUR_POSITIVITY_UNDER_ALPHA_POSITIVE
POST_TRANSITION_SIGN_THEOREMS_OPEN
```
