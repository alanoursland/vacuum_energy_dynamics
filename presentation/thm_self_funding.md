# Does the expanding universe have to pay for the space it creates?

A reader who knows the floor is a real, constant, intensive energy density and wants to know how new volume gets funded when the universe expands — this is the theorem that closes the books.

## The theorem

Cosmic expansion has two possible readings, and the closed FRW metric sector cannot distinguish them — both give the same `a^3` volume history and the same dust stress:

- **Stretch:** the packing graph is fixed, edge length dilates, `l = l_0 * a(t)`, cell count `N` fixed.
- **Growth:** edge length stays at the packing's natural scale, `l = const`, and cell count grows, `N ~ a^3`.

The discriminator isn't the metric — it's what each reading does to quantities the theory has already locked elsewhere. Both readings die or survive on *existing* results, not new assumptions.

**Stretch is killed twice, independently:**
1. The floor–Newton lock ties `G ~ 1/(f'(Delta_0) * l)`. Under stretch, `l` grows with `a(t)`, forcing `Gdot/G ~ -H ~ -7.2e-11/yr` — excluded by lunar laser ranging (`|Gdot/G| < 1.5e-13/yr`) by a factor of ~480.
2. Wedge energies are dilation-invariant (measured), so under stretch the *total* floor energy `E_floor` stays constant while volume grows, giving `p_floor = -dE/dV = 0` — a dustlike, `w = 0` component whose density then dilutes as `u ~ a^-3`. That breaks the intensivity P3 sequestering depends on, and the resulting floor density gravitates at ~5e112 J/m^3 — about 1e122x closure. Stretch would also demolish the sequestering architecture, not just fail a bound.

**Growth survives, and does more than survive — it self-funds:**

```text
growth: l = const  =>  G = const, exactly
floor intensive (u = const, measured)  =>  p = -dE/dV = -u
=>  w = -1 exactly, at the substance level
=>  creation cost u*dV = negative-pressure work -p*dV, term by term
```

The first law pays for creation directly: the energy needed to fill new volume at density `u` is exactly what negative pressure `p = -u` does as work when that volume opens up. No external funding mechanism, no separate creation-field, no free parameter — the same constancy of `l` that keeps `G` fixed is the constancy that makes the floor intensive, and floor-intensive is definitionally `w = -1` at the substance level. One reading (growth), three locks (G fixed, w = -1, creation funded) closing simultaneously, zero tuning.

This forces a standing commitment: **Gdot = 0, exactly, forever** — not asymptotically, not as a current best-fit, but structurally, because there's no mechanism left in the theory for G to drift. It also opens a live question the theory does not yet answer: a proposed creation-suppression clause, `C = 3H(1 - alpha*delta)`, where mass suppresses local creation and new space appears preferentially away from overdensities. Its background average `<C> = 3H` for any `alpha` (since `<delta> = 0`), so it's invisible to everything derived so far — `alpha` is only computable once the Lorentzian creation dynamics (O-P10-4) are in hand. No observable is claimed for it yet.

**Proof:** derivation 054, "the 045 seam, decided" → [../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md).

**Where next:**
- [The Floor →](idea_floor.md) — what the intensive density `u` this theorem leans on actually is and where the 037/038/041 numbers come from.
- [Sequestering →](idea_sequestering.md) — why constant density doesn't gravitate, the other half of why the floor can sit at Planckian scale safely.
- [The Vacuum-Flow Idea →](idea_vacuum_flow.md) — the founding intuition behind the `C = 3H(1 - alpha*delta)` clause this theorem leaves open.
- [The falsifier trail →](hub_predictions.md) — Gdot = 0 as a pre-registered, currently-testable commitment.
