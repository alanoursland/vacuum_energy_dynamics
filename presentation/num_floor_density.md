# What is the actual number for the vacuum's floor density, and why has no one ever seen it?

The frustration floor isn't a hand-wave "Planck density" placeholder — it's a specific derived number, and the theory also derives, independently, why it can never show up in an experiment.

## The number

Every other piece of this program's cosmological-constant story is qualitative (sequestering hides constant density; the floor is a candidate filler for Face 2 of the CC problem). This node is the one place a number actually gets produced and evaluated.

The floor-Newton lock (derivation 039) plus the derived edge-density constant `c_e` (derivation 052, pure geometry — see `num_edge_density.md`) fix the floor's energy density with no free coefficient once the packing scale `a` and the mean-square hinge frustration `<delta^2>` are fixed:

```text
u_floor = c^4 * c_e * <delta^2> / (32 * pi * G * Delta_0 * a^2)
```

`Delta_0` is the exact five-tetrahedra deficit angle (`num_delta0.md`); `c_e` is pure packing geometry; `G` and `c` are measured constants — the only physics input left is the packing scale `a`. At the natural, maximally-frustrated choice `a = l_P` (Planck length):

```text
u_floor ~= 5.07e+112 Pa  (= J/m^3)
```

That's the textbook cosmological-constant-problem number, derived rather than asserted — sitting roughly 122 orders above the observed dark-energy density, which is exactly the scale of catastrophe the naive QFT vacuum-energy sum has always produced. VacuumForge derivation 053 evaluates the same formula at the most generous packing scale anyone could argue for, `a = 30 um` (tuned to the UFFT Casimir-squeeze window), and still gets `u_floor ~= 1.47e+52 Pa` — 52 orders above the Casimir-class anomalous-pressure bound of ~1e-2 Pa. There is no reading of `a`, from Planck length to laboratory-generous, where this density would fail to be catastrophic if it coupled to anything measurable.

It doesn't. Two independent derivations kill every channel by which `u_floor` could be seen, for structurally different reasons:

- **Gravity never sees it.** Constant bulk density enters the field equations only through the P3 unimodular constraint (`AB = 1`), never as a curvature source (`idea_sequestering.md`, `idea_cc_problem.md` Face 1). This is a statement about the field equations' structure, independent of the number's size.
- **Boundaries never see it either.** The one channel that structurally *could* read an energy difference instead of an absolute density — confining a slab to quasi-2D, where frustration relaxes to exactly zero (2D tetrahedral packing is frustration-free) — was built out explicitly and killed by magnitude: `P = u_floor`, constant in thickness, excluded by 54 to 114 orders of magnitude against real Casimir bounds (derivation 053, the boundary-channel operator).

So the number isn't small, and it isn't hidden by a cancellation tuned after the fact — it's exactly Planckian, exactly where naive QFT said the catastrophe should be, and every mechanism by which it could leak into an observable is independently and structurally closed. The catastrophe is real and unrelieved on paper; it is simply, provably, never visible.

**Proof:** derivation 053 (boundary channel operator, evaluates `u_floor` at `a = l_P` and `a = 30 um`) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/boundary_channel_operator_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/boundary_channel_operator_vacuumforge.md); the floor-Newton lock and floor identity underlying the formula are derivations 037-039, 041.

**Where next:**
- [Could you tap the vacuum's floor by boxing it into 2D? →](kill_boundary_channel.md) — the full kill certificate for the boundary channel, same number, worked in detail.
- [What is the frustration floor? →](idea_floor.md) — where `u_floor`'s formula comes from and what `<delta^2>` and `a` physically mean.
- [How does constant density become invisible to gravity? →](idea_sequestering.md) — the other, independent invisibility mechanism, closed at the field-equation level.
- [Why split the cosmological constant problem into two problems, not one? →](idea_cc_problem.md) — how this number's catastrophic size and its total invisibility coexist without contradiction.
