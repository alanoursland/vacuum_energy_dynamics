# Einstein-Hilbert Origin Tests: Status After Proofs 109-113

## What This Batch Adds

Proofs `109` through `113` close the remaining weak-field and Lovelock-gate
bookkeeping around the Einstein-Hilbert origin tests.

## Cosmological Constant Gate

Proof `109` validates:

```text
Phi = -GM/r - Lambda r^2/6
Delta Phi = -Lambda
```

outside localized matter.

So the cosmological term is allowed by the Lovelock gate, but it is a separate
vacuum-background branch. The asymptotically flat scalar boundary-flux bridge is
the `Lambda=0` sector unless nonzero vacuum curvature is independently supplied.

## Gauss-Bonnet Gate

Proof `110` validates the dimensional status of Gauss-Bonnet:

```text
D < 4: vanishes
D = 4: topological
D > 4: dynamical
```

In four dimensions it can affect topology or boundary bookkeeping, but it does
not add local second-order metric dynamics.

## Reduced Newtonian EH Source Sign

Proof `111` validates the trace-reversed Newtonian-sector source normalization:

```text
B = bar h_00 = -4 Phi
-Delta B = 16*pi*G rho
```

and the reduced interaction:

```text
E_cross = -G M1 M2/d.
```

This ties the EH weak-field source coupling to the scalar boundary-flux reduced
action with the standard attractive sign.

## Metric Variable Selection

Proof `112` validates two selection gates:

```text
symmetric metric perturbation in 4D -> 2 massless spin-2 degrees of freedom
metric source coupling gauge invariance -> partial_a T^ab = 0
```

This supports the metric as the correct universal lift variable, while still
leaving the ontology-to-metric derivation open.

## Projection Ladder to Boundary Flux

Proof `113` validates the exact chain:

```text
r_k = (2k-1)/(2k+3)
  = R=0 regularity-ladder ratio
  -> m=2 primitive level
  -> u=a^3 f transform
  -> L*_w L[f]=S equivalent to -u''=aS
  -> integral aS dx is the boundary-flux defect.
```

This is the clean bridge from the original projection row to the later scalar
and geometric boundary-flux interpretation.

## Current Impact

The proof chain now establishes:

```text
1. The original ratio is a regularity/admissibility ratio.
2. The admissibility defect is a boundary-flux quantity.
3. Boundary flux in three spatial dimensions gives the inverse-square field.
4. The scalar field lifts to the Newtonian sector of linearized geometry.
5. Linearized geometry requires the Fierz-Pauli / linearized Einstein operator.
6. Einstein-Hilbert contains that linearized operator.
7. Under the Lovelock gate, EH is the unique four-dimensional nonlinear local
   metric completion up to Lambda and topological terms.
```

## What Is Still Not Proven

The remaining gap is specific:

```text
The proof chain has not yet derived the Lovelock gate assumptions from the
vacuum-energy ontology.
```

Still open:

```text
why the vacuum configuration variable must be the metric;
why the nonlinear action must be local, metric-only, diffeomorphism invariant,
and second order;
why no additional thermodynamic/vacuum state variables survive into the
macroscopic field equation;
whether the cosmological constant is forced to vanish, forced nonzero, or free;
whether the original projection ladder fixes the EH boundary term rather than
only matching its weak-field boundary flux.
```

## Destination

The direction is now clear:

```text
regularity ladder
  -> boundary flux
  -> scalar inverse-square bridge
  -> linearized metric geometry
  -> Einstein-Hilbert nonlinear completion gate
  -> ontology-derived action principle.
```

The next proof folder should not keep re-proving the weak-field bridge. It
should test the ontology-to-action step: what assumptions on vacuum energy,
configuration variables, locality, covariance, and boundary bookkeeping force
the Einstein-Hilbert action rather than merely allow it.
