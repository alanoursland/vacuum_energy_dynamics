# Paper 8 Outline: Gravity from a Frustrated Packing

## Working Title

**Geometric Frustration as the Origin of the Einstein-Hilbert Action:
A Regge/Delaunay Microphysics for the Vacuum**

Shorter title option:

**Frustration Is Why Gravity Is Einstein-Hilbert**

## Target Venues

Primary path: arXiv gr-qc preprint; Zenodo DOI fallback.

Journal targets:

- Classical and Quantum Gravity (discrete-gravity referee pool:
  Regge calculus, CDT, causal sets).
- Physical Review D (if trimmed toward the theorem + numerics core).

Spin-off option (decide during drafting): the evenness/dispersion
theorem as a standalone short PRD note if the main paper exceeds ~30
pages.

## Central Claim

Model the vacuum as a packing: an edge-length graph, piecewise-flat
cells, hinge-deficit curvature, energy a smooth per-hinge function
f(delta) of the closure mismatch. Then:

```text
THE EXPANSION-POINT THEOREM. Regular tetrahedra do not tile 3-space:
the ground state is FRUSTRATED, sitting at delta = Delta_0 =
2 pi - 5 arccos(1/3) where f'(Delta_0) != 0. Expanding the energy
about a frustrated point makes the LINEAR term -- the Regge action,
hence Einstein-Hilbert -- the generic leading response. An
unfrustrated ground state would have given R^2 gravity.

Gravity is the linear elasticity of a vacuum that cannot relax.
```

Supporting results, each forge-verified and each with a measured
numerical counterpart where applicable:

```text
- flatness forces exact coordination mixtures and derived constants:
  x_6 = 2 pi/arccos(1/3) - 5 (3D), x_4 = 5 - 2 pi/arccos(1/4) (4D),
  mean coordinations 5.1043 / 4.7668, edge density
  c_e = 36 arccos(1/3)/(sqrt 2 pi) = 9.9743 per a^3 -- one geometric
  input per dimension; FLATNESS IS BOUGHT (the floor is its price)
- continuum limit: complete regular families converge to EH at
  quadratic rate (2D exact; 3D and 4D computed; general case a
  declared import)
- the evenness theorem: real finite-range harmonic actions on ANY
  graph have spectra exactly even in k -- no linear Lorentz
  violation, structurally; leading correction quadratic and
  Planck-suppressed
- the scalaron scoping: the R^2-class correction survives the
  unimodular constraint (refutation recorded) but is Planck-range --
  P7' holds as the a -> 0 idealization with two derived, controlled,
  sub-observable corrections
- the selector closure: the edge-length ontology stores EXACTLY a
  metric per cell (C(n+1,2) = n(n+1)/2); Finsler data is unstorable
- the kill record: partial relief dead; boundary channel dead (the
  operator instantiated and excluded by 54-114 orders); doors close
  rather than open
- the lab: floor measured and local-order-dependent; five-fold
  minimum; intensivity; defect spectrum; disclination networks
```

## Paper Scope

Claim strongly:

- the expansion-point theorem and its converse (unfrustrated => R^2);
- the exact ground-state structure (mixtures, coordinations, c_e) at
  mean-field level, with the fence stated;
- the evenness theorem for the entire model class;
- the numerical results (all seeded/deterministic, archive-stable);
- the closures and kills (Finsler, boundary channel, partial relief).

Scope carefully:

- the general irregular-triangulation continuum limit is a
  Fierz-Pauli-class import (CMS84/FFLR84); in-house proofs cover
  complete regular families in 2D/3D/4D;
- Lorentzian dynamics is kinematic + linearized (043); the
  initial-value problem is the stated frontier;
- the packing scale a is underived; Planck-scale a is an assumption,
  used only where explicitly marked;
- matter is not in this paper (the defect spectrum is an exhibit; the
  matter-as-defect charter is gated).

## Intended Reader

- discrete-gravity community (Regge, CDT, causal sets, quantum
  graphity);
- condensed-matter/geometric-frustration researchers (their concept,
  exported);
