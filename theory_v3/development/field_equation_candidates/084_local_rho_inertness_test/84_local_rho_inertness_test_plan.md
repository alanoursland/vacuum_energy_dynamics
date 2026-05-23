# 84_local_rho_inertness_test — Plan

## Purpose

Group 84 tests the biggest physical danger left after Groups 82–83:

```text
rho is exact/weighted-neutral in a reduced sense,
but rho remains locally nonzero.
```

Group 82 derived flat integrated neutrality for a concrete compact-support exact remainder and showed local `rho` is nonzero. Group 83 strengthened the weighted route by deriving the skew:

```text
c = 3 ell/(2R)
```

from measure-gradient orthogonality in the reduced weighted-exactness class.

But neither group proved that local nonzero `rho` is physically inert.

Group 84 now tests whether the derived skewed local remainder is invisible to a low-order payload probe basis. This is a concrete finite-mode inertness test, not a full covariant payload theorem.

## Group Name

```text
84_local_rho_inertness_test
```

## Central Question

```text
After the Group 83 weighted-neutral skew is imposed, is local nonzero rho inert to admissible low-order payload probes,
or does local payload obstruction remain?
```

## Starting State

Imported from Group 83:

```text
measure-gradient orthogonality derived;
weighted skew c = 3ell/(2R) derived in reduced class;
skew unique within linear-skew compact-support family;
repair concern reduced inside the reduced model;
full covariant theorem remains open;
local rho nonzero remains;
payload inertness remains open;
parent divergence identity unproven;
recombination blocked.
```

## Concrete Object

Use the Group 82/83 compact-support family:

```text
y in [-1, 1]
f = (1 - y^2)^3
w = (1 - y^2)^2
Xi = f * (1 + c y)
J = w * dXi/dy
rho = dJ/dy
```

Then impose the Group 83 derived skew:

```text
c = 3ell/(2R)
```

so:

```text
rho_skew = rho | c = 3ell/(2R)
```

## Payload Probe Basis

Use a minimal low-order probe basis:

```text
P0 = 1       uniform/global source probe
P1 = y       dipole/gradient probe
P2 = y^2     quadratic/curvature-width probe
```

This is not a full physical payload basis, but it is a meaningful reduced local-inertness test.

Define moments:

```text
M_n = ∫ y^n rho dy
```

A local inertness candidate would need these low-order moments to vanish or be physically excluded.

## Desired Outcome

A useful result would be one of these.

### Route A: Local Inertness Supported

The derived skew satisfies:

```text
M0 = 0
M1 = 0
M2 = 0
```

and weighted probe moments also vanish.

Status:

```text
local inertness route strengthened.
```

### Route B: Partial Inertness

The derived skew satisfies:

```text
M0 = 0
```

but leaves:

```text
M1 != 0
or M2 != 0
```

Status:

```text
global source neutrality only;
local payload inertness not established.
```

### Route C: Obstruction

The test finds a structural obstruction:

```text
M2 != 0 independent of c
```

or:

```text
weighted neutrality requires c != 0
but dipole inertness requires c = 0
```

Status:

```text
local inertness fails in the tested finite-mode class.
```

## Expected Likely Result

The likely result is Route C:

```text
M0 = 0;
M1 != 0 after weighted skew;
M2 != 0 independent of c;
weighted neutrality and dipole inertness are incompatible unless ell=0;
local payload inertness remains obstructed in this reduced finite-mode test.
```

This would be real progress because it says the exactness route has a local payload problem, not just an untested obligation.

## What This Group May Do

Group 84 may:

```text
define a low-order payload probe basis;
compute flat payload moments;
compute weighted payload moments;
test whether skew can satisfy weighted neutrality and local dipole inertness simultaneously;
test whether quadratic payload moment can be killed by linear skew;
classify local inertness as supported, partial, or obstructed.
```

## What This Group Must Not Do

Group 84 must not:

```text
claim full physical payload theorem from finite-mode test;
claim covariant closure;
claim local rho = 0;
adopt an axiom;
write a parent field equation;
insert B_s/F_zeta;
solve D_layer legitimacy;
construct active O by label;
open recombination.
```

## Recommended Script Batch

