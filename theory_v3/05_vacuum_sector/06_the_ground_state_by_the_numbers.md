# 06 — The Ground State, By the Numbers

**STATUS: This document records what the first post-adoption campaign
(derivations 046–053, 2026-07-01/02) established about the adopted
packing itself: its ground-state structure, its derived constants, its
survival of its own sharpest self-threats, and the two doors it closed
behind it. Everything here is forge-verified; every number below is a
function of one geometric input per dimension — arccos(1/3) in 3D,
arccos(1/4) in 4D — plus, where physical units enter, Newton's G
through the floor-Newton lock.**

## The One-Input Structure

P10 was adopted with two microphysics constants owed (O-P10-1: the
packing scale $a$ and the edge density $c_e$) and a handful of
structural questions open. The campaign's central discovery is how
little freedom the axiom actually left. The dihedral angle of the
regular simplex — $\theta_3 = \arccos\tfrac13$ in 3D,
$\theta_4 = \arccos\tfrac14$ in 4D — turns out to determine
*everything* below:

```text
quantity                          exact form              value
---------------------------------------------------------------------
frustration deficit (3D)          2π − 5θ₃                +7.356°
ground mixture, 3D                x₆ = 2π/θ₃ − 5          10.43% n=6
mean edge coordination, 3D        2π/θ₃                   5.1043
edge density                      36θ₃/(√2 π)             9.9743 / a³
conversion prefactor              c_e Δ₀/2                0.6403
ground mixture, 4D                x₄ = 5 − 2π/θ₄          23.32% n=4
mean hinge coordination, 4D       2π/θ₄                   4.7668
mixed 4D floor (quadratic)        x₄δ₄² + x₅δ₅²           0.3107 rad²
```

No constant in this table was chosen. Each was forced by the same
three-step logic, discovered at 050 and reused since:

1. no integer coordination closes flat (the deficit ladder has no
   zero);
2. the softest single coordination (n = 5, both dimensions) carries
   *negative* deficit and therefore cannot tile flat space alone;
3. the flat frustrated ground state (037/041) imposes zero mean
   deficit, which fixes the coordination **mixture** exactly.

**Flatness is bought.** The mixed floor is strictly positive and sits
strictly between the pure-coordination costs: the vacuum pays for
being flat by promoting a derived fraction of its hinges to the
expensive coordination. This is `01_substance_energy.md`'s identity in
its sharpest form — the floor is not incidental to flatness, it is
flatness's *price*.

## Measured, Not Asserted (the bulk lab, 051)

The relaxation lab's phase 2 took the packing into statistical bulk
(seeded, deterministic) and measured four claims:

```text
INTENSIVE FLOOR    relaxed energy per vertex stable across ×4 in
                   system size: the floor is a bulk energy density,
                   as ρ_v = const requires. (This measurement turns
                   out to carry the whole expansion story — see 07.)
MIXTURE WINDOW     real 4D Delaunay complexes have mean hinge
                   coordination 4.98, moving to 4.86 under
                   regularization — toward the predicted 4.7668.
DEFECT SPECTRUM    wedge-ring excess over the n=5 floor: positive,
                   quantized by coordination, monotone in |δ(n)|.
DISCLINATION NETS  wrong-coordination edges form a single spanning
                   component threading the bulk — line defects, not
                   dust. The dark-excess candidate's morphology.
```

The full realizability verdict (do energy-relaxed periodic packings
achieve the exact mixture fractions?) is phase-3 work
(`periodic_energy_relaxation_051`).

## The Self-Threats, Survived

Two computations could have killed P10 outright at adoption time.
Both were run; both resolved in the axiom's favor — one by theorem,
one by ruling.

**Dispersion (046, the A5 threat).** A naive lattice generically
produces linear-order Lorentz violation, already excluded past the
Planck scale. The evenness theorem removed the threat for the entire
P10 class: for *any* real, finite-range, harmonic action on *any*
graph, $D(-k) = D(k)^*$ forces the spectrum exactly even in $k$ — no
linear term can exist, protected by the reality of the strain energy,
no lattice symmetry required. Leading modification: quadratic,
Planck-suppressed, ~9 orders beyond current bounds. The threat
converted to a standing falsifier (register A5: confirmed linear LIV
now kills P10 outright). Watch: chiral matter discretizations evade
the theorem's hypotheses.

