#!/usr/bin/env python3
"""
make_24_action_branch_status.py

Summarize torsion_defect_exclusion proofs 19-23.

Output:
    24_action_branch_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "19_eh_branch_with_zero_contorsion.md",
    "20_torsion_extended_action_branch.md",
    "21_torsion_boundary_current_gate.md",
    "22_no_hidden_torsion_in_projection_boundary_data.md",
    "23_action_branch_decision_table.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Torsion Defect Exclusion 24: Action Branch Status

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
"""

out = base / "24_action_branch_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Action branch status validated.")
print(f"Wrote {out.resolve()}")

