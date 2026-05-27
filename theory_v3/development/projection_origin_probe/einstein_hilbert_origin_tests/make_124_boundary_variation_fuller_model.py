#!/usr/bin/env python3
"""
make_124_boundary_variation_fuller_model.py

Validate a fuller one-dimensional boundary-term model: a second-derivative
bulk density has derivative-of-variation boundary data until the boundary term
is added.

Output:
    124_boundary_variation_fuller_model.md
"""

from pathlib import Path
import sympy as sp


x, eps = sp.symbols("x eps")
q = sp.Function("q")(x)
eta = sp.Function("eta")(x)
q_eps = q + eps * eta


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def variation_density(L):
    return simplify_expr(sp.diff(L.subs(q, q_eps), eps).subs(eps, 0))


checks = []

L_curv = -q * sp.diff(q, x, 2)
L_boundary = sp.diff(q * sp.diff(q, x), x)
L_strain = sp.diff(q, x) ** 2

require_equal("curvature plus boundary equals strain", L_curv + L_boundary, L_strain)
checks.append("curvature plus boundary equals strain")

delta_curv = variation_density(L_curv)
curv_decomposition = -2 * eta * sp.diff(q, x, 2) + sp.diff(-q * sp.diff(eta, x) + sp.diff(q, x) * eta, x)
require_equal("curvature variation decomposition", delta_curv, curv_decomposition)
checks.append("curvature variation decomposition")

delta_boundary = variation_density(L_boundary)
boundary_variation = sp.diff(eta * sp.diff(q, x) + q * sp.diff(eta, x), x)
require_equal("boundary variation decomposition", delta_boundary, boundary_variation)
checks.append("boundary variation decomposition")

delta_total = simplify_expr(delta_curv + delta_boundary)
total_decomposition = -2 * eta * sp.diff(q, x, 2) + sp.diff(2 * eta * sp.diff(q, x), x)
require_equal("total variation has no derivative-of-variation boundary data", delta_total, total_decomposition)
checks.append("total variation has no derivative-of-variation boundary data")

delta_strain = variation_density(L_strain)
require_equal("strain variation matches completed total variation", delta_strain, total_decomposition)
checks.append("strain variation matches completed total variation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 124: Boundary Variation Fuller Model

## Purpose

This report validates a fuller one-dimensional model of the
Einstein-Hilbert/GHY boundary role.

The model is:

```text
L_curv = -q q''
L_boundary = d(q q')/dx
L_strain = (q')^2.
```

## Validated Checks

{validation_bullets}

## Density Split

SymPy verifies:

```text
-q q'' + d(q q')/dx = (q')^2.
```

## Variation Before Boundary Completion

The curvature-like term varies as:

```text
delta L_curv
  = -2 eta q''
    + d(-q eta' + q' eta)/dx.
```

The boundary data includes `eta'`, the derivative of the variation.

## Variation After Boundary Completion

The boundary term varies as:

```text
delta L_boundary
  = d(eta q' + q eta')/dx.
```

Adding the two gives:

```text
delta(L_curv + L_boundary)
  = -2 eta q''
    + d(2 eta q')/dx.
```

The derivative-of-variation boundary datum has canceled.

## Interpretation

This is the precise toy analogue of why the EH bulk term requires boundary
bookkeeping for a well-posed fixed-configuration variation. The physical
configuration is fixed at the boundary; the normal derivative of its variation
should not also have to be fixed.
"""

out = Path(__file__).with_name("124_boundary_variation_fuller_model.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
