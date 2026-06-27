# Dark-Energy Accounting

## Status

```text
result type:   accounting / interpretation; grounding partly solid, the
               floor = Lambda identification is a proposal
scope:         what VED does and does not say about dark energy, the energy
               buckets in background space, and how each behaves under expansion
conclusion:    configuration energy gravitates and bulk density is a constraint
               (grounded in the field equations); the frustration floor is the
               natural occupant of the open Lambda slot
non-conclusion: this does not derive Lambda's value; it does not address dark
               matter; it changes no closed result
```

This note consolidates a development thread on what the theory's dark-energy
content is. It is the grounding companion to
[dimensional_relaxation_channel.md](dimensional_relaxation_channel.md), which
proposes how the floor recorded here might be locally released. The unimodular
mechanics behind "Lambda is an integration constant, set by a global datum"
live in [lovelock_breaks.md](lovelock_breaks.md) and are not repeated here.

## 1. VED is a dark-energy theory, not a dark-matter theory

The framework identifies vacuum with energy and spacetime (P1, P2) and does not
attempt to say what *matter* is relative to the vacuum. Consequently it has
nothing to say about dark **matter** (the clustering, pressureless, `a^-3`
component). Everything below concerns dark **energy**: the smooth, `w = -1`,
non-diluting component.

This matters because the two behave oppositely under expansion, and conflating
them produces a false contradiction:

```text
dark matter:  w = 0,  rho ~ a^-3   (dilutes; pinned by CMB/BBN)
dark energy:  w = -1, rho = const  (does not dilute)
```

A component "created with new space at constant density" is `w = -1` dark
energy by the iron rule below; it is not dark matter.

## 2. The iron rule: constant density forces w = -1

For any component whose density stays constant as the universe expands, the
continuity equation forces

```text
rho' + 3 (a'/a)(rho + p/c^2) = 0,   rho' = 0  =>  p = -rho c^2  =>  w = -1.
```

So "energy created in step with expansion, at constant density" and "a
cosmological constant" are the **same thing**. Creating dark energy is not
exotic: a cosmological constant already *is* energy whose total grows with
volume (energy is not globally conserved in expanding GR). Observations
therefore do **not** forbid dark-energy creation — they **require** it to track
expansion closely, i.e. `w ~ -1` (measured `w = -1.0 +/- 0.03`). Departures
from exact lockstep are the evolving-dark-energy signal (the DESI handle).

## 3. The three energy buckets in background space

```text
(1) substance bulk     constant density per volume of spacetime
(2) configuration floor frustration energy of flat 3+1 vacuum
(3) GW background       stochastic gravitational-wave energy
```

| bucket | created/diluted under expansion | w | role |
|---|---|---|---|
| (1) substance bulk | created with space, constant density | -1 | a cosmological-constant-like contribution |
| (2) configuration floor | created with space (born frustrated), constant density | -1 | candidate for the *observed* Lambda |
| (3) GW background | dilutes as `a^-4`; re-pumped by mergers | +1/3 | small, possibly drives slight evolution |

Note on (2): the configuration floor does not need a separate source. New space
is born frustrated, so a single creation event supplies both the bulk substance
and its frustration configuration cost together — the configuration energy is
the unavoidable tax on creating frustrated 3D space, paid through the
substance/configuration exchange the framework already posits.

## 4. The field-equation grounding (what is solid)

Two facts are read directly from `04_field_equations/`, not proposed here.

**Configuration energy gravitates.** P9 states configuration energy gravitates
at the universal coupling, counted exactly once
(`04_field_equations/proof.md`). It is load-bearing: the static field energy

```text
u_field = - c^4 (s')^2 / (8 pi G)
```

is a configuration energy, and P9's count-once placement of it as the nonlinear
self-coupling is what selects the Schwarzschild exterior in the derivation. So
configuration energy is a genuine gravitating source, not a passive label.

**Bulk constant density is a constraint, not a source.** In the derivation, P3
(constant density) is used as a constraint — its metric shadow is `AB = 1`
(`proof.md`: "P3 (constant density) gives its metric shadow ... asymptotic
flatness sets the constant to 1"), i.e. the volume/trace condition
`kappa = (1/2) ln(AB) = 0`. The constant bulk density is **not inserted as a
curvature source** anywhere; the only sources are matter `T_ab` and the
configuration self-energy (geometry-side, P9).

The consequence: bucket (1) does not gravitate as a source (it constrains the
volume), which is the field-equation-level form of the unimodular sequestering
in `lovelock_breaks.md`. A potentially huge bulk density therefore cannot
produce a Lambda catastrophe — it never enters as a source.

## 5. The floor is the open Lambda slot (the proposal)

Two further facts set up the identification:

```text
Lambda is allowed but NOT valued by the derived equations
  (04_field_equations: "the cosmological term is allowed but not valued").

flat empty vacuum currently has ZERO field energy:
  no mass => s = 0 => u_field = - c^4 (s')^2 / 8 pi G = 0.
```

So the current theory builds in **no floor** — empty space is flat and
field-energy-free, and Lambda sits in an empty slot. A frustration floor is
therefore genuinely *new* content: a nonzero configuration energy of flat,
frustrated 3+1 vacuum. Because configuration energy gravitates (P9, section 4),
that floor **would gravitate** — it is the natural occupant of the open Lambda
slot.

```text
proposal:  observed Lambda  =  the gravitating configuration frustration floor
           (bucket 2), while the bulk (bucket 1) is the non-gravitating volume
           constraint.
```

This is consistent with the field equations and supported by P9, but it is a
**proposal**, not a derived result: the equations *permit* it and leave Lambda
open; they do not force the identification, and they do not supply the value.

## 6. Honest limits

```text
- Dark matter is out of scope; nothing here addresses it.
- "Bulk never gravitates" is not a formal theorem; bulk currently enters only
  as the P3 constraint and Lambda is left open. The floor = Lambda
  identification is the proposal.
- The value of the floor is unsolved. A nonzero flat-vacuum configuration
  energy is allowed; why it is ~ (meV)^4 is the open magnitude gate, posed
  sharply as: what is the configuration energy of flat, frustrated 3+1 vacuum?
- At the background level, "created at constant density" and "a cosmological
  constant" are observationally identical, so the creation ontology is safe but
  not yet a distinct prediction. The distinction would come from how creation
  interacts with frustration (see the relaxation-channel note) or from w != -1.
```

## 7. Forge obligations

```text
1. Verify the iron rule symbolically: rho' = 0 in the continuity equation
   forces w = -1.
2. Reconfirm from the field-equation scripts that (a) u_field enters as a
   gravitating source via P9 and (b) P3 enters only as the AB = 1 constraint,
   not as a source term.
3. Confirm flat vacuum (s = 0) has zero field energy in the reduced functional,
   so a nonzero floor is additive new content (the Lambda slot).
```

## 8. Related materials

```text
dimensional_relaxation_channel.md      how the floor recorded here might be
                                       locally released
lovelock_breaks.md                     Lambda as a unimodular integration
                                       constant; bulk sequestering
candidate_vacuum_response_shapes.md    Shape 3 (frustration / packing Lambda)
                                       and the elasticity reframing
../intuition_models/informal_continuum_graph_model.md
                                       the substance/configuration and
                                       density/amount distinctions; dimensional
                                       frustration as a baseline-energy prompt
../ontology_and_mechanism/p4_sign_fork_infall_ledger.md
                                       the configuration-energy sign fork
../../04_field_equations/01_the_field_equations.md
../../04_field_equations/proof.md      P9, u_field, the P3 = AB = 1 shadow
04_lambda_baseline/                    the Lambda selector sweep this explains
```
