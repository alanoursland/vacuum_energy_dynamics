# Vacuum Action Origin 17: Conformal Boundary Flux to Metric Boundary

## Purpose

This report strengthens the boundary-flux bridge in a metric sector.

For a conformal metric:

```text
g_ab = exp(2s) eta_ab,
```

the curvature density separates into:

```text
boundary flux + first-derivative metric strain.
```

## Validated Checks

- conformal metric boundary plus strain split: passed
- four-dimensional boundary flux density: passed
- four-dimensional bulk conformal strain: passed
- two-dimensional bulk conformal strain vanishes: passed
- linearized D4 flux momentum coefficient: passed

## One-Dimensional Conformal Sector

The conformal curvature density along one coordinate has the form:

```text
sqrt(g)R =
  -2(D-1) exp((D-2)s) s''
  -(D-1)(D-2) exp((D-2)s)(s')^2.
```

Define the boundary flux density:

```text
F_boundary = -2(D-1) exp((D-2)s) s'.
```

SymPy verifies:

```text
sqrt(g)R - dF_boundary/dx
  =
  (D-1)(D-2) exp((D-2)s)(s')^2.
```

## Four-Dimensional Case

For `D=4`:

```text
F_boundary = -6 exp(2s) s'
bulk strain = 6 exp(2s)(s')^2.
```

The linearized boundary momentum coefficient is:

```text
-6.
```

## Interpretation

This is the conformal metric analogue of the scalar boundary-flux variational
source. The EH/GHY boundary structure is not an unrelated add-on: in this
sector it is exactly the boundary-flux completion of metric strain.
