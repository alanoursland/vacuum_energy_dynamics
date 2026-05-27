# Matter Source Origin Gate 38: Shared Interval Variation Gate

## Purpose

This proof checks a variable-ownership condition:

```text
matter source variation and vacuum boundary variation must act on the same
interval variable if they are to balance directly.
```

## Validated Checks

- independent variables produce separate variation equations: passed
- shared variable produces direct boundary/source balance: passed
- stationarity sets vacuum boundary coefficient equal to matter interval source: passed
- near A=1 the leading matter boundary coefficient is M/2: passed

## Split Variables

If the vacuum boundary term uses `A_v` while matter proper time uses a
separate `A_m`:

```text
E = F A_v - M sqrt(A_m),
```

then the variations are separate:

```text
dE/dA_v = F
dE/dA_m = -M/(2 sqrt(A_m)).
```

No direct source/boundary balance follows unless another constraint identifies
the variables.

## Shared Variable

If both terms use the same interval component `A`:

```text
E = F A - M sqrt(A),
```

then:

```text
dE/dA = F - M/(2 sqrt(A)).
```

Stationarity gives:

```text
F = M/(2 sqrt(A)).
```

Near `A=1`, the leading matter coefficient is:

```text
F = M/2 + higher-order terms.
```

## Gate Interpretation

The source-origin chain requires the matter interval and the vacuum boundary
interval to be the same variable, or else requires an explicit identification
constraint. Hidden duplicate interval variables do not close the source law.
