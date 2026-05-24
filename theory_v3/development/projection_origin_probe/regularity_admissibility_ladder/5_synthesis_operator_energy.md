# Synthesis Proof 5: Operator and Energy Structure

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

- primitive derivative identity: passed
- pullback integrand identity: passed
- operator divergence form: passed
- wrong rescaling rejected: passed
- transformed variable operator: passed
- Dirichlet energy simplification: passed
- weighted adjoint integrand identity: passed
- Lstar L composition: passed
- L Lstar composition: passed
- zeroth-order composition residue: passed
- variational integrand identity: passed

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
