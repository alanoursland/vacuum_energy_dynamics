# Why does the flat 3D packing carry 5.1043 tetrahedra per edge, not 5?

The 3D twin of [the forced mixture](thm_forced_mixture.md): flatness pins the edge-hinge coordination to a specific fraction, not to the softest integer.

## The claim

Five regular tetrahedra around an edge is the softest coordination — smallest deficit magnitude, |delta(5)| < |delta(6)| — but delta(5) = +7.36 deg is not zero. A pure n=5 edge packing is uniformly curved, not flat. Six around an edge overshoots the other way: delta(6) = -63.17 deg. Neither integer works; a flat ground state has to mix them.

Zero mean deficit is one equation; x_5 + x_6 = 1 is the other. Together they force the n=6 fraction exactly:

```text
x_6 = 2*pi/arccos(1/3) - 5 = 0.104299
```

So 10.43% of edges in the flat ground packing carry six tetrahedra, the rest carry five. Equivalently, the mean edge coordination is

```text
n_bar = 2*pi/arccos(1/3) = 5.104299
```

This is the same hinge identity that appears in 4D (n_bar = 2*pi/theta, theta = arccos(1/(d-1))) — it falls out of "zero mean deficit" alone, independent of which two coordinations are doing the mixing. The whole result is a function of one number, arccos(1/3), the regular-tetrahedron dihedral angle — the same sole input as Delta_0 (the icon gap) and the relief function.

The mixture isn't a free parameter chosen to make the geometry work; it's the unique solution once you demand exact flatness from an integer-coordination packing. And it isn't free of cost either — the mixed floor sits strictly between the pure-n=5 and pure-n=6 energies, because 10.43% of edges are forced into the "expensive" n=6 slot as the price of zero mean curvature. That mixture fraction feeds directly into the edge density (6/(V_tet n_bar), derivation 052) and from there into the floor energy density itself.

Cross-check against a bulk proxy (seeded, smoothed 3D Delaunay, N=600): mean interior edge coordination comes out 5.2158 against the predicted 5.1043 — within 10%, on a random complex that isn't the actual energy-relaxed ground packing. Direction and window are the meaningful pre-phase-3 signal; the exact realizability of x_6 = 0.1043 in a real periodic, energy-relaxed 3D packing is still open (phase 3, not yet run).

**Proof:** derivation 052 ("050's logic, one dimension down") → [../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md)

**Where next:**
- [The Forced Mixture →](thm_forced_mixture.md) — the theorem this number instantiates, side by side with its 4D twin.
- [num_mixture_4d.md](num_mixture_4d.md) — the same forcing one dimension up: x_4 = 0.2332, mean hinge coordination 4.7668.
- [num_edge_density.md](num_edge_density.md) — what this mixture buys: 9.9743 edges per a^3, pure geometry, one free constant left.
- [The Gap Delta_0 →](num_delta0.md) — the other exact number built from the same single input, arccos(1/3).
