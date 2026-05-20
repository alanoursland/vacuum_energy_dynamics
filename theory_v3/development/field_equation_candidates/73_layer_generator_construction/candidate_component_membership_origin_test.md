# candidate_component_membership_origin_test — Result Note

## Result

`candidate_component_membership_origin_test.py` tests component membership in a generated boundary object.

It writes:

```text
B_generated = m_jump D_jump + m_layer D_layer + m_tail D_tail
```

and compares it with:

```text
B_target = D_jump + D_layer + D_tail
```

The compatibility solution is:

```text
m_jump = 1
m_layer = 1
m_tail = 1
```

## Main Findings

The exact membership burden is explicit.

A common boundary object must include jump, layer, and tail components. If the layer component is missing, the residual is:

```text
-D_layer
```

So the boundary generator is incomplete unless `D_layer` is actually a member of the same geometric object.

The script correctly warns that setting `m_layer = 1` is only compatibility. It does not derive layer membership.

## Boundary

Component membership is not proven.

`m_layer = 1` must be derived from common boundary geometry, not declared.

The old diagnostic transition response cannot satisfy layer membership.

## Steering Consequence

Proceed to `candidate_payload_purity_and_role_test.py`.

The next test should ensure that even if `D_layer` is a member, it does not carry forbidden source, trace, mass, repair, active-O, or diagnostic payloads.
