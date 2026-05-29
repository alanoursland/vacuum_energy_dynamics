#!/usr/bin/env python3
"""
make_7_source_safety_gate_status.py

Summarize source-safety gate proofs 1-6.

Output:
    7_source_safety_gate_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "1_count_once_incidence_gate.md",
    "2_residual_nonentry_gate.md",
    "3_source_role_purity_gate.md",
    "4_scalar_tail_flux_exclusion.md",
    "5_boundary_current_flux_silence.md",
    "6_compact_support_no_shell_gate.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Source Safety Gate: Status After Proofs 1-6

## Purpose

This folder reconstructs the archived source-safety guardrails as small
symbolic proofs.

It does not promote the projection hierarchy into a field equation. It proves
the bookkeeping and reduced-flux gates that any later source-origin theorem
must satisfy.

## Proofs Completed

Proof `1` validates the count-once trace incidence gate:

```text
i_Bs + i_res = 1.
```

The clean B_s route is:

```text
i_Bs = 1
i_res = 0.
```

Proof `2` validates residual nonentry:

```text
i_res_metric = 0
i_res_source = 0.
```

Proof `3` validates ordinary source role-purity:

```text
i_A = 1
i_Bs = i_zeta = i_kappa = 0.
```

Proof `4` validates the scalar-tail flux witness:

```text
phi = C0 + C1/r
4*pi*r^2 phi' = -4*pi*C1.
```

Proof `5` validates the current-flux witness:

```text
J_r = I/(4*pi*r^2)
4*pi*r^2 J_r = I.
```

Proof `6` validates the reduced compact-support boundary-flux gate:

```text
phi0*(1-r/R)       -> nonzero boundary flux
phi0*(1-r/R)^2     -> zero boundary flux
phi0*(1-r^2/R^2)^2 -> zero boundary flux.
```

## Interpretation

The source side now has a crisp gate structure:

```text
ordinary matter must enter once;
residual terms must not re-enter as metric or source load;
non-A sectors must not duplicate ordinary source;
scalar tails and far-zone currents must be silent unless explicitly routed;
compact support requires at least flux-safe boundary contact.
```

## Remaining Gap

These proofs are necessary safety gates, not source-origin derivations.

The next proof target is a matter-source-origin theorem:

```text
derive why ordinary source enters the A-sector once,
derive why B_s/residual sectors are source-neutral,
derive why any projection-source vector is formal unless tied to that source law.
```
"""

out = base / "7_source_safety_gate_status.md"
out.write_text(md, encoding="utf-8")

print("Source safety gate status validated.")
print(f"Wrote {out.resolve()}")
