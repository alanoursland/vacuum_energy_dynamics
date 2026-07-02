# How does a graph of flat pieces store curvature?

Regge calculus, sixty years old, gives the packing's edges a job: curvature lives entirely in the angle gaps at the hinges.

## The idea

A Delaunay-style graph — vertices ("bits of space") joined by edges with lengths `l_e` — is not just combinatorics. Glue a flat simplex onto every cell defined by the graph, using the edge lengths as the only geometric data, and you get a piecewise-flat manifold. Every simplex is internally flat; all the curvature the manifold has is squeezed onto the hinges (2D: vertices, 3D: edges, 4D: triangles), measured as a deficit angle:

```text
delta_h = 2 pi - (sum of dihedral angles incident on hinge h)
```

This is Regge's insight: instead of a smooth curvature tensor, you carry a finite list of numbers, one per hinge, and they carry exactly the same content. Two theorems anchor this as more than a good analogy:

- **Discrete Gauss-Bonnet.** Sum the deficits over an icosahedron's 12 vertices and you get exactly 4π = 2π·χ(S²) — the topological invariant, recovered exactly from a coarse discrete object, no smoothing required.
- **Edge lengths encode curvature at leading order.** For an equilateral geodesic triangle of side `s` on the unit sphere, the angle sum computed purely from the three side lengths exceeds π by (√3/4)s² + O(s⁴) = K × area — the Delaunay intuition ("edge lengths alone tell you the curvature") is exact, not approximate, up to O(s⁴) discretization error.

Now bring in the frustration result from elsewhere in the program: regular tetrahedra cannot close in flat 3-space, so the packing's flat ground state doesn't sit at deficit zero — it sits at the irreducible deficit Δ₀ = 2π − 5·arccos(1/3), the same constant that seeds the floor. Every hinge in the ground state carries this deficit, whether or not anything is curving.

That single fact reorganizes what deficit angle means for this program. Expand a smooth per-wedge energy `f(delta_h)` about the frustrated ground state δ = Δ₀ (not about δ = 0, the naive choice):

```text
E = sum_h V_h f(Delta_0)                                <- floor: substance, sequestered
  + f'(Delta_0) sum_h V_h (delta_h - Delta_0)            <- Regge action -> Einstein-Hilbert
  + (1/2) f''(Delta_0) sum_h V_h (delta_h - Delta_0)^2   <- R^2-class, a^2-suppressed
```

Three consequences fall out of one Taylor series:

1. **The constant term is the floor.** Even a perfectly flat, unstrained packing pays f(Δ₀) at every hinge — this is the substance energy the vacuum sector already argued for on other grounds, now located microscopically at the hinges.
2. **The linear term is gravity.** Because the ground state sits at nonzero deficit, f'(Δ₀) ≠ 0 generically — the Regge action (deficit × edge length, the discrete Einstein-Hilbert integrand) is the leading dynamical response to any departure from the ground state. An unfrustrated packing would instead minimize at δ = 0, forcing f'(0) = 0 by definition of a minimum, and its leading response would be curvature-squared (R² gravity) instead. **Geometric frustration is why gravity is Einstein-Hilbert, not R²** — conditional on the packing being the right ontology, but not an assumption smuggled in: it's a consequence of expanding about the actual (frustrated, nonzero) ground state rather than an idealized (unfrustrated, zero) one.
3. **The floor and Newton's constant are the same stiffness.** ρ_v = (c_e Δ₀ / 2a³) f'(Δ₀) — one wedge-energy stiffness sets both the vacuum's substance density and the coefficient in front of the Einstein-Hilbert term. They cannot be dialed independently.

A closed-form check on the exact coarsest possible mesh: triangulating the unit 3-sphere with the 600-cell (720 edges, chord length 1/φ, every hinge exactly Δ₀) gives S_Regge = 720Δ₀/φ = 0.9648 × (1/2)∫R√g — the frustration deficit reproduces the continuum Einstein-Hilbert action to 3.5%, with no fitting, at the coarsest lattice that exists.

What this does *not* yet claim: no continuum-limit theorem (the 3.5% is one exact data point, not a convergence proof), no 4D/Lorentzian lift, and an honest open tension — the quadratic (R²-class) term carries a Planck-scale coefficient that P7′, as adopted, forces to be exactly zero. Either the packing's f'' term cancels or routes elsewhere, or P7′ is the a→0 idealization of an unobservable Planck-suppressed scalaron. Recorded open, not resolved.

**Proof:** derivation 039 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md), model detail in [../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md).

**Where next:**
- [The Frustration →](idea_frustration.md) — why the ground state sits at Δ₀ instead of zero in the first place, the fact this whole node leans on.
- [The Floor →](idea_floor.md) — the constant term f(Δ₀) in the expansion, argued independently as the vacuum's substance energy.
- [Flatness Is Bought →](idea_flatness_is_bought.md) — the campaign-level theme this node gives a microscopic mechanism for.
- [The Packing Model →](idea_packing.md) — the axioms (edge-length graph, flat cells, per-hinge energy) this node's theorems are proved on top of.
