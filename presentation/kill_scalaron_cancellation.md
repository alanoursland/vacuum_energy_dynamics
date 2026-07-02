# Did the unimodular constraint save us from our own scalaron?

We proposed a fix for a tension in our own theory, then refuted the fix ourselves, same week.

## The kill

The packing's f(R) correction is R²-class (an f'' term), which carries
a scalaron — a propagating scalar degree of freedom. P7′, as adopted,
requires the four-derivative sector to be exactly empty. That's a
tension: O-P10-3.

**The hope (ours):** the theory already leans on the unimodular
constraint to turn Λ into a free integration constant (derivation 033).
Maybe that same mechanism projects the scalaron out too — the
traceless (unimodular) field equations just never see it, and the
tension dissolves for free.

**The test:** take the f(R) Euler-Lagrange tensor for f = R + αR²,
impose no field equations, and check whether it's identically
conserved on FRW. It is. That means the divergence of the traceless
system reconstructs the missing trace equation up to one integration
constant — exactly the Bianchi-identity move that made Λ free in the
first place:

```text
f'R - 2f + 3 box f' = kappa T + const
=>  (6 alpha box - 1) R = kappa T + const
```

The scalaron propagates anyway, with m² = 1/(6α), fully intact. The
same mechanism that frees Λ *resurrects* the scalaron rather than
killing it. "Unimodular f(R)" is just "f(R) + a free Λ" — the
constraint does no additional work on the four-derivative sector.
Proposal refuted, in-house, using the theory's own tools.

**What was left standing:** the numbers were never the problem. The
packing coefficient gives scalaron range l* = √(6α) ~ a — for Planck
packing, ~4×10⁻³⁵ m against the 54-micron laboratory frontier, a
margin of ~10³⁰. Every observable face of the theory is exactly what
P7′-exact predicts; the scalaron is real in principle but ~30 orders
below any test that could see it.

**The actual resolution** (not the hoped-for one): a scoping ruling,
not a cancellation. Either (i) P7′ is exact in the a→0 continuum
idealization, with the scalaron as a controlled O(a²) correction
*within* the postulate — same shape as the already-accepted F1
expansion leak — or (ii) demand strict all-orders exactness, which is
equivalent to imposing f″(Δ₀) = 0, an unmotivated inflection
constraint on the wedge potential. Recommendation on record: route
(i), by precedent and economy. Either way, no coefficient moves, no
observable changes, and the E3/G20 kills and the null-test falsifier
are untouched.

**Proof:** derivation 047 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/scalaron_unimodular_vacuumforge.md), also recorded in [09_the_graveyard.md](09_the_graveyard.md#our-own-scalaron-cancellation-mechanism-killed-2026-07-02-derivation-047)

**Where next:**
- [The Frustration →](kill_partial_relief.md) — the other Λ-mechanism hope killed the same month, for a different reason (quadratic flatness, not a Bianchi resurrection).
- [hub_graveyard.md](hub_graveyard.md) — the full run of self-inflicted kills, for the skeptical reader.
- [hub_lambda.md](hub_lambda.md) — how the unimodular constraint's real job (freeing Λ) actually works, the mechanism this kill leans on.
- [hub_packing.md](hub_packing.md) — where the R²-class term comes from in the microstructure in the first place.
