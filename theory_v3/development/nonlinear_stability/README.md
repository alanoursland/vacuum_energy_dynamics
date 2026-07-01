# Nonlinear Stability — Scoped Closure

## Purpose

This directory holds the closure of the nonlinear stability rigor debt
on the field-equation proof (`04_field_equations/proof.md` §3 proved
the sector-signature theorems at reduced/quadratic level; the debt was
their nonlinear extension).

Current status: closed at scoped level. See
`nonlinear_stability_note.md` and the forge script:

```text
vacuum_forge/src/field_equation_trials/020_nonlinear_stability/nonlinear_stability_scoped.py
```

## Scope

Three in-house pieces and one honestly-recorded external mathematical
anchor:

1. **Nonlinear source binding** (Theorem 3 lifted): vacuum + regular
   center force the flat state uniquely at full nonlinearity
   ($K = 12\,C_1^2/r^6$ kills the one-parameter Birkhoff family).
2. **No-mining theorem** (Misner–Sharp positivity):
   $m'(r) = (4\pi r^2/c^2)\rho$ exactly; $\rho \ge 0$ + regular center
   give $m \ge 0$ at arbitrary field strength. The negative static
   reservoir cannot drive a quasilocal mass negative.
3. **Sector signature at quadratic order**, inherited from G03/017 and
   re-verified (TT energy a positive sum of squares; scalar and vector
   sectors constraint-type).
4. **Global small-data stability** of the flat state: external
   mathematical import (Christodoulou–Klainerman 1993;
   Lindblad–Rodnianski 2010), same import class as Fierz–Pauli 1939 in
   proof.md §4.1 — mathematics about the derived equations, with no
   framework coefficient depending on it. Recorded as an import, not
   claimed as in-house work.

Archive results:

```text
nonlinear_source_binding_020
misner_sharp_no_mining_020
global_stability_external_anchor_020
```

This retires the nonlinear stability rigor debt at scoped level.
