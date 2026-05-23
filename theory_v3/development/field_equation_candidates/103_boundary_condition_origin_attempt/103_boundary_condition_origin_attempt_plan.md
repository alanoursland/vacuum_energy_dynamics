# 103_boundary_condition_origin_attempt — Plan

## Purpose

Group 103 follows Group 102.

Group 102 classified formal source-vector signatures:

```text
endpoint-weight families S=(1-x^2)^p -> all-negative signatures;
monomial families S=x^(2q) -> longer leading-positive runs as q increases;
mixed families S=x^(2q)(1-x^2)^p -> interpolation between endpoint suppression and endpoint concentration.
```

Group 102 concluded:

```text
PHYSICAL_SOURCE_NOT_SELECTED
BOUNDARY_DOMAIN_ORIGIN_REQUIRED
```

Group 103 asks whether simple boundary/domain constraints can explain why one source family should be preferred.

This group is not allowed to declare a physical boundary condition. It is a formal origin attempt.

## Group Name

```text
103_boundary_condition_origin_attempt
```

## Central Question

```text
Can endpoint behavior or simple boundary regularity requirements select one of the formal source-vector signature families?
```

## Starting State

Imported from Group 102:

```text
source-vector structure scanned;
monomial source classes identified;
endpoint-weight source classes identified;
mixed source classes identified;
clean formal signature families identified;
physical source not selected;
boundary/domain origin required;
physical ledger assignment deferred.
```

## Formal Source Families

Group 103 interprets the source profiles as endpoint behavior classes:

```text
S(x)=x^(2q)(1-x^2)^p.
```

Endpoint behavior:

```text
near x=0:
  S ~ x^(2q)

near x=1:
  S ~ (1-x^2)^p.
```

So:

```text
q controls origin regularity/central suppression;
p controls outer endpoint vanishing.
```

The test weight already has:

```text
w(x)=(1-x^2)^4.
```

Therefore, effective endpoint weight is:

```text
S(x)w(x)=x^(2q)(1-x^2)^(p+4).
```

## What This Group Should Test

Group 103 should:

```text
classify boundary behavior of S_pq at x=0 and x=1;
compute endpoint vanishing orders;
test if common regularity choices select source families:
  finite at x=0;
  vanishing at x=1;
  derivative vanishing at x=1;
  central suppression at x=0;
compare selected families to Group 102 sign classes;
classify whether boundary behavior can explain all-negative vs leading-positive signatures.
```

## Candidate Formal Boundary Classes

```text
B0_FINITE_ORIGIN:
  q >= 0.

B1_CENTER_SUPPRESSED:
  q >= 1.

B2_ENDPOINT_NONZERO:
  p = 0.

B3_ENDPOINT_VANISHING:
  p >= 1.

B4_ENDPOINT_SMOOTH_VANISHING:
  p >= 2.

B5_BALANCED_SUPPRESSED:
  q >= 1 and p >= 1.

B6_STRONG_ENDPOINT_SUPPRESSED:
  p >= q or p >= q-1.
```

## What This Group Must Not Do

Group 103 must not:

```text
claim x=0 is physical center;
claim x=1 is physical infinity/surface/boundary;
claim p or q is physically selected;
claim a source profile is mass, matter, J_curv, exchange, interface, or total burden;
claim boundary conditions are derived from the postulates;
insert parent equation terms;
open recombination.
```

## Recommended Script Batch

```text
candidate_boundary_origin_problem.py
candidate_endpoint_order_inventory.py
candidate_boundary_class_signature_map.py
candidate_boundary_selection_rule_probe.py
candidate_boundary_origin_classifier.py
candidate_group_103_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_boundary_origin_problem.py

Open Group 103 as a formal boundary/domain origin attempt.

### 2. candidate_endpoint_order_inventory.py

For `S_pq=x^(2q)(1-x^2)^p`, compute endpoint vanishing orders at `x=0` and `x=1`.

### 3. candidate_boundary_class_signature_map.py

Use Group 102-style source-vector signatures for `p=0..4`, `q=0..6`, and map them to boundary classes.

### 4. candidate_boundary_selection_rule_probe.py

Test candidate boundary selection rules against signature classes.

Examples:

```text
endpoint vanishing p>=1 mostly favors all-negative for q<=1;
endpoint concentration q large produces leading-positive/multi-flip;
balanced suppression p>=q may favor all-negative.
```

### 5. candidate_boundary_origin_classifier.py

Classify:

```text
ENDPOINT_BEHAVIOR_CLASSES_DEFINED
BOUNDARY_CLASS_SIGNATURE_MAP_BUILT
BOUNDARY_RULES_CAN_EXPLAIN_SIGNATURE_TRENDS
PHYSICAL_BOUNDARY_NOT_DERIVED
PHYSICAL_SOURCE_NOT_SELECTED
```

### 6. candidate_group_103_status_summary.py

Close the group.

## Key Success Criteria

Group 103 must produce:

```text
endpoint order inventory;
boundary-class/signature map;
selection-rule probe;
a conservative decision surface.
```

## Recommended Next Group

If a useful rule emerges:

```text
104_boundary_selected_source_vector_probe
```

If no useful rule emerges:

```text
104_residual_operator_origin_attempt
```

If returning to admissibility theorem:

```text
104_difference_numerator_factorization_attempt
```

## Final Interpretation

Group 103 asks:

```text
Can the boundary explain the ghost's shadow?
```

Goblin discipline:

```text
Do not call the doorway physical yet.
First see which shadows fit through it.
```
