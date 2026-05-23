# candidate_count_once_compatibility_sieve — Result Note

## Result

The script identifies the strict role-compatible parent incidence state:

```text
i_A = 1
i_src_extra = 0
i_B = 1
i_res = 0
i_trace_extra = 0
```

It also enumerates count-safe but role-rejected states:

```text
(0,1,0,0,1)
(0,1,0,1,0)
(0,1,1,0,0)
(1,0,0,0,1)
(1,0,0,1,0)
```

## Main Findings

This is one of the main Group 67 results.

It is not enough for incidence sums to equal one. Role purity matters.

The strict state means:

```text
ordinary source enters through A-sector only;
no extra source path;
trace enters through B-sector only;
no residual trace path;
no extra trace path.
```

Rejected routes:

```text
extra source repairing/replacing A;
residual or transition repairing/replacing B trace;
algebra-only count safety without role safety.
```

This prevents a false “count-once” win where the count adds to one only because the wrong object carries the payload.

## Boundary

The strict state is necessary, not sufficient. It clarifies parent-compatible incidence, but it does not prove divergence identity or recombination readiness.

## Steering Consequence

Proceed to residual nonentry. The compatibility sieve shows residual-bearing states are role-rejected; the next script should make residual nonentry explicit.
