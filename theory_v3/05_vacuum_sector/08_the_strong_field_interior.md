# 08 — The Strong-Field Interior: No Singularity, By Combinatorics

**STATUS: The cap scale is derived (derivation 055, 2026-07-03), at
mean-field level. Under P10, curvature cannot diverge: the packing has
a maximum sectional curvature set by the coordination floor, and a
collapsing interior bottoms out at a Planck-star-sized core deep
inside the horizon. Everything observable stays exactly GR; the echo
caveat of the predictions register resolves to a null. The interior
*metric* and collapse dynamics remain open.**

## The Question and Why It Stalled

General relativity ends the story of collapse at a singularity. A
substance ontology cannot: the vacuum is *something*, and something
has a maximum compression. The interior-cap lane (derivations
025–028) built the discipline for this claim — the exterior matching
lemma (interior freedom cannot leak out; everything tested stays GR)
and a contract demanding a *derived* admissibility scale — and then
stalled honestly: with no microphysics, the maximum strain κ_max was
an import, and imports are not derivations. The finite-strain probe's
verdict of record: "a derived microphysical or ontological bound
remains possible but absent."

## The Bound Was in the Coordination Number

P10 supplies the bound, and it is *combinatorial*, not an imposed
cutoff:

```text
1. THE COORDINATION FLOOR. An interior hinge of a 3D simplicial
   complex is shared by at least three cells. The deficit ladder
   delta(n) = 2π − n·arccos(⅓) is strictly decreasing, so the
   near-regular deficit is bounded above:
       delta_max = 2π − 3·arccos(⅓) = 2.590 rad (148.41°).
   Curvature concentration has a ceiling because you cannot put
   fewer than three cells around an edge.

2. THE MAXIMUM CURVATURE. With the Regge encoding (039) and the
   derived edge density (052):
       R_max = 2·c_e·delta_max / a² = 51.67 / a²
   — exact, a function of arccos(⅓) alone, joining Δ₀, the ground
   mixtures, and c_e in the one-input family.

3. THE CAP RADIUS. The Schwarzschild interior's curvature scale
   (√K = 4√3·GM/c²r³) saturates R_max at
       r_cap = 0.406 · (r_s a²)^⅓.
```

That is the **Planck-star scaling** — Rovelli and Vidotto conjectured
r ~ (r_s ℓ_P²)^⅓ from loop-quantum-cosmology bounce arguments. Here
it drops out of tetrahedral combinatorics, with the coefficient
computed. Two independent routes to the same core scaling; the
convergence is recorded, and neither route validates the other.

## Where the Cap Sits (and Why Nothing Observable Changes)

At Planck packing (the standing assumption, marked as such):

```text
1 M_sun    r_cap ≈ 3.7×10⁻²³ m    r_cap/r_s ≈ 10⁻²⁶
Sgr A*     r_cap ≈ 5.9×10⁻²¹ m    r_cap/r_s ≈ 5×10⁻³¹
```

The cap is twenty-six orders of magnitude inside a stellar-mass
horizon. The exterior matching lemma applies with vast room:
Schwarzschild/Kerr exteriors, ringdowns, and shadows are exactly GR
(register A4), and the register's long-standing caveat — "a cap
outside the horizon could in principle produce late-time echoes" —
**resolves to a null**: no echoes, at any astrophysical mass. A
confirmed echo now *falsifies* the derived placement rather than
opening a lane.

The cap meets the horizon only when r_s ~ a — at roughly **0.13
Planck masses**. That is an endpoint *marker*: where the semiclassical
picture ends, recorded without any claim about evaporation dynamics.

## The Picture in Substance Language

Collapse, read through P1/P10: matter compresses the packing; strain
(and hinge deficit) grows; at r_cap the deficit hits its combinatorial
ceiling and the vacuum simply *cannot curve further*. The "singularity"
is replaced by a core of maximally-compressed substance — the same
object the theory has carried informally since the earliest notes, now
with a derived size. Nothing inside this core is visible from outside
(the matching lemma), and nothing about it reopens any closed
coefficient.

## What Remains Open

```text
cap_junction_dynamics_055 (joint with O-P10-4):
  - the capped interior METRIC (this chapter derives a scale, not a
    solution);
  - junction/source bookkeeping at r_cap;
  - collapse dynamics (does infalling matter actually settle at
    r_cap, and on what timescale?);
  - the fence's energetics: strained cells can flatten and trade
    deficit against distortion (Cayley–Menger witness verified);
    for f″ > 0 the near-regular bound should be energetically
    enforced — stated, not proven. This is where a refutation
    would enter.
```

## Verification

```text
055  interior_cap_scale        the coordination floor, R_max, r_cap,
                               placement, endpoint, contract compliance
depends on: edge_density_052, regge_delaunay_bridge_039,
            exterior_matching_lemma_026
report:  ../development/vacuum_sector/07_interior_cap/
         interior_cap_scale_vacuumforge.md
lane:    ../development/vacuum_sector/07_interior_cap/ (the 025–028
         contract, matching lemma, and finite-strain probe)
```
