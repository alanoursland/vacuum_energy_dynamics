# Synthesis Proof 13: Energy Minimization in the `u = a^3 f` Variable

## Purpose

This report validates the strongest energy-minimization simplification in the
synthesis:

```text
u = a^3 f.
```

Under this change of variable, the weighted first-order energy becomes an
ordinary one-dimensional Dirichlet energy.

## Validated Identities

- operator transform: passed
- quadratic energy density transform: passed
- source coupling transform: passed
- variation quadratic density transform: passed
- variation source density transform: passed
- transformed parent operator: passed
- Euler-Lagrange equivalence: passed
- u-variable variation identity: passed
- constant-u null mode: passed

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