**The scalaron (047/048, the P7′ tension).** The packing's expansion
carries an $R^2$-class term; P7′ demands the four-derivative sector
exactly empty. The hoped-for escape — the unimodular constraint kills
the scalaron — was **refuted in-house**: the f(R) EL tensor is
identically conserved, so the same Bianchi mechanism that made Λ an
integration constant reconstructs the scalaron equation from the
unimodular system, mass $m^2 = 1/(6\alpha)$ intact. The theory-owner
ruling (048, route i) resolved the tension by scoping: **P7′ is exact
in the double idealization** $H \to 0$ *and* $a \to 0$, and "no static
flow, exactly zero" is officially a limit result. The physical vacuum
carries exactly two derived, controlled, sub-observable corrections —
the expansion κ-leak and the Planck-range scalaron
($\ell^* = \sqrt6\,\ell_P$, ~30 orders below the laboratory frontier)
— each quadratic in its small parameter. Any third correction must
arrive the same way: derivation, magnitude, kill condition.

## The Doors Closed

**The quadratic selector (049).** The oldest import at the root of
the GR branch — "interval response is exactly quadratic; no
Finsler/constitutive residual" — became a theorem: flat cells are
definitionally quadratic (parallelogram, polarization, and
fundamental-tensor identities hold identically for a generic form),
and the edge-length ontology stores *exactly* a metric per cell —
$\binom{n+1}{2}$ edges $= \tfrac{n(n+1)}2$ quadratic components, every
$n$, with no storage slot for the 35 coefficients a 4D quartic norm
would need. Finsler structure is not suppressed; it is **unstorable**.
The only direction dependence the packing can express lives at hinges,
as deficit — curvature, the theory's subject.

**The boundary channel (053).** The long-quarantined
dimensional-relaxation idea — engineer boundaries that confine the
vacuum to frustration-free 2D packing and release the floor — finally
got its owed operator, and the operator killed it. The mechanism is
real in form (a constant attractive pressure, cleanly distinct from
QFT Casimir's $d^{-4}$), but the floor-Newton lock fixes its magnitude
with no free coefficient: $\sim 10^{112}$ Pa at Planck packing,
excluded by 54–114 orders of magnitude by bench-top bounds. Matter
boundaries cannot confine the packing at any detectable coupling —
consistent with matter being strain content *of* the packing, not
walls outside it. Consequences, recorded: the engineered energy
release is closed at leading order; "gravity sequesters, boundaries
reveal" is dead (the floor hides from *both* channels); the UFFT
micron window is no longer VED-motivated.

## The Floor's Magnitude, Stated Plainly

With everything above, the floor density is locked up to the single
remaining unknown:

```text
u_floor = c⁴ c_e ⟨δ²⟩ / (32π G Δ₀ a²)  ≈  11.2 × (c⁴/32πG) / a²
        ≈  5×10¹¹² J/m³   at Planck packing (a = ℓ_P, ASSUMED)
```

This is the cosmological-constant problem's famous number — ~122
orders above the observed dark energy — now derived from the
microphysics rather than estimated from field modes. The theory's
posture toward it is a theorem stack, not an apology: the floor
cannot gravitate (sequestering), cannot partially relax into Λ (the
relief kill), and cannot be tapped by boundaries (053). It is the
substance energy of space: enormous, structural, and invisible except
as the thing whose strain is geometry.

## What Remains

```text
the packing scale a        the sole free microphysics constant
                           (o_p10_1_packing_scale_052); Planck-scale a
                           is an assumption, recorded as such
the discreteness battery   if a is EVER measured: the floor-Newton
                           lock must reproduce G AND a scalaron Yukawa
                           must appear at range √6·a — parameter-free,
                           twice overdetermined (register C4)
phase 3                    energy-relaxed periodic packings: the exact
                           mixture fractions and floor value
                           (periodic_energy_relaxation_051)
```

## Verification

```text
046  packing_dispersion            evenness theorem (A5 resolved)
047  scalaron_unimodular           cancellation refuted (honest negative)
048  p7prime_scoping_ruling        route (i) adopted; O-P10-3 closed
049  quadratic_selector_closure    metric-vs-Finsler audit closed
050  ground_coordination_4d        the forced 4D mixture
051  bulk_relaxation_phase2        intensivity, spectrum, networks
052  edge_density                  c_e derived; one unknown left
053  boundary_channel_operator     channel killed (counterexample)
```

All under `vacuum_forge/src/vacuum_sector/`; reports under
`../development/vacuum_sector/08_packing_microphysics/`.
