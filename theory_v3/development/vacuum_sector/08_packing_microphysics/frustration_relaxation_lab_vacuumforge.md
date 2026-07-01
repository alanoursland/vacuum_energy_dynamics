# VacuumForge: The Frustration Relaxation Lab (numerical module, phase 1)

## Purpose

The forge's first experimental instrument: deterministic numerical
relaxation of frustrated spring networks under P5 dynamics, measuring
what the packing model claims. All prior packing results were symbolic;
these are measured.

## Instrument

Spring networks (unit rest length, harmonic), deterministic symmetric
initial conditions, BFGS relaxation, convergence asserted by gradient
norm < 1e-7. No randomness anywhere: archive-stable.

## Measured Results

```text
E1. Cluster contrast. The 13-vertex icosahedral cluster (42 edges)
    relaxes to E = 0.021108 > 0 -- geometrically frustrated, in
    agreement with the exact symmetric optimum (surface/spoke ratio
    4/sqrt(10+2 sqrt 5)); the cuboctahedral (FCC-13) cluster relaxes
    to E < 1e-12 -- exactly unfrustrated. The floor is a property of
    tetrahedral/icosahedral local order, not of spring networks
    generally.

E2. The wedge ring. Rings of n tetrahedra around a shared edge:
  n = 3:  E = 0.163362
  n = 4:  E = 0.061149
  n = 5:  E = 0.000649
  n = 6:  E = 0.052330
  n = 7:  E = 0.242762
    Minimum at n = 5, strictly positive: Delta_0's arithmetic (037)
    measured as dynamical output of a relaxed network.

E3. Sector signature, many-body. The relaxed 5-ring's angle energy is
    dilation-invariant to machine precision and shear-stiff with
    QUADRATIC response about equilibrium (ratio dE(2e)/dE(e) ~ 4):
    linear deficit shifts cancel by symmetry -- the discrete analog of
    stationarity. The exact-flat vs quadratic-stiff asymmetry between
    the modes is the sector signature, measured at the many-body level.

E4. Defect excess. n = 4 and n = 6 rings are relaxed, locally stable,
    and carry strictly positive excess energy over the n = 5 floor,
    quantized by coordination number; decay to ground coordination
    requires a discrete topological move. Disclination-type defects
    have exactly the persistence-and-excess profile the dark-excess
    lane needs its gravitating excursions to have.
```

## Classification

```text
result type: numerical experiments (instrument phase 1)
scope:       small deterministic clusters and wedge rings; no bulk
             thermodynamic limit, no statistics, no dynamics beyond
             relaxation
conclusion:  the frustration floor, its local-order dependence, the
             five-fold minimum, the dilation-flat/shear-stiff
             signature, and coordination-defect excess are all
             MEASURED properties of relaxed networks
non-conclusion: nothing here licenses dark-excess production or
             abundance (gates unchanged); no continuum or bulk claims;
             the packing reading remains a candidate ontology
```

## Newly Opened Obligation

```text
bulk_relaxation_scaling_041:
  phase 2 of the instrument: periodic bulk packings -- floor density
  intensivity vs system size, defect-line (disclination network)
  formation, and the defect energy spectrum. Feeds the dark-excess
  source ledger with a candidate microphysical object.
```

## Verification

```text
vacuum_forge/src/vacuum_sector/041_frustration_relaxation_lab/frustration_relaxation_lab.py
```

Archive record: `frustration_relaxation_lab_041`.
