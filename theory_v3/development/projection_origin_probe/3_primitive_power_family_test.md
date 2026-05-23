# Primitive Power Family Test

## Purpose

The previous two notes showed that:

```text
psi_k
```

comes from a boundary-vanishing primitive, and that the pullback lands on the weighted-divergence operator:

```text
L[f] = (1 - x^2)f' - 6xf.
```

This note tests the main danger:

```text
Is the observed primitive power m = 2 distinguished,
or does every primitive power m give an equally plausible construction?
```

The test family is:

```text
G_(k,m)(x) = x^(2k - 1)(1 - x^2)^m.
```

Let:

```text
a = 1 - x^2.
```

Then:

```text
G_(k,m)(x) = x^(2k - 1)a^m.
```

## Status

Current result:

```text
Every m gives a formal derivative identity.
For the regular flux-power range 1 <= m <= 5, the IBP pullback validates directly.
The observed m = 2 is selected by the observed ratio r_k = (2k - 1)/(2k + 3).
The observed m = 2 also gives the balanced adjacent ladder a^2 -> a^3 -> a^4 -> a^5.
Boundary cleanliness alone does not distinguish m = 2.
Physical meaning remains open.
```

This is a useful but dangerous result.

It strengthens the formal derivation while also showing that the construction has a family-artifact risk.

## 1. General Derivative Identity

Start with:

```text
G_(k,m)(x) = x^(2k - 1)a^m.
```

Differentiate:

```text
G'_(k,m)
=
(2k - 1)x^(2k - 2)a^m
-
2m x^(2k)a^(m - 1).
```

Factor:

```text
G'_(k,m)
=
a^(m - 1)x^(2k - 2)[(2k - 1)a - 2mx^2].
```

Since:

```text
a = 1 - x^2,
```

this becomes:

```text
G'_(k,m)
=
a^(m - 1)x^(2k - 2)[(2k - 1) - (2k + 2m - 1)x^2].
```

Therefore:

```text
G'_(k,m)
=
-(2k + 2m - 1)a^(m - 1) psi_(k,m)(x),
```

where:

```text
psi_(k,m)(x)
=
x^(2k) - r_(k,m)x^(2k - 2)
```

and:

```text
r_(k,m) = (2k - 1)/(2k + 2m - 1).
```

## 2. Observed Case

The original projection hierarchy used:

```text
r_k = (2k - 1)/(2k + 3).
```

The general family gives:

```text
r_(k,m) = (2k - 1)/(2k + 2m - 1).
```

Matching the observed denominator requires:

```text
2k + 2m - 1 = 2k + 3
```

so:

```text
m = 2.
```

Thus the previously derived primitive:

```text
G_(k,2)(x) = x^(2k - 1)(1 - x^2)^2
```

is exactly the member selected by the observed projection ratio.

## 3. General Pullback Operator

The projection weight remains:

```text
w = a^4.
```

The derivative identity gives:

```text
psi_(k,m)
=
-1 / [(2k + 2m - 1)a^(m - 1)]
d/dx[x^(2k - 1)a^m].
```

Then:

```text
integral psi_(k,m) f a^4 dx
=
-1/(2k + 2m - 1)
integral f a^(5 - m) G'_(k,m) dx.
```

Let:

```text
H_m[f] = f a^(5 - m).
```

Integrating by parts gives:

```text
integral psi_(k,m) f a^4 dx
=
-1/(2k + 2m - 1)[H_m G_(k,m)]_0^1
+
1/(2k + 2m - 1)
integral G_(k,m) H_m' dx.
```

Now:

```text
H_m'
=
a^(4 - m)[a f' - 2(5 - m)xf].
```

Define:

```text
L_m[f] = a f' - 2(5 - m)xf.
```

Then:

```text
G_(k,m)H_m'
=
x^(2k - 1)a^m a^(4 - m)L_m[f]
=
x^(2k - 1)a^4 L_m[f].
```

Therefore, when the endpoint term is clean:

```text
integral psi_(k,m) f a^4 dx
=
1/(2k + 2m - 1)
integral x^(2k - 1)a^4 L_m[f] dx.
```

For `m > 5`, `H_m = f a^(5-m)` contains negative powers at `a=0`. The formal algebra still gives the same expression, but endpoint regularity would need separate treatment. The script directly validates the regular nonnegative flux-power range:

