# candidate_lift_identity_input_gate — Result Note

## Result

`candidate_lift_identity_input_gate.py` defines the concrete-input gate for the lift identity route.

The shared lift residual carried forward is:

```text
rho
```

Accepted input:

```text
covariant lift identity candidate;
common K origin;
sign/orientation relation;
rho handling target;
L_bulk/L_gauge domain and role.
```

Rejected input:

```text
L_bulk = -L_gauge by choice;
dropped L_bulk or L_gauge;
exact-pair scaffold alone;
free sign or coefficient;
repair current.
```

The archive dependency check is clean:

```text
g81_acceptance: dependency_satisfied
```

## Main Findings

The gate correctly preserves the lift-route burden from Groups 75–77. A future lift attempt must explain the origin of `K`, the sign/orientation relation, and how `rho` is handled.

The script rejects the old traps:

```text
chosen cancellation;
dropped lift residues;
exact-pair scaffold without origin;
free sign/coefficient;
repair current.
```

## Boundary

No lift identity theorem is proven. `rho` remains live.

## Steering Consequence

Proceed to the `rho` exactness input gate.
