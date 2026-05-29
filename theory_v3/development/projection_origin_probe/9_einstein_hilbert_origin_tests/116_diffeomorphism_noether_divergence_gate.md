# Einstein-Hilbert Origin Test 116: Diffeomorphism Noether Divergence Gate

## Purpose

This report validates the local bookkeeping behind the statement:

```text
diffeomorphism gauge invariance
  -> divergence-free geometric field equation.
```

The proof is a flat symbolic model. It records the integration-by-parts
identity that survives in covariant form.

## Validated Checks

- gauge variation is boundary plus field divergence residual: passed
- field equation divergence matches source conservation bookkeeping: passed

## Gauge Variation

For a symmetric field equation tensor `E_ab` and:

```text
delta h_ab = partial_a xi_b + partial_b xi_a,
```

the variation density is:

```text
1/2 E^ab delta h_ab = E^ab partial_a xi_b.
```

SymPy verifies:

```text
E^ab partial_a xi_b
  = boundary divergence
    - xi_b partial_a E^ab.
```

Therefore gauge invariance for arbitrary `xi_b` requires:

```text
partial_a E^ab = 0
```

up to the corresponding covariant replacement in nonlinear geometry.

## Source Bookkeeping

For:

```text
E_ab = kappa T_ab,
```

the total equation has consistent gauge bookkeeping only when the same
divergence identity is matched by source conservation.

## Interpretation

This is the action-level reason the nonlinear metric equation must have a
covariant divergence identity. The Einstein tensor has this identity through
the contracted Bianchi identity, which is why it can couple consistently to
conserved stress-energy.
