# VacuumForge Casimir/UFFT Channel Contract

## Purpose

This report writes the first concrete contract for a Casimir/UFFT-like
non-gravitational vacuum channel. It does not derive an effect.

This report depends on:

```text
non_grav_channel_quarantine_020
```

It satisfies:

```text
casimir_ufft_channel_contract_required_020
```

## Symbolic Distinction Check

Apparatus-channel placeholder:

```text
Delta O_ch = chi_m*eta_ch/L**4
d(Delta O_ch)/d chi_m = eta_ch/L**4
```

Gravitational-Yukawa residual placeholder:

```text
Delta Phi_Y = alpha_y*exp(-r/lambda_y)/r
d(Delta Phi_Y)/d chi_m = 0
```

Metric leakage proxy:

```text
Delta_metric = chi_m*epsilon_g*eta_ch/L**4
Delta_metric | epsilon_g = 0 -> 0
```

The distinction is only a contract-level quarantine check. Material/boundary
dependence is compatible with an apparatus channel, but it does not derive the
operator or coefficient.

## Contract Gates

| gate | requirement | current entry | status | next obligation | ready |
| --- | --- | --- | --- | --- | --- |
| channel_variable | state the apparatus-level channel variable | boundary/material data B = (L, chi_m, boundary class, frequency window) | contracted | keep distinct from metric variable g_ab | True |
| coupling_schema | state the symbolic coupling schema | Delta O_ch = eta_ch * chi_m / L^4 as a scaling placeholder | schema only | derive or justify the operator and coefficient eta_ch | True |
| operator_derivation | derive the channel operator before prediction | not supplied | missing | casimir_ufft_operator_instantiation_required_021 | False |
| metric_quarantine | show the channel does not modify the closed metric response | epsilon_g = 0 unless rerouted through residual gates | contracted | do not count apparatus response as K_residual | True |
| source_ledger | separate apparatus/material exchange from T_ab insertion | not supplied | missing | write source/exchange bookkeeping for any concrete apparatus claim | False |
| observable | state the observable | differential response with L, material, boundary-class, or frequency dependence | contracted | turn target window into an experimental bound before prediction | True |
| falsifier | state what kills or reroutes the channel | no material/boundary scaling, or only universal Yukawa-like scaling | contracted | bind to current bounds before quantitative use | True |

Readiness:

```text
5/7 gates ready
```

## Current Conclusion

The Casimir/UFFT channel now has a contract shape and a symbolic quarantine
from a gravitational-Yukawa misroute. It is not prediction-ready because the
channel operator and source/exchange ledger are still missing.

## Classification

```text
result type: non-gravitational channel contract
scope: Casimir/UFFT-like boundary/material apparatus response
conclusion: contract drafted, no effect licensed
non-conclusion: no Casimir/UFFT operator, coefficient, or target window derived
```

The next technical target is:

```text
casimir_ufft_operator_instantiation_required_021
```
