# Torsion Defect Exclusion 13: Metric Compatibility Does Not Remove Torsion

## Purpose

This proof reproduces the core connection warning inside the torsion selector
folder.

Metric compatibility does not imply torsion-free.

## Validated Checks

- flat metric compatibility residual vanishes for `Gamma^a_bc = tau epsilon_abc`: passed
- torsion witness `T^0_12 = 2 tau` is nonzero when `tau` is nonzero: passed

## Model

Use flat metric data:

```text
g_ab = delta_ab
```

and connection:

```text
Gamma^a_bc = tau epsilon_abc.
```

Sympy verifies:

```text
nabla_c delta_ab = 0.
```

But:

```text
T^0_12 = Gamma^0_12 - Gamma^0_21 = 2 tau.
```

## Interpretation

Metric compatibility preserves the interval. It does not remove independent
antisymmetric connection structure. The torsion-free condition is an
additional selector.
