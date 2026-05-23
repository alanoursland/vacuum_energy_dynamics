# candidate_group_85_status_summary — Analysis Note

## Result

`candidate_group_85_status_summary.py` closes Group 85 with this stable result:

```text
even quartic shape family tested;
P = 1 - 12y^2 + 51y^4 found from M2=M4 constraints;
profile is regular/positive on [-1,1];
endpoint compact flux retained;
M0..M5 vanish;
W0..W3 vanish under quadratic measure;
local rho remains nonzero;
M6 and W4 remain nonzero;
Group 84 linear-skew obstruction is not universal;
shape origin remains open;
full local inertness not proven;
parent divergence identity remains unproven;
recombination blocked.
```

## Interpretation

Group 85 makes real positive progress.

Group 84 found that the compact-support linear-skew family could not prove local inertness. Group 85 shows that this obstruction was not universal. A richer even quartic shape can suppress a substantially larger block of local payload moments.

This changes the route status from:

```text
local exactness payload suppression looks obstructed
```

to:

```text
local exactness payload suppression is possible in a richer finite-mode shape family,
but shape origin and all-order closure remain open.
```

That is a genuine improvement.

## What Changed

The exactness route now has three reduced-class successes:

```text
Group 82:
  flat integrated neutrality.

Group 83:
  weighted-total skew derived from measure-gradient orthogonality.

Group 85:
  low-order flat and weighted payload moments suppressed by an even quartic profile.
```

Group 84 remains important, but its obstruction is now properly scoped:

```text
linear-skew obstruction,
not universal obstruction.
```

## What Did Not Change

Group 85 does not prove full local inertness.

The local field remains nonzero:

```text
rho(0) = -30
```

and the next moments remain:

```text
M6 = 65536/323323
W4 = 65536 ell^2 / 323323
```

So this is finite-mode suppression, not pointwise removal or all-order inertness.

The profile is also moment-derived, not geometry-derived. That is the largest remaining concern.

## Steering Consequence

The best next group is:

```text
86_shape_origin_geometry_derivation
```

The project now has an effective and regular shape:

```text
P(y) = 1 - 12y^2 + 51y^4
```

The next question is whether that profile is forced by geometry, variational principle, orthogonality hierarchy, or minimal payload criterion, or whether it is just a clever moment-designed filter.
