# candidate_rho_status_axiom_candidates — Result Note

## Result

`candidate_rho_status_axiom_candidates.py` inventories possible `rho` status axioms.

Candidate-only routes:

```text
RHO_ZERO_AXIOM:
  rho = 0 by explicit postulate

RHO_GAUGE_EXACT_AXIOM:
  rho = dXi and physical remainder vanishes

RHO_BOUNDARY_EXACT_AXIOM:
  rho = divB and bulk physical remainder vanishes

RHO_NO_PAYLOAD_AXIOM:
  rho carries no source/trace/mass/divergence payload
```

Rejected routes:

```text
DROPPED_RHO_AXIOM:
  would erase rho without theorem/adoption

EXACT_BY_LABEL_AXIOM:
  would call rho exact without content
```

The gauge and boundary forms still include physical remainder:

```text
dXi + rho_phys
divB + rho_phys
```

The archive dependency check is clean:

```text
g79_lift_axioms: dependency_satisfied
```

## Main Findings

The `rho` inventory is clean. It preserves `rho` as a named obstruction and permits only explicit candidate postulates that would need a future adoption surface.

No `rho` axiom is adopted.

## Boundary

`rho` remains unresolved. This file inventories possible axiom candidates but does not prove zero, exactness, boundary exactness, or no-payload behavior.

## Steering Consequence

Proceed to the risk sieve. The candidate list is only useful if the project records the risks each axiom would carry.
