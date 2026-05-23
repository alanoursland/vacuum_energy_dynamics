#!/usr/bin/env python3
"""
make_2_operator_L_origin_tests.py

Generate 2_operator_L_origin_tests.md and validate the symbolic derivation.

Run from:
    theory_v3/development/projection_origin_probe/

Output:
    2_operator_L_origin_tests.md

Purpose:
    The previous note derived psi_k from an integration-by-parts primitive.
    This script tests the new operator

        L[f] = (1 - x^2) f' - 6 x f

    as a weighted-divergence / adjoint / second-order-composition object.
"""

from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------
# Symbols and core definitions
# ---------------------------------------------------------------------

x = sp.symbols("x", real=True)
alpha = sp.symbols("alpha")
a = 1 - x**2

f = sp.Function("f")
g = sp.Function("g")

w = a**4

L_f = a * sp.diff(f(x), x) - 6 * x * f(x)
Lstar_g = -a * sp.diff(g(x), x) + 4 * x * g(x)

# General family:
#
#   L_alpha[f] = a^(-alpha) d/dx[a^(alpha+1) f]
#
# expands to:
#
#   L_alpha[f] = a f' - 2(alpha+1)x f
#
L_alpha_f = a ** (-alpha) * sp.diff(a ** (alpha + 1) * f(x), x)
L_alpha_expanded = a * sp.diff(f(x), x) - 2 * (alpha + 1) * x * f(x)


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


def apply_L(expr):
    """Special operator L[f] = a f' - 6xf applied to an expression."""
    return sp.expand(a * sp.diff(expr, x) - 6 * x * expr)


def apply_Lstar(expr):
    """Weighted adjoint L*_w[g] = -a g' + 4xg applied to an expression."""
    return sp.expand(-a * sp.diff(expr, x) + 4 * x * expr)


def apply_L_alpha(expr, A):
    """Concrete L_alpha applied to an expression."""
    return sp.expand(a * sp.diff(expr, x) - 2 * (A + 1) * x * expr)


def apply_L_alpha_beta_star(expr, A, B):
    """Concrete weighted adjoint under weight a^B."""
    return sp.expand(-a * sp.diff(expr, x) + 2 * (B - A) * x * expr)


def integrate_poly(expr):
    """Exact integral over [0,1] for polynomial expressions."""
    return sp.integrate(sp.expand(expr), (x, 0, 1))


# ---------------------------------------------------------------------
# Symbolic validation
# ---------------------------------------------------------------------

checks = []

# 1. Divergence form:
#
#   L[f] = a^(-2) d/dx[a^3 f]
divergence_identity = a ** (-2) * sp.diff(a**3 * f(x), x) - L_f
require_zero("specific divergence form", divergence_identity)
checks.append("specific divergence form")

# 2. General divergence family:
#
#   a^(-alpha) d/dx[a^(alpha+1) f]
#     = a f' - 2(alpha+1)x f
general_divergence_identity = L_alpha_f - L_alpha_expanded
require_zero("general divergence family", general_divergence_identity)
checks.append("general divergence family")

# 3. Confirm that alpha=2 gives the observed L.
require_equal(
    "alpha=2 specialization",
    L_alpha_expanded.subs(alpha, 2),
    L_f,
)
checks.append("alpha=2 specialization")

# 4. Weighted-adjoint identity for a concrete integer family.
#
# Manual formula:
#
#   <L_A f, g>_B
#   =
#   [a^(B+1) f g]_0^1
#   +
#   <f, L^*_(A,B) g>_B
#
# where:
#
#   L^*_(A,B)[g] = -a g' + 2(B-A)xg.
#
# SymPy struggles with simplifying the fully symbolic exponent version,
# so the script validates the identity over a grid of integer A,B values.
for A in range(0, 6):
    for B in range(0, 7):
        L_A = apply_L_alpha(f(x), A)
        Lstar_AB = apply_L_alpha_beta_star(g(x), A, B)
        integrand_identity = (
            L_A * g(x) * a**B
            - sp.diff(a ** (B + 1) * f(x) * g(x), x)
            - f(x) * Lstar_AB * a**B
        )
        require_zero(f"weighted-adjoint integrand identity A={A} B={B}", integrand_identity)
