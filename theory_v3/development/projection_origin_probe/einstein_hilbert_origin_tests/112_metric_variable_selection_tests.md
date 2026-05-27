# Einstein-Hilbert Origin Test 112: Metric Variable Selection Tests

## Purpose

This report records algebraic tests that support the metric perturbation as the
correct weak-field geometric variable once the scalar boundary-flux bridge is
lifted to a universal field theory.

This is not yet a derivation of the metric from the vacuum ontology. It is a
selection gate.

## Validated Checks

- massless spin-2 dof formula: passed
- four-dimensional graviton dof count: passed
- three-dimensional local graviton dof count: passed
- four-dimensional vector dof count: passed
- scalar dof count: passed
- metric source gauge variation is boundary plus conservation residual: passed

## Degree-of-Freedom Gate

A symmetric rank-two perturbation in `D` dimensions has:

```text
D(D+1)/2
```

components. Linearized diffeomorphism gauge structure removes `2D` phase-space
degrees of freedom, leaving:

```text
D(D-3)/2.
```

In four dimensions:

```text
D(D-3)/2 = 2.
```

This is the massless spin-2 count.

## Source-Coupling Gate

For:

```text
delta h_ab = partial_a xi_b + partial_b xi_a,
S_source = (1/2) integral h_ab T^ab,
```

SymPy verifies in a two-coordinate symbolic model:

```text
(1/2)T^ab delta h_ab
  = boundary divergence
    - xi_b partial_a T^ab.
```

So the source coupling is gauge invariant up to a boundary term exactly when:

```text
partial_a T^ab = 0.
```

## Interpretation

The scalar field alone carries the Newtonian potential, but the universal
conserved-source lift requires the symmetric metric perturbation. This supports
the route:

```text
scalar boundary flux
  -> Newtonian metric sector
  -> linearized spin-2 field
  -> Einstein-Hilbert nonlinear completion under the Lovelock gate.
```
