# How far off from AB = 1 does a real static exterior sit?

The static shadow $AB = 1$ (P7′) is exact only in an idealized H → 0 cosmos; a real mass sits in an expanding one, and the leak has now been derived rather than guessed.

## The number

The postulate P7′ says a strictly static vacuum carries no t-r energy current, and its metric shadow is $A(r)B(r) = \text{const} = 1$. No real exterior is strictly static — every mass sits in an expanding cosmos — so the honest question is how big the deviation is. Trial F1 answers it in three steps:

- **Pure-Λ era: zero, exactly.** Schwarzschild–de Sitter (B = 1/A) solves the closed field equations for any Λ, and $AB = 1$ identically. The dark-energy component leaks nothing — P7′ is *stronger* here than the adoption note assumed.
- **The O(H₀r/c) piece is frame, not geometry.** In Painlevé form, the comoving velocity v = H₀r is the whole first-order content, and it's curvature-free — flat space in falling coordinates, gauge in GR. It only becomes physical if something couples to the substance frame, which the closed local sector does not do. This kills the original "linear in system size" estimate that P7′ was adopted with.
- **The real leak is matter-sourced and second order.** Uniform background dust gives the quasi-static potentials φ = ψ = (2πGρ/3)r², and running that through the areal shadow and the Friedmann equation gives one clean coefficient:

```text
AB - 1 = (3/2) * Omega_m * (H0*r/c)^2
```

At the present epoch (Λ contributes zero by the first bullet) this evaluates to **AB − 1 ≈ 5.6×10⁻³¹ at 1 AU** — no free parameter, just Ω_m, H₀, and r.

That's roughly 15 orders of magnitude below the Cassini bound on γ (2.3×10⁻⁵) stacked on top of the fact that it's now quadratic instead of linear in H₀r/c. The framework's advertised "first naturally-sized deviation prediction" from the P7′ adoption note is superseded — this is a smaller, better-grounded, and less falsifiable number. Trial F1's own verdict calls it "an honest downgrade": the theorem says P7′ is stronger than adopted, not weaker.

**Proof:** Trial F1 (derived 2026-06-12) → [../theory_v3/01_postulates/p7_prime_static_frame_indifference.md](../theory_v3/01_postulates/p7_prime_static_frame_indifference.md) (REVISION banner) and [../theory_v3/development/field_equation_trials/lab_reports/trial_F1_kappa_leak_lab_report.md](../theory_v3/development/field_equation_trials/lab_reports/trial_F1_kappa_leak_lab_report.md) for the T1/T2/T3 derivation chain; machinery in `vacuum_forge/src/field_equation_trials/011_trial_F_cosmology/trial_F1_kappa_leak_coefficient.py`.

**Where next:**
- [Why does a static vacuum carry no energy current? →](idea_frame_indifference.md) — the postulate P7′ this number is a correction to, and its sibling correction (the packing scalaron).
- [The gdot margin →](num_gdot_margin.md) — the other H₀-scale number in the register, from the same cosmology branch, with a very different fate (it killed an entire mechanism instead of shrinking a bound).
- [The scalaron range →](num_scalaron_range.md) — the *other* registered correction to P7′'s double idealization, this one from a → 0 rather than H → 0.
- [The falsifier trail →](hub_predictions.md) — where this number sits among the program's other predictions, and why "derived and unobservable" is a different status than "predicted and testable."
