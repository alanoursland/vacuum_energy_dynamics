# Why does the frustrated packing have a floor energy at all?

Every other node in this wiki inherits a positive floor density from one fact: a flat ground state costs the packing something, and that cost is computable, not assumed.

## The idea

A coordination-n hinge in the packing carries a deficit angle delta(n) = 2*pi - n*theta, where theta is the regular-simplex dihedral angle for the dimension in question. No integer n makes delta(n) exactly zero — the deficit ladder has no rung at flat. So a packing built entirely from one coordination number is never flat: it's either positively or negatively curved, hinge by hinge.

The 4D case (triangle hinges, theta = arccos(1/4)) makes the mechanism explicit:

```text
delta(n) = 2*pi - n*arccos(1/4):
    n = 3:  +133.44 deg      n = 5:   -17.61 deg
    n = 4:   +57.91 deg      n = 6:   -93.13 deg
```

n = 5 is the softest wedge — smallest |delta|, confirmed by direct relaxation (BFGS on n regular 4-simplices sharing a fixed hinge: n=5 gives the strict energy minimum, 0.004778, against 0.047293 at n=4 and 0.197289 at n=3). If the packing simply picked the cheapest coordination everywhere, it would go pure n=5 — but every hinge in that packing carries negative deficit. By the Regge encoding, that configuration is negatively curved, not flat. A single winning coordination and a flat ground state are mutually exclusive.

Flatness therefore has to be *bought*: the ground state mixes coordinations so the deficits cancel on average, zero mean deficit pinning the mixture exactly —

```text
x_4 * delta(4) + x_5 * delta(5) = 0
```

with x_4 + x_5 = 1. Solved: x_4 = 5 - 2*pi/arccos(1/4) = 0.233208, x_5 = 2*pi/arccos(1/4) - 4 = 0.766792 (equivalently mean coordination n_bar = 2*pi/arccos(1/4) = 4.766792). About 23% of hinges are forced into the *expensive* n=4 wedge purely to cancel the cheap n=5 wedges' curvature.

That mixture has a strictly positive residual energy — it sits between the pure-n=4 and pure-n=5 costs, not at either extreme:

```text
E/hinge = x_4*delta_4^2 + x_5*delta_5^2 = 0.310691 rad^2
```

This is the punchline the campaign keeps citing under the name "flatness is bought": the frustration floor isn't a leftover or an approximation error, it is the literal price tag of zero curvature, and both the price and the exact mixture that pays it are functions of arccos(1/4) alone — no free parameters. The same shape holds in 3D with edge hinges and theta = arccos(1/3) (n=6 plays the role n=4 does here). This is the mean-field version — it treats deficits as independently assignable per hinge; whether real periodic 4D triangulations actually realize this exact fraction is the open face (mixture_realizability_050), and the bulk relaxation lab already measures real complexes landing close (mean coordination ~4.98, vs. 4.7668 predicted).

**Proof:** derivation 050 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md)

**Where next:**
- [The Frustration →](idea_frustration.md) — the more basic fact this builds on: why regular tetrahedra can't tile space in the first place.
- [The Floor →](idea_floor.md) — what this bought energy becomes once you call it the vacuum's substance density.
- [The Deficit Angle →](idea_deficit_angle.md) — the Regge machinery (hinge deficits as curvature) that makes "negative deficit means negatively curved" precise.
- [The microstructure trail →](hub_packing.md) — the full campaign this result sits inside, mixture through bulk lab through the number itself.
