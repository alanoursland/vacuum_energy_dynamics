# Regular-Mesh Benchmark: Maxwell on the 600-Cell Quotient

## Status

```text
result type:   exploratory scratch calculation (Astra session,
               2026-11-23) + exact smooth benchmark; NOT yet
               forge-verified
scripts:       scratch_2026-11-23/cell_check.py (stdout:
               cell_output.txt)
reproduction:  owed as derivation 056
               (maxwell_regular_mesh_reproduction_056)
rerun:         2026-11-23, independent rerun on commit d0c4c23
               (NumPy 2.5.3, SciPy 1.18.1): stdout byte-identical
               to cell_output.txt
result:        icosahedral symmetry protects the threefold mode pattern
               on the regular reference mesh; the discrete metric
               fixes its frequency, omega R / c = 2.10292445 vs the
               smooth 2
```

## 1. One Group, Two Roles

The 120 unit quaternions that form the binary icosahedral group I\*
are exactly the vertices of the unit 600-cell.

- **VED** uses the 600-cell as a curved reference geometry: 600 flat
  regular tetrahedra with straight chord edges of length 1/φ, 720
  edges, five tetrahedra around every edge. The chord tetrahedra
  realize the preferred (regular) arrangement, and every hinge carries
  its deficit δ_h = Δ₀ as intrinsic piecewise-flat curvature. 039,
  result 3, gives

  $$\sum_e \ell_e\delta_e = \frac{720\,\Delta_0}{\varphi}
  \simeq 0.9648\,\Big(\tfrac12\int_{S^3}\mathrm{Scal}\,dV\Big)$$

  at unit radius. The smooth round sphere is the comparison geometry.
  The two metrics differ, which is why the 3.5% gap is meaningful.
  See [../08_packing_microphysics/regge_delaunay_model.md](../08_packing_microphysics/regge_delaunay_model.md).
- **The manuscript** uses I\* as a symmetry group acting on S³. Its
  quotient is the Poincaré homology sphere, on which it constructs a
  Maxwell field.

## 2. The Smooth Field

Treat S³_R as the quaternions of norm R, and let I\* act on the left,
q ↦ hq. The manuscript writes S³_R/I\*; with the action explicit, the
quotient is I\*\\S³_R.

**Fields that descend.** The left-invariant frame fields
X_a(q) = q e_a / R, for e_a = i, j, k, satisfy X_a(hq) = h X_a(q), so
they are well defined on the quotient. The opposite-handed
right-invariant triplet e_a q, which sits at the same frequency on S³,
does not descend, because h e_a q ≠ e_a h q. Higher I\*-invariant modes
also survive the quotient.

**Curl eigenfields.** The X_a are divergence-free, and with the
manuscript's orientation curl X_a = −2X_a/R.

**The field.**

$$\mathbf E = A\,(X_1\cos\omega t + X_2\sin\omega t),\qquad
c\mathbf B = A\,(X_1\sin\omega t - X_2\cos\omega t).$$

- Ampère: ∂E/∂t = −ω·cB must equal c·curl(cB) = −(2c/R)·cB.
- Faraday: ∂(cB)/∂t = ωE must equal −c·curl E = (2c/R)·E.
- Both give **ω = 2c/R**, an exact target: ωR/c = 2.

**Character of the field.** It is circularly polarized, with
|E| = |cB| and E ⟂ B. Its energy density is uniform, because the frames
are orthonormal. At t = 0, E = AX₁ and cB = −AX₂, so
E × B = −(A²/c)X₃: the energy flows along **−X₃**.

**Lowest positive frequency.** H¹ = 0 for the Poincaré sphere, which
rules out harmonic one-forms, the zero-frequency modes. That 2c/R is
the lowest positive frequency follows from the round-sphere curl
spectrum on coexact one-forms, |λ| = (k+2)/R for k ≥ 0, together with
the fact that every quotient mode lifts to an I\*-invariant mode on the
cover.

## 3. Why the 600-Cell Carries the Field

Left multiplication by I\* is an isometry of S³ that maps the 600-cell
onto itself. It permutes vertices, edges, faces and cells. The 600-cell
therefore descends to a **one-vertex quotient triangulation with face
identifications**:

```text
upstairs:  120 vertices, 720 edges, 1200 triangles, 600 tetrahedra
quotient:    1 vertex,     6 edges,   10 triangles,   5 tetrahedra
Euler characteristic 1 - 6 + 10 - 5 = 0 (closed 3-manifold)
```

