# Vacuum Action Origin 54: Torsion Source Absence Audit

## Purpose

This proof restates the torsion-free branch as a source selector.

Torsion-free geometry is not forced by metric compatibility alone. It is
selected when the total torsion source is absent, or when sources cancel by a
separate physical mechanism.

## Validated Checks

- torsion variation is 24*mu*tau-J_total: passed
- stationary torsion is proportional to total torsion source: passed
- torsion-free branch is stationary only when total torsion source vanishes: passed
- torsion-free can be obtained by source absence or exact cancellation: passed
- with no source, positive torsion stiffness minimizes at tau=0: passed

## Torsion Source Ledger

Let:

```text
J_total = J_spin + J_defect + J_aux.
```

Use the reduced torsion energy:

```text
E = 12 mu tau^2 - J_total tau.
```

The variation is:

```text
dE/dtau = 24 mu tau - J_total.
```

So:

```text
tau = J_total/(24 mu).
```

## Torsion-Free Branch

At:

```text
tau = 0,
```

the residual is:

```text
-J_total.
```

Therefore torsion-free stationarity requires:

```text
J_total = 0.
```

## Interpretation

The remaining physical selector is not mathematical. The theory must explain
why spin/defect/auxiliary torsion sources vanish or cancel. Without that, the
natural action branch is torsion-extended rather than pure EH.
