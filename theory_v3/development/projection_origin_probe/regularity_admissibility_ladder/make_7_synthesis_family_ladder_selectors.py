#!/usr/bin/env python3
"""
make_7_synthesis_family_ladder_selectors.py

Validate synthesis claims about the primitive-power family, the beta-ladder
generalization, adjoint pairing, and compactified radial measure rejection.

Run from:
    theory_v3/development/projection_origin_probe/

Output:
    7_synthesis_family_ladder_selectors.md
"""

from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------
# Symbols and core definitions
# ---------------------------------------------------------------------

x = sp.symbols("x", real=True)
k = sp.symbols("k", integer=True, positive=True)
beta = sp.symbols("beta", positive=True)
m_symbol = sp.symbols("m_symbol")
n, c = sp.symbols("n c", positive=True)
n_free, c_free = sp.symbols("n_free c_free")

f = sp.Function("f")
g = sp.Function("g")

a = 1 - x**2
w = a**4


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


def G(K_symbolic, M):
    return x ** (2 * K_symbolic - 1) * a**M


def psi(K_symbolic, M):
    D = 2 * K_symbolic + 2 * M - 1
    r = sp.simplify((2 * K_symbolic - 1) / D)
    return x ** (2 * K_symbolic) - r * x ** (2 * K_symbolic - 2)


def L_m(expr, M):
    """Family pullback operator L_m[f] = a f' - 2(5-m)xf."""
    return sp.expand(a * sp.diff(expr, x) - 2 * (5 - M) * x * expr)


def L_m_star(expr, M):
    """Weighted adjoint under w=a^4."""
    return sp.expand(-a * sp.diff(expr, x) + 2 * M * x * expr)


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

checks = []

# 1. Primitive derivative identity:
#
#   d[x^(2k-1)a^M]/dx = -(2k+2M-1)a^(M-1) psi_(k,M).
for M in range(1, 9):
    D = 2 * k + 2 * M - 1
    derivative_identity = sp.diff(G(k, M), x) + D * a ** (M - 1) * psi(k, M)
    require_zero(f"primitive derivative identity M={M}", derivative_identity)
checks.append("primitive derivative identity grid M=1..8")

# 2. Observed ratio selects M=2:
observed_solution = sp.solve(sp.Eq(2 * k + 2 * m_symbol - 1, 2 * k + 3), m_symbol)
if observed_solution != [2]:
    raise AssertionError(f"unexpected observed-ratio m solution: {observed_solution}")
checks.append("observed ratio selects m=2")

# 3. Pullback operator specialization:
#
#   L_2[f] = a f' - 6xf.
require_equal("L_2 specialization", L_m(f(x), 2), a * sp.diff(f(x), x) - 6 * x * f(x))
checks.append("L_2 operator specialization")

# 4. Weighted adjoint identity for the family over regular M=1..5:
#
#   L_m[f] g w = d(a^5fg)/dx + f L_m^*[g] w.
for M in range(1, 6):
    integrand_identity = (
        L_m(f(x), M) * g(x) * w
        - sp.diff(a**5 * f(x) * g(x), x)
        - f(x) * L_m_star(g(x), M) * w
    )
    require_zero(f"family weighted adjoint identity M={M}", integrand_identity)
checks.append("family weighted adjoint identity grid M=1..5")

# 5. Adjoint pairing:
#
#   L_m^* = -L_(5-m).
for M in range(1, 6):
    require_equal(
        f"adjoint pairing M={M}",
        L_m_star(g(x), M),
        -L_m(g(x), 5 - M),
    )
checks.append("adjoint pairing L_m^*=-L_(5-m)")

# 6. No integer skew-adjoint point in M=1..5:
skew_adjoint_integers = []
for M in range(1, 6):
    if simplify_expr(L_m_star(g(x), M) + L_m(g(x), M)) == 0:
        skew_adjoint_integers.append(M)

if skew_adjoint_integers:
    raise AssertionError(f"unexpected integer skew-adjoint points: {skew_adjoint_integers}")

skew_solution = sp.solve(sp.Eq(m_symbol, 5 - m_symbol), m_symbol)
if skew_solution != [sp.Rational(5, 2)]:
    raise AssertionError(f"unexpected skew-adjoint fixed point: {skew_solution}")

checks.append("skew-adjoint fixed point m=5/2, no integer M=1..5")

# 7. Ordered adjacent ladder for beta=4:
#
#   primitive, flux, weight, boundary = M, 5-M, 4, 5.
ladder_selectors = []
for M in range(1, 6):
    ladder = (M, 5 - M, 4, 5)
    if ladder == (2, 3, 4, 5):
        ladder_selectors.append(M)

if ladder_selectors != [2]:
    raise AssertionError(f"adjacent ladder selector failed: {ladder_selectors}")
checks.append("ordered adjacent ladder selects m=2 for beta=4")

# 8. General beta ladder:
#
#   flux = beta+1-m.  Adjacent ladder requires:
#       beta+1-m = m+1
#       beta = beta+1-m+1
#   The first gives m=beta/2.  The second gives m=2.  Together they
#   force beta=4, m=2 for a fully consecutive four-term chain.
eq1_solution = sp.solve(sp.Eq(beta + 1 - m_symbol, m_symbol + 1), m_symbol)
eq2_solution = sp.solve(sp.Eq(beta, beta + 1 - m_symbol + 1), m_symbol)