- modified-gravity readers who ask "why EH and not R^2?".

The paper must be readable WITHOUT the VED postulate stack: the
packing model is stated axiomatically in section 2, and the ontology
appears only as motivation (one subsection) plus the sequestering
cross-reference to paper 7.

## Abstract Skeleton

We propose and develop a microphysical model of the gravitational
vacuum as a packing: an edge-length graph whose cells are
piecewise-flat, whose curvature is hinge-deficit, and whose energy is
a smooth per-hinge function of the closure mismatch. Because regular
tetrahedra do not tile three-dimensional space, the model's ground
state is geometrically frustrated: it sits where the energy has
nonzero slope. Expanding about this pre-tensioned point makes the
linear (Regge) term the generic leading response, so the emergent
low-energy action is Einstein-Hilbert; an unfrustrated microstructure
would instead have produced curvature-squared gravity. We quantify the
ground state exactly at mean-field level -- flatness forces derived
coordination mixtures, a derived edge density, and a strictly positive
frustration floor that is the price of flatness -- and verify the
structure numerically in relaxed and statistical packings. We prove
that no member of the model class produces linear-order Lorentz
violation (a reality/evenness theorem), locate the surviving
Planck-range scalaron correction, show that the edge-length state
space cannot store Finsler structure, and record two decisive negative
results (the partial-relief route to the cosmological constant; the
engineered-boundary release channel). The model's floor is
Planck-scale and exactly sequestered from gravity; its observational
profile is a set of sharp nulls. All results are machine-verified.

## Section Plan

### 1. Introduction

- The question: why is the low-energy gravitational action EH rather
  than R^2 (or Finsler, or nonlocal)?
- The answer in one line: because the vacuum's ground state is
  frustrated, and loaded springs respond at first order.
- Situate: Regge calculus; CDT; causal sets; induced/Sakharov
  gravity; geometric frustration in condensed matter.
- Roadmap + verification-archive statement.

### 2. The Model

- Axioms: edge-length graph; piecewise-flat cells; hinge deficits;
  E = sum_h V_h f(delta_h); smoothness of f; ground state = flat,
  minimum-energy subject to closure.
- The motivating ontology in one subsection (cite papers 1, 7).
- What the state space IS: the degree-of-freedom count
  C(n+1,2) = n(n+1)/2 -- the cell stores exactly a metric
  (this early, because it pays off twice later).

### 3. Frustration: the Ground State Cannot Relax

- The deficit ladder in 3D: no integer coordination closes flat;
  Delta_0 = 2 pi - 5 arccos(1/3).
- The exact dihedral/relief function; quadratic flatness (the
  partial-relief kill, first negative result).
- The relaxation lab, phase 1: the floor measured
  (icosahedral-frustrated vs FCC-unfrustrated); the five-fold
  minimum; dilation-flat/shear-stiff.

### 4. The Expansion-Point Theorem

- Statement and proof: E = floor + f'(Delta_0) x (Regge action)
  + (1/2) f''(Delta_0) x (R^2-class, a^2-suppressed).
- The converse: f'(ground) = 0 => leading response R^2.
- The floor-Newton lock: f'(Delta_0) calibrated by G; no residual
  freedom.
- The 600-cell anchor (EH action reproduced at 3.5% at the coarsest
  mesh) and the quadratic-rate convergence of complete regular
  families (2D exact; 3D three-family; 4D two-family); the CMS84/
  FFLR84 import boundary stated precisely.

### 5. The Ground State, Quantified

- Flatness forces mixtures: the zero-mean-deficit argument; 3D
  (x_6 = 0.1043, mean coordination 5.1043) and 4D (x_4 = 0.2332,
  mean 4.7668).
- FLATNESS IS BOUGHT: the mixed floor strictly positive, strictly
  between pure costs.
- The edge density c_e = 9.9743/a^3; the conversion factor reduced
  to one unknown (a).
- The bulk lab: intensivity (E/N stable across x4 size); 4D Delaunay
  coordination statistics vs the prediction; defect spectrum;
  disclination networks. Mean-field fence + phase-3 statement.

