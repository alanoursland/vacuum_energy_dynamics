# candidate_remainder_status_requirements — Result Note

## Result

`candidate_remainder_status_requirements.py` states the legal statuses for `rho`.

Allowed status categories:

```text
ZERO_DERIVED:
  rho = 0 by theorem

GAUGE_EXACT:
  rho = dXi and physical remainder vanishes

BOUNDARY_EXACT:
  rho = div_boundary(Pi) and physical bulk remainder vanishes

INERT:
  rho carries no source/trace/mass/divergence payload by theorem

PHYSICAL_REMAINDER:
  rho_phys remains

UNRESOLVED:
  no theorem status derived
```

The script also records the basic forms:

```text
zero residual = 0
gauge-exact form = dXi + rho_phys
boundary-exact form = divB + rho_phys
```

## Main Findings

This script gives Group 77 its status vocabulary. The key burden is that `rho_phys` must vanish or be proven inert for exact routes to be safe.

The script correctly rejects:

```text
status by label;
dropped rho.
```

## Boundary

The script states requirements only. It does not prove any status for `rho`.

## Steering Consequence

Proceed to the zero-remainder theorem test. The next script should determine whether `rho = 0` is derived or only compatible.
