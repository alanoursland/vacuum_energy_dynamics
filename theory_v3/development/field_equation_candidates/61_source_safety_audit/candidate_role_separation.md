# candidate_role_separation — Result Note

## Result

The script reapplies source and trace role-separation diagnostics.

The source residual is:

```text
S_M*(i_A + i_trans_src - 1)
```

The trace residual is:

```text
T_zeta*(i_Bs + i_res + i_trans_trace - 1)
```

The script finds:

```text
source clean = 0
source carrying = S_M
source repair = 0
trace clean = 0
trace carrying = T_zeta
residual reentry = T_zeta
```

## Main Findings

Source carrying remains rejected because `i_A=1, i_trans_src=1` duplicates ordinary source.

Source repair remains rejected because `i_A=0, i_trans_src=1` replaces the A-sector source. The incidence residual can vanish in that case, but the route still fails role-purity.

Trace carrying and residual reentry remain rejected because they add trace or residual payload.

## Boundary

This is only an incidence audit. It is not a full source-safety theorem.

## Steering Consequence

The next check should test a subtler leak: source dependence through the transition stress amplitude.
