# 82_rho_exactness_concrete_test — Plan

## Purpose

Group 82 is a real theorem attempt on the `rho` obstruction, not another ledger.

Group 81 built the concrete-input handoff gate and said future theorem work requires a real object. Group 82 supplies a concrete candidate object for the `rho` route:

```text
rho = dJ/dy
```

with a compact-support flux `J` on a reduced layer coordinate:

```text
y in [-1, 1]
```

The goal is to test whether an exact/divergence remainder can be treated as nonphysical or neutral in a controlled class.

The group should not claim full covariant closure. It should test a concrete exactness scaffold hard enough to learn something:

```text
flat integral neutrality may be derivable;
local rho may remain nonzero;
weighted-measure neutrality may fail unless extra structure is supplied;
physical payload must still be excluded.
```

This is not an axiom-adoption group and not a parent-equation group.

## Group Name

```text
82_rho_exactness_concrete_test
```

## Central Question

```text
Can a concrete exact/divergence form for rho remove the lift remainder,
or does it only prove a weaker global-neutrality result while leaving local/weighted/physical obstructions?
```

## Starting State

Imported from Group 81:

```text
future work requires a real object;
rho route accepts an exactness operator, boundary divergence object, inertness/no-payload theorem candidate, physical remainder test, and payload filter;
rho = 0 by assertion, exact by label, dropped rho, no-payload by wish, and boundary-exact by name only are rejected;
parent divergence identity unproven;
recombination blocked.
```

## Concrete Candidate

Use a reduced layer coordinate:

```text
y in [-1, 1]
```

Define a compact-support even window:

```text
w(y) = (1 - y^2)^2
```

Use a smooth test potential:

```text
Xi(y) = (1 - y^2)^3 * (1 + c y)
```

Define flux and exact remainder:

```text
J(y) = w(y) * dXi/dy
rho_exact(y) = dJ/dy
```

Endpoint flux should vanish:

```text
J(-1) = J(1) = 0
```

So the flat integrated charge should close:

```text
∫_{-1}^{1} rho_exact dy = 0
```

But a nonconstant geometric measure:

```text
mu(y) = R^2 + 2 R ell y + ell^2 y^2
```

may produce a weighted charge:

```text
∫ mu(y) rho_exact(y) dy
```

that does not vanish automatically.

## Desired Outcome

A useful result should be one of these.

### Route A: Exactness Strongly Retained

The concrete exact form gives:

```text
flat charge = 0
weighted charge = 0
local rho either inert or payload-free
```

without tuning.

Status:

```text
rho exactness route strengthened.
```

### Route B: Partial Exactness

The concrete exact form gives:

```text
flat charge = 0
local rho != 0
weighted charge may be nonzero unless additional skew/measure condition is supplied
```

Status:

```text
exactness route partially validated but not sufficient for full lift closure.
```

### Route C: Exactness Fails

The concrete exact form fails even flat neutrality or creates forbidden payload.

Status:

```text
rho exactness route obstructed in this tested class.
```

## Expected Likely Result

The likely result is Route B:

```text
compact-support exactness proves flat integrated neutrality;
rho remains locally nonzero;
weighted/geometric neutrality imposes an extra condition;
payload inertness remains a separate theorem burden;
parent divergence and recombination remain blocked.
```

That would be real progress because it distinguishes:

```text
global exact neutrality
from
local lift-remainder removal
from
weighted/covariant neutrality
from
physical inertness.
```

## What This Group May Do

Group 82 may:

```text
construct a concrete exactness operator;
derive endpoint flux neutrality;
derive flat integrated neutrality;
test local nonzero rho;
test weighted measure neutrality;
solve for a skew condition if one exists;
test physical payload channels;
classify whether exactness is strong, partial, or insufficient.
```

## What This Group Must Not Do

Group 82 must not:

```text
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
erase rho by assertion;
call exactness local zero unless proven;
drop weighted charge by prose;
construct active O by label;
claim parent divergence identity proven;
open recombination.
```

