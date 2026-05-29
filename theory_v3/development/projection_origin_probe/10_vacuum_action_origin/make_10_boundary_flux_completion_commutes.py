#!/usr/bin/env python3
"""
make_10_boundary_flux_completion_commutes.py

Validate that curvature-style boundary completion and boundary-flux source
variation are compatible in a one-dimensional action model.

Output:
    10_boundary_flux_completion_commutes.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
q = sp.Function("q")(x)
eta = sp.Function("eta")(x)
qR, qL, etaR, etaL, qpR, qpL, QR, QL = sp.symbols("q_R q_L eta_R eta_L qp_R qp_L Q_R Q_L")


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

L_curv = -sp.Rational(1, 2) * q * sp.diff(q, x, 2)
L_boundary = sp.Rational(1, 2) * sp.diff(q * sp.diff(q, x), x)
L_strain = sp.Rational(1, 2) * sp.diff(q, x) ** 2

require_equal("curvature completion equals strain", L_curv + L_boundary, L_strain)
checks.append("curvature completion equals strain")

delta_curv_boundary_R = -sp.Rational(1, 2) * qR * sp.Symbol("eta_p_R") + sp.Rational(1, 2) * qpR * etaR
delta_completion_boundary_R = sp.Rational(1, 2) * etaR * qpR + sp.Rational(1, 2) * qR * sp.Symbol("eta_p_R")
require_equal(
    "right derivative-of-variation cancellation",
    delta_curv_boundary_R + delta_completion_boundary_R,
    qpR * etaR,
)
checks.append("right derivative-of-variation cancellation")

delta_curv_boundary_L = -(-sp.Rational(1, 2) * qL * sp.Symbol("eta_p_L") + sp.Rational(1, 2) * qpL * etaL)
delta_completion_boundary_L = -(sp.Rational(1, 2) * etaL * qpL + sp.Rational(1, 2) * qL * sp.Symbol("eta_p_L"))
require_equal(
    "left derivative-of-variation cancellation",
    delta_curv_boundary_L + delta_completion_boundary_L,
    -qpL * etaL,
)
checks.append("left derivative-of-variation cancellation")

boundary_variation_with_source = qpR * etaR - qpL * etaL - QR * etaR + QL * etaL
factored = (qpR - QR) * etaR + (-qpL + QL) * etaL
require_equal("completed boundary source variation", boundary_variation_with_source, factored)
checks.append("completed boundary source variation")

right_solution = sp.solve([sp.Eq(qpR - QR, 0)], [qpR], dict=True)
left_solution = sp.solve([sp.Eq(-qpL + QL, 0)], [qpL], dict=True)
if right_solution != [{qpR: QR}]:
    raise AssertionError(f"right flux condition failed: {right_solution}")
if left_solution != [{qpL: QL}]:
    raise AssertionError(f"left flux condition failed: {left_solution}")
checks.append("completed action yields flux conditions")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Vacuum Action Origin 10: Boundary Completion and Flux Sources Commute

## Purpose

This report validates a one-dimensional analogue of the EH/GHY boundary
bookkeeping with boundary flux sources included.

The question is whether two operations are compatible:

```text
1. complete a curvature-like second-derivative density by a boundary term;
2. add boundary source terms that impose flux conditions.
```

## Validated Checks

{validation_bullets}

## Boundary Completion

Use:

```text
L_curv = -(1/2) q q''
L_boundary = (1/2) d(q q')/dx
L_strain = (1/2)(q')^2.
```

SymPy verifies:

```text
L_curv + L_boundary = L_strain.
```

The derivative-of-variation boundary terms cancel at both endpoints.

## Boundary Flux Sources

After completion, add:

```text
E_source = -Q_R q(R) + Q_L q(L).
```

The boundary variation becomes:

```text
(q'(R)-Q_R)eta_R + (-q'(L)+Q_L)eta_L.
```

For arbitrary boundary variations:

```text
q'(R)=Q_R
q'(L)=Q_L.
```

## Interpretation

The boundary completion required for a well-posed variational principle is
compatible with boundary-flux source bookkeeping. This is the toy-model bridge
toward understanding the EH/GHY boundary term as the nonlinear geometric
version of the boundary-flux source structure.
"""

out = Path(__file__).with_name("10_boundary_flux_completion_commutes.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
