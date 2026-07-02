# What is the vacuum actually made of, structurally?

The axiom underneath everything else in this program: space is a graph of edge lengths trying to be regular tetrahedra, and failing.

## The idea

P10 states the vacuum's microphysics as a single axiomatic package, not
a metaphor. Four pieces, each doing specific work:

- **Configuration variable: an edge-length graph.** The vacuum's
  degrees of freedom are discrete — "bits of space" joined by edges
  with lengths. No background metric is assumed; the metric is *read
  off* the edge lengths, cell by cell.
- **Flat cells.** Each cell (tetrahedron) is internally flat. All
  curvature is pushed to the hinges — edges in 3D, triangles in 4D —
  where cells meet and fail to close. This is piecewise-flat geometry:
  curvature as a discrete, local, measurable closure deficit, not a
  smooth field guessed at everywhere.
- **Per-hinge energy.** The cost function is local and smooth in the
  deficit at each hinge:

```text
E[X] = sum_h  V_h f(delta_h)
```

  with $V_h$ the hinge measure and $f$ a smooth function of the
  mismatch between what the packing *wants* (regular tetrahedral
  cells) and what closure *forces*.
- **A frustrated flat ground state.** Regular tetrahedra cannot tile
  flat 3-space — five of them around an edge fall short of closing by
  exactly $\Delta_0 = 2\pi - 5\arccos(1/3)$, a fixed geometric number,
  not a free parameter. So the minimum-energy configuration (P5) is
  not "no deficit anywhere" — that configuration doesn't exist. It's
  flat, with the irreducible mismatch spread as uniform strain across
  every cell. The vacuum's ground state is a compromise it is
  geometrically forced into, not a state it chooses.

Why state this as an axiom rather than derive it: P10 doesn't add new
physics to P1–P6, it says what they were *about*. The substance energy
(P1/P3) is this strain. The curvature (P3a) is the strain's spatial
variation. The two energy ledgers (P4) are the uniform and varying
parts of one strain field. P10 is adopted late (2026-07-01), after
derivations 037–043 showed four independent lines of structure —
sector signature, unimodular constraint, substance-energy identity,
Λ-sweep negatives — all converging on this one packing picture. That's
coherence evidence, not a blind prediction, and the file says so
plainly: the postulate's forward weight has to come from consequences
not yet checked, which is why it ships with pre-registered falsifiers
(a volume-mode restoring force; the floor scale and P1's conversion
factor pulling apart; a detected Yukawa deviation) rather than open
praise.

The payoff that justifies stating it axiomatically: with a frustrated
expansion point selected, any smooth per-hinge $f$ yields — order by
order — a constant sequestered floor, then (because $f'(\Delta_0)\neq
0$ generically) the Regge/Einstein–Hilbert action as the *linear* term,
then $a^2$-suppressed corrections. An *unfrustrated* packing would give
curvature-squared gravity instead. Frustration is why gravity comes out
Einstein–Hilbert and not something else.

**Proof:** P10 → [../theory_v3/01_postulates/p10_packing_axiom.md](../theory_v3/01_postulates/p10_packing_axiom.md), model and derivations 037–043 in `development/vacuum_sector/08_packing_microphysics/`.

**Where next:**
- [The Frustration →](idea_frustration.md) — why regular tetrahedra can't tile 3-space in the first place, and what "failing to close" means geometrically.
- [The Deficit Angle →](idea_deficit_angle.md) — how the hinge closure gap encodes curvature exactly, à la Regge.
- [The Floor →](idea_floor.md) — what the ground-state strain costs, as an energy density.
- [The microstructure trail →](hub_packing.md) — the full campaign: the ground-state numbers, the bulk lab, and the self-threats this axiom survived.
