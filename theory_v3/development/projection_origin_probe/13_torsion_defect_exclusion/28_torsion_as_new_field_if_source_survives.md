# Torsion Defect Exclusion 28: Torsion As New Field If Source Survives

## Purpose

This proof records the honest classification if a torsion source survives.

Torsion becomes an additional field branch with its own source and stiffness.

## Validated Checks

- surviving source gives a torsion field equation: passed
- stationary torsion responds to source strength: passed
- stationary torsion responds to torsion stiffness: passed
- reduced action contains an explicit source correction: passed

## Field Branch

Use:

```text
L_total = L_EH + 12 mu tau^2 - J_total tau.
```

The torsion equation is:

```text
-J_total + 24*mu*tau = 0.
```

So:

```text
tau = J_total/(24*mu).
```

Its sensitivities are:

```text
d tau / dJ_total = 1/(24*mu)
d tau / dmu      = -J_total/(24*mu**2).
```

The reduced action becomes:

```text
-(J_total**2 - 48*L_EH*mu)/(48*mu).
```

## Interpretation

If `J_total` survives, torsion is not EH data. It is a separate field branch
with a source ledger, stiffness, boundary/current conditions, and reduced
action correction.
