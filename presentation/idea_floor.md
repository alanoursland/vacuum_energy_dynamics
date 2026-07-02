# Why does empty space cost energy just for being three-dimensional?

The vacuum's substance energy isn't a free parameter to be measured — it's the strain cost of a packing that cannot close, present in every cell of space because 3D geometry itself cannot relax.

## The idea

Regular tetrahedra cannot tile flat 3-space. Five of them fit around a shared edge and fall short of closing by an exact, computable deficit:

```text
Delta_0 = 2*pi - 5*arccos(1/3) ~= 7.3561 degrees
```

(exact, forge derivation 037 — the full relief function `cos(delta(s)) = cos(s)/(1+2cos(s))` closes only on the 600-cell, a curved object, not flat space). Flat embedding forces every hinge to close to `2*pi` anyway, so the cells can't take the curvature they "want" — edges stretch off rest length, dihedrals sit off preference, and the mismatch that cannot exist as geometry exists as energy instead. This is the floor: **unrealized curvature, paid for in strain**.

It's measured, not merely asserted. Derivation 041 relaxes many-body configurations and finds the five-fold wedge is the least-frustrated arrangement of n = 3..7 tetrahedra around an edge, and it still cannot reach zero: E(5) = 0.00065 > 0 in lab units. FCC-type packings relax to exactly zero. The floor is a property of *tetrahedral* local order specifically — of what this vacuum's substance is, not an artifact of the calculation. Two dimensions is free (triangles tile perfectly); three is the first dimension where merely existing costs energy.

This gives P1's founding claim — "the vacuum's reality and its energy content are the same fact, viewed two ways" — an actual mechanism. Being three-dimensional space and carrying strain turn out to be the same fact, because 3D tetrahedral packing cannot close for free.

The density, in the minimal harmonic-wedge model:

```text
rho_v = (c_e * kappa_w * Delta_0^2) / (2 * a^3)
```

with `a` the packing scale, `c_e` the edge-density coefficient, `kappa_w` the wedge stiffness (derivation 038). The floor–Newton lock (039) trades `kappa_w` for the gravitational coupling, so the same wedge energy sets both the vacuum's substance density and the strength of gravity — one number, two readings. `a` and `c_e` remain open (obligation O-P10-1, tracked as `packing_stiffness_microphysics_038`); at Planck-scale `a` the density is Planckian, which would be a flat-out catastrophe if it gravitated locally.

It doesn't, and that's a theorem, not a tuning: dihedral angles are exactly scale-invariant, so any angle-based energy — which is what a frustration floor is — has zero restoring force on the volume mode. P3's constant-density postulate is exactly the unimodular constraint that then fixes that mode, and the unimodular constraint sequesters the constant sector out of the trace-free dynamics gravity actually sees. **The postulate that defines the substance energy is the postulate that hides it.**

The floor is reachable only through processes that change the packing itself — P6 exchange (kinetic energy funded by real vacuum exchange) and a quarantined dimensional-relaxation channel — never through gravity directly.

**Proof:** derivations 037 (exact deficit), 038 (identity/action split/sector signature), 039 (floor–Newton lock), 041 (measured floor, five-fold minimum) → [../theory_v3/05_vacuum_sector/01_substance_energy.md](../theory_v3/05_vacuum_sector/01_substance_energy.md), identification chain and forge pointers in [../theory_v3/development/vacuum_sector/substance_energy_frustration_identity.md](../theory_v3/development/vacuum_sector/substance_energy_frustration_identity.md).

**Where next:**
- [The Frustration →](idea_frustration.md) — the geometric root cause: why regular tetrahedra can't tile 3-space at all.
- [Sequestering →](idea_sequestering.md) — the full mechanism by which a constant density becomes invisible to gravity.
- [The Unimodular Constraint →](idea_unimodular_constraint.md) — how P3's constant-density postulate turns out to be the fixed-measure constraint, not an add-on.
- [Flatness Is Bought →](idea_flatness_is_bought.md) — the campaign-wide theme this node is the founding instance of.
