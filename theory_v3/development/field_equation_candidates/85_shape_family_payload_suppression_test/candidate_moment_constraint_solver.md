# candidate_moment_constraint_solver — Analysis Note

## Result

`candidate_moment_constraint_solver.py` computes the generic moments for the even quartic family:

```text
M0 = 0
M1 = 0
M2 = -1024(p + q - 39)/45045
M3 = 0
M4 = 2048(17p + q + 153)/765765
M5 = 0
```

Solving:

```text
M2 = 0
M4 = 0
```

gives the unique profile:

```text
p = -12
q = 51
```

so:

```text
P(y) = 1 - 12y^2 + 51y^4
```

## Interpretation

This is the first major positive result of Group 85.

Group 84 showed that the linear-skew family cannot kill the quadratic payload moment. Group 85 shows that adding an even quartic shape family can kill both the quadratic and quartic moments simultaneously.

This is not a small improvement. It means the Group 84 local-inertness obstruction was not universal. It was a limitation of the chosen profile family.

The result also has a strong uniqueness property inside this normalized family:

```text
P(0) = 1;
P even quartic;
M2 = M4 = 0
```

force:

```text
P = 1 - 12y^2 + 51y^4.
```

## What Changed

The status should no longer be:

```text
local payload suppression obstructed
```

without qualification.

It should become:

```text
linear-skew local payload suppression obstructed;
even-quartic finite-mode suppression profile exists.
```

That is a meaningful improvement in the exactness route.

## What Did Not Change

The profile is moment-derived. That is not the same as geometry-derived.

The script correctly rejects the overclaim:

```text
shape origin proven.
```

The next burden is now:

```text
why P = 1 - 12y^2 + 51y^4?
```

## Steering Consequence

The next validation must check that the derived profile actually suppresses the expected moment block and remains regular/compact.
