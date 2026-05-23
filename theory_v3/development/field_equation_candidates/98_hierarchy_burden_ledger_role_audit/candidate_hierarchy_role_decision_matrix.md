# candidate_hierarchy_role_decision_matrix — Analysis Note

## Result

`candidate_hierarchy_role_decision_matrix.py` scores possible physical roles for the hierarchy branch.

The result is:

```text
CONFIGURATION_ONLY:
  NOT_LICENSED

EXCHANGE_COMPENSATION:
  NOT_LICENSED

INTERFACE_SMOOTHING:
  NOT_LICENSED

TOTAL_BURDEN:
  NOT_LICENSED

AUXILIARY_ADMISSIBILITY:
  SUPPORTED

AUXILIARY_RECONSTRUCTION:
  SUPPORTED
```

The strongest licensed role is:

```text
AUXILIARY_ADMISSIBILITY
```

The missing evidence is explicit.

For `CONFIGURATION_ONLY`:

```text
covariant_J_curv_definition;
source_origin;
ordinary_matter_separation.
```

For `EXCHANGE_COMPENSATION`:

```text
exchange_current_definition;
source_origin;
divergence_identity;
ordinary_matter_separation.
```

For `TOTAL_BURDEN`:

```text
total_burden_functional;
covariant_J_curv_definition;
exchange_current_definition;
interface_profile_definition;
source_origin;
divergence_identity;
ordinary_matter_separation.
```

## Interpretation

This is the main decision result of Group 98.

The hierarchy branch has enough mathematical structure to support:

```text
finite response uniqueness / nondegeneracy;
admissibility-chain proof targets;
exact numerator positivity as a theorem target.
```

But it does not yet have the evidence required to assign it to a physical ledger.

This is not a demotion to useless algebra. It is a precise status:

```text
The hierarchy is an auxiliary admissibility candidate.
```

That means if later work derives a burden functional or source problem that produces this hierarchy, then the determinant/Schur/numerator branch becomes a support theorem for that physical structure.

## What Changed

The hierarchy now has a safe current role.

Old informal temptation:

```text
this might be J_curv or exchange or total burden.
```

Correct current status:

```text
this is auxiliary admissibility until source/functional origin is derived.
```

## What Did Not Change

No physical ledger assignment is licensed.

## Carry-forward status

```text
HIERARCHY_ROLE_AUXILIARY_ADMISSIBILITY_CANDIDATE
AUXILIARY_RECONSTRUCTION_SUPPORTED_AS_FALLBACK
CONFIGURATION_ONLY_ASSIGNMENT_NOT_LICENSED
EXCHANGE_COMPENSATION_ASSIGNMENT_NOT_LICENSED
INTERFACE_SMOOTHING_ASSIGNMENT_NOT_LICENSED
TOTAL_BURDEN_ASSIGNMENT_NOT_LICENSED
PHYSICAL_LEDGER_ASSIGNMENT_DEFERRED
```
