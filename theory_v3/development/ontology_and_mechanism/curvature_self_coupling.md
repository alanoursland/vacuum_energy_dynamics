# Curvature Self-Coupling and the Bootstrap Selector

## What This Document Is

This document is a development note. It records the resolution of the
question "does curvature energy itself gravitate?", its observational and
internal status, and the strategic consequence: self-coupling consistency
is a candidate selector for K_GR (the K_strain question).

Tiny goblin version:

```text
The bend costs treasure, and the treasure bends a little more.
The ledger converges -- until the vault door, where the rules change.
```

---

## 1. The Three Branches

```text
B1: curvature energy does not gravitate (no self-coupling; linear theory)
B2: curvature energy gravitates; the series converges to finite values,
    with breakdown only at horizon scales
B3: curvature energy gravitates; the series runs away
```

## 2. Branch Verdicts

**B1 is dead twice over.**

Observationally: the Nordtvedt test. Earth's gravitational self-energy is
~4.6e-10 of its mass; if self-energy did not gravitate, Earth and Moon
would fall differently toward the Sun, polarizing the lunar orbit. Lunar
laser ranging bounds the Nordtvedt parameter near zero: gravitational
self-energy both falls and sources gravity normally. (Strong equivalence
principle, gravitational sector.)

Internally: P8 IS the self-coupling commitment. "Temporal distortion is
part of the vacuum configuration and acts on already-distorted rates" is
self-coupling stated ontologically; it is where beta = 1 comes from (T4),
and perihelion precession (T9, gate G22) tests it. A no-self-coupling
variant of the framework predicts the wrong precession.

**B2 is the observed structure, and the convergence is exact.**

The self-coupling series converges outside the horizon; the exact exterior
A = 1 - r_s/r is the resummed sum. (This is why the exact mechanics branch
found that the naive exponential A = exp(-r_s/r) is wrong at second order:
the difference is precisely the self-coupling resummation.) Convergence
holds for r > r_s; the horizon is where the bookkeeping changes; the
interior is where GR runs to a singularity and where the J_curv
finite-admissibility principle proposes a cap instead. The framework's
distinctive strong-field content, if any, lives inside the horizon.

**B3 does not occur for ordinary exteriors** (weak-field self-coupling is
suppressed by Phi/c^2 per order) and is excluded at convergence radius by
the same resummation.

## 3. The Bootstrap Selector (strategic consequence)

Taking B2 seriously to all orders is one of the classical derivations of
GR: the Gupta-Kraichnan-Feynman-Deser bootstrap. A free spin-2 field
required to couple consistently to its own stress-energy generates the
full Einstein-Hilbert structure uniquely (under the usual locality and
derivative-order assumptions).

Consequence for the K_strain frontier
(`projection_origin_probe/research_synthesis/07_missing_strain_functional.md`):

```text
CANDIDATE SELECTOR: self-coupling consistency.
If the vacuum ontology requires configuration energy to gravitate
(P4 + P6 + Nordtvedt), and requires the coupling to be self-consistent
to all orders, the bootstrap result suggests K_strain's leading term is
forced to be EH-like -- i.e. epsilon = 0 at leading order, with any
residual confined to structures the bootstrap does not fix (boundary
terms, finite-admissibility caps inside horizons, non-geometric
sectors).
```

This selector should be registered against the strain-branch programs as a
testable route: formalize "configuration energy enters its own source
ledger consistently" in reduced variables and check whether it reproduces
P7/P8 (it should: P8 is its first-order shadow) and whether it forces the
exact exterior resummation A = 1 - r_s/r from the reduced A-action.

## 4. The Count-Once Placement Question

In GR, gravitational energy is NOT in T_munu; it lives in the nonlinearity
of the geometric side. Placing E_config naively on the source side
double-counts or breaks Bianchi compatibility -- which is exactly the
H_curv divergence-safety obstruction found by field_equation_candidates
groups 17/19, and the cosmological-scale face of the count-once rule.

Design rule for any trial functional:

```text
configuration/frustration energy is counted exactly once:
either inside the nonlinear geometry (GR-style) or as an explicit
source with a derived, divergence-safe compensation -- never both.
```

## 5. Consequence for Trial D

The standing-frustration excess MUST gravitate (dark matter is detected
only gravitationally), and may do so safely: at halo densities
Phi/c^2 ~ 1e-6, so its self-coupling correction is one part in a million
and the series converges trivially. Trial D inherits the count-once
placement obligation above.

## 6. What Is Not Established

```text
A reduced-variable formalization of the bootstrap selector.
That the bootstrap assumptions (locality, second order, no extra
  fields) are all forced by the vacuum ontology -- they are gates
  G15-G20, currently conditional.
The interior (finite-admissibility cap vs singularity) behavior.
```
