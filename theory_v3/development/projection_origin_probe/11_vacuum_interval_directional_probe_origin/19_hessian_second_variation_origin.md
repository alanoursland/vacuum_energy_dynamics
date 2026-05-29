# Vacuum Interval Directional Probe Origin 19: Hessian Second-Variation Origin

## Purpose

This proof gives a conditional origin for metric-quality interval data.

If the local vacuum interval response comes from the second variation of a
scalar local functional, the quadratic branch is the Hessian.

## Validated Checks

- Hessian at the reference state is symmetric and equals the quadratic tensor: passed
- first variation is a separate linear/stationarity channel: passed
- directional second variation equals `v^T H v`: passed
- cubic corrections do not enter the Hessian at the reference state: passed

## Local Functional

Use:

```text
F = f0 + l_i x^i + 1/2 h_ij x^i x^j + cubic terms.
```

At the reference state:

```text
H_ij = d_i d_j F |0 = [[h11,h12],[h12,h22]].
```

Along a direction:

```text
x = lambda v1
y = lambda v2
```

Sympy verifies:

```text
d^2/dlambda^2 F(lambda v)|0 = v^T H v.
```

The first variation is:

```text
d/dlambda F(lambda v)|0 = l1 v1 + l2 v2.
```

## Interpretation

The metric branch is naturally a Hessian/second-variation object. This also
shows what must be controlled: the first variation must vanish or be routed as
a force/source channel, while higher-order terms are not part of the metric
quadratic branch.
