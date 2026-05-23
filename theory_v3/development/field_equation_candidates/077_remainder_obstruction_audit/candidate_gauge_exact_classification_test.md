# candidate_gauge_exact_classification_test — Result Note

## Result

`candidate_gauge_exact_classification_test.py` tests a gauge-exact decomposition:

```text
rho = dXi*i_exact + i_phys*rho_phys
```

The exact-only route is:

```text
dXi
```

The physical-only remainder is:

```text
rho_phys
```

The unresolved exact-plus-physical remainder is:

```text
dXi + rho_phys
```

## Main Findings

Gauge-exact status is retained only as a theorem target.

It requires two separate derivations:

```text
dXi is genuinely exact/nonphysical;
rho_phys = 0.
```

The script correctly rejects:

```text
exactness by label;
unresolved physical remainder.
```

## Boundary

No gauge-exact theorem is proven. The physical remainder remains open.

## Steering Consequence

Proceed to boundary-exactness testing. A parallel classification is needed for boundary-exact remainder handling.
