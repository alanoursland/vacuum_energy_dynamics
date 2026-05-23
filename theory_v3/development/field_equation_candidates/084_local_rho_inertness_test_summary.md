# Group 84 Summary: Local Rho Inertness Test

## Purpose

Group 84 tested the biggest physical danger left after Groups 82–83.

Groups 82–83 established that the exactness route is globally useful:

```text
flat integrated neutrality derived;
weighted total neutrality restored by c = 3ell/(2R);
the skew is derived from measure-gradient orthogonality in the reduced class.
```

But local `rho` remained nonzero.

Group 84 asked:

```text
After the Group 83 weighted-neutral skew is imposed,
is local nonzero rho inert to low-order payload probes?
```

The answer is:

```text
no, not in the tested finite-mode class.
```

## Main Result

Group 84 is complete.

Stable result:

```text
low-order payload probe basis defined;

global flat source moment M0 = 0 retained;

dipole moment M1 nonzero after Group 83 skew;

quadratic moment M2 nonzero and independent of c;

weighted total moment W0 = 0 retained;

weighted local moments W1/W2 nonzero;

weighted neutrality and dipole inertness require incompatible c unless ell = 0;

linear skew cannot kill quadratic payload moment;

local inertness obstructed in finite-mode test;

rho exactness remains globally useful but locally payload-dangerous;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 84 is real progress because it turns a vague remaining burden:

```text
payload inertness remains open
```

into a concrete obstruction:

```text
the Group 83 skewed rho is visible to low-order local payload probes.
```

The exactness route now has a very clear status:

```text
good for total neutrality;
bad for local inertness in the tested family.
```

## Script-Level Analysis

### 1. Local Inertness Problem

The opener correctly targets the live risk:

```text
local rho nonzero remains;
payload inertness remains open.
```

It also keeps the scope honest:

```text
finite-mode inertness test only;
not full covariant payload theorem.
```

This was the right next move after Group 83.

### 2. Payload Probe Basis

The probe basis is:

```text
P0 = 1
P1 = y
P2 = y^2
```

with moments:

```text
M_n = ∫ y^n rho dy
```

Interpretation:

```text
M0: global/source neutrality
M1: dipole/gradient sensitivity
M2: quadratic/width/curvature sensitivity
```

This is a good minimal basis because it tests whether the exact remainder is visible to the simplest local payload channels.

### 3. Flat Probe Moment Test

With the Group 83 skew:

```text
c = 3ell/(2R)
```

the flat moments are:

```text
M0 = 0
M1 = -512ell/(1155R)
M2 = 1024/1155
```

Interpretation:

```text
global neutrality survives;
dipole and quadratic local probes detect rho.
```

This is the first payload obstruction.

### 4. Weighted Probe Moment Test

With:

```text
mu = R^2 + 2Rell*y + ell^2*y^2
```

the weighted moments are:

```text
W0 = 0
W1 = 512ell*(13R^2 + 2ell^2)/(5005R)
W2 = 1024*(13R^2 + 12ell^2)/15015
```

Interpretation:

```text
weighted total neutrality survives;
weighted local probes still detect rho.
```

This prevents the Group 83 weighted result from being overused as local inertness.

### 5. Skew-Inertness Tradeoff Test

For generic linear skew:

```text
M1 = -1024c/3465
weighted total = -1024ell*(2Rc - 3ell)/3465
```

Dipole inertness requires:

```text
c = 0
```

Weighted neutrality requires:

```text
c = 3ell/(2R)
```

These are incompatible unless:

```text
ell = 0
```

Interpretation:

```text
finite-thickness weighted neutrality and dipole inertness pull the skew in different directions.
```

This is a real structural tradeoff.

### 6. Quadratic Payload Obstruction

For generic linear skew:

```text
M2 = 1024/1155
dM2/dc = 0
```

There is no linear-skew solution for:

```text
M2 = 0
```

Interpretation:

```text
the quadratic payload obstruction cannot be tuned away by the linear skew.
```

This is the strongest obstruction in the group.

### 7. Local Inertness Route Classifier

The classifier correctly records:

```text
GLOBAL_SOURCE_NEUTRALITY_RETAINED
DIPOLE_PAYLOAD_NONZERO
QUADRATIC_PAYLOAD_NONZERO
WEIGHTED_TOTAL_NEUTRALITY_RETAINED
WEIGHTED_LOCAL_PAYLOAD_NONZERO
WEIGHTED_NEUTRALITY_DIPOLE_INERTNESS_TRADEOFF
LINEAR_SKEW_CANNOT_KILL_QUADRATIC_PAYLOAD
LOCAL_INERTNESS_OBSTRUCTED_IN_FINITE_MODE_TEST
RHO_EXACTNESS_STILL_GLOBALLY_USEFUL
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

This is the right final status.

### 8. Group Status Summary

The final summary preserves the main distinction:

```text
rho exactness remains globally useful but locally payload-dangerous.
```

That sentence should carry forward.

## Final Status Ledger

```text
flat_global_source_moment:
  M0 = 0
  RETAINED

flat_dipole_moment:
  M1 = -512ell/(1155R)
  NONZERO_FOR_FINITE_ELL_OVER_R

flat_quadratic_moment:
  M2 = 1024/1155
  NONZERO
  INDEPENDENT_OF_C

weighted_total_moment:
  W0 = 0
  RETAINED

weighted_dipole_moment:
  W1 = 512ell*(13R^2 + 2ell^2)/(5005R)
  NONZERO

weighted_quadratic_moment:
  W2 = 1024*(13R^2 + 12ell^2)/15015
  NONZERO

weighted_neutrality_condition:
  c = 3ell/(2R)

dipole_inertness_condition:
  c = 0

tradeoff:
  INCOMPATIBLE_UNLESS_ELL_EQUALS_ZERO

linear_skew_quadratic_suppression:
  IMPOSSIBLE

local_inertness:
  OBSTRUCTED_IN_FINITE_MODE_TEST

rho_exactness:
  GLOBALLY_USEFUL
  LOCALLY_PAYLOAD_DANGEROUS

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 84 rejects:

```text
global neutrality as payload inertness;
weighted total neutrality as payload inertness;
linear skew as complete payload cure;
finite-mode result as full physical payload theorem;
parent equation jump.
```

## Strategic Interpretation

Group 84 changes the strategy.

Groups 82–83 made the exactness route look promising for global and weighted total neutrality. Group 84 says that is not enough if local payload matters.

The route now splits:

```text
If only total layer neutrality matters:
  rho exactness remains promising.

If local payload matters:
  the current compact-support linear-skew family is insufficient.
```

That distinction should guide future work.

## Recommended Next Group

The best next technical group is:

```text
85_shape_family_payload_suppression_test
```

Reason:

```text
Group 84 shows the linear-skew family cannot suppress low-order payload moments.
A richer shape family may have enough degrees of freedom to satisfy:
  W0 = 0,
  M1 = 0,
  M2 = 0.
```

If richer shape families fail, then pressure increases toward:

```text
85_payload_projection_operator_necessity
```

or toward accepting local `rho` as a physical layer payload.

## Final Interpretation

Group 84 poked the local goblin.

```text
The total charge vanished.
The weighted total vanished.
The dipole twitched.
The quadratic tooth stayed fixed.
The goblin is not asleep.
```
