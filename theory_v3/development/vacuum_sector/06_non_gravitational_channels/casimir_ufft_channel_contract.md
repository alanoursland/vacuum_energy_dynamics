# Casimir/UFFT Channel Contract

## Claim

A Casimir/UFFT-like effect can be treated as a non-gravitational vacuum channel
only if it is formulated as an apparatus-level boundary/material response with
its own coupling, source ledger, observable, falsifier, and metric quarantine.

## Scope

This contract covers possible non-gravitational channels with dependence on:

```text
boundary separation or geometry
material response
boundary class
frequency or mode window
apparatus calibration
```

It does not license a gravitational short-range force, dark-sector source, or
Lambda contribution.

## Channel Variable

Use a boundary/material channel variable:

```text
B = (L, chi_m, boundary class, frequency window)
```

where `L` is an apparatus boundary scale and `chi_m` denotes material response
data. This is not the metric variable `g_ab`.

## Coupling Schema

The current placeholder schema is:

```text
Delta O_ch = eta_ch * chi_m / L^4
```

This is a scaling placeholder, not a derived operator. The coefficient
`eta_ch`, the operator content, and the apparatus target window are still open.

## Metric Quarantine

Use the split:

```text
Delta_metric = epsilon_g * Delta O_ch
```

For the non-gravitational channel interpretation:

```text
epsilon_g = 0
```

unless the claim is explicitly rerouted through the residual-gate ledger. The
apparatus response cannot be counted as `K_residual` by notation.

## Source Ledger

The source/exchange ledger is not yet supplied. Any concrete channel must
separate:

```text
apparatus energy exchange
material response
external driving or calibration
ordinary stress-tensor bookkeeping
```

The channel cannot be inserted into `T_ab` as an unexplained source.

## Observable

The observable must be a differential apparatus response with dependence on
boundary, material, geometry, or frequency controls.

The symbolic distinction check used by VacuumForge is:

```text
Delta O_ch = eta_ch * chi_m / L^4
d(Delta O_ch)/d chi_m = eta_ch / L^4
```

For comparison, a gravitational-Yukawa placeholder:

```text
Delta Phi_Y = alpha_y * exp(-r/lambda_y) / r
d(Delta Phi_Y)/d chi_m = 0
```

This does not prove a channel exists. It only keeps the apparatus channel from
being silently reclassified as a universal gravitational residual.

## Falsifier

The channel fails or reroutes if:

```text
the effect has no material, boundary, geometry, or frequency dependence;
the only surviving fit is a universal gravitational Yukawa-like residual;
the source/exchange ledger cannot be written;
the coupling operator cannot be derived or bounded;
the signal violates existing calibration or preferred-frame bounds.
```

## Current Classification

The first VacuumForge pass records:

```text
derivation: casimir_ufft_channel_contract_021
obligation satisfied: casimir_ufft_channel_contract_required_020
new obligation: casimir_ufft_operator_instantiation_required_021
```

Current conclusion:

```text
The Casimir/UFFT channel has a contract shape, but no signal is licensed.
```

The missing objects are the channel operator, coefficient, source/exchange
ledger, and quantitative target window.
