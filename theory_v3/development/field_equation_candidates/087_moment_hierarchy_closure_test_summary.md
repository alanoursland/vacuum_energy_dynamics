# Group 87 Summary: Moment Hierarchy Closure Test

## Purpose

Group 87 tested whether the Group 86 quartic payload-suppression profile was a one-off or part of a systematic hierarchy.

Group 86 derived:

```text
P2(y) = 1 - 12y^2 + 51y^4
```

as the unique minimal even quartic profile suppressing:

```text
M2 = 0
M4 = 0
```

Group 87 generalized to:

```text
P_N(y) = 1 + a1 y^2 + ... + aN y^(2N)
```

and tested whether each `N` can uniquely suppress:

```text
M2, M4, ..., M(2N).
```

## Main Result

Group 87 is complete.

Stable result:

```text
general even compact-support operator tested;

odd moments vanish by parity;

finite moment hierarchy supported for N=1..4;

unique normalized even profile per order through N=4;

quadratic-measure weighted block inheritance derived;

next even moment M(2N+2) remains nonzero in tested cases;

local rho remains nonzero;

all-order closure not proven;

physical/covariant origin remains open;

parent divergence identity remains unproven;

recombination remains blocked.
```

## What We Actually Learned

Group 87 makes real progress.

The quartic profile is not a one-off. It is the `N=2` member of a finite hierarchy, supported through `N=4`.

The hierarchy says:

```text
degree 2N normalized even profile
  kills M2 through M(2N)
  has a unique solution through tested N
  inherits weighted suppression under quadratic measure
  leaves M(2N+2) nonzero
```

So the exactness route has a finite-order payload-suppression mechanism.

But it does not have all-order local inertness yet.

## Script-Level Analysis

### 1. Moment Hierarchy Problem

The opener correctly asks whether the Group 86 quartic profile is systematic.

It preserves the correct scope:

```text
finite hierarchy evidence;
not all-order proof;
parent divergence blocked;
recombination blocked.
```

### 2. General Even Shape Operator

The general even profile satisfies:

```text
P(-y)-P(y) = 0
J(-y)+J(y) = 0
rho(-y)-rho(y) = 0
J(-1)=J(1)=0
```

Odd moments vanish automatically:

```text
M1 = M3 = M5 = M7 = 0
```

Interpretation:

```text
odd moments are not independent constraints;
the N coefficients can target the N nontrivial even moments.
```

### 3. Hierarchy Profiles N1 to N4

The solved profiles are:

```text
N=1:
  P1 = 1 + 39y^2
  kills M2
  next M4 = 32768/15015

N=2:
  P2 = 1 - 12y^2 + 51y^4
  kills M2,M4
  next M6 = 65536/323323

N=3:
  P3 = 1 + 153y^2 - 969y^4 + 1615y^6
  kills M2,M4,M6
  next M8 = 10485760/22309287

N=4:
  P4 = 1 - (4332/131)y^2 + (51186/131)y^4
       - (166060/131)y^6 + (163875/131)y^8
  kills M2,M4,M6,M8
  next M10 = 33554432/1252507113
```

This is the central hierarchy result.

### 4. Constraint Rank Uniqueness Test

For each `N=1..4`, the constraint matrix is full-rank:

```text
N=1: rank=1, unique=True
N=2: rank=2, unique=True
N=3: rank=3, unique=True
N=4: rank=4, unique=True
```

Interpretation:

```text
the hierarchy profiles are forced by the constraints through N=4;
they are not free-parameter families.
```

This matters because it reduces repair concern inside the reduced problem.

### 5. Weighted Block Inheritance Theorem

For quadratic measure:

```text
mu = R^2 + 2Rell y + ell^2 y^2
```

the weighted moments obey:

```text
Wn = R^2 M_n + 2Rell M_(n+1) + ell^2 M_(n+2)
```

So if:

```text
M0..M(2N+1) = 0
```

then:

```text
W0..W(2N-1) = 0.
```

Interpretation:

```text
weighted suppression is inherited from the flat moment block;
it does not require separate tuning.
```

