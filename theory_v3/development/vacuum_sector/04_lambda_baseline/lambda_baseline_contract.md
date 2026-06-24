# Lambda Baseline Contract

This contract separates the vacuum baseline from local strain residuals.

## Starting Point

The closed local branch allows:

```text
S = (c^4 / 16*pi*G) integral sqrt(-g) (R - 2 Lambda)
```

but the preceding strain-residual gates do not compute `Lambda`.

The allowed term has three distinct roles that must not be conflated:

```text
1. Lambda = 0 as the asymptotically flat scalar boundary-flux sector.
2. Lambda as an allowed Lovelock/background constant.
3. Lambda as a derived nonzero vacuum floor, if a selector is found.
```

## Contract Questions

Before any nonzero baseline is adopted, a branch must answer:

```text
what selects the vacuum reference state?
what boundary data replace asymptotic flatness?
what source ledger distinguishes Lambda from matter and dark excess?
what variational or admissibility rule fixes the sign and value?
what prevents local residuals from being smuggled in as baseline curvature?
what observational or internal consistency condition can kill the branch?
```

## Current Classification

```text
Lambda = 0:
  status: asymptotically flat boundary-flux sector
  role: selected when no nonzero background curvature is supplied

Lambda free:
  status: allowed but unvalued Lovelock parameter
  role: legal local metric baseline, not an ontology result

Lambda nonzero derived:
  status: selector required
  role: live vacuum-sector target only after a baseline-selection principle
```

## Non-Conclusions

This contract does not:

```text
derive the observed Lambda value;
license a dark-sector excess;
modify the closed local gravitational equations;
rescue higher-curvature residuals;
turn boundary bookkeeping into a bulk source.
```

## First Test

The first check is bookkeeping only:

```text
Phi_Lambda = -Lambda r^2 / 6
Delta Phi_M = 0 for r > 0
Delta Phi_Lambda = -Lambda
a_r = -GM/r^2 + Lambda r/3
```

This confirms that nonzero `Lambda` is a background-curvature sector, not the
asymptotically flat scalar bridge.
