# VacuumForge Lambda Measure Identity Probe

## Purpose

This report tests whether a measure identity can supply a conserved density or
curvature scale for `Lambda` without observed-value insertion or dark-excess
double counting. It does not derive the observed cosmological constant.

This report depends on:

```text
lambda_topology_global_constraint_probe_013
```

It satisfies:

```text
lambda_measure_identity_probe_required_013
```

## Symbolic Checks

Dimension check:

```text
dim(kappa) + dim(rho) - dim(Lambda) = 0
```

Dimensional fit:

```text
Lambda = C/L**2
```

Conserved floor:

```text
Lambda_floor = kappa*rho0
d Lambda_floor / da = 0
rho(w=-1) = rho0
```

Transportable/excess scalings:

```text
rho(w=0) = rho0/a**3
Lambda_dust(a) = kappa*rho0/a**3
d Lambda_dust / da = -3*kappa*rho0/a**4
rho(w=-2/3) = rho0/a
d Lambda_string / da = -2*kappa*rho0/a**3
```

## Probe Ledger

| probe | candidate identity | conservation face | source ledger | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
| no_measure_identity | no measure identity is written | none | undetermined | cannot select Lambda | write a covariant identity before claiming a measure-derived value |
| dimensional_fit | Lambda = C/L**2 | constant if L is supplied | observed or imported length scale unless L is derived | dimensionally valid but not a derivation | derive L or reject as dimensional fitting |
| conserved_vacuum_density_floor | Lambda = kappa*rho0 | w = -1 gives constant rho and constant Lambda | Lambda floor candidate if rho0 is derived before observation | candidate only after the measure derives rho0 | derive rho0 and prove covariant conservation |
| dustlike_measure_excess | Lambda(a) = kappa*rho0/a**3 | w = 0 gives a^-3 scaling and dLambda/da != 0 | dark-sector excess, not constant Lambda | route to dark-sector ledger | do not count clustered excess as the Lambda floor |
| defectlike_measure_excess | measure density with string/wall-like scaling | w != -1 gives variable density | defect/excess sector, not constant Lambda | route to dark-sector or defect ledger | classify equation of state and clustering before use |

## Current Conclusion

A measure identity can be a Lambda selector only if it supplies a derived,
covariantly conserved, constant floor before observation is used. Dimensional
fits import a scale. Dustlike, stringlike, wall-like, clustered, or
transportable densities belong to dark-sector or defect ledgers, not the
constant Lambda baseline.

The clean split is:

```text
conserved w = -1 floor:
  possible Lambda selector only after rho0 is derived

Lambda = C/L^2:
  dimensional fit unless L is derived

w != -1 measure density:
  variable/excess sector, not constant Lambda
```

## Classification

```text
result type: Lambda measure identity probe
scope: measure identities as Lambda baseline selectors
conclusion: a measure route needs a derived conserved floor; otherwise it is fitting or dark excess
non-conclusion: no nonzero Lambda value is derived; relaxation/fixed-point routes are not yet tested
```

The next technical target is:

```text
lambda_relaxation_fixed_point_probe_required_014
```
