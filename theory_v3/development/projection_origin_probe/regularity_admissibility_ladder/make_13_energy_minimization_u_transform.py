#!/usr/bin/env python3
"""
make_13_energy_minimization_u_transform.py

Validate the energy-minimization synthesis under the transformed variable
u = a^3 f.

Output:
    13_energy_minimization_u_transform.md
"""

from pathlib import Path
import sympy as sp


x = sp.symbols("x", real=True)
a = 1 - x**2
w = a**4

f = sp.Function("f")
u = sp.Function("u")
eta = sp.Function("eta")
v = sp.Function("v")
S = sp.Function("S")


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    out = sp.simplify(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def L(expr):
    return sp.expand(a * sp.diff(expr, x) - 6 * x * expr)


def Lstar(expr):
    return sp.expand(-a * sp.diff(expr, x) + 4 * x * expr)


checks = []

f_from_u = u(x) / a**3
eta_from_v = v(x) / a**3

# 1. Operator transform:
#
#   f = u/a^3  =>  L[f] = a^-2 u'.
require_equal("operator transform", L(f_from_u), a ** (-2) * sp.diff(u(x), x))
checks.append("operator transform")

# 2. Quadratic energy density:
#
#   (L[f])^2 w = (u')^2.
require_equal(
    "quadratic energy density transform",
    L(f_from_u) ** 2 * w,
    sp.diff(u(x), x) ** 2,
)
checks.append("quadratic energy density transform")

# 3. Source coupling:
#
#   S f w = S (u/a^3) a^4 = S u a.
require_equal("source coupling transform", S(x) * f_from_u * w, S(x) * u(x) * a)
checks.append("source coupling transform")

# 4. Variation transform:
#
#   eta = v/a^3 => L[eta] = a^-2 v',
#   so <L[f],L[eta]>_w = integral u' v' dx.
require_equal(
    "variation quadratic density transform",
    L(f_from_u) * L(eta_from_v) * w,
    sp.diff(u(x), x) * sp.diff(v(x), x),
)
checks.append("variation quadratic density transform")

require_equal(
    "variation source density transform",
    S(x) * eta_from_v * w,
    S(x) * v(x) * a,
)
checks.append("variation source density transform")

# 5. Euler-Lagrange operator equivalence:
#
#   L*_w L[f] = -a^-1 u''.
#   Therefore L*_w L[f] = S is equivalent to -u'' = aS.
Lstar_L_u = Lstar(L(f_from_u))
require_equal("transformed parent operator", Lstar_L_u, -a ** (-1) * sp.diff(u(x), x, 2))
checks.append("transformed parent operator")

require_equal(
    "Euler-Lagrange equivalence",
    a * (Lstar_L_u - S(x)),
    -sp.diff(u(x), x, 2) - a * S(x),
)
checks.append("Euler-Lagrange equivalence")

# 6. First variation integration-by-parts identity in u:
#
#   u'v' - a S v = d(u'v)/dx + (-u'' - aS)v.
u_variation_identity = (
    sp.diff(u(x), x) * sp.diff(v(x), x)
    - a * S(x) * v(x)
    - sp.diff(sp.diff(u(x), x) * v(x), x)
    - (-sp.diff(u(x), x, 2) - a * S(x)) * v(x)
)
require_zero("u-variable variation identity", u_variation_identity)
checks.append("u-variable variation identity")

# 7. Null mode:
#
#   L[f]=0 => u'=0.  u=constant gives f=C/a^3.
C = sp.symbols("C")
require_equal("constant-u null mode", L(C / a**3), 0)
checks.append("constant-u null mode")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Synthesis Proof 13: Energy Minimization in the `u = a^3 f` Variable

## Purpose

This report validates the strongest energy-minimization simplification in the
synthesis:

```text
u = a^3 f.
```

Under this change of variable, the weighted first-order energy becomes an
ordinary one-dimensional Dirichlet energy.

## Validated Identities

{validation_bullets}

## Energy Transform

Start with the candidate energy:

```text
E[f] = 1/2 <L[f], L[f]>_w - <S, f>_w
```

where:

```text
a = 1 - x^2
w = a^4
L[f] = a f' - 6xf = a^(-2)d(a^3 f)/dx.
```

Set:

```text
u = a^3 f
f = u/a^3.
```

Then:

```text
L[f] = a^(-2)u'
```

and:

```text
(L[f])^2 w = (u')^2.
```

The source coupling transforms as:

```text
S f w = S (u/a^3) a^4 = S u a.
```

So the candidate energy becomes:

```text
E[u] = 1/2 integral_0^1 (u')^2 dx
       - integral_0^1 a S u dx.
```

## Euler-Lagrange Equation

For variations `v = a^3 eta`, the first variation is:

```text
delta E[u;v]
  = integral_0^1 u'v' dx - integral_0^1 a S v dx.
```

Integrating by parts gives:

```text
delta E[u;v]
  = [u'v]_0^1
    + integral_0^1 (-u'' - aS)v dx.
```

Thus the interior Euler-Lagrange equation is:

```text
-u'' = aS.
```

SymPy verifies the operator equivalence:

```text
L*_w L[f] = S
```

is exactly:

```text
-u'' = aS
```

after multiplying by `a`.

## Null Mode

The source-free zero-energy condition is:

```text
L[f] = 0.
```

In the `u` variable this is:

```text
u' = 0.
```

So:

```text
u = constant
f = constant / a^3.
```

Regularity of `f` at `x=1` forces this constant to vanish unless the domain,
baseline, or variable choice is changed.

## Interpretation Boundary

This report proves that the candidate weighted variational problem is
equivalent, algebraically, to an ordinary one-dimensional Dirichlet/Poisson
problem in `u`.

It does not prove that this energy is physically derived.
"""

out = Path("13_energy_minimization_u_transform.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
