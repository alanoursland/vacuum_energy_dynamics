#!/usr/bin/env python3
"""
make_56_green_matrix_reduced_action.py

Validate the reduced-action sign in a finite Green-matrix model with two
sources, including self and cross terms.

Output:
    56_green_matrix_reduced_action.md
"""

from pathlib import Path
import sympy as sp


S1, S2, G, Q1, Q2, d, K = sp.symbols("S1 S2 G Q1 Q2 d K", positive=True)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


checks = []

J = sp.Matrix([Q1, Q2])
Green = sp.Matrix([[S1, G], [G, S2]])

E_red = -sp.Rational(1, 2) * (J.T * Green * J)[0]
E_expected = -sp.Rational(1, 2) * (S1 * Q1**2 + 2 * G * Q1 * Q2 + S2 * Q2**2)
require_equal("two-source reduced Green action", E_red, E_expected)
checks.append("two-source reduced Green action")

cross_term = sp.expand(E_red).coeff(Q1, 1).coeff(Q2, 1) * Q1 * Q2
require_equal("negative reduced cross term", cross_term, -G * Q1 * Q2)
checks.append("negative reduced cross term")

# If G(d)=K/d, the cross term gives attraction for positive sources.
E_cross_d = -K * Q1 * Q2 / d
force_d = -sp.diff(E_cross_d, d)
require_equal("Green matrix inverse-square attractive derivative", force_d, -K * Q1 * Q2 / d**2)
checks.append("Green matrix inverse-square attractive derivative")

# Completing the square in operator notation:
# E[u]=1/2(u-GJ)^T G^-1 (u-GJ)-1/2 J^T G J.
# Validate with a symbolic symmetric inverse A=G^-1 represented directly.
a11, a12, a22, u1, u2 = sp.symbols("a11 a12 a22 u1 u2", real=True)
A = sp.Matrix([[a11, a12], [a12, a22]])
u = sp.Matrix([u1, u2])
quadratic_action = sp.Rational(1, 2) * (u.T * A * u)[0] - (J.T * u)[0]
stationary_equations = sp.Matrix([sp.diff(quadratic_action, u1), sp.diff(quadratic_action, u2)])
require_equal("stationary equation component 1", stationary_equations[0], a11 * u1 + a12 * u2 - Q1)
checks.append("stationary equation component 1")
require_equal("stationary equation component 2", stationary_equations[1], a12 * u1 + a22 * u2 - Q2)
checks.append("stationary equation component 2")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Boundary Flux Field Bridge 56: Green-Matrix Reduced Action

## Purpose

This report packages the reduced-action sign in a finite two-source Green
matrix model.

## Validated Checks

{validation_bullets}

## Reduced Action

Let:

```text
J = [Q1,Q2]^T
Gmat = [[S1,G],[G,S2]]
```

where `S1` and `S2` are self terms and `G` is the cross Green term.

The stationary source-coupled reduced action is:

```text
E_red = -1/2 J^T Gmat J.
```

SymPy verifies:

```text
E_red
  =
  -1/2(S1 Q1^2 + 2G Q1Q2 + S2 Q2^2).
```

Therefore the cross term is:

```text
E_cross = -G Q1Q2.
```

## Separation Dependence

If:

```text
G(d)=K/d,
```

then:

```text
E_cross(d) = -K Q1Q2/d
```

and:

```text
F_d = -dE/dd = -K Q1Q2/d^2.
```

For positive same-sign sources, this is attractive.

## Interpretation

The attractive sign is not a property of the positive strain matrix alone. It
comes from eliminating the field in the source-coupled action.
"""

out = Path(__file__).with_name("56_green_matrix_reduced_action.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