### 6. Conservation, Boundaries, and the Lorentzian Lift

- Schlafli identity (discrete Bianchi); Hartle-Sorkin additivity
  (the GHY property).
- 4D hinges; rapidity algebra; Wick term-by-term; gauge zero modes
  and the Rocek-Williams import.
- The frontier stated: initial-value dynamics (O-P10-4) is open.

### 7. The Model Defends Itself (self-tests and closures)

- The evenness theorem: D(-k) = D(k)* for any real finite-range
  harmonic action => spectrum even in k => no linear LIV, ever;
  quadratic scale ~ sqrt(24) E_P; margin ~6e8; the chiral watch item.
  (Spin-off decision point lives here.)
- The scalaron: the unimodular-cancellation refutation (honest
  negative, shown in-house), the Bianchi reconstruction, and the
  scoping resolution -- P7' exact in the (H -> 0, a -> 0) double
  idealization; two derived corrections, both quadratic in their
  small parameter, both sub-observable.
- The selector closure: parallelogram/polarization identities for
  generic forms; Finsler unstorable (the DOF table); direction
  dependence lives only at hinges, as curvature.
- The boundary-channel kill: the operator derived (constant pressure,
  distinct from Casimir d^-4), its locked magnitude, the 54-114 order
  exclusion; matter is strain content, not walls.

### 8. Observational Profile

- The sharp nulls: no Yukawa at any range; no linear LIV (now a
  falsifier); GW purity; exact GR black-hole exteriors.
- The floor: Planck-scale, sequestered (cite paper 7), boundary-
  invisible (section 7.4); the CC problem restated as structure.
- The discreteness consistency battery: if a is ever measured, the
  floor-Newton lock must reproduce G AND a scalaron Yukawa must
  appear at range sqrt(6) a -- parameter-free, twice overdetermined.
- Pointer to paper 9 (expansion as creation; Gdot = 0).

### 9. What the Model Does Not Do (honesty section)

- a underived; matter not included; Lorentzian dynamics open;
  mean-field mixtures pending phase 3; dark-excess candidates gated.

### 10. Conclusion

### References

Regge; Cheeger-Muller-Schrader; Feinberg-Friedberg-Lee-Ren;
Hartle-Sorkin; Rocek-Williams; Hamber; Ambjorn-Loll (CDT); Bombelli
et al. (causal sets); Sakharov; geometric-frustration reviews
(Sadoc-Mosseri); Lorentz-violation bounds (GRB time-of-flight);
Eot-Wash; repository DOI + verification index.

### Appendix A: Exact Dihedral and Relief Functions
### Appendix B: Complete Regular Families (2D/3D/4D convergence data)
### Appendix C: The Evenness Theorem (full proof + witnesses)
### Appendix D: The Lab (instrument specification; all seeds; all
                measured tables)
### Appendix E: Forge Verification Index (claim -> derivation ->
                script, 037-053)

## Figures

1. The frustrated wedge: five tetrahedra around an edge, the 7.36 deg
   gap (the paper's icon).
2. E(n) wedge-ring curves, 3D and 4D (lab data).
3. Expansion-point schematic: f(delta) with the ground state on the
   slope; EH from the linear term; R^2 inset for the unfrustrated
   case.
4. Convergence plot: complete regular families -> EH, quadratic rate.
5. Coordination histograms (3D and 4D Delaunay, raw vs smoothed, with
   predicted mixture lines).
6. Disclination network render (the 051 defect subgraph).
7. Dispersion: omega(k) for the witness chain; the evenness argument
   as a one-panel diagram.

## Writing Notes

- The expansion-point theorem is the paper; everything else is
  support. Front-load it (statement in the introduction, proof by
  section 4).
- Every number in prose carries its exact form (functions of
  arccos(1/3), arccos(1/4)) at first occurrence.
- Negative results get their own headers -- the kill record is part
  of the claim to seriousness.
- Length target: 25-35 pages + appendices; if over, spin off the
  evenness note.
