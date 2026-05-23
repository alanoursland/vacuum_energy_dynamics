#!/usr/bin/env python3
"""
make_4_m2_selector_tests.py

Generate 4_m2_selector_tests.md and validate the symbolic derivation.

Run from:
    theory_v3/development/projection_origin_probe/

Output:
    4_m2_selector_tests.md

Purpose:
    Keep the projection-origin probe contained.

    The prior note showed that the IBP construction works for a primitive-power
    family

        G_(k,m)(x) = x^(2k-1)(1-x^2)^m.

    This note asks the narrow selector question:

        Can m = 2 be selected independently of already observing
        r_k = (2k-1)/(2k+3)?

    The tests are:
        1. weighted-adjoint selector
        2. exponent-ladder selector
        3. compactified radial measure selector

    The note includes a stop rule to prevent selector hunting from spiraling.
"""

from pathlib import Path
import sympy as sp


# ---------------------------------------------------------------------
# Symbols and core definitions
# ---------------------------------------------------------------------

x = sp.symbols("x", real=True)
n, c = sp.symbols("n c", positive=True)
n_free, c_free = sp.symbols("n_free c_free")
a = 1 - x**2

f = sp.Function("f")
g = sp.Function("g")

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


def L_m_expr(expr, M):
    """Family pullback operator L_m applied to expression expr."""
    return sp.expand(a * sp.diff(expr, x) - 2 * (5 - M) * x * expr)


def L_m_star_expr(expr, M):
    """Weighted adjoint under w=a^4."""
    return sp.expand(-a * sp.diff(expr, x) + 2 * M * x * expr)


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

checks = []

# 1. Weighted adjoint formula over M=1..5.
#
#   <L_m f, g>_w
#   =
#   [a^5 f g]_0^1
#   +
#   <f, L_m^* g>_w
#
# with:
#
#   L_m^*[g] = -a g' + 2m xg.
for M in range(1, 6):
    Lm_f = L_m_expr(f(x), M)
    Lm_star_g = L_m_star_expr(g(x), M)

    integrand_identity = (
        Lm_f * g(x) * w
        - sp.diff(a**5 * f(x) * g(x), x)
        - f(x) * Lm_star_g * w
    )

    require_zero(f"weighted adjoint integrand identity M={M}", integrand_identity)

checks.append("weighted adjoint identity grid M=1..5")

# 2. Adjoint pairing:
#
#   L_m^* = -L_(5-m)
#
# for M=1..5.
for M in range(1, 6):
    paired = -L_m_expr(g(x), 5 - M)
    require_equal(f"adjoint pairing M={M}", L_m_star_expr(g(x), M), paired)

checks.append("adjoint pairing L_m^* = -L_(5-m)")

# 3. Integer skew-adjointness check.
#
#   L_m^* = -L_m
#
# would require m = 5/2, so no integer M in 1..5 is selected.
integer_skew_adjoint = []
for M in range(1, 6):
    test_expr = simplify_expr(L_m_star_expr(g(x), M) + L_m_expr(g(x), M))
    if test_expr == 0:
        integer_skew_adjoint.append(M)

if integer_skew_adjoint:
    raise AssertionError(f"unexpected integer skew-adjoint M values: {integer_skew_adjoint}")

checks.append("no integer m is skew-adjoint under w=a^4")

# 4. Exponent ladder selector.
#
# General exponents:
#
#   primitive: m
#   flux: 5-m
#   weight: 4
#   boundary: 5
#
# Requiring the adjacent ordered ladder:
#
#   m, 5-m, 4, 5 = 2, 3, 4, 5
#
# selects m=2.
ladder_selectors = []
for M in range(1, 6):
    ladder = (M, 5 - M, 4, 5)
    if ladder == (2, 3, 4, 5):
        ladder_selectors.append(M)

if ladder_selectors != [2]:
    raise AssertionError(f"adjacent ladder selector failed: {ladder_selectors}")

checks.append("ordered adjacent exponent ladder selects m=2")

# 5. Adjoint pair symmetry gives the pair {2,3}, not m=2 alone.
adjacent_pair = []
for M in range(1, 6):
    if abs(M - (5 - M)) == 1:
        adjacent_pair.append(M)

if adjacent_pair != [2, 3]:
    raise AssertionError(f"adjoint-pair adjacency check failed: {adjacent_pair}")

checks.append("adjoint-pair adjacency gives pair {2,3}, not m=2 alone")

