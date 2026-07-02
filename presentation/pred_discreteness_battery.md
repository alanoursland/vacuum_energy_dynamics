# If the packing scale is ever measured, does the theory survive contact?

A reader who has absorbed that the packing scale `a` is currently unmeasured and unmeasurable needs to see what happens the day that changes — this is the theory's most exposed conditional bet, twice overdetermined and parameter-free.

## The claim

Everywhere else in the register, `a` is a free constant nobody can reach — G, Lambda, and the closed field equations are all continuum results that don't depend on its value. That silence is a feature (it's why the theory has no tunable knobs to hide behind) but it also means the packing's discreteness has never been checked against data. C4 in the predictions register is the standing commitment for the day that changes.

The setup: derivation 052 pins down the vacuum energy density as a pure-geometry function of `a` alone —

```text
rho_v = (c_e Delta_0 / 2) f'(Delta_0) / a^3,   c_e = 36 arccos(1/3)/(sqrt(2) pi) = 9.974276
```

`c_e` (edges per unit cell) is exact, derived from the same single input — `arccos(1/3)`, the tetrahedral dihedral defect — that fixes the relief geometry (037) and the ground-state coordination mixture (050). `f'(Delta_0)` is eliminated by the floor-Newton lock (039): it's fixed by the requirement that the packing reproduce the observed Newton's constant. So the reduction leaves **exactly one unknown constant in the whole theory: `a`.**

Two independent things happen if `a` is ever pinned down by an outside probe:

1. **The floor-Newton lock must still hold.** Plug the measured `a` into the lock and the predicted G must come out to the observed value. This isn't a fit — `f'(Delta_0)` was already used up closing the lock; there's no dial left to turn.
2. **A scalaron Yukawa must appear at range `sqrt(6) a`.** The four-derivative sector isn't exactly empty away from the continuum idealization (P7' scoping ruling, 047/048): at finite packing scale the surviving R²-class term produces a Yukawa correction to Newtonian gravity with range `l* = sqrt(6 alpha) ~ sqrt(6) a` — currently ~4e-35 m at Planck-scale packing, unobservably short, but *not* zero once `a` stops being an idealization.

Both consequences are forced by the same measured number, through unrelated machinery (a static-limit coupling constant vs. a four-derivative correction term). Get either one wrong and the packing model — not just the numerology — is falsified. This is why the register calls it a battery, not a prediction: it's two independent checks that must both pass, with no free parameter left to absorb a miss.

No value of `a` is proposed or needed for this entry to count as a real prediction — it fires the moment any independent discreteness probe reports a number, regardless of what that number is.

**Proof:** derivations 047, 048 (`p7prime_scoping_ruling_048`), 052 (`o_p10_1_ce_derived_052`) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md), [../theory_v3/development/vacuum_sector/08_packing_microphysics/p7prime_scoping_ruling_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/p7prime_scoping_ruling_vacuumforge.md), register entry C4 in [../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md).

**Where next:**
- [Zero short-range deviation from Newton →](pred_no_yukawa.md) — the companion null: no Yukawa at any *accessible* range, which is what makes the sqrt(6)*a battery entry a genuinely future-only commitment rather than something already excluded.
- [The Microstructure Trail →](hub_packing.md) — where `a`, `c_e`, and the ground-state coordination mixture come from.
- [The Falsifier Trail →](hub_predictions.md) — this entry's place among the register's live-fire, standing-null, and gated-future tiers.
- [Gdot = 0 exactly →](pred_gdot_zero.md) — the other Tier A commitment built directly on the floor-Newton lock, currently under the tightest experimental pressure of any entry in the register.