### 6. Next Moment Obstruction Test

Each tested profile leaves the next even moment nonzero:

```text
N=1: M4 = 32768/15015
N=2: M6 = 65536/323323
N=3: M8 = 10485760/22309287
N=4: M10 = 33554432/1252507113
```

The corresponding leading weighted obstruction is:

```text
ell^2 * M(2N+2)
```

The local field remains nonzero:

```text
N=1: rho(0)=72
N=2: rho(0)=-30
N=3: rho(0)=300
N=4: rho(0)=-9450/131
```

Interpretation:

```text
the hierarchy suppresses finite blocks but does not close all moments or remove local rho.
```

### 7. Moment Hierarchy Route Classifier

The classifier correctly records:

```text
FINITE_MOMENT_HIERARCHY_SUPPORTED_N1_TO_N4
UNIQUE_PROFILE_PER_ORDER_N1_TO_N4
WEIGHTED_BLOCK_INHERITANCE_DERIVED
NEXT_MOMENT_OBSTRUCTION_PERSISTS
ALL_ORDER_CLOSURE_NOT_PROVEN
LOCAL_RHO_NONZERO_REMAINS
PHYSICAL_COVARIANT_ORIGIN_OPEN
PARENT_DIVERGENCE_UNPROVEN
RECOMBINATION_BLOCKED
```

### 8. Group Status Summary

The final summary is conceptually sound. Group 87 establishes finite hierarchy evidence, not closure.

## Final Status Ledger

```text
general_even_operator:
  DERIVED

odd_moments:
  VANISH_BY_PARITY

finite_hierarchy:
  SUPPORTED_THROUGH_N4

unique_profile_per_order:
  TRUE_THROUGH_N4

N1_profile:
  P1 = 1 + 39y^2

N2_profile:
  P2 = 1 - 12y^2 + 51y^4

N3_profile:
  P3 = 1 + 153y^2 - 969y^4 + 1615y^6

N4_profile:
  P4 = 1 - (4332/131)y^2 + (51186/131)y^4
       - (166060/131)y^6 + (163875/131)y^8

weighted_block_inheritance:
  DERIVED_FOR_QUADRATIC_MEASURE

next_moment_obstruction:
  PERSISTS

all_order_closure:
  NOT_PROVEN

local_rho:
  NONZERO_REMAINS

physical_covariant_origin:
  OPEN

parent_divergence:
  NOT_PROVEN

recombination:
  BLOCKED
```

## Rejected Overclaims

Group 87 rejects:

```text
quartic profile as one-off;
finite pattern as infinity;
finite hierarchy as all-order inertness;
weighted suppression as separate tuning;
moment suppression as pointwise rho=0;
parent equation jump;
recombination opening.
```

## Strategic Interpretation

Group 87 strengthens the exactness/payload-suppression route.

The recent arc is now:

```text
Group 82:
  exactness gives flat total neutrality.

Group 83:
  weighted skew comes from measure-gradient orthogonality.

Group 84:
  linear-skew local inertness fails.

Group 85:
  even quartic shape suppresses low-order local payload.

Group 86:
  quartic shape has reduced structural/variational origin.

Group 87:
  quartic shape is part of a finite hierarchy through N=4.
```

This is a real pattern.

The remaining danger is that finite hierarchy is not all-order closure. It may still only push payload visibility to higher moments. The next group needs to attack the general formula or the all-order limit.

## Recommended Next Group

Best next group:

```text
88_hierarchy_formula_derivation
```

Purpose:

```text
Derive a recurrence or closed form for the hierarchy coefficients.
```

Second-best route:

```text
88_all_order_limit_obstruction
```

Purpose:

```text
Determine whether the hierarchy converges to all-order inertness or fails in the limit.
```

My recommendation is:

```text
88_hierarchy_formula_derivation
```

because Group 87 has enough finite evidence to justify looking for the rule behind the sequence.

## Final Interpretation

Group 87 found the keyring.

```text
The quartic key was not alone.
More teeth appear when more tumblers are named.
But every finite key still leaves one tooth catching.
Now we need the pattern that cuts the whole ring.
```
