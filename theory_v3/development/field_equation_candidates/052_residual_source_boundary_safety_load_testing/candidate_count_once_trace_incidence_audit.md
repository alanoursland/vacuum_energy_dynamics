# candidate_count_once_trace_incidence_audit — Result Note

## Result

The count-once trace audit produces the first concrete Group 52 diagnostic witness.

It defines an incidence model for trace payload `T_zeta` entering the `B_s/F_zeta` channel and/or residual `zeta/kappa` channel:

```text
trace_load = T_zeta*(i_Bs + i_res)
target     = T_zeta
residual   = T_zeta*(i_Bs + i_res - 1)
```

When both channels are active, `i_Bs=1` and `i_res=1`, the residual is:

```text
T_zeta
```

So double entry is visibly nonzero. When only `B_s/F_zeta` carries the trace and residual entry is absent, `i_Bs=1` and `i_res=0`, the residual is zero.

## Main Findings

This script does not prove count-once trace. It does something narrower and useful: it shows exactly what must be avoided.

The diagnostic says:

```text
B_s/F_zeta trace entry + residual trace reentry = double count
B_s/F_zeta trace entry + residual nonentry = clean once, at this incidence level
```

That means any physical-use route must prove that residual `zeta/kappa` cannot re-enter the metric trace if the trace payload is already present in `B_s/F_zeta`.

The output therefore sharpens the residual nonentry burden. It is no longer a vague caveat. It is a visible incidence condition.

## Boundary

The incidence ledger is not a theorem. It does not derive dynamics, does not prove residual nonentry, and does not license insertion. It is a diagnostic double-count witness.

## Steering Consequence

Any later insertion route must carry a count-once trace theorem. The immediate next step is to test residual nonentry routes and reject attempts to set residual incidence to zero by declaration.
