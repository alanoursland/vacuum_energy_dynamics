#!/usr/bin/env python3
"""
make_14_u_green_regular_solution.py

Derive and validate the Green solution of the transformed energy equation:

    -u'' = a S

with boundary conditions:

    u'(0) = 0
    u(1) = 0.

Output:
    14_u_green_regular_solution.md
"""

from pathlib import Path
import sympy as sp


x, y = sp.symbols("x y", real=True)
p, q = sp.symbols("p q", integer=True, nonnegative=True)
a_x = 1 - x**2
a_y = 1 - y**2


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


def source(P, Q, var):
    return var ** (2 * Q) * (1 - var**2) ** P


def forcing(P, Q, var):
    """F = a S for source-family S."""
    return var ** (2 * Q) * (1 - var**2) ** (P + 1)


def u_solution(P, Q):
    """
    Solve -u'' = F with u'(0)=0 and u(1)=0:

        u(x) = integral_x^1 (1-t) F(t) dt
             + (1-x) integral_0^x F(t) dt

    Equivalently, Green kernel G(x,y)=1-max(x,y).
    """
    t = sp.symbols("t", real=True)
    F_t = forcing(P, Q, t)
    return sp.simplify(
        sp.integrate((1 - t) * F_t, (t, x, 1))
        + (1 - x) * sp.integrate(F_t, (t, 0, x))
    )


def u_solution_single_integral(P, Q):
    """Same solution in compact integral form for polynomial sources."""
    t = sp.symbols("t", real=True)
    F_t = forcing(P, Q, t)
    return sp.simplify(sp.integrate((1 - sp.Max(x, t)) * F_t, (t, 0, 1)))


checks = []

# 1. Green kernel:
#
# For fixed y, G(x,y)=1-y for x<=y and 1-x for x>=y.
# It satisfies G'(0,y)=0 and G(1,y)=0.
G_left = 1 - y
G_right = 1 - x
require_equal("Green left x-derivative", sp.diff(G_left, x), 0)
require_equal("Green right boundary", G_right.subs(x, 1), 0)
require_equal("Green continuity", G_left.subs(x, y), G_right.subs(x, y))

# Derivative jump for -d^2/dx^2:
# G_x(right) - G_x(left) = -1.
jump = sp.diff(G_right, x).subs(x, y) - sp.diff(G_left, x).subs(x, y)
require_equal("Green derivative jump", jump, -1)
checks.append("Green kernel boundary and jump conditions")

# 2. Direct polynomial source solutions.
solution_rows = []
regularity_rows = []
for P in range(0, 5):
    for Q in range(0, 5):
        u_pq = sp.expand(u_solution(P, Q))
        F = forcing(P, Q, x)

        require_equal(f"ODE source P={P} Q={Q}", -sp.diff(u_pq, x, 2), F)
        require_equal(f"Neumann origin P={P} Q={Q}", sp.diff(u_pq, x).subs(x, 0), 0)
        require_equal(f"Dirichlet boundary P={P} Q={Q}", u_pq.subs(x, 1), 0)

        u1 = sp.simplify(u_pq.subs(x, 1))
        up1 = sp.simplify(sp.diff(u_pq, x).subs(x, 1))
        upp1 = sp.simplify(sp.diff(u_pq, x, 2).subs(x, 1))
        u3_1 = sp.simplify(sp.diff(u_pq, x, 3).subs(x, 1))
        u4_1 = sp.simplify(sp.diff(u_pq, x, 4).subs(x, 1))

        regular_for_f = (
            u1 == 0
            and up1 == 0
            and upp1 == 0
            and u3_1 == 0
            and u4_1 == 0
        )

        solution_rows.append((P, Q, sp.factor(u_pq)))
        regularity_rows.append((P, Q, up1, upp1, u3_1, u4_1, regular_for_f))

checks.append("source-family Green solutions P,Q=0..4")

