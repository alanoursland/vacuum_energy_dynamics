# Vacuum Action Origin: Initial Status After Proofs 1-5

## Purpose of This Folder

This folder starts the phase after `einstein_hilbert_origin_tests`.

The EH tests showed:

```text
if the standard metric/action assumptions are accepted,
then Einstein-Hilbert is the selected four-dimensional nonlinear completion
of the scalar boundary-flux and linearized metric bridge, up to Lambda and
topological terms.
```

This folder asks where those assumptions come from.

## Proof 1: Response Reciprocity to Metric Candidate

Proof `1` validates:

```text
smooth local response cost
zero self-cost
reciprocity under displacement reversal
  -> symmetric quadratic leading term.
```

That symmetric quadratic term is the metric candidate.

## Proof 2: Signature Invariance

Proof `2` validates:

```text
G' = J^T G J
det(G') = det(J)^2 det(G).
```

So metric signature is not a coordinate artifact. A relativistic theory still
needs a reason for Lorentzian signature.

## Proof 3: Local Additivity

Proof `3` validates:

```text
additive finite-cell energy
  -> zero mixed independent-cell Hessians
  -> cell-local variation.
```

Cross-cell terms are the obstruction to strict local additivity.

## Proof 4: Relabeling-Invariant Density

Proof `4` validates:

```text
coordinate relabeling
  -> action density must transform with the Jacobian
  -> derivative strain requires metric compensation.
```

This is the vacuum-action route to diffeomorphism bookkeeping.

## Proof 5: Boundary Flux as Variational Source

Proof `5` validates:

```text
E = (1/2) integral (u')^2 dx - Q_R u(R) + Q_L u(L)
```

gives a source-free bulk equation plus boundary flux conditions:

```text
u'(R)=Q_R
u'(L)=Q_L.
```

For `-u''=S`, the integrated source is:

```text
integral S dx = -u'(R)+u'(L).
```

So the source integral is a boundary-flux defect.

## Current Impact

This first batch establishes a controlled route from vacuum response
assumptions to action ingredients:

```text
reciprocal local response -> metric candidate
signature invariance -> Lorentzian signature is a physical selector
local additivity -> local energy density
relabeling invariance -> geometric action density
boundary source variation -> boundary flux defect
```

## What Is Still Open

The next proof targets are:

```text
7. derive or exclude Lorentzian signature from response stability;
8. connect local additivity with gradient strain between neighboring cells;
9. test torsion as a possible defect mode in the vacuum-action language;
10. lift the boundary-flux variational source toward the EH/GHY boundary term;
11. assemble the first vacuum-action candidate and compare its gates to EH.
```

The goal is not to re-prove Einstein-Hilbert. The goal is to derive, reject, or
modify the assumptions that made Einstein-Hilbert the selected completion in
the previous folder.
