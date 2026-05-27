# Boundary Flux Field Bridge 43: Radial Reduction to Admissibility Defect

## Purpose

This report strengthens the bridge between the earlier one-dimensional
regularity result and the 3D radial boundary-flux model.

It shows that both systems have the same conserved-flux obstruction structure.

## Validated Checks

- radial flux derivative identity: passed
- uniform ball total charge: passed
- exterior flux equals enclosed source: passed
- exterior source-free flux conservation: passed
- 1D flux obstruction identity: passed

## 3D Radial Source Equation

Use the sign convention:

```text
-Delta u = rho.
```

For a radial field:

```text
Delta u = u'' + (2/r)u'.
```

Define enclosed flux/charge:

```text
Q(r) = -4*pi*r^2*u'(r).
```

Then:

```text
Q'(r) = 4*pi*r^2*rho(r).
```

So total enclosed source is exactly the change in radial flux.

## Uniform Ball Audit

For constant density `rho0` inside radius `R`:

```text
Q_total = integral_0^R 4*pi*r^2*rho0 dr
        = 4*pi*rho0*R^3/3.
```

The exterior solution is:

```text
u(r) = Q_total/(4*pi*r).
```

and its exterior flux is:

```text
-4*pi*r^2*u'(r) = Q_total.
```

## 1D Admissibility Analog

The transformed one-dimensional problem had:

```text
-u'' = F.
```

With:

```text
J = -u',
```

one gets:

```text
J' = F.
```

Thus:

```text
integral F dx
```

is the one-dimensional version of total enclosed source/flux.

## Interpretation

The earlier first admissibility condition:

```text
integral F dx = 0
```

is the zero-net-flux sector.

The boundary-field bridge keeps the same obstruction but interprets a controlled
nonzero value as boundary/source charge:

```text
integral F dx != 0
  -> nonzero conserved exterior flux.
```
