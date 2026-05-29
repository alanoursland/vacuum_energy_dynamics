#!/usr/bin/env python3
"""
make_57_remaining_physical_selectors_status.py

Summarize vacuum-action-origin proofs 52-56.

Output:
    57_remaining_physical_selectors_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "52_directional_interval_boundary_tensor_data.md",
    "53_shear_probe_requirement.md",
    "54_torsion_source_absence_audit.md",
    "55_dimensionality_selector_consistency.md",
    "56_lambda_asymptotic_flatness_gate.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Action Origin: Remaining Physical Selectors Status After Proofs 52-56

## Purpose

This report summarizes the first remaining-selector audit after the scalar
projection ladder failed to produce full tensor GHY boundary data.

## Proofs Completed

Proof `52` validates that directional interval probes can recover tensor
boundary components:

```text
h12 = (Q(e1+e2)-Q(e1)-Q(e2))/2.
```

Proof `53` validates that shear requires directional probes:

```text
tr(qI+S) = 2q
Q(e1)-Q(e2) = 2s.
```

Proof `54` validates torsion-source absence:

```text
tau = J_total/(24 mu)
```

so torsion-free stationarity requires:

```text
J_total = 0.
```

Proof `55` validates consistency of the dimension selectors:

```text
inverse-square flux -> n=3
two spin-2 polarizations -> D=4
4D Lovelock -> EH unique dynamical curvature term beyond Lambda.
```

Proof `56` validates the Lambda/asymptotic-flatness branch:

```text
Phi = -GM/r - lambda r^2/6
-Phi' = -GM/r^2 + lambda r/3.
```

The pure inverse-square branch requires `lambda=0`.

## Current Result

The action-origin chain now has a clean selector map:

```text
tensor boundary completion:
  needs directional interval/shear data, not scalar projection rows alone.

torsion-free EH branch:
  needs absence or cancellation of torsion sources.

3+1 dimension:
  is consistently selected by inverse-square flux, spin-2 polarizations, and
  the 4D Lovelock gate, but not yet derived from ontology.

Lambda:
  zero Lambda is the asymptotically-flat inverse-square branch; nonzero Lambda
  is a separate vacuum baseline branch.
```

## Remaining Gap

The remaining work is now physical selector derivation, not algebraic cleanup.

Possible next folders:

```text
vacuum_interval_directional_probe_origin
torsion_defect_exclusion
vacuum_dimension_selector
lambda_relaxation_mechanism
```

Within `vacuum_action_origin`, further scripts should only be added if they
attack one of those selectors directly.
"""

out = base / "57_remaining_physical_selectors_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Remaining physical selectors status validated.")
print(f"Wrote {out.resolve()}")
