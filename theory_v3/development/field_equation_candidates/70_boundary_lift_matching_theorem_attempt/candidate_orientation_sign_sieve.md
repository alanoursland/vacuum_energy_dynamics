# candidate_orientation_sign_sieve — Result Note

## Result

The script solves the orientation sign requirement under the common-generator ansatz.

Residual:

```text
-B*(sigma - 1) + L_bulk + L_gauge
```

With:

```text
L_bulk = 0
L_gauge = 0
```

the strict residual is:

```text
B*(1 - sigma)
```

Solving:

```text
B*(1 - sigma) = 0
```

gives:

```text
sigma = 1
```

## Main Findings

The required orientation sign is now explicit:

```text
sigma = 1
```

This means the lift-boundary term must anti-match the boundary generator with the exact opposite sign.

The script correctly rejects:

```text
choosing sigma=1 by convenience.
```

The sign must be derived from boundary orientation / covariant-lift convention.

## Boundary

The sign requirement is derived as a compatibility condition, not as an orientation theorem.

## Steering Consequence

Proceed to component coefficient matching. Even if `sigma=1`, the component-level coefficients must be forced by common geometry rather than chosen.
