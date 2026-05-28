# Torsion Defect Exclusion 7: Torsion Source Ledger Decomposition

## Purpose

This proof defines the torsion-source ledger used by the rest of the folder.

## Validated Checks

- total torsion source decomposes into spin, defect, and auxiliary routes: passed
- stationary torsion is controlled by the total source: passed
- torsion-free cancellation condition is explicit: passed
- full source absence gives `J_total = 0`: passed

## Ledger

Use:

```text
J_total = J_spin + J_defect + J_aux.
```

The reduced torsion energy is:

```text
E_T = 12 mu tau^2 - J_total tau.
```

The variation is:

```text
dE_T/dtau = -J_aux - J_defect - J_spin + 24*mu*tau.
```

So:

```text
tau = J_total/(24 mu).
```

## Cancellation Condition

The torsion-free branch requires:

```text
J_total = 0.
```

Solving for the auxiliary route gives:

```text
J_aux = -J_spin - J_defect.
```

## Interpretation

This ledger makes the selector explicit. The EH branch is selected by source
absence or structural cancellation, not by relabeling torsion as part of the
metric branch.
