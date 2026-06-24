# VacuumForge Neighboring-Mismatch Inventory

## Purpose

This inventory makes the neighboring-mismatch contract operational. It does not
choose a strain action. It classifies currently inventoried ways to compare
`X(p)` and `X(q)` before candidate branch dynamics are opened.

This inventory depends on:

```text
x_contract_inventory_002
```

because an `X` option does not generate dynamics until a between-point
comparison rule is supplied.

## Inventory

| branch | comparison rule | candidate invariant | boundary requirement | conservation route | mode risk | epsilon status | status | next obligation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Levi-Civita metric transport | compare g_ab by the torsion-free metric-compatible connection | EH/GHY curvature scalar baseline | induced metric plus GHY-style boundary term | Bianchi identity and stress conservation in GR branch | baseline two-TT-mode branch after constraints | epsilon = 0 definition if selected | metric-transport placeholder | explain why vacuum ontology selects Levi-Civita metric transport |
| independent affine connection | compare X using a connection independent of metric reduction | Palatini/metric-affine curvature or connection strain | connection boundary data or compatible boundary counterterm | requires metric compatibility, projective gauge, or routed nonmetric current | torsion, nonmetricity, or projective modes if not constrained | extra-field route required | extra-connection route required | derive compatibility or route torsion/nonmetric residuals explicitly |
| calibration map | compare local interval responses through a calibration/coherence map | calibration mismatch scalar not yet specified | calibration boundary data not yet specified | Noether identity absent until calibration field/action is defined | nonmetric drift or species-dependent clock/ruler effects | underdetermined without new axiom | partial mismatch contract | define calibration variable, invariant, and matter-coupling route |
| holonomy or loop mismatch | compare transport around infinitesimal loops | curvature/holonomy scalar; EH-like versus curvature-squared choice unresolved | curvature-action boundary term depends on derivative order | Bianchi-like identity possible but invariant-dependent | curvature-squared or higher-derivative modes unless routed | not yet classified | partial mismatch contract | explain why the leading scalar is EH-like or classify residual modes |
| medium strain tensor | compare internal medium/order-parameter gradients | constitutive elastic scalar not yet specified | medium boundary/defect data not yet specified | requires medium stress and exchange ledger | preferred-frame, anisotropy, longitudinal or extra medium modes | underdetermined without new axiom | underdetermined without new axiom | state constitutive law and route extra modes and frame effects |
| Finsler direction map | compare direction-dependent interval responses | Finsler/nonquadratic strain scalar not yet specified | direction-bundle boundary data not yet specified | requires routed nonmetric matter calibration identity | null-cone, PPN, propagation, and species-calibration deviations | requires explicit residual route | partial mismatch contract | route nonquadratic response through epsilon tests before physical use |
| nonlocal kernel | compare X(p) and X(q) through a kernel or global constraint | nonlocal relaxation functional not yet specified | global/bulk-boundary split not yet specified | requires nonlocal conservation or relaxation identity | large-scale response, acausality, or hidden local equation modification | nonlocal route required | nonlocal route required | quarantine to Lambda/dark/large-scale sector unless local equations stay closed |

## Current Conclusion

No currently inventoried non-baseline neighboring-mismatch rule is complete
enough to open candidate strain dynamics without additional routing. The
Levi-Civita metric transport rule is usable as the GR baseline, but remains a
metric-transport placeholder for the vacuum ontology unless a selector explains
why vacuum strain uses that comparison rule.

This is an inventory result, not a global no-go theorem against nonmetric,
nonlocal, holonomy, Finsler, or medium mismatch rules.

## Classification

```text
result type: neighboring-mismatch inventory / governance classification
scope: candidate between-point comparison rules for X(p), X(q)
conclusion: no currently inventoried non-baseline mismatch rule is strain-ready without routing
non-conclusion: no K_strain selected; no epsilon computed; no residual branch licensed
```

The next technical target is the residual gate ledger:

```text
which tests must a routed residual pass before candidate branch work opens?
```
