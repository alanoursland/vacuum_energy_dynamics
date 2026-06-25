# VacuumForge Non-Gravitational Channel Quarantine

## Purpose

This report opens the non-gravitational vacuum-channel workstream. It does not
derive a Casimir/UFFT signal, preferred-frame coupling, or material-boundary
effect.

This report depends on:

```text
dark_excess_abundance_production_probe_019
```

It satisfies:

```text
non_grav_channel_quarantine_required_019
```

## Symbolic Checks

Metric leakage proxy:

```text
Delta_metric = c_channel*epsilon_g
Delta_metric | epsilon_g = 0 -> 0
```

Non-gravitational observable proxy:

```text
Delta_observable = c_channel*delta_O
```

The check is intentionally narrow: a non-gravitational channel may carry an
observable coupling only if its metric-leak coefficient is quarantined at zero
or routed through the residual-gate ledger.

## Channel Quarantine Ledger

| row | channel | coupling object | metric quarantine | source ledger | observable | falsifier | disposition | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| casimir_ufft_channel | boundary/material vacuum channel such as Casimir or UFFT | not yet written; must be a channel operator, not a metric residual | closed metric response unchanged unless a residual gate is explicitly reopened | not yet supplied; cannot be inserted into T_ab without bookkeeping | geometry/material/frequency dependence in a nongravitational apparatus channel | null target-window dependence or scaling incompatible with the channel operator | quarantined candidate only | write casimir_ufft_channel_contract |
| substance_frame_channel | preferred-substance-frame observable channel | not yet written; must state the frame-sensitive operator | frame velocity cannot modify the closed metric sector by assumption | not yet supplied; matter-calibration effects need their own ledger | anisotropy, calibration drift, or Lorentz/preferred-frame target window | existing or proposed null bounds on preferred-frame/calibration response | quarantined candidate only | write substance_frame_coupling_contract |
| material_boundary_channel | material or boundary vacuum-response channel | not yet written; needs boundary/material state variables | boundary response is not a universal gravitational potential | not yet supplied; material energy exchange must be separated | material, geometry, or boundary-condition dependence | loss of material/boundary dependence after controls | quarantined candidate only | route through a concrete channel contract before use |
| gravitational_yukawa_misroute | reinterpret channel effect as local gravitational Yukawa residual | metric residual coefficient without residual gates | fails: changes closed metric response | fails: bypasses epsilon residual ledger | short-range force fit | already belongs in gravitational residual tests, not this folder | rejected as wrong ledger | route through residual gates before any gravitational use |
| stress_tensor_insertion_misroute | insert channel energy into T_ab as unexplained source | source term without production, exchange, or conservation route | fails: becomes gravitational source bookkeeping | fails: double-counting risk is unresolved | whatever source fit is desired | not operational until the source ledger is stated | rejected as unbooked source insertion | return to source ledger before any metric coupling |

## Readiness Check

| row | minimum gates ready | live channel |
| --- | ---: | --- |
| casimir_ufft_channel | 4/6 | False |
| substance_frame_channel | 4/6 | False |
| material_boundary_channel | 4/6 | False |
| gravitational_yukawa_misroute | 2/6 | False |
| stress_tensor_insertion_misroute | 0/6 | False |

## Current Conclusion

No non-gravitational vacuum channel is live yet. Casimir/UFFT,
substance-frame, and material-boundary routes are carried forward only as
quarantined candidates. They need a channel variable, coupling object, source
ledger, observable, falsifier, and explicit metric quarantine before they can
be used.

Direct gravitational-Yukawa reinterpretation and unbooked stress-tensor
insertion are rejected as wrong-ledger moves.

## Classification

```text
result type: non-gravitational channel quarantine ledger
scope: vacuum channels outside the closed metric response
conclusion: no non-grav channel is live until its coupling and falsifier are written
non-conclusion: no Casimir/UFFT or preferred-frame mechanism has been killed
```

The next technical target is:

```text
casimir_ufft_channel_contract_required_020
```
