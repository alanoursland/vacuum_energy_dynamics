# Vacuum Dimension Selector 14: Scalar And Vector Mode Mismatch

## Purpose

This proof prevents a common counting mistake: matching a number of degrees of
freedom is not the same as matching the field type.

## Validated Checks

- in `D=4`, a massless vector and a massless spin-2 field both have two
  propagating degrees of freedom: passed
- scalar, vector, and symmetric tensor ranks are distinct: passed

## Computation

```text
N_scalar = 1
N_vector(D) = D - 2
N_spin2(D) = D*(D - 3)/2
N_vector(4) = 2
N_spin2(4) = 2
```

But the field ranks differ:

```text
scalar rank = 0
vector rank = 1
symmetric metric perturbation rank = 2
```

## Interpretation

The weak-field GR lift needs a symmetric rank-2 field, not merely any field with
two modes. Vector and scalar branches remain separate candidate branches unless
an independent argument excludes or embeds them.
