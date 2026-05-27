# Einstein-Hilbert Origin Test 103: Palatini Variation Identity

## Purpose

This report validates the Palatini identity for a torsion-free connection on a
controlled 2D symbolic connection. The identity is tensorial; the 2D check keeps
the full component calculation tractable for SymPy.

## Validated Checks

- Palatini identity verified for all 2D components: passed

## Identity

Starting from:

```text
R_ab =
  partial_c Gamma^c_ab
  - partial_b Gamma^c_ac
  + Gamma^c_cd Gamma^d_ab
  - Gamma^c_bd Gamma^d_ac,
```

vary the connection:

```text
Gamma -> Gamma + eps delta Gamma.
```

SymPy verifies:

```text
delta R_ab
  =
  nabla_c(delta Gamma^c_ab)
  - nabla_b(delta Gamma^c_ac).
```

## Interpretation

This is the core variation identity behind the Einstein-Hilbert action. It
shows why varying curvature produces a bulk Einstein term plus boundary
bookkeeping.
