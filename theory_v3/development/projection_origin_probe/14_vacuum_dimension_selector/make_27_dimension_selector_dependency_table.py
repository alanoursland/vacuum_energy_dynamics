#!/usr/bin/env python3
"""
make_27_dimension_selector_dependency_table.py

Create a dependency table for the dimension selector chain.

Output:
    27_dimension_selector_dependency_table.md
"""

from pathlib import Path
import sympy as sp


n, D = sp.symbols("n D", integer=True, positive=True)

checks = [
    sp.simplify((n + 1).subs(n, 3) - 4),
    sp.simplify((D * (D - 3) / 2).subs(D, 4) - 2),
    sp.simplify((D - 1).subs(D, 4) - 3),
]

if any(check != 0 for check in checks):
    raise AssertionError(f"dependency arithmetic failed: {checks}")

rows = [
    ("Conserved scalar flux", "radial flux model in n-space", "n=3 for inverse-square", "does not derive spacetime"),
    ("One clock channel", "exactly one time direction", "D=n+1=4", "clock channel imported"),
    ("Massless spin-2", "standard weak-field GR lift", "two polarizations at D=4", "metric lift imported"),
    ("Lovelock action", "local metric, diffeomorphism invariance, second-order equations", "EH curvature term singled out in D=4", "assumptions imported"),
    ("Boundary hypersurface", "spacetime boundary data", "D=4 gives three-boundary induced metric", "scalar sector incomplete"),
]

table_lines = [
    "| Selector | Required Assumption | Result | Remaining Dependency |",
    "|---|---|---|---|",
]
for row in rows:
    table_lines.append("| " + " | ".join(row) + " |")

md = f"""# Vacuum Dimension Selector 27: Dimension Selector Dependency Table

## Purpose

This report makes the dependencies explicit so that the folder cannot be read
as deriving four-dimensional spacetime from the scalar projection hierarchy
alone.

## Validated Arithmetic

- `n=3` plus one clock gives `D=4`: passed
- `D=4` gives two massless spin-2 degrees of freedom: passed
- `D=4` gives a three-dimensional spacetime boundary hypersurface: passed

## Dependency Table

{chr(10).join(table_lines)}

## Interpretation

The current proof chain is a selector intersection, not a complete ontological
derivation. Its value is that it isolates which assumptions must be supplied by
the parent vacuum theory.
"""

out = Path(__file__).with_name("27_dimension_selector_dependency_table.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Dimension selector dependency table passed.")
print(f"Wrote {out.resolve()}")

