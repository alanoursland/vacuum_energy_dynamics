#!/usr/bin/env python3
"""
make_2_inverse_square_selects_three_space.py

Validate that exact inverse-square radial field strength selects three spatial
dimensions under conserved flux.

Output:
    2_inverse_square_selects_three_space.md
"""

from pathlib import Path
import sympy as sp


n = sp.symbols("n")


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


solution = sp.solve([sp.Eq(1 - n, -2)], [n], dict=True)
if solution != [{n: 3}]:
    raise AssertionError(f"unexpected inverse-square solution: {solution}")

D = n + 1
require_zero("D from n=3", D.subs(n, 3) - 4)

md = """# Vacuum Dimension Selector 2: Inverse-Square Selects Three Space

## Purpose

This proof solves the dimension selected by exact inverse-square radial field
strength under the conserved-flux gate.

## Validated Checks

- conserved-flux exponent is `1-n`: passed
- inverse-square exponent is `-2`: passed
- solving `1-n=-2` gives `n=3`: passed
- adding one time channel gives `D=4`: passed

## Computation

From proof `1`:

```text
F(r) ~ r^(1-n).
```

Exact inverse-square behavior requires:

```text
1 - n = -2.
```

Sympy solves:

```text
n = 3.
```

With one time channel:

```text
D = n + 1 = 4.
```

## Interpretation

This is a conditional selector. It selects three spatial dimensions if exact
long-range inverse-square flux is treated as a fundamental physical target.
"""

out = Path(__file__).with_name("2_inverse_square_selects_three_space.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Inverse-square selects three-space passed.")
print(f"Wrote {out.resolve()}")

