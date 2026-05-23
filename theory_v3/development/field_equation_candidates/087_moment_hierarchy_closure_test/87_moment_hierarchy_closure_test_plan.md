# 87_moment_hierarchy_closure_test — Plan

## Purpose

Group 87 tests whether the Group 85/86 quartic suppression profile is the first member of a systematic hierarchy.

Group 86 derived a reduced structural origin for:

```text
P_2(y) = 1 - 12 y^2 + 51 y^4
```

as the unique minimal-degree normalized even quartic shape that kills:

```text
M2 = 0
M4 = 0
```

and as the unique zero-action minimizer of:

```text
A = M2^2 + M4^2
```

Group 87 now asks whether the same mechanism generalizes.

For normalized even polynomial profiles:

```text
P_N(y) = 1 + a1 y^2 + a2 y^4 + ... + aN y^(2N)
```

inside the same compact-support exactness structure:

```text
Xi = (1-y^2)^3 P_N(y)
J = (1-y^2)^2 dXi/dy
rho = dJ/dy
```

test whether the `N` coefficients uniquely suppress:

```text
M2, M4, ..., M(2N)
```

and whether the next moment remains nonzero.

This is real progress if it shows the quartic profile is not a one-off trick but part of a finite-order payload-suppression hierarchy.

This is not full local inertness and not a covariant theorem.

## Group Name

```text
87_moment_hierarchy_closure_test
```

## Central Question

```text
Does the reduced exactness shape family form a systematic moment-suppression hierarchy,
or was the Group 85/86 quartic profile a one-off?
```

## Starting State

Imported from Group 86:

```text
moment map derived;
degree 4 minimal for M2/M4 suppression;
P=1-12y^2+51y^4 uniquely derived in normalized even quartic family;
same P minimizes A=M2^2+M4^2;
W0..W3 weighted suppression follows from M0..M5 flat moment block;
shape origin strengthened inside reduced model;
full physical/covariant origin remains open;
local rho nonzero remains;
higher moments M6/W4 remain;
parent divergence identity unproven;
recombination blocked.
```

## Concrete Hierarchy

For:

```text
P_N = 1 + sum_{k=1}^N a_k y^(2k)
```

define moments:

```text
M_m = ∫ y^m rho dy
```

Because `P_N` is even:

```text
rho is even
M_odd = 0
```

The hierarchy test is:

```text
M2 = M4 = ... = M(2N) = 0
```

Expected profiles:

```text
N=1:
  P_1 = 1 + 39 y^2
  kills M2
  next M4 != 0

N=2:
  P_2 = 1 - 12 y^2 + 51 y^4
  kills M2,M4
  next M6 != 0

N=3:
  P_3 = 1 + 153 y^2 - 969 y^4 + 1615 y^6
  kills M2,M4,M6
  next M8 != 0

N=4:
  P_4 = 1 - (4332/131)y^2 + (51186/131)y^4 - (166060/131)y^6 + (163875/131)y^8
  kills M2,M4,M6,M8
  next M10 != 0
```

## Desired Outcome

A useful result is:

```text
For N=1..4, the finite moment-suppression hierarchy exists:
  degree 2N gives a unique normalized even profile killing M2..M(2N);
  next even moment M(2N+2) remains nonzero.
```

and:

```text
For quadratic measure mu=R^2+2Rell y+ell^2 y^2,
  if M0..M(2N+1)=0,
  then W0..W(2N-1)=0.
```

Status:

```text
moment hierarchy supported through N=4;
all-order closure not proven;
local rho nonzero remains;
shape physical/covariant origin remains open.
```

## What This Group May Do

Group 87 may:

```text
derive the hierarchy moment operator;
solve hierarchy profiles for N=1..4;
test uniqueness/rank of the constraint matrix;
derive weighted-block inheritance for quadratic measure;
identify the next nonzero obstruction moment;
classify finite hierarchy support versus all-order closure.
```