checks.append("weighted-adjoint integrand identity for integer A,B grid")

# 5. Special adjoint under alpha=2, beta=4:
#
#   L*_w[g] = -a g' + 4xg
require_equal(
    "alpha=2 beta=4 adjoint specialization",
    apply_L_alpha_beta_star(g(x), 2, 4),
    Lstar_g,
)
checks.append("alpha=2 beta=4 adjoint specialization")

# 6. Boundary term under beta=4:
#
#   [a^5 f g]_0^1
boundary_term = a**5 * f(x) * g(x)
expected_boundary_term = (1 - x**2) ** 5 * f(x) * g(x)
require_equal("boundary term shape", boundary_term, expected_boundary_term)
checks.append("boundary term shape")

# 7. Second-order compositions.
#
#   L*_w L[f]
#   =
#   -a^2 f'' + 12x a f' + (6 - 30x^2)f
#
#   L L*_w[g]
#   =
#   -a^2 g'' + 12x a g' + (4 - 28x^2)g
Lstar_L_f = apply_Lstar(apply_L(f(x)))
expected_Lstar_L_f = (
    -a**2 * sp.diff(f(x), x, 2)
    + 12 * x * a * sp.diff(f(x), x)
    + (6 - 30 * x**2) * f(x)
)
require_equal("Lstar L composition", Lstar_L_f, expected_Lstar_L_f)
checks.append("Lstar L composition")

L_Lstar_g = apply_L(apply_Lstar(g(x)))
expected_L_Lstar_g = (
    -a**2 * sp.diff(g(x), x, 2)
    + 12 * x * a * sp.diff(g(x), x)
    + (4 - 28 * x**2) * g(x)
)
require_equal("L Lstar composition", L_Lstar_g, expected_L_Lstar_g)
checks.append("L Lstar composition")

# 8. Finite polynomial adjoint checks.
#
# The boundary term is [a^5 f g]_0^1.
# At x=1 it vanishes for regular f,g.
# At x=0 it equals -f(0)g(0) in the integrated identity.
# For odd g, g(0)=0, so the boundary term vanishes.
coeff_f = sp.symbols("c0:5")
coeff_g = sp.symbols("d0:5")

f_even = sum(coeff_f[j] * x ** (2 * j) for j in range(5))
g_odd = sum(coeff_g[j] * x ** (2 * j + 1) for j in range(5))

lhs = integrate_poly(apply_L(f_even) * g_odd * w)
rhs = integrate_poly(f_even * apply_Lstar(g_odd) * w)
require_zero("finite polynomial adjoint check with odd g", lhs - rhs)
checks.append("finite polynomial adjoint check with odd g")

# 9. Finite polynomial boundary check with general even g.
#
# Here g(0) need not vanish, so:
#
#   integral Lf g w - integral f L*g w
#   =
#   [a^5 f g]_0^1
#   =
#   -f(0)g(0)
#
g_even = sum(coeff_g[j] * x ** (2 * j) for j in range(5))
lhs_even = integrate_poly(apply_L(f_even) * g_even * w)
rhs_even = integrate_poly(f_even * apply_Lstar(g_even) * w)
boundary_even = -f_even.subs(x, 0) * g_even.subs(x, 0)
require_zero("finite polynomial adjoint boundary check with even g", lhs_even - rhs_even - boundary_even)
checks.append("finite polynomial adjoint boundary check with even g")


# ---------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# Operator `L` Origin Tests

## Purpose

This note follows the integration-by-parts derivation of `psi_k`.

The previous result established:

```text
psi_k(x)
=
-1 / ((2k + 3)(1 - x^2))
d/dx [x^(2k - 1)(1 - x^2)^2]
```

and therefore:

