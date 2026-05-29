# Einstein-Hilbert Origin Test 109: Cosmological Constant Gate

## Purpose

This report tests the Newtonian-sector effect of the allowed Lovelock `p=0`
term.

The cosmological constant is allowed by the Lovelock gate, but it is not part
of the asymptotically flat scalar boundary-flux bridge unless it is set to
zero or treated as a separate background branch.

## Validated Checks

- off-source mass potential is harmonic: passed
- cosmological potential solves modified vacuum Poisson equation: passed
- combined exterior equation: passed
- radial acceleration with Lambda: passed
- scalar bridge recovered at Lambda equals zero: passed
- positive Lambda potential is not asymptotically flat: passed

## Radial Potentials

For the mass term:

```text
Phi_M = -GM/r,
```

SymPy verifies off source:

```text
Delta Phi_M = 0.
```

For the cosmological term:

```text
Phi_Lambda = -Lambda r^2/6,
```

SymPy verifies:

```text
Delta Phi_Lambda = -Lambda.
```

So:

```text
Phi = -GM/r - Lambda r^2/6
```

satisfies:

```text
Delta Phi = -Lambda
```

outside localized matter.

## Acceleration

The radial acceleration is:

```text
-dPhi/dr = -GM/r^2 + Lambda r/3.
```

Positive `Lambda` adds an outward term and destroys asymptotic flatness.

## Interpretation

The cosmological term is a legitimate four-dimensional Lovelock option, but
it is a separate vacuum-background parameter. The scalar boundary-flux bridge
selects the `Lambda=0` asymptotically flat sector unless a nonzero vacuum
curvature background is independently supplied.
