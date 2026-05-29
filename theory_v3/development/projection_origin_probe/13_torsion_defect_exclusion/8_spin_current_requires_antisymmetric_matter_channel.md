# Torsion Defect Exclusion 8: Spin Current Requires Antisymmetric Matter Channel

## Purpose

This proof checks the index structure of a spin-like torsion source.

Symmetric metric stress data does not by itself provide a spin/torsion source.
An antisymmetric or internal-angular carrier is required.

## Validated Checks

- symmetric tensor contraction with spin-like antisymmetric tensor vanishes: passed
- antisymmetric carrier pairs nontrivially with spin-like source: passed

## Algebra

Let `T_sym` be symmetric and let `Spin` be antisymmetric. Sympy verifies:

```text
sum_ij T_sym_ij Spin_ij = 0.
```

With an antisymmetric carrier `B`, the pairing is:

```text
sum_ij Spin_ij B_ij = 2*(bx*sx + by*sy + bz*sz).
```

## Interpretation

A spin-like torsion source requires data with antisymmetric/internal-angular
index structure. It cannot be hidden inside the symmetric metric stress or
directional interval Hessian channel.
