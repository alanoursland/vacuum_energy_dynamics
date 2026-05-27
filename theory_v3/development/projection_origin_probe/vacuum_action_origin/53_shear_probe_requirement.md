# Vacuum Action Origin 53: Shear Probe Requirement

## Purpose

This proof records a second tensor-boundary guardrail:

```text
isotropic/trace interval changes do not determine shear.
```

## Validated Checks

- trace sees the isotropic component q: passed
- trace is blind to shear parameter s: passed
- directional interval difference recovers shear: passed
- shear can be nonzero while trace sees only q: passed

## Trace Plus Shear Model

Use:

```text
H = q I + [[s,0],[0,-s]].
```

The trace is:

```text
tr H = 2q.
```

It is independent of `s`.

But directional probes see the shear:

```text
Q(e1)-Q(e2) = 2s.
```

## Interpretation

Any derivation of the full nonlinear boundary term must supply shear-sensitive
interval data. A scalar trace admissibility ladder can at most seed the trace
sector.
