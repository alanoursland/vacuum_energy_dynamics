# 71_common_boundary_generator_search — Plan

## Purpose

Group 71 searches for, or cleanly rejects, a real common boundary generator behind the Group 70 compatibility package.

Group 70 derived the exact compatibility requirements for the retained Group 69 structural route:

```text
sigma = 1
a_jump = -1
a_layer = -1
a_tail = -1
L_bulk = 0
L_gauge = 0
```

But Group 70 did **not** prove that these values are forced by geometry.

Group 71 should now test whether a shared boundary/covariant generator can force those signs, coefficients, and neutralities. If it cannot, the boundary-lift matching route should be downgraded from “theorem target” to “compatibility-only ansatz” or split into separate theorem targets.

This is not a parent-equation construction group.

## Group Name

```text
71_common_boundary_generator_search
```

## Central Question

```text
Is there a common boundary/covariant generator that forces the Group 70 matching package, or are the required signs and coefficients only selectable repair choices?
```

## Starting State

Imported from Group 70:

```text
boundary-lift matching compatibility requirements derived;
sigma = 1 required;
a_jump = -1 required;
a_layer = -1 required;
a_tail = -1 required;
L_bulk = 0 required;
L_gauge = 0 required;
boundary-lift matching theorem not proven;
parent divergence identity unproven;
recombination blocked.
```

## Desired Outcome

A useful result would be one of these:

### Route A: Common Generator Retained

```text
A candidate generator G_boundary is identified.

It produces:
  D_boundary = +B(G_boundary)
  L_boundary = -B(G_boundary)

and therefore:
  sigma = 1
  a_jump = a_layer = a_tail = -1

It also leaves:
  L_bulk = 0
  L_gauge = 0

or it cleanly separates those as still-open covariant-lift neutrality burdens.

Status:
  boundary-lift matching route retained as theorem target;
  parent divergence identity still unproven unless all burdens close.
```

### Route B: Common Generator Rejected

```text
No generator in the tested class can force the required signs and coefficients.

Status:
  boundary-lift matching route downgraded to compatibility-only;
  separate zero theorems or active-O construction become future alternatives;
  parent divergence identity remains unproven.
```

### Route C: Partial Generator

```text
A generator can force:
  sigma = 1
  a_jump = a_tail = -1

but cannot derive:
  a_layer = -1
  or L_bulk = 0
  or L_gauge = 0

Status:
  route split into sub-burdens;
  layer term or covariant-lift neutrality becomes the next blocker.
```

## What This Group May Do

Group 71 may:

```text
define candidate generator classes;
test orientation-forced anti-matching;
test component coefficient forcing;
test bulk/gauge leakage;
classify generator success, partial success, or failure;
downgrade routes that only work by selected coefficients;
choose the next route based on the failure mode.
```

## What This Group Must Not Do

Group 71 must not:

```text
write a parent field equation;
insert B_s/F_zeta;
revive or insert the transition response;
use diagnostic transition material as D_layer;
construct active O by label;
choose sigma=1 by convenience;
choose a_jump=a_layer=a_tail=-1 by convenience;
drop L_bulk or L_gauge by prose;
claim parent divergence identity proven unless all burdens are actually derived;
open recombination.
```

## Recommended Script Batch