```text
1 <= m <= 5.
```

## 4. Boundary Term

The boundary term is:

```text
H_m G_(k,m)
=
f a^(5 - m) x^(2k - 1)a^m
=
f x^(2k - 1)a^5.
```

This is independent of `m`.

That means boundary cleanliness alone does not select the observed case.

At `x = 1`, the factor `a^5` vanishes for regular `f`.

At `x = 0`, the factor `x^(2k - 1)` vanishes for `k >= 1`.

So the IBP boundary term is clean for the regular primitive-power family, not only for `m = 2`.

This is the main warning.

## 5. The Observed Operator As One Family Member

The general pullback operator is:

```text
L_m[f] = a f' - 2(5 - m)xf.
```

For `m = 2`:

```text
L_2[f] = a f' - 6xf.
```

This is exactly the operator found in the previous note:

```text
L[f] = (1 - x^2)f' - 6xf.
```

So `L` is not isolated. It is the `m = 2` member of a family of pullback operators.

## 6. Exponent Structure

For general `m`, the exponent roles are:

```text
primitive factor:       a^m
operator flux factor:   a^(5 - m)
projection weight:      a^4
IBP boundary factor:    a^5
```

For the observed case `m = 2`, this becomes:

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

This adjacent exponent ladder is special to `m = 2`.

However, adjacency is not yet a derivation of physical meaning. It is a structural clue.

## 7. Interpretation

This test changes the status of the branch.

Positive result:

```text
The observed psi_k is still derived.
The observed ratio still selects m = 2.
The operator L is still the pullback operator for that selected primitive.
The exponent ladder for m = 2 is unusually clean.
```

Danger result:

```text
The existence of an IBP pullback is not unique to m = 2.
Boundary cleanliness is not unique to m = 2.
A family of psi_(k,m) and L_m operators exists.
```

Therefore:

```text
m = 2 is distinguished by the observed projection hierarchy,
not yet by an independent boundary or operator principle.
```

## 8. Updated Status

```text
psi_k origin:
  derived

m = 2 selection from observed ratio:
  derived

general primitive family:
  derived

boundary cleanliness selecting m = 2:
  failed

adjacent exponent ladder selecting m = 2:
  suggestive, not decisive

L[f]:
  m = 2 member of general L_m family

physical interpretation:
  still open
```

## 9. What This Means For The Project

This is not a kill result, but it is a warning.

The projection-origin thread remains alive because the observed hierarchy selects a precise member of the family:

```text
m = 2.
```

But the thread is weaker if it cannot explain why that member should arise before observing the ratio.

The next decisive question is therefore:

```text
Can m = 2 be derived independently?
```

Possible independent selectors:

```text
the projection weight a^4
regular adjacent exponent ladder a^2 -> a^3 -> a^4 -> a^5
a boundary/domain dimension count
a compactified radial measure
a flux regularity condition
a variational or adjoint closure condition
a source-signature requirement
```

If none of these selects `m = 2`, then the construction may remain formal admissibility machinery.

## Validation Summary

The generating script validated:

```text
- primitive derivative identity grid M=1..8: passed
- m=2 observed ratio: passed
- H derivative / pullback / boundary identities grid M=1..5: passed
- m=2 operator specialization: passed
- finite polynomial pullback grid K=1..5 M=1..5: passed
- adjacent exponent ladder identifies m=2: passed
```

## Bottom Line

The family test found the main artifact danger.

For primitive powers:

```text
G_(k,m)(x) = x^(2k - 1)(1 - x^2)^m,
```

there is a corresponding row:

```text
psi_(k,m)(x)
=
x^(2k) - ((2k - 1)/(2k + 2m - 1))x^(2k - 2),
```

and, in the regular flux-power range, a corresponding pullback operator:

```text
L_m[f]
=
(1 - x^2)f' - 2(5 - m)xf.
```

The observed hierarchy corresponds to:

```text
m = 2.
```

That case is special because it matches the observed ratio and gives the clean adjacent ladder:

```text
a^2 -> a^3 -> a^4 -> a^5.
```

But the mere existence of the IBP construction does not select it.

The next test should be:

```text
derive or kill an independent selector for m = 2.
```
