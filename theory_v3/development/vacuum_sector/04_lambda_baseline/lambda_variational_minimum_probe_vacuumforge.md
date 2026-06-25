# VacuumForge Lambda Variational-Minimum Probe

## Purpose

This report tests the variational-minimum Lambda selector opened by the
selector sieve. It tests selector functionals `F(Lambda)`, not variation of
the full EH action with respect to `Lambda`. It does not derive the observed
cosmological constant. It asks whether a bare stationarity/minimum principle
over `Lambda` selects a nonzero value before a bias, target, boundary class,
or microphysical scale is supplied.

This report depends on:

```text
lambda_selector_sieve_010
```

It satisfies:

```text
lambda_variational_minimum_probe_required_010
```

## Symbolic Checks

SymPy checks five selector prototypes.

No selector object:

```text
dF/dLambda = 0
```

No-scale convex minimum:

```text
dF/dLambda = Lambda*a
Lambda_*   = 0
d2F/dLambda2 = a
```

Linear bias without stabilizing dynamics:

```text
dF/dLambda = b
```

This means no interior stationary point on an unconstrained continuous
`Lambda` domain for nonzero `b`. A boundary extremum would belong to the
boundary/admissibility probe, not to this bare variational probe.

Biased convex minimum:

```text
dF/dLambda = Lambda*a + b
Lambda_*   = -b/a
d2F/dLambda2 = a
```

Target-inserted minimum:

```text
dF/dLambda = a*(Lambda - Lambda_star)
Lambda_*   = Lambda_star
d2F/dLambda2 = a
```

## Probe Ledger

| probe | selector functional | stationarity result | source of scale | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
| lambda_independent_selector | F = c | dF/dLambda = 0 identically; Lambda remains free | none | does not select a value | supply an actual selector equation or boundary condition |
| no_scale_convex_minimum | F = Lambda**2*a/2 | Lambda = 0 | none; only positive stiffness a | selects Lambda = 0, not nonzero Lambda | nonzero value requires a bias, target, boundary class, or new scale |
| linear_bias_no_minimum | F = Lambda*b | dF/dLambda = b | imported linear bias b | no interior stationary point for nonzero b on an unconstrained continuous domain | add a boundary/admissibility domain, dynamics, or stabilizing term before claiming a minimum |
| biased_convex_minimum | F = Lambda**2*a/2 + Lambda*b | Lambda = -b/a | imported bias b and stiffness a | nonzero value is inherited from imported coefficients | derive b/a from vacuum ontology before using the value |
| target_inserted_minimum | F = a*(Lambda - Lambda_star)**2/2 | Lambda = Lambda_star | imported target Lambda_star | selects the supplied target, not a derived value | do not treat target insertion as a selector derivation |

## Current Conclusion

A bare variational-minimum selector does not currently derive a nonzero
`Lambda`. The available outcomes are:

```text
no selector object: Lambda remains free;
no-scale convex minimum: Lambda = 0;
linear bias alone: no interior stationary point on an unconstrained domain;
biased convex minimum: nonzero Lambda inherits imported b/a;
target minimum: nonzero Lambda is inserted as Lambda_star.
```

Therefore the variational-minimum route is not mechanism-ready as a derived
nonzero baseline. It can be reopened only after the project supplies the
missing source of scale: a boundary/admissibility class, a global constraint, a
measure identity, relaxation dynamics, or microphysical floor.

## Provenance

This agrees with the older Lambda branch-selector status:

```text
zero Lambda is selected by asymptotically flat finite-flux boundary data;
constant nonzero Lambda is allowed but not selected by the local metric branch;
cancellation or nonzero targeting is tuning unless a dynamics or selector
equation supplies it.
```

## Classification

```text
result type: variational-minimum selector probe
scope: Lambda baseline selection before boundary, measure, relaxation, or microphysics
conclusion: variational minimum alone does not derive nonzero Lambda
non-conclusion: no global no-go theorem against nonzero Lambda; no other selector class is killed
```

The next technical target is:

```text
lambda_boundary_admissibility_probe_required_011
```
