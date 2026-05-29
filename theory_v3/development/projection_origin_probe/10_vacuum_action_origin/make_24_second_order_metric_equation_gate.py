#!/usr/bin/env python3
"""
make_24_second_order_metric_equation_gate.py

Validate in a conformal metric sector that first-derivative connection strain
produces second-order metric equations.

Output:
    24_second_order_metric_equation_gate.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
s = sp.Function("s")(x)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def euler_lagrange_first_derivative(L):
    return simplify_expr(sp.diff(L, s) - sp.diff(sp.diff(L, sp.diff(s, x)), x))


checks = []

spx = sp.diff(s, x)
spp = sp.diff(s, x, 2)
s3 = sp.diff(s, x, 3)
s4 = sp.diff(s, x, 4)

# Four-dimensional conformal EH bulk strain after boundary completion:
#   sqrt(g)R = boundary + 6 exp(2s)(s')^2.
L_eh_conf = 6 * sp.exp(2 * s) * spx**2
EL_eh_conf = euler_lagrange_first_derivative(L_eh_conf)

require_equal("conformal EH strain Euler-Lagrange equation", EL_eh_conf, -12 * sp.exp(2 * s) * (spp + spx**2))
checks.append("conformal EH strain Euler-Lagrange equation")

if EL_eh_conf.has(s3) or EL_eh_conf.has(s4):
    raise AssertionError(f"EH conformal strain produced higher derivatives:\n{EL_eh_conf}")
checks.append("conformal EH strain has no third or fourth derivatives")

require_equal("highest derivative coefficient is second order", sp.diff(EL_eh_conf, spp), -12 * sp.exp(2 * s))
checks.append("highest derivative coefficient is second order")

# General first-derivative strain proxy.
alpha, K = sp.symbols("alpha K")
L_general = K * sp.exp(alpha * s) * spx**2
EL_general = euler_lagrange_first_derivative(L_general)
require_equal("general first-derivative strain variation", EL_general, -K * sp.exp(alpha * s) * (alpha * spx**2 + 2 * spp))
checks.append("general first-derivative strain variation")

if EL_general.has(s3) or EL_general.has(s4):
    raise AssertionError(f"general first-derivative strain produced higher derivatives:\n{EL_general}")
checks.append("general first-derivative strain remains second order")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 24: Second-Order Metric Equation Gate

## Purpose

This report validates the second-order action-selection gate in a conformal
metric sector.

The gate is:

```text
first-derivative connection strain
  -> second-order metric equation.
```

## Validated Checks

{validation_bullets}

## Conformal EH Strain

From the previous boundary split, the four-dimensional conformal EH bulk strain
is:

```text
L = 6 exp(2s)(s')^2.
```

SymPy verifies:

```text
delta L / delta s
  =
  -12 exp(2s)[s'' + (s')^2].
```

No third or fourth derivatives occur.

## General First-Derivative Strain

For:

```text
L = K exp(alpha s)(s')^2,
```

SymPy verifies:

```text
delta L / delta s
  =
  -K exp(alpha s)[alpha(s')^2 + 2s''].
```

Again, the equation is second order.

## Interpretation

If the vacuum action is built from local comparison strain, and that strain is
first derivative in the metric, the field equation is naturally second order.
This is the action-origin version of the Lovelock second-order gate.
"""

out = Path(__file__).with_name("24_second_order_metric_equation_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
