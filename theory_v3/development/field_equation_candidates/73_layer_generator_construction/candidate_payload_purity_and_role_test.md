# candidate_payload_purity_and_role_test — Result Note

## Result

`candidate_payload_purity_and_role_test.py` audits whether a candidate `D_layer` carries forbidden physical payloads.

It tests source, trace, mass, repair, active-O, and diagnostic payload channels.

The source and trace residuals are:

```text
S_M * (i_A + i_layer_src - 1)
T_zeta * (i_B + i_layer_trace + i_res - 1)
```

Layer-source and layer-trace routes produce nonzero residuals:

```text
S_M
T_zeta
```

## Main Findings

The role-purity result is strong.

A legal `D_layer` must not carry:

```text
ordinary source load;
trace payload;
A-sector mass response;
repair-current payload;
active-O payload;
diagnostic-transition payload.
```

This protects the layer route from becoming a hidden source channel, residual reentry path, mass patch, repair current, or disguised projection operator.

## Boundary

Payload purity does not derive `D_layer`.

It only rejects forbidden interpretations and preserves the possible pure geometric route as an obligation.

## Steering Consequence

Proceed to `candidate_boundary_lift_interface_test.py`.

The next test should verify whether a clean geometric `D_layer_geo`, if later derived, can participate in the boundary-lift anti-match without closing the remaining lift-cleanliness obligations.
