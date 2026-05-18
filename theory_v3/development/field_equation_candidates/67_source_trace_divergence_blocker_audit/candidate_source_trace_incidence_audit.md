# candidate_source_trace_incidence_audit — Result Note

## Result

The script derives explicit source and trace count-once incidence residuals.

Source residual:

```text
S_M*(i_A + i_src_extra - 1)
```

Trace residual:

```text
T_zeta*(i_B + i_res + i_trace_extra - 1)
```

Enumerated safe source states:

```text
(i_A, i_src_extra) = (0,1)
(i_A, i_src_extra) = (1,0)
```

Enumerated safe trace states:

```text
(i_B, i_res, i_trace_extra) = (0,0,1)
(i_B, i_res, i_trace_extra) = (0,1,0)
(i_B, i_res, i_trace_extra) = (1,0,0)
```

## Main Findings

This turns vague count-once language into explicit algebra.

Ordinary source is count-safe only if:

```text
i_A + i_src_extra = 1
```

Trace payload is count-safe only if:

```text
i_B + i_res + i_trace_extra = 1
```

The script also preserves the Group 65 fence:

```text
diagnostic transition response contributes no parent incidence.
```

So `i_src_extra` and `i_trace_extra` cannot be secretly interpreted as the diagnostic transition response becoming physical again.

Rejected shortcuts:

```text
source repair through extra source route;
trace repair through residual or transition route;
transition carrier route.
```

## Boundary

This is necessary incidence algebra. It is not yet a role-safe parent condition, because some count-safe states are repair/replacement states.

## Steering Consequence

Proceed to the compatibility sieve. The next script must identify which count-safe state is also role-safe for parent use.
