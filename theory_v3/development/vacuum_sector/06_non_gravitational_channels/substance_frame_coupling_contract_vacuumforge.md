# VacuumForge Substance-Frame Coupling Contract

## Purpose

This report writes the first contract for a substance-frame
non-gravitational channel. It does not derive a preferred-frame signal.

This report depends on:

```text
casimir_ufft_operator_instantiation_audit_022
```

It satisfies:

```text
substance_frame_coupling_contract_required_022
```

## Symbolic Checks

Frame-anisotropy placeholder:

```text
Delta O_frame = beta_frame*cos(theta)**2
d(Delta O_frame)/d theta = -2*beta_frame*sin(theta)*cos(theta)
Delta O_frame | beta_frame = 0 -> 0
```

Metric leakage proxy:

```text
Delta_metric = beta_frame*epsilon_g*cos(theta)**2
Delta_metric | epsilon_g = 0 -> 0
```

The check is narrow: a frame variable is observationally silent unless a
coupling is added. A nonzero coupling creates a preferred-frame/calibration
channel that must be bounded and kept out of the closed metric response.

## Route Ledger

| route | frame variable | coupling object | metric quarantine | observable | bounds route | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| silent_frame | unit timelike substance-frame direction u^a | none | closed metric sector has no u^a force term | none | not applicable until a coupling is added | ontological frame only; no preferred-frame prediction | do not infer signal from frame existence alone |
| calibration_anisotropy_channel | u^a plus apparatus direction n^a | beta_frame * (u dot n)^2 calibration response | epsilon_g = 0 unless residual gates are reopened | orientation or sidereal calibration drift | preferred-frame, anisotropy, and calibration bounds required | quarantined candidate only | derive beta_frame and bind to bounds |
| matter_clock_channel | u^a plus matter clock or phase variable | frame-sensitive matter-clock operator, not yet derived | epsilon_g = 0 unless residual gates are reopened | clock, phase, or matter-calibration anisotropy | Lorentz and preferred-frame bounds required | deferred pending operator and source ledger | write operator and exchange bookkeeping |
| metric_preferred_frame_reroute | u^a inserted into gravitational action | preferred-frame metric residual | fails: changes closed metric response | preferred-frame gravity | belongs to residual gates and gravitational tests | rejected as wrong ledger | return to epsilon residual gates if desired |

## Readiness

| route | coupling written | source ready | metric quarantined | bounds ready | live |
| --- | --- | --- | --- | --- | --- |
| silent_frame | False | True | True | True | False |
| calibration_anisotropy_channel | True | False | True | False | False |
| matter_clock_channel | False | False | True | False | False |
| metric_preferred_frame_reroute | True | False | False | False | False |

## Current Conclusion

No substance-frame coupling route is live. The frame may remain an ontological
object without predicting a preferred-frame signal. Observable routes require a
coupling operator, source/exchange ledger, metric quarantine, and preferred
frame or calibration bounds.

## Classification

```text
result type: substance-frame coupling contract
scope: non-gravitational preferred-frame/calibration channels
conclusion: frame existence alone predicts no signal; coupled routes are unlicensed
non-conclusion: no global no-go theorem against substance-frame channels
```

The next technical target is:

```text
substance_frame_bounds_sieve_required_023
```
