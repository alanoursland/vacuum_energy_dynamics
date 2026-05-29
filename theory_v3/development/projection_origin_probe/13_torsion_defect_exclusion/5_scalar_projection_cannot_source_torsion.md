# Torsion Defect Exclusion 5: Scalar Projection Cannot Source Torsion

## Purpose

This proof checks the scalar projection/admissibility channel.

A scalar can form a trace/isotropic object, but it does not provide an
antisymmetric torsion source unless an additional oriented or antisymmetric
carrier is supplied.

## Validated Checks

- scalar-isotropic tensor has zero antisymmetric contraction: passed
- torsion source from a scalar requires an extra carrier: passed

## Scalar Channel

Let a scalar projection output be:

```text
s.
```

The canonical isotropic tensor it can form is:

```text
s delta_ij.
```

For an antisymmetric candidate:

```text
A_ij = -A_ji,
```

Sympy verifies:

```text
sum_ij s delta_ij A_ij = 0.
```

## Extra Carrier Requirement

A scalar torsion source would need a separate oriented carrier:

```text
J_torsion = eta s.
```

The dependence on `eta` is explicit:

```text
dJ_torsion/deta = s.
```

## Interpretation

The scalar projection ladder cannot silently source torsion. If it is used to
build a torsion source, the missing oriented/antisymmetric carrier is a new
physical datum and must be routed explicitly.
