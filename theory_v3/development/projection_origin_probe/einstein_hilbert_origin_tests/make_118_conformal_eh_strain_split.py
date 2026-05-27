#!/usr/bin/env python3
"""
make_118_conformal_eh_strain_split.py

Validate the conformal Einstein-Hilbert split into a boundary term plus a
first-derivative strain density.

Output:
    118_conformal_eh_strain_split.md
"""

from pathlib import Path
import sympy as sp


x, y = sp.symbols("x y")
D = sp.symbols("D", integer=True, positive=True)
s = sp.Function("s")(x, y)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

E = sp.exp((D - 2) * s)
grad_sq = sp.diff(s, x) ** 2 + sp.diff(s, y) ** 2
lap = sp.diff(s, x, 2) + sp.diff(s, y, 2)

# Conformal transformation formula:
# sqrt(g)R = e^((D-2)s)[-2(D-1)Delta s - (D-1)(D-2)|grad s|^2]
sqrt_g_R = -2 * (D - 1) * E * lap - (D - 1) * (D - 2) * E * grad_sq

boundary_divergence = -2 * (D - 1) * (
    sp.diff(E * sp.diff(s, x), x) + sp.diff(E * sp.diff(s, y), y)
)

bulk_strain = (D - 1) * (D - 2) * E * grad_sq

require_equal("conformal EH boundary plus strain split", sqrt_g_R - boundary_divergence, bulk_strain)
checks.append("conformal EH boundary plus strain split")

require_equal("four-dimensional conformal strain coefficient", bulk_strain.subs(D, 4), 6 * sp.exp(2 * s) * grad_sq)
checks.append("four-dimensional conformal strain coefficient")

require_equal("two-dimensional conformal EH has no bulk strain", bulk_strain.subs(D, 2), 0)
checks.append("two-dimensional conformal EH has no bulk strain")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 118: Conformal EH Strain Split

## Purpose

This report validates a controlled conformal-sector version of the
Einstein-Hilbert boundary/strain split.

For:

```text
g_ab = exp(2s) delta_ab,
```

the EH density can be written as:

```text
sqrt(g)R = boundary divergence + first-derivative strain density.
```

## Validated Checks

{validation_bullets}

## Conformal Split

Using the conformal transformation formula:

```text
sqrt(g)R =
  exp((D-2)s)[
    -2(D-1)Delta s
    -(D-1)(D-2)|grad s|^2
  ],
```

SymPy verifies:

```text
sqrt(g)R
  - [-2(D-1) div(exp((D-2)s) grad s)]
  =
  (D-1)(D-2) exp((D-2)s)|grad s|^2.
```

In four dimensions:

```text
bulk strain = 6 exp(2s)|grad s|^2.
```

In two dimensions:

```text
bulk strain = 0.
```

## Interpretation

This is a compact nonlinear test of the idea that EH is connection-strain plus
boundary bookkeeping. The second-derivative curvature density becomes a
first-derivative strain density after the appropriate boundary divergence is
separated.
"""

out = Path(__file__).with_name("118_conformal_eh_strain_split.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
