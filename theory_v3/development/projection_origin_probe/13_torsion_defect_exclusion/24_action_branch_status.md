# Torsion Defect Exclusion 24: Action Branch Status

## Purpose

This report summarizes the fourth torsion selector proof batch.

## Proofs Completed

Proof `19` validates the zero-contorsion branch:

```text
tau = 0, J = 0 -> L_total = L_EH.
```

Proof `20` validates the torsion-extended branch:

```text
L_reduced = L_EH - J^2/(48 mu).
```

Proof `21` validates that torsion boundary/current terms require explicit
boundary conditions or source routing.

Proof `22` validates that scalar projection boundary defects cannot silently
absorb torsion boundary data.

Proof `23` validates the reduced action branch table.

## Current Result

The action branch is now explicit:

```text
K = 0 and J_total = 0:
  Levi-Civita / Einstein-Hilbert branch.

K sourced:
  torsion-extended branch with source correction and boundary/current gates.

K excluded:
  EH branch is recovered only if all torsion source routes are absent or
  structurally canceled.
```

## Remaining Gap

The next and final batch should close the selector:

```text
state the sufficient no-spin/no-defect/no-aux condition;
prove positive torsion stiffness minimizes at tau = 0 under that condition;
show hidden source failure explicitly;
classify surviving torsion as a new field;
close the folder.
```
