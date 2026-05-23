# candidate_hierarchy_physical_object_map — Analysis Note

## Result

`candidate_hierarchy_physical_object_map.py` maps the hierarchy objects to safe weak physical meanings.

Allowed weak mappings:

```text
det(A_N) nonzero:
  finite hierarchy uniqueness / nondegeneracy;
  admissibility support;
  not a physical energy functional.

row-signed Schur positivity:
  stable leading response chain;
  admissibility support;
  not J_curv definition.

Schur gap positivity:
  positive post-transition admissibility gap;
  proof target;
  not exchange current.

parity branch monotonicity:
  structured response convergence clue;
  proof target;
  not field equation.

difference numerator positivity:
  exact algebraic sign target for admissibility;
  next theorem target;
  not source law.
```

Rejected strong mappings:

```text
hierarchy = covariant J_curv;
hierarchy = H_curv;
hierarchy = H_exch;
hierarchy = total burden functional;
hierarchy = merger energy prediction;
hierarchy = source law;
hierarchy = anti-singularity dynamics.
```

## Interpretation

This map is very useful because it preserves the value of the hierarchy without overclaiming.

The hierarchy can safely mean:

```text
candidate uniqueness / nondegeneracy structure for a response system.
```

It cannot yet mean:

```text
the actual physical energy functional.
```

This distinction matters for future writing. When discussing Groups 91–97, the safe phrase is:

```text
auxiliary admissibility theorem candidate.
```

The unsafe phrase is:

```text
proof of the burden functional.
```

## What Changed

The hierarchy now has a vocabulary for safe interpretation.

## What Did Not Change

The source origin remains missing.

The functional origin remains missing.

The merger check cannot be performed from this hierarchy alone.

## Carry-forward status

```text
DET_NONZERO_MAPS_TO_FINITE_RESPONSE_UNIQUENESS_CANDIDATE
SCHUR_POSITIVITY_MAPS_TO_STABLE_ADMISSIBILITY_CHAIN_CANDIDATE
NUMERATOR_POSITIVITY_MAPS_TO_EXACT_ADMISSIBILITY_PROOF_TARGET
HIERARCHY_NOT_J_CURV
HIERARCHY_NOT_H_CURV
HIERARCHY_NOT_H_EXCH
HIERARCHY_NOT_TOTAL_BURDEN
HIERARCHY_NOT_SOURCE_LAW
SOURCE_ORIGIN_AUDIT_REQUIRED
FUNCTIONAL_ORIGIN_AUDIT_REQUIRED
```
