# VacuumForge Dark Excess Abundance/Production Probe

## Purpose

This report tests abundance and production bookkeeping for pressureless
dark-sector excess. It does not derive dark matter abundance.

This report depends on:

```text
dark_excess_clustering_conservation_probe_018
```

It satisfies:

```text
dark_excess_abundance_production_required_018
```

## Symbolic Checks

Dilution from formation:

```text
rho_today = a_form**3*rho_form/a0**3
required rho_form from rho_obs = a0**3*rho_obs/a_form**3
```

Conserved yield:

```text
rho_today = Y*m*s0
required Y from rho_obs = rho_obs/(m*s0)
```

Freezeout proxy:

```text
rho_today = C/sigma_v
required sigma_v from rho_obs = C/rho_obs
```

Formation fraction:

```text
rho_today = a_form**3*f_form*rho_tot_form/a0**3
required f_form from rho_obs = a0**3*rho_obs/(a_form**3*rho_tot_form)
```

## Abundance Ledger

| row | route | symbolic result | imported input | disposition | next obligation |
| --- | --- | --- | --- | --- | --- |
| observed_density_backsolve | solve for initial density from observed density | rho_form = a0**3*rho_obs/a_form**3 | rho_obs | rejected as observed-value insertion | do not use as production mechanism |
| yield_route | conserved yield abundance | rho_today = Y*m*s0 | mass m, yield Y, entropy density s0 | candidate only if Y is derived | derive yield from production microphysics |
| freezeout_proxy_route | inverse interaction-strength relic proxy | rho_today = C/sigma_v | interaction scale or cross section sigma_v | candidate only if interaction route exists | derive coupling/cross section and freezeout regime |
| formation_fraction_route | defect/excitation formation fraction | rho_today = a_form**3*f_form*rho_tot_form/a0**3 | formation fraction f_form and formation epoch | candidate only if formation dynamics derive f_form | derive formation fraction and epoch from vacuum dynamics |

## Current Conclusion

No dark-sector abundance route is currently licensed. Back-solving from the
observed density is rejected. Yield, freezeout-like, and formation-fraction
routes remain possible only after their production microphysics, interaction
scale, or formation fraction is derived before observation is used.

## Classification

```text
result type: dark-excess abundance/production probe
scope: abundance bookkeeping after clustering/conservation readiness
conclusion: no abundance route is licensed without production microphysics
non-conclusion: dustlike excess is not globally killed; no halo model is tested
```

The next technical target is:

```text
non_grav_channel_quarantine_required_019
```
