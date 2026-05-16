# candidate_boundary_filter — Result Note

## Result

The boundary filter applies the reduced exterior scalar-silence conditions from Group 54.

It uses:

```text
phi = C0 + C1/r
flux = -4*pi*C1
```

and verifies the silent conditions:

```text
C0=0, C1=0 -> phi = 0
C1=0 -> flux = 0
J=0 -> no-shell diagnostic
```

The nonzero boundary flux route is rejected.

## Main Findings

This filter kills boundary-leaking insertion routes. Any insertion family that produces:

```text
nonzero C1;
nonzero scalar flux;
nonzero shell jump J;
boundary repair behavior
```

is not admissible for physical use.

The silent boundary route survives only conditionally:

```text
zero tail;
zero flux;
no shell source.
```

Those conditions require theorem support. They are not insertion permission.

## Boundary

The boundary filter is reduced and diagnostic. It does not prove full boundary neutrality, zero scalar charge, or no-shell matching.

## Steering Consequence

Insertion families that create scalar tails, scalar flux, or shell sources are excluded. Any surviving route must be boundary-silent before it can even be considered.
