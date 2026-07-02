# Does the frustration deficit actually look like curvature?

Before trusting the packing to encode gravity at all, check its coarsest possible triangulation against the textbook integral it's supposed to reproduce.

## The number

The 600-cell is the regular 4-polytope built from 600 tetrahedral cells — the finest regular tessellation of the 3-sphere, but also, for this purpose, the *coarsest* mesh you could legitimately test: one exact edge length, one exact deficit angle, no averaging over a distribution.

Every one of its 720 edges has chord length 1/phi and identical deficit angle Delta_0 = 2pi - 5 arccos(1/3) — the same frustration gap that shows up everywhere else in this program (see `num_delta0.md`). Sum the Regge action over all 720 edges:

```text
S_Regge = 720 * Delta_0 / phi
```

Evaluate it and compare to the continuum Einstein-Hilbert integrand on a unit S^3, (1/2) int R sqrt(g), computed exactly from the sphere's known curvature. The ratio comes out to

```text
S_Regge / S_EH = 0.9647
```

3.5% off, at a mesh with exactly one cell size and one deficit value — no fitting, no free parameter, no continuum limit invoked. The frustration deficit, summed the Regge way, reproduces the Einstein-Hilbert action on the sphere it triangulates.

This is a sanity check, not a convergence proof. It says the correspondence isn't a coincidence of algebra that only works in some limit — it already works at the single coarsest data point available. It's the anchor the rest of the Regge/Delaunay bridge (`idea_frustration.md`'s claim that geometric frustration is *why* gravity is Einstein-Hilbert, via the expansion-point theorem) leans on for plausibility before the harder convergence and 4D/Lorentzian lift work is done.

What it does not do: it doesn't establish a refinement/convergence theorem (does the ratio -> 1 as the mesh refines?), and it doesn't touch the Lorentzian or 4D case — the 600-cell result lives entirely in Euclidean S^3. Both are open obligations, logged as `regge_continuum_limit_039` in the source file.

**Proof:** forge `regge_delaunay_bridge_039`, verified result 3 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md), computation at `vacuum_forge/src/vacuum_sector/039_regge_delaunay_bridge/regge_delaunay_bridge.py`.

**Where next:**
- [The Frustration →](idea_frustration.md) — why this 3.5% match is supposed to explain gravity being Einstein-Hilbert rather than R^2, via the expansion-point theorem.
- [Delta_0 →](num_delta0.md) — the 7.356deg gap that supplies both the deficit angle here and the packing's defining constant everywhere else.
- [The Packing Trail →](hub_packing.md) — where this anchor check sits among the rest of the packing-microphysics results.
- [The Graveyard →](hub_graveyard.md) — for the open obligations this check leaves unresolved (continuum limit, Lorentzian lift, the R^2-class tension).
