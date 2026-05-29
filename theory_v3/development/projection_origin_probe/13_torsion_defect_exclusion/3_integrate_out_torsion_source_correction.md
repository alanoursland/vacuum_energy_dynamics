# Torsion Defect Exclusion 3: Integrating Out Torsion Source Correction

## Purpose

This proof shows what happens if a torsion source survives.

The result is not pure Einstein-Hilbert. The torsion sector leaves a reduced
source correction.

## Validated Checks

- stationary torsion is substituted into the torsion energy: passed
- reduced energy is `-J_total^2/(48 mu)`: passed
- no-source branch has zero reduced torsion correction: passed
- nonzero source changes the reduced action: passed

## Computation

Use:

```text
E_T = 12 mu tau^2 - J_total tau.
```

At:

```text
tau = J_total/(24 mu),
```

Sympy gives:

```text
E_reduced = -J_total**2/(48*mu).
```

When:

```text
J_total = 0,
tau = 0,
```

the torsion correction is:

```text
0.
```

## Interpretation

If a torsion source remains, torsion is not a harmless eliminated variable. It
produces a real source-dependent correction. The pure EH branch is recovered
only on the no-source branch or under a structural cancellation.
