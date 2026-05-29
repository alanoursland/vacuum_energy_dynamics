# Vacuum Action Origin 35: Induced Interval Shared Boundary Variable

## Purpose

This proof records the boundary-variable ownership condition needed for the
nonlinear action handoff.

The matter boundary source and the vacuum boundary term must vary the same
induced interval variable.

## Validated Checks

- shared induced interval gives one boundary variation equation: passed
- shared induced interval balances vacuum and matter coefficients: passed
- split induced variables produce separate variation equations: passed
- weak induced interval variation has coefficient 1/2: passed

## Shared Boundary Variable

Let `h` represent a reduced induced interval/metric component on the boundary.
If:

```text
E_boundary = C sqrt(h) - M sqrt(h),
```

then:

```text
dE/dh = (C-M)/(2 sqrt(h)).
```

Stationarity gives:

```text
C = M.
```

## Split Variables

If the vacuum term uses `h_v` and matter uses a different `h_m`:

```text
E_boundary = C sqrt(h_v) - M sqrt(h_m),
```

then the variations are independent. No direct boundary/source balance follows
unless another theorem identifies:

```text
h_v = h_m.
```

## Interpretation

The nonlinear boundary action must use the same induced interval variable that
matter uses for proper time/length. Otherwise the source-origin chain and the
vacuum-action chain do not close on the same degree of freedom.
