#!/usr/bin/env python3
"""
make_55_dimensionality_selector_consistency.py

Validate consistency between the inverse-square, spin-2, and Lovelock
dimension selectors.

Output:
    55_dimensionality_selector_consistency.md
"""

from pathlib import Path
import sympy as sp


n, D = sp.symbols("n D", integer=True)


def simplify_expr(expr):
    return sp.factor(sp.cancel(sp.simplify(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


checks = []

inverse_square_eq = sp.Eq(1 - n, -2)
n_solution = sp.solve([inverse_square_eq], [n], dict=True)
if n_solution != [{n: 3}]:
    raise AssertionError(f"unexpected inverse-square solution: {n_solution}")
checks.append("inverse-square monopole field selects n=3 spatial dimensions")

D_from_n = n + 1
require_zero("n=3 gives D=4", D_from_n.subs(n, 3) - 4)
checks.append("n=3 plus one time dimension gives D=4")

spin2_dof = simplify_expr(D * (D - 3) / 2)
D_spin2 = sp.solve([sp.Eq(spin2_dof, 2)], [D], dict=True)
if D_spin2 != [{D: -1}, {D: 4}]:
    raise AssertionError(f"unexpected spin-2 solutions: {D_spin2}")
checks.append("positive spin-2 two-polarization solution is D=4")

require_zero("D=4 spin-2 dof", spin2_dof.subs(D, 4) - 2)
checks.append("D=4 has two massless spin-2 degrees of freedom")

def lovelock_status(dim, order):
    if order == 0:
        return "cosmological"
    if dim < 2 * order:
        return "vanishes"
    if dim == 2 * order:
        return "topological"
    return "dynamical"


expected_4d = {
    0: "cosmological",
    1: "dynamical",
    2: "topological",
    3: "vanishes",
}
for order, expected in expected_4d.items():
    actual = lovelock_status(4, order)
    if actual != expected:
        raise AssertionError(f"unexpected 4D Lovelock status p={order}: {actual}")
checks.append("in D=4, EH is the unique non-topological Lovelock curvature term beyond Lambda")

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 55: Dimensionality Selector Consistency

## Purpose

This proof packages the dimensionality selectors into one consistency check.

It does not derive the dimension from vacuum ontology. It records the
convergence of already-used physical criteria.

## Validated Checks

{validation_bullets}

## Selector 1: Inverse-Square Flux

In `n` spatial dimensions, a monopole field scales as:

```text
F(r) ~ r^(1-n).
```

Inverse-square behavior requires:

```text
1-n = -2
```

so:

```text
n = 3.
```

With one time dimension:

```text
D = 4.
```

## Selector 2: Massless Spin-2 Polarizations

The massless spin-2 degree count is:

```text
D(D-3)/2.
```

The positive solution with two polarizations is:

```text
D = 4.
```

## Selector 3: Lovelock Gate

In four dimensions:

```text
Lambda: cosmological
EH: dynamical
Gauss-Bonnet: topological
higher Lovelock: vanishes.
```

## Interpretation

The dimension selector is consistent but still conditional. The theory must
still explain why these physical criteria are fundamental rather than merely
matched.
"""

out = Path(__file__).with_name("55_dimensionality_selector_consistency.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("Dimensionality selector consistency passed.")
print(f"Wrote {out.resolve()}")
