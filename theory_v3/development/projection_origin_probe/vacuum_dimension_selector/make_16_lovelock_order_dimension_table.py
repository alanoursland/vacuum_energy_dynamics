#!/usr/bin/env python3
"""
make_16_lovelock_order_dimension_table.py

Validate the Lovelock order/dimension status table.

Output:
    16_lovelock_order_dimension_table.md
"""

from pathlib import Path


def lovelock_status(D, p):
    if D < 2 * p:
        return "vanishes"
    if D == 2 * p:
        return "topological"
    return "dynamical"


checks = {
    (4, 0): "dynamical",
    (4, 1): "dynamical",
    (4, 2): "topological",
    (4, 3): "vanishes",
    (5, 2): "dynamical",
    (6, 3): "topological",
    (7, 3): "dynamical",
}

for key, expected in checks.items():
    got = lovelock_status(*key)
    if got != expected:
        raise AssertionError(f"Lovelock status failed for {key}: {got} != {expected}")

rows = []
for D in range(2, 8):
    row = [str(D)]
    for p in range(0, 4):
        row.append(lovelock_status(D, p))
    rows.append(row)

table_lines = [
    "| D | p=0 | p=1 | p=2 | p=3 |",
    "|---:|---|---|---|---|",
]
for row in rows:
    table_lines.append("| " + " | ".join(row) + " |")

md = f"""# Vacuum Dimension Selector 16: Lovelock Order Dimension Table

## Purpose

This proof records the dimension status of Lovelock densities.

## Rule Checked

For Lovelock order `p` in spacetime dimension `D`:

```text
D < 2p  -> term vanishes
D = 2p  -> term is topological
D > 2p  -> term can be dynamical
```

## Validated Table

{chr(10).join(table_lines)}

## Interpretation

This table is a standard action-classification gate. It does not derive the
Einstein-Hilbert action, but it identifies which Lovelock terms can carry local
dynamics in each dimension.
"""

out = Path(__file__).with_name("16_lovelock_order_dimension_table.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Lovelock order dimension table passed.")
print(f"Wrote {out.resolve()}")

