# Does the discrete Regge action actually close — conserve and glue — like a real gravitational action should?

Two identities, both exact and both old (Regge 1961, Hartle-Sorkin 1981), verified on the packing's own hinges: the Schlafli identity closes the field equations, and the boundary term is exactly additive under gluing.

## The theorem

A gravitational action isn't done just because it has the right integrand. It has to survive two more tests: varying it must produce field equations built only from the curvature data (not stray boundary junk), and cutting a manifold in half and re-gluing it must reproduce the whole action exactly. In the continuum these are the (contracted) Bianchi identity and the Gibbons-Hawking-York (GHY) boundary term. The packing model owed both — they were the last two open fields in the strain-axiom contract (031) — and this derivation (042) fills them.

**1. Conservation — the Schlafli identity.** For a flat tetrahedron, under *every* shape deformation:

```text
sum_e l_e * d(delta_e) = 0
```

the edge lengths weighted by the *change* in dihedral deficit at each edge sum to zero identically. Verified to 50-digit precision at generic exact configurations and exactly, symbolically, on the symmetric one-parameter family. In 2D the anchor is even more elementary: a triangle's angle sum is identically π under every deformation — the base case of the same identity.

Consequence: `d S_Regge = sum_e delta_e d l_e`. The `l_e d(delta_e)` terms cancel identically, so the Regge action's variation carries *only* the deficit-times-edge-length terms — the discrete field equations are built purely from the deficits, with no leftover dependence on how the dihedral angles themselves move. This is the discrete Bianchi/diffeomorphism structure: under vertex displacements (the packing's discrete relabeling freedom), the action varies only through the metric data. Nothing extra to gauge-fix, nothing extra to renormalize away.

**2. Boundary data — Hartle-Sorkin additivity.** Define the hinge boundary term:

```text
psi_h = pi - sum(dihedral angles at h)
```

for a hinge sitting on a cut boundary. Gluing two pieces M1, M2 along that boundary should reproduce the action of the whole: S(M1) + S(M2) = S(M1 ∪ M2). Verified as an exact identity — the two boundary terms sum to exactly the interior deficit that would have been there had the hinge never been cut: psi_1 + psi_2 = Delta_0 (checked on a wedge-ring 2+3 witness: (π − 2δ) + (π − 3δ) = Δ₀, exact). Additivity under gluing is precisely the defining property of GHY in the continuum — a boundary term that makes the variational principle well-posed on manifolds-with-boundary and costs nothing extra when you don't cut at all.

**3. A free bonus — discrete Gauss-Bonnet with boundary.** Combinatorially exact: sum_int delta + sum_bnd kappa = 2π·χ, given the Euler-type relations 2E_int + E_bnd = 3F and E_bnd = V_bnd, checked on a flat hexagonal-disk witness.

Together these fill the last two of nine fields in the strain-axiom contract:

```text
conservation identity    Schlafli => Regge variation closes    FILLED (042)
boundary data             Hartle-Sorkin psi_h, additive         FILLED (042)
```

Eight of nine fields are now filled; the ninth (full Lorentzian mode count) is partial, pending the 4D lift. The strain-axiom adoption decision (032) is now a live decision with content — not a placeholder waiting on missing math.

What this does *not* claim: the constant-curvature (non-flat-simplex) Schlafli formula, and the full 4D/Lorentzian version of both identities, are not needed for the contract as stated and are not proved here. Scope is flat-simplex Schlafli, 2D/3D.

**Proof:** derivation 042 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/discrete_conservation_boundary_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/discrete_conservation_boundary_vacuumforge.md), verification script `vacuum_forge/src/vacuum_sector/042_discrete_conservation_boundary/discrete_conservation_boundary.py`.

**Where next:**
- [The Continuum Convergence →](thm_continuum_convergence.md) — once the action is known to close and glue correctly, does it converge to Einstein-Hilbert as the mesh refines?
- [The Expansion Point →](thm_expansion_point.md) — why the closed Regge action is the *leading* response at all, rather than an R² theory.
- [The Einstein Closure →](thm_einstein_closure.md) — the master result this conservation identity is a load-bearing piece of.
- [The Lorentzian Lift →](thm_lorentzian_lift.md) — the open 4D/Lorentzian mode count this node leaves as the ninth, unfilled contract field.
- [The Microstructure Trail →](hub_packing.md) — back to the packing model these two identities are proved on top of.
