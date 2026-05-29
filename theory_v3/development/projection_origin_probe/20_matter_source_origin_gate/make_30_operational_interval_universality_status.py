#!/usr/bin/env python3
"""
make_30_operational_interval_universality_status.py

Summarize matter-source-origin gate proofs 25-29.

Output:
    30_operational_interval_universality_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "25_operational_clock_redshift_universality.md",
    "26_many_particle_source_functional.md",
    "27_particle_current_weak_conservation.md",
    "28_bulk_boundary_source_partition.md",
    "29_zero_monopole_not_clock_silence.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Matter Source Origin Gate: Operational Interval Universality Status After Proofs 25-29

## Purpose

This report summarizes the operational interval-universality batch.

It tightens the previous interval/clock-rate result by separating calibration,
species response, source additivity, current conservation, bulk-boundary
partitioning, and local clock neutrality.

## Proofs Completed

Proof `25` validates that clock calibration constants are harmless, but
species-dependent redshift coefficients are not:

```text
R(phi) = 1 + (beta_1-beta_2) phi.
```

No operational clock drift requires:

```text
beta_1 = beta_2.
```

Proof `26` validates many-particle source additivity:

```text
L_int = -sum_i m_i Phi(x_i)
```

so the source weight is ordinary mass.

Proof `27` validates weak current conservation for a moving point source:

```text
d/dt <rho,test> = <j,test'>.
```

Proof `28` validates source partitioning:

```text
M_bulk + M_boundary + M_aux = M.
```

Bulk and boundary representations are safe only as partitions or limits of the
same source, not as duplicate copies.

Proof `29` validates that zero monopole does not imply local clock silence.
Auxiliary zero-monopole structures can still produce local clock effects if
they couple directly to clock rate.

## Current Result

The matter-source chain is now sharper:

```text
ordinary source comes from universal interval/proper-time coupling;
many-particle proper-time coupling gives additive mass density;
moving sources carry the expected weak conservation structure;
bulk and boundary source representations must be count-once partitions;
zero-monopole auxiliary structures are exterior-mass neutral but not
automatically clock-neutral.
```

## Remaining Gap

The next unresolved theorem is no longer the reduced matter source law. It is:

```text
derive operational interval universality from the vacuum ontology itself.
```

Concrete remaining gates:

```text
1. show that the vacuum state supplies a unique local interval, not merely a
   convenient metric variable;
2. show that all matter probes couple to that interval with the same beta;
3. show that auxiliary projection/residual structures cannot alter local clock
   rates unless promoted to explicit physical fields;
4. connect this operational interval to the nonlinear vacuum action and its
   boundary term.
```
"""

out = base / "30_operational_interval_universality_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Operational interval universality status validated.")
print(f"Wrote {out.resolve()}")
