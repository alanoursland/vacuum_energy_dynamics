# VacuumForge Lambda Relaxation/Fixed-Point Probe

## Purpose

This report tests whether relaxation/fixed-point dynamics can select a nonzero
`Lambda` floor without target insertion. It does not derive the observed
cosmological constant.

This report depends on:

```text
lambda_measure_identity_probe_014
```

It satisfies:

```text
lambda_relaxation_fixed_point_probe_required_014
```

## Symbolic Checks

Scale-free damping:

```text
Lambda(t) = Lambda0*exp(-gamma*t)
limit = 0
```

Target relaxation:

```text
Lambda(t) = Lambda_star + (Lambda0 - Lambda_star)*exp(-gamma*t)
limit = Lambda_star
```

Domain-scale relaxation:

```text
Lambda(t) = (Lambda0 - sigma/L**2)*exp(-gamma*t) + sigma/L**2
limit = sigma/L**2
```

Nonlinear self-fixed-point flow:

```text
flow = Lambda**2*beta - Lambda*gamma
fixed points = 0, gamma/beta
linearized derivative at zero = -gamma
linearized derivative at nonzero point = gamma
```

## Probe Ledger

| probe | dynamics | fixed point | source of scale | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
| zero_relaxation | dLambda/dt = -gamma Lambda | Lambda -> 0 | none | selects Lambda = 0 | do not infer nonzero floor from scale-free damping |
| target_relaxation | dLambda/dt = -gamma (Lambda - Lambda_star) | Lambda -> Lambda_star | imported target Lambda_star | selects the supplied target, not a derived value | derive Lambda_star before claiming selection |
| domain_scale_relaxation | dLambda/dt = -gamma (Lambda - sigma/L^2) | Lambda -> sigma/L**2 | domain length L and dimensionless sigma | nonzero floor inherits a supplied domain scale | derive L from admissibility, measure, or microphysics |
| nonlinear_self_fixed_point | dLambda/dt = -gamma Lambda + beta Lambda^2 | Lambda = 0 or Lambda = gamma/beta | coefficient ratio gamma/beta | nonzero fixed point is coefficient-derived only if gamma/beta is derived | derive coefficients and prove stable physical branch before use |

## Current Conclusion

Relaxation dynamics can select zero without an extra scale. Nonzero fixed
points appear only when the dynamics import a target, domain length, kernel
scale, or coefficient ratio. Such a route becomes a Lambda selector only after
that scale and the conservation law are derived by the vacuum ontology.

The clean split is:

```text
dLambda/dt = -gamma Lambda:
  selects Lambda = 0

dLambda/dt = -gamma (Lambda - Lambda_star):
  imports Lambda_star

dLambda/dt = -gamma (Lambda - sigma/L^2):
  imports L

nonlinear fixed point:
  imports coefficient ratio unless coefficients are derived
```

## Classification

```text
result type: Lambda relaxation/fixed-point probe
scope: relaxation dynamics as Lambda baseline selectors
conclusion: nonzero relaxation floors require a derived target, scale, or coefficient ratio
non-conclusion: no nonzero Lambda value is derived; microphysical floor routes are not yet tested
```

The next technical target is:

```text
lambda_frustration_floor_microphysics_probe_required_015
```
