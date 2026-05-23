# Group 85 Summary: Shape Family Payload Suppression Test

## Purpose

Group 85 tested whether the local payload obstruction found in Group 84 was universal or specific to the compact-support linear-skew family.

Group 84 showed:

```text
M0 = 0
W0 = 0
```

but:

```text
M1 != 0
M2 != 0
W1 != 0
W2 != 0
```

and more sharply:

```text
weighted neutrality requires c = 3ell/(2R);
dipole inertness requires c = 0;
M2 is independent of c.
```

So the linear-skew family could not provide local inertness.

Group 85 introduced a richer even quartic shape:

```text
P(y) = 1 + p y^2 + q y^4
```

inside the same compact-support exactness structure.

It asked:

```text
Can a richer compact-support exactness shape suppress the low-order local payload moments?
```

The answer is:

```text
yes, in a reduced finite-mode sense.
```

## Main Result

Group 85 is complete.

Stable result:

```text
even quartic shape family tested;

P = 1 - 12y^2 + 51y^4 found from M2=M4 constraints;

profile is regular/positive on [-1,1];

endpoint compact flux retained;

M0..M5 vanish;

W0..W3 vanish under quadratic measure;

local rho remains nonzero;

M6 and W4 remain nonzero;

Group 84 linear-skew obstruction is not universal;

shape origin remains open;

full local inertness not proven;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 85 makes real progress.

It shows that Group 84’s local payload obstruction was a limitation of the linear-skew family, not a universal obstruction to compact-support exactness.

The exactness route now has a richer status:

```text
globally useful;
weighted-total useful;
finite-mode local payload suppressible;
not all-order inert;
not pointwise zero;
not physically derived yet.
```

## Script-Level Analysis

### 1. Shape Suppression Problem

The opener correctly identifies the Group 84 limitation:

```text
linear skew cannot kill the quadratic payload.
```

It then asks a stronger question:

```text
can additional shape degrees of freedom suppress that payload?
```

That is the right way to make progress instead of repeating the obstruction.

### 2. Even Quartic Shape Family

The tested family is:

```text
P = 1 + p y^2 + q y^4
```

The script verifies:

```text
P even;
J odd;
rho even;
J(-1)=J(1)=0.
```

This is structurally useful. It preserves compact endpoint flux and automatically suppresses odd flat moments by parity.

### 3. Moment Constraint Solver

The generic moments include:

```text
M2 = -1024(p + q - 39)/45045
M4 = 2048(17p + q + 153)/765765
```

Solving:

```text
M2 = 0
M4 = 0
```

gives the unique normalized even quartic profile:

```text
p = -12
q = 51
```

so:

```text
P(y) = 1 - 12y^2 + 51y^4.
```

This is the first major positive result.

### 4. Suppressed Profile Validation

For:

```text
P = 1 - 12y^2 + 51y^4
```

the flux and remainder are:

```text
J = -30y(y - 1)^4(y + 1)^4(17y^4 - 10y^2 + 1)

rho = -30(y - 1)^3(y + 1)^3
      (221y^6 - 195y^4 + 39y^2 - 1)
