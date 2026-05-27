# Einstein-Hilbert Origin Test 118: Conformal EH Strain Split

## Purpose

This report validates a controlled conformal-sector version of the
Einstein-Hilbert boundary/strain split.

For:

```text
g_ab = exp(2s) delta_ab,
```

the EH density can be written as:

```text
sqrt(g)R = boundary divergence + first-derivative strain density.
```

## Validated Checks

- conformal EH boundary plus strain split: passed
- four-dimensional conformal strain coefficient: passed
- two-dimensional conformal EH has no bulk strain: passed

## Conformal Split

Using the conformal transformation formula:

```text
sqrt(g)R =
  exp((D-2)s)[
    -2(D-1)Delta s
    -(D-1)(D-2)|grad s|^2
  ],
```

SymPy verifies:

```text
sqrt(g)R
  - [-2(D-1) div(exp((D-2)s) grad s)]
  =
  (D-1)(D-2) exp((D-2)s)|grad s|^2.
```

In four dimensions:

```text
bulk strain = 6 exp(2s)|grad s|^2.
```

In two dimensions:

```text
bulk strain = 0.
```

## Interpretation

This is a compact nonlinear test of the idea that EH is connection-strain plus
boundary bookkeeping. The second-derivative curvature density becomes a
first-derivative strain density after the appropriate boundary divergence is
separated.
