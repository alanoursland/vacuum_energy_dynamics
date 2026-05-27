# Vacuum Action Origin 9: Torsion Defect Mode Action Gate

## Purpose

This report tests what torsion means in an action-origin language.

The result is not that torsion must exist. The result is sharper:

```text
torsion-free is a real physical gate.
```

If torsion is allowed, it behaves as an additional defect/source mode.

## Validated Checks

- totally antisymmetric torsion norm: passed
- torsion no-source variation: passed
- positive torsion stiffness with no source sets torsion to zero: passed
- torsion source variation: passed
- torsion source produces algebraic defect mode: passed
- integrated-out torsion source energy: passed

## Torsion Sector

Use a metric-compatible toy connection:

```text
Gamma^a_bc = tau epsilon_abc.
```

Its torsion is:

```text
T^a_bc = Gamma^a_bc - Gamma^a_cb.
```

SymPy verifies:

```text
T^a_bc T_a^bc = 24 tau^2.
```

## No-Source Gate

For a positive torsion stiffness:

```text
E_T = (mu/2) T^2,
```

SymPy verifies:

```text
dE_T/dtau = 24 mu tau.
```

So without a torsion source:

```text
tau = 0.
```

## Defect Source

With a source-like defect coupling:

```text
E_T = (mu/2)T^2 - J tau,
```

SymPy verifies:

```text
tau = J/(24 mu).
```

Integrating out torsion gives:

```text
E_reduced = -J^2/(48 mu).
```

## Interpretation

Pure Einstein-Hilbert corresponds to the branch where no independent torsion
defect mode is present. If the vacuum ontology has rotational, spin-like, or
defect-like response variables, then torsion is a real extension gate rather
than a harmless convention.
