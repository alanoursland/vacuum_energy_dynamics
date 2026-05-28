#!/usr/bin/env python3
"""
make_5_flux_dimension_gate_status.py

Summarize vacuum_dimension_selector proofs 1-4.

Output:
    5_flux_dimension_gate_status.md
"""

from pathlib import Path


base = Path(__file__).parent
required = [
    "1_n_dimensional_flux_scaling.md",
    "2_inverse_square_selects_three_space.md",
    "3_green_function_dimension_classes.md",
    "4_flux_dimension_not_ontology_derivation.md",
]

missing = [name for name in required if not (base / name).exists()]
if missing:
    raise FileNotFoundError(f"missing required reports: {missing}")

md = """# Vacuum Dimension Selector 5: Flux Dimension Gate Status

## Purpose

This report summarizes the first dimension-selector proof batch.

## Proofs Completed

Proof `1` validates conserved flux scaling:

```text
F(r) ~ r^(1-n).
```

Proof `2` validates the inverse-square selector:

```text
1-n = -2 -> n = 3.
```

Proof `3` validates dimension-dependent Green-function classes:

```text
n=1: linear
n=2: logarithmic
n>2: r^(2-n).
```

Proof `4` validates the dependency:

```text
n = 1 - target_exp.
```

## Current Result

The flux gate conditionally selects:

```text
n = 3
```

if exact long-range inverse-square behavior is accepted as a fundamental
target.

## Remaining Gap

This is not yet an ontology derivation. The next proofs must add the time
channel:

```text
n=3 plus one universal clock/propagation channel -> D=4.
```
"""

out = base / "5_flux_dimension_gate_status.md"
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Flux dimension gate status validated.")
print(f"Wrote {out.resolve()}")

