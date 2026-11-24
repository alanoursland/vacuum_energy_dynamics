# Free-Relaxation Diagnostics: The 051 E1 Rerun

## Status

```text
result type:   exploratory scratch diagnostics on 051 E1 (Astra
               session, 2026-11-23); NOT forge-verified
scripts:       scratch_2026-11-23/virial_check.py (stdout:
               packing_output.txt)
               scratch_2026-11-23/mode_proxy.py (stdout:
               proxy_output.txt)
reproduces:    051 E1 checkpoints E/N = 0.20241, 0.22928, 0.25048
rerun:         2026-11-23, independent rerun on commit d0c4c23
               (NumPy 2.5.3, SciPy 1.18.1, OPENBLAS_NUM_THREADS=1;
               vacuum_forge/ unchanged since dc1d7aa): stdout
               byte-identical to packing_output.txt and
               proxy_output.txt
findings:      (1) zero virial stress at positive residual energy;
               (2) an exact identity linking the edge-extension fabric
                   to the strain-energy fabric;
               (3) 44-49% of the original tetrahedra reverse
                   orientation during free relaxation;
               (4) a metric-response mode proxy, labeled as such
opens:         fence_051_e1_orientation
```

## The Setup Being Rerun

051 E1 generates seeded 3D point sets (rng 20260702, drawn in the order
N = 80, 160, 320), computes their Delaunay edges, rescales to unit mean
edge length, and relaxes vertex positions with the original edge list
held fixed:

$$E = \sum_e (\ell_e - 1)^2 ,$$

with ℓ_e in units of the preferred edge length. The box is not periodic, the boundary is free, and nothing is
retriangulated. 051's own report separates this tractable relaxation
model from the open problem of a periodic, energy-relaxed bulk packing
(`periodic_energy_relaxation_051`).

The scratch script extracts `delaunay_edges`, `relax_nd`,
`spring_energy_nd` and `spring_grad_nd` from the repo's 051 source and
runs them unchanged.

## 1. Zero Stress at Positive Energy

At any stationary point of E, an arbitrary small affine deformation
x → (I + ε)x costs nothing at first order. That gives

$$W \equiv \sum_e (\ell_e - 1)\,\ell_e\;\hat u_e\otimes\hat u_e = 0 ,$$

the full virial tensor, trace included. Pressure and deviatoric stress
both vanish, while E stays positive.

```text
N     E/N          eigenvalues of W / |edges|
80    0.2024051    1.5e-07   6.3e-07   9.0e-07
160   0.2292751   -2.0e-08   1.4e-07   4.5e-07
320   0.2504823   -3.7e-07  -9.6e-08   3.6e-07
```

These are zero at the solver tolerance (L-BFGS-B, gtol 1e-8).

## 2. The Extension-Fabric Identity

Since (ℓ − 1) = (ℓ − 1)ℓ − (ℓ − 1)², the identity is exact:

$$\sum_e (\ell_e-1)\,\hat u_e\otimes\hat u_e
= W - \sum_e (\ell_e-1)^2\,\hat u_e\otimes\hat u_e .$$

At a free stationary point W = 0, so:

- the direction-weighted average of edge extensions is minus the
  fabric of where the strain energy sits: (ℓ_e − 1)² is the energy
  stored in each spring, so a packing can balance all its forces while
  storing more energy in some directions than in others;
- its trace is −E: on average the relaxed edges are slightly short;
- it can be nonzero even though the mechanical stress vanishes, because
  it weights edges differently from the stress.

The scratch quantity Q is the traceless part of
(1/|edges|) Σ(ℓ − 1) û⊗û, so it is minus the deviatoric
strain-energy fabric per edge:

```text
N     eigenvalues of Q                            spread
80    -6.34e-04  -5.77e-04   1.21e-03            1.85e-03
160   -5.08e-04  -3.84e-04   8.93e-04            1.40e-03
320   -5.83e-04   2.08e-04   3.75e-04            9.6e-04
```

The spread falls with N across these three sizes, with one seed each.
That is consistent with finite-sample fluctuation, but three points do
not establish a scaling law.

In a periodic box at fixed cell, affine deformations are no longer
free, so W need not vanish. Comparing stress with the extension fabric
becomes a measurement there instead of an identity.

## 3. Orientation Reversal

For every tetrahedron of the initial Delaunay triangulation, keep the
same ordered vertex labels before and after relaxation and compute

$$D = \det\,[\,x_1 - x_0,\; x_2 - x_0,\; x_3 - x_0\,]$$

at both endpoints. Count tetrahedra with D_before · D_after < 0.
Reversing the vertex ordering flips both signs, so the count does not
depend on that choice.

```text
N     reversed fraction
80    43.5233%
160   48.7265%
320   47.0181%
```

This measures net endpoint reversal of an original tetrahedron. It does
not count intermediate crossings, and it does not retriangulate the
final points.

**Consequences.**

- A spring network can minimize its objective while folding its
  original mesh. The final coordinates of a free 051 relaxation cannot
  be used as an intact optical domain.
- Folding enlarges the set of configurations the relaxation can reach.
  The published E/N values are therefore expected to sit at or below
  what a non-inverting relaxation would reach from the same start.
  Local minima make this a likely bound, not a strict one.
- **`fence_051_e1_orientation`**: 051 E1's floor values were measured
  on configurations in which close to half the original tetrahedra are
  inverted. The fence belongs in 051's report the next time its script
  is touched. The report is generated by the script, so a hand edit
  would be overwritten.

## 4. The Mode Proxy

`mode_proxy.py` turns each sample's Q into edge-length scales on the
regular 600-cell quotient,

$$s_c = 1 + \hat v_c^{\mathsf T}\, Q\, \hat v_c ,$$

for each of the six edge classes c with direction v̂_c, and recomputes
the Maxwell spectrum:

```text
N     low triplet omega R / c                  splitting
reg   2.10292445  2.10292445  2.10292445       0
80    2.10045343  2.10067609  2.10765506       7.20e-03
160   2.10094444  2.10142669  2.10640834       5.46e-03
320   2.10065384  2.10373548  2.10438669       3.73e-03
```

**Label: metric-response proxy.**

- A constant tensor in left-invariant frame components is a
  homogeneous anisotropic metric on the quotient. The proxy therefore
  measures how the modes respond to a metric change of size Q, not a
  microstructure effect at fixed macroscopic metric.
- How the flat box's axes line up with the 600-cell frame is a choice;
  nothing physical fixes it.
- It produces an **example** splitting for one chosen mapping of Q onto
  the six edge classes and one orientation. It is not a bound: a bound
  would require showing that no other allowed mapping or orientation
  produces a larger splitting.
- Its value is as a sensitivity test: how much does the triplet split
  when this measured strain anisotropy is mapped onto the edge classes
  in this particular way? In the three runs examined, smaller spread in
  Q accompanied smaller splitting. Three sizes with one mapping do not
  establish a scaling law.
- It does not answer the research question, which is posed at fixed
  macroscopic metric.

## Ledger

```text
diagnostics:  free_relaxation_diagnostics (2026-11-23, scratch)
reproduces:   051 E1 E/N checkpoints (exact to printed precision)
opens:        fence_051_e1_orientation
feeds:        periodic_noninverting_spring_control (charter, stage 2)
              maxwell_packing_sweep (charter, stage 4)
```
