# 85_shape_family_payload_suppression_test — Plan

## Purpose

Group 85 tests whether the Group 84 local payload obstruction is a limitation of the compact-support **linear-skew** family, or whether it persists when the exactness profile is given a richer shape family.

Group 84 showed that the Group 83 linear-skew profile is globally useful but locally payload-dangerous:

```text
M0 = 0
M1 = -512 ell/(1155 R)
M2 = 1024/1155

W0 = 0
W1 != 0
W2 != 0
```

and, more sharply:

```text
weighted neutrality requires c = 3ell/(2R)
dipole inertness requires c = 0
M2 is independent of c
```

So the linear-skew family cannot prove local inertness.

Group 85 tests a richer exactness profile:

```text
Xi = f(y) P(y)
f = (1 - y^2)^3
w = (1 - y^2)^2
J = w dXi/dy
rho = dJ/dy
```

with an even quartic shape:

```text
P(y) = 1 + p y^2 + q y^4
```

The goal is to test whether the shape parameters can suppress low-order local payload moments without relying on a linear skew.

This is not full physical inertness and not a covariant theorem. It is a concrete reduced-class shape-family test.

## Group Name

```text
85_shape_family_payload_suppression_test
```

## Central Question

```text
Can a richer compact-support exactness shape suppress the low-order local payload moments that defeated the linear-skew family?
```

## Starting State

Imported from Group 84:

```text
global flat source moment M0 = 0 retained;
dipole moment M1 nonzero after Group 83 skew;
quadratic moment M2 nonzero and independent of linear skew;
weighted total moment W0 = 0 retained;
weighted local moments W1/W2 nonzero;
local inertness obstructed in finite-mode test;
rho exactness remains globally useful but locally payload-dangerous;
parent divergence identity unproven;
recombination blocked.
```

## Concrete Shape Family

Use:

```text
P(y) = 1 + p y^2 + q y^4
```

with:

```text
Xi = (1-y^2)^3 P(y)
J = (1-y^2)^2 dXi/dy
rho = dJ/dy
```

Because `P` is even, `J` is odd and `rho` is even.

This automatically gives:

```text
M0 = 0
M1 = 0
M3 = 0
```

by exactness and parity.

Then solve:

```text
M2 = 0
M4 = 0
```

Expected result:

```text
p = -12
q = 51
```

so:

```text
P(y) = 1 - 12 y^2 + 51 y^4
```

For this shape, expected moments:

```text
M0 = M1 = M2 = M3 = M4 = M5 = 0
M6 = 65536/323323
```

Under quadratic measure:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

expected weighted moments:

```text
W0 = W1 = W2 = W3 = 0
W4 = 65536 ell^2 / 323323
```

This would be real progress: the richer shape suppresses all local payload probes through quadratic order and their weighted extensions through cubic order.

## Desired Outcome

A useful result is one of these.

### Route A: Shape Suppression Works

A profile is found such that:

```text
M0..M5 = 0
W0..W3 = 0
```

while preserving:

```text
endpoint compact support
local rho nonzero
finite next obstruction M6/W4
```

Status:

```text
local payload suppression strengthened in reduced class;
not full inertness.
```

### Route B: Shape Suppression Partially Works

Some moments vanish, but a low-order moment remains.

Status:

```text
linear-skew obstruction softened but not removed.
```

### Route C: Shape Suppression Fails

No admissible quartic shape suppresses the required moments.

Status:

```text
payload obstruction strengthened.
```

## Expected Likely Result

The likely result is Route A:

```text
P = 1 - 12y^2 + 51y^4
```

suppresses low-order moments through:

```text
M5
```

and weighted moments through:

```text
W3
```

but leaves:

```text
M6 and W4 nonzero.
```

Interpretation:

```text
the local payload obstruction from Group 84 is not universal;
it was a limitation of the linear-skew family.

However, finite-mode suppression is still not full local inertness.
A shape-origin theorem is now required.
```

## What This Group May Do

Group 85 may:

```text
derive moment formulas for the even quartic shape family;
solve moment constraints;
test endpoint compact support;
test positivity/regularity of P(y);
compute flat and weighted moments;
classify whether suppression is genuine, partial, or repair-like.
```

