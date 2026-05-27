# Vacuum Interval Directional Probe Origin 1: Quadratic Polarization Identity

## Purpose

This proof establishes the minimal algebra needed for directional interval
probes to carry tensor data.

If the local interval response is:

```text
Q(v) = v^T H v
```

then the symmetric bilinear tensor `H` is recovered by polarization.

## Validated Checks

- quadratic interval probe expands correctly: passed
- polarization recovers the symmetric bilinear pairing: passed

## Identity

For:

```text
H = [[h11,h12],[h12,h22]]
u = (u1,u2)
v = (v1,v2)
```

Sympy verifies:

```text
(Q(u+v)-Q(u)-Q(v))/2 = u^T H v.
```

## Interpretation

Directional interval comparisons are not scalar trace data. They are
quadratic-form data. Once the ontology supplies `Q(v)` for enough directions,
the symmetric bilinear object is algebraically determined.
