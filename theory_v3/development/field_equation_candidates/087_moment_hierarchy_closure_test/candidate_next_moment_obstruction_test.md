# candidate_next_moment_obstruction_test — Analysis Note

## Result

`candidate_next_moment_obstruction_test.py` computes the first unsuppressed moment for each hierarchy profile.

The next flat moments are:

```text
N=1:
  M4 = 32768/15015
  rho(0)=72

N=2:
  M6 = 65536/323323
  rho(0)=-30

N=3:
  M8 = 10485760/22309287
  rho(0)=300

N=4:
  M10 = 33554432/1252507113
  rho(0)=-9450/131
```

The leading weighted obstructions are:

```text
ell^2 * M(2N+2)
```

for the corresponding inherited weighted block boundary.

## Interpretation

This is the main caution result of Group 87.

The hierarchy suppresses finite blocks, but every tested order leaves a next obstruction. The local field is also pointwise nonzero in every tested case.

So the hierarchy is not a closure mechanism yet. It is a deferral mechanism:

```text
raise N;
push payload visibility to a higher moment;
do not eliminate payload entirely.
```

That is still useful. But it is not local inertness.

## What Changed

The hierarchy is now understood as finite-order suppression with a sharp next-tooth obstruction.

That is a better status than either:

```text
local payload impossible
```

or:

```text
local payload solved.
```

## What Did Not Change

Local rho remains nonzero. All-order closure remains unproven.

If the theory needs exact local inertness, the finite hierarchy is insufficient unless a limit exists and is well-behaved.

## Steering Consequence

The next real progress target should be one of these:

```text
derive the general hierarchy formula;
test the all-order limit;
determine whether the sequence converges to a distribution/profile with true moment annihilation;
or prove an obstruction to that limit.
```