```text
candidate_generator_search_problem.py
candidate_boundary_generator_requirements.py
candidate_orientation_forcing_test.py
candidate_component_forcing_test.py
candidate_bulk_gauge_leakage_test.py
candidate_generator_class_sieve.py
candidate_generator_route_classifier.py
candidate_group_71_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_generator_search_problem.py

Open Group 71 as a common-generator search.

It should restate:

```text
compatibility package known;
theorem not proven;
generator search required.
```

### 2. candidate_boundary_generator_requirements.py

Convert Group 70 compatibility into generator requirements.

A successful generator must force:

```text
D_boundary = +B
L_boundary = -B
```

where:

```text
B = D_jump + D_layer + D_tail
```

and must not produce uncontrolled:

```text
L_bulk
L_gauge
repair current
active O
diagnostic transition insertion
```

### 3. candidate_orientation_forcing_test.py

Test whether a candidate generator can force orientation anti-match:

```text
sigma = 1
```

Reject:

```text
sigma chosen by sign convention without derivation;
sigma chosen to cancel residual.
```

A useful result would classify:

```text
orientation forced;
orientation free;
orientation contradictory.
```

### 4. candidate_component_forcing_test.py

Test whether the generator forces:

```text
a_jump = -1
a_layer = -1
a_tail = -1
```

Reject any route where those coefficients are inserted manually.

A partial result should identify which component fails.

Special attention:

```text
a_layer
```

because `D_layer` is dangerous: it can easily become hidden diagnostic-transition insertion.

### 5. candidate_bulk_gauge_leakage_test.py

Test whether the generator introduces or eliminates:

```text
L_bulk
L_gauge
```

Possible classifications:

```text
bulk/gauge neutral:
  L_bulk = 0
  L_gauge = 0

bulk leakage:
  L_bulk != 0

gauge leakage:
  L_gauge != 0

mixed leakage:
  L_bulk + L_gauge can cancel only by repair-like choice
```

### 6. candidate_generator_class_sieve.py

Test broad generator classes.

Suggested classes:

```text
pure boundary generator;
boundary plus lift-boundary generator;
bulk-contaminated generator;
gauge-contaminated generator;
layer-dependent generator;
free-coefficient generator;
```

Likely classification:

```text
pure/common generator:
  retained if it forces signs and coefficients.

free-coefficient generator:
  rejected as repair.

bulk/gauge contaminated generator:
  rejected or deferred unless leakage is controlled.

layer-dependent generator:
  dangerous unless D_layer is derived physically and not diagnostic insertion.
```

### 7. candidate_generator_route_classifier.py

Classify final status.

Possible outcomes:

```text
GENERATOR_FOUND_STRONG:
  rare; would still require archive theorem support.

GENERATOR_PARTIAL:
  likely; route splits into remaining burdens.

GENERATOR_NOT_FOUND:
  boundary-lift matching downgraded to compatibility-only.

GENERATOR_FREE_PARAMETER_ONLY:
  rejected as repair-like.
```

### 8. candidate_group_71_status_summary.py

Speculative closing summary.

It should preserve:

```text
compatibility versus theorem distinction;
no parent equation;
no recombination;
no active O by label;
no diagnostic transition insertion.
```

## Expected Summary Shape

Likely result:

```text
Group 71 searches for a common boundary generator.
It tests whether the Group 70 compatibility package is forced or merely selectable.
If only free coefficients reproduce the package, the route is rejected as repair-like.
If a partial generator exists, the route splits into layer, bulk, or gauge burdens.
If no generator is found, the boundary-lift route downgrades to compatibility-only.
Parent divergence identity remains unproven.
Parent recombination remains blocked.
```

## Key Success Criteria

A successful generator must derive, not assume:

```text
sigma = 1
a_jump = -1
a_layer = -1
a_tail = -1
L_bulk = 0
L_gauge = 0
```

The strongest success would show:

```text
D_boundary and L_boundary are the same boundary object with opposite orientation.
```

The safest failure result would show:

```text
the matching package only appears when coefficients are selected by hand.
```

## Safe Handoff Options

Likely next groups:

```text
72_covariant_lift_neutrality_attempt
72_layer_term_legitimacy_audit
72_boundary_lift_route_downgrade
72_active_O_necessity_or_rejection
```

The next group should depend on Group 71’s result:

```text
If generator partial due to L_bulk/L_gauge:
  72_covariant_lift_neutrality_attempt

If generator partial due to D_layer:
  72_layer_term_legitimacy_audit

If generator not found:
  72_boundary_lift_route_downgrade

If O-free route fails but divergence target still demands closure:
  72_active_O_necessity_or_rejection
```

## Final Interpretation

Group 71 should answer a simple but important question:

```text
Are the Group 70 signs carved by geometry, or are they just knobs we turned until the leak stopped?
```

Goblin discipline:

```text
A key found in the lock is useful.
A key filed by hand to fit the lock is suspicious.
```
