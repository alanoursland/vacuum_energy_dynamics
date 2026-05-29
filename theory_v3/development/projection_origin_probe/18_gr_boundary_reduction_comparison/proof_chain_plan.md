# GR Boundary Reduction Comparison — proof chain plan

## Purpose

This folder tests the question raised after the boundary-reduction audit:

```text
Are the starting projection/admissibility boundary conditions different from
what weak-field GR reduces to, or are they the same boundary ledger written in
projection variables?
```

The folder is deliberately modest. It does **not** derive GR from the scalar
projection hierarchy. It compares the weak-field scalar/ Newtonian reduction of
GR against the compactified moment/admissibility structure that produced

```text
r_k = (2k - 1)/(2k + 3).
```

The intended conclusion is conditional:

```text
Under the same radial scalar reduction, compactification, and moment-pairing
normalization, the GR/Newtonian weak-field boundary ledger lies in the same
boundary/admissibility universality class as the projection-origin r_k ladder.
Therefore r_k is not a novel boundary condition by itself. The vacuum ontology,
if it does work, does it upstream by explaining why this GR-like reduction is
the relevant scalar shadow of the deeper interval/metric structure.
```

## Strategy

The proof chain separates four issues that can otherwise be conflated:

1. **Weak-field GR scalar reduction.**  In the Newtonian limit, the metric
   trace/scalar sector reduces to a Poisson equation with Gauss flux.
2. **Boundary ledger.**  The exterior solution and conserved flux are standard
   boundary data; they are not special to the vacuum ontology.
3. **Projection normalization.**  The projection ratio is recovered from a
   compactified beta-moment functional.  Under the same compactified variable
   and test space, the same moment-kernel coefficient appears.
4. **Ontology work.**  Matching the GR boundary ledger does not mean the vacuum
   ontology is idle.  It only means the ontology is not doing distinctive work
   inside the already-reduced scalar boundary algebra.  Its possible work is
   upstream: selecting quadratic metric response, calibration-coherent transport,
   EH/GHY variation, and the scalar weak-field reduction itself.

## Proof batches

### Batch A: GR/Newtonian scalar ledger

Scripts 1–5 check the normalized weak-field Poisson law, radial Gauss flux,
exterior harmonic solution, boundary energy cross term, and finite-flux
asymptotic class.

### Batch B: Compactified projection ledger

Scripts 6–11 check the compactified beta-moment functional, the base `r_k`,
the generalized endpoint-contact ladder, the primitive identity, endpoint
contact order, and flux-silence/contact distinction.

### Batch C: Comparison gates

Scripts 12–18 compare the two ledgers under variable normalization. They verify
which structures are invariant under the comparison and which are convention-
dependent: raw displayed weights may change under variable choice, but moment
ratios and contact kernels are the invariant comparison target.

### Batch D: Interpretation and status

Scripts 19–24 record the conditional interpretation: identical boundary ledger
means same reduced universality class, not absence of upstream ontology work;
differences would appear as different contact class, different admissibility
functional, or different bulk/tensor sector.
