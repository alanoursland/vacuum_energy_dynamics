# Non-Gravitational Vacuum Channels

This folder is for vacuum-sector channels that would be observable without
being inserted as modifications of the closed gravitational field equations.

Examples include:

```text
Casimir/UFFT-like boundary or material channels
substance-frame calibration or anisotropy channels
other apparatus-level vacuum response channels
```

The folder is not a shortcut for:

```text
local gravitational Yukawa residuals
unbooked additions to T_ab
dark-sector abundance fitting
Lambda baseline selection
```

Those routes already have their own ledgers.

## Current Result

The first quarantine pass is recorded in:

```text
channel_quarantine_contract.md
non_grav_channel_quarantine_vacuumforge.md
casimir_ufft_channel_contract.md
casimir_ufft_channel_contract_vacuumforge.md
casimir_ufft_operator_instantiation_audit.md
casimir_ufft_operator_instantiation_vacuumforge.md
substance_frame_coupling_contract.md
substance_frame_coupling_contract_vacuumforge.md
substance_frame_bounds_sieve.md
substance_frame_bounds_sieve_vacuumforge.md
```

Current conclusion:

```text
No non-gravitational vacuum channel is live yet. Candidate channels must state
their channel variable, coupling object, metric quarantine, source ledger,
observable, falsifier, current bounds or target window, and failure route.
```

Casimir/UFFT, substance-frame, and material-boundary rows are carried forward
only as quarantined candidates. Direct gravitational-Yukawa reinterpretation
and unbooked stress-tensor insertion are rejected as wrong-ledger moves.

The Casimir/UFFT contract now states a boundary/material channel variable,
symbolic coupling schema, observable, falsifier, and metric quarantine. It is
not prediction-ready because the channel operator, coefficient, source/exchange
ledger, and target window are still missing.
The operator-instantiation audit finds no live new Casimir/UFFT operator.
Standard Casimir scaling is ordinary QFT/material boundary physics unless a
new ontology coupling is derived. Fitting a channel coefficient to that scaling
is a backsolve, and a free boundary-channel schema remains unlicensed.
The substance-frame coupling contract states that frame ontology alone predicts
no preferred-frame signal. Any observable frame channel needs a coupling
operator, source/exchange ledger, metric quarantine, and preferred-frame or
calibration bounds.
The first bounds sieve keeps silent frame ontology allowed but rejects
observed-signal backsolves and unbounded preferred-frame claims. No bounded
observable frame channel is licensed.

## Required Channel Contract

Every channel file must answer:

```text
What is the channel variable?
What is the coupling object?
Why does it not modify the closed metric response?
What source ledger does it use?
What is the observable?
What is the falsifier?
What current bounds or target window apply?
What failure route kills or reroutes the channel?
```

## Next Work

The next concrete contract is:

```text
interior_cap_admissibility_contract_required_024
```

That obligation moves the program into the strong-field/interior admissibility
workstream.
