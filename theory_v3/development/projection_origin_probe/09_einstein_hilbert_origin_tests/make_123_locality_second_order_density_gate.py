#!/usr/bin/env python3
"""
make_123_locality_second_order_density_gate.py

Validate in a one-dimensional variational proxy that local quadratic dependence
on nth derivatives generically gives 2n-order Euler-Lagrange equations.

Output:
    123_locality_second_order_density_gate.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
q = sp.Function("q")(x)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def euler_lagrange_1d(L, max_order):
    result = sp.diff(L, q)
    for order in range(1, max_order + 1):
        q_deriv = sp.diff(q, x, order)
        result += (-1) ** order * sp.diff(sp.diff(L, q_deriv), x, order)
    return simplify_expr(result)


checks = []

L0 = sp.Rational(1, 2) * q**2
EL0 = euler_lagrange_1d(L0, 0)
require_equal("zeroth-derivative density gives algebraic equation", EL0, q)
checks.append("zeroth-derivative density gives algebraic equation")

L1 = sp.Rational(1, 2) * sp.diff(q, x) ** 2
EL1 = euler_lagrange_1d(L1, 1)
require_equal("first-derivative density gives second-order equation", EL1, -sp.diff(q, x, 2))
checks.append("first-derivative density gives second-order equation")

L2 = sp.Rational(1, 2) * sp.diff(q, x, 2) ** 2
EL2 = euler_lagrange_1d(L2, 2)
require_equal("second-derivative density gives fourth-order equation", EL2, sp.diff(q, x, 4))
checks.append("second-derivative density gives fourth-order equation")

L_linear_second = q * sp.diff(q, x, 2)
EL_linear_second = euler_lagrange_1d(L_linear_second, 2)
require_equal("linear second-derivative density reduces to second-order equation", EL_linear_second, 2 * sp.diff(q, x, 2))
checks.append("linear second-derivative density reduces to second-order equation")

boundary_split = simplify_expr(L_linear_second - (sp.diff(q * sp.diff(q, x), x) - sp.diff(q, x) ** 2))
require_equal("linear second-derivative term is first-derivative density plus boundary", boundary_split, 0)
checks.append("linear second-derivative term is first-derivative density plus boundary")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 123: Locality and Second-Order Density Gate

## Purpose

This report validates a one-dimensional variational proxy for the locality
gate:

```text
local quadratic dependence on nth derivatives
  -> Euler-Lagrange equations of order 2n.
```

## Validated Checks

{validation_bullets}

## Variational Proxy

For:

```text
L0 = (1/2)q^2
L1 = (1/2)(q')^2
L2 = (1/2)(q'')^2
```

SymPy verifies:

```text
EL(L0) = q
EL(L1) = -q''
EL(L2) = q''''.
```

Thus a local density quadratic in second derivatives generically produces a
fourth-order equation.

## Boundary Exception

A term linear in second derivatives can be a boundary-shifted first-derivative
density:

```text
q q'' = d(q q')/dx - (q')^2.
```

SymPy verifies this identity and the corresponding second-order
Euler-Lagrange equation.

## Interpretation

If the vacuum macroscopic field equation is required to be local and second
order, the action must be first-derivative strain plus boundary bookkeeping, or
an exceptional Lovelock combination. This is the variational reason the
Einstein-Hilbert density can contain second derivatives only through a boundary
split, while generic curvature-squared densities fail the gate.
"""

out = Path(__file__).with_name("123_locality_second_order_density_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
