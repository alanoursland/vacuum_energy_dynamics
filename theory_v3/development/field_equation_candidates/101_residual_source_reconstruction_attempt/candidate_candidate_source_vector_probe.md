# candidate_candidate_source_vector_probe — Analysis Note

## Result

`candidate_candidate_source_vector_probe.py` computes formal source vectors:

```text
b_k(S)=2∫psi_k S w dx
```

for simple source profiles:

```text
S=1
S=x^2
S=1-x^2
S=(1-x^2)^2.
```

The sign patterns are:

```text
S=1:
  [-1, -1, -1, -1, -1, -1, -1, -1]

S=x^2:
  [1, -1, -1, -1, -1, -1, -1, -1]

S=1-x^2:
  [-1, -1, -1, -1, -1, -1, -1, -1]

S=(1-x^2)^2:
  [-1, -1, -1, -1, -1, -1, -1, -1].
```

Governance records:

```text
source vector probes:
  simple formal source vectors computed

source selection:
  no source profile physically selected

structure clue:
  source profiles produce distinct sign patterns.
```

## Interpretation

This is a useful exploratory result.

The formal source-vector map is sensitive to the choice of `S(x)`. Most simple positive source profiles tested produce all-negative source projections, while `S=x^2` produces a positive first component and negative later components.

That means the sign-changing test functions matter. They do not simply measure positive source mass. They measure a signed balance of the source profile relative to each row root.

This is a clue for source selection:

```text
the physical S(x), if one exists, cannot be chosen casually.
```

It must be derived from the residual/boundary problem, because different simple profiles produce meaningfully different source-vector signatures.

## What It Does Not Prove

No tested `S(x)` is selected as physical.

The source vector is not ordinary matter, not mass density, not `J_curv`, not `H_exch`, and not total burden by declaration.

## Carry-forward status

```text
SIMPLE_SOURCE_VECTOR_PROBES_COMPLETED
SOURCE_VECTOR_SIGN_PATTERNS_COMPUTED
SOURCE_PROFILES_PRODUCE_DISTINCT_SIGN_SIGNATURES
PHYSICAL_SOURCE_NOT_SELECTED
FORMAL_BK_NOT_MATTER_SOURCE
```
