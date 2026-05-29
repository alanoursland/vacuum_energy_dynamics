# Quadratic Response Selector 21: Local Action Quadratic Density Gate

## Purpose

This proof records that the standard local quadratic strain-density branch
assumes a fixed quadratic response structure.

## Computation

For the quadratic density

```text
E2 = 1/2 lambda tr(s)^2 + mu ||s||^2,
```

SymPy computes a strain-independent Hessian:

```text
Hessian(E2) = Matrix([
[lam + 2*mu,    0,        lam],
[         0, 4*mu,          0],
[       lam,    0, lam + 2*mu]])
```

After adding a quartic correction `eps tr(s)^4`, the Hessian drift is:

```text
Matrix([
[12*eps*(s11 + s22)**2, 0, 12*eps*(s11 + s22)**2],
[                    0, 0,                     0],
[12*eps*(s11 + s22)**2, 0, 12*eps*(s11 + s22)**2]])
```

## Interpretation

A local quadratic action density belongs to the metric/Hessian branch. Higher
strain response must be separately justified, suppressed, or routed.