## What This Group Must Not Do

Group 87 must not:

```text
claim all-order inertness;
claim full covariant geometry;
claim rho(y)=0;
erase next moments;
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_moment_hierarchy_problem.py
candidate_general_even_shape_operator.py
candidate_hierarchy_profiles_N1_to_N4.py
candidate_constraint_rank_uniqueness_test.py
candidate_weighted_block_inheritance_theorem.py
candidate_next_moment_obstruction_test.py
candidate_moment_hierarchy_route_classifier.py
candidate_group_87_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_moment_hierarchy_problem.py

Open Group 87 as a hierarchy test.

It should restate:

```text
Group 86 gave reduced origin for N=2;
Group 87 tests whether this is systematic for N=1..4.
```

### 2. candidate_general_even_shape_operator.py

Construct the general even polynomial profile and moment map.

Show:

```text
P_N even;
J odd;
rho even;
M_odd = 0.
```

### 3. candidate_hierarchy_profiles_N1_to_N4.py

Solve the hierarchy for N=1..4.

Expected profiles:

```text
N=1: [39]
N=2: [-12,51]
N=3: [153,-969,1615]
N=4: [-4332/131, 51186/131, -166060/131, 163875/131]
```

### 4. candidate_constraint_rank_uniqueness_test.py

For N=1..4, build the linear constraint matrix for:

```text
M2..M(2N)
```

and test rank.

Expected:

```text
rank = N
unique solution
```

### 5. candidate_weighted_block_inheritance_theorem.py

Prove the block inheritance formula:

```text
Wn = R^2 M_n + 2Rell M_(n+1) + ell^2 M_(n+2)
```

For even profiles with odd moments zero and suppressed even block through `M(2N)`:

```text
W0..W(2N-1)=0.
```

### 6. candidate_next_moment_obstruction_test.py

For each N=1..4, compute the next unsuppressed moment:

```text
M(2N+2)
```

Expected nonzero values:

```text
N=1: M4 = 32768/15015
N=2: M6 = 65536/323323
N=3: M8 = 10485760/22309287
N=4: M10 = 33554432/1252507113
```

This proves finite-order hierarchy, not full closure.

### 7. candidate_moment_hierarchy_route_classifier.py

Classify:

```text
FINITE_MOMENT_HIERARCHY_SUPPORTED_N1_TO_N4
UNIQUE_PROFILE_PER_ORDER
WEIGHTED_BLOCK_INHERITANCE_DERIVED
NEXT_MOMENT_OBSTRUCTION_PERSISTS
ALL_ORDER_CLOSURE_NOT_PROVEN
LOCAL_RHO_NONZERO_REMAINS
PHYSICAL_COVARIANT_ORIGIN_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. candidate_group_87_status_summary.py

Close the group.

Expected result:

```text
the quartic profile is part of a hierarchy through N=4;
finite-order suppression strengthened;
all-order closure remains open.
```

## Key Success Criteria

Group 87 must earn real hierarchy statements:

```text
For N=1..4, the normalized even degree-2N profile uniquely kills M2..M(2N).
```

and:

```text
Quadratic-measure weighted suppression W0..W(2N-1) follows from the flat moment block.
```

and:

```text
M(2N+2) remains nonzero in the tested cases.
```

## Safe Handoff Options

Likely next groups:

```text
88_hierarchy_formula_derivation
88_all_order_limit_obstruction
88_covariant_payload_suppression_lift
88_shape_variational_physical_origin
88_parent_blocker_refresh
```

If the N=1..4 hierarchy works, the best next group is probably:

```text
88_hierarchy_formula_derivation
```

because the next real progress is deriving the general coefficient formula or recurrence.

## Final Interpretation

Group 87 asks:

```text
Was the quartic key a one-off,
or the second tooth in a whole keyring?
```

Goblin discipline:

```text
A pattern through four teeth is not infinity.
But it is no longer a single shiny tooth.
```
