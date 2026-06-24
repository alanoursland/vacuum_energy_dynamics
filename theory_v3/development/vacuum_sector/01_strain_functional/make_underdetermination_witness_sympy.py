#!/usr/bin/env python3
"""
Validate a minimal underdetermination witness for the vacuum strain sector.

The witness is deliberately a scalar prototype existence witness. It checks
that two functionals can share the same pointwise V_local Hessian while
differing in gradient terms, Euler-Lagrange equations, derivative order, and
boundary data.

Output:
    underdetermination_witness_sympy.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x")
m, a, b, epsilon = sp.symbols("m a b epsilon")
y = sp.symbols("y")
X = sp.Function("X")(x)


def simplify_expr(expr):
    return sp.simplify(sp.factor(sp.cancel(expr)))


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def euler_lagrange_1d(lagrangian, field):
    """Euler-Lagrange operator through second derivatives in one coordinate."""
    dx_field = sp.diff(field, x)
    ddx_field = sp.diff(field, x, 2)
    return simplify_expr(
        sp.diff(lagrangian, field)
        - sp.diff(sp.diff(lagrangian, dx_field), x)
        + sp.diff(sp.diff(lagrangian, ddx_field), x, 2)
    )


def boundary_pair_1d(lagrangian, field):
    """Boundary coefficients multiplying eta and eta' for L(X,X',X'')."""
    dx_field = sp.diff(field, x)
    ddx_field = sp.diff(field, x, 2)
    coeff_eta_prime = sp.diff(lagrangian, ddx_field)
    coeff_eta = sp.diff(lagrangian, dx_field) - sp.diff(coeff_eta_prime, x)
    return simplify_expr(coeff_eta), simplify_expr(coeff_eta_prime)


checks = []

V_local = m**2 * y**2 / 2
local_hessian = sp.diff(V_local, y, 2)
require_equal("pointwise V_local Hessian", local_hessian, m**2)
checks.append("pointwise V_local Hessian is m^2")

L0 = m**2 * X**2 / 2 + a * sp.diff(X, x) ** 2 / 2
L1 = L0 + epsilon * b * sp.diff(X, x, 2) ** 2 / 2

local_hessian_L0 = sp.diff(L0.subs({sp.diff(X, x): 0, sp.diff(X, x, 2): 0}), X, 2)
local_hessian_L1 = sp.diff(L1.subs({sp.diff(X, x): 0, sp.diff(X, x, 2): 0}), X, 2)
require_equal("same pointwise V_local Hessian in L0", local_hessian_L0, m**2)
require_equal("same pointwise V_local Hessian in L1", local_hessian_L1, m**2)
require_equal("matching pointwise V_local Hessians", local_hessian_L0, local_hessian_L1)
checks.append("two functionals share the same pointwise V_local Hessian")

EL0 = euler_lagrange_1d(L0, X)
EL1 = euler_lagrange_1d(L1, X)
EL_residual = simplify_expr(EL1 - EL0)

require_equal("EL0", EL0, m**2 * X - a * sp.diff(X, x, 2))
require_equal("EL residual", EL_residual, epsilon * b * sp.diff(X, x, 4))
checks.append("gradient residual changes the Euler-Lagrange equation")

eta0, eta_prime0 = boundary_pair_1d(L0, X)
eta1, eta_prime1 = boundary_pair_1d(L1, X)
require_equal("L0 eta boundary coefficient", eta0, a * sp.diff(X, x))
require_equal("L0 eta-prime boundary coefficient", eta_prime0, 0)
require_equal(
    "L1 eta boundary coefficient",
    eta1,
    a * sp.diff(X, x) - epsilon * b * sp.diff(X, x, 3),
)
require_equal("L1 eta-prime boundary coefficient", eta_prime1, epsilon * b * sp.diff(X, x, 2))
checks.append("gradient residual changes boundary data")

if sp.diff(X, x, 4) not in EL1.atoms(sp.Derivative):
    raise AssertionError("EL1 derivative-order check failed")
checks.append("residual raises derivative order")

validation_bullets = "\n".join(f"- {item}: passed" for item in checks)

md = f"""# SymPy Underdetermination Witness

## Purpose

This is a scalar prototype existence witness validating the narrow logical point used by
`underdetermination_witness.md`:

```text
same pointwise V_local Hessian does not imply same strain dynamics.
```

It is not a physical action, not a full tensor/covariant theorem, and does not
license any residual branch.

## Validated Checks

{validation_bullets}

## Prototype

Use a local part:

```text
V_local(X) = (m^2/2) X^2
```

so the pointwise `V_local` Hessian is:

```text
d^2 V_local / dX^2 = m^2.
```

Compare:

```text
L0 = (m^2/2) X^2 + (a/2) (dX/dx)^2
L1 = L0 + epsilon (b/2) (d^2X/dx^2)^2.
```

Both have the same pointwise `V_local` Hessian:

```text
m^2.
```

## Euler-Lagrange Result

SymPy verifies:

```text
EL(L0) = m^2 X - a X''
EL(L1) = m^2 X - a X'' + epsilon b X''''.
```

Therefore the same local response can coexist with different strain dynamics.

## Boundary Result

For variations through second derivatives, the boundary terms have the form:

```text
B_eta eta + B_eta_prime eta'.
```

SymPy verifies:

```text
L0:
  B_eta = a X'
  B_eta_prime = 0

L1:
  B_eta = a X' - epsilon b X'''
  B_eta_prime = epsilon b X''.
```

Thus the residual also changes admissible boundary data.

## Conclusion

The pointwise `V_local` Hessian fixes pointwise response in this prototype, but it does not
fix:

```text
Euler-Lagrange equation
derivative order
boundary data
epsilon residual
```

This validates the contract-level conclusion:

```text
local response alone does not choose K_strain.
```
"""

out = Path(__file__).with_name("underdetermination_witness_sympy.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
