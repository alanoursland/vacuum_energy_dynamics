# Field Search Survivor Audit 9: Archive-to-Math Interpretation

## Purpose

This report captures the useful interpretive synthesis from the archive
without importing overstrong claims.

The archive supports a strong historical statement:

```text
r_k was not imported from a named classical basis.
r_k survived a bottom-up search through exactness, moment suppression,
source-safety, and projection constraints.
```

The archive does not yet support:

```text
the hierarchy is the parent field equation;
the hierarchy is the matter source law;
the projection matrix is a positive energy Hessian;
the projection source is physically identified.
```

## Validated Checks

- observed ratio is the auxiliary/contact a-weight moment ratio: passed
- projection-weight a^4 zero-mean ratio would be (2k-1)/(2k+9): passed
- observed ratio is not the ordinary same-weight a^4 zero-mean ratio: passed
- primitive identity explains the auxiliary/contact moment cancellation: passed

## What The Archive Adds

### 1. The Search Did Not Start From A Named Basis

The row family:

```text
psi_k = x^(2k) - ((2k-1)/(2k+3)) x^(2k-2)
```

is best read as a survivor of the search tree, not as a standard special
function pulled from a table.

The archive first isolated the ratio through the Group 88 moment-hierarchy
identity:

```text
M_(2k)=0
  iff
I_k(P) = ((2k-1)/(2k+3)) I_(k-1)(P).
```

The later primitive identity explains why that survivor has a compact
operator form.

### 2. The Important Weight Distinction

A common misreading is:

```text
psi_k is orthogonal to constants under the projection weight a^4.
```

That is false.

The observed ratio is:

```text
(2k-1)/(2k+3).
```

The direct same-weight zero-mean ratio under:

```text
w = a^4 = (1-x^2)^4
```

would be:

```text
(2k-1)/(2k+9).
```

The observed ratio is instead the auxiliary/contact-weight ratio under:

```text
a = 1-x^2.
```

Equivalently:

```text
integral_0^1 a psi_k dx = 0.
```

That is why the primitive identity is so clean:

```text
d/dx [x^(2k-1) a^2]
  =
  -(2k+3) a psi_k.
```

The projection weight `a^4` enters later through the pullback and energy
pairing, not as the same-weight zero-mean rule for `psi_k`.

### 3. Primitive Identity Is Stronger Than Zero Integral

It is true that any one-dimensional integrand with zero total integral can be
written as the derivative of a boundary-matched primitive after choosing an
antiderivative.

But the actual result is stronger:

```text
x^(2k-1) a^2
```

is a closed monomial-times-boundary-envelope primitive, and differentiating it
produces exactly:

```text
-(2k+3) a psi_k.
```

So the primitive identity is not merely a generic consequence of zero integral.
It is a compact structural explanation of the survivor ratio.

### 4. What The Guardrails Mean

Groups 98 through 101 correctly prevent the following promotions:

```text
projection hierarchy -> physical field equation
projection hierarchy -> matter source law
projection matrix -> positive Hessian
formal source vector -> identified physical source
```

The current role remains:

```text
AUXILIARY_ADMISSIBILITY_CANDIDATE
```

with a proved mathematical spine.

### 5. Why The Source-Safety Work Matters

The count-once, residual-nonentry, scalar-tail, and boundary-flux checks
explain why an admissibility filter of this kind is relevant to the broader
field-equation search.

They protect against:

```text
ordinary source duplication;
residual reentry as metric/source content;
unlicensed scalar 1/r tails;
boundary shell leakage;
mass shifts from nominally neutral sectors.
```

Those checks do not prove that the projection hierarchy is the field equation.
They prove necessary safety gates any later source-origin theorem has to pass.

## Corrected One-Paragraph Reading

The archive shows a bottom-up survivor: a two-term moment row basis produced
by exactness, moment-suppression, and source-safety constraints, later
explained by a boundary-vanishing primitive and a weighted divergence operator.
The ratio is a beta/moment-contact ratio, not a named classical OPS coefficient
and not the same-weight zero-mean ratio for `w=a^4`. The current mathematical
status is strong: a custom boundary-adapted Galerkin/admissibility row family
with a clean operator pullback. The physical status remains guarded: it is a
candidate admissibility filter, not yet a derived covariant field equation or
matter source law.
