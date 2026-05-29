#!/usr/bin/env python3
"""
make_18_connection_split_status.py

Summarize torsion_defect_exclusion proofs 13-17.

Output:
    18_connection_split_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "13_metric_compatibility_does_not_remove_torsion.md",
    "14_levi_civita_uniqueness_requires_torsion_free.md",
    "15_contorsion_decomposition_gate.md",
    "16_symmetric_interval_blind_to_antisymmetric_connection.md",
    "17_geodesic_autoparallel_split_gate.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Torsion Defect Exclusion 18: Connection Split Status

## Purpose

This report summarizes the third torsion selector proof batch.

## Proofs Completed

Proof `13` validates that metric compatibility does not remove torsion:

```text
Gamma^a_bc = tau epsilon_abc
```

is metric-compatible for the flat metric but has nonzero torsion.

Proof `14` validates the positive Levi-Civita selector:

```text
metric compatibility + torsion-free -> unique Levi-Civita connection.
```

Proof `15` validates the contorsion split:

```text
Gamma = LeviCivita + K
T^a_bc = K^a_bc - K^a_cb.
```

Proof `16` validates that symmetric interval probes are blind to antisymmetric
connection slots:

```text
v^T A v = 0 when A_ij = -A_ji.
```

Proof `17` validates that velocity-squared connection contraction sees the
lower-pair symmetric slot and can miss a purely antisymmetric torsion slot.

## Current Result

The connection split is now explicit:

```text
metric data
  -> symmetric interval/Hessian branch;

metric compatibility
  -> preserves metric data but does not remove torsion;

torsion-free condition
  -> selects Levi-Civita;

contorsion K
  -> carries the torsion branch if not excluded.
```

## Remaining Gap

The next batch must decide the action branch:

```text
K = 0:
  pure Levi-Civita / Einstein-Hilbert branch.

K != 0:
  torsion-extended action branch with its own source/current conditions.
```

The scalar projection ladder and symmetric interval branch cannot silently
absorb the torsion branch.
"""

out = base / "18_connection_split_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Connection split status validated.")
print(f"Wrote {out.resolve()}")