# 6. Compactified radial measure selector.
#
# Generic compactification family:
#
#   r = x / a^c, c > 0
#
# Then:
#
#   dr/dx = a^(-c-1)(1 + (2c-1)x^2)
#
# and an n-dimensional radial measure gives:
#
#   r^(n-1) dr
#   =
#   x^(n-1) [1 + (2c-1)x^2] a^(-cn - 1) dx.
#
# The a-exponent from measure alone is -cn - 1.
#
# For c>0,n>0 this is negative and cannot equal +4.
r = x / a**c
drdx = sp.diff(r, x)
expected_drdx = a ** (-c - 1) * (1 + (2 * c - 1) * x**2)

# Validate at a few rational c values because SymPy can resist proving symbolic
# exponent identities with arbitrary positive c.
for C in [sp.Rational(1, 2), sp.Rational(1, 1), sp.Rational(2, 1)]:
    require_equal(
        f"compactification derivative c={C}",
        drdx.subs(c, C),
        expected_drdx.subs(c, C),
    )

checks.append("compactified radial derivative validated for c=1/2,1,2")

# For the standard compactification c=1/2:
#
#   exponent = -n/2 - 1 = -(n+2)/2
#
# This cannot equal +4 for positive n.
standard_exponent_positive_n = -n / 2 - 1
positive_solution = sp.solve(sp.Eq(standard_exponent_positive_n, 4), n)
if positive_solution != []:
    raise AssertionError(f"unexpected positive-dimensional standard solution: {positive_solution}")

# Without positivity assumptions, the formal solution is n=-10.
standard_exponent_free_n = -n_free / 2 - 1
formal_solution = sp.solve(sp.Eq(standard_exponent_free_n, 4), n_free)
if formal_solution != [-10]:
    raise AssertionError(f"unexpected formal standard compactification solution: {formal_solution}")

checks.append("standard compactified radial measure cannot yield a^4 for positive dimension")

# More generally, -c*n - 1 = 4 has no positive n,c solution, and formally
# gives n = -5/c.
general_positive_solution = sp.solve(sp.Eq(-c * n - 1, 4), n)
if general_positive_solution != []:
    raise AssertionError(f"unexpected positive-dimensional general compactification solution: {general_positive_solution}")

general_formal_solution = sp.solve(sp.Eq(-c_free * n_free - 1, 4), n_free)
if general_formal_solution != [-5 / c_free]:
    raise AssertionError(f"unexpected general compactification formal solution: {general_formal_solution}")

checks.append("generic c>0 compactified radial measure cannot yield a^4 alone")


# ---------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------

validation_bullets = "\n".join("- " + item + ": passed" for item in checks)

