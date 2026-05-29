#!/usr/bin/env python3
"""
make_63_neumann_dirichlet_legendre_duality.py

Validate the Legendre duality between fixed-potential Dirichlet energy and
fixed-flux/source-coupled reduced action.

Output:
    63_neumann_dirichlet_legendre_duality.md
"""

from pathlib import Path
import sympy as sp


l1, l2, g = sp.symbols("lambda1 lambda2 gamma", positive=True)
U1, U2, q1, q2 = sp.symbols("U1 U2 q1 q2", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

Lambda = sp.Matrix([[l1, g], [g, l2]])
N = sp.simplify(Lambda.inv())
U = sp.Matrix([U1, U2])
q = sp.Matrix([q1, q2])

E_D = sp.Rational(1, 2) * (U.T * Lambda * U)[0]
legendre_expression = (q.T * U)[0] - E_D

stationary = sp.Matrix([sp.diff(legendre_expression, U1), sp.diff(legendre_expression, U2)])
require_equal("Legendre stationarity component 1", stationary[0], q1 - l1 * U1 - g * U2)
checks.append("Legendre stationarity component 1")
require_equal("Legendre stationarity component 2", stationary[1], q2 - g * U1 - l2 * U2)
checks.append("Legendre stationarity component 2")

U_star = sp.simplify(N * q)
for i in range(2):
    require_zero(f"Legendre stationary solution component {i}", (Lambda * U_star - q)[i])

checks.append("Legendre stationary solution U=Nq")

E_star = sp.simplify(legendre_expression.subs({U1: U_star[0], U2: U_star[1]}))
E_dual = sp.simplify(sp.Rational(1, 2) * (q.T * N * q)[0])
require_equal("positive Legendre dual energy", E_star, E_dual)
checks.append("positive Legendre dual energy")

source_reduced = -E_dual
source_action = E_D - (q.T * U)[0]
source_action_star = sp.simplify(source_action.subs({U1: U_star[0], U2: U_star[1]}))
require_equal("source-coupled reduced action is negative dual", source_action_star, source_reduced)
checks.append("source-coupled reduced action is negative dual")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 63: Neumann-Dirichlet Legendre Duality

## Purpose

This report proves that fixed-potential and fixed-flux boundary descriptions are
Legendre dual, not interchangeable descriptions with the same energy sign.

## Validated Checks

{validation_bullets}

## Fixed Potential

The Dirichlet energy is:

```text
E_D[U] = 1/2 <U,Lambda U>.
```

The conjugate boundary flux is:

```text
q = Lambda U.
```

## Legendre Dual

The positive Legendre dual is:

```text
E_D^*[q]
  =
  sup_U (<q,U> - E_D[U])
  =
  1/2 <q,Lambda^-1 q>.
```

## Source-Coupled Reduced Action

The source-coupled action uses the opposite sign:

```text
E_source[U;q] = E_D[U] - <q,U>.
```

Eliminating `U` gives:

```text
E_source,red[q] = -E_D^*[q].
```

## Interpretation

The attractive sign in the fixed-flux model is the negative Legendre dual of
the positive fixed-potential energy.
"""

out = Path(__file__).with_name("63_neumann_dirichlet_legendre_duality.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
