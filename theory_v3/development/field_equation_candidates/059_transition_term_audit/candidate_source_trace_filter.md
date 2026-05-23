# candidate_source_trace_filter — Result Note

## Result

The script applies reduced source and trace incidence filters to transition candidates.

The source residual is:

```text
S_M*(i_A+i_layer-1)
```

The safe route is:

```text
i_A=1
i_layer=0
```

The source-carrying route is rejected:

```text
i_A=1
i_layer=1
-> residual = S_M
```

The trace residual is:

```text
T_zeta*(i_Bs+i_layer+i_res-1)
```

The safe route is:

```text
i_Bs=1
i_layer=0
i_res=0
```

Trace double-counting and residual reentry are rejected:

```text
i_Bs=1, i_layer=1, i_res=0 -> T_zeta
i_Bs=1, i_layer=0, i_res=1 -> T_zeta
```

The `layer-only trace` case has zero incidence residual, but it is not the current paired trace-normalization route. It remains informational, not adopted.

## Main Findings

This script prevents a dangerous misuse of the weighted-neutral layer.

A profile with zero weighted scalar charge is not automatically source-clean. A transition response could still duplicate ordinary source load if it carries `i_layer=1` in the source channel.

Likewise, a transition term cannot carry extra trace payload on top of `B_s` without double-counting trace.

The filter therefore preserves two core rules:

```text
ordinary source remains A-sector routed;
trace payload is counted exactly once.
```

## Boundary

This is an incidence filter, not a full source theorem. It does not prove that a surviving transition response is source-neutral in the actual theory.

## Steering Consequence

Proceed to the divergence filter. Candidate transition stress must be reduced-divergence compatible; otherwise it cannot become a serious candidate surface.
