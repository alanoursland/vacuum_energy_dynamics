# Substance-Frame Bounds Sieve

## Claim

No substance-frame observable channel is licensed until its coupling is derived
and shown compatible with preferred-frame, anisotropy, Lorentz, and calibration
bounds.

## Scope

This is a symbolic bounds ledger. It does not import numerical experimental
bounds and does not claim that any particular frame-sensitive coupling is
already excluded.

## Sieve

Use the signal proxy:

```text
Delta O_frame = beta_frame * A
```

where `A` is the apparatus orientation or calibration response factor.

A desired target response requires:

```text
beta_required = delta_target / A
```

The same coupling must satisfy an independent bound:

```text
beta_frame <= beta_bound
```

Therefore a target can be compatible only when:

```text
delta_target / A <= beta_bound
```

This is not a derivation. It is a required compatibility ledger.

## Route Classification

```text
silent frame:
    allowed, but predicts no preferred-frame observable

derived bounded coupling:
    candidate only if beta_frame, beta_bound, A, delta_target, and source
    bookkeeping are supplied before observation

observed-signal backsolve:
    rejected as target-value insertion

unbounded frame coupling:
    rejected as unbounded preferred-frame claim
```

## Current Classification

The VacuumForge sieve records:

```text
derivation: substance_frame_bounds_sieve_024
obligation satisfied: substance_frame_bounds_sieve_required_023
new obligation: interior_cap_admissibility_contract_required_024
```

Current conclusion:

```text
No bounded observable substance-frame channel is licensed.
```

The non-gravitational-channel sweep therefore remains conservative: Casimir,
UFFT, substance-frame, and material-boundary routes are possible only as
quarantined candidates unless a concrete operator, source ledger, and bounds
route are supplied.
