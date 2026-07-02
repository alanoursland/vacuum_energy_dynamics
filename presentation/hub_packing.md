# What does the vacuum actually look like, and did anyone check?

The discrete-gravity trail: the packing model, the ground state pinned to numbers, the lab that measured it, and the self-threats it survived.

## The trail

This hub walks the path from "space is a frustrated tetrahedral
packing" (an axiom, P10) to "here is exactly what that axiom forces,
computed and lab-tested" (a closed campaign, derivations 046–053).
Read in order if you're new to the microstructure; jump to any stop if
you already know the frustration story.

**1. The one-input structure.** Everything below is a function of a
single geometric constant per dimension: the regular-simplex dihedral
angle, θ₃ = arccos(1/3) in 3D, θ₄ = arccos(1/4) in 4D. No coordination
number tiles flat space exactly — the deficit ladder has no zero — so
the flat frustrated ground state is forced to a specific *mixture* of
coordinations, not a free choice:

```text
ground mixture, 3D    x₆ = 2π/θ₃ − 5   = 10.43% n=6
ground mixture, 4D    x₄ = 5 − 2π/θ₄   = 23.32% n=4
edge density           36θ₃/(√2 π)     = 9.9743 / a³
```

Flatness is bought, not free: the mixed floor sits strictly between
the pure-coordination costs, because the vacuum pays for zero mean
deficit by promoting a derived fraction of hinges to the expensive
coordination. This is why a floor energy density exists at all.

**2. Measured, not asserted — the bulk lab (051).** Phase 2 of the
relaxation lab took the packing into statistical bulk (seeded,
deterministic) and checked four things against the theory: the floor
is intensive (stable across ×4 system size, as a bulk energy density
must be); real 4D Delaunay complexes sit near the predicted mean hinge
coordination (4.98 measured, 4.86 under regularization, vs. 4.7668
predicted); the defect spectrum is positive and quantized by
coordination; and wrong-coordination edges form a single spanning
network through the bulk — line defects, not scattered dust. Phase 3
(exact mixture realizability in energy-relaxed periodic packings) is
still open.

**3. The self-threats, survived.** Two computations could have killed
the axiom outright. Dispersion (046): a naive lattice usually leaks
linear Lorentz violation, already excluded past the Planck scale — but
an evenness theorem (real reality of the strain action forces
D(−k) = D(k)\*) kills the linear term for *any* graph in the whole P10
class, no lattice symmetry required; the leading correction is
quadratic and ~9 orders below current bounds. The scalaron (047/048):
hoped that the unimodular constraint would cancel the packing's
R²-term, but that cancellation was refuted in-house — the same Bianchi
mechanism that makes Λ an integration constant reconstructs the
scalaron. The tension was closed by scoping instead: P7′ is exact in
the double idealization H→0, a→0.

**4. The doors closed.** The quadratic selector (049): the edge-length
ontology stores exactly a metric per cell (n(n+1)/2 components, every
dimension) — a quartic Finsler norm needs more slots than exist, so
Finsler structure isn't suppressed, it's unstorable. The boundary
channel (053): the long-hoped-for mechanism to confine the vacuum
behind matter walls and release the floor got its operator, and the
operator killed the idea — the same floor-Newton lock that fixes G
fixes the released pressure at ~10¹¹² Pa, excluded 54–114 orders of
magnitude by bench-top bounds.

**5. The number itself.** With the mixture, edge density, and lock all
fixed, the floor density reduces to one open constant (the packing
scale a):

```text
u_floor = c⁴ c_e ⟨δ²⟩ / (32π G Δ₀ a²) ≈ 5×10¹¹² J/m³   at a = ℓ_P (assumed)
```

the cosmological-constant problem's ~122-orders number, now derived
from microphysics rather than estimated from field modes — and shown
incapable of gravitating, partially relaxing, or leaking through a
boundary.

**Proof:** derivations 046–053 → [../theory_v3/05_vacuum_sector/06_the_ground_state_by_the_numbers.md](../theory_v3/05_vacuum_sector/06_the_ground_state_by_the_numbers.md)

**Where next:**
- [The hook trail →](hub_why_eh.md) — start earlier, at why the deficit angle forces an expansion-point theorem in the first place.
- [The cosmological-constant trail →](hub_lambda.md) — what happens to this floor once gravity and sequestering enter.
- [The assumption ledger →](hub_postulates.md) — see P10 itself, its fence, and the two microphysics constants it still owes.
- [The skeptic's entrance →](hub_graveyard.md) — the boundary-channel death certificate and the other self-inflicted kills, told from the graveyard side.
