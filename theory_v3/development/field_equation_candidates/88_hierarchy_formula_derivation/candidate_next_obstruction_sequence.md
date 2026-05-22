# candidate_next_obstruction_sequence — Analysis Note

## Result

`candidate_next_obstruction_sequence.py` computes the first unsuppressed moment through `N=6`.

The sequence is:

```text
N=1: M4  = 32768/15015,            rho(0)=72
N=2: M6  = 65536/323323,           rho(0)=-30
N=3: M8  = 10485760/22309287,      rho(0)=300
N=4: M10 = 33554432/1252507113,    rho(0)=-9450/131
N=5: M12 = 2147483648/24744476055, rho(0)=18480/19
N=6: M14 = 7516192768/2595164583825, rho(0)=-21021/157
```

## Interpretation

This is the caution result that keeps Group 88 honest.

The formula generates finite hierarchy profiles, but every generated profile still leaves a next moment obstruction. The local field also remains nonzero at the origin.

So the formula is not a proof of inertness. It is a proof of finite-order suppression.

The hierarchy is acting like a filter:

```text
increase N;
suppress a larger finite block;
leave the next moment visible.
```

That may still be useful, but it is not closure.

## What Changed

The next-obstruction sequence is now known through `N=6`, extending the Group 87 obstruction data.

This strengthens the interpretation that the hierarchy is systematic but finite-order.

## What Did Not Change

The local goblin still bites:

```text
rho(0) != 0
```

through all tested generated profiles.

The result also leaves open whether the next moments tend to zero, stabilize, or reveal an obstruction in the all-order limit.

## Steering Consequence

This result points directly to an all-order limit problem:

```text
Does M(2N+2) shrink enough to support distributional/local inertness in a limit,
or does it remain a persistent obstruction?
```

But before the limit is meaningful, the determinant/nonzero existence question likely needs to be addressed.
