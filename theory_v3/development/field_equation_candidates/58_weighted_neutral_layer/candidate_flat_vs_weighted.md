# candidate_flat_vs_weighted — Result Note

## Result

The script compares the failed flat-odd profile from Group 57 with the new weighted-neutral profile from Group 58.

For the odd profile:

```text
rho_odd = rho1*y
```

it finds:

```text
Q_flat_odd = 0
Q_weighted_odd = 4*R*ell*rho1/3
```

So flat cancellation fails under spherical weighting.

For the new profile:

```text
rho_weighted = -rho0*(y^2 - 1)^2*(2*R*ell - y*(7*R^2 + ell^2))/(7*R^2 + ell^2)
```

it finds:

```text
Q_weighted = 0
```

The weighted-neutral profile does not need zero flat charge:

```text
Q_flat_weighted = -32*R*ell*rho0/(105*R^2 + 15*ell^2)
```

## Main Findings

This is a clean correction of the Group 57 warning.

The correct neutrality condition is not:

```text
integral rho dy = 0
```

The correct reduced spherical condition is:

```text
integral (R+ell*y)^2 rho dy = 0
```

The weighted-neutral profile fixes the problem by using geometry-aware skew.

This also creates a useful rule for future layer work:

```text
flat symmetry is not physical neutrality;
weighted neutrality is the target.
```

## Boundary

Weighted neutrality does not prove source safety, covariant lift, or insertion. It only fixes the reduced weighted scalar charge diagnostic.

## Steering Consequence

Future profiles and candidate transition terms must be judged by weighted charge, not flat charge. The next check should verify that the weighted-neutral profile is finite-energy and nonfree.