# 3. Endpoint derivative formulas.
#
# With u(x)=int_x^1 (t-x)F(t)dt + (1-x)int_0^xF(t)dt:
#   u'(1) = -int_0^1 F(t)dt.
#   u''(1) = -F(1).
# Higher derivatives are derivatives of -F at x=1.
for P in range(0, 5):
    for Q in range(0, 5):
        t = sp.symbols("t", real=True)
        F_t = forcing(P, Q, t)
        F_x = forcing(P, Q, x)
        u_pq = sp.expand(u_solution(P, Q))
        require_equal(
            f"u prime boundary formula P={P} Q={Q}",
            sp.diff(u_pq, x).subs(x, 1),
            -sp.integrate(F_t, (t, 0, 1)),
        )
        require_equal(
            f"u second boundary formula P={P} Q={Q}",
            sp.diff(u_pq, x, 2).subs(x, 1),
            -F_x.subs(x, 1),
        )
checks.append("endpoint derivative formulas")

# 4. Positive forcing obstruction:
#
# For source-family F>=0 and not identically zero, u'(1)=-int F < 0.
# We cannot prove positivity symbolically for all P,Q here, but exact grid
# checks show the moment is positive for P,Q=0..8.
moment_rows = []
for P in range(0, 9):
    for Q in range(0, 9):
        t = sp.symbols("t", real=True)
        moment = sp.integrate(forcing(P, Q, t), (t, 0, 1))
        if not (moment > 0):
            raise AssertionError(f"expected positive forcing moment for P={P} Q={Q}: {moment}")
        moment_rows.append((P, Q, sp.factor(moment)))
checks.append("positive forcing moment grid P,Q=0..8")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
solution_lines = "\n".join(
    f"P={P}, Q={Q}: u(x) = {expr}" for P, Q, expr in solution_rows
)
regularity_lines = "\n".join(
    (
        f"P={P}, Q={Q}: u'(1)={up1}, u''(1)={upp1}, "
        f"u'''(1)={u3_1}, u''''(1)={u4_1}, regular f? {regular}"
    )
    for P, Q, up1, upp1, u3_1, u4_1, regular in regularity_rows
)

md = f"""# Synthesis Proof 14: Green Solution in the `u` Variable

## Purpose

This report solves the transformed energy equation:

```text
-u'' = aS
```

with boundary conditions:

```text
u'(0) = 0
u(1) = 0.
```

These are natural first tests: even/Neumann behavior at `x=0`, and the
minimal Dirichlet condition at the boundary `x=1`.

## Validated Checks

{validation_bullets}

## Green Kernel

For:

```text
-u'' = F
u'(0)=0
u(1)=0,
```

the Green kernel is:

```text
G(x,y) = 1 - max(x,y).
```

Equivalently,

```text
G(x,y) =
  1 - y,  x <= y
  1 - x,  x >= y.
```

Thus:

```text
u(x) = integral_0^1 G(x,y) F(y) dy
```

with:

```text
F = aS.
```

For polynomial source families this can be written without `max` as:

```text
u(x)
  = integral_x^1 (1-t)F(t)dt
    + (1-x) integral_0^x F(t)dt.
```

## Source-Family Test

For:

```text
S_(p,q) = x^(2q)(1-x^2)^p
F_(p,q) = aS_(p,q) = x^(2q)(1-x^2)^(p+1),
```

SymPy verifies the exact polynomial solutions for `P,Q=0..4`.

```text
{solution_lines}
```

## Boundary Boundedness for `f = u/a^3`

Boundedness of:

```text
f = u/a^3
```

at `x=1` requires `u` to vanish to at least third order in `1-x`, equivalently
high-order vanishing in `1-x`. The minimal boundary condition `u(1)=0` is not
enough.

For the nonnegative source-family tests, the first obstruction appears at:

```text
u'(1) = - integral_0^1 F(t)dt.
```

Since `F=x^(2q)(1-x^2)^(p+1)` has positive integral for the tested family,
`u'(1)` is nonzero and negative. Therefore the resulting `f=u/a^3` is singular
at `x=1` for these positive source probes under this simple boundary problem.

```text
{regularity_lines}
```

## Interpretation

The transformed equation is explicitly solvable, but boundedness of `f` is much
stronger than the simple Dirichlet condition `u(1)=0`.

This suggests a concrete admissibility direction:

```text
bounded/contact-controlled f requires moment/endpoint cancellations in F=aS.
```

For positive source-family probes, those cancellations do not occur.
"""

out = Path(__file__).with_name("14_u_green_regular_solution.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")

