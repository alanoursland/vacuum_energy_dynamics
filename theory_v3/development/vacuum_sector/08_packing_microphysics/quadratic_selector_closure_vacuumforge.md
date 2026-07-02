# The Quadratic Selector Closure (Metric vs Finsler) -- VacuumForge Record

## Status

```text
result type:   selector-closure theorem (2026-07-02, derivation 049)
conclusion:    under P10 the quadratic interval-response gate is DERIVED,
               not imported: flat cells are exactly quadratic, and the
               edge-length ontology has no storage for Finsler data.
               The metric-vs-Finsler audit is CLOSED.
closes:        the two root rows of the GR-branch capstone's imported-
               assumption table ("exact quadratic response", "epsilon = 0"
               for interval response) --
               development/projection_origin_probe/34_gr_branch_closure_capstone/
non-conclusion: the OTHER capstone imports (matter action, shared interval
               ownership, second-order locality, quantum structure, ...)
               are untouched and remain on their own ledger.
verification:  vacuum_forge/src/vacuum_sector/049_quadratic_selector_closure/
```

## The Question

The projection-origin probe established that IF interval response is
exactly quadratic, polarization produces a pseudo-Riemannian metric and
the GR branch follows; if not, the structure is Finsler-class and must
be routed as explicit extra structure (`K_strain = K_metric + eps
K_Finsler`). The probe built gates and witnesses -- notably the
parallelogram gate and the quartic obstruction witness with residual
`12 eps` -- but the selector itself was an import: nothing in the
pre-P10 ontology said WHY response is quadratic.

## The Theorem (four verified parts)

```text
1. FLAT IS QUADRATIC. For a generic symmetric form G (n = 4, any
   signature), the cell response Q(v) = v.G.v satisfies the
   parallelogram identity IDENTICALLY, polarization returns an exactly
   bilinear object, and the fundamental tensor (1/2)Hess(Q) = G is
   direction-independent. P10's flatness clause is the quadratic gate.

2. THE ONTOLOGY CANNOT STORE FINSLER DATA. Per n-cell the packing
   stores C(n+1,2) edge lengths; a quadratic form in a vertex frame
   has n(n+1)/2 = C(n+1,2) components -- EXACT match, every n. The
   smallest Finsler deformation class (quartic) needs C(n+3,4)
   coefficients: 35 in 4D against 10 edges. Deficit 25: Finsler
   structure is not suppressed, it is UNSTORABLE.

3. EDGE DATA IS METRIC DATA, BIJECTIVELY. The law-of-cosines
   inversion G_ij = (l_0i^2 + l_0j^2 - l_ij^2)/2 reconstructs the
   full generic form from the edge lengths exactly (verified
   symbolically). The stored numbers ARE the metric.

4. THE WITNESS IS OUTSIDE THE STATE SPACE. The probe's own quartic
   witness reproduces (parallelogram residual 12 eps at u=v=(1,0));
   its fundamental tensor is direction-dependent (g_11 differs by
   4 eps between axes), so it has no Gram matrix -- and by (2)+(3)
   no P10 cell can hold it, even perturbatively.
```

## Where Direction Dependence Actually Lives

The packing is not globally quadratic -- and that is the point. The
only place the axiom can express direction dependence is ACROSS cells,
at hinges, as deficit angle. Deficit is curvature: the very thing the
theory is about. What P10 forbids is direction dependence WITHIN the
interval response -- a hidden norm -- and it forbids it structurally.
The old routing rule ("nonquadratic response must be routed explicitly
as Finsler/medium/constitutive structure") is now a theorem of the
form: under P10 there is nothing to route; the epsilon branch of
`K_metric + eps K_Finsler` has an empty state space.

## Ledger

```text
derivation:  quadratic_selector_closure_049
satisfies:   quadratic_gate_import_closed_049 (capstone rows 1-2)
depends on:  regge_delaunay_bridge_039, p10_adoption_record_044
kill face:   any demonstration that the packing's effective long-
             wavelength interval response develops a direction-
             dependent norm (e.g. from anisotropic ground order)
             would reopen the audit -- flagged as the watch item:
             the ground state's isotropy is O-P10-2/O-P10-5 territory.
```
