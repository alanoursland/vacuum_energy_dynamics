# Torsion Defect Exclusion 23: Action Branch Decision Table

## Purpose

This proof records the reduced action branch table.

## Validated Checks

- no-source zero-contorsion branch reduces to `L_EH`: passed
- sourced torsion branch reduces to `L_EH - J_total^2/(48 mu)`: passed
- nonzero source makes `tau = 0` nonstationary: passed
- excluding all source routes gives `J_total = 0`: passed

## Reduced Action

Use:

```text
J_total = J_spin + J_defect + J_aux
L_total = L_EH + 12 mu tau^2 - J_total tau.
```

The variation is:

```text
dL_total/dtau = -J_aux - J_defect - J_spin + 24*mu*tau.
```

## Branch Table

```text
EH branch:
  J_spin = J_defect = J_aux = 0
  tau = 0
  L_total = L_EH

sourced torsion branch:
  tau = J_total/(24 mu)
  L_reduced = -(J_aux**2 + 2*J_aux*J_defect + 2*J_aux*J_spin + J_defect**2 + 2*J_defect*J_spin + J_spin**2 - 48*L_EH*mu)/(48*mu)

invalid hidden-source EH branch:
  tau = 0
  residual = -J_aux - J_defect - J_spin
```

## Interpretation

There are only three honest choices:

```text
exclude torsion sources and recover EH;
route torsion as a sourced extension;
prove structural cancellation.
```

Leaving a nonzero source while calling the branch EH is inconsistent.
