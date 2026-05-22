# candidate_group_86_status_summary — Analysis Note

## Result

`candidate_group_86_status_summary.py` closes Group 86 with this stable result:

```text
moment map from even shape coefficients to payload moments derived;
degree 0 and degree 2 obstruction derived;
degree 4 is minimal for killing M2 and M4;
P = 1 - 12y^2 + 51y^4 uniquely derived in normalized even quartic family;
same P is unique zero-action minimizer of A = M2^2 + M4^2;
W0..W3 weighted suppression follows from M0..M5 flat moment block;
shape origin strengthened inside reduced model;
full physical/covariant origin remains open;
local rho nonzero remains;
higher moments M6/W4 remain;
parent divergence identity remains unproven;
recombination remains blocked.
```

## Interpretation

Group 86 is a real progress group.

Group 85 found a good shape. Group 86 explains why that shape is special inside the reduced payload-suppression problem.

The biggest improvement is this:

```text
P(y)=1-12y^2+51y^4
```

is no longer merely:

```text
the shape found by solving M2=M4=0.
```

It is now:

```text
the minimal-degree normalized even polynomial that can kill M2 and M4;
the unique quartic solution;
the unique zero-action minimizer of A=M2^2+M4^2;
the source of W0..W3 suppression through the flat M0..M5 block.
```

That is a substantial internal origin result.

## What Changed

The correct carry-forward status is:

```text
SHAPE_ORIGIN_STRENGTHENED_IN_REDUCED_MODEL
```

or:

```text
REDUCED_STRUCTURAL_ORIGIN_DERIVED
```

with strict scope.

## What Did Not Change

This is not full physics yet.

Still open:

```text
physical/covariant origin of the reduced payload action;
why this reduced payload action is fundamental;
higher moment hierarchy;
local rho nonzero;
M6/W4 obstruction;
parent divergence;
recombination.
```

The exactness route is stronger, but not closed.

## Steering Consequence

The best next group is probably:

```text
87_moment_hierarchy_closure_test
```

Reason:

```text
Group 86 suggests a hierarchy:
higher-degree even profiles may suppress larger moment blocks.
```

Testing that would tell us whether the quartic profile is a one-off trick or the first member of a systematic payload-suppression family.
