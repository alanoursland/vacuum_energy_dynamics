# Field Search Survivor Audit 2: Corrected r_k Provenance

## Purpose

This report reconstructs the corrected provenance of:

```text
r_k = (2k - 1)/(2k + 3).
```

The historical archive route is Group 88's moment-ratio identity. The later
primitive identity is a compact explanation of the same ratio, not the original
discovery route.

## Validated Checks

- Group 88 row moment-ratio integrand: passed
- later primitive identity explaining r_k: passed
- auxiliary moment ratio: passed
- endpoint-contact ladder beta ratio: passed
- original ratio is R=0 ladder row: passed
- projection-weight zero-mean ratio differs: passed

## Historical Route: Group 88 Moment Ratio

Group 88 introduced:

```text
I_k(P) = integral_0^1 t^(k-1/2)(1-t)^4 P(t) dt.
```

The finite hierarchy condition was:

```text
I_k(P) = ((2k - 1)/(2k + 3)) I_(k-1)(P).
```

Equivalently, under:

```text
mu(t) = t^(-1/2)(1-t)^4,
q_k(t) = t^k - r_k t^(k-1),
```

the row test is:

```text
integral_0^1 q_k(t) P(t) mu(t) dt = 0.
```

SymPy verifies this row-integrand form directly for a monomial probe.

## Later Compact Proof: Primitive Identity

With:

```text
a = 1 - x^2
psi_k = x^(2k) - r_k x^(2k-2),
```

The later first-series proof verifies:

```text
d/dx [x^(2k-1)a^2]
  =
  -(2k+3)a psi_k.
```

Expanding the derivative explains the same ratio:

```text
r_k = (2k - 1)/(2k + 3).
```

## Auxiliary Moment Cancellation

The same ratio is also recovered from the auxiliary same-row moment condition:

```text
integral_0^1 psi_k(x)(1-x^2) dx = 0.
```

The ratio is:

```text
[integral x^(2k)(1-x^2) dx]
/
[integral x^(2k-2)(1-x^2) dx]
=
(2k-1)/(2k+3).
```

## Endpoint-Contact Ladder

The endpoint-contact/admissibility ladder ratio is:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

The later ladder verifies that the observed ratio is:

```text
R = 0.
```

This is a base boundary-contact/admissibility level. It is not an independent
physical derivation of `R=0`.

## Not Same-Weight Projection Orthogonality

Under the projection weight `(1-x^2)^4`, the zero-mean ratio would be:

```text
(2k - 1)/(2k + 9).
```

That is not the observed ratio. The observed ratio belongs to the archived
moment-ratio row object and later primitive / admissibility structure, not to
ordinary zero-mean Gram orthogonality under the projection weight.

The beta-ratio step uses the exact recurrence:

```text
B(z+1,5)/B(z,5) = z/(z+5),
```

with `z = k - 1/2`.

## Provenance Status

```text
Group 88: original archived moment-ratio route.
1_psi_k_ibp_origin: later compact primitive proof.
regularity_admissibility_ladder: later R=0 base-contact interpretation.
```
