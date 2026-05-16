# candidate_trace_count_filter — Result Note

## Result

The trace-count filter applies the count-once trace condition to insertion families.

It uses:

```text
trace residual = T_zeta*(i_Bs + i_res - 1)
```

and obtains:

```text
B_s clean route:
  i_Bs=1, i_res=0 -> residual = 0

double-entry route:
  i_Bs=1, i_res=1 -> residual = T_zeta

missing-entry route:
  i_Bs=0, i_res=0 -> residual = -T_zeta

residual-only route:
  i_Bs=0, i_res=1 -> residual = 0
```

## Main Findings

The filter rejects two insertion families:

```text
double-entry trace routes;
missing-entry trace routes.
```

The `B_s/F_zeta` route survives only under the clean incidence condition:

```text
i_Bs=1
i_res=0
```

That requires a residual nonentry theorem. The filter itself does not prove residual nonentry.

The residual-only route is clean at the incidence level, but it is not a `B_s/F_zeta` insertion route. It cannot be used as a back door for inserting `B_s/F_zeta`.

## Boundary

This is an incidence filter, not a dynamics proof. It does not prove residual nonentry and does not license insertion.

## Steering Consequence

Any insertion route that counts trace twice or misses required trace entry is dead. The only possible `B_s/F_zeta` route must prove residual nonentry.
