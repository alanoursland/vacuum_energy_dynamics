# If a vacuum-energy shift ever gravitated, would that kill the theory?

A reader who knows sequestering hides the floor from gravity needs to know where that claim can actually be checked against nature — this is the prediction, not just the mechanism.

## The claim

Sequestering (idea_sequestering.md) isn't only an explanation of why the floor's ~10^122-orders density doesn't blow up Λ. It's a standing commitment about every *other* constant vacuum-energy shift too — and that commitment has an edge nature could in principle press on.

The commitment: any change in the vacuum's constant energy density — a cosmological phase transition (electroweak, QCD) shifting the zero-point budget, or any other mechanism that adds a constant to ρ_vac — produces **no gravitational effect and no shift in the effective Λ.** Not "a small effect below current sensitivity." None.

This is the sharp opposite of the standard picture. In GR-with-Λ-as-coupling, Λ is a term you put in the action by hand, and any process that shifts the vacuum's zero-point energy (EW symmetry breaking, QCD confinement, any first-order phase transition) *should* gravitate — that's the radiative-instability face of the cosmological constant problem: nothing protects Λ from getting kicked around by every phase transition in the thermal history. VED says this can't happen, structurally, because Λ is not a coupling at all — it's an integration constant of the unimodular conservation law (thm_lambda_integration_constant.md). A constant shift in the stress tensor gets absorbed exactly into the integration constant (`Λ' = Λ - k·ρ_shift`) and never touches the field equations. The mechanism doesn't care what sourced the shift — floor, EW transition, QCD transition, anything constant — the shift-invariance argument is agnostic to origin.

```text
T_ab -> T_ab - rho_shift * g_ab   leaves the field equations unchanged;
Lambda' = Lambda - k*rho_shift    (relabeled constant, no new gravitational effect)
```

Why this belongs in the predictions register and not just the idea trail: it names a falsifier. If anyone ever demonstrated a vacuum-energy shift gravitating — a phase-transition-era signature tying a known ΔρEW or ΔρQCD to an observed jump in the effective cosmological constant or expansion history — that would be a direct kill against the closed vacuum sector, not a parameter to retune. The theory has no free coupling to relax; sequestering is a theorem (forge 033 check 4, 035, 038), not a fit.

The honest status: this is a slow-fire edge, not a live one. Early-universe phase-transition cosmology (BBN-era and later constraints on Λ/dark-energy behaving anomalously across the EW and QCD epochs) is the long-run arena, and nothing in the current cosmological record shows any such coupling — every phase transition in the thermal history has come and gone without leaving a gravitational fingerprint on Λ, which is exactly what sequestering predicts and exactly what the standard-picture radiative-instability worry says *shouldn't* be guaranteed. Tier B in the register: distinctive and falsifiable in principle, but not under the kind of active experimental pressure Tier A entries (like A1's DESI confrontation) are under. Direct access is hard — there's no telescope pointed at "did the QCD transition nudge Λ" the way DESI is pointed at w(z).

**Proof:** register entry B1, forced by the sequestering theorem chain (033 check 4, 035, 038) → [../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md), mechanism detail in [../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md](../theory_v3/05_vacuum_sector/03_lambda_and_the_global_datum.md).

**Where next:**
- [The Sequestering Mechanism →](idea_sequestering.md) — the actual shift-invariance argument this prediction rests on, worked in full.
- [w = -1 Exactly →](pred_w_minus_1.md) — the live-fire Tier A sibling of this Tier B entry: same integration-constant logic, but under DESI pressure right now.
- [The Falsifier Trail →](hub_predictions.md) — how this edge sits among the theory's other kill conditions, tiered by sharpness.
- [The Cosmological-Constant Trail →](hub_lambda.md) — the full argument for why Λ is a global datum rather than a local source, which is what makes this prediction possible at all.
