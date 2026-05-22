# candidate_flat_probe_moment_test — Analysis Note

## Result

`candidate_flat_probe_moment_test.py` computes flat payload moments after imposing the Group 83 skew:

```text
c = 3ell/(2R)
```

The skewed local remainder is:

```text
rho_skew =
-3*(y - 1)^3*(y + 1)^3
*(18*R*y^2 - 2*R + 35*ell*y^3 - 11*ell*y)/R
```

The moments are:

```text
M0 = 0
M1 = -512ell/(1155R)
M2 = 1024/1155
```

## Interpretation

This is the first major obstruction in Group 84.

The result confirms that Group 83’s skew preserves global flat neutrality:

```text
M0 = 0
```

But it fails local finite-mode inertness immediately:

```text
M1 != 0 for ell/R != 0
M2 != 0 always
```

This means the derived weighted-neutral skew makes `rho` visible to a dipole/gradient probe whenever the layer has finite thickness relative to curvature radius. Even worse, the quadratic moment is nonzero independent of `ell/R` in this expression.

The interpretation is not:

```text
rho exactness failed.
```

The correct interpretation is:

```text
rho exactness remains globally useful but locally detectable.
```

## What Changed

Before this script, payload inertness was merely open. After this script, low-order flat probes detect a payload obstruction.

The status should update to:

```text
GLOBAL_SOURCE_NEUTRALITY_RETAINED
DIPOLE_PAYLOAD_NONZERO
QUADRATIC_PAYLOAD_NONZERO
LOCAL_INERTNESS_NOT_ESTABLISHED
```

## What Did Not Change

This does not erase the Group 82/83 wins. Flat and weighted total neutrality remain useful.

But those wins can no longer be interpreted as local inertness.

## Steering Consequence

The exactness route now faces a fork:

```text
1. accept that only integrated neutrality is required;
2. find a richer shape family that suppresses M1/M2;
3. introduce a legitimate payload projection/inertness mechanism;
4. show these moments do not correspond to physical payload channels.
```

Without one of those, local `rho` remains dangerous.