```text
<psi_k, f>_w
=
1/(2k + 3) <x^(2k - 1), L[f]>_w
```

with:

```text
w(x) = (1 - x^2)^4
```

and:

```text
L[f] = (1 - x^2)f' - 6xf.
```

This note asks the next question:

```text
Does L[f] have a natural operator origin,
or is it only a formal pullback artifact?
```

## Status

Current result:

```text
L has a real weighted-divergence form.
L has a clean weighted adjoint under w = (1 - x^2)^4.
L produces a definite second-order composition L*_w L.
Physical meaning remains open.
```

This does not yet identify `x`, `f`, or `S(x)` physically.

## 1. Divergence Form

Let:

```text
a(x) = 1 - x^2.
```

Then:

```text
L[f] = a f' - 6xf.
```

This can be written as:

```text
L[f] = a^(-2) d/dx[a^3 f].
```

Expanding:

```text
d/dx[a^3 f]
=
a^3 f' + 3a^2 a' f
=
a^3 f' - 6x a^2 f
=
a^2(a f' - 6xf).
```

Therefore:

```text
a^(-2) d/dx[a^3 f]
=
a f' - 6xf
=
L[f].
```

So `L` is not an arbitrary first-order expression. It is a weighted-divergence-like derivative.

## 2. General Divergence Family

There is a simple family:

```text
L_alpha[f]
=
a^(-alpha) d/dx[a^(alpha + 1) f].
```

Expanding gives:

```text
L_alpha[f]
=
a f' - 2(alpha + 1)x f.
```

The observed operator has coefficient `-6xf`, so:

```text
2(alpha + 1) = 6
alpha = 2.
```

Thus:

```text
L[f] = L_2[f].
```

This places the operator in a natural one-parameter family rather than leaving it as an isolated accident.

## 3. Exponent Ladder

The `psi_k` derivation and the operator pullback contain the ladder:

```text
primitive boundary factor:        (1 - x^2)^2
operator flux numerator:          (1 - x^2)^3
projection weight:                (1 - x^2)^4
IBP boundary term:                (1 - x^2)^5
```

or, in `a = 1 - x^2` notation:

```text
a^2 -> a^3 -> a^4 -> a^5.
```

This is meaningful algebraic structure.

It is not yet physical structure.

The next question is whether this exponent ladder comes from a real measure, domain, compactification, or boundary condition.

## 4. Weighted Adjoint Under the Projection Weight

Use the weighted inner product:

```text
<u, v>_w = integral_0^1 u(x)v(x)w(x) dx
```

with:

```text
w(x) = a^4 = (1 - x^2)^4.
```

For the general family:

```text
L_alpha[f] = a f' - 2(alpha + 1)x f
```

under weight:

```text
w_beta = a^beta,
```

integration by parts gives:

```text
<L_alpha f, g>_beta
=
[a^(beta + 1) f g]_0^1
+
<f, L^*_(alpha,beta) g>_beta
```

where:

```text
L^*_(alpha,beta)[g]
=
-a g' + 2(beta - alpha)xg.
```

Manual derivation:

```text
integral a f' g a^beta dx
=
[a^(beta + 1)fg]_0^1
-
integral f d/dx[a^(beta + 1)g] dx.
```

Also:

```text
d/dx[a^(beta + 1)g]
=
a^(beta + 1)g'
-
2(beta + 1)x a^beta g.
```

Therefore:

```text
L_alpha contribution after integration by parts
=
-a g'
+
2(beta + 1)xg
-
2(alpha + 1)xg
=
-a g' + 2(beta - alpha)xg.
```

For the observed case:

```text
alpha = 2
beta = 4
```

this becomes:

```text
L^*_w[g]
=
-(1 - x^2)g' + 4xg.
```

So:

```text
<Lf, g>_w
=
[(1 - x^2)^5 f g]_0^1
+
<f, L^*_w g>_w.
```

The boundary term is:

```text
[(1 - x^2)^5 f g]_0^1.
```

