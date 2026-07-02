# Why can't the vacuum floor just be "stretching" as the universe expands?

The floor-Newton lock turns a reading choice about expansion into a testable number, and the number is off by 480x.

## The claim

Expansion could mean one of two things for a fixed packing of tetrahedral cells: either the *cells stretch* (graph fixed, edge length l grows as `l = l_0 a(t)`) or *new cells get created* (edge length l stays fixed at Planck scale, cell count N grows as `a^3`). Both readings reproduce the same a^3 volume history and the same dust-like stress-energy — the closed FRW metric sector cannot distinguish them, and no metric measurement ever will.

But the two readings have different side effects on quantities the theory has already locked elsewhere, and those side effects are decisive.

The floor-Newton lock (derivation 039) ties Newton's constant to the packing edge length: `G ~ 1/(f'(Delta_0) l)`. If expansion is stretching, l grows with the scale factor, so G must drift:

```text
Gdot/G = -H0 ~ -7.2e-11/yr        (stretch reading, forced)
|Gdot/G| < 1.5e-13/yr             (lunar laser ranging bound)
```

That's a factor of about 480 past the LLR exclusion bound — not a marginal tension, an outright kill. Stretching is falsified by data that already exists, no new experiment required.

There's a second, independent kill on top of it. The wedge energies making up the floor are measured (derivation 041, E3) to be exactly dilation-invariant. Under stretching, that means total floor energy E stays constant while volume V grows, giving pressure p = -dE/dV = 0 — a dust-like (w=0) component. But then the floor density u = E/V falls off as a^-3, which breaks intensivity and voids the sequestering mechanism (P3 protects constant density only). A w=0 component sitting at the floor density (~5x10^112 J/m^3) would gravitate at roughly 10^122 times closure. Stretching dies twice, by two unrelated arguments.

The growth reading survives both kills automatically: l stays fixed, so G is exactly constant (Gdot=0, no margin issue at all), and the floor stays intensive (u=const, measured), which forces w=-1 exactly — negative-pressure work that self-funds the creation of new cells, term by term, in the first law. One reading choice, three previously separate locks click into place together, with no new tuning.

The 480x margin is what makes this a *decision* rather than a preference: it's not that growth is prettier, it's that stretch is dead on arrival from an existing bound, twice over.

**Proof:** derivation 054 (cosmological creation face) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/cosmological_creation_face_vacuumforge.md), building on the floor-Newton lock (derivation 039), the dilation-invariance measurement (derivation 041, E3), and floor intensivity (derivation 051, E1).

**Where next:**
- [The Floor's Density →](num_floor_density.md) — the ~5x10^112 J/m^3 number that a failed sequestering would have dumped into the metric.
- [The Bulk Relaxation Lab →](lab_bulk.md) — where floor intensivity (u=const) was actually measured across a 4x size range, the fact this whole argument leans on.
- [The Predictions Trail →](hub_predictions.md) — Gdot=0 is now a hard, falsifiable pre-registered commitment (register A6); see what else is on the line.
- [README →](README.md) — front door to the wiki.
