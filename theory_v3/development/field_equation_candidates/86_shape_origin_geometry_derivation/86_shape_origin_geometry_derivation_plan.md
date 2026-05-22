# 86_shape_origin_geometry_derivation — Plan

## Purpose

Group 86 tests whether the Group 85 suppression profile

```text
P(y) = 1 - 12 y^2 + 51 y^4
```

has a structural origin inside the reduced exactness model, or whether it is merely a moment-fit profile.

Group 85 found that this even quartic shape suppresses low-order payload moments:

```text
M0..M5 = 0
W0..W3 = 0
```

while preserving compact endpoint flux. It also found that the local field remains nonzero and higher moments remain:

```text
rho(0) = -30
M6 != 0
W4 != 0
```

The open question is:

```text
why this P?
```

Group 86 tries to derive the profile as the unique minimal-degree reduced payload-suppression shape, and also as the unique minimizer of a low-order payload action.

This is not full covariant geometry and not full physical derivation. It is a real reduced-class origin test.

## Group Name

```text
86_shape_origin_geometry_derivation
```

## Central Question

```text
Is P(y)=1-12y^2+51y^4 forced by a structural reduced payload-suppression principle,
or is it only a fitted moment-cancellation profile?
```

## Starting State

Imported from Group 85:

```text
even quartic shape family tested;
P=1-12y^2+51y^4 found from M2=M4 constraints;
profile regular/positive on [-1,1];
M0..M5 vanish;
W0..W3 vanish;
local rho remains nonzero;
M6 and W4 remain nonzero;
linear-skew obstruction is not universal;
shape origin remains open;
full local inertness not proven;
parent divergence identity unproven;
recombination blocked.
```

## Concrete Origin Candidates

Group 86 tests these origin claims.

### 1. Minimal-Degree Origin

For even shapes:

```text
P_N(y) = 1 + a1 y^2 + ... + aN y^(2N)
```

the constraints:

```text
M2 = 0
M4 = 0
```

cannot both be satisfied by degree 0 or degree 2.

They can be uniquely satisfied at degree 4:

```text
P(y)=1-12y^2+51y^4
```

So the profile is the minimal even normalized polynomial that suppresses the first two nontrivial even payload moments.

### 2. Payload-Action Variational Origin

Define a low-order payload action on the even quartic family:

```text
A(p,q) = M2(p,q)^2 + M4(p,q)^2
```

The expected result is:

```text
A >= 0
A = 0 only at p=-12, q=51
```

Thus the same profile is the unique global minimizer of the reduced low-order payload action.

### 3. Weighted Consistency Origin

Because the measure is quadratic:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

and the profile kills:

```text
M0..M5
```

it automatically kills:

```text
W0..W3
```

This explains why Group 85's weighted suppression followed from the flat moment block.

## Desired Outcome

A useful result is:

```text
P=1-12y^2+51y^4 is derived as:
  the unique minimal-degree normalized even polynomial that kills M2 and M4;
  the unique zero-action minimizer of A=M2^2+M4^2;
  a profile whose flat moment block automatically implies weighted suppression through W3 for quadratic mu.
```

Status:

```text
shape origin strengthened inside reduced model;
not full covariant/physical origin;
higher moments and local rho remain.
```

## What This Group May Do

Group 86 may:

```text
derive the moment map from polynomial coefficients;
prove lower-degree obstruction;
prove quartic uniqueness;
derive the low-order payload action minimizer;
show weighted consistency follows from flat moment block;
classify whether the shape is structurally derived inside the reduced model.
```

## What This Group Must Not Do

Group 86 must not:

```text
claim full geometry/covariance;
claim full local inertness;
claim rho(y)=0;
erase M6/W4;
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_shape_origin_problem.py
candidate_moment_map_from_shape_coefficients.py
candidate_minimal_degree_obstruction.py
candidate_quartic_uniqueness_theorem.py
candidate_payload_action_minimizer.py
candidate_weighted_consistency_from_flat_block.py
candidate_shape_origin_route_classifier.py
candidate_group_86_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_shape_origin_problem.py

Open Group 86 as a structural origin test.

It should restate:

```text
Group 85 found an effective profile;
Group 86 tests whether its origin is structural inside the reduced model.
```

### 2. candidate_moment_map_from_shape_coefficients.py

For:

```text
P = 1 + a1 y^2 + a2 y^4 + a3 y^6
```

derive the moment map:

```text
M2, M4, M6
```

as linear functions of the shape coefficients.

This clarifies that moment suppression is a linear operator from shape coefficients to payload moments.

### 3. candidate_minimal_degree_obstruction.py

Test degree 0 and degree 2.

Expected:

```text
degree 0 cannot kill M2;
degree 2 can kill M2 but not M4;
therefore degree 4 is minimal for killing M2 and M4.
```

### 4. candidate_quartic_uniqueness_theorem.py

Solve the quartic system:

```text
P = 1 + p y^2 + q y^4
M2 = 0
M4 = 0
```

Expected unique solution:

```text
p=-12
q=51
```

### 5. candidate_payload_action_minimizer.py

Define:

```text
A(p,q) = M2^2 + M4^2
```

Derive:

```text
grad A = 0
```

Expected unique minimizer:

```text
p=-12
q=51
A=0
```

This is the reduced variational origin.

### 6. candidate_weighted_consistency_from_flat_block.py

Show that if:

```text
M0..M5 = 0
```

then for quadratic measure:

```text
W0..W3 = 0
```

because:

```text
Wn = R^2 M_n + 2Rell M_(n+1) + ell^2 M_(n+2)
```

This turns the Group 85 weighted suppression into a consequence of the flat moment block.

### 7. candidate_shape_origin_route_classifier.py

Classify:

```text
MINIMAL_DEGREE_ORIGIN_DERIVED
QUARTIC_UNIQUENESS_DERIVED
LOW_ORDER_PAYLOAD_ACTION_MINIMIZER_DERIVED
WEIGHTED_SUPPRESSION_FOLLOWS_FROM_FLAT_BLOCK
SHAPE_ORIGIN_STRENGTHENED_IN_REDUCED_MODEL
FULL_GEOMETRIC_ORIGIN_OPEN
LOCAL_RHO_NONZERO_REMAINS
HIGHER_MOMENTS_REMAIN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. candidate_group_86_status_summary.py

Close the group.

Expected result:

```text
the profile has a reduced structural origin, not just a fitted profile;
but full covariant/physical origin remains open.
```

## Key Success Criteria

Group 86 must earn real origin statements:

```text
degree 4 is minimal for killing M2 and M4 among normalized even polynomial shapes;
P=1-12y^2+51y^4 is unique at degree 4;
P is the unique zero-action minimizer of A=M2^2+M4^2;
quadratic-measure W0..W3 suppression follows from flat M0..M5 suppression.
```

## Safe Handoff Options

Likely next groups:

```text
87_moment_hierarchy_closure_test
87_covariant_payload_suppression_lift
87_shape_variational_physical_origin
87_payload_projection_operator_necessity
87_parent_blocker_refresh
```

If Group 86 succeeds, the best next group is probably:

```text
87_moment_hierarchy_closure_test
```

because the reduced origin is strong enough to ask whether higher-degree profiles create a hierarchy of moment suppression.

## Final Interpretation

Group 86 asks:

```text
Was the quartic key carved by the reduced lock,
or filed by hand after seeing the tumblers?
```

Goblin discipline:

```text
A key cut by the lock is better than a key filed by panic.
But it is still only for that lock.
```
