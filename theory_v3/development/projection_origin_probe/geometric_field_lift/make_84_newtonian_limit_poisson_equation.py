#!/usr/bin/env python3
"""
make_84_newtonian_limit_poisson_equation.py

Validate the Newtonian limit of the linearized Einstein tensor for:

    g_00 = -(1+2 Phi)
    g_ij = (1-2 Phi) delta_ij

with static Phi.  The linearized Einstein tensor satisfies:

    G_00 = 2 Delta Phi.

Then G_00 = 8*pi*G*rho gives:

    Delta Phi = 4*pi*G*rho.

Output:
    84_newtonian_limit_poisson_equation.md
"""

from pathlib import Path
import sympy as sp


t, x, y, z = sp.symbols("t x y z", real=True)
coords = (t, x, y, z)
eta = [-1, 1, 1, 1]
dim = 4
Gconst = sp.symbols("G", positive=True)
rho = sp.Function("rho")(x, y, z)
Phi = sp.Function("Phi")(x, y, z)


def require_zero(label, expr):
    result = sp.simplify(sp.factor(expr))
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def d_up(a, expr):
    return eta[a] * sp.diff(expr, coords[a])


def box(expr):
    return sum(eta[a] * sp.diff(expr, coords[a], 2) for a in range(dim))


def lap3(expr):
    return sp.diff(expr, x, 2) + sp.diff(expr, y, 2) + sp.diff(expr, z, 2)


checks = []

# Metric perturbation h_ab = g_ab - eta_ab.
h = [[sp.Integer(0) for _ in range(dim)] for _ in range(dim)]
h[0][0] = -2 * Phi
for i in (1, 2, 3):
    h[i][i] = -2 * Phi

trace_h = sum(eta[a] * h[a][a] for a in range(dim))


def Ricci(a, b):
    term1 = sum(d_up(c, sp.diff(h[b][c], coords[a])) for c in range(dim))
    term2 = sum(d_up(c, sp.diff(h[a][c], coords[b])) for c in range(dim))
    return sp.Rational(1, 2) * (
        term1 + term2 - box(h[a][b]) - sp.diff(trace_h, coords[a], coords[b])
    )


R_scalar = sum(eta[a] * Ricci(a, a) for a in range(dim))
G00 = Ricci(0, 0) - sp.Rational(1, 2) * eta[0] * R_scalar

require_equal("Newtonian ansatz G00", G00, 2 * lap3(Phi))
checks.append("Newtonian ansatz G00")

einstein_00 = sp.Eq(G00, 8 * sp.pi * Gconst * rho)
poisson_residual = sp.simplify(G00 - 8 * sp.pi * Gconst * rho)
require_equal(
    "Einstein 00 equation reduces to Poisson residual",
    poisson_residual / 2,
    lap3(Phi) - 4 * sp.pi * Gconst * rho,
)
checks.append("Einstein 00 equation reduces to Poisson residual")

# Vacuum exterior: rho=0 gives Laplace equation.
require_equal("vacuum Newtonian exterior", poisson_residual.subs(rho, 0) / 2, lap3(Phi))
checks.append("vacuum Newtonian exterior")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Geometric Field Lift 84: Newtonian Limit Poisson Equation

## Purpose

This report validates the Newtonian limit of the linearized Einstein tensor.

## Validated Checks

{validation_bullets}

## Weak-Field Ansatz

Use:

```text
g_00 = -(1+2 Phi)
g_ij = (1-2 Phi) delta_ij.
```

Equivalently:

```text
h_00 = -2 Phi
h_ij = -2 Phi delta_ij.
```

For static `Phi`, SymPy verifies:

```text
G_00 = 2 Delta Phi.
```

## Poisson Equation

The `00` component of the Einstein equation:

```text
G_00 = 8*pi*G*rho
```

therefore gives:

```text
Delta Phi = 4*pi*G*rho.
```

In the source-free exterior:

```text
Delta Phi = 0.
```

## Interpretation

The scalar boundary-flux bridge matches the Newtonian exterior sector if its
positive scalar field is identified as:

```text
u = -Phi.
```
"""

out = Path(__file__).with_name("84_newtonian_limit_poisson_equation.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
