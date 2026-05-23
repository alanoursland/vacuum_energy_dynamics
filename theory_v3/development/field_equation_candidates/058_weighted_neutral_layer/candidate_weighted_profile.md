# candidate_weighted_profile — Result Note

## Result

The script constructs a nontrivial localized finite-layer profile with exact weighted neutrality.

It uses:

```text
r(y)=R+ell*y
w(y)=(1-y^2)^2
rho(y)=rho0*w(y)*(y-c)
```

Solving the weighted charge condition:

```text
integral_{-1}^{1} (R+ell*y)^2 w(y)(y-c) dy = 0
```

gives:

```text
c = 2*R*ell/(7*R^2 + ell^2)
```

With this value:

```text
Q_weighted = 0
rho(-1)=0
rho(1)=0
```

and the profile is nontrivial:

```text
rho(0) = -2*R*ell*rho0/(7*R^2 + ell^2)
rho(1/2) = 9*rho0*(7*R^2 - 4*R*ell + ell^2)/(32*(7*R^2 + ell^2))
```

## Main Findings

This is the main constructive result of Group 58.

The Group 57 blocker was not only restated; it was answered. A finite-layer profile can be:

```text
localized at the endpoints;
nontrivial inside the layer;
exactly neutral under spherical r^2 weighting.
```

The skew is not arbitrary tuning. It is fixed by the geometry-weighted neutrality condition:

```text
c = 2*R*ell/(7*R^2 + ell^2)
```

This is an important conceptual improvement. The real smoothing function does not need to be flat-symmetric. It may need geometry-aware skew to remain neutral.

## Boundary

The profile is not ordinary matter source. It is not an insertion law. It is not a covariant theorem.

## Steering Consequence

The next check should compare this result against the rejected flat-odd profile. The group should make explicit that weighted neutrality, not flat neutrality, is the correct target.
