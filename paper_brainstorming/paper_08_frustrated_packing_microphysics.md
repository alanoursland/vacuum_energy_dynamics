# Paper 8: Gravity from a Frustrated Packing

**Working title:** *Geometric Frustration as the Origin of the
Einstein–Hilbert Action: A Regge/Delaunay Microphysics for the Vacuum*

**Venue:** arXiv gr-qc. Journal: CQG or PRD for the full paper;
the discrete-gravity community (Regge calculus, CDT, causal sets)
is the natural referee pool. This is the program's flagship result
after paper 1 and the most novel single idea in the repository.

**Audience:** discrete/emergent gravity (Regge, CDT, causal sets,
quantum graphity), condensed-matter-for-gravity people (geometric
frustration is *their* concept, imported to the vacuum), and anyone
who has asked why gravity is EH rather than R².

## The claim

Model the vacuum as a packing: an edge-length graph, piecewise-flat,
hinge-deficit curvature, energy a smooth per-hinge function f(δ) of
the closure mismatch. Then:

1. **THE EXPANSION-POINT THEOREM (the headline).** Regular tetrahedra
   do not tile 3-space: the ground state is *frustrated*, sitting at
   δ = Δ₀ = 2π − 5arccos(1/3) ≠ 0 where f′(Δ₀) ≠ 0. Expanding the
   energy about a frustrated point makes the *linear* term — the
   Regge action, hence Einstein–Hilbert — the generic leading
   response. An unfrustrated ground state (f′ = 0) would have given
   R² gravity. **Frustration is why gravity is Einstein–Hilbert.**
2. The ground state is quantified with one geometric input per
   dimension: flatness forces exact coordination mixtures
   (x₆ = 2π/arccos(1/3) − 5 in 3D; x₄ = 5 − 2π/arccos(1/4) in 4D),
   exact mean coordinations, and the edge density
   c_e = 36arccos(1/3)/(√2π). Flatness is *bought* — the floor is
   its price.
3. The floor is the substance energy: enormous (~Planck density with
   the O(1) factor now derived), exactly sequestered (paper 7's
   mechanism), dilation-flat/shear-stiff (the trace-constrained
   sector signature emerges bottom-up).
4. The model survives its sharpest self-tests: the evenness theorem
   (real harmonic actions on ANY graph give spectra exactly even in
   k — no linear Lorentz violation, by structure, not by tuning) and
   the scalaron scoping (the R²-class correction is Planck-range,
   ~30 orders below laboratory reach).
5. Numerical companion: the relaxation lab (floor measured,
   local-order-dependent; five-fold minimum; intensivity; defect
   spectrum; disclination networks) — every structural claim has a
   measured counterpart.

## Results inventory (forge derivations)

```text
037  exact dihedral function; relief quadratic-flat; the flat
     frustrated ground state
038  substance-ledger identity; dilation-flat/shear-stiff signature
039  Regge/Delaunay bridge; THE EXPANSION-POINT THEOREM; floor-Newton
     lock (600-cell EH anchor at 3.5%)
040  continuum limit: complete regular families converge to EH at
     quadratic rate (2D exact; 3D three-family; 4D two-family;
     general case a declared CMS84/FFLR84 import)
041  relaxation lab phase 1 (measured floor, minimum, signature,
     defects)
042  Schläfli conservation; Hartle–Sorkin boundary additivity
043  4D/Lorentzian lift (contract 9/9; Wick term-by-term; gauge
     zero modes; Roček–Williams import)
044  adoption record (fence, falsifiers, honest epistemic status)
046  the evenness/dispersion theorem (A5 resolved; margin ~6e8)
047/048  scalaron: cancellation refuted, scoping ruling (route i)
049  quadratic selector: Finsler unstorable (metric-vs-Finsler
     audit closed — the edge-length ontology stores exactly a metric)
050  4D forced mixture (the "flatness is bought" theorem)
051  bulk lab phase 2 (intensivity; 4D coordination statistics;
     spectrum; disclination networks)
052  edge density c_e derived; conversion factor down to one constant
053  boundary-channel kill (the operator instantiated; excluded by
     54-114 orders; matter is strain content, not walls)
```

## What makes it publishable

- The expansion-point theorem is, to our knowledge, a new answer to
  "why EH?": not from symmetry, not from thermodynamics, but from
  the ground state being *pre-tensioned*. One sentence, checkable in
  an afternoon, and it reframes R² gravity as the signature of an
  UNfrustrated vacuum.
- The evenness theorem is a standalone-quality result (real,
  finite-range, harmonic ⟹ no linear dispersion on ANY graph): it
  answers the standard "discreteness ⟹ Lorentz violation" objection
  at the level of the whole model class. (Option: spin it off as a
  short PRD note if the main paper runs long.)
- The forced-mixture results give the model parameter-free structural
  numbers (5.1043, 4.7668, 9.9743, 0.2332...) — rare for an emergent
  -gravity proposal, and they make the model falsifiable from inside.
- The kill record (Finsler unstorable; boundary channel dead;
  partial-relief dead) demonstrates the model closes doors rather
  than opening escape hatches.

## What's missing / to do

- The general (irregular-triangulation) continuum limit rests on the
  CMS84/FFLR84 import; the paper must state precisely what is proven
  in-house (complete regular families, all dimensions computed) vs
  imported (the Fierz–Pauli-class citations).
- Positioning vs CDT and causal sets: this model is kinematic-first
  (ground state and response derived; Lorentzian initial-value
  dynamics open — O-P10-4 must be stated as the frontier, not
  glossed).
- The mean-field fence on the mixtures (phase-3 lab pending) must be
  a limitation section, not a footnote.
- Figures: the lab plots (E(n) curves, coordination histograms,
  disclination networks) practically draw themselves; the 600-cell
  anchor deserves a diagram.

## Kill risks / honesty notes

- A referee will ask "where is matter?" — the honest answer is the
  matter-as-defect charter (gated, not licensed) and the defect
  spectrum as a suggestive exhibit only.
- The packing scale a is underived; Planck-scale a is an assumption
  and the paper says so (with the two-face discreteness consistency
  battery as the in-principle test).
- Confirmed linear LIV kills the model outright (register A5) —
  state it.

## One-line pitch

Regular tetrahedra don't tile space; the vacuum therefore sits
pre-tensioned at a frustrated minimum; expanding any smooth energy
about that point yields Einstein–Hilbert as the generic leading
response — gravity is the linear elasticity of a vacuum that cannot
relax.
