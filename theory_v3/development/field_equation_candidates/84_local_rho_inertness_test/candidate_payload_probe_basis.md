# candidate_payload_probe_basis — Analysis Note

## Result

`candidate_payload_probe_basis.py` defines the low-order payload probe basis:

```text
P0 = 1
P1 = y
P2 = y^2
```

The corresponding moments are:

```text
M_n = ∫ y^n rho dy
```

with interpretations:

```text
M0: global/source neutrality
M1: dipole/gradient sensitivity
M2: quadratic/width/curvature sensitivity
```

## Interpretation

This is a good minimal probe basis. It does not pretend to be complete, but it tests the first three things that local residuals usually leak into:

```text
net charge;
dipole asymmetry;
quadratic width/curvature-like response.
```

The choice is especially appropriate because Group 83 introduced a skew proportional to `ell/R`. A skewed profile can easily preserve total neutrality while generating dipole sensitivity. So `P1 = y` is the correct probe to test whether the geometry-paid skew creates local asymmetry.

`P2 = y^2` is also important because it tests an even local width/curvature payload that a linear skew might not control.

## What Changed

The vague phrase:

```text
payload inertness must be tested
```

has become a concrete finite test:

```text
M0, M1, M2.
```

This is progress because it gives future groups a clear payload obstruction language.

## What Did Not Change

The script correctly states that this is not a complete physical basis. Passing these probes would not prove full inertness.

But failing these probes is meaningful. A nonzero `M1` or `M2` means the local remainder is visible to simple reduced payload channels.

## Steering Consequence

The next result should be judged harshly:

```text
M0 = 0 alone is not enough.
```

Finite-mode inertness would require at least:

```text
M0 = M1 = M2 = 0
```

in this reduced test.
