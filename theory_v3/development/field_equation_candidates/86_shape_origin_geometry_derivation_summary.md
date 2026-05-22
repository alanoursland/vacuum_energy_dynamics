# Group 86 Summary: Shape Origin Geometry Derivation

## Purpose

Group 86 tested whether the Group 85 profile

```text
P(y) = 1 - 12y^2 + 51y^4
```

has a structural origin inside the reduced exactness/payload-suppression model.

Group 85 showed that this profile is effective:

```text
M0..M5 = 0
W0..W3 = 0
```

while:

```text
rho(0) != 0
M6 != 0
W4 != 0
```

But Group 85 left the profile origin open.

Group 86 asked:

```text
Was the quartic key carved by the reduced lock,
or filed by hand after seeing the tumblers?
```

The answer is:

```text
inside the reduced model, the profile is structurally forced.
```

## Main Result

Group 86 is complete.

Stable result:

```text
moment map from even shape coefficients to payload moments derived;

degree 0 and degree 2 obstruction derived;

degree 4 is minimal for killing M2 and M4;

P = 1 - 12y^2 + 51y^4 uniquely derived in normalized even quartic family;

same P is unique zero-action minimizer of A = M2^2 + M4^2;

W0..W3 weighted suppression follows from M0..M5 flat moment block;

shape origin strengthened inside reduced model;

full physical/covariant origin remains open;

local rho nonzero remains;

higher moments M6/W4 remain;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 86 changes the status of the Group 85 shape.

Before Group 86, the shape was:

```text
effective but moment-derived.
```

After Group 86, it is:

```text
structurally derived inside the reduced finite-mode payload-suppression problem.
```

That is real progress.

The profile is not arbitrary inside the reduced model. It is forced by a combination of:

```text
minimal degree;
quartic uniqueness;
payload-action minimization;
weighted consistency from a flat moment block.
```

## Script-Level Analysis

### 1. Shape Origin Problem

The opener correctly imports Group 85’s result and targets the open question:

```text
why P = 1 - 12y^2 + 51y^4?
```

It keeps the scope honest:

```text
reduced model origin;
not full physical geometry;
not all-order inertness;
not parent equation.
```

### 2. Moment Map From Shape Coefficients

For:

```text
P = 1 + a1 y^2 + a2 y^4 + a3 y^6
```

the moment map is:

```text
M0 = 0

M2 = -1024*(17*a1 + 17*a2 + 9*a3 - 663)/765765

M4 = 2048*(323*a1 + 19*a2 - 21*a3 + 2907)/14549535

M6 = 1024*(209*a1 + 49*a2 + 9*a3 + 969)/4849845
```

Interpretation:

```text
payload suppression is a linear map from shape coefficients to moments.
```

This gives the reduced origin problem a linear-algebra structure.

### 3. Minimal Degree Obstruction

Degree 0 gives:

```text
M2 = 1024/1155
M4 = 2048/5005
```

so constant shape fails.

Degree 2 gives:

```text
M2 = -1024*(p - 39)/45045
M4 = 2048*(p + 9)/45045
```

Killing `M2` requires:

```text
p = 39
```

but then:

```text
M4 = 32768/15015
```

There is no simultaneous degree-2 solution.

Interpretation:

```text
degree 4 is minimal for suppressing M2 and M4 among normalized even polynomial shapes.
```

### 4. Quartic Uniqueness Theorem

For:

```text
P = 1 + p y^2 + q y^4
```

the relevant moments are:

```text
M2 = -1024*(p + q - 39)/45045

M4 = 2048*(17p + q + 153)/765765
```

Solving:

```text
M2 = 0
M4 = 0
```

gives:

```text
p = -12
q = 51
```

so:

```text
P = 1 - 12y^2 + 51y^4.
```

Interpretation:

```text
the Group 85 profile is unique in the normalized even quartic family.
```

### 5. Payload Action Minimizer

The reduced action is:

```text
A(p,q) = M2^2 + M4^2
```

The unique critical point is:

```text
p = -12
q = 51
```

and:

```text
A = 0
```

Since `A` is a sum of squares and reaches zero, this profile is the unique zero-action minimizer.

Interpretation:

```text
the profile has a reduced variational origin:
it minimizes low-order payload leakage.
```

This is not yet a physical action, but it is stronger than moment fitting.

### 6. Weighted Consistency From Flat Block

For:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

the weighted moments are:

```text
W0 = R^2 M0 + 2Rell M1 + ell^2 M2

W1 = R^2 M1 + 2Rell M2 + ell^2 M3

W2 = R^2 M2 + 2Rell M3 + ell^2 M4

W3 = R^2 M3 + 2Rell M4 + ell^2 M5
```

Therefore:

```text
M0..M5 = 0
```

implies:

```text
W0..W3 = 0.
```

Interpretation:

```text
weighted suppression from Group 85 was not separately tuned;
it follows from the flat moment block under the quadratic measure.
```

### 7. Shape Origin Route Classifier

The classifier records the correct carry-forward statuses:

```text
MOMENT_MAP_DERIVED
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

### 8. Group Status Summary

The final summary is conceptually sound. Group 86 derives a reduced structural origin, not a full physical/covariant origin.

## Final Status Ledger

```text
moment_map:
  DERIVED

minimal_degree:
  DEGREE_4_MINIMAL_FOR_M2_M4_SUPPRESSION

quartic_profile:
  UNIQUE_NORMALIZED_EVEN_QUARTIC

profile:
  P(y) = 1 - 12y^2 + 51y^4

payload_action:
  A = M2^2 + M4^2

payload_action_minimizer:
  UNIQUE_ZERO_ACTION_MINIMIZER

weighted_consistency:
  W0..W3 FOLLOW_FROM M0..M5 FOR QUADRATIC_MEASURE

shape_origin:
  STRENGTHENED_IN_REDUCED_MODEL

physical_geometric_origin:
  OPEN

local_rho:
  NONZERO_REMAINS

higher_moments:
  M6/W4 REMAIN

full_inertness:
  NOT_PROVEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 86 rejects:

```text
profile arbitrary inside the reduced model;
moment-derived profile as full physical geometry;
reduced payload action as physical action;
finite-mode suppression as all-order inertness;
shape origin as parent equation;
recombination opening.
```

## Strategic Interpretation

Group 86 strengthens the exactness/payload-suppression route.

The route now has a coherent reduced progression:

```text
Group 82:
  exactness gives flat total neutrality.

Group 83:
  weighted skew is derived from measure-gradient orthogonality.

Group 84:
  linear-skew local inertness fails.

Group 85:
  richer quartic shape suppresses low-order payload moments.

Group 86:
  quartic shape is structurally forced inside the reduced payload-suppression problem.
```

This is a real arc. It does not close the theory, but it turns a previously ad hoc-looking profile into the minimal reduced payload-suppression shape.

## Recommended Next Group

Best next group:

```text
87_moment_hierarchy_closure_test
```

Reason:

```text
Group 86 suggests a hierarchy:
higher-degree even profiles may suppress larger moment blocks.
```

The next technical question is whether:

```text
degree 2N profiles uniquely suppress M2..M(2N),
and whether weighted suppression follows by moment-block inheritance.
```

Other viable next routes:

```text
87_covariant_payload_suppression_lift
87_shape_variational_physical_origin
87_payload_projection_operator_necessity
87_parent_blocker_refresh
```

## Final Interpretation

Group 86 cut the key more cleanly.

```text
The quartic key was not filed by panic.
Inside this little lock, the tumblers demand it.
But the lock is still a model,
and the big door has not opened.
```
