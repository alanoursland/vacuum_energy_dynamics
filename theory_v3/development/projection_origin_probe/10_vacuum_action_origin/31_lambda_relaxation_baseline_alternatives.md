# Vacuum Action Origin 31: Lambda Relaxation and Baseline Alternatives

## Purpose

This report separates three Lambda possibilities:

```text
fixed parameter;
relaxed vacuum baseline;
source-shifted baseline.
```

## Validated Checks

- relaxation potential variation: passed
- relaxation sets Lambda to baseline: passed
- zero-baseline relaxation sets Lambda to zero: passed
- source-shifted Lambda variation: passed
- source shifts Lambda baseline: passed
- integrated-out Lambda shift energy: passed
- Lambda potential equation: passed

## Relaxed Baseline

For:

```text
U(lambda) = (kappa/2)(lambda - lambda_0)^2,
```

SymPy verifies:

```text
dU/dlambda = kappa(lambda - lambda_0)
```

and stationarity gives:

```text
lambda = lambda_0.
```

If:

```text
lambda_0 = 0,
```

then relaxation sets:

```text
lambda = 0.
```

## Source-Shifted Baseline

For:

```text
U(lambda) = (kappa/2)lambda^2 - J lambda,
```

SymPy verifies:

```text
lambda = J/kappa.
```

Integrating out the baseline variable gives:

```text
U_reduced = -J^2/(2kappa).
```

## Newtonian Branch

The Lambda potential:

```text
Phi_lambda = -lambda r^2/6
```

satisfies:

```text
Delta Phi_lambda = -lambda.
```

## Interpretation

The proof chain cannot set Lambda by algebra alone. It can only classify the
branches:

```text
Lambda fixed     -> external baseline parameter;
Lambda relaxed   -> value selected by vacuum baseline potential;
Lambda shifted   -> value responds to an additional vacuum source variable.
```

The inverse-square boundary-flux bridge corresponds to the zero-Lambda
asymptotically flat sector.
