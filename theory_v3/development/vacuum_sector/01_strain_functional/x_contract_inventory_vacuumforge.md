# VacuumForge X Contract Inventory

## Purpose

This inventory makes the `X` contract operational. It does not choose a final
vacuum variable. It classifies candidate `X` choices by whether they are ready
for strain-branch work or still require routing/axioms.

This inventory depends on:

```text
local_response_underdetermines_strain_001
```

because the pointwise local response result showed that an `X` choice must be
paired with a neighboring-mismatch rule before it can generate dynamics.

## Inventory

| branch | X variable | metric reduction | status | next obligation |
| --- | --- | --- | --- | --- |
| metric-data branch | g_ab | identity: X = g_ab; Q_p(v) = g_ab v^a v^b | metric-only placeholder | cannot by itself explain why vacuum ontology chooses metric data as X |
| interval-response branch | Q_p(v) | quadratic gate plus polarization gives g_ab(p) | partial contract | supply neighboring mismatch rule for Q_p across points |
| frame/coframe branch | e^a_mu or coframe data | g_mu_nu = eta_ab e^a_mu e^b_nu | extra-field route required | route torsion/spin/frame observables and prove no hidden preferred frame |
| connection/transport branch | connection or transport map | requires separate metric/calibration relation | extra-field route required | derive metric compatibility or route nonmetric/torsion residuals |
| internal-medium branch | medium/order-parameter data | requires constitutive map from medium response to Q_p or g_ab | underdetermined without new axiom | state constitutive law and route extra modes, anisotropy, and frame effects |
| deeper-premetric branch | unspecified premetric variable | not yet specified | underdetermined without new axiom | define X before any strain branch can be evaluated |

## Current Conclusion

No non-metric `X` option is complete enough to open candidate strain dynamics
without additional routing. The metric-data branch is usable as the GR baseline
but remains a metric-only placeholder for the vacuum ontology unless a selector
explains why vacuum configuration reduces to `g_ab`.

The next technical target is the neighboring-mismatch contract:

```text
how are X(p) and X(q) compared?
```
