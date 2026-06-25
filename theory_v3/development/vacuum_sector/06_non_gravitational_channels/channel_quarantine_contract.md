# Channel Quarantine Contract

## Claim

A non-gravitational vacuum channel can remain outside the closed GR metric
sector only if it supplies its own channel variable, coupling object, source
ledger, observable, falsifier, and metric quarantine.

## Scope

This contract applies to apparatus-level or matter-calibration channels such
as Casimir/UFFT, material-boundary response, and substance-frame couplings.

It does not apply to:

```text
gravitational residuals in K_strain
Lambda baseline selection
dark-sector excess abundance
ordinary source insertion into T_ab
```

Those claims must return to their own ledgers.

## Required Inputs

Each channel must provide:

```text
channel variable
coupling object
closed-metric-response quarantine
source ledger
observable
falsifier
current bounds or target window
failure route
```

## What Is Not Assumed

The existence of a vacuum ontology does not by itself imply a detectable
apparatus channel.

A channel observable is not automatically:

```text
a gravitational Yukawa force
a nonzero epsilon residual
a dark-sector abundance source
a contribution to Lambda
a source term in T_ab
```

Any of those reinterpretations must pass the appropriate existing gate.

## Quarantine Rule

Use the split:

```text
Delta_observable = channel response
Delta_metric = epsilon_g * channel leak
```

For a non-gravitational channel, the required quarantine is:

```text
epsilon_g = 0
```

unless the claim is explicitly rerouted through the residual-gate ledger. The
channel may still have a nonzero apparatus observable, but that observable
cannot be counted as a modification of the closed metric field equation.

## Current Classification

The first VacuumForge pass records:

```text
derivation: non_grav_channel_quarantine_020
obligation satisfied: non_grav_channel_quarantine_required_019
new obligation: casimir_ufft_channel_contract_required_020
```

Current conclusion:

```text
No non-gravitational channel is live yet.
```

Casimir/UFFT, substance-frame, and material-boundary channels are quarantined
candidates. Direct gravitational-Yukawa reinterpretation and unbooked
stress-tensor insertion are rejected as wrong-ledger moves.

## Non-Conclusions

This contract does not kill Casimir/UFFT, substance-frame, or material-boundary
mechanisms. It only says that none of them can be used until its own coupling,
source ledger, observable, falsifier, and metric quarantine are written.
