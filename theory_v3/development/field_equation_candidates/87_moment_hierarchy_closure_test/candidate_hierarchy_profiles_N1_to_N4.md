# candidate_hierarchy_profiles_N1_to_N4 — Analysis Note

## Result

`candidate_hierarchy_profiles_N1_to_N4.py` solves the hierarchy profiles for `N=1..4`.

The profiles are:

```text
N=1:
  P1 = 1 + 39 y^2
  kills M2
  next M4 = 32768/15015

N=2:
  P2 = 1 - 12 y^2 + 51 y^4
  kills M2,M4
  next M6 = 65536/323323

N=3:
  P3 = 1 + 153 y^2 - 969 y^4 + 1615 y^6
  kills M2,M4,M6
  next M8 = 10485760/22309287

N=4:
  P4 = 1 - (4332/131)y^2 + (51186/131)y^4
       - (166060/131)y^6 + (163875/131)y^8
  kills M2,M4,M6,M8
  next M10 = 33554432/1252507113
```

## Interpretation

This is the main positive result of Group 87.

The quartic profile from Groups 85–86 is not a one-off. It is the `N=2` member of a finite hierarchy, at least through `N=4`.

The pattern is clear:

```text
degree 2N normalized even profile
  -> kills M2 through M(2N)
  -> leaves M(2N+2) nonzero
```

This means higher-degree exactness shapes can push the first visible payload moment farther out.

That is a major improvement in the local-payload story. Group 84 showed the linear-skew family failed early. Group 85 found a quartic fix. Group 87 shows there is a systematic finite-order mechanism.

## What Changed

The route status should be upgraded from:

```text
quartic profile structurally derived
```

to:

```text
finite moment-suppression hierarchy supported through N=4
```

That is real progress.

## What Did Not Change

The next moment remains nonzero at every tested order. This is not all-order closure.

The result says:

```text
payload visibility can be delayed to higher order
```

not:

```text
payload visibility disappears.
```

## Steering Consequence

The next technical problem is no longer whether the hierarchy exists in low orders. It does. The next problem is to derive the general recurrence or coefficient formula.
