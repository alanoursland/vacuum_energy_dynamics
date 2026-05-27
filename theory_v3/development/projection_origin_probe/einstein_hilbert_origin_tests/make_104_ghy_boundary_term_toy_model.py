#!/usr/bin/env python3
"""
make_104_ghy_boundary_term_toy_model.py

Validate a one-dimensional toy model for why a boundary term is needed when an
action contains second derivatives.

The toy identity:

    -q q'' + d(q q')/dx = (q')^2

shows how adding a boundary divergence turns a second-derivative action into a
first-derivative strain action and removes variation terms involving eta' from
the boundary variation.

Output:
    104_ghy_boundary_term_toy_model.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
q = sp.Function("q")(x)
eta = sp.Function("eta")(x)
eps = sp.symbols("eps", real=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

second_derivative_density = -q * sp.diff(q, x, 2)
boundary_divergence = sp.diff(q * sp.diff(q, x), x)
first_derivative_density = sp.diff(q, x) ** 2

require_equal(
    "second-derivative density plus boundary term",
    second_derivative_density + boundary_divergence,
    first_derivative_density,
)
checks.append("second-derivative action converts to first-derivative strain action")

q_eps = q + eps * eta
delta_second = sp.diff((-q_eps * sp.diff(q_eps, x, 2)), eps).subs(eps, 0)
delta_first = sp.diff((sp.diff(q_eps, x) ** 2), eps).subs(eps, 0)

second_variation_identity = (
    delta_second
    - (-2 * sp.diff(q, x, 2) * eta)
    - sp.diff(sp.diff(q, x) * eta - q * sp.diff(eta, x), x)
)
require_zero("second-derivative variation identity", second_variation_identity)
checks.append("second-derivative variation has eta-prime boundary term")

first_variation_identity = (
    delta_first
    - (-2 * sp.diff(q, x, 2) * eta)
    - sp.diff(2 * sp.diff(q, x) * eta, x)
)
require_zero("first-derivative variation identity", first_variation_identity)
checks.append("boundary-corrected variation removes eta-prime boundary term")

boundary_variation_delta = simplify_expr(delta_first - delta_second)
require_equal(
    "added boundary term variation",
    boundary_variation_delta,
    sp.diff(q * sp.diff(eta, x) + eta * sp.diff(q, x), x),
)
checks.append("added boundary term supplies missing variation")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 104: GHY Boundary Term Toy Model

## Purpose

This report validates a one-dimensional toy model for the role played by a
Gibbons-Hawking-York-like boundary term.

## Validated Checks

{validation_bullets}

## Toy Split

The second-derivative density:

```text
-q q''
```

becomes a first-derivative strain density after adding a boundary divergence:

```text
-q q'' + d(q q')/dx = (q')^2.
```

## Variation

The second-derivative action variation contains a boundary term involving
`eta'`:

```text
delta(-q q'')
  =
  -2q'' eta
  + d(q' eta - q eta')/dx.
```

The boundary-corrected first-derivative action has:

```text
delta((q')^2)
  =
  -2q'' eta
  + d(2q' eta)/dx.
```

The `eta'` boundary variation has been removed.

## Interpretation

This toy model mirrors the Einstein-Hilbert/GHY issue: curvature actions contain
second derivatives, and a boundary term is needed for a well-posed fixed-metric
variation.
"""

out = Path(__file__).with_name("104_ghy_boundary_term_toy_model.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
