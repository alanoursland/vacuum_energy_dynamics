# Torsion Defect Exclusion 25: No Spin / No Defect / No Aux Condition

## Purpose

This proof states the sufficient no-source condition for the torsion-free EH
branch.

## Validated Checks

- setting spin, defect, and auxiliary torsion sources to zero gives `J_total = 0`: passed
- no-source torsion variation reduces to `24 mu tau`: passed
- no-source stationary torsion is `tau = 0`: passed

## Source Ledger

Use:

```text
J_total = J_spin + J_defect + J_aux.
```

The sufficient condition:

```text
J_spin = 0
J_defect = 0
J_aux = 0
```

gives:

```text
J_total = 0.
```

Then:

```text
dE_T/dtau = 24 mu tau.
```

So:

```text
tau = 0.
```

## Interpretation

This is sufficient, not automatic. The folder has shown that scalar projection
data and symmetric interval data do not themselves supply these sources. Any
independent spin, holonomy, or auxiliary channel must still be ruled out or
routed explicitly.
