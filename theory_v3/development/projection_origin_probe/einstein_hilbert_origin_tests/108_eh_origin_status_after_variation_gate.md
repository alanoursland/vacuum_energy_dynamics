# Einstein-Hilbert Origin Tests: Status After Proofs 103-107

## Main Update

This batch strengthens the Einstein-Hilbert origin chain in three ways:

```text
1. variation structure;
2. boundary bookkeeping;
3. nonlinear action selection gate.
```

## Variation Structure

Proof `103` validates the Palatini identity:

```text
delta R_ab
  =
  nabla_c(delta Gamma^c_ab)
  - nabla_b(delta Gamma^c_ac).
```

This is the identity behind the statement that varying curvature produces a
bulk Einstein term plus boundary terms.

## Boundary Bookkeeping

Proof `104` validates a toy model for the GHY role:

```text
-q q'' + d(q q')/dx = (q')^2.
```

The boundary term removes derivative-of-variation boundary data. This mirrors
why Einstein-Hilbert needs a boundary term for a well-posed fixed-metric
variation.

## Linearized Action Recovery

Proof `105` validates:

```text
L_GG^(2) = 1/2 h^ab G_ab[h].
```

So the Gamma-Gamma part of Einstein-Hilbert linearizes directly to the
Fierz-Pauli / linearized Einstein action.

## Boundary Mass

Proof `106` validates the weak-field agreement of ADM, Komar, metric flux, and
scalar bridge flux:

```text
Q_scalar = 4*pi*G M.
```

This supports the earlier boundary-flux interpretation in standard weak-field
geometric terms.

## Selection Gate

Proof `107` records the Lovelock gate:

```text
local metric-only diffeomorphism-invariant second-order field equations in 4D
  -> cosmological term + Einstein-Hilbert + topological Gauss-Bonnet.
```

Under those assumptions, EH is the unique dynamical nonlinear metric action.

## Current State

The Einstein-Hilbert action now passes these origin tests:

```text
EH contains Gamma-Gamma connection strain plus boundary divergence.
EH linearizes to Fierz-Pauli.
EH recovers the Newtonian scalar boundary-flux sector.
EH has the standard ADM/Komar boundary mass normalization.
EH is selected by the Lovelock gate if the gate assumptions are accepted.
```

## What Is Still Not Proven

The open issue has sharpened.

Not yet proven:

```text
that the vacuum-energy ontology itself forces the Lovelock gate assumptions;
that the metric is uniquely the vacuum configuration variable;
that the EH boundary term/source coupling is forced by the original
regularity/admissibility ladder;
that no additional matter/vacuum thermodynamic terms are present.
```

## Next Proof Targets

The next useful tests are:

```text
109_cosmological_constant_gate.py
110_gauss_bonnet_topological_4d_gate.py
111_eh_plus_boundary_source_reduced_newtonian.py
112_metric_variable_selection_tests.py
113_projection_ladder_to_boundary_flux_summary.py
114_einstein_hilbert_origin_status.py
```

The next question is no longer whether EH contains the weak-field bridge. It
does. The question is whether the vacuum ontology selects the assumptions that
make EH the unique nonlinear completion.
