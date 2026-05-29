# Vacuum Action Origin 13: Interval Field Self-Reference Gate

## Purpose

This report tests the next lift:

```text
response field on a metric
  vs.
response field that is the metric.
```

## Validated Checks

- metric perturbation changes interval by h contraction: passed
- interval Hessian recovers metric perturbation: passed
- fixed-background scalar does not change interval: passed
- conformal response rescales background interval: passed
- conformal response has no shear component: passed
- general metric perturbation can carry shear interval response: passed

## Metric Response

For a displacement `d` and background interval:

```text
I_0(d) = d^T eta d,
```

let the response be a metric perturbation `h`.

Then:

```text
I(d) = d^T(eta+h)d
delta I = d^T h d.
```

SymPy verifies that:

```text
(1/2) Hessian_d(delta I) = h.
```

So the metric response is self-referential: the response changes the local
measurement rule itself.

## Scalar on Fixed Background

If `q` is a scalar living on a fixed interval:

```text
I_0(d) = d^T eta d,
```

SymPy verifies:

```text
partial I_0 / partial q = 0.
```

The scalar can have energy, but it does not by itself change the local interval.

## Conformal Limitation

A conformal response:

```text
h_ab = 2 sigma eta_ab
```

only rescales the background interval:

```text
delta I = 2 sigma I_0.
```

It has no shear component. A general metric perturbation can carry:

```text
2 h_01 d0 d1.
```

## Interpretation

The action-origin path to gravity requires the vacuum response variable to
modify the interval itself, not merely live on a fixed interval. A scalar action
is a useful prototype, but the gravitational lift begins when response becomes
metric self-reference.
