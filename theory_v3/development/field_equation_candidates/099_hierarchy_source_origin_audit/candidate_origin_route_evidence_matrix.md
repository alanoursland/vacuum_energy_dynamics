# candidate_origin_route_evidence_matrix — Analysis Note

## Result

`candidate_origin_route_evidence_matrix.py` scores candidate origin routes.

The result is:

```text
MOMENT_PROJECTION:
  PLAUSIBLE_BUT_UNDERDERIVED

VARIATIONAL_HESSIAN:
  NOT_LICENSED

INTERFACE_SMOOTHING:
  NOT_LICENSED

EXCHANGE_COMPENSATION:
  NOT_LICENSED

TOTAL_BURDEN:
  NOT_LICENSED

AUXILIARY_ADMISSIBILITY:
  SUPPORTED
```

For `MOMENT_PROJECTION`, the missing items are:

```text
continuum_residual_identified;
test_basis_identified;
source_vector_identified;
boundary_conditions_identified.
```

For `VARIATIONAL_HESSIAN`, the missing items are:

```text
functional_defined;
hessian_symmetry_or_weighting;
physical_units_tracked;
ordinary_matter_separation.
```

For `TOTAL_BURDEN`, the missing items include:

```text
total_burden_defined;
functional_defined;
exchange_current_defined;
interface_domain_defined;
ordinary_matter_separation;
divergence_identity.
```

## Interpretation

This is the main origin-route classification of Group 099.

The result is conservative and useful:

```text
A_N looks like it could be a moment/projection matrix,
but the actual projection problem has not been derived.
```

Everything stronger remains unlicensed.

This matters because it prevents a hidden leap from:

```text
A_N has a moment-like formula
```

to:

```text
A_N is the burden functional.
```

That leap is not allowed.

## What Changed

The best physical-grounding trail is now clear:

```text
derive a continuum residual,
choose test/basis functions,
derive A_N as a projection/moment matrix,
identify the source vector and boundary conditions.
```

## What Did Not Change

The hierarchy remains auxiliary admissibility until that derivation exists.

## Carry-forward status

```text
MOMENT_PROJECTION_ORIGIN_PLAUSIBLE_BUT_UNDERDERIVED
VARIATIONAL_HESSIAN_ORIGIN_NOT_LICENSED
INTERFACE_SMOOTHING_ORIGIN_NOT_LICENSED
EXCHANGE_COMPENSATION_ORIGIN_NOT_LICENSED
TOTAL_BURDEN_ORIGIN_NOT_LICENSED
AUXILIARY_ADMISSIBILITY_SUPPORTED
```