## Recommended Script Batch

```text
candidate_rho_exactness_problem.py
candidate_exact_operator_requirements.py
candidate_compact_support_exact_remainder.py
candidate_local_remainder_nonzero_test.py
candidate_weighted_measure_neutrality_test.py
candidate_skew_condition_for_weighted_neutrality.py
candidate_payload_inertness_filter.py
candidate_rho_exactness_route_classifier.py
candidate_group_82_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_rho_exactness_problem.py

Open Group 82 as a concrete rho exactness test.

It should restate:

```text
Group 81 requires real input;
Group 82 supplies a concrete exact/divergence candidate;
no parent/recombination.
```

### 2. candidate_exact_operator_requirements.py

State requirements for exactness to matter:

```text
rho = dJ/dy;
J endpoints vanish for flat global neutrality;
weighted neutrality must be checked separately;
local nonzero rho is not automatically harmless;
payload inertness must be tested.
```

### 3. candidate_compact_support_exact_remainder.py

Construct:

```text
w = (1-y^2)^2
Xi = (1-y^2)^3
J = w * dXi/dy
rho = dJ/dy
```

Test:

```text
J(-1)=J(1)=0
∫rho dy = 0
```

This should prove flat integrated neutrality in the reduced class.

### 4. candidate_local_remainder_nonzero_test.py

Show that the same `rho` is generally not identically zero.

This separates:

```text
global exact neutrality
from
local lift residual removal.
```

### 5. candidate_weighted_measure_neutrality_test.py

Use:

```text
mu = R^2 + 2 R ell y + ell^2 y^2
```

Test:

```text
∫mu*rho dy
```

Likely result:

```text
weighted charge not automatically zero.
```

### 6. candidate_skew_condition_for_weighted_neutrality.py

Use the skewed potential:

```text
Xi = (1-y^2)^3 * (1 + c y)
```

Test whether a `c` exists such that:

```text
∫mu*rho dy = 0
```

If yes, classify it as a compatibility condition unless `c` is derived geometrically.

### 7. candidate_payload_inertness_filter.py

Test whether a nonzero local `rho` would carry source, trace, mass, or divergence payload.

Safe route requires all payload channels absent/inert by theorem.

### 8. candidate_rho_exactness_route_classifier.py

Classify:

```text
FLAT_EXACT_NEUTRALITY_DERIVED_IN_REDUCED_CLASS
LOCAL_RHO_NOT_ZERO
WEIGHTED_NEUTRALITY_EXTRA_CONDITION
PAYLOAD_INERTNESS_OPEN
RHO_EXACTNESS_PARTIAL
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 9. candidate_group_82_status_summary.py

Close the group.

Expected result:

```text
concrete exactness gives flat integrated neutrality;
does not by itself give local zero or weighted/covariant neutrality;
rho exactness route strengthened but still partial;
parent/recombination blocked.
```

## Key Success Criteria

A successful Group 82 must make at least one real mathematical statement.

Expected useful theorem-level statement in reduced class:

```text
If rho = dJ/dy and J(-1)=J(1)=0, then ∫_{-1}^{1} rho dy = 0.
```

Expected caution:

```text
This does not imply rho(y)=0.
This does not imply weighted/covariant neutrality.
This does not imply physical inertness.
```

## Safe Handoff Options

Likely next groups:

```text
83_weighted_exactness_geometry_derivation
83_local_rho_inertness_test
83_covariant_exactness_lift
83_parent_blocker_refresh
```

If weighted neutrality requires a skew coefficient, the best next group is probably:

```text
83_weighted_exactness_geometry_derivation
```

because it asks whether the required skew is derived by geometry or merely chosen.

## Final Interpretation

Group 82 asks:

```text
Does exactness pay any of the rho debt?
```

Goblin discipline:

```text
A vanished integral is a coin.
A vanished local field is a different coin.
Do not spend one as the other.
```