**Sampling.** Take the edge q_i → q_j. Its geodesic is
q_i·exp(θn), with n the unit imaginary direction of q̄_i q_j. The
tangent's left-frame components equal n and are constant along the
geodesic. So the integrals of the three dual frame one-forms along the
edge are a common factor times

$$\operatorname{Im}(\bar q_i q_j) = \sin\theta\; n .$$

- Every regular edge has the same angular length θ, so the factor is
  common to all edges.
- Simultaneous left multiplication (q_i, q_j) → (hq_i, hq_j) leaves
  q̄_i q_j unchanged.
- So Im(q̄_i q_j) is both the field sample and the label of the edge
  class.

**Edge classes.** The twelve neighbors of 1 come in inverse pairs
g, g⁻¹. Their imaginary parts are negatives of each other; the
quaternions themselves are not antipodes. The six pairs lie along the
six fivefold axes and give the six quotient edges, each with a sign
convention for orientation.

## 4. The Discrete Calculation

```text
unknowns   E: 1-cochain on the 6 edge classes
           B: 2-cochain on the 10 face classes
equation   d1^T *2 d1 e = (omega/c)^2 *1 e
weights    circumcentric *1, *2 from the flat chord tetrahedra
           (edge 1/phi), circumradius R = 1
```

**No zero modes.** With one vertex, d₀ = 0. With H¹ = 0, ker d₁ = 0.
So this six-dimensional electric edge problem has no exact-gradient and
no harmonic zero modes, and its spectrum is strictly positive. This is
a statement about this edge problem, not a broader claim about
electromagnetic potentials.

**Result** (scratch, `cell_output.txt`):

```text
B^T B / 120 eigenvalues:   0.52786405 x3,  9.47213595 x3
frame samples D:           exact eigenvectors of the low block
                           (residual 1.9e-16)
omega R / c:               2.10292445 x3   (smooth target: 2)
                           8.90813092 x3
1% stretch of one class:   2.08334853 x2, 2.13210754
                           8.8915233 x2,  8.89990167
```

The stretch control lowers the mean of the low triplet by about 0.16%.
That matches one sixth of the edges lengthening by 1%, so the solver
responds to anisotropic geometry in the expected way.

**Why the triplets.** Right multiplication commutes with the left
action, so it acts on the quotient, and right multiplication by I\* maps
the 600-cell to itself. It rotates Im(q̄_i q_j), so it acts on the six
oriented edge classes by signed permutations. The central elements ±1
act identically, so the action factors through the icosahedral group
A₅. Across A₅'s five conjugacy classes (identity, the 15 involutions,
the 20 three-cycles, and the two classes of 12 five-cycles) the
character is

```text
chi_edges = (6, -2, 0, 1, 1)
chi_3     = (3, -1, 0, phi, 1 - phi)
chi_3'    = (3, -1, 0, 1 - phi, phi)
chi_3 + chi_3' = (6, -2, 0, 1, 1)
```

The regular-mesh Maxwell operator commutes with this action, so each
irreducible triplet has a single eigenvalue.

- **Symmetry explains** that there are two triplets and that the
  sampled frame patterns, which transform as one 3-dimensional
  representation, span an eigenspace.
- **The calculation establishes** which triplet is lower, and how close
  its frequency is to 2c/R.

The second triplet at 8.908 is reported without interpretation. With
six degrees of freedom it is most likely a mesh-scale mode.

## 5. What the Benchmark Does and Does Not Do

It does:

- give an exactly known smooth Maxwell mode on a triangulation VED
  already uses;
- validate a discrete Maxwell solver against a known answer before it
  is applied to strained or relaxed configurations;
- identify what to watch in the strained work: whether the degeneracy
  survives, whether the frequency shifts, and which changes persist
  after averaging.

It does not:

- claim that spatial quanta produce electromagnetism;
- test helicity: the discrete operator measures ω², so the curl sign
  −2/R is a manuscript input;
- establish convergence under refinement: one mesh is a benchmark;
- bear directly on the research question. The 600-cell is the
  unstrained reference, where curvature absorbs Δ₀. The question
  concerns flat periodic packings at fixed metric, where Δ₀ is stored as
  strain.

## Implementation Notes for 056

- The quotient's edges are loops. Work upstairs on all 720 edges,
  classed by Im(q̄_i q_j), or use a cell-complex structure that allows
  loops.
- The scratch Hodge assembly uses unsigned circumcentric distances.
  That is valid for the regular mesh and small perturbations of it. It
  is not a general signed Hodge star.
- The scratch code accumulates both sides of the eigenproblem over all
  120 copies. The factor cancels in the generalized eigenvalue.
