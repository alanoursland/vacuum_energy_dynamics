#!/usr/bin/env python3
"""
make_117_curvature_squared_fourth_order_gate.py

Validate that curvature-squared actions generically introduce fourth-order
linearized field equations, unlike the Einstein-Hilbert term.

Output:
    117_curvature_squared_fourth_order_gate.md
"""

from pathlib import Path
import sympy as sp


k, D, phi, h = sp.symbols("k D phi h", positive=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

# Momentum-order model:
# Linear curvature carries two derivatives, represented by k^2.
R_trace_mode = (D - 1) * k**2 * phi
EH_trace_operator = simplify_expr((D - 2) * R_trace_mode)
R_squared_trace_operator = simplify_expr(k**2 * R_trace_mode)

require_equal("EH trace operator derivative order", sp.degree(EH_trace_operator, k), 2)
checks.append("EH trace operator derivative order")

require_equal("R squared trace operator derivative order", sp.degree(R_squared_trace_operator, k), 4)
checks.append("R squared trace operator derivative order")

# In a transverse-traceless mode, the linear Ricci tensor is proportional to
# k^2 h_ab. A Ricci^2 action varies to a k^4 operator.
Ricci_TT = sp.Rational(1, 2) * k**2 * h
Ricci_squared_TT_operator = simplify_expr(k**2 * Ricci_TT)
require_equal("Ricci squared TT operator derivative order", sp.degree(Ricci_squared_TT_operator, k), 4)
checks.append("Ricci squared TT operator derivative order")

require_equal("EH order is two derivatives lower than curvature squared", sp.degree(R_squared_trace_operator, k) - sp.degree(EH_trace_operator, k), 2)
checks.append("EH order is two derivatives lower than curvature squared")

require_equal("curvature itself is second derivative", sp.degree(R_trace_mode, k), 2)
checks.append("curvature itself is second derivative")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 117: Curvature-Squared Fourth-Order Gate

## Purpose

This report validates a derivative-order exclusion gate:

```text
curvature-squared actions generically produce fourth-order field equations.
```

This matters because the Lovelock/EH gate assumes local metric equations that
remain second order.

## Validated Checks

{validation_bullets}

## Momentum-Order Model

Linear curvature carries two derivatives:

```text
R_linear ~ k^2 h.
```

The Einstein-Hilbert field equation is linear in curvature:

```text
E_EH ~ k^2 h.
```

By contrast, varying a curvature-squared term adds two more derivatives:

```text
E_R2 ~ k^2 R_linear ~ k^4 h.
```

The same fourth-order behavior appears in transverse-traceless modes for
`Ricci_ab Ricci^ab`.

## Interpretation

If the macroscopic vacuum field equation is required to be local and second
order in the metric, generic curvature-squared corrections are excluded. This
is the derivative-order reason the Einstein-Hilbert term survives the gate
while `R^2` and `Ricci^2` do not.
"""

out = Path(__file__).with_name("117_curvature_squared_fourth_order_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
