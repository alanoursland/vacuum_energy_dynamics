#!/usr/bin/env python3
"""
make_45_eh_ghy_normalization_status.py

Summarize vacuum-action-origin proofs 40-44.

Output:
    45_eh_ghy_normalization_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "40_eh_ghy_prefactor_to_a_flux.md",
    "41_induced_metric_boundary_variation_components.md",
    "42_trace_traceless_boundary_decomposition.md",
    "43_conformal_trace_sector_prefactor.md",
    "44_projection_boundary_current_roles.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Action Origin: EH/GHY Normalization Status After Proofs 40-44

## Purpose

This report summarizes the EH/GHY boundary-normalization batch.

The target was to connect the weak A-sector source normalization to the
boundary-action normalization, while keeping the projection/admissibility
boundary current in its correct role.

## Proofs Completed

Proof `40` validates:

```text
alpha_A = 8*pi*G/c^2
K = 1/(2 alpha_A) = c^2/(16*pi*G).
```

Thus the weak boundary normalization imported from the source gate matches the
reduced EH/GHY prefactor convention.

Proof `41` validates that nonlinear boundary variation is componentwise in the
induced metric:

```text
P_ij = S_ij.
```

A scalar trace source cannot supply off-diagonal/shear boundary variation.

Proof `42` validates the trace/traceless decomposition:

```text
H = (tr H/3)I + H_T
tr H_T = 0.
```

Scalar trace functionals are blind to traceless boundary data.

Proof `43` validates the conformal trace-sector prefactor:

```text
D=4 conformal boundary flux coefficient = -6
K_EH*(-6) = -3c^2/(8*pi*G).
```

This is a trace-variable coefficient and requires an explicit map to the
reduced A variable.

Proof `44` validates the projection boundary current roles:

```text
diagnostic -> no induced-metric variation;
promoted scalar current -> trace-sector variation;
count-once partition -> allowed only if explicit;
extra independent copy -> forbidden.
```

## Current Result

The normalization bridge is now sharper:

```text
source-origin weak boundary normalization
  -> K=c^2/(16*pi*G)
  -> reduced EH/GHY prefactor convention.
```

The projection/admissibility boundary current still does not become the full
nonlinear GHY term. Its allowed roles remain:

```text
scalar trace-sector seed;
auxiliary diagnostic;
explicit trace boundary field;
count-once partition term if a partition theorem is supplied.
```

## Remaining Gap

The next proof target is no longer the weak normalization. It is the nonlinear
boundary completion:

```text
derive, not merely match, the full tensor GHY boundary variation from vacuum
interval/comparison structure.
```

For the projection ladder specifically, the next honest question is:

```text
does the ladder produce tensor boundary data beyond the scalar trace sector?
```

If not, it remains auxiliary to the nonlinear EH/GHY action.
"""

out = base / "45_eh_ghy_normalization_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("EH/GHY normalization status validated.")
print(f"Wrote {out.resolve()}")