```text
candidate_local_inertness_problem.py
candidate_payload_probe_basis.py
candidate_flat_probe_moment_test.py
candidate_weighted_probe_moment_test.py
candidate_skew_inertness_tradeoff_test.py
candidate_quadratic_payload_obstruction.py
candidate_local_inertness_route_classifier.py
candidate_group_84_status_summary.py
order.txt
```

## Script Intent

### 1. candidate_local_inertness_problem.py

Open Group 84 as a local inertness test.

It should restate:

```text
weighted skew derived;
local rho nonzero;
payload inertness open;
finite-mode test only.
```

### 2. candidate_payload_probe_basis.py

Define the low-order payload probes:

```text
1, y, y^2
```

and the moment test:

```text
M_n = ∫ y^n rho dy
```

Explain the interpretation:

```text
M0: global/source neutrality
M1: dipole/gradient sensitivity
M2: quadratic/width/curvature sensitivity
```

### 3. candidate_flat_probe_moment_test.py

Compute moments for the derived skew:

```text
c = 3ell/(2R)
```

Expected:

```text
M0 = 0
M1 = -512ell/(1155R)
M2 = 1024/1155
```

Interpretation:

```text
flat source/global charge vanishes;
dipole and quadratic local probes do not.
```

### 4. candidate_weighted_probe_moment_test.py

Compute measure-weighted moments:

```text
W_n = ∫ mu y^n rho dy
```

with:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

Expected:

```text
W0 = 0 by Group 83 skew;
W1 != 0;
W2 != 0.
```

Interpretation:

```text
weighted neutrality of total charge does not imply weighted inertness to local probes.
```

### 5. candidate_skew_inertness_tradeoff_test.py

Use generic `c` and compare:

```text
weighted neutrality condition:
  c = 3ell/(2R)

dipole inertness condition:
  c = 0
```

Expected:

```text
incompatible unless ell = 0.
```

Interpretation:

```text
the skew that fixes weighted charge creates/retains dipole sensitivity.
```

### 6. candidate_quadratic_payload_obstruction.py

Use generic `c` and show:

```text
M2 = 1024/1155
```

independent of `c`.

Interpretation:

```text
no linear-skew choice kills the quadratic payload moment.
```

This is the strongest obstruction.

### 7. candidate_local_inertness_route_classifier.py

Classify:

```text
GLOBAL_SOURCE_NEUTRALITY_RETAINED
DIPOLE_PAYLOAD_NONZERO
QUADRATIC_PAYLOAD_NONZERO
WEIGHTED_TOTAL_NEUTRALITY_RETAINED
WEIGHTED_LOCAL_PAYLOAD_NONZERO
WEIGHTED_NEUTRALITY_DIPOLE_INERTNESS_TRADEOFF
LINEAR_SKEW_CANNOT_KILL_QUADRATIC_PAYLOAD
LOCAL_INERTNESS_OBSTRUCTED_IN_FINITE_MODE_TEST
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. candidate_group_84_status_summary.py

Close the group.

Expected result:

```text
local inertness not established;
finite-mode payload obstruction found;
rho exactness remains globally/weighted useful but locally dangerous;
next route requires stronger shape family, payload projection, or physical interpretation of local rho.
```

## Key Success Criteria

Group 84 must earn a real result.

Expected useful theorem-level statements:

```text
For the Group 83 skewed compact-support exact rho:
  ∫rho dy = 0
  ∫y rho dy = -512ell/(1155R)
  ∫y^2 rho dy = 1024/1155
```

and:

```text
For generic linear skew:
  dipole inertness requires c = 0
  weighted neutrality requires c = 3ell/(2R)
  quadratic moment M2 = 1024/1155 independent of c
```

## Safe Handoff Options

Likely next groups:

```text
85_shape_family_payload_suppression_test
85_payload_projection_operator_necessity
85_covariant_exactness_lift
85_parent_blocker_refresh
```

If local payload obstruction remains strong, the best next group may be:

```text
85_shape_family_payload_suppression_test
```

to test whether a richer shape family can satisfy weighted neutrality and suppress low-order payload moments without repair.

## Final Interpretation

Group 84 asks:

```text
Does the local goblin still bite?
```

Goblin discipline:

```text
A vanished total charge is not a sleeping local goblin.
Poke it with y and y^2.
