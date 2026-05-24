#!/usr/bin/env python3
"""
make_17_regularity_ladder_source_classes.py

Derive the regularity ladder for f=u/a^3 in the transformed problem:

    -u'' = F = aS
    u'(0)=0
    u(1)=0.

Output:
    17_regularity_ladder_source_classes.md
"""

from pathlib import Path
import sympy as sp


x, t = sp.symbols("x t", real=True)
r_sym = sp.symbols("r", integer=True, nonnegative=True)
a = 1 - x**2
a_t = 1 - t**2

S = sp.Function("S")


def simplify_expr(expr):
    out = sp.simplify(expr)
    out = sp.factor(out)
    out = sp.powsimp(out, force=True)
    out = sp.cancel(out)
    out = sp.factor(out)
    return out


def require_zero(label, expr):
    result = simplify_expr(expr)
    if result != 0:
        raise AssertionError(f"{label} failed:\n{result}")


def require_equal(label, lhs, rhs):
    require_zero(label, lhs - rhs)


def integrate_poly(expr):
    return sp.integrate(sp.expand(expr), (x, 0, 1))


def moment_a_power(n, power):
    return sp.simplify(
        sum(
            sp.binomial(power, ell) * (-1) ** ell / (n + 2 * ell + 1)
            for ell in range(power + 1)
        )
    )


def u_green_from_F(F_t):
    return sp.simplify(
        sp.integrate((1 - t) * F_t, (t, x, 1))
        + (1 - x) * sp.integrate(F_t, (t, 0, x))
    )


def vanishing_order_at_one(poly):
    poly = sp.Poly(sp.expand(poly), x)
    power = 0
    expr = poly.as_expr()
    while sp.simplify(expr.subs(x, 1)) == 0:
        quotient, remainder = sp.div(sp.Poly(expr, x), sp.Poly(x - 1, x))
        if remainder.as_expr() != 0:
            break
        power += 1
        expr = quotient.as_expr()
        if expr == 0:
            return sp.oo
    return power


checks = []

# ---------------------------------------------------------------------
# 1. Generic endpoint derivative identities.
# ---------------------------------------------------------------------

coeffs = sp.symbols("c0:10")
F_t = sum(coeffs[i] * t**i for i in range(10))
F_x = sum(coeffs[i] * x**i for i in range(10))
u = sp.expand(u_green_from_F(F_t))

require_equal("generic ODE", -sp.diff(u, x, 2), F_x)
require_equal("generic u prime boundary", sp.diff(u, x).subs(x, 1), -sp.integrate(F_t, (t, 0, 1)))

for n in range(2, 8):
    require_equal(
        f"generic endpoint derivative n={n}",
        sp.diff(u, x, n).subs(x, 1),
        -sp.diff(F_x, x, n - 2).subs(x, 1),
    )
checks.append("endpoint derivative identities through n=7")

# ---------------------------------------------------------------------
# 2. F=aS endpoint derivatives in terms of S derivatives.
# ---------------------------------------------------------------------

F_symbolic = a * S(x)
symbolic_rows = []
for m in range(0, 7):
    actual = sp.diff(F_symbolic, x, m).subs(x, 1)
    if m == 0:
        expected = 0
    elif m == 1:
        expected = -2 * S(1)
    else:
        expected = (
            -2 * m * sp.diff(S(x), x, m - 1).subs(x, 1)
            - m * (m - 1) * sp.diff(S(x), x, m - 2).subs(x, 1)
        )
    require_equal(f"F=aS endpoint derivative m={m}", actual, expected)
    symbolic_rows.append((m, actual))
checks.append("F=aS endpoint derivative formulas through m=6")

# ---------------------------------------------------------------------
# 3. C^r source-class ladder.
#
# f=u/a^3 is C^R at x=1 if u vanishes to order at least R+3.
# With u(1)=0, this requires:
#   int F = 0
#   F^(m)(1)=0 for m=0..R.
#
# For F=aS and regular S, this becomes:
#   int aS = 0
#   S^(m)(1)=0 for m=0..R-1  (for R>=1).
# ---------------------------------------------------------------------

ladder_rows = []
for R in range(0, 6):
    conditions = ["integral_0^1 aS dx = 0"]
    if R >= 1:
        conditions.extend(f"S^({m})(1) = 0" if m else "S(1) = 0" for m in range(0, R))
    ladder_rows.append((R, conditions))
