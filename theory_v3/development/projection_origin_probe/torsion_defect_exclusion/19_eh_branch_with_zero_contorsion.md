# Torsion Defect Exclusion 19: EH Branch With Zero Contorsion

## Purpose

This proof validates the reduced action branch where contorsion is absent.

## Validated Checks

- zero contorsion gives zero torsion norm: passed
- zero torsion source and zero contorsion reduce the action to `L_EH`: passed
- torsion variation vanishes on the no-source zero-contorsion branch: passed

## Reduced Model

Use:

```text
L_total = L_EH + (mu/2) T^2 - J tau
T^2 = 24 tau^2.
```

So:

```text
L_total = -J*tau + L_EH + 12*mu*tau**2.
```

On the branch:

```text
tau = 0
J = 0
```

Sympy verifies:

```text
L_total = L_EH
dL_total/dtau = 0.
```

## Interpretation

The pure Einstein-Hilbert branch is recovered when the contorsion/torsion mode
is absent and no torsion source is present. This is the clean EH selector
inside the reduced torsion model.
