# Why does one angle, 7.356°, run the whole vacuum sector?

Every number in the packing's ground state — the floor density, Newton's constant, the coordination mixtures — is a function of a single leftover angle from stacking five tetrahedra around an edge.

## The claim

Five regular tetrahedra sharing an edge in flat space overshoot a full turn — but not by much, and not by zero. Each tetrahedron's dihedral angle is `arccos(1/3) ≈ 70.529°`; five of them sum to `≈ 352.644°`, short of `360°`. Flip the sign convention (deficit, not excess) and the gap is:

```text
Delta_0 = 2*pi - 5*arccos(1/3)  ~=  7.356 degrees  (0.1284 rad)
```

This is the irreducible frustration of the tetrahedral packing in flat space — the thing five-around-an-edge cannot close, no matter how the tetrahedra are shaped, because a regular tetrahedron's dihedral angle is fixed by its regularity. It is not tunable, not fit, not chosen: it falls straight out of `arccos(1/3)`, itself forced by the regular-simplex geometry the packing axiom (P10) assumes.

Why it is "the icon": nearly every downstream constant in the vacuum sector is Δ₀ dressed in different clothes.

- The ground-state coordination mixture in 3D is fixed by demanding the *mean* deficit vanish — which pins the fraction of six-coordinated edges to `x6 = 2π/arccos(1/3) − 5 ≈ 10.43%`, a direct corollary of Δ₀'s value (see `num_mixture_3d.md`).
- The floor energy density `u_floor` carries Δ₀ in its denominator as a normalizing conversion factor (`c_e Δ₀/2 ≈ 0.6403`) and Δ₀² in the substance-energy quadratic form `ρ_v = c_e κ_w Δ₀² / (2 a³)`.
- Newton's constant is read off as the *preload stiffness* of the response at exactly this deficit: `G⁻¹ ∝ f'(Δ₀)` — gravity's strength is the packing's elastic response evaluated at the frustration angle, not at zero.
- The relief geometry (the derivation that killed "partial relief" as a route to Λ's small value) is a one-parameter deformation of this same angle: curving the packing changes the dihedral angle continuously, `cos δ(s) = cos s/(1 + 2 cos s)`, and Δ(s) = 2π − 5δ(s) reduces to Δ₀ exactly at flat space (s = 0), falling *quadratically* in curvature from there — `Delta(s) = Delta_0 − (5√2/24) s² + O(s⁴)`.

So Δ₀ is simultaneously: the frustration that forces a non-uniform coordination mixture (there is no flat, single-coordination ground state), the angle at which G is read off the packing's stiffness, and the anchor point of the curvature expansion that killed the relief mechanism. One angle, three separate jobs, no free parameters in any of them.

**Proof:** relief_exact_geometry_037 (`Delta_0 = 2*pi - 5*arccos(1/3)`, exact endpoint of the relief curve) → [../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md); full numeric table (derivations 046–053) → [../theory_v3/05_vacuum_sector/06_the_ground_state_by_the_numbers.md](../theory_v3/05_vacuum_sector/06_the_ground_state_by_the_numbers.md); original definition and substance-energy role (derivation 039) → [../theory_v3/05_vacuum_sector/01_substance_energy.md](../theory_v3/05_vacuum_sector/01_substance_energy.md)

**Where next:**
- [The 3D ground mixture →](num_mixture_3d.md) — the coordination fraction that Δ₀ = 0-mean-deficit directly forces.
- [The 4D twin →](num_mixture_4d.md) — same forcing logic, one dimension up, with `arccos(1/4)` in Δ₀'s place.
- [The edge density →](num_edge_density.md) — the other pure-geometry constant Δ₀ combines with to fix the floor.
- [The floor's magnitude →](num_floor_density.md) — where Δ₀² lands: the ~5×10¹¹² J/m³ number and why it can't be seen.
