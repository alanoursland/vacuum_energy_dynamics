# VacuumForge Lambda Baseline Inventory

## Purpose

This report opens the Lambda baseline workstream after the higher-curvature
residual detour. It does not derive the observed cosmological constant. It
separates baseline selection from local strain residuals and dark-sector
excess bookkeeping.

This report depends on:

```text
higher_curvature_tensor_route_audit_007
```

It satisfies:

```text
lambda_baseline_folder_required_007
```

## Symbolic Checks

For a localized mass plus cosmological term:

```text
Phi_M      = -G*M/r
Phi_Lambda = -Lambda*r**2/6
Phi_total  = -G*M/r - Lambda*r**2/6
```

SymPy verifies:

```text
Delta Phi_M (r > 0) = 0
Delta Phi_Lambda = -Lambda
Delta Phi_total  = -Lambda
a_r              = -G*M/r**2 + Lambda*r/3
Lambda -> 0 bridge residual = 0
lim Phi_Lambda as r -> infinity = -oo
```

Therefore positive nonzero `Lambda` is a background-curvature sector, not the
asymptotically flat scalar boundary-flux bridge.

The vacuum equation-of-state bookkeeping gives:

```text
rho_vac + 3 P_vac = -2*rho_vac
```

This is only a source-ledger identity. It does not compute the value of
`rho_vac`.

## Route Inventory

| route | baseline role | boundary data | source ledger | status | next obligation |
| --- | --- | --- | --- | --- | --- |
| lambda_zero_flat_bridge | scalar boundary-flux sector with no supplied background curvature | asymptotic flatness | ordinary localized matter only | selected baseline when no background curvature is supplied | do not use this sector to infer the observed nonzero Lambda |
| free_lovelock_constant | allowed EH/Lovelock p=0 term | de Sitter or anti-de Sitter background data required | vacuum background, not matter and not dark excess | allowed but unvalued | provide a selector before treating the value as derived |
| derived_vacuum_floor | nonzero vacuum baseline selected by ontology, measure, topology, or admissibility | baseline-selection boundary data not yet supplied | must distinguish constant floor from transportable excess | selector required | state the variational/admissibility rule that fixes sign and value |
| relaxation_or_nonlocal_selection | global or history-dependent vacuum floor | domain/history/kernel data required | must leave closed local metric equations intact or explicitly route deviations | not yet evaluated | prove local-equation quarantine and conservation identity |
| dark_excess_not_lambda | transportable or clustered excess over the floor | downstream dark-sector workstream | must not be inserted as constant Lambda | separate workstream | open only after baseline ledger prevents source double-counting |

## Current Conclusion

The Lambda baseline workstream is open. The `Lambda = 0` branch is the
asymptotically flat scalar boundary-flux sector when no nonzero background
curvature is supplied. Nonzero `Lambda` is allowed by the EH/Lovelock branch
but remains unvalued. A derived nonzero vacuum floor requires a selector:
variational, admissibility, topology, measure, or relaxation.

Dark-sector excess remains downstream and must not be inserted as the constant
baseline.

## Classification

```text
result type: Lambda baseline inventory / selector contract opener
scope: baseline/background curvature after local residual routes
conclusion: Lambda is allowed but not valued; nonzero Lambda requires a baseline selector
non-conclusion: observed Lambda is not derived; no dark-sector excess is licensed
```

The next technical target is a selector test:

```text
state candidate baseline selectors and kill conditions before any nonzero
Lambda mechanism is used.
```
