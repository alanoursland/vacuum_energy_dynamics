# Does the frustrated floor survive being scaled up into a real bulk packing?

Phase 2 of the relaxation lab: take the frustration story out of the single-hinge, single-vertex regime and into statistical bulk, and check whether the theory's four load-bearing predictions still hold.

## The lab

Phase 1 (derivation 041) measured the floor at small scale — one relaxed neighborhood, the five-fold coordination minimum, dilation-flat/shear-stiff response, quantized single-vertex defects. Phase 2 (derivation 051) asks the harder question: does any of that survive going to a real statistical bulk, with hundreds of points, seeded and deterministic, no cherry-picked configuration? Four measurements, each aimed at a specific theoretical commitment:

**E1 — Intensivity.** The floor is supposed to be a bulk energy *density* (the substance identity, ρ_v = const, derivation 038) — not a boundary effect, not a finite-size artifact. Relaxed spring energy per vertex of Poisson-Delaunay networks, unit mean edge:

```text
N = 80:  E/N = 0.20241
N = 160: E/N = 0.22928
N = 320: E/N = 0.25048
```

Stable across a factor of 4 in system size. This is the cheapest possible falsifier — if E/N had drifted with N, the floor would be a surface term or a discretization artifact, not a density — and it didn't drift.

**E2 — 4D coordination vs. the mixture prediction.** The 050 ground-state derivation predicts a forced mixture of hinge coordinations in 4D, mean 2π/arccos(1/4) ≈ 4.7668. Interior triangle-hinge census of a 400-point 4D Delaunay complex: mean coordination 4.9805 raw, 4.8614 after a smoothing pass (neighbor-centroid relaxation proxy); {4,5} coordination fraction 0.581 after smoothing. The hinge identity (mean n = 2π / mean dihedral) checks to under 1%. Real triangulations land in the predicted window and move *toward* the mean-field mixture number under regularization — the right direction, not yet the full realizability test.

**E3 — Defect spectrum.** Excess energy over the n=5 floor, by coordination:

```text
n=3: +0.162713   n=4: +0.060500   n=5: +0.000000   n=6: +0.051681   n=7: +0.242112
```

Positive at every n ≠ 5, quantized by coordination, monotone in |Δn|. This is the shape the dark-matter-as-defect candidate needs (see the packing trail) — a well-defined cost ladder, not a continuum of arbitrary defect energies.

**E4 — Disclination networks.** Smoothed 500-point 3D bulk: modal interior edge coordination is 5 (the ground value, as required), defect fraction 0.559, and the largest connected defect component holds 100.0% of all defect vertices. Wrong-coordination edges aren't scattered dust through the bulk — they form one spanning line-like network. This is the morphology phase 1 (041) predicted in advance, now confirmed at bulk scale.

**Proof:** derivation 051 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/bulk_relaxation_phase2_vacuumforge.md)

## The fences

Read exactly what this phase does and doesn't license:

- Smoothing is a relaxation *proxy* — neighbor-centroid averaging, no energy gradient descent, no retriangulation dynamics, no periodic box. The full mixture-realizability verdict is deferred to phase 3 (periodic_energy_relaxation_051), which runs true energy relaxation in a periodic cell.
- E3 and E4 are microstructure exhibits only. No dark-excess production rate or abundance is licensed by this lab — the 017–019 gates and the P9 fence are unchanged. A spectrum shape and a network morphology are not a cosmology.
- Every run is seeded (rng 20260702) and bit-identical; the archive is deterministic and reproducible, not a one-off simulation.

**Where next:**
- [The Frustration →](idea_frustration.md) — why five tetrahedra around an edge leave a gap in the first place, the source of everything phase 2 is measuring.
- [The Floor →](idea_floor.md) — what E1's intensivity result is actually confirming: the constant term in the deficit expansion as a real energy density.
- [The microstructure trail →](hub_packing.md) — the full one-input structure (θ₃, θ₄, the forced mixtures) that E2 is testing against real triangulations.
- [The skeptic's entrance →](hub_graveyard.md) — for the self-threats this same campaign closed elsewhere (dispersion, the scalaron, the boundary channel).
