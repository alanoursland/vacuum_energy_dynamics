#!/usr/bin/env python3
"""
make_120_ontology_action_gate_status.py

Generate a status report after proofs 115-119.

Output:
    120_ontology_action_gate_status.md
"""

from pathlib import Path


md = """# Einstein-Hilbert Origin Tests: Status After Proofs 115-119

## What This Batch Adds

Proofs `115` through `119` test the ontology-to-action gates that sit between
the scalar/linear bridge and the full Einstein-Hilbert action.

## Levi-Civita Selection

Proof `115` validates:

```text
metric + torsion-free connection + metric compatibility
  -> unique Levi-Civita connection.
```

This means that once the macroscopic vacuum configuration is a metric and the
connection is required to preserve it without torsion, the strain object is
fixed.

## Diffeomorphism Noether Gate

Proof `116` validates the integration-by-parts identity:

```text
E^ab partial_a xi_b
  = boundary divergence - xi_b partial_a E^ab.
```

This is the flat symbolic version of:

```text
diffeomorphism invariance -> covariant divergence identity.
```

It explains why a consistent universal metric field equation must have a
divergence-free left side.

## Curvature-Squared Exclusion

Proof `117` validates the derivative-order gate:

```text
EH field equation      ~ k^2 h
curvature-squared term ~ k^4 h.
```

So if the macroscopic equation must remain second order, generic `R^2` and
`Ricci^2` corrections are excluded.

## EH Strain Split

Proof `118` validates, in the conformal sector:

```text
sqrt(g)R = boundary divergence
           + (D-1)(D-2) exp((D-2)s)|grad s|^2.
```

This is a compact nonlinear check that EH is connection strain plus boundary
bookkeeping.

## Nonlinear Bianchi Check

Proof `119` validates on flat-FRW:

```text
nabla_a G^a_b = 0.
```

This confirms the nonlinear consistency identity that source coupling requires.

## Current Interpretation

The chain now has a sharper conditional form:

```text
if the macroscopic vacuum configuration is a metric,
if its connection is torsion-free and metric-compatible,
if the action is local and diffeomorphism invariant,
if the field equation is second order,
if the theory is four-dimensional,
then the Einstein-Hilbert action is the selected nonlinear bulk action,
up to Lambda and topological boundary terms.
```

## What Is Still Open

The remaining unproven step is not inside standard differential geometry. It is
the origin step:

```text
vacuum-energy ontology
  -> metric as macroscopic configuration variable
  -> torsion-free metric-compatible connection
  -> local diffeomorphism-invariant second-order action.
```

That is the next target. The EH side of the bridge is now heavily constrained;
the open work is to derive the bridge assumptions from the vacuum framework
rather than import them from standard geometry.

## Next Proof Targets

Useful next tests:

```text
121_metric_from_local_distance_or_interval_gate.py
122_torsion_gate_and_why_it_is_absent_or_allowed.py
123_locality_gate_for_vacuum_energy_density.py
124_boundary_term_variation_fuller_model.py
125_ontology_to_eh_assumption_table.py
```

These should focus on assumption origin, not on revalidating the weak-field
Newtonian sector.
"""

out = Path(__file__).with_name("120_ontology_action_gate_status.md")
out.write_text(md, encoding="utf-8")

print(f"Wrote {out.resolve()}")
