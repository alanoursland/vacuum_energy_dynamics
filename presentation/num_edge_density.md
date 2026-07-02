# How many edges does the frustrated ground packing have, per unit volume?

The 3D floor's edge density is not a fit parameter — it's a closed-form function of one angle, and it collapses the vacuum's microphysics to a single remaining unknown.

## The claim

The flat, frustrated ground packing (regular tetrahedra, mean edge coordination forced by zero mean deficit) has an exact edge density:

```text
c_e = 36 arccos(1/3) / (sqrt(2) pi) = 9.974276  edges per a^3
```

where `a` is the packing's edge-length scale. This is pure geometry — no free parameter, no fit, no measured input. It follows from two already-derived facts stacked on top of each other:

- The 3D ground mixture (thm_forced_mixture / num_mixture_3d): zero mean deficit angle forces mean edge coordination `n_bar = 2*pi/arccos(1/3) = 5.104299`, mixing coordination-5 and coordination-6 hinges in fixed proportion `x_6 = 0.104299`. This is a hinge identity — it holds regardless of *which* hinges carry which coordination, only the mixture fraction is fixed.
- Counting: each near-regular tetrahedron (edge length `a`, volume `sqrt(2) a^3/12`) contributes 6 edges, but each edge is shared by `n_bar` cells. So edge density is cells-per-volume times edges-per-cell divided by sharing:

```text
c_e = 6 / (V_tet * n_bar) = 36 arccos(1/3) / (sqrt(2) pi)
```

Both `n_bar` and `c_e` are functions of `arccos(1/3)` alone — the same single geometric seed that already produces the deficit gap `Delta_0` (idea_frustration, num_delta0) and the 3D mixture fraction itself. Nothing new is assumed; this is that same angle counted a different way.

**Why it matters — the reduction.** The floor density formula was:

```text
rho_v = (c_e * Delta_0 / 2) * f'(Delta_0) / a^3
```

`f'(Delta_0)` was already eliminated by the floor–Newton lock (thm_self_funding / derivation 039), which ties it to Newton's constant `G`. With `c_e` now derived here, the whole coefficient collapses to a pure number: `rho_v = 0.640290 * f'(Delta_0) / a^3`. Every microphysics constant in the floor is fixed *except* the packing scale `a` itself — the one remaining open question in this whole line (num_gdot_margin's stretching-vs-creation debate lives downstream of the same unknown).

**Bulk cross-check (not yet the real target).** A seeded, smoothed 3D Delaunay complex (N=600 points) gives mean interior edge coordination 5.2158 against the predicted 5.1043, and edge density 11.7361 against the predicted 9.9743 — tens-of-percent off, but the comparison is against a smoothed *random* proxy complex, not the true energy-relaxed ground packing. Phase 3 of the relaxation lab (lab_bulk) is what actually tests the exact value; this run only confirms direction and rough scale ahead of that.

**Proof:** derivation 052 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md)

**Where next:**
- [The Forced Mixture →](num_mixture_3d.md) — the `x_6 = 0.1043` composition this edge count is built on.
- [The Frustration Gap →](num_delta0.md) — the same `arccos(1/3)` seed, read as a deficit angle instead of a density.
- [The Floor Density →](num_floor_density.md) — where `c_e` plugs in to produce the ~10^112 J/m^3 number.
- [The Microstructure Trail →](hub_packing.md) — the full one-input structure this number is one node of.
