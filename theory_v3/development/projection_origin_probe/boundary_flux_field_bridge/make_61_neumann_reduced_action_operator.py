#!/usr/bin/env python3
"""
make_61_neumann_reduced_action_operator.py

Validate the abstract Neumann/source-flux reduced action:

    E[U;q] = 1/2 <U, Lambda U> - <q, U>

where Lambda maps boundary potential to boundary flux.  The stationary
solution is:

    U = N q,  N = Lambda^-1

and the reduced action is:

    E_red[q] = -1/2 <q, N q>.

Output:
    61_neumann_reduced_action_operator.md
"""

from pathlib import Path
import sympy as sp


l1, l2, g = sp.symbols("lambda1 lambda2 gamma", positive=True)
q1, q2, U1, U2 = sp.symbols("q1 q2 U1 U2", real=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

Lambda = sp.Matrix([[l1, g], [g, l2]])
U = sp.Matrix([U1, U2])
q = sp.Matrix([q1, q2])

action = sp.Rational(1, 2) * (U.T * Lambda * U)[0] - (q.T * U)[0]
stationary = sp.Matrix([sp.diff(action, U1), sp.diff(action, U2)])

require_equal("stationary equation component 1", stationary[0], l1 * U1 + g * U2 - q1)
checks.append("stationary equation component 1")
require_equal("stationary equation component 2", stationary[1], g * U1 + l2 * U2 - q2)
checks.append("stationary equation component 2")

N = sp.simplify(Lambda.inv())
U_star = sp.simplify(N * q)

for i in range(2):
    require_zero(f"stationary solution component {i}", (Lambda * U_star - q)[i])

checks.append("stationary solution U=Nq")

reduced = sp.simplify(action.subs({U1: U_star[0], U2: U_star[1]}))
expected_reduced = sp.simplify(-sp.Rational(1, 2) * (q.T * N * q)[0])
require_equal("Neumann reduced action", reduced, expected_reduced)
checks.append("Neumann reduced action")

reduced_gradient = sp.Matrix([sp.diff(expected_reduced, q1), sp.diff(expected_reduced, q2)])
require_equal("reduced action derivative component 1", reduced_gradient[0], -U_star[0])
checks.append("reduced action derivative component 1")
require_equal("reduced action derivative component 2", reduced_gradient[1], -U_star[1])
checks.append("reduced action derivative component 2")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 61: Neumann Reduced Action Operator

## Purpose

This report validates the abstract boundary-flux/source-action operator
bookkeeping.

Let `Lambda` be the Dirichlet-to-Neumann operator:

```text
q = Lambda U.
```

Let:

```text
N = Lambda^-1
```

be the Neumann-to-boundary-potential operator.

## Validated Checks

{validation_bullets}

## Source-Coupled Boundary Action

Use the finite-dimensional boundary model:

```text
E[U;q] = 1/2 <U,Lambda U> - <q,U>.
```

Stationarity with respect to `U` gives:

```text
Lambda U = q.
```

Therefore:

```text
U = N q.
```

Substituting the stationary boundary potential back into the action gives:

```text
E_red[q] = -1/2 <q,Nq>.
```

## Interpretation

The attractive sign found earlier is the general Neumann/source-flux reduced
action sign. It is not specific to the two-point Green kernel.
"""

out = Path(__file__).with_name("61_neumann_reduced_action_operator.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
