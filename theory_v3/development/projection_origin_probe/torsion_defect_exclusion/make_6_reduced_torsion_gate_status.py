#!/usr/bin/env python3
"""
make_6_reduced_torsion_gate_status.py

Summarize torsion_defect_exclusion proofs 1-5.

Output:
    6_reduced_torsion_gate_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "1_torsion_norm_and_source_variation.md",
    "2_torsion_free_stationarity_iff_no_source.md",
    "3_integrate_out_torsion_source_correction.md",
    "4_symmetric_interval_cannot_source_torsion.md",
    "5_scalar_projection_cannot_source_torsion.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Torsion Defect Exclusion 6: Reduced Torsion Gate Status

## Purpose

This report summarizes the first torsion selector proof batch.

## Proofs Completed

Proof `1` validates the reduced torsion norm and variation:

```text
T^a_bc T_a^bc = 24 tau^2
dE_T/dtau = 24 mu tau - J.
```

Proof `2` validates the no-source stationarity condition:

```text
tau = 0 is stationary iff J_total = 0.
```

Proof `3` validates the integrate-out correction:

```text
E_reduced = -J_total^2/(48 mu).
```

Proof `4` validates that symmetric interval data has no antisymmetric torsion
source slot:

```text
H_ij A_ij = 0 when H_ij = H_ji and A_ij = -A_ji.
```

Proof `5` validates that scalar projection data cannot source torsion without
an additional oriented/antisymmetric carrier.

## Current Result

The reduced torsion gate is now local to this folder:

```text
torsion-free EH branch
  requires J_total = 0.
```

The existing scalar and symmetric metric channels do not by themselves supply
`J_total`.

## Remaining Gap

This does not yet prove:

```text
J_total = 0.
```

It proves only that `J_total` cannot be hidden inside the already-established
scalar projection or symmetric interval channels.

The next batch must classify possible torsion source routes:

```text
spin channel;
rotational/holonomy defect channel;
auxiliary torsion channel;
structural cancellation.
```
"""

out = base / "6_reduced_torsion_gate_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Reduced torsion gate status validated.")
print(f"Wrote {out.resolve()}")