## What This Group Must Not Do

Group 85 must not:

```text
claim full local inertness;
claim full covariant closure;
claim the shape is physically derived;
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_shape_suppression_problem.py
candidate_even_quartic_shape_family.py
candidate_moment_constraint_solver.py
candidate_suppressed_profile_validation.py
candidate_weighted_payload_extension.py
candidate_shape_admissibility_and_repair_discriminator.py
candidate_shape_suppression_route_classifier.py
candidate_group_85_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_shape_suppression_problem.py

Open Group 85 as a richer shape-family test.

It should restate:

```text
Group 84 obstructed local inertness in the linear-skew family;
Group 85 tests whether richer shape degrees of freedom can suppress payload moments.
```

### 2. candidate_even_quartic_shape_family.py

Define:

```text
P = 1 + p y^2 + q y^4
Xi = f P
J = w Xi'
rho = J'
```

Show parity:

```text
P even
J odd
rho even
```

Interpretation:

```text
odd payload moments vanish automatically.
```

### 3. candidate_moment_constraint_solver.py

Compute generic moments and solve:

```text
M2 = 0
M4 = 0
```

Expected:

```text
p = -12
q = 51
```

### 4. candidate_suppressed_profile_validation.py

Use:

```text
P = 1 - 12y^2 + 51y^4
```

Validate:

```text
J(-1)=J(1)=0
M0..M5 = 0
M6 != 0
rho(0) != 0
```

### 5. candidate_weighted_payload_extension.py

Compute weighted moments:

```text
Wn = ∫ mu y^n rho dy
```

Expected:

```text
W0..W3 = 0
W4 != 0
```

Interpretation:

```text
quadratic-measure local probes are suppressed through cubic order, but not all orders.
```

### 6. candidate_shape_admissibility_and_repair_discriminator.py

Check regularity and repair status.

Expected:

```text
P(y) = 1 - 12y^2 + 51y^4
```

is positive on `[−1,1]`, with minimum:

```text
85/289
```

This is admissible as a regular compact profile.

But shape coefficients are still moment-derived, not physically derived.

Status:

```text
not repair inside the reduced finite-mode suppression problem;
not full theory until shape origin is derived.
```

### 7. candidate_shape_suppression_route_classifier.py

Classify:

```text
EVEN_QUARTIC_SUPPRESSION_PROFILE_FOUND
LOW_ORDER_FLAT_PAYLOAD_SUPPRESSED_THROUGH_M5
LOW_ORDER_WEIGHTED_PAYLOAD_SUPPRESSED_THROUGH_W3
NEXT_MOMENT_OBSTRUCTION_M6_W4
LOCAL_RHO_NONZERO_REMAINS
SHAPE_ORIGIN_OPEN
FULL_LOCAL_INERTNESS_NOT_PROVEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. candidate_group_85_status_summary.py

Close the group.

Expected result:

```text
richer shape family overcomes the Group 84 low-order obstruction;
exactness route strengthened again;
full inertness not proven;
shape origin and higher moments remain open.
```

## Key Success Criteria

Group 85 must earn a real result.

Expected theorem-level statement:

```text
Within the even quartic compact-support exactness family,
P(y)=1-12y^2+51y^4 is the unique profile with P(0)=1 that kills M2 and M4,
thereby suppressing M0..M5 and W0..W3 under the quadratic measure.
```

Expected caution:

```text
This does not imply rho(y)=0.
This does not imply all moments vanish.
This does not derive the profile from geometry.
```

## Safe Handoff Options

Likely next groups:

```text
86_shape_origin_geometry_derivation
86_moment_hierarchy_closure_test
86_covariant_payload_suppression_lift
86_payload_projection_operator_necessity
86_parent_blocker_refresh
```

If the shape suppression works, the best next group is probably:

```text
86_shape_origin_geometry_derivation
```

because the project must know whether `P=1-12y^2+51y^4` is geometrically forced or just a moment-designed profile.

## Final Interpretation

Group 85 asks:

```text
Can the local goblin be lulled by a better-shaped exactness profile?
```

Goblin discipline:

```text
If the shape works, ask who carved it.
