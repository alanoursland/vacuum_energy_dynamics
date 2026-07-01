# The Regge/Delaunay Packing Model

## Status

```text
result type:   model definition + first theorems (derivation 039,
               forge-verified); candidate microphysics for the vacuum
               substance
scope:         the model is a candidate reading of P1-P5's ontology at
               the packing level; its first theorems are exact discrete
               geometry; continuum limit and 4D/Lorentzian lift are open
conclusion:    curvature is exactly encoded in edge data; the frustrated
               expansion point makes Einstein-Hilbert the generic
               gravitational response (roadmap 1C's weighting question,
               answered conditionally); the floor density and the EH
               coefficient are locked by one wedge energy
non-conclusion: no continuum-limit theorem; no quantum formulation; the
               packing reading remains a candidate ontology, not a
               licensed derivation of the closed sector
verification:  vacuum_forge/src/vacuum_sector/039_regge_delaunay_bridge/
               report: regge_delaunay_bridge_vacuumforge.md
```

## The Model

This formalizes the theory owner's long-standing intuition — "bits of
space connected by a Delaunay graph with different edge lengths
representing curvature" — and identifies it with a sixty-year-old
formalism: **Regge calculus with a frustrated ground state.**

```text
X (configuration variable):  a graph — vertices ("bits of space"),
                             edges with lengths l_e
geometry:                    piecewise-flat simplices glued on the graph;
                             all geometric content is in the edge lengths
curvature:                   concentrated on hinges (2D: vertices,
                             3D: edges, 4D: triangles) as deficit angles
                             delta_h = 2 pi - sum of incident dihedrals
frustration:                 in flat 3D, regular tetrahedral packing
                             cannot close: every edge-hinge carries the
                             irreducible deficit
                             Delta_0 = 2 pi - 5 arccos(1/3)  (exact, 037)
energy:                      E[X] = sum_h V_h f(delta_h) for a smooth
                             per-wedge energy f (V_h = hinge measure:
                             edge length in 3D, triangle area in 4D)
ground state (P5):           the minimum-frustration configuration —
                             flat, delta_h = Delta_0 everywhere (037:
                             curving to relieve costs more than it saves
                             at any sub-packing curvature)
```

The correspondences already established elsewhere in the program:

- the ground state's constant energy density is the **substance energy**
  (P1/P3), sequestered (035, 038);
- angle-based energy is exactly dilation-flat and shear-stiff, giving
  the trace-constrained / shear-energetic sector signature bottom-up
  (038);
- relief geometry is exact and nonperturbative (037).

## The 039 Theorems

**1. Discrete Gauss–Bonnet (2D anchor).** Icosahedron vertex deficits
sum to $4\pi = 2\pi\chi(S^2)$, exactly. Hinge-concentrated curvature
carries the continuum's topological content.

**2. Edge lengths encode curvature.** The angle sum of an equilateral
geodesic triangle, computed from its side lengths alone, exceeds $\pi$
by $(\sqrt3/4)s^2 + O(s^4) = K\times$area. The Delaunay intuition is
exact at leading order, with $O(s^4)$ discretization error.

**3. The deficit is the discrete EH integrand.** Triangulating unit
$S^3$ by the 600-cell (720 edges, chord length $1/\varphi$, five flat
tetrahedra per edge), every hinge carries exactly $\Delta_0$, and

$$S_{\rm Regge} = \sum_e \ell_e\,\delta_e = \frac{720\,\Delta_0}{\varphi}
= 0.9648 \times \tfrac12\!\int_{S^3}\! R\sqrt{g}.$$

The same exact number that seeds the floor reproduces the
Einstein–Hilbert action to 3.5% at the coarsest possible mesh.

**4. The expansion-point theorem (the central result).** Expanding the
wedge energy about the frustrated ground state:

