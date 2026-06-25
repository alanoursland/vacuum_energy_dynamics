# Casimir/UFFT Operator Instantiation Audit

## Claim

The Casimir/UFFT channel contract does not yet instantiate a new
vacuum-sector operator. Standard Casimir scaling, coefficient matching, and
free boundary-channel schemas do not derive the missing vacuum-channel
coupling.

## Scope

This audit covers candidate operator routes for the Casimir/UFFT
non-gravitational channel. It does not test every possible apparatus
configuration and does not claim a global no-go theorem.

## Symbolic Routes

Standard Casimir-scaling placeholder:

```text
O_C = -C_qft / L^4
```

Channel schema from the contract:

```text
O_ch = eta_ch * chi_m / L^4
```

Matching the channel schema to the standard scaling gives:

```text
eta_ch = -C_qft / chi_m
```

That fixes the channel coefficient by importing the standard coefficient and
material response. It is a backsolve, not an ontology-derived operator.

Free boundary-channel schema:

```text
O_B = eta_ch * chi_m * G_B / L^4
```

This remains a schema only unless `eta_ch`, `G_B`, and the source/exchange
ledger are derived before data are used.

## Route Audit

```text
standard Casimir QFT/material scaling:
    baseline/background, not a new vacuum-sector channel

fit to standard scaling:
    rejected as coefficient backsolve

free boundary-channel schema:
    deferred pending operator, coefficient, and source ledger

universal Yukawa reroute:
    rejected as wrong ledger; return to residual gates if desired
```

## Current Classification

The VacuumForge audit records:

```text
derivation: casimir_ufft_operator_instantiation_audit_022
obligation satisfied: casimir_ufft_operator_instantiation_required_021
new obligation: substance_frame_coupling_contract_required_022
```

Current conclusion:

```text
No Casimir/UFFT operator route is live as a new vacuum-sector channel.
```

This does not kill Casimir/UFFT-like channels. It says the current work has not
derived the operator and should move to the next non-gravitational channel
family unless a concrete operator proposal is supplied.
