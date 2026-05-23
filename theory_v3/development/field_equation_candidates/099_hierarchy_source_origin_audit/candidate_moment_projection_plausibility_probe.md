# candidate_moment_projection_plausibility_probe — Analysis Note

## Result

`candidate_moment_projection_plausibility_probe.py` tests whether `beta_moment(s)` has a beta-type moment-integral representation.

It defines:

```text
I_s = ∫_0^1 x^(2s) (1-x^2)^4 dx.
```

SymPy evaluates:

```text
I_s
=
384 / (32s^5 + 400s^4 + 1840s^3 + 3800s^2 + 3378s + 945).
```

The target is:

```text
beta_moment(s)
=
768 / [(2s+1)(2s+3)(2s+5)(2s+7)(2s+9)].
```

The script verifies:

```text
target / (2 I_s) = 1
sample ratios = [1, 1, 1, 1, 1, 1, 1]
sample integral check failures = []
```

So:

```text
beta_moment(s) = 2 ∫_0^1 x^(2s) (1-x^2)^4 dx.
```

## Interpretation

This is the strongest positive result of Group 099.

It shows that the moment-like appearance is not superficial. The `beta_moment` sequence has a clean beta-integral representation with weight:

```text
(1-x^2)^4
```

on `[0,1]`.

That gives a concrete next derivation target:

```text
Find a residual/projection problem whose weighted moments produce A[k,j].
```

The shifted terms:

```text
beta_moment(k+j)
beta_moment(k+j-1)
```

now suggest integrals involving powers such as:

```text
x^(2k+2j)
x^(2k+2j-2)
```

and a row-dependent coefficient:

```text
(2k-1)/(2k+3).
```

This is a real clue. It does not make `A_N` physical yet, but it gives the next group something specific to reconstruct.

## What Changed

The origin status improves from:

```text
moment-like by formula shape
```

to:

```text
moment-like by explicit beta-integral representation.
```

## What Did Not Change

The physical residual, basis functions, source vector, and boundary conditions remain missing.

The integral identity is not a field equation.

## Carry-forward status

```text
BETA_MOMENT_INTEGRAL_STRUCTURE_SUPPORTED
BETA_MOMENT_EQUALS_2_WEIGHTED_EVEN_MOMENT
WEIGHT_FUNCTION_CANDIDATE_IDENTIFIED
MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
PHYSICAL_RESIDUAL_NOT_DERIVED
SOURCE_VECTOR_NOT_DERIVED
BOUNDARY_CONDITIONS_NOT_DERIVED
```
