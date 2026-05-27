#!/usr/bin/env python3
"""
make_15_regularity_admissibility_conditions.py

Derive boundedness/admissibility conditions for f=u/a^3 from the transformed
problem:

    -u'' = F
    u'(0) = 0
    u(1) = 0.

Output:
    15_regularity_admissibility_conditions.md
"""

from pathlib import Path
import sympy as sp


x, t = sp.symbols("x t", real=True)
p, q = sp.symbols("p q", integer=True, nonnegative=True)
a = 1 - x**2


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


def forcing(P, Q, var):
    return var ** (2 * Q) * (1 - var**2) ** (P + 1)


def u_green_from_F(F_t):
    return sp.simplify(
        sp.integrate((1 - t) * F_t, (t, x, 1))
        + (1 - x) * sp.integrate(F_t, (t, 0, x))
    )


def vanishing_order_at_one(poly):
    """
    Return multiplicity of factor (x-1) in a polynomial expression.
    """
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

# Use a generic polynomial F with enough coefficients to verify endpoint
# derivative identities by exact integration.
coeffs = sp.symbols("c0:8")
F_t = sum(coeffs[i] * t**i for i in range(8))
F_x = sum(coeffs[i] * x**i for i in range(8))
u = sp.expand(u_green_from_F(F_t))

require_equal("ODE identity", -sp.diff(u, x, 2), F_x)
require_equal("origin Neumann identity", sp.diff(u, x).subs(x, 0), 0)
require_equal("boundary Dirichlet identity", u.subs(x, 1), 0)
checks.append("Green solution satisfies ODE and base boundary conditions")

moment_F = sp.integrate(F_t, (t, 0, 1))
require_equal("u prime boundary identity", sp.diff(u, x).subs(x, 1), -moment_F)
require_equal("u second boundary identity", sp.diff(u, x, 2).subs(x, 1), -F_x.subs(x, 1))
require_equal(
    "u third boundary identity",
    sp.diff(u, x, 3).subs(x, 1),
    -sp.diff(F_x, x).subs(x, 1),
)
require_equal(
    "u fourth boundary identity",
    sp.diff(u, x, 4).subs(x, 1),
    -sp.diff(F_x, x, 2).subs(x, 1),
)
checks.append("endpoint derivative identities through fourth derivative")

# Bounded f=u/a^3 requires u to have factor (1-x^2)^3.  Since 1+x is
# nonzero at x=1, this is equivalent locally to order at least 3 in (x-1).
model_rows = []
for R in range(0, 7):
    u_model = (1 - x) ** R
    quotient = simplify_expr(u_model / a**3)
    order = vanishing_order_at_one(u_model)
    bounded = R >= 3
    model_rows.append((R, order, quotient, bounded))
    if bounded:
        # Limit should be finite for R>=3.
        limit = sp.limit(quotient, x, 1, dir="-")
        if limit in [sp.oo, -sp.oo, sp.zoo]:
            raise AssertionError(f"expected bounded quotient for R={R}: {limit}")
    else:
        limit = sp.limit(quotient, x, 1, dir="-")
        if limit not in [sp.oo, -sp.oo]:
            raise AssertionError(f"expected divergent quotient for R={R}: {limit}")
checks.append("u/a^3 boundedness threshold is order >=3 at x=1")

# Ordinary smoothness of f is not the same as forcing additional endpoint
# contact in u. The counterexample f=1, u=a^3 is smooth, but u only has
# third-order contact at x=1 and the corresponding S does not vanish there.
u_counter = a**3
f_counter = simplify_expr(u_counter / a**3)
S_counter = simplify_expr(-sp.diff(u_counter, x, 2) / a)
require_equal("smooth counterexample f", f_counter, 1)
require_equal("smooth counterexample source", S_counter, 6 * a - 24 * x**2)
require_equal("smooth counterexample S endpoint", S_counter.subs(x, 1), -24)
if vanishing_order_at_one(u_counter) != 3:
    raise AssertionError(f"expected u=a^3 to have order 3: {u_counter}")
checks.append("ordinary smoothness is not the endpoint-contact ladder")

# For Green solution, u has order >=3 at x=1 iff u'(1)=0 and u''(1)=0,
# given u(1)=0.  Translate to moment/endpoint conditions:
#
#   int F = 0
#   F(1) = 0.
admissibility_conditions = [
    ("u(1)=0", sp.simplify(u.subs(x, 1))),
    ("u'(1)=0 iff int F=0", sp.simplify(sp.diff(u, x).subs(x, 1) + moment_F)),
    ("u''(1)=0 iff F(1)=0", sp.simplify(sp.diff(u, x, 2).subs(x, 1) + F_x.subs(x, 1))),
]
for label, residual in admissibility_conditions:
    require_zero(label, residual)
checks.append("bounded f admissibility conditions derived")

# Source-family obstruction under positive probes.
source_rows = []
for P in range(0, 6):
    for Q in range(0, 6):
        F_pq_t = forcing(P, Q, t)
        F_pq_x = forcing(P, Q, x)
        moment = sp.factor(sp.integrate(F_pq_t, (t, 0, 1)))
        endpoint = sp.simplify(F_pq_x.subs(x, 1))
        if not (moment > 0):
            raise AssertionError(f"expected positive moment for P={P} Q={Q}: {moment}")
        if endpoint != 0:
            raise AssertionError(f"expected endpoint vanishing for P={P} Q={Q}: {endpoint}")
        source_rows.append((P, Q, moment, endpoint))
checks.append("positive source-family fails moment cancellation but satisfies F(1)=0")

