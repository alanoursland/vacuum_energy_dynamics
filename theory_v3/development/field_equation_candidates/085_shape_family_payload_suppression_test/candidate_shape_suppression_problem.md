# candidate_shape_suppression_problem — Analysis Note

## Result

`candidate_shape_suppression_problem.py` opens Group 85 as a richer exactness shape-family test.

The central question is:

```text
Can a richer exactness shape suppress the low-order payload moments that defeated linear skew?
```

The imported Group 84 status is the right starting point:

```text
global and weighted total neutrality retained;
dipole and quadratic payload moments nonzero in the linear-skew family;
linear skew cannot kill quadratic payload;
local inertness obstructed in finite-mode test;
parent divergence identity unproven;
recombination blocked.
```

The concrete route is:

```text
P(y) = 1 + p y^2 + q y^4
```

## Interpretation

This opener asks the right next question.

Group 84 did not prove that all exactness profiles fail local payload suppression. It proved that the compact-support linear-skew family fails. Group 85 correctly avoids overgeneralizing that obstruction by adding new shape degrees of freedom.

This is real progress territory because the group is testing whether the obstruction is structural or family-specific.

The key strategic distinction is:

```text
Group 84:
  linear skew cannot suppress low-order local payload.

Group 85:
  test whether an even quartic shape can.
```

That is a meaningful escalation in model capacity.

## What Changed

The theory route is no longer stuck at:

```text
local inertness obstructed
```

in a universal sense. It is now testing:

```text
local inertness obstructed for the linear-skew family,
but possibly recoverable with a richer compact-support profile.
```

## What Did Not Change

The opener correctly preserves the boundary:

```text
finite shape suppression is not full inertness;
moment-designed shape is not physical derivation;
parent equation remains blocked.
```

That boundary matters because if the quartic profile works, the next danger is treating a moment-fit profile as if it were geometrically forced.

## Steering Consequence

The group should be judged by whether it does one of two things:

```text
find a profile that suppresses low-order moments;
or prove that even the richer family fails.
```

The outputs show it finds such a profile, so the Group 84 obstruction is not universal.
