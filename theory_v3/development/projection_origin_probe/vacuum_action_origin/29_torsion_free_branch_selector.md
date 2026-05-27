# Vacuum Action Origin 29: Torsion-Free Branch Selector

## Purpose

This report sharpens the torsion result into a branch selector.

The question is not whether torsion can be written down. It can. The question
is when the pure Einstein-Hilbert branch is selected.

## Validated Checks

- torsion norm: passed
- torsion branch variation: passed
- torsion source solution: passed
- no-source branch sets torsion to zero: passed
- torsion-free residual: passed
- torsion-free branch requires no torsion source: passed
- positive no-source torsion energy: passed

## Torsion Sector

Use the same metric-compatible torsion model:

```text
Gamma^a_bc = tau epsilon_abc
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

SymPy verifies:

```text
T^a_bc T_a^bc = 24 tau^2.
```

With positive stiffness and a possible torsion source:

```text
E_T = (mu/2)T^2 - J tau.
```

The variation is:

```text
dE_T/dtau = 24 mu tau - J.
```

So:

```text
tau = J/(24 mu).
```

## Torsion-Free Branch

If there is no torsion source:

```text
J = 0,
```

then:

```text
tau = 0.
```

Conversely, imposing:

```text
tau = 0
```

leaves the residual:

```text
-J.
```

So the torsion-free branch is stationary only when no torsion source is present.

## Interpretation

Pure Einstein-Hilbert is selected by the no-torsion-source branch. If the
vacuum ontology contains independent spin, rotational defect, or torsion-source
structure, the natural action is no longer pure EH; it moves toward a torsion
extension. This branch point is physical, not algebraic.
