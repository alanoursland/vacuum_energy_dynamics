#!/usr/bin/env python3
"""
make_12_directional_selector_tensor_gate_status.py

Summarize directional interval selector proofs 7-11.

Output:
    12_directional_selector_tensor_gate_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "7_general_axis_pair_probe_sufficiency.md",
    "8_local_frame_covariance.md",
    "9_nonnull_scale_calibration.md",
    "10_boundary_tangent_normal_completion.md",
    "11_boundary_source_full_tensor_coupling.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Interval Directional Probe Origin 12: Tensor Gate Status

## Purpose

This report summarizes the second directional interval selector batch.

## Proofs Completed

Proof `7` validates that axis-plus-pair probes are sufficient in finite
dimensions:

```text
h_ii = Q(e_i)
h_ij = (Q(e_i+e_j)-Q(e_i)-Q(e_j))/2.
```

Proof `8` validates local frame covariance:

```text
H' = P^T H P
y^T H' y = (Py)^T H(Py).
```

Proof `9` validates that one non-null interval calibration fixes conformal
scale:

```text
Q(1,0) = measured -> c = -measured.
```

Proof `10` validates the boundary split:

```text
tangent probes -> h_ab
tangent + normal/mixed probes -> full boundary bulk split.
```

Proof `11` validates that source/action coupling must use full tensor data to
see shear:

```text
T^ab delta h_ab sees shear;
tau tr(delta h) does not.
```

## Current Result

The tensor-data gate is now algebraically closed:

```text
enough local directional probes
  -> symmetric bilinear form
  -> correct frame covariance
  -> interval scale when calibrated
  -> induced boundary metric from tangent probes
  -> full-tensor boundary/source coupling can use the data.
```

## Remaining Gap

This does not yet prove that the vacuum physically supplies those probes.

The next selector-level target is the origin question:

```text
What in the vacuum ontology provides local directional comparisons and a
non-null scale calibration?
```

If that origin is supplied, this folder can hand a concrete tensor-boundary
data source back to `vacuum_action_origin`.
"""

out = base / "12_directional_selector_tensor_gate_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Directional selector tensor gate status validated.")
print(f"Wrote {out.resolve()}")

