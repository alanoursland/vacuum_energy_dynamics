# candidate_group_84_status_summary — Analysis Note

## Result

`candidate_group_84_status_summary.py` closes Group 84 with this stable result:

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

## Interpretation

Group 84 makes real progress, but it is negative progress for the local-inertness route.

The important discovery is not just that some moments are nonzero. The important discovery is that the exactness route has separated into two different kinds of success:

```text
global/weighted total neutrality succeeds;
finite-mode local inertness fails.
```

This is the cleanest statement so far of the physical danger in local nonzero `rho`.

Groups 82–83 showed:

```text
rho can be exact and globally/weighted neutral.
```

Group 84 shows:

```text
that does not make rho locally inert.
```

## What Changed

The status of payload inertness should move from:

```text
PAYLOAD_INERTNESS_OPEN
```

to:

```text
LOCAL_INERTNESS_OBSTRUCTED_IN_FINITE_MODE_TEST
PAYLOAD_INERTNESS_OPEN_FOR_FULL_THEORY
```

The distinction matters. The full theory is not disproven, but the tested reduced family fails a meaningful local payload test.

## What Did Not Change

Parent divergence remains unproven. Recombination remains blocked. No active operator is constructed. No full physical payload theorem is proven.

The exactness route remains valuable for total neutrality:

```text
M0 = 0;
W0 = 0.
```

That should not be lost.

## Steering Consequence

The best next technical group is probably:

```text
85_shape_family_payload_suppression_test
```

because the obstruction may be due to the limited linear-skew family. The next real question is whether a richer shape family can satisfy:

```text
weighted total neutrality;
dipole inertness;
quadratic inertness.
```

If the richer family also fails, pressure increases toward either:

```text
payload projection/inertness mechanism;
or interpreting local rho as a real physical layer payload.
```
