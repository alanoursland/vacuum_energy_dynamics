# Why doesn't the ground state just pick one coordination number?

A reader coming from [the frustration idea](idea_frustration.md): the wedge-ring relaxation
finds a single softest coordination in both 3D and 4D — but flatness will not let the ground
state use it exclusively.

## The theorem

Around any hinge (an edge in 3D, a triangle in 4D), packing n regular simplices leaves an
angle deficit delta(n) = 2*pi - n*arccos(1/(d-1)) for dimension d. Delta is positive for small
n, negative for large n — flat is a knife-edge between over- and under-filling. The relaxed
wedge-ring energy is minimized at a single "softest" n in each case (n=5 in both 3D and 4D:
smallest |delta|). But delta(5) != 0 in either dimension, so a pure n=5 packing carries a
uniform curvature sign — negatively curved by the Regge encoding, not flat.

A perfectly flat ground state therefore cannot be built from one coordination number. It has
to mix two adjacent coordinations, one over-filled (positive deficit) and one under-filled
(negative deficit), in whatever ratio drives the *mean* deficit to exactly zero. This is not
a free parameter — flatness is one equation, x_lo + x_hi = 1 is the other, and the pair pins
the mixture fractions exactly:

```text
3D (edge hinges, arccos(1/3)):  x_6 = 2*pi/arccos(1/3) - 5 = 0.104299
                                 n_bar = 2*pi/arccos(1/3) = 5.104299
4D (triangle hinges, arccos(1/4)): x_4 = 5 - 2*pi/arccos(1/4) = 0.233208
                                    x_5 = 2*pi/arccos(1/4) - 4 = 0.766792
                                    n_bar = 2*pi/arccos(1/4) = 4.766792
```

Both mean coordinations are exactly 2*pi/theta, theta = arccos(1/(d-1)) — a hinge identity
that holds regardless of which two coordinations happen to be doing the mixing. It falls out
of "zero-mean-deficit" alone, not out of any assumption about which n's compete.

The mixture has a price, and the price is computable. In 4D the mixed floor is
E/hinge = x_4*delta_4^2 + x_5*delta_5^2 = 0.310691 rad^2, strictly between the pure-n=4 and
pure-n=5 costs — about 23% of hinges pay the "expensive" n=4 rate as the toll for exact
flatness. This is the substance-energy identity in its sharpest form: the frustration floor
isn't incidental to flatness, it *is* flatness's price, and both price and mixture are pure
functions of arccos(1/(d-1)).

What this does not settle: realizability (whether an actual periodic triangulation achieves
these fractions — opened as a separate obligation), and which of the two objects — the
Euclidean-3D edge-hinge packing or the Euclidean-4D triangle-hinge packing — the Lorentzian
(3+1) vacuum actually instantiates. The mean-field fence is explicit: deficits are treated as
independently assignable, not as living on a real lattice yet.

**Proof:** derivation 050 (4D) and derivation 052 (3D, "050's logic, one dimension down") →
[../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/ground_coordination_4d_vacuumforge.md)
and [../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/edge_density_vacuumforge.md).

**Where next:**
- [The Frustration →](idea_frustration.md) — the wedge-ring relaxation that found n=5 softest before this node shows why softest alone isn't enough.
- [hub_packing.md](hub_packing.md) — the rest of the microstructure trail: edge density, packing scale, the still-open realizability question.
- [The Expansion Point →](thm_expansion_point.md) — why a frustrated (deficit != 0) ground state is what forces the leading gravitational response to be Regge/Einstein-Hilbert rather than R^2.
- [hub_graveyard.md](hub_graveyard.md) — for the skeptic asking whether "mean-field" is doing too much work here.
