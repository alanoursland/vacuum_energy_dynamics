# 83_weighted_exactness_geometry_derivation — Plan

## Purpose

Group 83 tries to make real progress on the weighted-neutrality skew found in Group 82.

Group 82 tested a concrete exact/divergence candidate:

```text
rho = dJ/dy
J = (1 - y^2)^2 * d/dy[(1 - y^2)^3 * (1 + c y)]
```

It found:

```text
flat integrated neutrality = 0
local rho != 0
weighted charge = -1024*ell*(2*R*c - 3*ell)/3465
weighted neutrality requires c = 3*ell/(2R)
```

But Group 82 only solved for the skew. It did not derive the skew geometrically.

Group 83 tests whether that skew can be derived from a geometric exactness condition.

The concrete candidate is a measure-gradient orthogonality condition:

```text
Q_mu = ∫_{-1}^{1} mu(y) rho(y) dy
rho = dJ/dy
J(-1)=J(1)=0

Q_mu = - ∫_{-1}^{1} mu'(y) J(y) dy
```

Weighted neutrality is therefore equivalent to:

```text
∫ mu'(y) J(y) dy = 0
```

For:

```text
mu(y) = R^2 + 2 R ell y + ell^2 y^2
```

and the skewed flux family, Group 83 tests whether this condition forces:

```text
c = 3 ell/(2R)
```

from parity and geometric measure structure rather than arbitrary cancellation.

This is still a reduced-class theorem attempt, not full covariant closure.

## Group Name

```text
83_weighted_exactness_geometry_derivation
```

## Central Question

```text
Is the weighted-neutrality skew c = 3ell/(2R) forced by the geometry of the weighted exactness problem,
or is it still just a selected repair coefficient?
```

## Starting State

Imported from Group 82:

```text
flat exact neutrality derived in reduced compact-support class;
local rho remains nonzero;
weighted/geometric neutrality is not automatic;
skew condition for weighted neutrality exists as compatibility;
skew must be derived geometrically, not chosen;
payload inertness remains open;
parent divergence identity unproven;
recombination blocked.
```

## Concrete Geometric Route

Use the same reduced layer coordinate:

```text
y in [-1, 1]
```

Same compact support envelope:

```text
f(y) = (1 - y^2)^3
w(y) = (1 - y^2)^2
```

Skewed potential:

```text
Xi(y) = f(y) * (1 + c y)
```

Flux:

```text
J = w * dXi/dy
```

Measure:

```text
mu = R^2 + 2 R ell y + ell^2 y^2
```

The integration-by-parts identity gives:

```text
∫ mu rho dy = [mu J]_{-1}^{1} - ∫ mu' J dy
```

Endpoint compact support gives:

```text
[mu J]_{-1}^{1} = 0
```

so weighted neutrality is:

```text
∫ mu' J dy = 0
```

Decompose:

```text
J = J0 + c J1
```

where:

```text
J0 = w f'
J1 = w (f + y f')
```

Then parity gives:

```text
∫ J0 dy = 0
∫ y J1 dy = 0
```

and only two terms survive:

```text
∫ mu' J dy
  = 2 R ell c ∫ J1 dy + 2 ell^2 ∫ y J0 dy
```

So:

```text
c = - ell * ∫ y J0 dy / (R * ∫ J1 dy)
```

For this concrete shape:

```text
∫ J1 dy = 1024/3465
∫ y J0 dy = -512/1155
```

therefore:

```text
c = 3 ell/(2R)
```

## Desired Outcome

A useful result is:

```text
The skew c = 3ell/(2R) is derived inside the reduced weighted-exactness class from:
  compact endpoint flux;
  measure-gradient orthogonality;
  parity decomposition of flux;
  the chosen envelope f,w.

Status:
  weighted skew is no longer merely solved-for in Group 82;
  it is forced by the reduced weighted exactness condition.

Remaining limitations:
  reduced 1D class only;
  still depends on chosen f,w family;
  not full covariant lift theorem;
  local rho nonzero;
  payload inertness open;
  parent divergence/recombination blocked.
```

## What This Group May Do

Group 83 may:

