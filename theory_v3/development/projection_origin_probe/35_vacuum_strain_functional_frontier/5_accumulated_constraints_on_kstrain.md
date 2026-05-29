# 5. Accumulated Constraints on K_strain

The strain functional is not unconstrained.

The proof chain has already built a narrow enclosure around any acceptable `K_strain`.

## Constraint 1: metric reduction at lowest order

The strain branch must reduce to the metric/Hessian response supplied by local directional probes:

```text
Q_p(v) -> g_ab(p) v^a v^b.
```

A residual that destroys the metric limit is not a small extension; it is a different branch.

## Constraint 2: exact or routed quadratic response

Nonquadratic response cannot be hidden inside the metric branch.

It must either vanish in the metric limit or be routed explicitly:

```text
K_strain = K_EH + ε K_residual.
```

## Constraint 3: calibration coherence

The strain functional must preserve shared interval calibration unless it carries an explicit nonmetric/Weyl-drift field.

This pressures against hidden nonmetricity.

## Constraint 4: diffeomorphism / relabeling invariance

The strain functional cannot depend on a preferred coordinate labeling or hidden frame unless that structure is promoted to an explicit physical field.

## Constraint 5: Lorentzian hyperbolicity

The strain functional must support causal propagation with a universal cone structure in the GR limit.

Branches with elliptic, parabolic, dissipative, or medium-like behavior need explicit routing.

## Constraint 6: two TT degrees of freedom

The propagating tensor sector must reduce to the two massless spin-2 polarizations in the GR branch.

Extra modes require explicit routing.

## Constraint 7: boundary differentiability

The action must have a well-defined variational principle under the admissible boundary conditions.

This is the EH/GHY-style boundary closure constraint generalized to any residual branch.

## Constraint 8: symplectic radiation ledger

Radiative flux, news, and memory must live in the tensor symplectic boundary ledger rather than being double-counted as scalar monopole charge.

## Constraint 9: source-ledger purity

Residual strain terms must not duplicate matter source, scalar flux, Lambda baseline, torsion current, or nonmetric calibration drift unless they explicitly introduce those ledgers.

## Summary

The accumulated gates constrain the frontier to a residual problem around the Einstein branch:

```text
K_strain = K_EH + ε K_residual.
```

The work is to determine whether the constraints force `ε = 0`, allow a consistent nonzero residual, or expose the need for a new strain axiom.
