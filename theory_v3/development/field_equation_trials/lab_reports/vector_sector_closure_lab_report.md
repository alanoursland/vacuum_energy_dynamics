# Lab Report: Vector Sector Closure -- Frame Dragging Derived, No Structural Sectors Remain

## Experiment

**Script:** `vacuum_forge/src/field_equation_trials/012_vector_sector/vector_sector_closure.py`
**Experiment type:** Coefficient closure (armchair, stationary linear order)
**Status:** SECTOR CLOSED -- the FEC "normalization missing" blocker discharged
**Run date:** 2026-06-12
**Dependencies verified:** 008 static normalization anchor; E3 parent closure.

## Purpose

The FEC program left the vector/current sector structural:
$\nabla\times(\nabla\times W)=-(\alpha_W/2K_c)\,j_T$ with the
normalization explicitly listed as missing (seam map, groups ~010--017).
With the parent closed and its normalization derived, no freedom can
remain. Close the sector.

## Results

**T1.** Linearized stationary metric with $g_{ti}=w_i$ in divergence-free
(stream) gauge, machinery-verified: $G_{ti}^{(1)}=-\tfrac12\Delta w_i$.

**T2.** Closed parent ($N=c^4/8\pi G$, from 008) with slow dust
($T_{ti}=-\rho c^2 v_i$):
$$\Delta w_i = \frac{16\pi G}{c^2}\,\rho v_i$$
-- the FEC equation in stream form (curl curl = $-\Delta$ on
divergence-free fields), its missing normalization **derived**.

**T3.** Moment identity $\int\rho\,v_i x_j = -\tfrac12\epsilon_{ijk}S_k$
verified exactly on a rigid rotating ring; Green-function far field:
$$w_i = -\frac{2G}{c^2}\,\frac{(\mathbf S\times\mathbf r)_i}{r^3}$$
-- Lense-Thirring with GR's coefficient, the dipole harmonic verified to
solve the vacuum equation. Every constant in the chain traces to the
trials' own static sector.

**T4 (anchor, inherited kill condition).** Gravity Probe B measured
frame dragging consistent with GR (~19%); LAGEOS/LARES to a few percent
(magnitudes FROM_MEMORY, flagged; the pass requires only consistency
with GR). Since the derived sector IS GR's linearized gravitomagnetism
with zero free constants, disagreement would have falsified the parent.
It doesn't.

## Verdict

```text
Vector sector: STRUCTURAL -> DERIVED. The FEC alpha_W/K_c blocker is
discharged. Every sector of the reduced theory is now derived:
  static (C2/C3) - radiative (008) - trace (F1) - boundary (E1-E3)
  - vector (012).
NO STRUCTURAL SECTORS REMAIN.
```

## Relation to the program

This closes the last "structural" line in the status of record. The
reduced theory is finished as a derivation program: all sectors derived,
zero matched coefficients, boundary and cosmological corrections
theorem-graded. Remaining physics lives entirely in the non-EH budget
(Lambda's origin, dark-sector EoS, B2 measure identity, interior cap)
plus the covariant lifts.

## Next steps

1. Trial D2 / Trial B2 -- the non-EH frontier.
2. Covariant lifts (now spanning static, radiative, vector theorems).
