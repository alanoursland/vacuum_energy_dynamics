# candidate_physical_remainder_payload_test — Result Note

## Result

`candidate_physical_remainder_payload_test.py` audits possible physical payload carried by `rho_phys`.

Payload channels:

```text
source payload = S_M*i_src*rho_phys
trace payload = T_zeta*i_trace*rho_phys
mass payload = M_A*i_mass*rho_phys
divergence payload = D_parent*i_div*rho_phys
```

Total payload:

```text
rho_phys*(D_parent*i_div + M_A*i_mass + S_M*i_src + T_zeta*i_trace)
```

The safe no-payload route is:

```text
0
```

## Main Findings

Any physical `rho` payload blocks the shared lift identity until it is proven absent or inert.

The script correctly identifies the dangerous channels:

```text
source;
trace;
mass;
divergence.
```

This matters because even if `rho` is small or boundary-like, it cannot be ignored if it carries any of these loads.

## Boundary

No inertness theorem is proven. The script is a payload filter, not payload removal.

## Steering Consequence

Proceed to route classification. The final status should preserve `rho` as unresolved unless a zero/exact/inert theorem has been derived.
