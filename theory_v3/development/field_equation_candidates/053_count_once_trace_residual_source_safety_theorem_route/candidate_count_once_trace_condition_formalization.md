# candidate_count_once_trace_condition_formalization — Result Note

## Result

The script formalizes the count-once trace condition as an incidence equation:

```text
i_Bs + i_res = 1
```

using the residual:

```text
T_zeta*(i_Bs + i_res - 1)
```

It classifies four incidence patterns:

```text
B_s route:
  i_Bs=1, i_res=0 -> residual = 0

residual-only route:
  i_Bs=0, i_res=1 -> residual = 0

double-entry route:
  i_Bs=1, i_res=1 -> residual = T_zeta

missing-trace route:
  i_Bs=0, i_res=0 -> residual = -T_zeta
```

## Main Findings

The count-once condition is now cleanly stated. There are two single-entry incidence patterns, but only one of them corresponds to a `B_s/F_zeta` trace-entry route.

The `B_s` route is clean at incidence level only if residual nonentry is proven:

```text
i_Bs=1
i_res=0
```

The residual-only route is also clean at incidence level, but it does not activate the `B_s/F_zeta` route. So it cannot by itself support `B_s/F_zeta` insertion.

The double-entry and missing-entry cases are rejected for physical use. This is useful because it closes two fake escape routes: counting the trace twice, or pretending trace normalization has been satisfied when no trace channel carries it.

## Boundary

This is an incidence formalization, not dynamics. It does not prove residual nonentry. It does not choose a branch. It does not license insertion.

## Steering Consequence

The B_s route remains possible only as a theorem target with a residual nonentry proof. The next test should ask whether residual metric/source incidence can be set to zero without active `O` and without fiat.
