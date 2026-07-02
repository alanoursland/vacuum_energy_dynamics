# Does the Regge action actually converge to Einstein-Hilbert, or is the 3.5% match a coincidence?

The 600-cell's 3.5% agreement with ∫R√g is one coarse data point; this node is the refinement theorem that turns it into a limit.

## The theorem

A single mesh matching the continuum action to a few percent proves nothing by itself — every discretization scheme reproduces its target at *some* resolution if you're allowed to pick the resolution. What earns the claim is convergence: does the error shrink, in a controlled way, as the triangulation refines? This node discharges that obligation, in three separate pieces, for the packing's Regge-to-Einstein-Hilbert bridge (derivation 039).

**1. 2D is exact, not asymptotic.** For any closed triangulated surface with 2E = 3F, the deficit-angle sum is a combinatorial identity:

```text
sum_v delta_v = 2 pi V - pi F = 2 pi chi
```

There is no refinement limit to take in 2D — discrete Gauss-Bonnet holds exactly at every mesh, coarse or fine (checked on the icosahedron and geodesic refinements ν = 2, 4).

**2. The 2D local rate is exact and quadratic.** For an equilateral geodesic triangle of side `s`, the excess angle sum over the flat value is

```text
excess(s) = (sqrt(3)/4) s^2 [1 + (1/8) s^2 + O(s^4)]
```

— an exact rational relative-error coefficient (1/8), not a numerically fitted one. The Delaunay/deficit encoding converges to the continuum curvature integrand quadratically in edge length, term by term.

**3. The complete regular family in 3D converges quadratically.** There are exactly three regular tetrahedral triangulations of S³ (the only ones that exist): the 5-cell, 16-cell, and 600-cell boundaries. Comparing each exact Regge action to (1/2)∫R√g = 6π²:

```text
5-cell    ratio 0.6916    (1-r)/s^2 = 0.0927
16-cell   ratio 0.7791    (1-r)/s^2 = 0.0895
600-cell  ratio 0.9648    (1-r)/s^2 = 0.0893
```

This is not one point — it's the entire family that exists, and it is monotone toward 1 with a rate coefficient that stabilizes as the mesh refines (drift 3.6% → 0.3% across the three points). Every regular data point available confirms `1 - S_Regge/S_EH = c s^2 (1 + O(s^2))`, c ≈ 0.089, with no free parameter left to tune after the first two points fix it.

**4. What's imported, not proved in-house.** The general statement — arbitrary (non-regular) triangulations, and dimensions beyond 3 — is not re-derived here. It's carried as a declared external mathematical import: Cheeger-Muller-Schrader (1984) and Feinberg-Friedberg-Lee-Ren (1984) both establish Regge-to-continuum convergence in the general case (Fierz-Pauli class results). No coefficient anywhere in this framework depends on the imported piece; it only backstops the claim that irregular meshes and 4D don't break the pattern the regular family already shows.

What this does *not* claim: nothing here is a statement about the packing model's dynamics, mode content, or quantum behavior — this is pure discrete-differential-geometry, checking that the Regge integrand is the right leading-order object. The P7′ Planck-scale tension (the R²-class term that P7′ wants exactly zero) is untouched by this result. The 4D/Lorentzian lift of the *physics* model — as opposed to the geometric convergence proved here — remains a separate, open obligation.

**Proof:** derivation 040 (in-house 2D-exact + exact local rate + complete regular 3D family; general/4D case carried as CMS84/FFLR84 import) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_refinement_convergence_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_refinement_convergence_vacuumforge.md)

**Where next:**
- [Why Einstein-Hilbert →](hub_why_eh.md) — the expansion-point theorem this convergence result backstops: why the leading response is linear-in-deficit at all.
- [The Packing →](hub_packing.md) — the microstructure trail this theorem is one closure item within.
- [The Deficit Angle →](idea_deficit_angle.md) — how curvature is stored on hinges in the first place, the object being refined here.
- [The Graveyard →](hub_graveyard.md) — where claims that *don't* survive scrutiny like this are logged, for calibration.
