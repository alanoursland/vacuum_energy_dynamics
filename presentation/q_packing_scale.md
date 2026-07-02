# What sets the packing scale a?

Every microphysics constant in the vacuum floor is now an exact function of one angle, `arccos(1/3)` — except one number, and nobody has a derivation for it.

## The question

The flat, frustrated ground packing (regular tetrahedra mixing coordination-5 and coordination-6 hinges) has a single length scale: the tetrahedron edge `a`. Everything else in the floor's microphysics has collapsed to pure geometry:

- the deficit gap `Delta_0` — a function of `arccos(1/3)` alone
- the 3D ground mixture fraction `x_6 = 0.104299` and mean coordination `n_bar = 5.104299` — hinge identities, also functions of `arccos(1/3)` alone
- the edge density itself:

```text
c_e = 36 arccos(1/3) / (sqrt(2) pi) = 9.974276 edges per a^3
```

- `f'(Delta_0)`, eliminated entirely by the floor-Newton lock (derivation 039), which ties it to Newton's constant `G`.

Stack all of that and the floor density reduces to:

```text
rho_v = 0.640290 f'(Delta_0) / a^3
```

One symbol left undetermined: `a`. It is the sole remaining free microphysics constant in the whole discreteness sector, and derivation 052 is explicit that there is no derivation route on the books for it. Wherever a numeric value is needed downstream (floor density, LIV bounds, scalaron range), the theory plugs in Planck-scale `a` and *says so* — this is a stated assumption, not a result.

**Why this isn't a minor gap.** The framework's register of discreteness consistency (register C4) now reads: `G`, `rho_v`, and `a` sit in a one-parameter family, every coefficient exact. That means if any independent physical probe ever pins down a discreteness scale, the system is overdetermined *twice*: the floor-Newton lock must reproduce the observed `G`, and the scalaron (048) must appear at range `sqrt(6) a`. Two parameter-free consistency checks are sitting on the books, both waiting on a measurement nobody currently knows how to make. That's the honest status — not "unmeasurable in principle," but "no known experiment reaches it yet."

**What would close this.** Nothing internal to the packing geometry fixes `a` — it's a genuine scale, not an angle, and the derivation chain from `arccos(1/3)` only ever produces dimensionless ratios. Closing it requires either (a) an independent theoretical argument for why the packing edge should sit at the Planck length specifically, or (b) an experimental handle on a discreteness signature (the scalaron range, an LIV bound, a direct graininess probe) that back-solves for `a`. Neither exists yet.

**Proof:** derivation 052 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md)

**Where next:**
- [The Microstructure Trail →](hub_packing.md) — the full one-input geometric chain that this question is the loose end of.
- [Realizability →](q_phase3_realizability.md) — whether the energy-relaxed packing even hits these predicted mixture fractions, a prerequisite question below this one.
- [The Skeptic's Entrance →](hub_graveyard.md) — where honest open questions like this one get cataloged instead of hidden.
- [Lorentzian Dynamics →](q_lorentzian_dynamics.md) — another unstarted piece of the packing's physics, same frontier.
