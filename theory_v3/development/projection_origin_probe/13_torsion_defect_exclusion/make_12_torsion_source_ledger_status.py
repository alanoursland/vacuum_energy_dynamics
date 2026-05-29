#!/usr/bin/env python3
"""
make_12_torsion_source_ledger_status.py

Summarize torsion_defect_exclusion proofs 7-11.

Output:
    12_torsion_source_ledger_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "7_torsion_source_ledger_decomposition.md",
    "8_spin_current_requires_antisymmetric_matter_channel.md",
    "9_rotational_defect_requires_holonomy_channel.md",
    "10_auxiliary_torsion_routing_gate.md",
    "11_cancellation_structural_vs_tuned.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Torsion Defect Exclusion 12: Torsion Source Ledger Status

## Purpose

This report summarizes the second torsion selector proof batch.

## Proofs Completed

Proof `7` validates the torsion source ledger:

```text
J_total = J_spin + J_defect + J_aux.
```

Proof `8` validates that spin-like torsion sources require antisymmetric or
internal-angular data.

Proof `9` validates that rotational defect sources require a holonomy or
closure-failure channel.

Proof `10` validates that auxiliary torsion routing must be explicit:

```text
J_aux = eta s.
```

Proof `11` separates structural cancellation from unexplained parameter tuning.

## Current Result

The possible torsion source routes are now classified:

```text
J_spin:
  requires antisymmetric/internal-angular matter data.

J_defect:
  requires rotational holonomy or closure-failure data.

J_aux:
  requires an explicit auxiliary carrier.

J_total = 0:
  requires source absence or structural cancellation.
```

## Remaining Gap

This batch still does not prove `J_total = 0`.

It proves the narrower source-safety result:

```text
torsion source cannot be hidden inside scalar projection data,
symmetric interval data,
or unexplained cancellation.
```

The next batch should split metric data from connection torsion:

```text
metric compatibility does not remove torsion;
Levi-Civita uniqueness requires torsion-free;
contorsion carries the torsion branch;
symmetric intervals are blind to the antisymmetric connection slot.
```
"""

out = base / "12_torsion_source_ledger_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Torsion source ledger status validated.")
print(f"Wrote {out.resolve()}")

