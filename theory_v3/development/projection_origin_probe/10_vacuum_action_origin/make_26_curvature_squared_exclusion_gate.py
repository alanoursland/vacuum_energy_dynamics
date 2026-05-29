#!/usr/bin/env python3
"""
make_26_curvature_squared_exclusion_gate.py

Validate that curvature-squared candidates fail the second-order metric
equation gate in representative conformal and momentum-order models.

Output:
    26_curvature_squared_exclusion_gate.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
s = sp.Function("s")(x)
k, h, phi, D = sp.symbols("k h phi D", positive=True)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def euler_lagrange_second_derivative(L):
    return simplify_expr(
        sp.diff(L, s)
        - sp.diff(sp.diff(L, sp.diff(s, x)), x)
        + sp.diff(sp.diff(L, sp.diff(s, x, 2)), x, 2)
    )


checks = []

spx = sp.diff(s, x)
spp = sp.diff(s, x, 2)
s4 = sp.diff(s, x, 4)

# In the 4D one-coordinate conformal sector:
#   R = -6 exp(-2s)(s'' + (s')^2)
#   sqrt(g) = exp(4s)
# so sqrt(g) R^2 = 36(s'' + (s')^2)^2.
L_R2_conf = 36 * (spp + spx**2) ** 2
EL_R2_conf = euler_lagrange_second_derivative(L_R2_conf)

require_equal("conformal R squared fourth-derivative coefficient", sp.diff(EL_R2_conf, s4), 72)
checks.append("conformal R squared fourth-derivative coefficient")

if not EL_R2_conf.has(s4):
    raise AssertionError("conformal R squared variation did not contain fourth derivative")
checks.append("conformal R squared variation contains fourth derivative")

R_linear_trace = (D - 1) * k**2 * phi
R_squared_trace_operator = simplify_expr(k**2 * R_linear_trace)
require_equal("R squared trace operator degree", sp.degree(R_squared_trace_operator, k), 4)
checks.append("R squared trace operator degree")

Ricci_TT = sp.Rational(1, 2) * k**2 * h
Ricci_squared_TT_operator = simplify_expr(k**2 * Ricci_TT)
require_equal("Ricci squared TT operator degree", sp.degree(Ricci_squared_TT_operator, k), 4)
checks.append("Ricci squared TT operator degree")

EH_operator = simplify_expr(k**2 * h)
require_equal("EH linear operator degree", sp.degree(EH_operator, k), 2)
checks.append("EH linear operator degree")

require_equal("curvature squared is two derivative orders higher", sp.degree(Ricci_squared_TT_operator, k) - sp.degree(EH_operator, k), 2)
checks.append("curvature squared is two derivative orders higher")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 26: Curvature-Squared Exclusion Gate

## Purpose

This report validates why generic curvature-squared candidates fail the
second-order vacuum-action gate.

## Validated Checks

{validation_bullets}

## Conformal R Squared Test

In a four-dimensional one-coordinate conformal sector:

```text
R = -6 exp(-2s)[s'' + (s')^2]
sqrt(g) = exp(4s).
```

Therefore:

```text
sqrt(g) R^2 = 36[s'' + (s')^2]^2.
```

SymPy verifies that its Euler-Lagrange equation contains `s''''` with
coefficient:

```text
72.
```

## Momentum-Order Test

Linear curvature carries two derivatives:

```text
R_linear ~ k^2 h.
```

Curvature-squared variation adds two more:

```text
R^2 operator      ~ k^4 h
Ricci^2 operator  ~ k^4 h.
```

The EH linear operator is:

```text
EH operator ~ k^2 h.
```

## Interpretation

If the vacuum-action origin gates require local second-order metric equations,
generic `R^2` and `R_ab R^ab` terms are excluded. This is the action-origin
version of the Lovelock derivative-order gate.
"""

out = Path(__file__).with_name("26_curvature_squared_exclusion_gate.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
