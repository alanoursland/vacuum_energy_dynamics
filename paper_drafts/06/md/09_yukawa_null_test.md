# 9. Phenomenological Corollary: Yukawa Null Test

If `a` is allowed, the scalaron produces a short-range correction to the
Newtonian potential:

```text
V(r) = -G m1 m2 / r [1 + (1/3) exp(-r/ell)] .
```

The coupling is fixed:

```text
alpha = 1/3,
ell = sqrt(6a).
```

Short-range gravity experiments can therefore bound `ell` if the scalaron is
allowed. The current `ShortRangeGravity` v1 data gate contains two validated
95%-CL curves [Lee et al., 2020; Tan et al., 2020]:

```text
Lee 2020: |alpha| = 1 crossing   38.63 um
Lee 2020: alpha = 1/3 crossing   54.03 um

Tan 2020: |alpha| = 1 crossing   47.74 um
Tan 2020: alpha = 1/3 crossing   57.29 um
```

The Lee 2020 curve [Lee et al., 2020] is binding in the scalaron window.
Thus, without static frame indifference, the current data would bound the
scalaron range at

```text
ell < 54.03 um.
```

With static frame indifference, the prediction is stronger and cleaner:

```text
No gravitational-strength scalaron Yukawa channel exists at any range.
```

The data do not select `a = 0`; the principle does. The data show where the
principle is being tested. A confirmed gravitational-strength Yukawa signal
with the scalaron sign and coupling would falsify or force a scope revision of
static frame indifference.

The Lee value is independently cross-checked: the supplemental-table extraction
gives `54.03 um`, while the earlier vector-path extraction from Fig. 5 of
[Lee et al., 2020] gives `54.05 um`.
