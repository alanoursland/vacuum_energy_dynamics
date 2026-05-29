#!/usr/bin/env python3
"""
make_107_lovelock_uniqueness_gate_summary.py

Generate and validate a Lovelock selection-gate table.

This does not prove Lovelock's theorem. It records the implication of the
theorem for local diffeomorphism-invariant metric actions with second-order
field equations.

Output:
    107_lovelock_uniqueness_gate_summary.md
"""

from pathlib import Path
import sympy as sp


D, p = sp.symbols("D p", integer=True, nonnegative=True)


def lovelock_status(dim, order):
    if order == 0:
        return "cosmological"
    if dim < 2 * order:
        return "vanishes"
    if dim == 2 * order:
        return "topological"
    return "dynamical"


checks = []

expected_4d = {
    0: "cosmological",
    1: "dynamical",
    2: "topological",
    3: "vanishes",
    4: "vanishes",
}

for order, expected in expected_4d.items():
    actual = lovelock_status(4, order)
    if actual != expected:
        raise AssertionError(f"4D Lovelock status failed p={order}: {actual} != {expected}")

checks.append("4D Lovelock status table")

for dim in range(2, 9):
    max_dynamic = max([order for order in range(1, 6) if lovelock_status(dim, order) == "dynamical"], default=None)
    expected_max = (dim - 1) // 2
    if expected_max == 0:
        expected_max = None
    if max_dynamic != expected_max:
        raise AssertionError(f"max dynamic order failed D={dim}: {max_dynamic} != {expected_max}")

checks.append("maximum dynamical Lovelock order for D=2..8")

table_lines = []
for dim in range(2, 9):
    row = ", ".join(f"p={order}:{lovelock_status(dim, order)}" for order in range(0, 5))
    table_lines.append(f"D={dim}: {row}")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
table_text = "\n".join(table_lines)

md = f"""# Einstein-Hilbert Origin Test 107: Lovelock Uniqueness Gate

## Purpose

This report records the Lovelock selection gate relevant to the
Einstein-Hilbert origin question.

It does not prove Lovelock's theorem. It uses the theorem as a gate:

```text
local metric action
diffeomorphism invariant
field equations second order in the metric
four spacetime dimensions
```

Under those assumptions, the only dynamical Lovelock term in 4D is the
Einstein-Hilbert term, with cosmological constant allowed.

## Validated Checks

{validation_bullets}

## Lovelock Status Table

```text
{table_text}
```

## Four-Dimensional Gate

In `D=4`:

```text
p=0: cosmological term
p=1: Einstein-Hilbert, dynamical
p=2: Gauss-Bonnet, topological
p>=3: vanishes
```

So if the nonlinear completion must be:

```text
local
metric-only
diffeomorphism invariant
second-order
four-dimensional
```

then the Einstein-Hilbert action is selected up to a cosmological term and
topological additions.

## Interpretation

This is a selection gate, not a derivation from the vacuum ontology. The
remaining physics question is whether the vacuum-energy framework supplies
these assumptions rather than merely accepting them.
"""

out = Path(__file__).with_name("107_lovelock_uniqueness_gate_summary.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
