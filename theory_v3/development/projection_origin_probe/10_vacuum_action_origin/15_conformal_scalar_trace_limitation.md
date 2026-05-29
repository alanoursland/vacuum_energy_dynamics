# Vacuum Action Origin 15: Conformal Scalar Trace Limitation

## Purpose

This report validates why the scalar prototype cannot be the full gravitational
field.

The gate is:

```text
conformal/scalar metric response
  -> trace coupling only
  -> misses traceless and shear stress.
```

## Validated Checks

- traceless source condition: passed
- conformal coupling to traceless source vanishes: passed
- general metric coupling to traceless source: passed
- pure shear source seen by metric shear: passed
- pure shear source missed by conformal response: passed

## Traceless Source

Use a two-dimensional stress tensor with:

```text
T^00 = A
T^11 = A
T^01 = B.
```

With `eta_ab = diag(-1,1)`, its trace is:

```text
eta_ab T^ab = -A + A = 0.
```

## Conformal Coupling

A conformal response has:

```text
h_ab = 2 sigma eta_ab.
```

The source coupling:

```text
1/2 h_ab T^ab
```

vanishes for this traceless source.

## General Metric Coupling

A general metric response gives:

```text
1/2 h_ab T^ab = 1/2 A(h_00+h_11) + B h_01.
```

So shear stress is visible to the metric shear component `h_01`.

## Interpretation

A scalar or conformal response can model the trace sector of metric response.
It cannot encode the full universal coupling required by stress-energy. The
next lift must include traceless/shear metric degrees of freedom.
