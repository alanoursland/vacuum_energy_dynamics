# Does the frustration floor survive contact with an actual numerical relaxation, or was it only ever a symbolic artifact?

The forge's first instrument run: deterministic spring-network relaxation, measuring — not deriving symbolically — the floor, the five-fold minimum, the sector signature, and defect excess.

## The lab

Everything about the floor up to this point (Delta_0's arithmetic, the frustration argument, the Regge expansion) was symbolic geometry — exact, but never subjected to an actual dynamical relaxation. VacuumForge phase 1 closes that gap: build spring networks (unit rest length, harmonic springs), relax them under deterministic BFGS descent from symmetric initial conditions (gradient norm < 1e-7 convergence, no randomness anywhere — archive-stable, reproducible bit-for-bit), and read off what the packing actually does when you let it settle.

Four measured results:

```text
E1. Cluster contrast, tetrahedral vs FCC.
    13-vertex icosahedral cluster (42 edges): relaxes to E = 0.021108 > 0,
    matching the exact symmetric optimum (surface/spoke ratio
    4/sqrt(10 + 2 sqrt5)) -- geometrically frustrated.
    13-vertex cuboctahedral (FCC) cluster: relaxes to E < 1e-12 -- exactly
    unfrustrated. Same relaxation machinery, same convergence criterion,
    opposite outcome. The floor is a property of tetrahedral/icosahedral
    local order specifically, not an artifact of spring networks in general.

E2. The wedge ring, n = 3..7 tetrahedra around a shared edge:
      n=3: E=0.163362   n=4: E=0.061149   n=5: E=0.000649
      n=6: E=0.052330   n=7: E=0.242762
    Minimum at n = 5, strictly positive. This is Delta_0's symbolic
    arithmetic (derivation 037) reappearing as the dynamical output of
    an independent relaxed network -- not assumed, found.

E3. Sector signature, many-body. The relaxed 5-ring's angle energy is
    dilation-invariant to machine precision (no restoring force on
    volume) and shear-stiff with quadratic response about equilibrium
    (dE(2e)/dE(e) ~= 4). Linear deficit shifts cancel by symmetry -- the
    discrete analog of sitting at a stationary point. This is the
    exact-flat / quadratic-stiff asymmetry that sequestering depends on,
    now measured at the many-body level instead of asserted term-by-term.

E4. Defect excess. n=4 and n=6 rings relax to locally stable configurations
    with strictly positive excess energy over the n=5 floor, quantized by
    coordination number. Decay to ground coordination requires a discrete
    topological move, not a smooth slide. Persistent, quantized, positive-
    excess, locally stable: the profile the dark-excess candidate object
    (coordination defects) needs to have.
```

What this run does *not* claim: no bulk thermodynamic limit, no statistics, no dynamics beyond static relaxation, and nothing here licenses dark-excess production or abundance — the P9/P10 gates are untouched. This is small deterministic clusters and rings, an instrument calibration, not a cosmology.

**Proof:** archive record `frustration_relaxation_lab_041`, forge script `vacuum_forge/src/vacuum_sector/041_frustration_relaxation_lab/frustration_relaxation_lab.py` → [../theory_v3/development/vacuum_sector/08_packing_microphysics/frustration_relaxation_lab_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/frustration_relaxation_lab_vacuumforge.md)

**Where next:**
- [Phase 2: the bulk →](lab_bulk.md) — the open obligation this run leaves behind: does the floor stay intensive and do defect networks actually form at system size?
- [Delta_0, the icon →](num_delta0.md) — the exact symbolic number E2 rediscovers as a relaxed network's dynamical minimum.
- [If dark matter is a packing defect... →](pred_defect_dark_matter.md) — where E4's measured defect excess feeds the conditional dark-matter candidate, gated on the still-open production physics.
- [The microstructure trail →](hub_packing.md) — how this measurement fits among the packing model's other results, symbolic and numerical.