At `x = 1`, it vanishes for regular `f` and `g`.

At `x = 0`, it contributes:

```text
-f(0)g(0).
```

Therefore the adjoint relation is boundary-clean for test functions with `g(0)=0`, including the odd monomials that appeared in the `psi_k` pullback:

```text
g(x) = x^(2k - 1).
```

This matters. The adjoint identity is not boundary-free for arbitrary test functions.

## 5. Second-Order Composition

The weighted adjoint is:

```text
L^*_w[g] = -(1 - x^2)g' + 4xg.
```

Composing gives:

```text
L^*_w L[f]
=
-(1 - x^2)^2 f''
+
12x(1 - x^2)f'
+
(6 - 30x^2)f.
```

The reverse composition is:

```text
L L^*_w[g]
=
-(1 - x^2)^2 g''
+
12x(1 - x^2)g'
+
(4 - 28x^2)g.
```

These are Sturm-Liouville-like in the weak sense that they are second-order weighted operators with vanishing leading coefficient at `x = 1`.

However, this note does not yet claim that either composition is the natural operator of the theory.

The next useful test is whether one of these second-order forms can be derived independently from a variational problem, boundary regularity condition, compactified radial equation, or admissibility residual.

## 6. Relation To The `psi_k` Origin

The previous note showed that:

```text
psi_k
```

is generated by the primitive:

```text
x^(2k - 1)(1 - x^2)^2.
```

The current note shows that the resulting pullback operator is:

```text
L[f] = (1 - x^2)^(-2) d/dx[(1 - x^2)^3 f].
```

Together, the two results say:

```text
The row tests arise from moving a derivative off a boundary-vanishing primitive,
and the moved derivative lands on f through a weighted-divergence operator.
```

This is a real operator-level interpretation.

It is still formal.

## 7. Interpretation

The current evidence supports the following status:

```text
L as weighted divergence:
  derived

L as projection pullback:
  derived

L as physical flux:
  not derived

L as radial compactification operator:
  not derived

L as boundary-layer operator:
  not derived

L as admissibility residual:
  possible, not derived

L as pure artifact:
  still possible
```

The operator is more structured than a random formal byproduct, but it has not yet crossed the physical interpretation gate.

## 8. Next Tests

The next files should test the following possibilities.

### 8.1 Boundary Meaning

Ask whether the endpoint behavior:

```text
a^2, a^3, a^4, a^5
```

comes from a real boundary or compactification structure.

### 8.2 Flux Meaning

Treat:

```text
J_f = a^3 f
```

as a formal flux-like object and ask whether:

```text
L[f] = a^(-2) J_f'
```

has a natural conservation or admissibility interpretation.

Do not call `J_f` physical yet.

### 8.3 Second-Order Operator Meaning

Study:

```text
L^*_w L
```

and determine whether it has a natural self-adjoint form after a change of variables or rescaling.

### 8.4 Artifact Test

Try to construct nearby projection rows with different powers:

```text
x^(2k - 1)(1 - x^2)^m
```

and see whether the observed case `m = 2` is distinguished or merely one member of a broad arbitrary family.

## Validation Summary

The generating script validated:

```text
{validation_bullets}
```

## Bottom Line

The next object after `psi_k` is definitely:

```text
L[f] = (1 - x^2)f' - 6xf.
```

This note proves that `L` has a compact divergence form:

```text
L[f] = (1 - x^2)^(-2) d/dx[(1 - x^2)^3 f].
```

It also proves that, under the projection weight:

```text
w = (1 - x^2)^4,
```

the weighted adjoint is:

```text
L^*_w[g] = -(1 - x^2)g' + 4xg.
```

The result is strong enough to keep the projection-origin thread alive.

It is not strong enough to assign physical meaning.

The next decisive question is:

```text
Does this weighted-divergence operator arise from a real boundary, flux,
compactified radial, variational, or admissibility problem?
```
"""

out = Path("2_operator_L_origin_tests.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
