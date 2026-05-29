#!/usr/bin/env python3
"""
make_15_polarization_selector_status.py

Summarize the polarization selector gate.

Output:
    15_polarization_selector_status.md
"""

from pathlib import Path


base = Path(__file__).resolve().parent
required = [
    "11_symmetric_metric_component_count.md",
    "12_diffeomorphism_gauge_reduction_count.md",
    "13_two_polarization_selector.md",
    "14_scalar_and_vector_mode_mismatch.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Dimension Selector 15: Polarization Selector Status

## Status

The polarization gate is closed conditionally.

## What Was Proved

- a symmetric rank-2 field has `D(D+1)/2` components
- the standard massless spin-2 reduction gives `D(D-3)/2` propagating degrees
  of freedom
- two spin-2 polarizations select `D=4` among positive dimensions
- scalar/vector branches are not equivalent to the symmetric metric branch by
  degree count alone

## What Was Not Proved

The projection-origin algebra does not independently force a massless spin-2
metric field. This gate applies once the weak-field GR lift is adopted as the
target branch.

## Gate Result

```text
local massless spin-2 lift
+ two polarizations
=> D = 4.
```

This is an independent selector that agrees with the flux-plus-clock chain.
"""

out = base / "15_polarization_selector_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Polarization selector status report validated.")
print(f"Wrote {out}")

