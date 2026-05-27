# Radial Boundary Field Bridge 38: Admissibility Defect as Boundary Charge

## Purpose

This report validates the conceptual bridge from the one-dimensional
regularity/admissibility result to the radial boundary-field interpretation.

The core idea is:

```text
zero endpoint obstruction -> admissible regular solution
nonzero endpoint obstruction -> controlled boundary flux / charge
```

## Validated Checks

- 1D flux derivative equals source under -u''=F: passed
- balanced polynomial has zero total source: passed
- unbalanced source total: passed
- 3D radial conserved flux: passed
- 3D flux derivative vanishes in source-free exterior: passed

## 1D Transformed Problem

The regularity-admissibility ladder used:

```text
-u'' = F
```

with `F=aS`.

Define the 1D flux:

```text
J = -u'.
```

Then:

```text
J' = F.
```

Integrating over the domain gives:

```text
J(1)-J(0) = integral_0^1 F dx.
```

The first admissibility condition:

```text
integral_0^1 F dx = 0
```

is therefore the zero-net-flux case.

## Boundary-Charge Reading

If the first admissibility integral is not zero, the obstruction can be
recorded as an endpoint flux instead of treated only as a failure:

```text
Q_endpoint = integral F dx.
```

That is the mathematical move needed for the field-equation bridge.

## 3D Radial Exterior

In the 3D exterior source-free region, the radial flux is:

```text
Q = -4*pi*r^2*u'(r).
```

For:

```text
u(r) = Q/(4*pi*r),
```

SymPy verifies:

```text
Q = -4*pi*r^2*u'(r)
dQ/dr = 0.
```

So the same structural object that appeared as an endpoint obstruction in the
1D regularity problem becomes a conserved boundary charge in the 3D radial
field problem.

## Interpretation

The 1D proof said:

```text
regularity requires canceling the net source obstruction.
```

The radial bridge says:

```text
a mass-like boundary constraint is precisely a controlled nonzero obstruction,
carried as conserved exterior flux.
```

This is the first step toward field equations:

```text
admissibility defect
  -> boundary charge
  -> source-free exterior equation
  -> harmonic potential
  -> inverse-square field strength.
```
