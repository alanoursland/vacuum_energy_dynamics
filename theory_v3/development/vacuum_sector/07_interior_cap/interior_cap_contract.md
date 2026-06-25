# Interior-Cap Admissibility Contract

## Claim

Interior modification is admissible only if it preserves the tested exterior
sector or is explicitly routed back through residual gates. A finite interior
cap additionally needs a derived admissibility rule or scale.

## Scope

This contract covers compact-object interiors and strong-field admissibility.
It does not prove a nonsingular interior, a horizon cap, or a modified
equation of state.

## Exterior Preservation Rule

The exterior-preserving route must keep:

```text
exterior field equations
exterior mass/charge/angular-momentum data
asymptotic or Lambda baseline data
matching or junction bookkeeping
```

If the exterior changes, the claim leaves this folder and returns to the
residual-gate ledger.

## Interior Admissibility Rule

An interior cap must state:

```text
the interior strain or action quantity being bounded;
the admissibility bound;
the origin of that bound;
the cap radius or compactness threshold;
the source or surface-layer bookkeeping;
the observable face after exterior matching.
```

## Symbolic Placeholder

Use compactness:

```text
C = 2GM / (c^2 R_cap)
```

A cap at the GR horizon threshold gives:

```text
R_cap = 2GM / c^2
```

A finite-strain placeholder:

```text
K_int = 1 / (1 - C)
```

with an imposed bound `K_int = kappa_max` gives:

```text
R_cap = 2GM kappa_max / (c^2 (kappa_max - 1))
```

This imports `kappa_max` unless the vacuum ontology derives it.

## Current Classification

The first VacuumForge pass records:

```text
derivation: interior_cap_admissibility_contract_025
obligation satisfied: interior_cap_admissibility_contract_required_024
new obligation: exterior_matching_lemma_required_025
```

Current conclusion:

```text
No finite-strain interior cap is licensed.
```

Exterior-preserving interior modification remains a candidate contract only.
Imported cutoff radii and untracked exterior deviations are rejected.

## Non-Conclusions

This contract does not kill interior completion routes. It only blocks cap
claims that lack exterior matching, source bookkeeping, and a derived
finite-strain scale.
