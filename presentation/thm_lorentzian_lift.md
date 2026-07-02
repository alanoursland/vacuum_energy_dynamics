# Does the theory even make sense in 4D, with time?

Every earlier result in this program was built and checked in Euclidean 3D; this node is where the packing model gets lifted to 4D and given a light cone, and the checks that make that lift legitimate rather than assumed.

## The theorem

Three separate things have to be true simultaneously for the packing model to be a candidate 4D spacetime theory rather than a 3D toy: the hinge structure has to survive the dimension bump, the action has to admit a Lorentzian continuation at all, and the linearized dynamics have to reduce to something recognizable. All three are checked, at kinematic + linearized scope, and all three hold.

**1. 4D hinge structure is exact.** In 4D, Regge hinges are triangles (not edges), and the regular-n-simplex dihedral angle is `arccos(1/n)`, verified from exact coordinates at n = 2, 3, 4. Every integer coordination around a flat 4D triangle hinge is frustrated — n = 4 gives a deficit of +57.91°, n = 5 gives -17.61° — so, exactly as in 3D, the ground state cannot sit at zero deficit. This is what lets the expansion-point theorem carry over: a frustrated ground state (f'(D₀) ≠ 0) forces the leading gravitational response to be linear in curvature, i.e. Regge/Einstein-Hilbert, not R².

**2. The Lorentzian continuation is term-by-term legitimate.** By polarization, every dihedral cosine and every Gram-structure area/volume in the Regge action is algebraic in *squared* edge lengths — verified exactly for the tetrahedron dihedral (the coordinate expression and the squared-length expression agree). Because the action is built from ℓ² throughout, it continues analytically to ℓ² < 0 term by term. This is the Sorkin/CDT foundation for Regge calculus with a light cone: nothing in the packing model's action blocks the continuation.

**3. Timelike hinge algebra is exact, not approximate.** At timelike hinges the deficit angle becomes a rapidity, and boost composition is exactly additive under the hyperbolic analogue of the angle-sum law:

```text
artanh(u) + artanh(v) = artanh( (u+v) / (1+uv) )
```

— the relativistic velocity-addition identity, holding exactly, the same way Euclidean angles add exactly around a spacelike hinge.

**4. Gauge structure is right at linear order.** Vertex displacements (the discrete relabelings from the earlier coordination-mixture work) are exact zero modes of the deficit action on flat configurations — an interior vertex's angle sum is identically 2π under a symbolic stationarity check, so shifting vertices costs nothing, as required for diffeomorphism-like gauge freedom in a discrete theory. Given that, the mode count needed to call this "linearized Einstein gravity" — massless spin-2, transverse-traceless only — is Rocek & Williams' 1981 theorem that Regge calculus linearizes to Fierz-Pauli gravity. That theorem is imported, not re-derived here, and is flagged as an external declared import rather than an in-house result.

Bonus: the complete regular 4D family (S⁴'s only two members, the 5-simplex and 5-orthoplex boundaries) reproduces the same convergence signature seen in 3D — boundary ratios 0.3065 and 0.4434 against `(1/2)∫R√g = 16π²`, monotone toward 1 with matching quadratic-rate coefficients (0.2208 vs. 0.2256, under 3% apart) — so the continuum-convergence result is dimension-stable, not a 3D accident.

**What this is not.** No dynamical (initial-value / time-evolution) statement is made. The lift is explicitly kinematic + linearized; full nonperturbative Lorentzian dynamics is the CDT-adjacent research frontier and is out of scope by declaration. Also open: which 4D ground-state coordination (n = 4 under-closed vs. n = 5 over-closed, opposite-sign deficits) is the physical one — a genuine unresolved microphysics question, separate from and untouched by the 3D spatial-sign result.

**Proof:** derivation 043 (`lorentzian_4d_lift_043`) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/lorentzian_4d_lift_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/lorentzian_4d_lift_vacuumforge.md); verification script `vacuum_forge/src/vacuum_sector/043_lorentzian_4d_lift/lorentzian_4d_lift.py`. This derivation closes the ninth and final field of the strain-axiom contract (falsifiers, boundary/conservation, mode/hyperbolicity, and the rest all filled across derivations 038–043).

**Where next:**
- [The expansion-point theorem →](thm_expansion_point.md) — the 3D argument this node lifts to 4D: why a frustrated ground state forces the linear Regge/EH term.
- [The evenness theorem →](thm_evenness.md) — the companion no-Lorentz-violation result: why the spectrum is exactly even on any graph in this class, not just this 4D construction.
- [The Schlafli/conservation boundary →](thm_conservation_boundary.md) — the discrete Bianchi identity and hinge-term gluing that this Lorentzian action has to respect.
- [The microstructure trail →](hub_packing.md) — back out to the full packing campaign this 4D lift completes.
