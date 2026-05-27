#!/usr/bin/env python3
"""
make_30_dimensionality_selector_gate.py

Validate two dimensionality selectors present in the proof chain:
inverse-square boundary flux selects three spatial dimensions, and two
massless spin-2 polarizations select four spacetime dimensions.

Output:
    30_dimensionality_selector_gate.md
"""

from pathlib import Path
import sympy as sp


n, D, p = sp.symbols("n D p", integer=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# In n spatial dimensions, an exterior monopole has field strength scaling
# F(r) ~ r^(1-n). Inverse square means exponent -2.
field_exponent = 1 - n
inverse_square_solution = sp.solve([sp.Eq(field_exponent, -2)], [n], dict=True)
if inverse_square_solution != [{n: 3}]:
    raise AssertionError(f"inverse-square spatial dimension solution failed: {inverse_square_solution}")
checks.append("inverse-square field selects three spatial dimensions")

spacetime_dimension_from_flux = n + 1
require_equal("inverse-square plus one time dimension gives D=4", spacetime_dimension_from_flux.subs(n, 3), 4)
checks.append("inverse-square plus one time dimension gives D=4")

spin2_dof = simplify_expr(D * (D - 3) / 2)
spin2_two_solution = sp.solve([sp.Eq(spin2_dof, 2)], [D], dict=True)
positive_integer_solution = [sol for sol in spin2_two_solution if sol[D].is_integer and sol[D] > 0]
if positive_integer_solution != [{D: 4}]:
    raise AssertionError(f"spin-2 two-polarization solution failed: {spin2_two_solution}")
checks.append("two massless spin-2 polarizations select D=4")

require_equal("spin-2 dof in D=3", spin2_dof.subs(D, 3), 0)
checks.append("spin-2 dof in D=3")

require_equal("spin-2 dof in D=4", spin2_dof.subs(D, 4), 2)
checks.append("spin-2 dof in D=4")

require_equal("spin-2 dof in D=5", spin2_dof.subs(D, 5), 5)
checks.append("spin-2 dof in D=5")


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
        raise AssertionError(f"4D Lovelock status failed p={order}: {actual} != {expected}")

checks.append("4D Lovelock status gate")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 30: Dimensionality Selector Gate

## Purpose

This report validates two independent dimensionality selectors already present
in the proof chain.

It does not derive dimensionality from the vacuum ontology. It records what the
existing gates select if their physical criteria are accepted.

## Validated Checks

{validation_bullets}

## Boundary-Flux Selector

In `n` spatial dimensions, a monopole field strength scales as:

```text
F(r) ~ r^(1-n).
```

The inverse-square law requires:

```text
1 - n = -2.
```

SymPy verifies:

```text
n = 3.
```

With one propagation time dimension:

```text
D = n + 1 = 4.
```

## Spin-2 Selector

The number of massless spin-2 degrees of freedom in `D` spacetime dimensions is:

```text
D(D-3)/2.
```

Setting this equal to two gives the positive integer solution:

```text
D = 4.
```

## Lovelock Gate in Four Dimensions

In `D=4`:

```text
p=0: cosmological
p=1: Einstein-Hilbert dynamical
p=2: Gauss-Bonnet topological
p>=3: vanishes.
```

## Interpretation

The folder has not proved why the vacuum must have three spatial dimensions.
But the already established physical targets converge on four spacetime
dimensions:

```text
inverse-square boundary flux -> 3 space + 1 time
two spin-2 polarizations     -> 4 spacetime
4D Lovelock gate             -> EH as unique dynamical local metric action.
```
"""

out = Path(__file__).with_name("30_dimensionality_selector_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