checks.append("regularity ladder conditions assembled")

# ---------------------------------------------------------------------
# 4. Build balanced bases for C^R classes:
#
#   B_(R,q)(x) = a^R [x^(2q) - c_(R,q)]
#
# with c chosen so int a B_(R,q)=0.
# ---------------------------------------------------------------------

basis_rows = []
for R in range(0, 5):
    denom = moment_a_power(0, R + 1)
    for q in range(1, 6):
        c_Rq = sp.factor(moment_a_power(2 * q, R + 1) / denom)
        B_Rq = sp.expand(a**R * (x ** (2 * q) - c_Rq))
        require_zero(f"basis moment cancellation R={R} q={q}", integrate_poly(a * B_Rq))

        # Source vanishing order at x=1 should be at least R.
        if vanishing_order_at_one(B_Rq) < R:
            raise AssertionError(f"basis source order failed R={R} q={q}: {B_Rq}")

        F_Rq = sp.expand(a * B_Rq)
        u_Rq = sp.expand(u_green_from_F(F_Rq.subs(x, t)))
        order_u = vanishing_order_at_one(u_Rq)
        if order_u < R + 3:
            raise AssertionError(
                f"Green solution order failed R={R} q={q}: order={order_u}, u={u_Rq}"
            )

        basis_rows.append((R, q, c_Rq, sp.factor(B_Rq), order_u))
checks.append("balanced C^R source bases verified for R=0..4 q=1..5")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
symbolic_lines = "\n".join(f"m={m}: (aS)^({m})(1) = {expr}" for m, expr in symbolic_rows)
ladder_lines = "\n".join(
    f"C^{R} f condition: " + "; ".join(conditions)
    for R, conditions in ladder_rows
)
basis_lines = "\n".join(
    f"R={R}, q={q}: c={c_Rq}, B={B_Rq}, order_1(u)={order_u}"
    for R, q, c_Rq, B_Rq, order_u in basis_rows
)

md = f"""# Synthesis Proof 17: Regularity Ladder and Source Classes

## Purpose

This report extends the first admissibility condition into a regularity
ladder for:

```text
f = u/a^3
```

where:

```text
-u'' = F = aS
u'(0)=0
u(1)=0.
```

## Validated Checks

{validation_bullets}

## Endpoint Derivative Ladder

For the Green solution:

```text
u'(1) = - integral_0^1 F dx
```

and, for `n >= 2`:

```text
u^(n)(1) = -F^(n-2)(1).
```

This was checked through `n=7` for a generic polynomial forcing.

## Translating `F = aS`

For `F=aS`, the endpoint derivatives are:

```text
{symbolic_lines}
```

Since `a(1)=0`, the condition `F(1)=0` is automatic for regular `S`. Higher
endpoint conditions force vanishing derivatives of `S` at `x=1`.

## Regularity Conditions

For `f=u/a^3` to be `C^R` at `x=1`, `u` must vanish to order at least `R+3`.
With `u(1)=0` already imposed, the first conditions are:

```text
{ladder_lines}
```

Thus boundedness requires only:

```text
integral_0^1 aS dx = 0.
```

`C^1` regularity additionally requires:

```text
S(1)=0.
```

`C^2` regularity additionally requires:

```text
S(1)=0
S'(1)=0.
```

and so on.

## Balanced Source Classes

A source basis satisfying the `C^R` ladder through order `R` is:

```text
B_(R,q)(x) = a^R [x^(2q) - c_(R,q)]
```

where:

```text
c_(R,q) =
  integral_0^1 x^(2q)a^(R+1) dx
  /
  integral_0^1 a^(R+1) dx.
```

This ensures:

```text
integral_0^1 a B_(R,q) dx = 0
```

and gives `S` the endpoint vanishing needed for `C^R` regularity.

Exact checked basis rows:

```text
{basis_lines}
```

## Interpretation

The admissibility condition is not a single accident. It extends into a ladder:

```text
C^0 f:
  integral aS = 0

C^1 f:
  integral aS = 0 and S(1)=0

C^2 f:
  integral aS = 0 and S(1)=S'(1)=0

C^R f:
  integral aS = 0 and S vanishes to order R at x=1.
```

The balanced bases `B_(R,q)` provide explicit source classes satisfying these
conditions.
"""

out = Path("17_regularity_ladder_source_classes.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
