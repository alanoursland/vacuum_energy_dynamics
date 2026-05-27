#!/usr/bin/env python3
"""
make_101_eh_field_equation_newtonian_recovery.py

Validate that the Einstein-Hilbert field equation:

    G_ab = 8*pi*G T_ab

recovers the Newtonian Poisson equation for the standard weak-field ansatz.

Output:
    101_eh_field_equation_newtonian_recovery.md
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


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
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

# Weak-field Newtonian metric:
#   g_00=-(1+2Phi), g_ij=(1-2Phi)delta_ij.
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


def Einstein(a, b):
    return simplify_expr(Ricci(a, b) - sp.Rational(1, 2) * (eta[a] if a == b else 0) * R_scalar)


G00 = Einstein(0, 0)
require_equal("EH weak-field G00", G00, 2 * lap3(Phi))
checks.append("EH weak-field G00")

field_eq_residual = G00 - 8 * sp.pi * Gconst * rho
require_equal("EH 00 equation gives Poisson", field_eq_residual / 2, lap3(Phi) - 4 * sp.pi * Gconst * rho)
checks.append("EH 00 equation gives Poisson")

require_equal("source-free exterior gives Laplace", field_eq_residual.subs(rho, 0) / 2, lap3(Phi))
checks.append("source-free exterior gives Laplace")

# Boundary flux normalization for point-mass exterior.
r, M = sp.symbols("r M", positive=True)
Phi_ext = -Gconst * M / r
mass_flux = (1 / (4 * sp.pi * Gconst)) * 4 * sp.pi * r**2 * sp.diff(Phi_ext, r)
require_equal("Newtonian mass boundary flux", mass_flux, M)
checks.append("Newtonian mass boundary flux")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Einstein-Hilbert Origin Test 101: EH Field Equation Newtonian Recovery

## Purpose

This report validates that the Einstein-Hilbert field equation has the scalar
boundary-flux bridge as its Newtonian exterior limit.

## Validated Checks

{validation_bullets}

## Weak-Field Ansatz

Use:

```text
g_00 = -(1+2 Phi)
g_ij = (1-2 Phi)delta_ij.
```

The linearized Einstein tensor satisfies:

```text
G_00 = 2 Delta Phi.
```

## Einstein-Hilbert Field Equation

The field equation:

```text
G_00 = 8*pi*G rho
```

therefore gives:

```text
Delta Phi = 4*pi*G rho.
```

Outside sources:

```text
Delta Phi = 0.
```

## Boundary Flux

For:

```text
Phi = -GM/r,
```

the mass is recovered by:

```text
M = (1/(4*pi*G)) integral partial_n Phi dA.
```

## Interpretation

The Einstein-Hilbert field equation passes the first origin test: its weak-field
Newtonian sector matches the boundary-flux scalar bridge.
"""

out = Path(__file__).with_name("101_eh_field_equation_newtonian_recovery.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