$$E = \underbrace{\textstyle\sum_h V_h\, f(\Delta_0)}_{\text{floor
(substance, sequestered)}}
\;+\; \underbrace{f'(\Delta_0)\sum_h V_h(\delta_h - \Delta_0)}_{\text{Regge
action } \to \text{ EH}}
\;+\; \underbrace{\tfrac12 f''(\Delta_0)\sum_h V_h(\delta_h-\Delta_0)^2}_{
R^2\text{-class, } a^2K\text{-suppressed}} .$$

Because the ground state sits at **nonzero** deficit, $f'(\Delta_0)\neq0$
generically: the linear (Regge → Einstein–Hilbert) term is the generic
leading response. An *unfrustrated* packing would sit at its energy
minimum $\delta=0$, where $f'(0)=0$ necessarily — its leading response
would be curvature-squared.

**Geometric frustration is why gravity is Einstein–Hilbert.** This is
the answer to roadmap path 1C's open weighting question ("holonomy
selects EH only if the ontology supplies a reason for linear deficit
rather than squared mismatch"): the frustrated expansion point *is* the
reason. Conditional on the packing reading, stated as such.

**5. The floor–Newton lock.** One stiffness serves both ledgers:
$\rho_v = \big(c_e\Delta_0/2a^3\big)\,f'(\Delta_0)$ — the substance
energy of the vacuum and the strength of gravity are two readings of
one wedge energy, and $\kappa_w$ is eliminated from the model's
constants (remaining: $a$, $c_e$).

## Against the Strain-Axiom Contract

The 031 contract asked what any strain axiom must supply. This model is
the first candidate with most fields filled:

| contract field | this model |
|---|---|
| X | the edge-length graph |
| metric response map | edge lengths → piecewise-flat metric (exact) |
| neighboring mismatch | hinge deficits (exact) |
| K_strain invariant | $\sum_h V_h f(\delta_h)$ |
| boundary data | open (discrete GHY analog not constructed) |
| conservation identity | open (discrete Bianchi/Regge identities exist in the literature; not yet in-house) |
| mode/hyperbolicity | partially: dilation-flat/shear-stiff (038); full mode count open |
| epsilon classification | EH + $a^2$-suppressed $R^2$-class (039); continuum limit open |
| falsifier | volume-mode restoring force (breaks 038 identity); a detected boundary-smoothing scale (P7′ ledger) |

Two contract fields and the continuum limit stand between this model
and a strain-axiom adoption decision with actual content — which is
exactly what the 032 sieve said no candidate had. The sieve now has a
candidate worth sieving.

## Honest Tensions and Limits

1. **The P7′ tension** (`p7prime_packing_tension_039`): the expansion's
   quadratic term is $R^2$-class with Planck-scale coefficient; P7′
   forces the four-derivative sector *exactly* empty. Either the
   packing's $f''$ contribution cancels or routes into the constraint
   sector, or P7′ is the $a\to0$ idealization of a Planck-suppressed,
   observationally inert scalaron. No closed coefficient moves either
   way; the tension lives entirely at the Planck scale. Open.
2. **No continuum-limit theorem** (`regge_continuum_limit_039`): check 3
   is one exact coarse-mesh data point plus the known Regge convergence
   class; the in-house refinement theorem and the 4D/Lorentzian lift
   are owed.
3. **Discreteness is assumed, not derived.** The model presupposes a
   packing scale $a$. "Is space discrete?" remains the deepest open
   question; this model is what the ontology looks like *if* it is.
4. **No quantum formulation.** The graph is classical. The owner's
   quantum-unification hope lives beyond this note's scope.

## Open Obligations

```text
regge_continuum_limit_039       refinement/convergence theorem; 4D lift
p7prime_packing_tension_039     resolve a^2-suppressed R^2 vs exact P7'
packing_stiffness_microphysics_038 (reduced)  derive a, c_e
discrete boundary/conservation  the two unfilled contract fields
numerical relaxation module     simulate frustrated packings; measure
                                deficit distributions and defect
                                structures (the forge's first
                                experimental module; feeds the dark-
                                excess lane: defects = gravitating
                                excursions)
```
