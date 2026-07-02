# What exact fraction of the 4D vacuum's hinges pay the expensive price for flatness?

The number that answers it: x₄ = 5 − 2π/arccos(¼) = 0.233208 — the forced mixture the flat 4D ground state must adopt, with no free parameter.

## The number

A triangle-hinge in the 4D packing carries deficit angle δ(n) = 2π − n·arccos(¼), one value per coordination n. None of them is zero:

```text
δ(n) = 2π − n·arccos(1/4):
    n = 3:  +133.44°      n = 5:   −17.61°
    n = 4:   +57.91°      n = 6:   −93.13°
```

n = 5 is the softest wedge — smallest |δ|, and confirmed as the strict energy minimum by direct BFGS relaxation of n regular 4-simplices sharing a fixed hinge (E = 0.004778 at n=5, against 0.047293 at n=4 and 0.197289 at n=3). If the packing simply took the cheapest coordination everywhere it would go pure n=5 — but every hinge in that packing then carries negative deficit, which by the Regge encoding means negatively curved, not flat. A flat ground state and a single winning coordination are mutually exclusive, so the packing mixes n=4 and n=5 hinges in whatever ratio cancels the mean deficit exactly:

```text
x_4 * delta(4) + x_5 * delta(5) = 0,   x_4 + x_5 = 1
```

Solved in closed form:

```text
x_4 = 5 - 2*pi/arccos(1/4) = 0.233208
x_5 = 2*pi/arccos(1/4) - 4 = 0.766792
n_bar = 2*pi/arccos(1/4) = 4.766792
```

About 23.3% of hinges are forced into the pricier n=4 wedge purely to cancel the curvature the cheap n=5 wedges would otherwise leave behind. This is the exact 4D counterpart of the 3D edge-hinge mixture (x₆ = 0.1043, mean coordination 5.1043): same mechanism, different dihedral angle (arccos(¼) instead of arccos(⅓)), because 4D uses triangle hinges rather than edge hinges.

The mixture pins the floor's residual energy too — E/hinge = x₄δ₄² + x₅δ₅² = 0.310691 rad², strictly between the pure-n=4 and pure-n=5 costs, not at either extreme. Both numbers — the mixture and the price it buys — are pure functions of arccos(¼); nothing else goes into them.

Two fences on the number, stated plainly: it is mean-field (deficits treated as independently assignable per hinge, not yet checked against what an actual periodic 4D triangulation can realize — that's the open realizability face, joint with O-P10-5), and it says nothing about which of the 3D edge-hinge packing or the 4D triangle-hinge packing the Lorentzian vacuum actually instantiates — that's a separate open question. The bulk relaxation lab already lands close to the number without assuming it: measured mean coordination ≈4.98 (≈4.86 regularized) against the 4.7668 predicted here.

**Proof:** derivation 050 → [../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md)

**Where next:**
- [The 3D mixture →](num_mixture_3d.md) — the same mechanism one dimension down, with edge hinges and arccos(⅓).
- [Δ₀, the gap five tetrahedra leave →](num_delta0.md) — the more famous relative of this number, and the icon the whole frustration story hangs on.
- [Phase 2: the bulk lab →](lab_bulk.md) — where this mean-field prediction gets checked against real 4D Delaunay coordination statistics.
- [The microstructure trail →](hub_packing.md) — the full campaign this number sits inside, mixture through bulk lab through the floor density itself.