```text
derive the integration-by-parts weighted exactness identity;
decompose flux into parity components;
derive c from surviving parity terms;
test uniqueness of c within the linear-skew family;
test thin-limit scaling c ~ ell/R;
classify whether this removes repair-paint concern inside the reduced class.
```

## What This Group Must Not Do

Group 83 must not:

```text
claim full covariant weighted neutrality;
claim local rho = 0;
claim payload inertness;
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_weighted_skew_problem.py
candidate_measure_gradient_identity.py
candidate_flux_parity_decomposition.py
candidate_geometric_skew_derivation.py
candidate_uniqueness_and_scaling_test.py
candidate_repair_discriminator.py
candidate_weighted_exactness_route_classifier.py
candidate_group_83_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_weighted_skew_problem.py

Open Group 83 as a weighted-skew derivation attempt.

It should restate:

```text
Group 82 found c = 3ell/(2R) as compatibility;
Group 83 tests whether that c is forced by weighted exactness geometry.
```

### 2. candidate_measure_gradient_identity.py

Derive:

```text
∫ mu rho dy = [mu J] - ∫ mu' J dy
```

and with compact endpoint flux:

```text
Q_mu = -∫ mu' J dy
```

Interpretation:

```text
weighted neutrality is measure-gradient orthogonality of the flux.
```

### 3. candidate_flux_parity_decomposition.py

Decompose:

```text
J = J0 + c J1
J0 = w f'
J1 = w(f + y f')
```

Show parity:

```text
J0 odd
J1 even
mu' = 2Rell + 2ell^2 y
```

Only:

```text
2Rell c ∫J1
2ell^2 ∫yJ0
```

survive.

### 4. candidate_geometric_skew_derivation.py

Compute the integrals:

```text
A = ∫J1 dy = 1024/3465
B = ∫yJ0 dy = -512/1155
```

Then derive:

```text
c = -ell B/(R A) = 3ell/(2R)
```

This is the main theorem attempt.

### 5. candidate_uniqueness_and_scaling_test.py

Show the condition is linear in `c`, so the solution is unique in this linear-skew family.

Show scaling:

```text
c = O(ell/R)
c -> 0 as ell/R -> 0
```

Interpretation:

```text
skew is a geometric finite-thickness correction, not arbitrary constant.
```

### 6. candidate_repair_discriminator.py

Classify whether the skew is repair.

Expected result:

```text
Not repair inside the reduced weighted-exactness model if the model assumptions are accepted.
Still not full theorem because f,w and reduced measure are not derived covariantly.
```

### 7. candidate_weighted_exactness_route_classifier.py

Classify:

```text
WEIGHTED_SKEW_DERIVED_IN_REDUCED_CLASS
MEASURE_GRADIENT_ORTHOGONALITY_DERIVED
UNIQUE_LINEAR_SKEW
REDUCED_CLASS_ONLY
LOCAL_RHO_NONZERO_REMAINS
PAYLOAD_INERTNESS_OPEN
COVARIANT_LIFT_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. candidate_group_83_status_summary.py

Close the group.

Expected result:

```text
the Group 82 skew is derived in the reduced weighted-exactness class;
the route is strengthened;
local/payload/covariant burdens remain.
```

## Key Success Criteria

The group must earn a real mathematical statement:

```text
Within the tested compact-support linear-skew family, weighted exactness with measure mu forces c = 3ell/(2R).
```

And preserve the caution:

```text
This is not full covariant closure.
This does not imply local rho = 0.
This does not prove payload inertness.
```

## Safe Handoff Options

Likely next groups:

```text
84_local_rho_inertness_test
84_covariant_exactness_lift
84_shape_family_robustness_test
84_parent_blocker_refresh
```

If the user wants to keep making technical progress, a good next group is probably:

```text
84_local_rho_inertness_test
```

because weighted neutrality is now stronger, but local nonzero rho and payload inertness remain.

## Final Interpretation

Group 83 asks:

```text
Did geometry pay for the skew?
```

Goblin discipline:

```text
A coefficient solved from a leak is suspicious.
A coefficient forced by the measure is a better coin.
Still bite it.
```
