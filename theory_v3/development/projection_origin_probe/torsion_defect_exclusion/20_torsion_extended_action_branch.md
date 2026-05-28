# Torsion Defect Exclusion 20: Torsion-Extended Action Branch

## Purpose

This proof validates the opposite branch from proof `19`.

If torsion is nonzero or sourced, it is an explicit action sector, not a
notation change inside Einstein-Hilbert.

## Validated Checks

- torsion variation is `24 mu tau - J`: passed
- action depends explicitly on torsion source `J`: passed
- action depends explicitly on torsion stiffness `mu`: passed
- integrating out torsion leaves a reduced source correction: passed

## Reduced Action

Use:

```text
L_total = L_EH + 12 mu tau^2 - J tau.
```

The torsion variation is:

```text
dL_total/dtau = -J + 24*mu*tau.
```

The sensitivities are:

```text
dL_total/dJ  = -tau
dL_total/dmu = 12*tau**2.
```

At:

```text
tau = J/(24 mu),
```

the reduced action is:

```text
-(J**2 - 48*L_EH*mu)/(48*mu).
```

## Interpretation

A sourced torsion branch is a real extension. It changes the reduced action by
`-J^2/(48 mu)`. Pure EH is recovered only when this sector is absent, excluded,
or structurally canceled.
