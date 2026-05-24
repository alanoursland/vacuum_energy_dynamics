#!/usr/bin/env python3
"""
make_5_synthesis_operator_energy.py

Validate synthesis claims about the pullback operator, weighted adjoint,
second-order composition, and the transformed Dirichlet-energy variable.

Run from:
    theory_v3/development/projection_origin_probe/

Output:
    5_synthesis_operator_energy.md
"""

from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------
# Symbols and core definitions
# ---------------------------------------------------------------------

x = sp.symbols("x", real=True)
k = sp.symbols("k", integer=True, positive=True)

f = sp.Function("f")
g = sp.Function("g")
eta = sp.Function("eta")
u = sp.Function("u")

a = 1 - x**2
w = a**4

r_k = sp.simplify((2 * k - 1) / (2 * k + 3))
psi_k = x ** (2 * k) - r_k * x ** (2 * k - 2)
G_k = x ** (2 * k - 1) * a**2


# ---------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------

def simplify_expr(expr):
    """Aggressive cleanup for rational/power expressions."""
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.simplify(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def L(expr):
    """Observed pullback operator L[f] = a f' - 6xf."""
    return sp.expand(a * sp.diff(expr, x) - 6 * x * expr)


def Lstar(expr):
    """Weighted adjoint under w=a^4: L*_w[g] = -a g' + 4xg."""
    return sp.expand(-a * sp.diff(expr, x) + 4 * x * expr)


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

checks = []

# 1. Primitive derivative identity:
#
#   G_k' = -(2k+3)a psi_k.
primitive_identity = sp.diff(G_k, x) + (2 * k + 3) * a * psi_k
require_zero("primitive derivative identity", primitive_identity)
checks.append("primitive derivative identity")

# 2. Pullback integrand identity:
#
#   G_k d(a^3 f)/dx = x^(2k-1) a^4 L[f].
H_f = a**3 * f(x)
pullback_integrand_identity = G_k * sp.diff(H_f, x) - x ** (2 * k - 1) * w * L(f(x))
require_zero("pullback integrand identity", pullback_integrand_identity)
checks.append("pullback integrand identity")

# 3. Divergence form:
#
#   L[f] = a^-2 d(a^3 f)/dx.
divergence_identity = a ** (-2) * sp.diff(a**3 * f(x), x) - L(f(x))
require_zero("operator divergence form", divergence_identity)
checks.append("operator divergence form")

# 4. Correct rescaling warning:
#
#   L is not a^4 d(f/a^3)/dx.
wrong_rescaling = a**4 * sp.diff(f(x) / a**3, x)
wrong_difference = simplify_expr(wrong_rescaling - L(f(x)))
if wrong_difference == 0:
    raise AssertionError("wrong rescaling unexpectedly equals L")
checks.append("wrong rescaling rejected")

# 5. Natural transformed variable u=a^3 f:
#
#   if f = u/a^3, then L[f] = a^-2 u'.
f_from_u = u(x) / a**3
require_equal("transformed variable operator", L(f_from_u), a ** (-2) * sp.diff(u(x), x))
checks.append("transformed variable operator")

# 6. Dirichlet-energy simplification:
#
#   (L[u/a^3])^2 a^4 = (u')^2.
energy_density = simplify_expr(L(f_from_u) ** 2 * w)
require_equal("Dirichlet energy simplification", energy_density, sp.diff(u(x), x) ** 2)
checks.append("Dirichlet energy simplification")

# 7. Weighted adjoint integrand identity:
#
#   L[f] g w = d(a^5 f g)/dx + f L*_w[g] w.
adjoint_integrand_identity = (
    L(f(x)) * g(x) * w
    - sp.diff(a**5 * f(x) * g(x), x)
    - f(x) * Lstar(g(x)) * w
)
require_zero("weighted adjoint integrand identity", adjoint_integrand_identity)
checks.append("weighted adjoint integrand identity")

# 8. Second-order composition:
#
#   L*_w L[f] = -a^2 f'' + 12xa f' + (6-30x^2)f.
Lstar_L_f = Lstar(L(f(x)))
expected_Lstar_L_f = (
    -a**2 * sp.diff(f(x), x, 2)
    + 12 * x * a * sp.diff(f(x), x)
    + (6 - 30 * x**2) * f(x)
)
require_equal("Lstar L composition", Lstar_L_f, expected_Lstar_L_f)
checks.append("Lstar L composition")

# 9. Reverse composition:
#
#   L L*_w[g] = -a^2 g'' + 12xa g' + (4-28x^2)g.
L_Lstar_g = L(Lstar(g(x)))
expected_L_Lstar_g = (
    -a**2 * sp.diff(g(x), x, 2)
    + 12 * x * a * sp.diff(g(x), x)
    + (4 - 28 * x**2) * g(x)
)
require_equal("L Lstar composition", L_Lstar_g, expected_L_Lstar_g)
checks.append("L Lstar composition")

# 10. Zeroth-order residue:
#
#   (6-30x^2) - (4-28x^2) = 2a.
require_equal(
    "zeroth-order composition residue",
    (6 - 30 * x**2) - (4 - 28 * x**2),
    2 * a,
)
checks.append("zeroth-order composition residue")

# 11. Variational integrand identity:
#
#   L[f] L[eta] w = d(a^5 eta L[f])/dx + eta L*_w L[f] w.
variation_integrand_identity = (
    L(f(x)) * L(eta(x)) * w
    - sp.diff(a**5 * eta(x) * L(f(x)), x)
    - eta(x) * Lstar_L_f * w
)
require_zero("variational integrand identity", variation_integrand_identity)
checks.append("variational integrand identity")


# ---------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Synthesis Proof 5: Operator and Energy Structure

## Purpose

This report validates the operator and variational claims used in
`speculative_synthesis.md`.

It focuses on the chain:

```text
primitive identity
  -> IBP pullback
  -> divergence form of L
  -> weighted adjoint
  -> L*_w L parent-operator candidate
  -> transformed Dirichlet-energy variable
```

## Validated Identities

{validation_bullets}

## Main Results

The row primitive is:

```text
G_k = x^(2k - 1)a^2
```

and SymPy verifies:

```text
dG_k/dx = -(2k + 3)a psi_k.
```

The pullback operator is:

```text
L[f] = a f' - 6xf
```

with divergence form:

```text
L[f] = a^(-2) d/dx[a^3 f].
```

The natural transformed variable is:

```text
u = a^3 f.
```

Then:

```text
L[f] = a^(-2)u'
```

and the quadratic term simplifies:

```text
<L[f], L[f]>_w = integral_0^1 (u')^2 dx.
```

The weighted adjoint under `w=a^4` is:

```text
L*_w[g] = -a g' + 4xg.
```

The second-order compositions are:

```text
L*_w L[f] =
  -a^2 f'' + 12xa f' + (6 - 30x^2)f
```

and:

```text
L L*_w[g] =
  -a^2 g'' + 12xa g' + (4 - 28x^2)g.
```

Their zeroth-order residue is:

```text
(6 - 30x^2) - (4 - 28x^2) = 2a.
```

## Interpretation Boundary

This report proves the algebraic and variational identities. It does not prove
that the candidate energy functional is physically derived.
"""

out = Path("5_synthesis_operator_energy.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
