# candidate_boundary_exactness_test — Result Note

## Result

`candidate_boundary_exactness_test.py` tests a boundary-exact decomposition:

```text
rho = divB*i_boundary + i_bulk*rho_bulk
```

The boundary-only route is:

```text
divB
```

The bulk remainder is:

```text
rho_bulk
```

The unresolved boundary-plus-bulk route is:

```text
divB + rho_bulk
```

## Main Findings

Boundary-exact status is retained only as a theorem target.

It requires both:

```text
boundary exactness is derived;
rho_bulk = 0 is derived.
```

The script correctly rejects boundary-exactness by label and an unresolved bulk remainder.

## Boundary

No boundary-exact theorem is proven. The bulk physical remainder remains open.

## Steering Consequence

Proceed to physical remainder payload testing. If a physical remainder survives, it must be checked for source, trace, mass, and divergence load.
