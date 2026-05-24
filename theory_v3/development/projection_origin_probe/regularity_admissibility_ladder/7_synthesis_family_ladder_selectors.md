# Synthesis Proof 7: Family, Ladder, and Selector Tests

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

- primitive derivative identity grid M=1..8: passed
- observed ratio selects m=2: passed
- L_2 operator specialization: passed
- family weighted adjoint identity grid M=1..5: passed
- adjoint pairing L_m^*=-L_(5-m): passed
- skew-adjoint fixed point m=5/2, no integer M=1..5: passed
- ordered adjacent ladder selects m=2 for beta=4: passed
- general beta ladder gives m=beta/2 and beta=4 for four-term chain: passed
- compactification derivative grid c=1/2,1,2: passed
- compactified radial measure cannot yield a^4 for positive c,n: passed

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
