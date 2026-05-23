# candidate_blocker_dependency_graph — Result Note

## Result

The script records the dependency graph among remaining parent blockers.

Dependency shape:

```text
parent equation depends on recombination rule;

recombination rule depends on:
  source safety;
  trace safety;
  divergence identity;
  covariant lift;
  boundary neutrality;
  active O decision;
  trace-normalization decision;

source safety depends on:
  source count once;

trace safety depends on:
  trace count once;

divergence identity depends on:
  covariant lift;

boundary neutrality depends on:
  boundary diagnostic ledger.
```

## Main Findings

This gives the project a better route map.

The parent equation is downstream, not next.

The recombination rule is also downstream of several unresolved blockers. It cannot be honestly written until source, trace, divergence, covariance, boundary, active-O, and trace-normalization statuses are controlled.

The source/trace count-once cluster is central:

```text
source safety -> source count once
trace safety -> trace count once
```

The divergence/covariance cluster is also central:

```text
divergence identity -> covariant lift
```

Boundary diagnostics remain useful but not sufficient:

```text
boundary diagnostic ledger -> boundary neutrality
```

Rejected shortcuts:

```text
parent before dependencies;
use diagnostics as dependencies solved.
```

## Boundary

The graph organizes blockers. It does not solve blockers.

## Steering Consequence

Proceed to next-route priority. The dependency graph should determine what Group 67 attacks next.
