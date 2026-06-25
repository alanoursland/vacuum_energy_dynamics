# VacuumForge Global/Boundary/Topology Selector Rules

## Purpose

This report consolidates the cross-cutting selector rule exposed by the Lambda
and interior-cap probes. It does not derive a nonzero Lambda value, a topology
selector, or an interior cap.

This report depends on:

```text
finite_strain_admissibility_probe_027
```

It satisfies:

```text
global_boundary_topology_selector_rules_required_027
```

## Symbolic Checks

Two-dimensional topology relation:

```text
R = 4*pi*chi/A
R * A = 4*pi*chi
```

Four-dimensional constant-curvature Gauss-Bonnet proxy:

```text
E = 32*pi**2*chi/V
Lambda^2 = 12*pi**2*chi/V
```

Topology can supply dimensionless sector information. A dimensionful local
value still needs area, volume, measure, length, or an admissibility scale.

## Selector Rule Ledger

| rule | selector | supplies sector | supplies scale | dimensionful value | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
| topology_only | dimensionless topology or sector label | yes | no | not derived | constrains sectors only | supply area, volume, measure, or admissibility scale before value claims |
| topology_plus_measure | topology plus derived measure/volume | yes | only if measure is derived | candidate if sign and scale are supplied | deferred pending measure derivation | derive measure/volume and sign selector |
| boundary_admissibility_scale | boundary or admissibility class with derived length/area/volume | yes | only if boundary scale is selected by ontology | candidate after scale derivation | deferred pending boundary-scale selector | derive boundary/admissibility scale before value claims |
| observed_value_backsolve | choose scale to match observed Lambda or compactness | fit only | observed value inserted | backsolved | rejected as observed-value insertion | do not use as derivation |

## Readiness

| rule | constrains sector | derives scale | derives value | live value selector |
| --- | --- | --- | --- | --- |
| topology_only | True | False | False | False |
| topology_plus_measure | True | False | False | False |
| boundary_admissibility_scale | True | False | False | False |
| observed_value_backsolve | False | False | False | False |

## Current Conclusion

Global, boundary, topology, and admissibility selectors can restrict sectors
or admissible classes, but they do not set dimensionful values unless the
missing scale is also derived. Observed-value backsolves are rejected.

## Classification

```text
result type: cross-cutting selector rule
scope: Lambda, topology, boundary, measure, and interior admissibility selectors
conclusion: sector selection is not value selection without a derived scale
non-conclusion: no no-go theorem against global or topological selectors
```

The next technical target is:

```text
vacuum_sector_program_checkpoint_required_028
```