# Construct a simple admissible signed forcing with zero integral and F(1)=0.
#
# F = (1-x^2)(x^2 - c), choose c so int F = 0.
c = sp.symbols("c")
F_signed_t = (1 - t**2) * (t**2 - c)
c_solution = sp.solve(sp.Eq(sp.integrate(F_signed_t, (t, 0, 1)), 0), c)
if c_solution != [sp.Rational(1, 5)]:
    raise AssertionError(f"unexpected signed forcing c solution: {c_solution}")

F_signed_x = (1 - x**2) * (x**2 - sp.Rational(1, 5))
u_signed = sp.expand(u_green_from_F(F_signed_t.subs(c, sp.Rational(1, 5))))
require_equal("signed forcing ODE", -sp.diff(u_signed, x, 2), F_signed_x)
require_equal("signed forcing moment", sp.integrate(F_signed_x, (x, 0, 1)), 0)
require_equal("signed forcing endpoint", F_signed_x.subs(x, 1), 0)
if vanishing_order_at_one(u_signed) < 3:
    raise AssertionError(f"signed forcing u did not vanish to order 3: {u_signed}")
f_signed = simplify_expr(u_signed / a**3)
signed_limit = sp.limit(f_signed, x, 1, dir="-")
if signed_limit in [sp.oo, -sp.oo, sp.zoo]:
    raise AssertionError(f"signed admissible f limit diverged: {signed_limit}")
checks.append("example signed forcing satisfies bounded-f admissibility")


validation_bullets = "\n".join("- " + item + ": passed" for item in checks)
model_lines = "\n".join(
    f"u=(1-x)^{R}: order={order}, bounded u/a^3? {bounded}, quotient={quotient}"
    for R, order, quotient, bounded in model_rows
)
source_lines = "\n".join(
    f"P={P}, Q={Q}: int F={moment}, F(1)={endpoint}"
    for P, Q, moment, endpoint in source_rows
)

md = f"""# Synthesis Proof 15: Boundedness and Admissibility Conditions

## Purpose

This report turns the boundedness issue for:

```text
f = u/a^3
```

into explicit conditions on the transformed forcing:

```text
-u'' = F
u'(0)=0
u(1)=0.
```

For the energy transform, `F=aS`.

## Validated Checks

{validation_bullets}

## Endpoint Derivative Identities

For the Green solution with `u'(0)=0`, `u(1)=0`:

```text
u'(1)  = - integral_0^1 F dx
u''(1) = -F(1)
u'''(1) = -F'(1)
u''''(1) = -F''(1)
```

These identities were verified for a generic degree-7 polynomial forcing.

## Boundedness of `f = u/a^3`

Since:

```text
a = 1 - x^2 = (1-x)(1+x),
```

and `1+x` is nonzero at `x=1`, boundedness of:

```text
f = u/a^3
```

requires `u` to vanish to order at least 3 at `x=1`.

With `u(1)=0` already imposed, this means:

```text
u'(1)=0
u''(1)=0.
```

Using the derivative identities, boundedness of `f` requires:

```text
integral_0^1 F dx = 0
F(1) = 0.
```

For the original source variable, `F=aS`, this becomes:

```text
integral_0^1 aS dx = 0
(aS)(1) = 0.
```

The second condition is automatic for regular `S` because `a(1)=0`. The first
condition is a genuine global cancellation condition.

## Ordinary Smoothness Is Not the Ladder

The endpoint-contact ladder must not be read as ordinary `C^R` regularity.

Counterexample:

```text
f = 1
u = a^3 = (1-x^2)^3.
```

Then `f` is smooth, but `u` only vanishes to order `3` at `x=1`. The
corresponding source is:

```text
S = -u''/a = 6a - 24x^2,
```

so:

```text
S(1) = -24.
```

Thus ordinary smoothness of `f` does not force `S(1)=0`, nor does it force
arbitrarily high vanishing of `u`. The later `R` ladder measures boundary
contact / endpoint suppression, not ordinary differentiability.

## Model Boundedness Table

```text
{model_lines}
```

## Positive Source-Family Obstruction

For:

```text
S_(p,q) = x^(2q)a^p
F_(p,q) = aS_(p,q) = x^(2q)a^(p+1),
```

the endpoint condition `F(1)=0` holds, but the global cancellation condition
fails:

```text
integral_0^1 F_(p,q) dx > 0.
```

Exact checked moments:

```text
{source_lines}
```

Thus positive source-family probes produce singular `f` under the simple
Green-domain problem.

## Signed Admissible Example

A minimal signed forcing can satisfy the cancellation:

```text
F = (1-x^2)(x^2 - 1/5).
```

It obeys:

```text
integral_0^1 F dx = 0
F(1) = 0.
```

The corresponding Green solution vanishes to order at least 3 at `x=1`, and
`f=u/a^3` is bounded there.

For this example:

```text
u(x) = {sp.factor(u_signed)}
f(x) = {sp.factor(f_signed)}
lim_(x->1-) f(x) = {signed_limit}
```

## Interpretation

The transformed variational problem converts boundedness/contact of `f` into explicit
admissibility conditions on `F=aS`.

The first nontrivial condition is:

```text
integral_0^1 aS dx = 0.
```

This is a concrete global cancellation requirement, not just a local boundary
condition.
"""

out = Path(__file__).with_name("15_regularity_admissibility_conditions.md")
tmp = out.with_suffix(out.suffix + ".tmp")
tmp.write_text(md, encoding="utf-8")
tmp.replace(out)

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")

