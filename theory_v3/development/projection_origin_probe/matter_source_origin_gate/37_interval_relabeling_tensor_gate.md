# Matter Source Origin Gate 37: Interval Relabeling Tensor Gate

## Purpose

This proof connects operational interval uniqueness to tensor behavior under a
local relabeling.

If the same interval is written in two coordinate labels, the metric candidate
must transform as a bilinear tensor.

## Validated Checks

- g_new=J^T g_old J preserves the quadratic interval: passed
- symmetric interval form stays symmetric under relabeling: passed
- identity relabeling leaves metric components unchanged: passed

## Setup

Let:

```text
dx = J du
```

be a local coordinate relabeling. The old interval is:

```text
Q = dx^T g_old dx.
```

Substituting `dx=J du` gives:

```text
Q = du^T (J^T g_old J) du.
```

Therefore the relabeled metric components must be:

```text
g_new = J^T g_old J.
```

## Gate Interpretation

Once the vacuum supplies a unique quadratic interval, interval-preserving
relabeling forces the usual tensor transformation law for the metric candidate.
This is still a kinematic gate, not a derivation of the vacuum action.
