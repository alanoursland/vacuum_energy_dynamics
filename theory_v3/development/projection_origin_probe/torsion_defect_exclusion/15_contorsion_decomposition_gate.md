# Torsion Defect Exclusion 15: Contorsion Decomposition Gate

## Purpose

This proof records where the torsion branch lives.

If:

```text
Gamma = LeviCivita + K,
```

then torsion is carried by the contorsion `K`.

## Validated Checks

- torsion from `Gamma` equals torsion from `K`: passed
- flat Levi-Civita branch has no torsion: passed
- nonzero contorsion gives nonzero torsion witness: passed

## Model

Use:

```text
Gamma^a_bc = LC^a_bc + K^a_bc
LC^a_bc = 0
K^a_bc = tau epsilon_abc.
```

Then:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb
       = K^a_bc - K^a_cb.
```

For example:

```text
T^0_12 = 2 tau.
```

## Interpretation

The metric branch and torsion branch are different connection data. Setting
`K = 0` selects the Levi-Civita branch. Keeping `K` requires an explicit
torsion source, stiffness, or field equation.
