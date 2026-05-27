#!/usr/bin/env python3
"""
make_6_matter_source_origin_gate_status.py

Summarize matter-source-origin gate proofs 1-5.

Output:
    6_matter_source_origin_gate_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "1_a_sector_mass_flux_normalization.md",
    "2_non_a_scalar_tail_mass_exclusion.md",
    "3_projection_source_independence.md",
    "4_boundary_source_count_once_routing.md",
    "5_exact_remainder_not_mass_safety.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Matter Source Origin Gate: Status After Proofs 1-5

## Purpose

This folder starts the bridge between the source-safety gates and the
vacuum-action-origin chain.

It asks:

```text
what is allowed to carry ordinary matter source?
```

It does not yet derive a covariant matter action or a full field equation.

## Proofs Completed

Proof `1` validates the A-sector reduced mass flux:

```text
A_ext = 1 - 2GM/(c^2 r)
F_A = 4*pi*r^2 A_ext' = 8*pi*G*M/c^2
M_A = M.
```

Proof `2` validates the non-A scalar-tail exclusion:

```text
phi = C0 + C1/r
F_phi = -4*pi*C1.
```

Neutral non-A sectors require `C1=0`.

Proof `3` validates projection-source independence. The formal vector:

```text
b_k(S) = 2 integral psi_k S a^4 dx
```

can be nonzero on zero-monopole variations, so it is not ordinary mass by
itself.

Proof `4` validates count-once source routing for independent flux channels:

```text
i_A = 1
i_res = 0
i_proj = 0.
```

Proof `5` validates the exact-remainder warning:

```text
rho = dJ/dy
integral rho dy = 0
```

does not imply local, weighted, or geometric neutrality.

## Current Result

The reduced source-origin ledger now says:

```text
ordinary mass is carried by A-sector flux;
non-A scalar tails are excluded unless explicitly routed;
projection source vectors remain formal admissibility diagnostics;
exact residuals are not automatically mass safe;
count-once routing selects A-only for independent ordinary source flux.
```

## Remaining Gap

The next step is not another proof that non-A channels are dangerous. The next
step is a positive source-origin theorem:

```text
derive the ordinary matter coupling that produces the A-sector flux,
show how it remains compatible with the geometric/vacuum action,
show whether the formal projection source b_k(S) is ever routed to matter,
or prove that it remains an auxiliary admissibility diagnostic only.
```
"""

out = base / "6_matter_source_origin_gate_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Matter source origin gate status validated.")
print(f"Wrote {out.resolve()}")
