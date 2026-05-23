# candidate_source_trace_sieve — Result Note

## Result

The script reapplies strict source and trace incidence filters.

The source residual is:

```text
S_M*(i_A + i_trans_src - 1)
```

It finds:

```text
source clean transition = 0
source carrying transition = S_M
source repair transition = 0
```

The source-carrying route is correctly rejected. The source-repair route is also rejected even though the incidence residual can vanish, because replacing the A-sector source with a transition response is forbidden by role, not by this residual alone.

The trace residual is:

```text
T_zeta*(i_Bs + i_res + i_trans_trace - 1)
```

It finds:

```text
trace clean transition = 0
trace carrying transition = T_zeta
residual reentry transition = T_zeta
```

## Main Findings

This script preserves the source and trace guardrails.

The transition response cannot:

```text
carry ordinary source load;
repair or replace A-sector source;
add trace payload;
permit residual reentry.
```

The subtle point is the source repair case. Algebraically, if `i_A=0` and `i_trans_src=1`, the residual is zero. But that is still rejected because the transition layer is not allowed to replace the A-sector's ordinary source role. This is a governance/role-purity rejection, not a residual-size rejection.

## Boundary

This is still an incidence filter, not a full source safety theorem.

## Steering Consequence

The surviving candidate must remain ordinary-source neutral and trace-neutral in incidence. Source safety still needs a real theorem.