if eq1_solution != [beta / 2] or eq2_solution != [2]:
    raise AssertionError(
        f"unexpected beta ladder equations: eq1={eq1_solution}, eq2={eq2_solution}"
    )

# The second equation alone says m=2 because it compares flux to weight by one
# without relating primitive to flux. The full adjacent ladder requires both,
# so substitute m=2 into eq1 to force beta=4, or substitute m=beta/2 into eq2
# to force beta=4 under the four-term consecutive ladder.
beta_from_full_ladder = sp.solve(sp.Eq(beta / 2, 2), beta)
if beta_from_full_ladder != [4]:
    raise AssertionError(f"unexpected beta from full ladder: {beta_from_full_ladder}")

checks.append("general beta ladder gives m=beta/2 and beta=4 for four-term chain")

# 9. Compactified radial measure:
#
#   r = x/a^c
#   dr/dx = a^(-c-1)(1+(2c-1)x^2)
#   measure exponent from r^(n-1)dr is -cn-1.
r = x / a**c
drdx = sp.diff(r, x)
expected_drdx = a ** (-c - 1) * (1 + (2 * c - 1) * x**2)

for C in [sp.Rational(1, 2), sp.Rational(1, 1), sp.Rational(2, 1)]:
    require_equal(
        f"compactification derivative c={C}",
        drdx.subs(c, C),
        expected_drdx.subs(c, C),
    )
checks.append("compactification derivative grid c=1/2,1,2")

standard_exponent_positive_n = -n / 2 - 1
if sp.solve(sp.Eq(standard_exponent_positive_n, 4), n) != []:
    raise AssertionError("standard compactification unexpectedly has positive n solution")

standard_exponent_free_n = -n_free / 2 - 1
if sp.solve(sp.Eq(standard_exponent_free_n, 4), n_free) != [-10]:
    raise AssertionError("standard compactification formal n solution changed")

general_positive_solution = sp.solve(sp.Eq(-c * n - 1, 4), n)
if general_positive_solution != []:
    raise AssertionError(f"unexpected positive c,n solution: {general_positive_solution}")

general_formal_solution = sp.solve(sp.Eq(-c_free * n_free - 1, 4), n_free)
if general_formal_solution != [-5 / c_free]:
    raise AssertionError(f"unexpected general formal solution: {general_formal_solution}")

checks.append("compactified radial measure cannot yield a^4 for positive c,n")


# ---------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Synthesis Proof 7: Family, Ladder, and Selector Tests

## Purpose

This report validates the family and selector claims used in
`speculative_synthesis.md`.

It focuses on:

```text
primitive-power family
operator family L_m
weighted-adjoint pairing
adjacent exponent ladder
compactified radial measure rejection
```

## Validated Identities

{validation_bullets}

## Primitive-Power Family

For:

```text
G_(k,m)(x) = x^(2k - 1)a^m,
```

SymPy validates:

```text
G_(k,m)' = -(2k + 2m - 1)a^(m - 1) psi_(k,m).
```

The associated row function is:

```text
psi_(k,m)(x)
  = x^(2k) - ((2k - 1)/(2k + 2m - 1))x^(2k - 2).
```

The observed denominator `2k+3` forces:

```text
m = 2.
```

But the IBP construction works for the whole regular range tested here.

## Operator Family

The family pullback operator is:

```text
L_m[f] = a f' - 2(5 - m)xf.
```

The observed operator is the `m=2` member:

```text
L_2[f] = a f' - 6xf.
```

Under `w=a^4`, the weighted adjoint is:

```text
L_m^*[g] = -a g' + 2m xg.
```

The family is closed under the adjoint relation:

```text
L_m^* = -L_(5-m).
```

The skew-adjoint fixed point is:

```text
m = 5/2,
```

so no integer `m` in the regular range is uniquely selected by skew-adjointness.

## Ladder Selector

For `w=a^4`, the exponent roles are:

```text
primitive:   a^m
flux:        a^(5-m)
weight:      a^4
boundary:    a^5
```

The ordered adjacent chain:

```text
a^2 -> a^3 -> a^4 -> a^5
```

selects:

```text
m = 2.
```

For a general weight `w=a^beta`, the primitive/flux balance condition gives:

```text
m = beta/2.
```

For the full four-term chain:

```text
primitive -> flux -> weight -> boundary,
```

the second adjacency condition also forces:

```text
m = 2.
```

Together these return:

```text
beta = 4
m = 2.
```

This is a compact mathematical selector, but it remains conditional on the
ordered ladder being independently justified.

## Compactified Radial Measure Test

For:

```text
r = x/a^c,  c > 0,
```

the radial measure contributes an `a` exponent:

```text
-cn - 1.
```

For positive `c` and positive `n`, this exponent is negative and cannot equal
the positive projection exponent `+4`.

The standard compactification `c=1/2` would formally require:

```text
n = -10.
```

The generic formal solution is:

```text
n = -5/c.
```

Thus ordinary compactified radial measure does not explain `w=a^4`.
"""

out = Path("7_synthesis_family_ladder_selectors.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