md = f"""# `m = 2` Selector Tests

## Purpose

This note keeps the projection-origin probe small.

The prior notes established:

```text
psi_k:
  derived from an integration-by-parts primitive

L[f]:
  derived as a weighted-divergence pullback

primitive family:
  G_(k,m)(x) = x^(2k - 1)(1 - x^2)^m
```

The family test exposed the main danger:

```text
Every m gives an IBP construction.
Boundary cleanliness alone does not select m = 2.
```

This note asks only one question:

```text
Can m = 2 be selected independently of already observing
r_k = (2k - 1)/(2k + 3)?
```

The goal is containment. This is not a physical-interpretation note.

## Definitions

Let:

```text
a = 1 - x^2
```

and keep the projection weight:

```text
w = a^4.
```

The primitive-power family is:

```text
G_(k,m)(x) = x^(2k - 1)a^m.
```

The corresponding pullback operator is:

```text
L_m[f] = a f' - 2(5 - m)xf.
```

The observed operator is:

```text
L_2[f] = a f' - 6xf.
```

## Selector 1: Weighted-Adjoint Closure

Under the projection weight:

```text
w = a^4,
```

integration by parts gives:

```text
<L_m f, g>_w
=
[a^5 f g]_0^1
+
<f, L_m^* g>_w
```

where:

```text
L_m^*[g] = -a g' + 2m xg.
```

Compare this with:

```text
L_(5-m)[g] = a g' - 2m xg.
```

Therefore:

```text
L_m^* = -L_(5-m).
```

This is a real structural result.

But it does not select `m = 2`.

Instead, it pairs the family members:

```text
m = 1 <-> m = 4
m = 2 <-> m = 3
m = 3 <-> m = 2
m = 4 <-> m = 1
```

The fixed skew-adjoint value would be:

```text
m = 5/2,
```

which is not an integer primitive power.

So adjoint closure does not independently select the observed case.

Result:

```text
adjoint selector for m = 2:
  failed

adjoint structure:
  real, but family-wide

best it gives:
  the adjacent pair {{2,3}}, not m = 2 alone
```

## Selector 2: Exponent Ladder

For general `m`, the exponent roles are:

```text
primitive factor:       a^m
operator flux factor:   a^(5 - m)
projection weight:      a^4
IBP boundary factor:    a^5
```

For `m = 2`, this becomes:

```text
primitive factor:       a^2
operator flux factor:   a^3
projection weight:      a^4
IBP boundary factor:    a^5
```

or:

```text
a^2 -> a^3 -> a^4 -> a^5.
```

If one requires the ordered adjacent ladder:

```text
primitive -> flux -> weight -> boundary
```

to climb by one exponent at each step, then:

```text
m = 2
```

is selected.

This is suggestive.

But it is not yet an independent derivation unless the ordering principle itself is justified.

The adjoint-pair symmetry naturally gives the pair:

```text
{{2, 3}}
```

because:

```text
m <-> 5 - m.
```

Choosing the lower member `m = 2` requires an additional orientation:

```text
primitive before flux,
or lower endpoint order before higher flux order,
or a directed integration-by-parts interpretation.
```

That orientation may be reasonable, but it is not yet forced.

Result:

```text
exponent-ladder selector:
  suggestive

strict ordered ladder:
  selects m = 2

independent derivation:
  not yet
```

## Selector 3: Compactified Radial Measure

A possible independent selector would be a compactified radial measure.

Test a generic compactification family:

```text
r = x / a^c,    c > 0.
```

Then:

```text
dr/dx = a^(-c - 1)[1 + (2c - 1)x^2].
```

An `n`-dimensional radial measure gives:

```text
r^(n - 1) dr
=
x^(n - 1)[1 + (2c - 1)x^2] a^(-cn - 1) dx.
```

The important part is the power of `a`:

```text
a^(-cn - 1).
```

For:

```text
c > 0
n > 0
```

this is a negative power.

It cannot equal the positive projection weight:

```text
a^4.
```

The standard compactification:

```text
r = x / sqrt(1 - x^2)
```

has:

```text
c = 1/2
```

and gives measure exponent:

```text
-(n + 2)/2.
```

To equal `+4`, it would formally require:

```text
n = -10,
```

which is not a positive dimension.

Therefore:

```text
compactified radial measure alone:
  does not produce w = a^4
```

A compactified measure could still contribute if multiplied by an additional envelope, decay factor, density, or variational weight. But then `m = 2` is not selected by compactification alone.

Result:

```text
compactification-alone selector:
  failed

compactification plus extra envelope:
  possible, but would be a new assumption
```

## Combined Result

The three selector tests give:

```text
m = 2 from observed projection ratio:
  yes

m = 2 from adjoint closure:
  no

m = 2 from ordered exponent ladder:
  suggestive only

m = 2 from compactified radial measure alone:
  no

m = 2 independent derivation:
  not achieved
```

This is not a total failure.

It means the projection hierarchy remains:

```text
formal but structured
```

rather than:

```text
independently derived from operator/domain geometry.
```

## Updated Status

```text
psi_k origin:
  derived

L operator:
  derived

primitive family artifact risk:
  confirmed

m = 2 selector:
  observed-ratio selection only

adjoint structure:
  family pairing m <-> 5 - m

exponent ladder:
  strongest remaining clue

compactified measure:
  does not select m = 2 alone

physical interpretation:
  still closed
```

## Stop Rule

Do not keep adding selector tests unless a concrete new object appears.

Concrete objects could include:

```text
specific measure
specific boundary condition
specific variational functional
specific compactification with required envelope
specific source-signature theorem
specific self-adjoint domain
```

Labels do not count.

Without a new object, stop here and record:

```text
m = 2 is selected by the observed projection hierarchy,
not independently derived.
```

That is a valid result.

## Recommended Next Move

Do not start physical interpretation yet.

Do not start parent-equation construction.

Do not start broad source-signature mining.

The safest next action is to update the branch README/status to say:

```text
The projection hierarchy has a real IBP/operator structure,
but m = 2 has not been independently selected.
The branch remains formal but structured.
```

Then pause.

Only continue if the next step begins from a concrete object, not a new possible meaning.

## Validation Summary

The generating script validated:

```text
{validation_bullets}
```

## Bottom Line

The best current answer is:

```text
m = 2 is real within the observed projection hierarchy,
but not yet forced independently.
```

The hierarchy has survived the first origin tests, but it has not crossed the physical interpretation gate.

This branch should now be contained.
"""

out = Path("4_m2_selector_tests.md")
out.write_text(md, encoding="utf-8")

print("All symbolic checks passed.")
print(f"Wrote {out.resolve()}")
