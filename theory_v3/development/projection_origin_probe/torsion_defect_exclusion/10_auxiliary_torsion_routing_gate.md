# Torsion Defect Exclusion 10: Auxiliary Torsion Routing Gate

## Purpose

This proof checks the auxiliary route.

If an auxiliary carrier is allowed to convert scalar data into torsion source
data, that carrier is a separate routed field. It cannot remain hidden inside
the scalar projection ladder.

## Validated Checks

- auxiliary carrier changes stationary torsion: passed
- setting auxiliary carrier to zero removes its torsion contribution: passed
- torsion-free cancellation condition exposes the auxiliary carrier: passed

## Model

Let:

```text
J_aux = eta s
J_total = J_visible + eta s.
```

Then:

```text
tau = J_total/(24 mu)
    = (J_visible + eta*s)/(24*mu).
```

The sensitivity to the auxiliary carrier is:

```text
d tau / d eta = s/(24*mu).
```

Torsion-free cancellation would require:

```text
eta = -J_visible/s.
```

## Interpretation

An auxiliary torsion route is allowed only as an explicit branch. If `eta`
exists, it changes the torsion equation. If it does not exist or is constrained
to zero, the scalar `s` alone does not source torsion.
