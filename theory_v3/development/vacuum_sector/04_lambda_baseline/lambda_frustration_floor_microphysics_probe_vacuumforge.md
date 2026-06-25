# VacuumForge Lambda Frustration-Floor Microphysics Probe

## Purpose

This report tests whether microphysical frustration or a potential shape
derives an absolute constant `Lambda` floor. It does not derive the observed
cosmological constant.

This report depends on:

```text
lambda_relaxation_fixed_point_probe_015
```

It satisfies:

```text
lambda_frustration_floor_microphysics_probe_required_015
```

## Symbolic Checks

Landau-style shape:

```text
V(phi) = V0 + lambda_f*(phi**2 - v**2)**2/4
dV/dphi = lambda_f*phi*(phi - v)*(phi + v)
d2V/dphi2 = lambda_f*(3*phi**2 - v**2)
V(+v) = V0
V(-v) = V0
V(0) = V0 + lambda_f*v**4/4
mass^2 at minimum = 2*lambda_f*v**2
curvature at origin = -lambda_f*v**2
```

Offset checks:

```text
V0 = 0 floor = 0
V0 = rho_obs floor = rho_obs
p + rho for constant floor = 0
quadratic excitation energy = delta_phi**2*lambda_f*v**2
```

## Probe Ledger

| probe | candidate object | symbolic result | source ledger | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
| no_microphysical_variable | no microstate variable or coarse-graining map | no floor equation | undetermined | cannot select Lambda | state microstate variable before claiming microphysical floor |
| landau_shape_with_free_offset | V(phi) = V0 + lambda_f*(phi**2 - v**2)**2/4 | V(+/-v) = V0 | absolute offset V0 is free | potential shape does not derive the absolute floor | derive V0 before using it as Lambda |
| zero_offset_floor | same potential with V0 = 0 | floor = 0 | zero floor | selects no nonzero Lambda | do not infer nonzero floor from symmetry breaking alone |
| target_offset_floor | same potential with V0 = rho_obs | floor = rho_obs | observed-value insertion | not a derivation | reject unless rho_obs is independently derived |
| constant_floor_equation_of_state | constant floor stress ledger | p + rho = 0 | Lambda floor candidate only after V0 is derived | w = -1 ledger is necessary but not sufficient | derive V0 and prove non-clustering |
| massive_excitation_excess | fluctuations around the minimum | quadratic excitation energy = delta_phi**2*lambda_f*v**2 | transportable excitation/excess sector | route to dark-sector or particle/defect ledger, not Lambda | separate excitations from constant floor |

## Current Conclusion

Microphysical potential shape is not enough to derive a nonzero `Lambda`
baseline. A Landau-style potential can provide minima, excitations, and a
constant-floor ledger, but the absolute offset `V0` remains free unless the
microphysics derives it. Setting `V0 = 0` gives no nonzero floor. Setting
`V0 = rho_obs` inserts the target. Excitations around the floor are not the
constant Lambda baseline and must be routed to dark-sector or particle/defect
ledgers.

The clean split is:

```text
potential shape:
  derives minima and excitation scale, not absolute floor

constant offset V0:
  Lambda candidate only if derived before observation

fluctuations/excitations:
  transportable excess, not Lambda
```

## Classification

```text
result type: Lambda frustration-floor microphysics probe
scope: microphysical potentials as Lambda baseline selectors
conclusion: microphysics must derive the absolute constant offset before it selects Lambda
non-conclusion: no nonzero Lambda value is derived; dark-sector excess is not yet developed
```

The next technical target is:

```text
dark_excess_source_ledger_required_016
```
