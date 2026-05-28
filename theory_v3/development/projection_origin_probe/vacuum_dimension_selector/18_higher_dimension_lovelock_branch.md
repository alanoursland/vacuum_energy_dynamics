# Vacuum Dimension Selector 18: Higher-Dimension Lovelock Branch

## Purpose

This proof checks why dimensions above four are not the same action branch as
the four-dimensional Einstein-Hilbert selector.

## Validated Checks

- in `D=5`, Gauss-Bonnet (`p=2`) is dynamical: passed
- in `D=6`, Gauss-Bonnet remains dynamical and `p=3` is topological: passed
- in `D=7`, the cubic Lovelock term (`p=3`) is dynamical: passed

## Computation

```text
status(D=5, p=2) = dynamical
status(D=6, p=2) = dynamical
status(D=6, p=3) = topological
status(D=7, p=3) = dynamical
```

## Interpretation

Higher-dimensional metric theories have additional local second-order curvature
branches. A higher-dimensional lift is therefore not automatically the same
Einstein-Hilbert branch with extra coordinates; it must explain why those extra
Lovelock terms are absent or suppressed.
