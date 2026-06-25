# VacuumForge Dark Excess Source Ledger

## Purpose

This report opens the dark-sector excess ledger after the Lambda selector
sweep. It separates constant floor, transportable excess, radiationlike
excitations, and defectlike sectors before any dark-matter-like claim is used.

This report depends on:

```text
lambda_frustration_floor_microphysics_probe_016
```

It satisfies:

```text
dark_excess_source_ledger_required_016
```

## Symbolic Checks

Source split:

```text
T_vac = T_floor + T_excess
rho_total - rho_floor - rho_excess = 0
```

Equation-of-state scaling:

```text
rho(a,w) = a**(-3*w - 3)*rho0
w = -1:  rho0
w = 0:   rho0/a**3
w = 1/3: rho0/a**4
w = -1/3:rho0/a**2
w = -2/3:rho0/a
```

## Source Ledger

| row | source type | equation of state | scaling | ledger route | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- |
| lambda_floor | constant vacuum floor | w = -1 | rho(a) = rho0 | Lambda baseline | not dark-sector excess | keep floor in Lambda ledger unless an excess is separately defined |
| dustlike_excess | gapped/particlelike or nonrelativistic excess | w = 0 | rho(a) = rho0/a**3 | dark-sector excess candidate | candidate only after clustering, conservation, and abundance gates | prove clustering and source conservation before use |
| radiationlike_excess | relativistic excitation | w = 1/3 | rho(a) = rho0/a**4 | radiation/excitation ledger | not CDM-like | do not count as cold dark excess without a cooling/nonrelativistic route |
| stringlike_defect | stringlike defect network | w = -1/3 | rho(a) = rho0/a**2 | defect/excess candidate | not CDM-like without additional dynamics | route defect dynamics and observational face before use |
| walllike_defect | wall-like defect network | w = -2/3 | rho(a) = rho0/a | defect/excess candidate | not CDM-like without additional dynamics | route defect dynamics and pressure/anisotropy before use |

## Current Conclusion

The dark-sector excess ledger is open, but no dark-sector model is licensed.
The constant `w = -1` floor remains in the Lambda baseline ledger. A dustlike
`w = 0` excess is the only first-pass CDM-like candidate, and it still needs
conservation, clustering, production, abundance, and source-bookkeeping gates.
Radiationlike and defectlike rows are not CDM-like without further dynamics.

## Classification

```text
result type: dark-sector source ledger
scope: source split and equation-of-state routing after Lambda floor probes
conclusion: floor, dustlike excess, radiation, and defect sectors are separated
non-conclusion: no dark-sector abundance, clustering, or production mechanism is derived
```

The next technical target is:

```text
dark_excess_clustering_conservation_required_017
```