```

Endpoint flux is retained:

```text
J(-1)=J(1)=0
```

Flat moments:

```text
M0 = M1 = M2 = M3 = M4 = M5 = 0
M6 = 65536/323323
```

The local field is still nonzero:

```text
rho(0) = -30
```

Interpretation:

```text
low-order flat payload moments are suppressed through fifth order;
local rho is not pointwise removed;
next obstruction appears at M6.
```

### 5. Weighted Payload Extension

Under the quadratic measure:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

the weighted moments are:

```text
W0 = W1 = W2 = W3 = 0
W4 = 65536 ell^2 / 323323
```

Interpretation:

```text
the suppression survives the quadratic measure through W3;
the next weighted obstruction is W4.
```

This directly improves the Group 84 weighted-local result.

### 6. Shape Admissibility and Repair Discriminator

The profile is regular and positive on the interval.

Writing:

```text
t = y^2
P(t) = 51t^2 - 12t + 1
```

the minimum occurs at:

```text
t = 2/17
```

with:

```text
P_min = 5/17
```

and:

```text
P(0)=1
P(1)=40.
```

This corrects the earlier plan expectation; the actual minimum is `5/17`, which is positive and clean.

The repair status is nuanced:

```text
not repair inside the reduced moment problem;
not full theory because shape origin is not derived.
```

### 7. Shape Suppression Route Classifier

The classifier records the right status:

```text
EVEN_QUARTIC_SUPPRESSION_PROFILE_FOUND
LOW_ORDER_FLAT_PAYLOAD_SUPPRESSED_THROUGH_M5
LOW_ORDER_WEIGHTED_PAYLOAD_SUPPRESSED_THROUGH_W3
NEXT_MOMENT_OBSTRUCTION_M6_W4
LOCAL_RHO_NONZERO_REMAINS
LINEAR_SKEW_OBSTRUCTION_NOT_UNIVERSAL
SHAPE_ORIGIN_OPEN
FULL_LOCAL_INERTNESS_NOT_PROVEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

This is the correct carry-forward state.

### 8. Group Status Summary

The final summary preserves the core lesson:

```text
the richer shape family overcomes the Group 84 low-order obstruction,
but finite-mode suppression is not full local inertness.
```

## Final Status Ledger

```text
shape_family:
  EVEN_QUARTIC

suppression_profile:
  P(y) = 1 - 12y^2 + 51y^4

profile_origin:
  MOMENT_DERIVED
  NOT_GEOMETRY_DERIVED

profile_regular:
  YES

P_min:
  5/17 at y^2 = 2/17

endpoint_flux:
  J(-1)=J(1)=0

flat_moments:
  M0..M5 = 0
  M6 = 65536/323323

weighted_moments:
  W0..W3 = 0
  W4 = 65536 ell^2 / 323323

local_rho:
  NONZERO
  rho(0) = -30

linear_skew_obstruction:
  NOT_UNIVERSAL

finite_mode_payload_suppression:
  STRENGTHENED

full_local_inertness:
  NOT_PROVEN

shape_origin:
  OPEN

higher_moment_hierarchy:
  OPEN

covariant_lift:
  OPEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 85 rejects:

```text
linear-skew obstruction as universal;
finite-mode suppression as all-order inertness;
moment-derived shape as physical derivation;
rho moment suppression as rho(y)=0;
shape test as parent equation;
recombination opening.
```

## Strategic Interpretation

Group 85 meaningfully improves the exactness route.

After Group 84, the route looked locally dangerous. After Group 85, the route looks more subtle:

```text
local payload danger is real for simple profiles;
but richer profiles can suppress low-order payload moments.
```

This means the exactness route should not be abandoned on the basis of the Group 84 obstruction. Instead, the project should investigate whether there is a principled reason for the successful profile.

The central new question is:

```text
Why P(y) = 1 - 12y^2 + 51y^4?
```

If the profile is geometrically or variationally forced, the exactness route becomes much stronger. If the profile is merely engineered to kill moments, then it remains a clever reduced-class compatibility construction.

## Recommended Next Group

Best next group:

```text
86_shape_origin_geometry_derivation
```

Purpose:

```text
Search for a geometric, variational, orthogonality, or minimal-payload principle that forces
P(y)=1-12y^2+51y^4.
```

Other viable routes:

```text
86_moment_hierarchy_closure_test
86_covariant_payload_suppression_lift
86_payload_projection_operator_necessity
86_parent_blocker_refresh
```

My recommendation is:

```text
86_shape_origin_geometry_derivation
```

because Group 85 found a working shape, and the next question is whether it is carved by structure or filed by hand.

## Final Interpretation

Group 85 found a better-shaped key.

```text
The linear key broke on the quadratic tooth.
The quartic key turned several tumblers.
But the last teeth still catch.
Now we ask who cut the key.
```
