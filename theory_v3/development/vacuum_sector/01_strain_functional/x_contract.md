# X Contract

This document defines the minimum interface a vacuum configuration variable
`X` must provide before a strain functional can be treated as meaningful.

It is a contract, not a choice of final theory.

## Required Questions

Any candidate branch must answer:

```text
What is the vacuum configuration variable X?
```

Possible statuses include:

```text
metric data g_ab
interval-response data Q_p(v)
frame or coframe data
connection or transport data
internal medium data
deeper premetric variable
not yet specified
```

A candidate must also answer:

```text
How does X transform under relabelings?
How does X reduce to g_ab in the metric branch?
What map sends X to the local interval response Q_p(v)?
What map sends X to the metric/Hessian response when the quadratic gate holds?
What is the matter-coupling route?
What boundary data are admissible?
Which variables are physical?
Which variables are gauge?
```

## Metric-Branch Reduction

The metric branch must recover:

```text
Q_p(v) = g_ab(p) v^a v^b
```

at lowest order when the local response is exact quadratic.

If `X` is not simply metric data, the branch must state the reduction map:

```text
X -> Q_p(v) -> g_ab(p).
```

If the reduction is nonquadratic, Finsler-like, frame-dependent, or species
dependent, that fact must be explicitly routed outside the pure metric branch.

## Matter Coupling Route

A candidate branch must state whether matter couples to:

```text
g_ab only;
X directly;
a derived frame/coframe;
an independent connection;
a nonmetric calibration field;
an effective metric plus routed residual fields.
```

If matter couples to anything beyond the shared metric interval, the candidate
must identify the implied observable channel and route it through residual
tests.

## Boundary Data

The branch must state what is fixed on the boundary:

```text
metric or induced metric;
interval response;
frame/coframe;
connection data;
normal derivative data;
nonlocal/global data;
other branch-specific data.
```

Boundary data are not decoration. They determine whether the variational
problem is well posed and whether the branch silently changes the gravitational
sector.

## Contract Status Labels

Use these labels when evaluating a proposed `X`:

```text
complete contract
partial contract
metric-only placeholder
extra-field route required
underdetermined without new axiom
fails accumulated gate
not yet evaluated
```
